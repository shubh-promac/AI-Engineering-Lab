import numpy as np

scores = np.array([85, 90, 78, 92, 88])
# Comparison operators
print(scores == 80)  # Equal to 80
print(scores < 90)  # Less than 90
print(scores >= 85)  # Greater than 85
print(scores != 88)  # Not equal to 88

a = scores[scores > 85] # This creates a new array 'a' that contains only the scores greater than 85.
print(a)
scores[scores > 85] = 67 # Set all scores greater than 85 to 67
print(scores)
# Element-wise comparisons between two arrays
scores2 = np.array([80, 90, 78, 95, 88])
print(scores > scores2)  # Element-wise comparison
