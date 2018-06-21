# -*- coding: utf-8 -*-
"""
Listing 2-3. PARC
"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([-10,140,90,-10])

plt.axis('on')
plt.grid(True)

plt.arrow(0,0,20,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,20,head_length=4,head_width=3,color='k')

plt.text(16,-3,'x')
plt.text(-5,17,'y')

xc=20
yc=20
r=40

p1=20*np.pi/180
p2=70*np.pi/180
dp=(p2-p1)/100
for p in np.arange(p1,p2,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.scatter(x,y,s=1,color='g')
    
plt.text(61,34,'(x1,y1)')
plt.text(16,60,'(x2,y2)')
plt.scatter(xc,yc,s=10,color='k')
plt.text(xc+4,yc-4,'(xc,yc)',color='k')

plt.show()