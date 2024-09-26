import pandas as pd

s1 = pd.DataFrame({'':[0.044, 0.050, 0.101, 0.0113, 0.138, 0.037, 0.200, 0.281, 0.040]},
                    index=['AAPL', 'IBM', 'SAP', 'GOOG', 'C', 'SCGLY', 'BAR', 'DB', 'VW'])
print('s1:', s1)

s2 = pd.DataFrame({'':[0.025, 0.158, 0.028, 0.087, 0.004, 0.154, 0.034]},
                    index=['AAPL', 'BAR', 'C', 'DB', 'F', 'GOOG', 'IBM'])
print('\ns2:', s2)

print('\nApplying .reindex()') # is used to align one of these 1D Series objects with the other before adding them
print(s1.reindex(s2.index))
print('\notherwise: s1 + s2')
print(s1 + s2)
# in this case the data have been automatically aligned based on their labels and added together. 
# The result object contains the union of the labels between the two objects so that NO INFORMATION IS LOST

# reindexing can be avoided when Index objects are shared -> effective in performance-sensitive applications
print('\n\nIf columns are different')
# Data alignment using DataFrame occuts automatically on both the column and row labels. 
#This data alignment differs from any other tools outside of Python.
# if the columns themself are different, the resulting object will contain the union of the columns

s01 = pd.DataFrame({'AAPL':[0.044, 0.050, 0.0113, 0.138], 'GOOG':[0.037, 0.200, 0.281, 0.040]},
                    index=['2009-12-28', '2009-12-29', '2009-12-30', '2009-12-31'],
                    columns=['AAPL', 'GOOG'])
print(s01, '\n')

s02 = pd.DataFrame({'AAPL':[2.3e+07, 1.587e+07, 1.47e+07]},
                    index=['2009-12-28', '2009-12-29', '2009-12-30'],
                    columns=['AAPL'])
print(s02, '\n')

print('s01/s02:\n', s01/s02)# This grants immense freedom as there is no longer a need to sanitize data from an untrusted source

print('\nApplying .fillna()\n',(s01/s02).fillna(0))     # applying fillna

s03 = (s01/s02).dropna(axis=1, how='all')   # applying dropna
print('\nApplying .dropna()\n', s03)