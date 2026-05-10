import numpy as np
array3d = np.array([[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
                    , [["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r"]]
                    , [["s", "t", "u"], ["v", "w", "x"], ["y", "z", "_"]]])
# Chain Indexing
print(array3d[0][0][0])
print(array3d[1][1][1])
#Multidimensionsal Indexing
print(array3d[0, 0, 0]) # this will show the first element of the first row of the first layer, which is "a" in this case
print(array3d[1, 1, 1]) # this will show the second element of the second row of the second layer, which is "n" in this case

# Concatenation
word = array3d[0, 0, 0] + array3d[0, 0, 1] + array3d[0, 0, 2] # concatenation
print(word)

# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method
# can be used for those usecases.

arr23 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr23):
  print(idx, x)