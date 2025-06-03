import cv2
from PIL import Image
import torch
from torchvision import transforms, models
import torch.nn as nn
import os

model_path = "model.pth"
class_names = ["chill", "focus", "party", "romantic", "energetic"]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define Transform
transform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])

# Load Model
model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, len(class_names))
model.load_state_dict(torch.load(model_path, map_location=device, weights_only=True))
model.to(device)
model.eval()

# Capture image from webcam using OpenCV
cap = cv2.VideoCapture(0)
print("Press SPACE to capture an image.")
while True:
    ret, frame = cap.read()
    cv2.imshow("Capture Mood Image", frame)
    if cv2.waitKey(1) & 0xFF == ord(" "):  # Press SPACE to capture
        img_path = "captured_image.jpg"
        cv2.imwrite(img_path, frame)
        break
cap.release()
cv2.destroyAllWindows()

# Preprocess and predict
image = Image.open(img_path).convert("RGB")
input_tensor = transform(image).unsqueeze(0).to(device)

with torch.no_grad():
    output = model(input_tensor)
    predict_idx = torch.argmax(output, 1).item()
    predicted_mood = class_names[predict_idx]

# Display result
print("Predicted mood:", predicted_mood)
