from yahoo_fin import stock_info as si
import pandas as pd
import matplotlib.pyplot as plt

def find_w_pattern(data):
    """
    Function to identify "W" pattern in historical data.
    Returns a list of indices where the pattern is found.
    """
    w_pattern_indices = []
    for i in range(1, len(data) - 1): 
    #Iterates through the indices of the data list (which represents the historical price data), 
    # starting from index 1 and ending at the second-to-last index. 
    # The loop starts from index 1 because the code checks for conditions 
    # involving the previous and next elements.
        if (data[i] < data[i - 1] and data[i] < data[i + 1] and
                data[i + 1] > data[i] and data[i + 2] > data[i + 1]):
            #This line checks four conditions to identify a potential "W" pattern:
            #data[i] < data[i - 1]: Checks if the current price is lower than the previous price, 
            # indicating a downward movement.
            #data[i] < data[i + 1]: Checks if the current price is lower than the next price, 
            # indicating a trough or a bottom.
            #data[i + 1] > data[i]: Checks if the next price is higher than the current price, 
            # indicating a rise after the trough.
            #data[i + 2] > data[i + 1]: Checks if the price two days ahead is higher than the next price, 
            # indicating another rise after the initial rise.
            #If all four conditions are met, it suggests that a "W" pattern might be present, 
            # and the index i is appended to the w_pattern_indices list.
            w_pattern_indices.append(i)
    return w_pattern_indices

def find_W_pattern(data):
    # First Decline (Left Leg of the W): The price of the asset experiences a significant decline, 
    # reaching a trough (local minimum). This decline represents a period of bearish sentiment 
    # and selling pressure in the market.
        
    w_pattern_indices = []
    for i in range(1, len(data) - 1): 
       
        # Check for the first decline until trough
        if data[i] < data[i - 1]:  # Check if current day is lower than previous day
            decline_days = 1
            while data[i + decline_days] < data[i + decline_days - 1]:
                decline_days += 1  # Count the number of consecutive declining days
                if i + decline_days >= len(data) - 2:
                    break  # Break if end of data is reached
            # Check if the decline is followed by a recovery
            if (data[i + decline_days] > data[i + decline_days - 1] and
                    data[i + decline_days + 1] > data[i + decline_days]):
                # Check for the second decline until trough
                if data[i + decline_days + 2] < data[i + decline_days + 1]:  # Check if the next day is lower
                    decline_days_second = 1
                    while data[i + decline_days + 2 + decline_days_second] < data[i + decline_days + 2 + decline_days_second - 1]:
                        decline_days_second += 1  # Count the number of consecutive declining days
                        if i + decline_days + 2 + decline_days_second >= len(data) - 2:
                            break  # Break if end of data is reached
                    # Check if the second decline is followed by a final recovery
                    if (data[i + decline_days + 2 + decline_days_second] > data[i + decline_days + 2 + decline_days_second - 1] and
                            data[i + decline_days + 2 + decline_days_second + 1] > data[i + decline_days + 2 + decline_days_second]):
                        w_pattern_indices.append(i)
    return w_pattern_indices


# Specify the option symbol for /MES
option_symbol = '^GSPC' # S&P 500

# Get historical data for the option
historical_data = si.get_data(option_symbol, start_date='07/01/2023', end_date='01/31/2024')

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
    #df['adjclose'].plot()
    #plt.show()
    
    
    # Plot the 'adjclose' price
    df['adjclose'].plot()

    # Find "W" patterns in the adjusted close prices
    w_pattern_indices = find_w_pattern(df['adjclose'])

    # Plot markers for "W" pattern if found
    if w_pattern_indices:
        w_pattern_prices = df['adjclose'].iloc[w_pattern_indices]
        plt.scatter(w_pattern_prices.index, w_pattern_prices, color='red', marker='o', label='W pattern')

    plt.legend()
    plt.show()
else:
    print(f"No historical data available for {option_symbol}")
    
    
