import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Multinomial distribution
# Multinomial distribution is a generalization of the binomial distribution.
'''
It has three parameters:
n - number of times to run the experiment.
pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
size - The shape of the returned array.
'''
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)
sns.displot(x, kind="kde")
plt.show()