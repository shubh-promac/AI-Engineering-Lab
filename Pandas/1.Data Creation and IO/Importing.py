import pandas as pd

df = pd.read_csv('Pandas/Datasets/pokemondata.csv')
print(df) # This data will be truncated first and last 5 rows are shown. To see all data, use df.to_string()
print(df.head(2)) # can also use df.tail(2) to see last 2 rows
print(df.loc[67])

print(df.to_string())

df = pd.read_json('Pandas/Datasets/pokemondata.csv')
print(df)