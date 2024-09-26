import pandas as pd
import numpy as np

d = {'a':[1, 232, 0], 'b':[2, 123, 4], 'c':[3, 5, 23]}
ser = pd.Series(data=d, index=['a','c','b','d'])
print(ser)

print('\n\nExample2')
print('From a list to a serie, using False as copy parameter')
r = [1, 2]
ser = pd.Series(data=r, copy=False)
ser.iloc[0] = 3

print(r)
print(ser)

print('\n\nExample3')
print('Due to *input data type* the Series has a `view` on the original data, so the data is changed as well.')
g = np.array([1,2])
ser = pd.Series(data=g, copy=False)     # if the copy parameter was set to True it wouldn't change.
ser.iloc[0] = 999

print(g)
print(ser)