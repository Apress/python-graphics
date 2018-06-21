# -*- coding: utf-8 -*-
"""
Listing 1-3. CUSTOM_GRID
"""

import numpy as np
import matplotlib.pyplot as plt

x1=-5
x2=15
y1=-15
y2=5

plt.axis([x1,x2,y1,y2])

plt.axis('on')

dx=.5
dy=.5
for x in np.arange(x1,x2,dx): 
    for y in np.arange(y1,y2,dy):
        plt.scatter(x,y,s=1,color='grey')

plt.show()