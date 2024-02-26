import datetime as dt
import yfinance as yf
from stocktrends import Renko
import matplotlib.pyplot as plt
import numpy as np

# Function to convert ohlc data into renko bricks. Pass dataframe name and brick size
def df_to_renko(data, n):
    data.reset_index(inplace=True)
    data.columns = [i.lower() for i in data.columns]
    print(data.isnull().values.any())
    df = Renko(data)
    df.brick_size = n
    renko_df = df.get_ohlc_data()
    return renko_df

# Input ticker here
ticker_name="^GSPC" 

# Define the start and end dates for the data retrieval
start_date = dt.datetime(2018, 1, 1)
end_date = dt.datetime(2024, 1, 1)
ohlc = yf.download(ticker_name, start_date, end_date)

r_bars = df_to_renko(ohlc, 50)

plt.figure(figsize=(18, 9))

# Plot OHLC data
plt.subplot(2, 1, 1)
ohlc['close'].plot()
# Derive the date format dynamically from the 'Date' column
date_format = '%Y-%m'  # Default format
if len(ohlc) > 0:
    date_format = ohlc['date'].iloc[0].strftime('%Y-%m-%d')  # Use the format of the first date in the index
# Set the format of x-axis labels to include year and month
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter(date_format))
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

''' plt.plot(ohlc['date'], ohlc['close'], label='Close', color='blue')
plt.title('S&P 500 (^GSPC) - Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.gca().set_xticklabels(ohlc['date'].dt.strftime('%Y-%m-%d'))  # Set x-axis tick labels to dates
 '''
# Plot Renko bars
plt.subplot(2, 1, 2)
plt.bar(r_bars.index, r_bars['close'] - r_bars['open'], bottom=r_bars['open'], width=0.5, color=np.where(r_bars['close'] >= r_bars['open'], 'g', 'r'))
plt.title('Renko Bars')

# Adjust layout
#plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
