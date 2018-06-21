# -*- coding: utf-8 -*-
"""
Listing 5-5. LS
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians, sqrt

#-------------------------------------------------------------------------lists
x=[]
y=[]
z=[]

xg=[]
yg=[]
zg=[]

xc=80               #---sphere center
yc=50
zc=0

rs=40               #---sphere radius

#----------------------------------------------------------fill longitude lists
phi1=radians(-95)
phi2=radians(95)
dphi=radians(10)

for phi in np.arange(phi1,phi2,dphi):
    xp=rs*cos(phi)
    yp=rs*sin(phi)
    zp=0
    x.append(xp)
    y.append(yp)
    z.append(zp)
    xg.append(xp)
    yg.append(yp)
    zg.append(zp)
    
#======================================================define rotation function
def roty(xc,yc,zc,xp,yp,zp,Ry):
    a=[xp,yp,zp]
    b=[cos(Ry),0,sin(Ry)] #--------------------[cx11,cx12,cx13]
    xpp=np.inner(a, b)
    b=[0,1,0] #---------------[cx21,cx22,cx23]
    ypp=np.inner(a,b)   #--------------------scalar product of a,b
    b=[-sin(Ry),0,cos(Ry)]  #---------------[cx31,cx32,cx33]
    zpp=np.inner(a,b) 
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
    return[xg,yg,zg]
    
#=============================================================sphere longitudes 
def plotsphere(xg,yg,zg):
    lastxg=xg[0]
    lastyg=yg[0]
    for i in range(len(x)):   
        if i < len(x)/2:        
            plt.plot([lastxg,xg[i]],[lastyg,yg[i]],linewidth=1 ,color='k')
        else:                   
            plt.plot([lastxg,xg[i]],[lastyg,yg[i]],linewidth=1 ,color='k')
        lastxg=xg[i]
        lastyg=yg[i]
 
#================================================transform coordinates and plot   
def plotspherey(xc,yc,zc,Ry):
    for i in range(len(x)): #-----------------transform & plot Ry sphere
        [xg[i],yg[i],zg[i]]=roty(xc,yc,zc,x[i],y[i],z[i],Ry)
        
    plotsphere(xg,yg,zg)    #---plot rotated coordinates
    
#-------------------------------------------------plot longitudes
Ry1=radians(0)
Ry2=radians(180)
dRy=radians(10)

for Ry in np.arange(Ry1,Ry2,dRy):
    plotspherey(xc,yc,zc,Ry)
     
#--------------------------------------------------plot latitudes
alpha1=radians(0)
alpha2=radians(180)
dalpha=radians(10)

phi1=radians(-90)
phi2=radians(90)
dphi=radians(10)  

for phi in np.arange(phi1,phi2,dphi):             
    r=rs*cos(phi)   #------------------------latitude radius
    xplast=xc+r
    yplast=yc+rs*sin(phi)
    for alpha in np.arange(alpha1,alpha2,dalpha):
        xp=xc+r*cos(alpha)
        yp=yplast
        plt.plot([xplast,xp],[yplast,yp],color='k')
        xplast=xp
        yplast=yp

#-------------------------------------------------line and hit points
xb=-60    #---line beginning
yb=-30
zb=-20

xe=60     #---line end
ye=30
ze=-40    

a=xe-xb
b=ye-yb
c=ze-zb
Qbe=sqrt(a*a+b*b+c*c)      #---line length      
ux=a/Qbe                   #---unit vector $\hat{\mathbf{u}}$
uy=b/Qbe
uz=c/Qbe

dt=1
for t in np.arange(0,Qbe,dt):
    xp=xb+ux*t
    yp=yb+uy*t
    zp=zb+uz*t
    Qpc=sqrt(xp*xp+yp*yp+zp*zp)
    if Qpc>rs:
        plt.scatter(xp+xc,yp+yc,s=5,color='k')
    if Qpc<=rs:
        plt.scatter(xp+xc,yp+yc,s=80,color='r')
        tlast=t
        break
        
for t in np.arange(tlast,Qbe,dt):
    xp=xb+ux*t
    yp=yb+uy*t
    zp=zb+uz*t
    Qpc=sqrt(xp*xp+yp*yp+zp*zp)
    if Qpc>=rs:
        plt.scatter(xp+xc,yp+yc,s=80,color='r')
        tlast=t
        break
    
for t in np.arange(tlast,Qbe,dt):
    xp=xb+ux*t
    yp=yb+uy*t
    zp=zb+uz*t
    Qpc=sqrt(xp*xp+yp*yp+zp*zp)
    if Qpc>=rs:
        plt.scatter(xp+xc,yp+yc,s=5,color='k')
      
plt.axis([0,150,100,0])            #--plot axes and grid
plt.axis('off')
plt.grid(False)

plt.show()                        

