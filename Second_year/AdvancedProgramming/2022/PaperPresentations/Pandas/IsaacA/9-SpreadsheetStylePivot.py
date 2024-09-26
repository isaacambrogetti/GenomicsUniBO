import pandas as pd
from pandas import pivot_table
import numpy as np

df = pd.read_csv('ScientificPaper/tips.csv')
print(df)

print(pivot_table(df, 'tip_pct', columns='smoker'))

## check this shit better, the dataset you made is not even close to the one in the example 
## -> fake them