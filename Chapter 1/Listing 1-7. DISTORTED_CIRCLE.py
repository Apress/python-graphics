# -*- coding: utf-8 -*-
"""
Listing 1-7. DISTORTED_CIRCLE
"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0,100,100,0])

r=40
alpha1=np.radians(0)
alpha2=np.radians(360)
dalpha=np.radians(2)
xc=50
yc=50
plt.scatter(xc,yc,s=10,color='k')
for alpha in np.arange(alpha1,alpha2,dalpha):
    x=xc+r*np.cos(alpha)
    y=yc+r*np.sin(alpha)
    plt.scatter(x,y,s=5,color='k')

plt.show()