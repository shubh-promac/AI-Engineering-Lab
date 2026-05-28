import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 250, 10000) # np.random.normal(mean, standard deviation, number of data points)
print(len(x))
plt.hist(x, bins=10, color='blue', edgecolor='black')
# the bins argument controls the number of bars(intervals) the more number of bins the more intervals there are
plt.show()