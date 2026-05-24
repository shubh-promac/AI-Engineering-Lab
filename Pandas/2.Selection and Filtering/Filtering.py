import pandas as pd

df = pd.read_csv("Pandas/Datasets/pokemondata.csv")

M_pokemon = df.loc[df["Name"].str[0] == "M"] # Finding All pokemon whose name starts with M
# can also use M_pokemon = df[df["Name"].str.startswith("M")]
# m_ending = df.loc[df["Name"].str.endswith("M")]
# all pokemon whose name starts with M and are Mythical
print(M_pokemon.loc[df["Mythical"] == True, ["Name", "Type1", "Type2", "Height", "Weight"]].to_string(index=False)) # Don't need index here so index=False

# Traditional way
print(df[df["Weight"] > 100])

# Query way
print(df.query("Weight > 100")) # this is a more efficient way to filter data and also more readable

print(df.query("Type1 == 'Fire' and Name.str.startswith('R')"))