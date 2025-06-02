from torch.utils.data import random_split
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
import torch.nn as nn
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])

dataset = datasets.ImageFolder(root="images", transform=transform)
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size

train_dataset, val_dataset = random_split(
    dataset, [train_size, val_size], generator=torch.Generator().manual_seed(42)
)

train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=16, shuffle=False)

model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, len(dataset.classes))
state_dict = torch.load("model.pth", map_location=device, weights_only=True)
model.load_state_dict(state_dict)
model = model.to(device)
model.eval()

correct = 0
total = 0

with torch.no_grad():
    for imgs, labels in val_loader:
        imgs, labels = imgs.to(device), labels.to(device)
        outputs = model(imgs)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        print("Predicted:", predicted.cpu().numpy())
        print("Actual:", labels.cpu().numpy())

accuracy = 100 * correct / total
print(f" Validation Accuracy: {accuracy:.2f}%")
print("Validation set size:", len(val_dataset))
