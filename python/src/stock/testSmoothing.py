import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Generate some random data with spikes
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, 100)

# Apply smoothing using Savitzky-Golay filter
smoothed_y = savgol_filter(y, window_length=5, polyorder=3)

# Plot the original and smoothed data
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Original Data')
plt.plot(x, smoothed_y, label='Smoothed Data')
plt.legend()
plt.title('Original vs Smoothed Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
