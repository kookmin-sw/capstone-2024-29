import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import os

class VIDataloader(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transform = transform
        self.images = sorted(os.listdir(image_dir))

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        start_idx = idx - 5
        end_idx = idx

        images = []
        masks = []

        for i in range(start_idx, end_idx):
            img_path = os.path.join(self.image_dir, self.images[max(i, 0)])
            mask_path = os.path.join(self.mask_dir, self.images[max(i, 0)].replace("jpg", "png"))
            image = Image.open(img_path).convert("RGB")
            mask = Image.open(mask_path).convert("L")  # gray scale

            if self.transform is not None:
                image = self.transform(image)
                mask = self.transform(mask)

            images.append(image)
            masks.append(mask)

        images = torch.stack(images, dim=0).permute(1,0,2,3)
        masks = torch.stack(masks, dim=0).permute(1,0,2,3)

        return images, masks


def get_dataloader(image_dir, mask_dir, batch_size, transform=None):
    dataset = VIDataloader(image_dir, mask_dir, transform)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    return dataloader
