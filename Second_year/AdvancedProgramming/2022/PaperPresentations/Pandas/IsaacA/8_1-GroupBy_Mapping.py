import pandas as pd

print('In the previous examples, when we pass column names we are simply establishing a correspondance between the row lables and the group identifiers.\n',
        'There are other ways to do this; the most general is to pass a Python function (for single-key) or list of functions (for multi-key) which will be nivoked on each label, producing a group by specification.\n')

df = pd.DataFrame({'':['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04', '2000-01-05'],
                    'A':[0.121, 0.5434, 0.2321, 0.554, 0.232],
                    'B':[-3.202, 0.7927, 0.1461, 1.256, -2.655],
                    'C':[-1.834, 1.772, -0.67, 0.04931, -0.5215],
                    'D':[1.903, -0.7472, -0.309, 0.3939, 1.861]})
print(df)

mapping = {'A':'Group 1', 'B':'Group 2', 'C':'Group 1', 'D':'Group 2'}

for name, group in df.groupby(mapping.get, axis=1):
    print(name)
    print(group)