import pandas as pd

df = pd.DataFrame({'A':['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                    'B':['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                    'C':[-1.834, 1.772, -0.67, 0.04931, -0.5215, -3.202, 0.7927, 0.1461],
                    'D':[1.903, -0.7472, -0.309, 0.3939, 1.861, 0.9365, 1.256, -2.655]})
print(df)

df_groupA = df.groupby('A').mean()
print(df_groupA)

for key, values in df.groupby('A'):
    print(key)  # not needed this print
    print(values)

print('\nit is also possible to group by multiple columns')
df_groupAB = df.groupby(['A', 'B']).mean()      # you can also use .sum() or other operations.
print(df_groupAB)
print('The default result of a multi-key groupby aggregation is a hierarchical index.\n',
        'This can be disabled when calling groupby which may be useful in some settings')
df_groupAB_noix = df.groupby(['A', 'B'], as_index=False).mean()
print(df_groupAB_noix)