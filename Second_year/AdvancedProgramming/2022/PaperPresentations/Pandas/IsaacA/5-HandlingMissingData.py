import pandas as pd

# IMPORTANCE OF NaNs

# reindex and fillna methods are equipped with a couple simple interpolation 
# options to propagate values forward and backward, which is especially useful for time series data

ts1 = pd.DataFrame({'':[0.03825, -1.9884, 0.73255, -0.0588, -0.4767, 1.98008, 0.04410]},
                    index=['2000-01-03', '2000-01-04', '2000-01-05', '2000-01-06', '2000-01-07', '2000-01-10', '2000-01-11'])
print('printing ts1:',ts1)

ts2 = pd.DataFrame({'':[0.03825, -0.0588, 0.04410, -0.1786]},
                    index=['2000-01-03', '2000-01-06', '2000-01-11', '2000-01-14'])
print('\nprinting ts2:', ts2)

ts3 = ts1 + ts2
print('\nSum of two df:', ts3)

print('\n\nusing .fillna')
ts3 = ts3.fillna(method='ffill')       # fills with the last value available the data after
print(ts3)

print('\n\nusing .add')
ts_add = ts1.add(ts2, fill_value=0)     # treats missing values as 0 when adding two Series objects
print(ts_add)

print('\n\n')
print('sum of the sum of the values in the two tf:')
print((ts1 + ts2).sum())
print('\ncount of the values given by the sum of the two tf:')
print((ts1 + ts2).count())

# similar to R's is.na function, which detects NA (Not Available) values, 
# pandas has special API functions isnull and notnull for determining the validity of a data point.
# { this contrast with numpy.isnan in that they can be used with dtypes other than float 
# and also detect some other markers for 'missing' occurring in the wild, such as the python None value}
print(pd.notnull(ts1 + ts2))
print(pd.isnull(ts1/ts2))
        #   { it is used usually when importing .csv files which may contain null data points } ***