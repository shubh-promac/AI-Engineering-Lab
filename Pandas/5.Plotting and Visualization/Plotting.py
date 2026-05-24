import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Pandas/Datasets/morehealthdata.csv')

df.plot()

plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

# Bad correlation

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()

# Histogram
df["Duration"].plot(kind = 'hist')