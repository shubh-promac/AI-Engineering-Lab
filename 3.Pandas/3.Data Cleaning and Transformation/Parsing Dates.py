import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('3.Pandas/Datasets/Marvel movies.csv')
print(df.head())
print(df['release_date'].head())
print(df['release_date'].dtype)

df['parsed_dates'] = pd.to_datetime(df['release_date'], format = '%Y-%m-%d') # the release_date column is processed and a new column
print(df['parsed_dates'].dtype) # checking if it is in datetime data type
print(df)

print(df['parsed_dates'].dt.day.to_string()) # prints all days
print(df['parsed_dates'].dt.month) # prints first 5 months
print(df['parsed_dates'].dt.year) # prints first 5 years

day_of_the_month_movie_releases = df['parsed_dates'].dt.day.dropna()

# plot the day of the month
# seaborn.displot expects a DataFrame or explicit x parameter; convert Series to DataFrame
sns.displot(data=day_of_the_month_movie_releases.to_frame(name='day'), x='day', kind='hist', bins=31, rug=True)
plt.show()