import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]) # 2d array

#Slicing
#array[start:end:step]

print(array[3]) #returns the 4th row of the array, which is [13, 14, 15, 16].
print(array[-2]) #returns the 3rd row of the array, which is [9, 10, 11, 12].
print(array[1:3]) #returns the 2nd and 3rd rows of the array, which are [[5, 6, 7, 8], [9, 10, 11, 12]].
print(array[0:4]) # 4 is used to specify the end index, which is exclusive. It returns everything from index 0 to 3. Which is the whole array
print(array[:]) # as specified in line 9 if you put nothing it will default the end and the start
print(array[::2]) # returns every 2nd row of the array, startng from the first one
print(array[::-1]) # everything but reversed
print(array[::-2])# returns every 2nd row in reverse order

# selecting rows and columns
# array[row, column] you need to put : as a place holder for the row or column if you want to select a whole row or column
# array[start:end:step, start:end:step]
print(array[0,:])
print(array[:,0])
print(array[:,-1])
print(array[:, ::2])# array[start:end:step, start:end:step], this line selects every 2nd column of the array, starting from the start and ending at the end as left blank
print(array[::2, ::2])# every 2nd row and every 2nd column
print(array[:3, 1:3])
print(array[1:3, :3])