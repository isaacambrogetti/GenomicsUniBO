import pandas as pd

df = pd.DataFrame({'A':['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                    'B':['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                    'C':[-1.834, 1.772, -0.67, 0.04931, -0.5215, -3.202, 0.7927, 0.1461],
                    'D':[1.903, -0.7472, -0.309, 0.3939, 1.861, 0.9365, 1.256, -2.655]})
print(df)

print('\nGroup the df object by column A, select just C column, and apply the describe function to each subgroup:')
df_groupA_C = df.groupby('A')['C'].describe().T     # .T transpose the df
print(df_groupA_C)