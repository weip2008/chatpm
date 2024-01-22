import yahoo_fin.options as ops
import pandas as pd

# get the expiration dates for ^GSPC options
stock_symbol = 'AAPL'
#stock_symbol = '^GSPC'

exp_dates = ops.get_expiration_dates(stock_symbol)
print("Expiration date:\n",exp_dates)


# print the expiration dates
print("\n".join(exp_dates))

print("=============================================================")
# find the date that matches 2023/9/30 using a try-except block
try:
    target_date = [date for date in exp_dates if date.endswith("2024") and date.startswith("January 26")][0]
    # get the options chain for ^GSPC with the target date
    print("Target date:\n", target_date)
    chain = ops.get_options_chain(stock_symbol, target_date)
    
    print("=============================================================")
    # get the call options dataframe
    calls = chain["calls"]
    print("Call options dataframe:\n", calls)
    
    print("=============================================================")
    # find the row that matches the strike price of 180
    call_option = calls[calls["Strike"] == 180]
    # print the call option data
    print("Call options data:\n", call_option)
except IndexError:
    print("No date found that matches 2024/1/26")
