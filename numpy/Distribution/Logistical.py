import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Logistical distribution
# Continous distribution

'''
It has three parameters:
loc - mean, where the peak is. Default 0.
scale - standard deviation, the flatness of distribution. Default 1.
size - The shape of the returned array.
'''

x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)
sns.displot(x.flatten(), kind="kde")
plt.show()

sns.displot(random.logistic(loc = 4, scale = 67, size=1000), kind="kde")
plt.show()

# Difference between Logistic and Normal distribution
# Both distributions are near identical, but logistic distribution has more area under the tails, meaning it represents more possibility of occurrence of
# an event further away from mean.

data = {
    "normal": random.normal(loc=0, scale=1, size=1000),
    "logistic": random.logistic(loc=0, scale=1, size=1000)
}
sns.displot(data, kind="kde")
plt.show()