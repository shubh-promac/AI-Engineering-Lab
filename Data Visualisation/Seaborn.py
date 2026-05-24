import seaborn as sns
import matplotlib.pyplot as plt

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()
sns.displot([0, 1, 2, 3, 4, 5], kind="kde") # kind="kde" makes it a smooth curve instead of bars

plt.show()
