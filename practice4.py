import numpy as np
a= np.arange(1,10).reshape(3,3)
b = np.arange(21,30).reshape(3,3)

print(np.einsum('ii->i',a))
print(np.einsum('ij',a))
print(np.einsum('ji',a))
print(np.einsum('ij,jk',a,b))
print(np.einsum('ii',a))


print(np.histogram(a))
print(np.std(a))
print(np.var(b))
np.set_printoptions(precision=2)
y = np.array([(1,2,3),(4,5,6)])
print(y.ravel())