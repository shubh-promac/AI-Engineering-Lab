from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Binomial distribution
# Binomial distribution is a Discrete Distribution.
# It describes the number of successes in a fixed number of independent Bernoulli trials with the same probability of success.
'''
n - number of trials.
p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).
size - The shape of the returned array.
'''
x = random.binomial(n=10, p=0.5, size=10)
print(x)

sns.displot(random.binomial(n=10, p=0.5, size=100))
plt.show()

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()