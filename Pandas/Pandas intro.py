import pandas as pd

print(pd.__version__)

data = [1.4, 1, 1]

series = pd.Series(data) # Creates an 1 dimensional array
print(series)

series = pd.Series(data, index=['a', 'b', 'c']) # i can also label the index, 
print(series)

# We can also locate values using the index labels
print(series['a']) # this will print 1.4
print(series.loc['a']) # this will also print 1.4

# Position-based indexer. Use this if you want to find the first item, regardless of what its label is.
print(series.iloc[0]) # or if you want to find the second item, you can use iloc[1]
data = [set([1, 2, 3]), set([4, 5, 6]), set([7, 8, 9])]

df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)