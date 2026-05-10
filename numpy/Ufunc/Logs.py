import numpy as np
from math import log

arr = np.arange(1, 10)
# write the number in logn() where n is the base of the logarithm
print(np.log2(arr))
print(np.log10(arr))

# natural logarithm or at base e
print(np.log(arr))

# Log at any base
'''
NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log()
with two input parameters and one output parameter:
'''

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))