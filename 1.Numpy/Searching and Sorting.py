import numpy as np
# Searching

# 1. np.where() Linear search
arr = np.array([1, 2, 3, 4, 5])# returns the indices of the elements that satisfy the condition, the indicies are always returned as a tuple
result = np.where(arr > 3)
print(result)
# 2. np.searchsorted() Binary Search
arr1 = np.array([1, 2, 3, 4, 5])
result = np.searchsorted(arr1, 3) # returns the index, the indicies are always returned as a tuple
print(result)

arr67 = np.array([6, 7, 8, 9])
x = np.searchsorted(arr67, 7, side='right')
print(x)

# Sorting
arr2 = np.array([5, 3, 1, 4, 2]) # By default the left most index is returned, but we can give side='right' to return the right most index instead.
sorted_arr = np.sort(arr2) # ascending order
print(sorted_arr)

arr56 = np.array(['banana', 'cherry', 'apple'])# alphabetical order
print(np.sort(arr56))