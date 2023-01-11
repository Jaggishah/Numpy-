import numpy as np

arr = np.array([1,2,3,5])
newarr = arr.copy()
newarr[2] = 4
print(arr.shape,newarr)

newarr2 = arr.view()
newarr2[3] = 9
print(arr,newarr)
print(arr.base,newarr2.base)

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1,2,4,5,6,7,7,5])
print(arr.reshape(2,4))
print(arr.reshape(2,4).base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)
# reshape flatten the arraty(-1)
print(newarr)