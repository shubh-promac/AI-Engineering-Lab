import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''
Used to describe probability where every event has equal chances of occuring.

It has three parameters:
low - lower bound - default 0.0
high - upper bound - default 1.0
size - The shape of the returned array
'''
x = random.uniform(size=(2, 3))
print(x)
sns.displot(x.flatten(), kind="kde") # flatten() is used to convert the 2D array into a 1D array for plotting
plt.show()

'''
In a Uniform Distribution, every value within a specific range is equally likely to occur.
This results in a probability density function that is flat across the top.
While the edges of the first graph are slightly rounded (likely due to kernel density smoothing), it is the only one that attempts to show a constant
probability between its bounds.
'''