import pandas as pd

s01 = pd.DataFrame({'price':[0.044, 0.050, 0.0113, 0.138, 0.037, 0.200, 0.281, 0.040], 
                    'volume':[37, 200, 281, 4000, 440, 500, 113, 138],
                    'company':['AAPL', 'AAPL', 'AAPL', 'AAPL', 'GOOG', 'GOOG', 'GOOG', 'GOOG'],
                    'date':['2009-12-28', '2009-12-29', '2009-12-30', '2009-12-31',
                            '2009-12-28', '2009-12-29', '2009-12-30', '2009-12-31']})
print(s01)

print('\n')

s01_piv = s01.pivot(index='date', columns=['company'])
print(s01_piv)

s01_piv_stack = s01_piv.stack()     # by default the innermost level is stacked. The level to stack can be specified explicitly
print(s01_piv_stack)

s01_piv_stack2 = s01_piv_stack.stack()   # The level to stack can be specified explicitly
print(s01_piv_stack2)

s01_piv_unstack = s01_piv_stack2.unstack(1)
print(s01_piv_unstack)

s01_max = s01_piv_unstack.max(1).unstack()
print(s01_max)