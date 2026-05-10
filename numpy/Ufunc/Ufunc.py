import numpy as np

# Ufuncs/ Aggregate functions

'''
ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
ufuncs also take additional arguments, like:
where: boolean array or condition defining where the operations should take place.

dtype: defining the return type of elements.

out: output array where the return value should be copied.
'''

# Vectorization using ufuncs
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)


# Using ufuncs
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)
print(np.multiply(x, y))

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np.sum(array))
print(np.mean(array))
print(np.std(array)) # standard deviation
# Standard deviation is a statistical measure of how spread out numbers are in a data set,
#representing the average distance between each data point and the mean (average)
print(np.var(array)) # Variance, square of the standard deviation
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) # Index of the minimum value
print(np.argmax(array)) # Index of the maximum value
print(np.cumsum(array)) # Cumulative sum of the elements

print(np.sum(array, axis=0)) # Sum along columns
print(np.sum(array, axis=1)) # Sum along rows

