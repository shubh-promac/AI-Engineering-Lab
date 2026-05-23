import pandas as pd

brawlers = {'Name': ['Stu', 'Colt', 'Meg', 'Shelly', 'Nita', 'Barley'],
          'Rarity': ['Epic', 'Rare', 'Legendary', 'Starter', 'Rare', 'Rare'],
          'Job': ['Circus Performer', 'Brawl Police', 'Superhero', 'Brawl Police', None, 'Waiter'],
          'Ability': ['Speed Boost', 'Silver Bullet', 'Mecha Punch', 'Power Shot', 'Bear Fur', 'Spillage'],
          'Number': [1, 2, 3, 4, 5, 6]}


df = pd.DataFrame(brawlers, columns=['Name', 'Rarity', 'Job', 'Ability', 'Number'], index=['Brawler1', 'Brawler2', 'Brawler3', 'Brawler4', 'Brawler5', 'Brawler6'])

# Summary functions
print(df.describe())  # Quick Statistical Summary # Get summary statistics of the DataFrame
print(df.info())  # Get information about the DataFrame, including data types and non-null
print(df.Number.mean())
print(df.Number.unique()) # To see a list of unique values
print(df.Number.value_counts()) # To see the count of each unique value


# Maps
# Using map to create a new column based on existing data

number_mean = df.Number.mean()
df['Number_Category'] = df.Number.map(lambda p: p - number_mean) # map only applies to a series or a single column, element-wise
print(df)

def remean_points(row):
    row.Number = row.Number - number_mean
    return row

df.apply(remean_points, axis='columns') # use apply when doing it to a whole dataframe or series, column-wise
print(df)

df.head(1)