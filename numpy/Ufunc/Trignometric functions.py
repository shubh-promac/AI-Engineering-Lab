import numpy as np
'''
Trigonometric functions:
- np.sin()
- np.cos()
- np.tan()
- np.arcsin()
- np.arccos()
- np.arctan()
'''
x = np.sin(np.pi/2)
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

# Convert degrees to radians
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

# Convert radians to degrees
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)

# Finding the hypotenuse of a right triangle using trigonometric functions
base = 3
perp = 4

x = np.hypot(base, perp)

print(x)
