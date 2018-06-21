# -*- coding: utf-8 -*-


"""
Listing 2-13. 2DROTCIRCLE2
"""

import matplotlib.pyplot as plt
import numpy as np

plt.axis([-10,150,100,-10])
plt.axis('on')
plt.grid(True)

#--------------------------------------------------------------------------axes
plt.arrow(0,0,40,0,head_length=4,head_width=2,color='b')
plt.arrow(0,0,0,40,head_length=4,head_width=2,color='b')
plt.text(30,-3,'Xg',color='b')
plt.text(-8,34,'Yg',color='b')

xc=80       #--------------------center of rotation
yc=30 
plt.plot([xc-50,xc+60],[yc,yc],linewidth=1,color='grey') #----X
plt.plot([xc,xc],[yc-35,yc+60],linewidth=1,color='grey') #----Y
plt.text(xc+50,yc-2,'X')
plt.text(xc-5,yc+55,'Y')

plt.scatter(xc,yc,s=20,color='k')   #---plot center of rotation
plt.text(xc-5,yc-3,'c')

#-----------------------------------------------------define rotation matrix Rz
def rotz(xp,yp,rz):
    c11=np.cos(rz)
    c12=-np.sin(rz)
    c21=np.sin(rz)
    c22=np.cos(rz)
    xpp=xp*c11+yp*c12    #----relative to xc,yc
    ypp=xp*c21+yp*c22
    xg=xc+xpp            #----relative to xg,yg
    yg=yc+ypp
    return [xg,yg]
    
#------------------------------------------------------------------plot circles
p1=0
p2=2*np.pi
dp=(p2-p1)/100

alpha1=0
alpha2=2*np.pi
dalpha=(alpha2-alpha1)/5

for alpha in np.arange(alpha1,alpha2,dalpha):
    xcc=25*np.cos(alpha)
    ycc=25*np.sin(alpha)
    for p in np.arange(p1,p2,dp):
        xp=xcc+10*np.cos(p)
        yp=ycc+10*np.sin(p)
        [xg,yg]=rotz(xp,yp,0)
        if p < np.pi:
            plt.scatter(xg,yg,s=1,color='r')
        else:        
            plt.scatter(xg,yg,s=1,color='g')
        xp1=xcc+10
        yp1=ycc+0
        [xg1,yg1]=rotz(xp1,yp1,0)
        xp2=xcc-10
        yp2=ycc+0
        [xg2,yg2]=rotz(xp2,yp2,0)
        plt.plot([xg1,xg2],[yg1,yg2],color='b')
        plt.scatter(xg1,yg1,s=10,color='b')
        plt.scatter(xg2,yg2,s=10,color='b')
        
plt.text(xc+34,yc-10,'starting circle')
plt.arrow(xc+34,yc-10,-2,2,head_length=1,head_width=1)
                
plt.show()
