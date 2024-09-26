import pandas as pd

df = pd.DataFrame({'A':[-0.1047, 0.3245, 0.3453, 0.5432, 1.3234],
                    'B':[1.032, 2.543, 1.342, 0.999, 2.012],
                    'C':[123, 432, 1234, 543, 323],
                    'D':[-0.232, -0.323, -0.212, 0.232, 0.453]})
print('\n',df)

df_slice = df.loc[:3, ['A', 'B', 'C']]
print(df_slice)

df_slice['ind'] = df_slice['A'] > 0
print(df_slice)

