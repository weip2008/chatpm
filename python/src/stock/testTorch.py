import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for demonstration purposes
def generate_data(num_samples):
    images = []
    labels = []

    for _ in range(num_samples):
        # Generate a random "W" shape image (simplified for demonstration)
        img = np.zeros((28, 28))  # Assuming image size of 28x28 pixels
        x_center = np.random.randint(5, 23)  # Random x-coordinate for the center of the "W"
        y_center = np.random.randint(5, 23)  # Random y-coordinate for the center of the "W"
        img[x_center, y_center-2:y_center+3] = 1  # Top of the "W"
        img[x_center+1, y_center-1:y_center+2] = 1  # Middle of the "W"
        img[x_center+2, y_center-2:y_center+3] = 1  # Bottom of the "W"

        images.append(img)
        labels.append(1)  # "W" shape label

    return np.array(images), np.array(labels)

# Generate synthetic training data
X_train, y_train = generate_data(1000)

# Preprocess the data
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

X_train = torch.Tensor(X_train).unsqueeze(1) / 255.0  # Add channel dimension and normalize pixel values
y_train = torch.LongTensor(y_train)

# Create dataset and dataloader
dataset = TensorDataset(X_train, y_train)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Define the CNN model
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.fc1 = nn.Linear(64 * 5 * 5, 128)
        self.fc2 = nn.Linear(128, 2)  # Output layer with 2 classes: "W" shape or not

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 64 * 5 * 5)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Initialize the model, loss function, and optimizer
model = CNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
num_epochs = 10
for epoch in range(num_epochs):
    running_loss = 0.0
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * inputs.size(0)
    epoch_loss = running_loss / len(dataset)
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}')

# Save the trained model for future use
torch.save(model.state_dict(), 'w_shape_recognition_model.pth')

# Plot some example images (optional)
plt.figure(figsize=(10, 5))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(X_train[i].squeeze(), cmap='gray')
    plt.title('W' if y_train[i] == 1 else 'Not W')
    plt.axis('off')
plt.show()
