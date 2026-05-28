import numpy as np
# Joining arrays
'''Joining means putting contents of two or more arrays in a single array. In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.'''
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr67 = np.concatenate((arr1, arr2), axis=1)
print(arr67)
'''Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.'''
arr76 = np.stack((arr1, arr2), axis=0)
print(arr76)

# Stacking along rows(Horizontal stacking)
arr87 = np.hstack((arr1, arr2))
print(arr87)

# Stacking along columns(Vertical stacking)
arr88 = np.vstack((arr1, arr2))
print(arr88)

# Stacking along depth
arr89 = np.dstack((arr1, arr2))
print(arr89)

# Splitting arrays
'''Splitting is reverse operation of Joining. Joining merges multiple arrays into one and Splitting breaks one array into multiple.
We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.'''
arr90 = np.array([1, 2, 3, 4, 5, 6])
arr91 = np.array_split(arr90, 3)
print(arr91)
'''We can also specify the axis along which we want to split the array.'''
arr92 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
arr93 = np.array_split(arr92, 4, axis=0)
print(arr93)
arr94 = np.array_split(arr92, 3, axis=1)
print(arr94)

# Splitting along rows(Horizontal splitting)
arr95 = np.hsplit(arr92, 3)
print(arr95)
# Splitting along columns(Vertical splitting)
arr96 = np.vsplit(arr92, 3)
print(arr96)
# Splitting along depth
arr97 = np.dsplit(arr92, 3)
print(arr97)    