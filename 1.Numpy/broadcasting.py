import numpy as np

array1 = np.array([[1, 2, 3, 4]])
array2= np.array([[1], 
                  [2], 
                  [3], 
                  [4]])
result = array1 + array2 # Look at broadcasting.png for reference
print(array1.shape)
print(array2.shape)
print(result)
print(array1 * array2)
'''
array3 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
array4 = np.array([[1], [2], [3], [4]])
print(array3.shape)
print(array4.shape)
print(array3 * array4)
'''
a1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
a2 = np.array([[1],[2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(a1 * a2)