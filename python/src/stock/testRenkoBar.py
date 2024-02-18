import datetime as dt
import yfinance as yf
import pandas as pd
import mplfinance as fplt

start_date = dt.datetime.today()- dt.timedelta(1825) # getting data of around 5 years.
end_date = dt.datetime.today()
ticker_name = "AAPL"
#ticker_name = "F"
ohlcv = yf.download(ticker_name, start_date, end_date)

# Function to calculate average true range
def ATR(DF, n):
  df = DF.copy() # making copy of the original dataframe
  df['H-L'] = abs(df['High'] - df['Low']) 
  df['H-PC'] = abs(df['High'] - df['Adj Close'].shift(1))# high -previous close
  df['L-PC'] = abs(df['Low'] - df['Adj Close'].shift(1)) #low - previous close
  df['TR'] = df[['H-L','H-PC','L-PC']].max(axis =1, skipna = False) # True range
  df['ATR'] = df['TR'].rolling(n).mean() # average –true range
  df = df.drop(['H-L','H-PC','L-PC'], axis =1) # dropping the unneccesary columns
  df.dropna(inplace = True) # droping null items
  return df

#print(ATR(ohlcv, 50))

bricks = round(ATR(ohlcv,50)["ATR"][-1],0) #capturing the latest ATR
#rounding off the result to an integer.
print(bricks)

fplt.plot(ohlcv,type='renko',renko_params=dict(brick_size=bricks, atr_length=14),
          style='yahoo',figsize =(18,7),
          title = "RENKO CHART WITH ATR{0}".format('ticker_name'))


