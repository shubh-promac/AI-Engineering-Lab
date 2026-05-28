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

# what are the type1 of all pokemon how many of each type in the data set
# Creates a series whose index is the Type1 and whose values count how many of each type there are
reviews_written = df.groupby('Type1').size()
print(reviews_written)
# OR
reviews_written = df.groupby('Type1').Type1.count()
print(reviews_written)

# counts the total number of items (names) for every unique combination of Type1 and Type2
m = df.groupby(['Type1', 'Type2']).Name.agg([len]) #old way
m.reset_index() # in general the multi-index method you will use most often is the one for converting back to a regular index
# so if index was something else the index now starts from 0
print(m) # converts your MultiIndex (country and province) back into regular columns 

uniquepokemon = df.groupby(['Type1', 'Type2']).Name.agg(Total_Count='count') # modern way
print(uniquepokemon)

# Sorting
mi = uniquepokemon.index
print(type(mi))
uniquepokemon.reset_index()
# To see the sorted output, assign to a variable or use inplace=True
sorted_uniquepokemon = uniquepokemon.sort_values(by='Total_Count', ascending=False) # type: ignore
uniquepokemon.sort_index()
print(sorted_uniquepokemon)
uniquepokemon.sort_values(by=['Type1','Total_Count']) # type: ignore #forms the data set into alphabetical order 
print(uniquepokemon)

