import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.preprocessing import minmax_scaling # using mix max scaling
from scipy import stats

'''
Scaling and normalization are used in data preprocessing to bring numerical variables onto a comparable footing.
Without these transformations, machine learning algorithms and data models can easily become biased toward features with larger numeric values,
severely degrading overall performance.
Main points are:
- Prevents Dominance by Large Numbers
- Speeds Up Algorithm Convergence
- Fixes Distance-Based Calculations
- Improves Visualization and Interpretation

In both Scaling and Normalization, you're transforming the values of numeric variables so that the transformed data points have specific helpful properties.
The difference is that:
~Scaling: you're changing the range of your data
~Normalization: you're changing the shape of the distribution of your data.
'''

'''
Scaling:
Transforming your data so that it fits within a specific scale, like 0-100 or 0-1.
You want to scale data when you're using methods based on measures of how far apart data points are,
like support vector machines (SVM) or k-nearest neighbors (KNN) or Linear & Logistic Regressions
'''
np.random.seed(0)
original_data = np.random.exponential(size=1000)

# min-max scale the data between 0 and 1
# mlxtend expects a 2D array for columns parameter, so reshape then flatten back
original_2d = original_data.reshape(-1, 1)
scaled_2d = minmax_scaling(original_2d, columns=[0])
scaled_data = scaled_2d.ravel() # converting the array back into an one-dimensional array

fig, ax = plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)# ax determines on which side which graph is placed
ax[0].set_title("Original Data")
sns.histplot(scaled_data, ax=ax[1], kde=True, legend=False)
ax[1].set_title("Scaled data")
plt.show()

'''
Normalization
Scaling just changes the range of your data. Normalization is a more radical transformation.
The point of normalization is to change your observations so that they can be described as a normal distribution(the bell curve) where most things fit in the middle.
'''

# normalize the exponential data with boxcox
normalized_data = stats.boxcox(original_data) # only work on positive non-zero numbers

fig, ax=plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(normalized_data[0], ax=ax[1], kde=True, legend=False)
ax[1].set_title("Normalized data")
plt.show()
# as you can probably see a bell curve in this graph, meaning the data has been normalized
