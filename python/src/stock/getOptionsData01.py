from yahoo_fin import options

symbol = "LULU"
date = "02/02/2024"

calls = options.get_calls(symbol, date)
puts = options.get_puts(symbol, date)

# Extract the desired columns
new_calls = calls[["Contract Name", "Strike", "Last Price", "Bid", "Ask"]]
new_puts = puts[["Contract Name", "Strike", "Last Price", "Bid", "Ask"]]

calls.to_csv("python/data/LULU_calls.csv")
puts.to_csv("python/data/LULU_puts.csv")

print(calls)
print("\n---------------------------------------------------\n")
print(puts)

print("\n========================================================\n")


print(new_calls)
print("\n---------------------------------------------------\n")
print(new_puts)