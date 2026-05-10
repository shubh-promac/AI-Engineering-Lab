import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
# Remember arrays can only be 1D
x = np.unique(arr) # Used to find unique elements in an array. It returns the sorted unique elements of an array.
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)
print(newarr)

newarr = np.intersect1d(arr1, arr2, assume_unique=True)
# assume_unique: if true can speed up the calculation, but the results can be wrong if the arrays are not unique.
print(newarr)

newarr = np.setdiff1d(arr1, arr2, assume_unique=True) # To find values unique to only the first set and not in the second set.
print(newarr)

newarr = np.setxor1d(arr1, arr2, assume_unique=True) # To find only the values that are NOT present in BOTH sets
print(newarr)