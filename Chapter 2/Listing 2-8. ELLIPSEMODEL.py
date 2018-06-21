# -*- coding: utf-8 -*-
"""
Listing 2-8. ELLIPSEMODEL
"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([-75,75,50,-50])

plt.axis('on')
plt.grid(True)

plt.arrow(0,0,60,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,40,head_length=4,head_width=3,color='k')

plt.text(58,-3,'x')
plt.text(-5,40,'y')

#-----------------------------------------------------ellipse
a=50.
b=30.
p1=0.
p2=180.*np.pi/180.
dp=(p2-p1)/180.

xplast=a
yplast=0
for p in np.arange(p1,p2+dp,dp):
    xp=np.abs(a*b*(b*b+a*a*(np.tan(p))**2.)**-.5)
    yp=np.abs(a*b*(a*a+b*b/(np.tan(p)**2.))**-.5)    
    if p > np.pi/2:
        xp=-xp
    plt.plot([xplast,xp],[yplast,yp],color='k')
    plt.plot([xplast,xp],[-yplast,-yp],color='k')
    xplast=xp
    yplast=yp
    
#--------------------------------------------------------line
plt.plot([0,40],[0,40],color='k')  

#-------------------------------------------------------point
p=45.*np.pi/180.
xp=np.abs(a*b*(b*b+a*a*(np.tan(p))**2.)**-.5)
yp=np.abs(a*b*(a*a+b*b/(np.tan(p)**2.))**-.5)  
plt.scatter(xp,yp,s=20,color='r') 

#------------------------------------------------------labels
plt.text(23,-3,'a',color='k') 
plt.text(-5,15,'b',color='k')
plt.text(32,28,'(xp,yp)')
plt.text(30,12,'p')
plt.text(10,18,'r')

p1=0
p2=45*np.pi/180
dp=(p2-p1)/180
r=30
for p in np.arange(p1,p2,dp):
    x=r*np.cos(p)
    y=r*np.sin(p)
    plt.scatter(x,y,s=.1,color='r')
    
plt.arrow(25,17.5,-1,1,head_length=3,head_width=2,color='r')

plt.show()