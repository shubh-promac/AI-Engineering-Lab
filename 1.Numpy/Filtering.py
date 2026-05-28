import numpy as np
# Filtering is the process of selecting specific elements from an array based on a condition.
ages = np.array([[22, 25, 18, 30, 27], 
                 [20, 24, 19, 28, 26]])
# Boolean indexing is a powerful technique for filtering arrays based on conditions. It allows you to create a boolean array that indicates which elements of the original array meet a certain condition, and then use that boolean array to select the desired elements.
# undeveloped = ages < 25 this is wrong as it will produce a boolean array
undeveloped = ages[ages < 25]
print(undeveloped)
developed = ages[ages >= 25]
print(developed)
#np.where()
# np.where(condition, array, fillvalue) is used to replace values in an array based on a condition
above20 = np.where(ages > 20, ages, np.nan) # np.nan is used to represent missing values numerical data
#np.where() is only used to preserve the shape of the original array, keeps the values that meet the condition unchanged as it is slower than boolean indexing
print(above20)
print(np.isnan(above20))
# np.isnan() is used to check for nan values in an array, it returns a boolean array where true indicates the presence of nan values


#Boolean Indexing
arr1 = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr1[x]
print(newarr)