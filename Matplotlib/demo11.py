#气泡图

from numpy import *;  
import numpy as np  
import matplotlib.pyplot as plt  
  
N = 50   
x = np.random.rand(N)   
y = np.random.rand(N)   
colors = np.random.rand(N)   
area = np.pi * (15 * np.random.rand(N))**2    
plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker=(9, 3, 30))  
plt.show()