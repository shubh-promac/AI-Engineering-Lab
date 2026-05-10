import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Rayleigh distribution
# Rayleigh distribution is a continuous probability distribution

'''
Think of the Rayleigh distribution as the "Distance from the Bullseye."
Imagine you are trying to hit the exact center of a target.
1. The Two ErrorsEvery time you throw, you make two small mistakes:
-Left or Right (The horizontal error)
-Up or Down (The vertical error)
2. What is "Strength"?
The strength is simply the total distance your dart landed away from the center.
-It doesn't care which direction you missed.
-It only cares how far you missed by.
3. Why the Rayleigh Shape?
If you throw 1,000 darts, the distances (the "strengths") create a specific pattern:
-Near Zero: It's hard to get a "perfect" 0.00 distance (dead center).
-The Hump: Most of your darts land at a medium distance away.
-The Tail: Very few darts land extremely far away (like on the next wall).

Rayleigh distribution is used in signal processing.

It has two parameters:
scale - (standard deviation) decides how flat the distribution will be default 1.0).
size - The shape of the returned array.
'''

x = random.rayleigh(scale=2, size=(2, 3))
print(x)
sns.displot(random.rayleigh(size=1000), kind="kde")
plt.show()
# Similarity Between Rayleigh and Chi Square Distribution
# At unit stddev and 2 degrees of freedom rayleigh and chi square represent the same distributions.
