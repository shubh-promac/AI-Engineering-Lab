
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Exponential distribution
# Exponential distribution is a continuous probability distribution
'''
Exponential distribution is used for describing time till next event
It has two parameters:
scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
size - The shape of the returned array.
'''

x = random.exponential(scale=1, size=100) # example for scale, papa burps every 1 hour on average, so scale is 1.
# If we want to model papa burping every 2 hours on average, we would set scale to 2.
print(x)
sns.displot(x.flatten(), kind="kde")
plt.show()

sns.displot(random.exponential(scale = 60, size=100), kind="kde")
plt.show()

# Relation Between Poisson and Exponential Distribution
# Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events.
