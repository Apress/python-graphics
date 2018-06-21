# -*- coding: utf-8 -*-
"""
Listing 2-5. CIRCLES
"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([-75,75,50,-50])

plt.axis('on')
plt.grid(True)

plt.arrow(0,0,20,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,20,head_length=4,head_width=3,color='k')

plt.text(16,-3,'x')
plt.text(-5,17,'y')

#-----------------------------------------------green circle
xc=0
yc=0
r=40

p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
for p in np.arange(p1,p2+dp,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    if p>90*np.pi/180 and p<270*np.pi/180:
        plt.plot([xlast,x],[ylast,y],color='g',linestyle=':')
    else:
        plt.plot([xlast,x],[ylast,y],color='g') 
    xlast=x
    ylast=y
    
    plt.scatter(xc,yc,s=15,color='g')

#--------------------------------------------------red circle
xc=-20
yc=-20
r=10

p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
for p in np.arange(p1,p2+dp,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.plot([xlast,x],[ylast,y],linewidth=4,color='r')
    xlast=x
    ylast=y
    
plt.scatter(xc,yc,s=15,color='r')
    
#------------------------------------------------purple circle
xc=20
yc=20
r=50

p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
for p in np.arange(p1,p2+dp,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.plot([xlast,x],[ylast,y],linewidth=2,color=(.8,0,.8))
    xlast=x
    ylast=y
    
#-----------------------------------------------solid blue disc
xc=-53
yc=-30
r1=0
r2=10
dr=1

p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100
xlast=xc+r1*np.cos(p1)
ylast=yc+r1*np.sin(p1)
for r in np.arange(r1,r2,dr):
    for p in np.arange(p1,p2+dp,dp):
        x=xc+r*np.cos(p)
        y=yc+r*np.sin(p)
        plt.plot([xlast,x],[ylast,y],linewidth=2,color=(0,0,.8))
        xlast=x
        ylast=y
    
plt.show()