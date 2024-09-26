# importing pandas library as alias pd
import pandas as pd

# calling the pandas read_csv() function.
# and storing the result in DataFrame df
df = pd.read_csv('ScientificPaper/homelessness.csv')

print(df.head())        # no indexing in this df

# using the pandas columns attribute.
col = df.columns
print(col)


# using the pandas set_index() function.
df_ind3 = df.set_index(['region', 'state', 'individuals'])
# we can sort the data by using sort_index()
df_ind3.sort_index()
print(df_ind3.head())     # get hierarchical indexing

print('\nSelecting indexes from level 0')
df_ind3_region = df_ind3.loc[['Pacific', 'Mountain']]
print(df_ind3_region.head(10))

print('\nUsing inner level indexes with the help of a list of tuples')
#   df.loc[[(level(0), level(1), level(2))]]
df_ind3_region_state = df_ind3.loc[[    ('Pacific', 'Alaska', 1434),
                                        ('Pacific', 'Hawaii', 4131),
                                        ('Mountain', 'Arizona', 7259),
                                        ('Mountain', 'Idaho', 1297)]]
print(df_ind3_region_state)



print('\n\nUtility methods for manipulating a MultiIndex:\tswaplevel & sortlevel')
df3_swapped = df_ind3.swaplevel(0, 1, axis=0)
print(df3_swapped)

df3_sortedl = df_ind3.sort_index()
print(df3_sortedl)

df3_sortedv = df_ind3.sort_values(by='family_members')
print(df3_sortedv)