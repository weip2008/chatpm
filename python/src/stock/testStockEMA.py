import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Fetch historical data for Apple (AAPL) from Yahoo Finance
#ticker = 'AAPL'\
ticker = 'F'
data = yf.download(ticker, start='2021-01-01', end='2024-01-01')

# Extract adjusted closing prices
adj_close_prices = data['Adj Close']

# Define a function for exponential moving average smoothing
def exponential_moving_average(data, alpha):
    ema = [data.iloc[0]] # Initialize the exponential moving average
    for i in range(1, len(data)):
        ema.append(alpha * data.iloc[i] + (1 - alpha) * ema[i-1])
    return np.array(ema)

# Apply exponential moving average smoothing
window_size = 10  # Adjust this parameter for desired smoothing effect
alpha = 2 / (window_size + 1)
smoothed_adj_close_prices = exponential_moving_average(adj_close_prices, alpha)

# Plot the original and smoothed data
plt.figure(figsize=(12, 6))
plt.plot(adj_close_prices.index, adj_close_prices, label='Original Adjusted Close Price', color='blue')
plt.plot(adj_close_prices.index, smoothed_adj_close_prices, label='Smoothed Adjusted Close Price', color='red')
plt.title(ticker + ' Adjusted Close Price with Exponential Moving Average Smoothing')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.grid(True)
plt.show()
