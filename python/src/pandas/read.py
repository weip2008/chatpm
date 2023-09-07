import pandas as pd
import os
import matplotlib.pyplot as plt


path1 = "data"
file1 = "AAPL.csv"

df1 = pd.read_csv(path1 + "/" + file1)
print(type(df1))
df1['date_column'] = pd.to_datetime(df1['Date'])
plt.plot(df1['date_column'], df1['Adj Close'])
plt.xticks(rotation=45)
plt.show()