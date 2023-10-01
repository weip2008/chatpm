from yahoo_fin import stock_info as si

stock_price = si.get_live_price("AAPL")  # Replace "AAPL" with the stock symbol you want to fetch
print(f"Current Price of AAPL: ${stock_price:.2f}")

import datetime

start_date = datetime.datetime(2020, 1, 1)
end_date = datetime.datetime(2021, 12, 31)

historical_data = si.get_data("AAPL", start_date, end_date)
print(historical_data)

# pe_ratio = si.get_quote_table("AAPL")["PE Ratio (TTM)"]
# print(f"P/E Ratio for AAPL: {pe_ratio}")

# Get the P/E ratio
quote_data = si.get_quote_table("AAPL")
if "PE Ratio (TTM)" in quote_data:
    pe_ratio = quote_data["PE Ratio (TTM)"]
    print(f"P/E Ratio for AAPL: {pe_ratio}")
else:
    print("P/E Ratio data not found for AAPL.")