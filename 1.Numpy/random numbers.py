import numpy as np

rng = np.random.default_rng()
# Generate 2 random integers between 1 and 10 (exclusive), rng.integers(low, high{exclusive}, size)
print(rng.integers(1, 10, 2))
# Generate 3 random floats between 0 and 1, rng.random(size)
# For readablity, you can use:
print(rng.integers(low=1, high=10, size=2)) # Generate 2 random integers between 1 and 10 (exclusive)
# You can also generate a 2d array
print(rng.integers(1, 10, (3,2))) # Generate a 2x3 array of random integers between 1 and 10 (exclusive)

rng2 = np.random.default_rng(1) # You can set a seed for reproducibility, it gives the same results on any device or any time we run the code
# rng2 = np.random.default_rng(seed=42) for more readability
print(rng2.integers(1, 101, (3,2))) # This will always generate the same random integers between 1 and 10 (exclusive) because of the seed

# np.random.uniform(low, high, size) generates random floats between low and high (exclusive)
print(np.random.uniform(0, 1, 5)) # Generate 5 random floats between 0 and 1
# you can also set a seed for reproducibility with np.random.seed(seed)
np.random.seed(1)
print(np.random.uniform(-1, 1, (3,2,3))) # Generate a 3D array of random floats between -1 and 1, with shape (3,2,3)

array1 = np.random.randint(1, 10, (3,2)) # Generate a 2D array of random integers between 1 and 10 (exclusive)
print(array1)

array = np.array([1, 2, 3])
print(np.random.choice(array, 2)) # Randomly select 2 elements from the array
print(np.random.choice(array, 5, replace=True)) # Randomly select 5 elements from the array with replacement (allowing duplicates)

#Shuffling an array
array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
rng67 = np.random.default_rng()
rng67.shuffle(array2) # Shuffle the array in place
print(array2)

x67 = np.random.rand(6) # Generate 6 random floats between 0 and 1
print(x67)

# Shuffling an array
gar = np.array([1, 2, 3, 4, 5])
np.random.shuffle(gar) # Shuffle the array in place, making changes to the original array
print(gar)


''' 
Permution is a random shuffling of an array, it returns a new array with the elements shuffled, while shuffle shuffles the array in place. No change made to original array.
# We can set the probability of selecting each element in the random selection process using the `p` parameter in the `numpy.random.choice` function.
# The `p` parameter takes an array of probabilities corresponding to each element in the input array. The probabilities should sum to 1.
'''
arr = np.array([1, 2, 3, 4, 5])
np.random.permutation(arr)
print(arr)
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).

# Probability in random selection

x = np.random.choice([3, 5, 7, 9], p=[0.067, 0.3, 0.6, 0.033], size=(100))
print(x)

xp = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(xp)