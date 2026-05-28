import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "Engineering", "Marketing", "Engineering", "Finance"],
    "Salary": [55000, 85000, 62000, 90000, 75000],
    "Experience_Years": [3, 6, 4, 7, 5]
}


df = pd.DataFrame(data).set_index('Employee_ID')

df.rename(columns={'Experience_Years': 'Experience', 'Salary': 'Income'}, inplace=True) # Renaming a few columns # without using inplace the changes won't apply
#print(df.rename(columns={'Experience_Years': 'Expereience', 'Salary': 'Income'})) # you could do this to get an output but it won't save to the original database
df.rename(index={101: 'firstEntry', 102: 'secondEntry'}, inplace=True) # renaming a few specific indexes only with out an error

'''
# Old Way
df.rename_axis("Field", axis='columns', inplace=True)
df.rename_axis("People", axis='rows', inplace=True)
print(df)
'''

# New Way
df.rename_axis(columns="Field", inplace=True)
df.rename_axis(index="People", inplace=True)
print(df)