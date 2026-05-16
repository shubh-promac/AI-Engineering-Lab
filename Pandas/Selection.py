import pandas as pd
df = pd.read_csv("Pandas/pokemondata.csv")

# SELECTION BY COLUMN

print(df["Height"].to_string()) # sepearate column

print(df[["Name", "Height", "Weight"]].to_string()) # multiple columns