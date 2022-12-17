import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0,3*np.pi,0.1)
b = np.sin(a)
plt.plot(a,b)
plt.show()