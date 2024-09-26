import pandas as pd

s01 = pd.DataFrame({'volume':[37, 200, 281, 4000, 440, 500, 113, 138],
                    'company':['AAPL', 'AAPL', 'AAPL', 'AAPL', 'GOOG', 'GOOG', 'GOOG', 'GOOG'],
                    'date':['2009-12-28', '2009-12-29', '2009-12-30', '2009-12-31',
                            '2009-12-28', '2009-12-29', '2009-12-30', '2009-12-31']})
print(s01)

s01_piv = s01.pivot(index='date', columns=['company'])
print(s01_piv)

s02 = pd.DataFrame({'volume':[12, 43, 21, 4300, 10, 200],
                    'company':['MSFT', 'MSFT', 'MSFT', 'YHOO', 'YHOO', 'YHOO'],
                    'date':['2009-12-28', '2009-12-29', '2009-12-30',
                            '2009-12-28', '2009-12-29', '2009-12-30']})
print(s02)

s02_piv = s02.pivot(index='date', columns=['company'])
print(s02_piv)

s_join = s01_piv.join(s02_piv)
print('\n',s_join)

