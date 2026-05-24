import pandas as pd

df = pd.read_csv("Pandas/Datasets/pokemondata.csv")

# groupby() function
# used to group data based on a specific column and perform aggregate functions on the grouped data.
group = df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())
print(df.groupby('Height').Weight.min()) # finds and displays the minimum Weight for each unique Height value

# print(df.groupby('Mythical').apply(lambda df: df.Name.iloc[0])) this method will be deprecated in the future
# finds and displays the very first Name that appears in each category of the Mythical column.

# So use this
print(df.groupby('Mythical')['Name'].first())
# or
print(df.groupby('Mythical')['Name'].nth(0))

print(df.groupby(['Type1', 'Type2']).apply(lambda df: df.loc[df.Weight.idxmax()]))
#Finds the complete row of the heaviest item (the one with the maximum Weight)
# for every unique combination of Type1 and Type2

print(df.groupby(['Type1']).Height.agg([len, min, max]))
# calculates three different statistics for the Height column across every unique category in Type1


# counts the total number of items (names) for every unique combination of Type1 and Type2
m = df.groupby(['Type1', 'Type2']).Name.agg([len]) #old way
m.reset_index() # in general the multi-index method you will use most often is the one for converting back to a regular index
# so if index was something else the index now starts from 0
print(m) # converts your MultiIndex (country and province) back into regular columns 

uniquepokemon = df.groupby(['Type1', 'Type2']).Name.agg(Total_Count='count') # modern way
print(uniquepokemon)

# Sorting
import pandas as pd

# 1. Create a raw dataset from scratch
data = {
    'country': ['US', 'US', 'Argentina', 'Greece', 'Argentina', 'US'],
    'province': ['California', 'Texas', 'Mendoza', 'Sterea Ellada', 'Mendoza', 'California'],
    'winery': ['Winery A', 'Winery B', 'Winery C', 'Winery D', 'Winery E', 'Winery F']
}
df = pd.DataFrame(data)
print("--- 1. Raw DataFrame ---")
print(df, "\n")

# 2. Group by multiple columns to automatically create a MultiIndex
# This counts the number of wineries per country and province
countries_reviewed = df.groupby(['country', 'province']).size().to_frame(name='len')
print("--- 2. DataFrame with a MultiIndex (Notice the nested row labels) ---")
print(countries_reviewed, "\n")

# 3. Flatten the MultiIndex into regular columns
countries_reviewed = countries_reviewed.reset_index()
print("--- 3. Flattened DataFrame (After reset_index) ---")
print(countries_reviewed, "\n")

# 4. Sort the DataFrame by the 'len' column in ascending order
countries_reviewed_sorted = countries_reviewed.sort_values(by='len')
print("--- 4. Final Sorted DataFrame ---")
print(countries_reviewed_sorted)

