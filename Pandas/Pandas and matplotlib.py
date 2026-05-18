import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Pandas/pokemondata.csv')

print(df["Type1"].value_counts())

plt.barh(df["Type1"].value_counts().index, df["Type1"].value_counts())
plt.xlabel('Count')
plt.ylabel('Type1')
plt.title('Count of Pokemon by Type1')
# plt.xticks(rotation=45) # if i make a horizontal bar chart, i don't need to rotate the x-axis labels
plt.show()