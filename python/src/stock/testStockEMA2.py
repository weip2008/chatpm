import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Fetch historical data for Apple (AAPL) from Yahoo Finance
#ticker = 'AAPL'
ticker = 'MSFT'
data = yf.download(ticker, start='2021-01-01', end='2022-01-01')

# Extract adjusted closing prices
adj_close_prices = data['Adj Close']

# Define a function for exponential moving average smoothing with triangular weighting
def exponential_moving_average(data, window_size):
    weights = np.arange(1, window_size + 1) / (window_size * (window_size + 1) / 2)
    ema = [] # Initialize the exponential moving average
    for i in range(len(data)):
        weight_sum = np.sum(weights[:min(i+1, window_size)])
        if i >= window_size - 1:
            alpha = np.sum(weights * data.iloc[i - window_size + 1:i+1]) / weight_sum
        else:
            alpha = np.sum(weights[:i+1] * data.iloc[:i+1]) / weight_sum
        ema.append(alpha)
    return np.array(ema)

# Apply exponential moving average smoothing
window_size = 11  # Adjust this parameter for desired smoothing effect
smoothed_adj_close_prices = exponential_moving_average(adj_close_prices, window_size)

# Adjust the length of the smoothed data to match the original data
#smoothed_adj_close_prices = smoothed_adj_close_prices[window_size-1:]
smoothed_adj_close_prices = smoothed_adj_close_prices[window_size-5:]

# Plot the original and smoothed data
plt.figure(figsize=(12, 6))
plt.plot(adj_close_prices.index, adj_close_prices, 
         label='Original Adjusted Close Price', color='blue')
plt.plot(adj_close_prices.index[:len(smoothed_adj_close_prices)], smoothed_adj_close_prices, 
         label='Smoothed Adjusted Close Price', color='red')
plt.title('AAPL Adjusted Close Price with Exponential Moving Average Smoothing (Triangular Weighting)')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.grid(True)
plt.show()
