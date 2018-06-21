# -*- coding: utf-8 -*-
"""
Listing 1-6. SQUARE
"""

import numpy as np
import matplotlib.pyplot as plt

plt.grid(True)
plt.axis('on')

plt.axis([-10,10,10,-10])

#-----------------custom grid
x1=-10
x2=10
y1=10
y2=-10

dx=.5
dy=-.5
for x in np.arange(x1,x2,dx):
    for y in np.arange(y1,y2,dy):
        plt.scatter(x,y,s=1,color='lightgrey')

#-----------------square box
plt.plot([-5,5],[-5,-5],linewidth=2,color='k')
plt.plot([5,5],[-5,5],linewidth=2,color='k')
plt.plot([5,-5],[5,5],linewidth=2,color='k')
plt.plot([-5,-5],[5,-5],linewidth=2,color='k')

plt.show()

