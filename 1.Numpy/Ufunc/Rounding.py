import numpy as np

arr = np.array([-3.1666, 3.6667])
print(np.trunc(arr))
# np.fix() is also used but will be removed in the future. np.trunc() is the recommended function to use for truncating values.
arr = np.around(arr, 2) # np.around(values to round, number of decimals to round to)
print(arr)

arr = np.floor([-3.1666, 3.6667]) # rounds down to the nearest integer
print(arr)

arr = np.ceil([-3.1666, 3.6667]) # rounds up to the nearest integer
print(arr)