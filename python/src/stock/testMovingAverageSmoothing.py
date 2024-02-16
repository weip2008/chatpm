import numpy as np
import matplotlib.pyplot as plt

# Generate some random data with spikes
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, 100)

# Define a function for moving average smoothing
def moving_average(data, window_size):
    weights = np.repeat(1.0, window_size) / window_size
    smoothed_data = np.convolve(data, weights, 'valid')
    return smoothed_data

# Apply moving average smoothing
window_size = 11  # Adjust this parameter for desired smoothing effect
smoothed_y = moving_average(y, window_size)

# Plot the original and smoothed data
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Original Data')
plt.plot(x[window_size//2:-(window_size//2)], smoothed_y, label='Smoothed Data')
plt.legend()
plt.title('Original vs Smoothed Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
