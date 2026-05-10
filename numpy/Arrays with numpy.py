import numpy as np

print(np.__version__)

a = np.array([1, 2, 3, 4])
#a*= 2 this will also work, but it modifies the original array in place, while a = a * 2 creates a new array and assigns it to a. In this case, since we are not using the original array after this operation, both will give the same result. However, if we were to use the original array later in the code, using a *= 2 would modify it and could lead to unexpected results.
a = a * 2 #
print(a)
print(type(a)) # this will show that a is a numpy array, not a list

array = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])
print(array.ndim) # this will show the number of dimensions of the array, which is 2 in this case

array3d = np.array([[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
                    , [["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r"]]
                    , [["s", "t", "u"], ["v", "w", "x"], ["y", "z", "_"]]])
''' i have used _ as a placeholder for the 27th element in the 3D array, 
since we have only 26 letters in the alphabet. This is just to complete the array and it prevents an error message about the array being incomplete.
As each sub-array in the 3D array needs to have the same number of consstent elements'''

print(array3d.ndim) # this will show the number of dimensions of the array, which is 3 in this case
print(array3d.shape) # this will show the number of rows, columns, and layers of the array, which is (3, 3, 3) in this case

# Copy or View
'''The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
   The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.'''

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

y = arr.view()
arr[0] = 67
print(arr)
print(y)

#Every NumPy array has the attribute base that returns None if the array owns the data. Otherwise, the base  attribute refers to the original object.
print(x.base) # this will show None, because x is a copy of arr and it owns its own data
print(y.base) # this will show the original array arr, because y is a view of arr and it does not own its own data

# Array Reshaping
arr67 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr67.reshape(4, 3)
print(newarr)

newarr67 = arr67.reshape(2, 3, 2)
print(newarr67)

newarr6 = arr67.reshape(2, 2, -1)
#You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.
print(newarr6)

#Iteration
'''
We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while
iterating. NumPy does not change the data type of the element in-place (where the element is in array) so it
needs some other space to perform this action, that extra space is called buffer, and in order to
enable it in nditer() we pass flags=['buffered'].op_dtypes are th main reason nditer() is used
'''
arr45 = np.array([1, 2, 3])
for x in np.nditer(arr45, flags=['buffered'], op_dtypes=['S']):
  print(x)

arr23 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr23[:, ::2]):#you can also slice the peiceof array you want to iterate over
  print(x)

# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method
# can be used for those usecases.
for idx, x in np.ndenumerate(arr23):
  print(idx, x)


'''
numpy.asarray(): Also creates an array, but it doesn't copy the input if it's already an array
np.ravel()
The numpy.ufunc.at() method performs an unbuffered, in-place operation on an array at specific indices.
np.resize()
np.repeat()
np.dot()
'''