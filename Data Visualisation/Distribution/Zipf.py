import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Zipf distribution
# Zipf distribution is a discrete probability distribution
'''
The Zipf distribution in NumPy generates integers where small numbers are very common and large numbers are extremely rare.
'''

# Create a generator (Modern NumPy way)
rng = random.default_rng()

# Generate 10 samples with distribution parameter a=2.0
samples = rng.zipf(a=2.0, size=10)
print(samples)

# If you want to simulate a library of 1,000 books where word popularity follows Zipf's law:
# Rank 1 (e.g., "the"): Occurs most frequently.
# Rank 10: Occurs roughly 1/10th as often as Rank 1.
# Rank 100: Occurs roughly 1/100th as often as Rank 1.
# Simulate 100,000 word occurrences in a text
word_counts = rng.zipf(a=2.0, size=100000)

# See how many times the "most popular" word (1) appeared vs others
unique, counts = np.unique(word_counts, return_counts=True) # Count occurrences of each unique word rank
# np.unique function in NumPy finds and returns the sorted, unique elements of an input array
zipf_dict = dict(zip(unique, counts))

print(f"Occurrences of word '1': {zipf_dict.get(1)}")
print(f"Occurrences of word '10': {zipf_dict.get(10)}")

# Legacy Way for zipf distribution
x = random.zipf(a=2, size=1000)
sns.displot(x[x<10])

plt.show()