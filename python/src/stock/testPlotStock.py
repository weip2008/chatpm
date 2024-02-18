import matplotlib.pyplot as plt
import yfinance as yf

# Get the data for the S&P 500 index
data = yf.download('^GSPC', '2019-01-01', '2024-01-01')

# Plot the close price of the S&P 500
data['Close'].plot()

# Derive the date format dynamically from the 'Date' column
date_column_name = 'Date'  # Adjust this according to the actual column name
date_format = '%Y-%m-%d'  # Default format
if date_column_name in data.columns:
    sample_dates = data[date_column_name].sample(min(5, len(data[date_column_name])))  # Sample a few dates
    date_format_candidates = set(sample_dates.dt.strftime('%Y-%m-%d'))  # Extract unique date formats
    if len(date_format_candidates) == 1:
        date_format = date_format_candidates.pop()  # Use the format if it's consistent across the sample

# Set the format of x-axis labels to include year and month
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter(date_format))

plt.show()
