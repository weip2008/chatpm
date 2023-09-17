import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web

start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2020, 8, 7)

df = web.DataReader("AAPL", 'yahoo', start, end)
df.to_csv('applestock.csv')
print("done.")