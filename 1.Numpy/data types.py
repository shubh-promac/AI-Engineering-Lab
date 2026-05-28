import numpy as np

'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

arr = np.array([1, 2, 3, 4])
print(arr.dtype)
arr1 = np.array(['apple', 'banana', 'cherry'], dtype='S')
print(arr1.dtype)
arr2 = np.array([1, 2, 3, 4], dtype='i4')
print(arr2.dtype)
arr3 = np.array([1, 2, 3, 4], dtype='i8')
print(arr3.dtype)

# Converting Data Type on Existing Arrays
# it truncates the decimal part and converts it into integer
arr4 = np.array([1.1, 2.1, 3.1])
newarr = arr4.astype('i')
print(newarr)
print(newarr.dtype)

