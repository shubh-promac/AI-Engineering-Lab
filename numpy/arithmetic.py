import numpy as np

array = np.array([1, 2, 3])
# Scalar operations
print(array + 1)
print(array - 1)
print(array * 2)
print(array / 2)
print(array ** 2)
print(array % 2)
print(array // 2)

# Vectorized operations
# These operations are performed on the whole array at once, without the need for explicit loops.
array2 = np.array([4.3, 5.67, 6.99])
print(np.sqrt(array2))
print(np.square(array2))
print(np.round(array2))
print(np.floor(array2))# Rounds down to the nearest integer
print(np.ceil(6.01)) # Rounds up to the nearest integer, regardless of the decimal part.
print(np.trunc(6.99)) # Rounds towards zero, removing the decimal part without rounding.
print(np.pi) # The mathematical constant π (pi), approximately equal to 3.14159.

#Element-wise operations
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print(a1 + a2)
print(a1 * a2)
print(a1 / a2)
print(a1 ** a2)