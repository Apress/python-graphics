# -*- coding: utf-8 -*-
"""
Listing 5-6. PS
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians, sqrt
#==================================================================define lists
x=[]
y=[]
z=[]

xg=[]
yg=[]
zg=[]

#------------------------------------------fill longitudes

rs=40
phi1=radians(0)
phi2=radians(360)
dphi=radians(10)    #--surface points spaced 5 degrees

Ry1=0
Ry2=radians(180)
dRy=radians(10)

for phi in np.arange(phi1,phi2+dphi,dphi): #--establish coordinates of sphere's
        xp=rs*cos(phi)                       #--longitudinal surface points.
        yp=rs*sin(phi)
        zp=0  
        x.append(xp)           #--fill lists
        y.append(yp)
        z.append(zp)
        xg.append(xp)
        yg.append(yp)
        zg.append(zp)
        
#=====================================================define rotation function
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
    
#-------------------------------------------------plot latitudes
xc=80               #sphere center
yc=50
zc=100    
rs=40               #--sphere's radius

Ry1=radians(0)
Ry2=radians(180)
dRy=radians(10  )

for Ry in np.arange(Ry1,Ry2,dRy):
    plotspherey(xc,yc,zc,Ry)
    
alpha1=radians(0)
alpha2=radians(180)
dalpha=radians(10)

phi1=radians(-90)
phi2=radians(90)
dphi=radians(10)  

for phi in np.arange(phi1,phi2,dphi):
    r=rs*cos(phi)   #---latitude circle radius
    xplast=xc+r
    yplast=yc+rs*sin(phi)
    for alpha in np.arange(alpha1,alpha2,dalpha):
        xp=xc+r*cos(alpha)
        yp=yc+rs*sin(phi)
        plt.plot([xplast,xp],[yplast,yp],color='k')
        xplast=xp
        yplast=yp

#-------------------------------------------------hits       
def plane(xb,yb,zb,xe,ye,ze,Q12,dt):
    hit='off'
    for t in np.arange(0,Q12,dt):    #---B to hit
        xp=xb+ux*t
        yp=yb+uy*t
        zp=zb+uz*t
        xpg=xc+xp
        ypg=yc+yp
        zpg=zc+zp
        Qpc=sqrt(xp*xp+yp*yp+zp*zp)
        if Qpc>=rs:
            plt.scatter(xpg,ypg,s=.5,color='k')
        if Qpc<=rs:
            if hit=='off':
                hit='on'
        if Qpc<rs:
            if hit=='on':
                plt.scatter(xpg,ypg,s=10,color='')
        if Qpc>=rs:
            if hit=='on':
                hit='off'
        if Qpc>rs:
            if hit=='off':
                plt.scatter(xpg,ypg,s=.5,color='k')  
        
#--------------------------------------------------------scan across plane  
x1=-40
y1=-30
z1=-20

x2=60
y2=25
z2=-35

x3=-65
y3=-20
z3=-50

a=x2-x1
b=y2-y1
c=z2-z1
Q12=sqrt(a*a+b*b+c*c)
ux=a/Q12
uy=b/Q12
uz=c/Q12
     
a=x3-x1
b=y3-y1
c=z3-z1
Q13=sqrt(a*a+b*b+c*c)
vx=a/Q13
vy=b/Q13
vz=c/Q13

dt=.7   #-----------------------------------scan increment  
ds=.7
for s in np.arange(0,Q13,ds):
    sbx=x1+s*vx
    sby=y1+s*vy
    sbz=z1+s*vz
    sex=x2+s*vx
    sey=y2+s*vy
    sez=z2+s*vz
    plane(sbx,sby,sbz,sex,sey,sez,Q12,dt)
   
plt.axis([0,150,100,0])            #--replot axes and grid
plt.axis('off')
plt.grid(False)

plt.show()                         #--plot latest rotation

