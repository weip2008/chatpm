import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

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
X_train = X_train.reshape(-1, 28, 28, 1)  # Reshape for CNN input
X_train = X_train.astype('float32') / 255.0  # Normalize pixel values to [0, 1]
y_train = to_categorical(y_train, num_classes=2)  # One-hot encode the labels

# Define the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(2, activation='softmax')  # Output layer with 2 classes: "W" shape or not
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Save the trained model for future use in the native Keras format
model.save('w_shape_recognition_model.keras')

# Plot some example images (optional)
plt.figure(figsize=(10, 5))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(X_train[i].reshape(28, 28), cmap='gray')
    plt.title('W' if np.argmax(y_train[i]) == 1 else 'Not W')
    plt.axis('off')
plt.show()
