import numpy as np
ar1 = np.array([1,2,3,4,5,6])
ar2 = np.array([3,4,5,8,9,1])
print(np.intersect1d(ar1,ar1))
print(np.setdiff1d(ar1,ar2))
print(np.setxor1d(ar1,ar2))
print(np.union1d(ar1,ar2))
# print(np.hsplit(ar1,2)) 
# vspl
print(np.hstack((ar1,ar2)))
print(np.allclose(ar1,ar2,0.5))
print(np.equal(ar1,ar2))
print(np.repeat('2018',1))
print(np.tile('2018',(3,2)))