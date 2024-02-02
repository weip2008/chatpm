import warnings
from datetime import date, datetime,timedelta
from yahoo_fin import options
from yahoo_fin.stock_info import get_live_price
#import yfinance as yf
import pandas as pd
import numpy as np

warnings.filterwarnings('ignore')

symbolList = []
#symbolList = ["BUD", "PBR", "TSM", "BABA", "NVO", "PDD", "SHEL", "SHOP", "SONY", "HSBC", "AZN", "ASML"]
#symbolList = ["ASML","BUD"]
dataValue = {}


def get_calls_and_puts(symbol: str, date: str) -> tuple:
    calls = options.get_calls(symbol, date)
    puts = options.get_puts(symbol, date)

    # Replace '-' with 0
    calls = calls.replace("-", 0)
    puts = puts.replace("-", 0)
    
    # Extract the desired columns
    new_calls = calls[["Contract Name", "Strike", "Last Price", "Bid", "Ask", "Volume"]]
    new_puts = puts[["Contract Name", "Strike", "Last Price", "Bid", "Ask", "Volume"]]

    return new_calls, new_puts

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

def calculateCall(df, given_price):
    # Get the the last row with strike price higher than the given price
    higher_rows = df[df["Strike"] >= given_price].head(1)
    index = higher_rows.index[0]
    bid = higher_rows.at[index, "Bid"]
    ask = higher_rows.at[index, "Ask"]
    cp = (bid + ask) / 2.0
    c = cp/given_price
    return c

def calculatePut(df, given_price):
    # Get the last row with strike price lower than the given price
    lower_rows = df[df["Strike"] <= given_price].tail(1)
    index = lower_rows.index[0]
    bid = lower_rows.at[index, "Bid"]
    ask = lower_rows.at[index, "Ask"]
    pp = (bid + ask) / 2.0
    p = pp/given_price
    return p

    
#path = "python/data/"
path = "d:/chatpm/python/data/"
today = date.today()
print(f"Today's date is {today.strftime('%m-%d-%Y')}")
next_friday = today + timedelta((4 - today.weekday()) % 7)
next_friday_string = next_friday.strftime("%m/%d/%Y")
print("Next Friday is "+next_friday_string)
#contractDate = "02/02/2024"
contractDate = next_friday_string

now = datetime.now()
currentDatetime = now.strftime("%m%d%Y-%H%M")
print(f"Current date time is " + currentDatetime)

fileName = path+"blacklist.txt"
with open(fileName, "r", encoding='utf-8-sig') as f:
    for line in f:
        symbolList.append(line.strip())

print(f"Symbol list: {symbolList}")

for symbol in symbolList:
    print("\n================================================================\n")
    print("\nSymbol:"+symbol)
    
    current_price = get_live_price(symbol)
    print(f"Current price for {symbol} is ${current_price:.2f}")
    
    try:    
        # Get calls and puts for given stock at contract date
        calls, puts = get_calls_and_puts(symbol, contractDate)

        """ print("\n========================= CALLS ===============================")
        print(calls)
        print("\n========================== PUTS ===============================")
        print(puts) """
    
        filtered_calls = filter_rows_by_price(calls, current_price)
        filtered_puts = filter_rows_by_price(puts, current_price)

        print(f"\n================== Filtered CALLS for ${current_price:.2f}====================" )
        print(filtered_calls)
        print(f"\n================== Filtered PUTS for ${current_price:.2f}=====================")
        print(filtered_puts)
        
        c = calculateCall(filtered_calls, current_price)
        p = calculatePut(filtered_puts, current_price)
        k = (c+p)/2.0
        r = k/current_price
        dataValue[symbol] = r
        
    except ValueError:
        #code that handle the exception
        print("No tables found!")
        dataValue[symbol] = 0.0    
# end of symbol list loop

""" print("\n=================== Data value pair =======================")   
print(dataValue)   """  

sorted_dataValue = sorted(dataValue.items(), key=lambda x:x[1], reverse=True )
#print(sorted_dataValue)

print("\n=================== Sorted Result =======================")  
print("{:<10} {:<10}".format('Symbol', 'Value'))
print("-" * 20)
for item in sorted_dataValue:
    print("{:<10} {:.8f}".format(item[0], item[1]))

fileName = path+"Options_sorted_"+currentDatetime+".txt"
with open(fileName, 'w') as f:
    f.write("{:<10} {:<10}\n".format('Symbol', 'Value'))
    f.write("-" * 20 + "\n")

    for item in sorted_dataValue:
        f.write("{:<10} {:.8f}\n".format(item[0], item[1]))
f.close()
