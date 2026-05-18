import pandas as pd

df = pd.read_csv('Pandas/morehealthdata.csv')
# 0.09 is a bad correlation but 0.9 is a very good correlation
# -0.09 is bad correlation but -0.9 is a very good correlation
# -1 and 1 are perfect correlations
print(df.corr())