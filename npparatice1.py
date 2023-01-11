import numpy as np

# a = np.array([[[1,2,3],[2,3,4],[4,5,6]]])

# a = np.array([1,2,3],ndmin=3)

a = np.array([1,2,3,5,6,7,8,9])
print(a[1]+a[2])
print(a.ndim)
print(a[:2])
print(a[1:5:2])



b = np.array([[1,2,3],[2,3,4]])
print(b[0,1])

c = np.array([[[1,3,4],[3,4,5]]])
print(c[0,1,2])

# arr = np.array(['apple', 'banana', 'cherry'])

# print(arr.dtype)
# arr = np.array([1, 2, 3, 4], dtype='i4')

# print(arr)
# print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(bool)
print(newarr.dtype)

