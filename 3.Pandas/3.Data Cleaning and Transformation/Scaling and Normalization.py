import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.preprocessing import minmax_scaling
from sklearn.preprocessing import MinMaxScaler

'''
In both Scaling and Normalization, you're transforming the values of numeric variables so that the transformed data points have specific helpful properties. 
The difference is that:
~Scaling: you're changing the range of your data
~Normalization: you're changing the shape of the distribution of your data.
'''

np.random.seed(0)
# generate data
original_data = np.random.exponential(size=1000)

# min-max scale the data between 0 and 1
# mlxtend expects a 2D array for columns parameter, so reshape then flatten back
original_2d = original_data.reshape(-1, 1)
scaled_2d = minmax_scaling(original_2d, columns=[0])
scaled_data = scaled_2d.ravel()

# plot both together to compare
fig, ax = plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(scaled_data, ax=ax[1], kde=True, legend=False)
ax[1].set_title("Scaled data")
plt.show()