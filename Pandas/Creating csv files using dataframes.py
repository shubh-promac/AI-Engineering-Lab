import pandas as pd

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals.to_csv("cows_and_goats.csv") # this line create a csv file
# you can create a json file do this:
animals.to_json("cows_and_goats.json") 