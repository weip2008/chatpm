from yahoo_fin import options
import pandas as pd

def get_calls_and_puts(symbol: str, date: str) -> tuple:
    calls = options.get_calls(symbol, date)
    puts = options.get_puts(symbol, date)

    # Extract the desired columns
    new_calls = calls.loc[:, ["Contract Name", "Strike", "Last Price", "Bid", "Ask"]]
    new_puts = puts.loc[:, ["Contract Name", "Strike", "Last Price", "Bid", "Ask"]]
    
    # Extract the desired columns
    #new_calls = calls[["Contract Name", "Strike", "Last Price", "Bid", "Ask"]]
    #new_puts = puts[["Contract Name", "Strike", "Last Price", "Bid", "Ask"]]

    return new_calls, new_puts

symbol = "LULU"
date = "01/26/2024"

calls, puts = get_calls_and_puts(symbol, date)

calls.to_csv("python/data/LULU_calls_selected.csv")
puts.to_csv("python/data/LULU_puts_selected.csv")

print(calls)
print("\n========================================================\n")
print(puts)


