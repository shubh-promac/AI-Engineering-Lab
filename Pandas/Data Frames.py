import pandas as pd

# You can only create an array with more than 1 dimension with DataFrames, not with Series

brawlers = {'Name': ['Stu', 'Colt', 'Meg'],
          'Rarity': ['Epic', 'Rare', 'Legendary']}

# Create a DataFrame from the dictionary
df = pd.DataFrame(brawlers, columns=['Name', 'Rarity'], index=['Brawler1', 'Brawler2', 'Brawler3'])

print(df)
# Accessing a column
print(df['Name'])
print(df.Name)
# Accessing a row
# print(df['Name'][0]) in future this will be deprecated, so we should use .loc or .iloc instead
print(df.loc['Brawler2'])
# Accessing a specific value
print(df.loc['Brawler3', 'Rarity'])
df['Job'] = ['Circus Performer', 'Brawl Police', 'Superhero']  # Adding a new column to the DataFrame
print(df)

print(df.loc[df.Name.isin(['Stu', 'Colt'])]) # type: ignore

# This style is type-safe and usually eliminates the need for '# type: ignore'
print(df.loc[df['Name'].isin(['Stu', 'Colt'])])

# Prefer this (only ignores the missing attribute error):
print(df.loc[df.Name.isin(['Stu', 'Colt'])])  # type: ignore[attr-defined]

# Summary functions and Maps
print(df.describe())  # Quick Statistical Summary # Get summary statistics of the DataFrame
print(df.info())  # Get information about the DataFrame, including data types and non-null

# Adding 2 dataframes together
brawlers2 = {'Name': ['Shelly', 'Nita', 'Barley'],
          'Rarity': ['Starter', 'Rare', 'Rare'], 
          'Job': ['Brawl Police', None, 'Waiter']}

new_row = pd.DataFrame(brawlers2, index=['Brawler4', 'Brawler5', 'Brawler6'])
# Concatenating the original DataFrame with the new DataFrame
df = pd.concat([df, new_row], ignore_index=False, sort=True) # we can use ignore_index=True to reset the index of the new dataframe
# the sort parameter sorts the indexes

print(df)

print(df['Job'].isnull())  # Check for null values in the DataFrame
print(df['Job'].notnull())  # Check for non-null values in the 'Job' column

# Add a 'critic' column to the DataFrame (was 'reviews' which is undefined)
df['Job'] = 'Unemployed' # making them all jobless
# this will change all the values in the 'Job' column to 'Unemployed', use a list to change specific values
print(df)

df['Ability'] = ['Speed Boost', 'Silver Bullet', 'Mecha Punch', 'Power Shot', 'Bear Fur', 'Spillage'] # this will create a whole new column
print(df)

i = ['Brawler1', 'Brawler2', 'Brawler3', 'Brawler4']
few_brawlers = df.loc[i]
print(few_brawlers)

cols = ['Name', 'Rarity', 'Job', 'Ability']
indices = ['Brawler1', 'Brawler2', 'Brawler3', 'Brawler4']
selected_brawlers = df.loc[indices, cols]
print(selected_brawlers)

rare_brawlers = df[df['Rarity'] == 'Rare']
print(rare_brawlers)