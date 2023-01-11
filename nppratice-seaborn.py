import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
from numpy import random
# sns.distplot([0,1,2,3,4,5])
# plt.show()

x= random.normal(loc=1,scale =2,size=(2,3))
print(x)
# sns.distplot(random.normal(size=1000),hist=False)
# plt.show()

# sns.distplot(random.binomial(n=10,p=0.5,size=1000),hist=True,kde=False)
# plt.show()

sns.distplot(random.normal(loc=50 , scale =5 , size =1000),hist=False,label='normal')
sns.distplot(random.binomial(n=100,p=0.5,size=1000),hist= False,label="Binomial")
sns.distplot(random.poisson(lam=50,size=1000),hist= False,label="Poisson")
plt.show()
