import pandas as pd

print(pd.__version__)

data = [1.4, 1, 1, 0.9, 0.6, 0.067]

series = pd.Series(data) # Creates an 1 dimensional array
print(series)

series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f'])
# You can also label the index, there has to be an index label for each item in the data list otherwise you will get an error
print(series)

# We can also locate values using the index labels

# Shorthand method to locate values using the index labels is to use the square brackets
print(series['a']) # this will print 1.4

# Clearer way to locate values using the index labels is to use the loc method
print(series.loc['a']) # this will also print 1.4

# Locating values using the index labels also allows us to change the value of an item
series.loc["c"] = 200
print(series)

# Position-based indexer. Use this if you want to find the first item, regardless of what its label is.
print(series.iloc[0]) # or if you want to find the second item, you can use iloc[1]

# Filtering a series using a boolean expression
print(series [series >= 1])

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
series = pd.Series(calories)
# Adding data to an existing value in a series
series.loc["Day 3"] += 800
print(series.loc[["Day 3"]])

# Filtering a series using a boolean expression
print(series[series > 2000])