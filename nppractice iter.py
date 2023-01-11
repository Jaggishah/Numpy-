import numpy as np


# arr = np.array([1, 2, 3])
# for i in np.nditer(arr , flags=['buffered'],op_dtypes=['S']):
#     print(i,end=" ")

arr = np.array([1, 2, 3])

for idx,x in np.ndenumerate(arr):
  print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])
newarr = np.concatenate((arr1,arr2))
print(newarr)


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)
aarrh = np.dstack((arr1,arr2))
print(aarrh)

print(arr)