import pandas as pd

df = pd.read_csv("Pandas/Datasets/pokemondata.csv")

# Cleaning the data by removing rows with missing values
#df.dropna(subset=["Type2"], inplace=True) # inplace=True means that the changes will be made to the original dataframe
# subset specifies the column to check for missing values
#print(df.to_string())

# Cleaning the data by filling missing values with a specific value
#df.fillna('nothing here', inplace=True) # inplace=True means that the changes will be made to the original dataframe
#df = df.fillna({"Type2": "None"}) # specifing the category
#df = df.Type2.fillna("None") #could also use this
print(df.to_string())

# Dropping a column
# df = df.drop(columns=["Mythical", "No"])
print(df.to_string())

# Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE", "Water": "WATER"})
print(df.to_string())

# Standardize text
df["Name"] = df["Name"].str.upper()
print(df.to_string())

# Fix data types
df["Mythical"] = df["Mythical"].astype(bool)

# Removing duplicates values
df.drop_duplicates(inplace=True) # inplace=True means that the changes will be made to the original dataframe
print(df.to_string())

df = pd.read_csv('Pandas/Datasets/healthdata.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())

# Replacing Values

df.loc[7, 'Duration'] = 45
print(df.loc[7])

print(df.duplicated()) # To discover duplicates, we can use the duplicated() method.

print(df.isnull())  # Check for null values in the DataFrame
print(df.notnull())  # Check for non-null values in the DataFrame