import numpy as np
# THE BASICS

# Initializing the arrays
a = np.array([1, 2, 3])
# specifying the type
c = np.array([1, 2, 3], "int16")
print(a)

b = np.array([[1, 4.0, 7.0], [3.0, 9.0, 8.9]])
print(b)

#  Get Dimension
print(b.ndim)

# Get Shape
print(b.shape)

# Get Type
print(a.dtype)
print(c.dtype)

# Get Item Size
print(a.itemsize)

# get total size
print(a.nbytes)
print(a.itemsize * a.size)

# ACCESSING/CHANGING

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# Get specific element [r,c]
print(a[1, 5])

# Get a specific row
print(a[0, :])

# Get a specific column
print(a[:, 2])

# Getting a little more fancy [starting:end:stepsize]
print(a[0, 1:6:2])

# Changing values
a[1, 5] = 20
print(a)

a[:, 2] = -1
print(a)

# With 3d
v = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(v)

# Get specific element in 3d (work outside in)
print(v[0, 1, 1])

# INITIALIZING DIFFERENT TYPES OF ARRAYS
# All 0s,1s matrix
zero = np.zeros((2, 3), dtype='int32')
one = np.ones((2, 3), dtype='int32')
print(one)
print(zero)

# Any Other Number
any = np.full((2,2),99)
print(any)

#random decimal numbers
np.random.rand(4,2)
np.random.random_sample(v.shape)

# Random Integer Values
np.random.randint(7,size=(3,3))

# The identity Matrix
np.identity(5) 

