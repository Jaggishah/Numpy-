import numpy as np

arr =np.array([1,3,4,5,6,3,55,66,3])
x = np.where(arr==4)
print(x[0][0])

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)
print(np.sort(arr))
