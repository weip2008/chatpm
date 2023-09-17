# Import yfinance module
import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'TSLA'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

# See the first 5 rows of the data frame
print(tickerDf)
print(tickerDf.columns)