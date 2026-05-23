from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Poisson distribution
# Poisson Distribution is a Discrete Distribution. It estimates how many times an event can happen in a specified time.
# lam - rate or known number of occurrences e.g. 2 for above problem.
# size - The shape of the returned array.


# 1. Setup parameters
avg_rate = 10    # Average customers per hour (Lambda)
simulations = 1000  # Number of hours to simulate

# 2. Generate Poisson data
# Each number represents the count of customers in one specific hour
data = random.poisson(lam=avg_rate, size=simulations)

# 3. Visualize using Seaborn
plt.figure(figsize=(10, 6))

# We use discrete=True because you can't have 10.5 customers
# We add the KDE to see the smooth "probability shape" line over the histogram
sns.histplot(data, kde=True, discrete=True, color='teal', alpha=0.6) # alpha is for transparency

plt.title(f'Poisson Distribution Simulation (Avg={avg_rate} Customers/Hour)')
plt.xlabel('Number of Customers in an Hour')
plt.ylabel('Frequency (How many hours)')
plt.axvline(avg_rate, color='red', linestyle='--', label=f'Mean ({avg_rate})')
plt.legend()

plt.show()

# 4. Check the results
print(f"Average of simulated data: {data.mean()}")
print(f"Max customers in an hour: {data.max()}")
print(f"Min customers in an hour: {data.min()}")