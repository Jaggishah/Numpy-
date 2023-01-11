import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

x = np.subtract(arr2,arr1)
print(x)
# multiply and division
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

y = np.power(arr1,arr2)
print(y)
z= np.divmod(arr1,arr2)
print(z)
k = np.absolute(arr1)
print(k)