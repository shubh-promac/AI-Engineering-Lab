import pandas as pd
df = pd.read_csv("Pandas/Datasets/pokemondata.csv", index_col='Name')
# index_col would set the index as the names of pokemon the rows

# SELECTION BY COLUMN

print(df["Height"].to_string()) # separate column
print(df[["Height", "Weight"]].to_string()) # multiple columns

# SELECTION BY ROW
print(df.loc["Zapdos"].to_string()) # separate row

zap = df.loc["Zapdos"]
print(df.loc['Zapdos', ["Height", "Weight"]])  # type: ignore # the code is correct but pylance is bugging so i have added this

print(df.loc['Zapdos':'Blastoise', ["Height", "Weight"]])

print(df.iloc[0:11:2])

print(df.iloc[0:11:2, 0:2])

pokemon = input("Enter a Pokemon name: ")
try:
    print(df.loc [pokemon])
except KeyError:
    print(f"{pokemon} not found")