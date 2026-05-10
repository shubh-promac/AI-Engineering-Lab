import numpy as np

# LCM of two numbers
num1 = 4
num2 = 6

x = np.lcm(num1, num2)
print(x)

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)
print(x)

arr = np.arange(1, 11) # arange() creates an array of integers from 1 to 10
x = np.lcm.reduce(arr)
print(x)

# LCM of two arrays
arr1 = np.array([2, 3, 4])
arr2 = np.array([5, 6, 7])
x = np.lcm(arr1, arr2)
print(x)