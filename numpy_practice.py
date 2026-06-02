import numpy as np

# --------------------------------
# Array Creation
# --------------------------------

array1 = np.array([10, 20, 30, 40, 50])

array2 = np.arange(1, 11)

array3 = np.zeros((2, 3))

array4 = np.linspace(0, 100, 5)

# --------------------------------
# Print Arrays
# --------------------------------

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\nArray 3:")
print(array3)

print("\nArray 4:")
print(array4)

# --------------------------------
# Inspect Arrays
# --------------------------------

print("\nArray 1 Details:")
print("Shape :", array1.shape)
print("Data Type :", array1.dtype)
print("Dimensions :", array1.ndim)

print("\nArray 3 Details:")
print("Shape :", array3.shape)
print("Data Type :", array3.dtype)
print("Dimensions :", array3.ndim)

# --------------------------------
# Indexing
# --------------------------------

print("\nFirst Element of Array1:")
print(array1[0])

# Negative Index
print("\nLast Element using Negative Index:")
print(array1[-1])

# --------------------------------
# Slicing
# --------------------------------

print("\nSubarray from Array2:")
print(array2[2:7])