from numpy import random
import numpy as np


# x= random.randint(100)
x= random.randint(100,size=(3,5))
print(x)
# y = random.rand()
y = random.rand(5)
print(y)
z = random.choice([3,5,6,7],size=(3,5))
print(z)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
# random.choice([1,2,323],p=[0.1,0.4] )
print(x)

arr= np.array([1,2,4,5])
random.shuffle(arr)
print(arr)
print(random.permutation(arr))