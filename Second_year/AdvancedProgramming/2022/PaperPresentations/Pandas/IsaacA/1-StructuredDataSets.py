import pandas as pd

stocks = pd.read_csv('data.csv')
print(stocks)
print(type(stocks))
print('\n')

group_symb = stocks.groupby('Symbol').Close.mean()
print(group_symb)
print('\n')
print(group_symb.index)
print('\n')

ser = stocks.groupby(['Symbol', 'Date']).Close.mean() # it's a serie multiindex
print(ser)
print('\n')
print(ser.index)
print('\n')
print(ser.unstack())
print(ser)

ser = stocks.groupby(['Date', 'Symbol', 'Close']).mean()
print(ser)

ser_swapped = ser.swaplevel(0, 1, axis=0)
print(ser_swapped)


ser_sortedl = ser_swapped.sort_index()
print(ser_sortedl)

ser_sortedv = ser.sort_values(by='Volume')
print(ser_sortedv)