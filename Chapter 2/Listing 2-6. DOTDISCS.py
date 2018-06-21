   # -*- coding: utf-8 -*-
"""
Listing 2-6. DOTDISCS
"""

import matplotlib.pyplot as plt
import numpy as np
import random as rnd

plt.axis([0,150,100,0])

plt.title('Program DOTDISCS')

plt.axis('on')
plt.grid(True)

plt.arrow(0,0,20,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,20,head_length=4,head_width=3,color='k')

plt.text(16,-3,'x')
plt.text(-5,15,'y')

#--------------------------------------------------------simple r,p dot pattern
xc=40
yc=40

p1=0
p2=2*np.pi
dp=np.pi/20

rmax=20
dr=2

for r in np.arange(dr,rmax,dr):
    for p in np.arange(p1,p2,dp):
        x=xc+r*np.cos(p)
        y=yc+r*np.sin(p)
        plt.scatter(x,y,s=2,color='k')

#--------------------------------------------------equal arc length dot pattern
xc=105
yc=40

p1=0
p2=2*np.pi

rmax=20    
dr=2
dc=np.pi*rmax/40

for r in np.arange(dr,rmax,dr):
    dpr=dc/r
    for p in np.arange(p1,p2,dpr):
      x=xc+r*np.cos(p)
      y=yc+r*np.sin(p)
      plt.scatter(x,y,s=2,color='k')
         
#------------------------------------------------------------------------labels
plt.text(38,66,'r,p')
plt.text(95,66,'equal arc')

plt.show()

