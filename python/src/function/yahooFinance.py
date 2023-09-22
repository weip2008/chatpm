"""Use Yahoo! Finance to get stock data"""

import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
import pandas as pd

STOCK_SYMBOL = "^GSPC"

def get_daily_stock_data(symbol, start):
    try:
        """Get daily stock data for the given symbol"""
        end = end_date = start + timedelta(days=1)

        # Download the data for the specified date range and interval
        df = yf.download(symbol, start=start, end=end, interval="1m")
        return df
        # return yf.download(symbol, start='2023-08-15', period="1d", interval="1m") # 1 minute interval
    except Exception as error:
        return None

def get_weekly_stock_data(symbol):
    """Get weekly stock data for the given symbol"""
    return yf.download(symbol, period="1wk", interval="1h") # 1 hour interval

def get_monthly_stock_data(symbol):
    """Get monthly stock data for the given symbol"""
    return yf.download(symbol, period="1mo", interval="1d") # 1 day intervaldef get_daily_stock_data(symbol):

def save_data_to_csv(data, filename):
    """Save data to a CSV file"""
    data.to_csv(filename) 
    # Save data to CSV file

def main():
    """Main function"""
    start_date=datetime.strptime('2023-09-01 09:30:00',"%Y-%m-%d %H:%M:%S")
    data = pd.DataFrame()
    for i in range(10):
        data1 = get_daily_stock_data(STOCK_SYMBOL,start_date)
        data = pd.concat([data, data1])
        start_date = start_date + timedelta(1)
        if data.empty:
            continue
        min_data = data["Low"].min()
        min_Low_row = data[data["Low"] == min_data]
        print(min_data, min_Low_row['Low'])
        max_data = data["High"].max()
        max_high_row = data[data["High"] == max_data]
        print(max_data, max_high_row['High'])

    # save_data_to_csv(data, "data/AAPL-1.csv")
    plt.plot(data.index, data['Low'])
    plt.plot(data.index, data['High'])
    # Find the row with the minimum 'Close' value
    # min_close_row = data[data["Close"] == data["Close"].min()]

    # # Extract the 'Date' value from the row
    # min_data = data["Close"].min()
    # print(min_data, min_close_row['Close'])
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    main()