import pandas as pd

index = pd.Index(['a', 'b','c','d','e'])

print(index.get_loc('d'))

sliced = index.slice_locs('b', 'd')
print(sliced)

# for aligning data
print(index.get_indexer(['c','e','f']))     # c -> postion 2, e -> pos 4, f -> cannot be found (-1)

