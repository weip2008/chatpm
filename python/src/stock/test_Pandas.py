#import pandas_datareader as webreader
from pandas_datareader import data as pdr
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yfin

yfin.pdr_override()
# Set the API 
#data_source = "yahoo"

# Set the API parameters
date_today = "2023-03-20" # period start date
date_start = "2010-01-01" # period end date

symbol = "^GDAXI" # asset symbol - For more symbols check yahoo.finance.com

# Send the request to the yahoo finance api endpoint
#df = webreader.get_data_yahoo(symbol, start="2022-12-01", end="2023-02-08")
#df = pdr.get_data_yahoo("SPY", start="2020-01-01", end="2022-12-31")
df = pdr.get_data_yahoo(symbol, start=date_start, end=date_today)
df.head(5)

# Plot the closing prices
fig, ax1 = plt.subplots(figsize=(12, 8))
plt.plot(df.index, df.Close)
plt.show()

