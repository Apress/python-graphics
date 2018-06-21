# -*- coding: utf-8 -*-
"""
Listing 1-9. COORDINATE_AXES
"""

import numpy as np
import matplotlib.pyplot as plt

x1=-10
x2=140
y1=90
y2=-10
plt.axis([x1,x2,y1,y2])

plt.title('Sample Axes')

#-----------grid
dx=5
dy=-5
for x in np.arange(x1,x2,dx):
    for y in np.arange(y1,y2,dy):
        plt.scatter(x,y,s=1,color='lightgray')
        
#-----------coordinate axes
plt.arrow(0,0,20,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,20,head_length=4,head_width=3,color='k')

plt.show()