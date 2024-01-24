import warnings
from datetime import date, datetime
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
    new_calls = calls[["Contract Name", "Strike", "Last Price", "Bid", "Ask", "Volume"]]
    new_puts = puts[["Contract Name", "Strike", "Last Price", "Bid", "Ask", "Volume"]]

    return new_calls, new_puts


""" def add_sign_column(df, currentPrice):
    # create a new column "Sign" and calculate its value
    df["Sign"] = (df["Bid"] + df["Ask"]) / 2.0 / currentPrice
    # return the updated DataFrame
    return df """


def add_sign_column(df):
    # create a new column "Sign" and calculate its value
    df["Sign"] = (df["Bid"] + df["Ask"]) / 2.0 / df["Strike"]
    # return the updated DataFrame
    return df

def filter_rows_by_price(df, given_price):
    # Get the 5 rows with strike price lower than the given price
    lower_rows = df[df["Strike"] < given_price].tail(5)

    # Get the 5 rows with strike price higher than the given price
    higher_rows = df[df["Strike"] > given_price].head(5)

    # Combine the two DataFrames
    result = pd.concat([lower_rows, higher_rows])
    
    # Reset the index and regenerate row number in the first column
    result = result.reset_index(drop=True)
    #result.index += 1

    return result

def filter_rows_by_name(df, given_price):

    # Extract the price from the Contract Name column
    df["Price"] = df["Contract Name"].str[-8:].astype(float) / 1000.0
    # Set the contract name column as the index
    #df = df.set_index("Price")
    
    # Get the 5 rows with strike price lower than the given price
    lower_rows = df[df.index < given_price].tail(5)

    # Get the 5 rows with strike price higher than the given price
    higher_rows = df[df.index > given_price].head(5)

    # Combine the two DataFrames
    result = pd.concat([lower_rows, higher_rows])
    
    # Remove the Price column
    result = result.drop(columns=["Price"])
    
    return result

symbol = "LULU"
contractDate = "01/26/2024"
path = "python/data/"
today = date.today()
print(f"Today's date is {today.strftime('%m-%d-%Y')}")
now = datetime.now()
currentDatetime = now.strftime("%m%d%Y-%H%M")
print(f"Current date time is " + currentDatetime)

# Get calls and puts for given stock at contract date
calls, puts = get_calls_and_puts(symbol, contractDate)

fileName = path+symbol+"_call_selected_"+today.strftime('%m-%d-%Y')+".csv"
print("File name:"+fileName)
calls.to_csv(fileName)
fileName = path+symbol+"_put_selected_"+today.strftime('%m-%d-%Y')+".csv"
puts.to_csv(fileName)

print("\n========================= CALLS ===============================")
print(calls)
print("\n========================== PUTS ===============================")
print(puts)

calculated_calls = add_sign_column(calls)
calculated_puts = add_sign_column(puts)

print("\n========================= Calculated CALLS ===============================")
print(calculated_calls)
print("\n========================= Calculated PUTS ===============================")
print(calculated_puts)

fileName = path+symbol+"_calls_calculated_"+today.strftime('%m-%d-%Y')+".csv"
calculated_calls.to_csv(fileName)
fileName = path+symbol+"_puts_calculated_"+today.strftime('%m-%d-%Y')+".csv"
calculated_puts.to_csv(fileName)

print("\n========================================================\n")
current_price = get_live_price(symbol)
print(f"The current price of {symbol} is ${current_price:.2f}")

filtered_calls = filter_rows_by_price(calculated_calls, current_price)
filtered_puts = filter_rows_by_price(calculated_puts, current_price)

print(f"\n======================= Filtered CALLS for ${current_price}===========================" )
print(filtered_calls)
print(f"\n======================= Filtered PUTS for ${current_price}============================")
print(filtered_puts)

#fileName = path+symbol+"_calls_filtered_"+today.strftime('%m-%d-%Y')+".csv"
fileName = path+symbol+"_calls_filtered_"+currentDatetime+".csv"
filtered_calls.to_csv(fileName)
#fileName = path+symbol+"_puts_filtered_"+today.strftime('%m-%d-%Y')+".csv"
fileName = path+symbol+"_puts_filtered_"+currentDatetime+".csv"
filtered_puts.to_csv(fileName)
