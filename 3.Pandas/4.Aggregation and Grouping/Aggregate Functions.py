import pandas as pd

df = pd.read_csv("Pandas/Datasets/pokemondata.csv")

# Whole dataframe

print(df.mean(numeric_only=True)) # numeric_only is used to ignore non-numeric columns and avoid errors.
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())

# Single column
print(df["Height"].mean())

# Single row
data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['X', 'Y', 'Z'])
print(data.loc['X'].mean())

print(data)

# groupby() function
# used to group data based on a specific column and perform aggregate functions on the grouped data.
group = df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())