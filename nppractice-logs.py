import numpy as np
from math import log
arr = np.arange(1,10)
print(np.log10(arr))

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])
print(newarr)

arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)

print(newarr)
# /prod cumprod

arr = np.array([10, 15, 25, 5])
print(np.diff(arr,n=2))