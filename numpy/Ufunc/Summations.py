import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2) # adding element-wise

print(newarr)

arr1 = np.array([1, 2, 6])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2]) # sums all values in both arrays
print(newarr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=0)
print(newarr)

arr = np.array([1, 2, 3])
newarr = np.cumsum(arr) # fibonacci sequence
print(newarr)