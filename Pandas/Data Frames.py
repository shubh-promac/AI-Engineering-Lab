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
df['Job'] = ['Circus Performer', 'Brawl Police', None]  # Adding a new column to the DataFrame
print(df)

# print(df.describe())  # Get summary statistics of the DataFrame
# print(df.info())  # Get information about the DataFrame, including data types and non-null