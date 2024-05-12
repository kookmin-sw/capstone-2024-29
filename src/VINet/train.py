import torch
from torch.autograd import Variable
from tqdm import tqdm

def repackage_hidden(h):
    # Wraps hidden states in new Variables, detach them from their history
    if isinstance(h, torch.Tensor):
        return h.detach()
    else:
        return tuple(repackage_hidden(v) for v in h)


def to_var(x, volatile=False):
    if torch.cuda.is_available():
        x = x.cuda()
    return Variable(x, volatile=volatile)
    

def train(epochs, dataloader, model, criterion_L1, criterion_ssim, optimizer, opt):
    opt.w_ST, opt.w_LT, opt.w_Flow = 0.0, 0.0, 0.0
    model.train()
    ts = opt.t_stride

    # epoch
    for epoch in range(epochs):
        total_loss = 0.0
        for images, masks in tqdm(dataloader, total=len(dataloader), desc=f"Epoch {epoch+1}/{epochs}"):  # tqdm으로 감싸고 전체 반복 횟수 제공
            images = torch.tensor(images)
            masks = torch.tensor(masks)
            images = 2. * images - 1. # [-1, 1]
            inverse_masks = 1. - masks
            masked_images = images.clone() * inverse_masks

            frame_i, frame_mi, frame_m = [], [], []

            frame_i.append(to_var(images[:,:,:,:,:]))
            frame_mi.append(to_var(masked_images[:,:,:,:,:]))
            frame_m.append(to_var(masks[:,:,:,:,:]))

            optimizer.zero_grad()
            lstm_state = None
            ST_loss, LT_loss = 0, 0
            RECON_loss, HOLE_loss = 0, 0
            flow_loss = 0

            # forward
            prev_mask = frame_m[0][:,:,3,:,:]
            prev_ones = to_var(torch.ones(prev_mask.size()))
            prev_feed = torch.cat([frame_mi[0][:,:,4,:,:], prev_ones, prev_ones*prev_mask], dim=1)

            frame_o1, _, lstm_state, _, occs = model(frame_mi[0], frame_m[0], lstm_state, prev_feed)
            lstm_state = None if opt.no_lstm else repackage_hidden(lstm_state)
            frame_o1 = frame_o1.squeeze(2) # time 차원 압축

            RECON_loss += 1*criterion_L1(frame_o1, frame_i[0][:,:,4,:,:]) - criterion_ssim(frame_o1, frame_i[0][:,:,4,:,:])
            HOLE_loss += 5*criterion_L1(
                frame_o1*frame_m[0][:,:,4,:,:].expand_as(frame_o1), 
                frame_i[0][:,:,4,:,:]*frame_m[0][:,:,4,:,:].expand_as(frame_o1)
                )

            frame_o = []
            frame_o.append(frame_o1)

            overall_loss = (RECON_loss + HOLE_loss + opt.w_ST * ST_loss + opt.w_LT * LT_loss + opt.w_Flow * flow_loss)

            overall_loss.backward()
            optimizer.step()

            total_loss += overall_loss.item()

        avg_loss = total_loss / len(dataloader)
        print(f"Epoch [{epoch+1}/{epochs}], Average Loss: {avg_loss:.4f}")

    return avg_loss