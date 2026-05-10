import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.divide(arr1, arr2))
print(np.mod(arr1, arr2))
print(np.power(arr1, arr2))
print(np.remainder(arr1, arr2))
print(np.floor_divide(arr1, arr2))
print(np.divmod(arr1, arr2))
arr = np.array([-1, -2, 1, 2, 3, -4])
print(np.absolute(arr)) # can aslo use abs(arr) for absolute value
# but should use np.absolute() to avoid confusion with python's inbuilt math.abs()