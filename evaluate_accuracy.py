from torch.utils.data import random_split
from torchvision import datasets, transforms


dataset = datasets.ImageFolder(root="images", transform=transform)
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
