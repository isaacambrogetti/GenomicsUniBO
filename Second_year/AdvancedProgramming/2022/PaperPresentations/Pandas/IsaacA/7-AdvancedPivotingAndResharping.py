import pandas as pd

df = pd.read_csv('ScientificPaper/data.csv')
print(df)

col = df.columns
print(col)

df_ind3 = df.set_index(['Date', 'Symbol'])
print(df_ind3)

df_ind3_st = df_ind3.stack()
print(df_ind3_st)

df_ind3_su = df_ind3.stack().unstack()
print(df_ind3_su)

df_ind3_piv = df.pivot(index='Date', columns='Symbol')
print(df_ind3_piv)

print(df_ind3_piv.stack().max(1).unstack())

