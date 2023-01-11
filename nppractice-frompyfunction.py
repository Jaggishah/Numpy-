import numpy as np

def add(x,y):
    return x+y

myadd = np.frompyfunc(add,2,1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
