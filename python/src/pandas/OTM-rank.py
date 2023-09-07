import pandas as pd

# 创建一个包含期权数据的DataFrame，这里仅作示例
data = {'OptionName': ['Option1', 'Option2', 'Option3'],
        'StrikePrice': [100, 110, 120],
        'LastPrice': [5.2, 3.8, 7.5]}

df = pd.DataFrame(data)

# 计算期权的价外价值（Out of The Money）：假设你有标的资产的当前价格 underlying_price
underlying_price = 105
# df['OTM'] = abs(df['StrikePrice'] - underlying_price) > 0
df['CallOTM'] = df['StrikePrice'] >= underlying_price
df['PutOTM'] = df['StrikePrice'] <= underlying_price
# 按照价外价值和最后价格降序排列DataFrame
sorted_df = df[df['CallOTM']].sort_values(by='LastPrice', ascending=False)

# 打印排名结果
print(sorted_df)
