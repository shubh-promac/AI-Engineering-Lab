import numpy as np

'''
A discrete difference means subtracting two successive elements.
E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]

To find the discrete difference, use the diff() function.
'''

arr = np.array([1, 2, 3, 4])
newarr = np.diff(arr)
print(newarr)
'''
We can perform this operation repeatedly by giving parameter n.

E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1].
Then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
'''
newarr = np.diff(arr, n=2)
print(newarr)