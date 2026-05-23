from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Pareto distribution
# continous probability distribution

'''
1. Matching the "80/20" RuleIf you want to simulate a scenario where X% of the effects come from Y% of the causes, you calculate a using this formula:
a = ln(1/P) / ln(R)
In the formula above, the X and Y from the "80/20" rule are embedded within P and R.To keep it simple:
-P represents the top percentage of the population (the "few").
-R represents the concentration ratio (how many times more they have).
Mapping the variables
If you have an X/Y rule (e.g., 80% of wealth is held by 20% of people):
-Y is the population portion: Usually the smaller group (e.g., 20% or 0.20). This becomes your P.
X is the wealth/effect portion: Usually the larger group (e.g., 80% or 0.80).
How to calculate R
R is the ratio between what they have versus what they are.R=X/Y

Step-by-step example (80/20 Rule)
1) Identify X and Y: X = 0.80, Y = 0.20.
2) Find P: P = Y = 0.20.
3) Find R: R = 0.80 / 0.20 = 4.
4) Plug into formula: 
  1. a = ln(1 / 0.20) / ln(4)
  2. a = ln(5) / ln(4)
  3. a = 1.16  aproximately.
'''

# Legacy Way for pareto distribution
x = random.pareto(a=2, size=(2, 3))
print(x)
sns.displot(random.pareto(a=1.16, size=1000), kind="kde")
plt.title("Pareto Distribution with a=1.16 (80/20 Rule)")
plt.show()

# Modern Way for pareto distribution
rng = random.default_rng(seed = 123)
data = rng.pareto(a=1.16, size=(1000))
sns.displot(data, kind="kde")
plt.title("Pareto Distribution with a=1.16 (80/20 Rule)")
plt.show()
