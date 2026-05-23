from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Chi square distribution
# Chi square distribution is a continuous probability distribution that is used in hypothesis testing and confidence interval estimation

'''
Chi Square distribution is used as a basis to verify the hypothesis.
It has two parameters:
df - (degree of freedom).
size - The shape of the returned array.
'''

x = random.chisquare(df=2, size=(2, 3))
print(x)
sns.displot(random.chisquare(df=1, size=1000), kind="kde")
plt.show()