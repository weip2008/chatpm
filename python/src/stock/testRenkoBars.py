import datetime as dt
import yfinance as yf
from stocktrends import Renko
import matplotlib.pyplot as plt
import matplotlib
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

#Input ticker here
ticker_name="^GSPC" 
#ticker_name = "AAPL"
#ticker_name = "F"

# Define the start and end dates for the data retrieval
start_date = dt.datetime(2022, 1, 1)
end_date = dt.datetime(2024, 1, 1)
#start_date = dt.datetime.today()- dt.timedelta(1825) # getting data of around 5 years.
#end_date = dt.datetime.today()
ohlc = yf.download(ticker_name, start_date, end_date)

# Display the first few rows of the data
print(ohlc.head())
print("--------------")
print(ohlc.tail())
print("# of rows in ohlc:",len(ohlc))

r_bars = df_to_renko(ohlc, 20)
print('# of rows in DF(Renko):',len(r_bars))

# r_bars.to_excel("output.xlsx", index=False)

new_df = r_bars[['open','close']]

plt.rcParams["figure.figsize"] = (18,9)

# create the figure
fig = plt.figure(1)
fig.clf()
axes = fig.gca()

# Add 10 extra spaces to the right
#num_bars = 200
num_bars = len(new_df)
df = new_df.tail(num_bars)

renkos = zip(df['open'],df['close'])
# plot the bars, green for 'up', red for 'down'
index = 1

for open_price, close_price in renkos:
    if (open_price < close_price):
        renko = matplotlib.patches.Rectangle((index,open_price), 1, close_price-open_price, 
                                             edgecolor='black', facecolor='green', alpha=0.5)
        axes.add_patch(renko)
    else:
        renko = matplotlib.patches.Rectangle((index,open_price), 1, close_price-open_price, 
                                             edgecolor='black', facecolor='red', alpha=0.5)
        axes.add_patch(renko)
    index = index + 1

""" x = np.arange(0,100, 1)
y= ohlc.loc[1:1257]['close']
plt.plot(x,y)    """ 
#adjust the axes
plt.xlim([0, num_bars+5])
plt.ylim([min(min(df['open']),min(df['close'])), max(max(df['open']),max(df['close']))])
plt.grid(True)
plt.show()

