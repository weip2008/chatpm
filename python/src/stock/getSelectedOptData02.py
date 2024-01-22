import warnings

from yahoo_fin import options
from yahoo_fin.stock_info import get_live_price
#import yfinance as yf
import pandas as pd

warnings.filterwarnings('ignore')

def get_calls_and_puts(symbol: str, date: str) -> tuple:
    calls = options.get_calls(symbol, date)
    puts = options.get_puts(symbol, date)

    # Extract the desired columns
    #new_calls = calls.loc[:, ["Contract Name", "Strike", "Last Price", "Bid", "Ask"]]
    #new_puts = puts.loc[:, ["Contract Name", "Strike", "Last Price", "Bid", "Ask"]]
    
    # Extract the desired columns
    new_calls = calls[["Contract Name", "Strike", "Last Price", "Bid", "Ask"]]
    new_puts = puts[["Contract Name", "Strike", "Last Price", "Bid", "Ask"]]

    return new_calls, new_puts


def add_sign_column(df, currentPrice):
    # create a new column "Sign" and calculate its value
    df["Sign"] = (df["Bid"] + df["Ask"]) / 2.0 / currentPrice
    # return the updated DataFrame
    return df


symbol = "LULU"
date = "01/26/2024"

calls, puts = get_calls_and_puts(symbol, date)

calls.to_csv("python/data/LULU_calls_selected.csv")
puts.to_csv("python/data/LULU_puts_selected.csv")

print("\n========================= CALLS ===============================")
print(calls)
print("\n========================== PUTS ===============================")
print(puts)

print("\n========================================================\n")
current_price = get_live_price(symbol)
print(f"The current price of {symbol} is ${current_price:.2f}")

# data = yf.download(symbol, period="1d")
# current_price = data["Close"][0]
# print(f"The current price of {symbol} is ${current_price:.2f}")

calculated_calls = add_sign_column(calls, current_price)
calculated_puts = add_sign_column(puts, current_price)
#sorted_calculated_calls = calculated_calls.sort_values(by="Sign")
print("\n========================= Calculated CALLS ===============================")
print(calculated_calls)
print("\n========================= Calculated PUTS ===============================")
print(calculated_puts)

calls.to_csv("python/data/LULU_calls_calculated.csv")
puts.to_csv("python/data/LULU_puts_calculated.csv")