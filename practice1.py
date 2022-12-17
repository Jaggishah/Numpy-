import numpy as np

a = np.arange(6)

print(a)

a = a.reshape(3,2)
print(a)

b = np.linspace(10,100,10)
print(b)

c = np.char.capitalize("jaggi is good guy")
print(c)

c = np.char.title("jaggi is good guy")
print(c)
d= np.random.randint(5,10,5,dtype=int)
print(d)
e = np.random.uniform(5,10,5)
print(e)
f = np.random.random(3)
g = np.random.randint(4)
print(f,g,"---")
h= np.zeros((3,2),dtype=int)
print(h)
i = np.ones((2,3),dtype=int)
print(i,np.resize(i,(4,5)))
print(i,np.reshape(i,(3,2)))
print(np.full((2,4),fill_value=2))
print(np.identity(4))
l = np.arange(9)
print(np.max(l),np.unique(l,return_counts=True),np.mean(l))