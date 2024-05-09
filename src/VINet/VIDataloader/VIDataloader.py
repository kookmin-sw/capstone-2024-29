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
        self.images = os.listdir(image_dir)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = os.path.join(self.image_dir, self.images[idx])
        mask_path = os.path.join(self.mask_dir, self.images[idx].replace("jpg", "png"))
        image = Image.open(img_path).convert("RGB")
        mask = Image.open(mask_path).convert("L")  # gray scale

        if self.transform is not None:
            image = self.transform(image)
            mask = self.transform(mask)

        return image, mask


def get_dataloader(image_dir, mask_dir, batch_size, transform=None):
    dataset = VIDataloader(image_dir, mask_dir, transform)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    return dataloader
