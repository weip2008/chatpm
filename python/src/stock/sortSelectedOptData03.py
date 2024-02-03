import warnings
from datetime import date, datetime,timedelta
from yahoo_fin import options
from yahoo_fin.stock_info import get_live_price
#import yfinance as yf
import pandas as pd
#import numpy as np

warnings.filterwarnings('ignore')

symbolList = []
#symbolList = ["BUD", "PBR", "TSM", "BABA", "NVO", "PDD", "SHEL", "SHOP", "SONY", "HSBC", "AZN", "ASML"]
#symbolList = ["ASML","BUD"]
dataValue = {}

def read_file_contents(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8-sig') as file:
            contents = file.read()
            file.close
            return contents
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None



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
#print("Next Friday is "+next_friday_string)

now = datetime.now()
currentDatetime = now.strftime("%m%d%Y-%H%M")
print(f"Current date time is " + currentDatetime)

# If it's Friday and after 4PM (16:00), then jump to next Friday
if now.weekday() == 4 and now.time() > datetime.time(datetime(1, 1, 1, 16, 0)):
    next_friday += timedelta(7)
    next_friday_string = next_friday.strftime("%m/%d/%Y")
    print("It's after 4 PM on Friday, so jumping to the following Friday: " + next_friday_string)
#contractDate = "02/02/2024"
contractDate = next_friday_string
print("Contract date:"+contractDate)

blacklist_file = path+"blacklist.txt"
# Read the filename from the blacklist file
file_to_read = read_file_contents(blacklist_file)

if file_to_read:
    # Read the contents of the specified file
    listFileName = path+file_to_read
    with open(listFileName, "r", encoding='utf-8-sig') as f:
        for line in f:
            symbolList.append(line.strip())
    f.close
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
        #k = (c+p)/2.0
        r = (c+p)/2.0/current_price * 1000
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
    f.write("{:<8} {:<8}\n".format('Symbol', 'Value'))
    f.write("-" * 20 + "\n")

    for item in sorted_dataValue:
        f.write("{:<8} {:.8f}\n".format(item[0], item[1]))
f.close()
