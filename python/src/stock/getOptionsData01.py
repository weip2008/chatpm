from yahoo_fin import options
# Get call dates for NFLX expiring on 12/31/2023
calls = options.get_calls("LULU", "01/26/2024")
#calls = options.get_calls("NFLX", "1/19/2024")

# Get put dates for NFLX expiring on 12/31/2023
puts = options.get_puts("LULU", "01/26/2024")
#puts = options.get_puts("NFLX", "1/19/2024")

calls.to_csv("python/data/LULU_calls.csv")
puts.to_csv("python/data/LULU_puts.csv")

print(calls)
print("---------------------------------------------------")
print(puts)

