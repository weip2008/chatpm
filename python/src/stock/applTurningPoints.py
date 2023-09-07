import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

def smooth(y, window):
    # Smooth the curve with a rolling window of 5 points
    y_smoothed = pd.Series(y).rolling(window=window, center=True).mean()
    return y_smoothed

# Define a function to compute the slope of a curve
def slope(x, y):
    dx = np.gradient(x)
    dy = np.gradient(y)
    return dy / dx

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('data/AAPL20150101-20200611.csv')

y = df['Adj Close']

window = 15
epsilon = 0.01

y_smoothed = smooth(y, window)

date = pd.to_datetime(df['Date'])
# x = datetime.datetime.strptime(x, '%Y-%m-%d').date().toordinal()
x = date.map(lambda a: a.toordinal())
# print(x)
# Print the DataFrame
# print(df)
m = np.array(slope(x, y_smoothed))

# Find the indices of points where the slope is zero
zero_slope_indices = np.where(np.abs(m) <= epsilon)[0]

plt.plot(date,y, 'r-', label='Origional data')
plt.plot(date, y_smoothed, label='Smoothed data')
plt.plot(date[zero_slope_indices], y[zero_slope_indices], 'y^', label='Turning Points')
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Adj Close')
plt.legend()
plt.title(f'Smooth window={window}, epsilon={epsilon}')
plt.show()