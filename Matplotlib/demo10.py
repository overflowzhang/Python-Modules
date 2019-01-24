#圆

from matplotlib.patches import Ellipse, Circle  
  
import matplotlib.pyplot as plt  
fig = plt.figure()  
ax = fig.add_subplot(111)  
cir1 = Circle(xy = (0.0, 1.0), radius=3, alpha=0.4)   
ax.add_patch(cir1)  
plt.axis('scaled')  
plt.axis('equal')   
plt.title('circle')  
plt.show() 