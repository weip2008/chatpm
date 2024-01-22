from yahoo_fin import stock_info as si
import pandas as pd
import matplotlib.pyplot as plt

# Specify the option symbol for /MES
option_symbol = '^GSPC'

# Get historical data for the option
historical_data = si.get_data(option_symbol, start_date='07/01/2023', end_date='09/21/2023')

# Check if data is available for the option
if not historical_data.empty:
    # Print out high and low price for each day
    for index, row in historical_data.iterrows():
        formatted_high = "${:.3f}".format(row['high'])
        formatted_low = "${:.3f}".format(row['low'])
        print(f"Date: {index.date()}, High: {formatted_high}, Low: {formatted_low}")

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(historical_data)

    # Display summary statistics
    print(df.describe())

    # Plot the 'close' price
    df['close'].plot()
    plt.show()
else:
    print(f"No historical data available for {option_symbol}")
