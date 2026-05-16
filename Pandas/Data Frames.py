import pandas as pd

# You can only create an array with more than 1 dimension with DataFrames, not with Series

brawlers = {'Name': ['Stu', 'Colt', 'Meg'],
          'Rarity': ['Epic', 'Rare', 'Legendary']}

# Create a DataFrame from the dictionary
df = pd.DataFrame(brawlers, columns=['Name', 'Rarity'], index=['Brawler1', 'Brawler2', 'Brawler3'])

print(df)
# Accessing a column
print(df['Name'])
# Accessing a row
print(df.loc['Brawler2'])
# Accessing a specific value
print(df.loc['Brawler3', 'Rarity'])
df['Job'] = ['Circus Performer', 'Brawl Police', 'Superhero']  # Adding a new column to the DataFrame
print(df)

# print(df.describe())  # Get summary statistics of the DataFrame
# print(df.info())  # Get information about the DataFrame, including data types and non-null

# Adding 2 dataframes together
brawlers2 = {'Name': ['Shelly', 'Nita', 'Barley'],
          'Rarity': ['Starter', 'Rare', 'Rare'], 
          'Job': ['Brawl Police', None, 'Waiter']}

new_row = pd.DataFrame(brawlers2, index=['Brawler4', 'Brawler5', 'Brawler6'])
# Concatenating the original DataFrame with the new DataFrame
df = pd.concat([df, new_row], ignore_index=False, sort=True) # we can use ignore_index=True to reset the index of the new dataframe
# the sort parameter sorts the indexes

print(df)