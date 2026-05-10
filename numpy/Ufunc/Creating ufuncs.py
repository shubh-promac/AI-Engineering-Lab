import numpy as np

print(type(np.add)) # output: <class 'numpy.ufunc'>
print(np.add(1, 2)) # output: 3
print(type(np.concatenate))

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

# How to create a ufunc
import numpy as np

def my_custom_logic(x, y):
    # This logic will be applied to each pair of elements
    return (x * 2) + y

# Create the ufunc: 2 inputs, 1 output
my_ufunc = np.frompyfunc(my_custom_logic, 2, 1) # 2 np.frompyfunc(func, nin, nout)
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])

result = my_ufunc(arr1, arr2)
print(result)  # Output: [12 24 36]