import numpy as np

'''
Hyperbolic functions:
- np.sinh()
- np.cosh()
- np.tanh()
- np.arcsinh()
- np.arccosh()
- np.arctanh()
'''

x = np.arcsinh(np.pi/2)
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.cosh(arr)
print(x)