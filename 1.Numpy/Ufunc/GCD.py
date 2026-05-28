import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)
print(x)

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)

# GCD of two arrays
arr1 = np.array([20, 8, 32, 36, 16])
arr2 = np.array([4, 12, 16, 24, 8])
x = np.gcd(arr1, arr2)
print(x)