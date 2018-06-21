# -*- coding: utf-8 -*-
"""
Listing 5-4. LCSTEST
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians, degrees, sqrt, acos

plt.axis([0,150,100,0])

plt.axis('on')
plt.grid(True)

x=[0,20,40,5]
y=[0,-35,0,-25]
z=[0,0,0,0]

xc=40
yc=60
zc=0
r=40

#-----------------------------------------hit test
a=x[3]-x[0]
b=y[3]-y[0]
c=z[3]-z[0]
rh=sqrt(a*a+b*b+c*c)

a=x[3]-x[0]
b=y[3]-y[0]
c=z[3]-z[0]
Q0h=sqrt(a*a+b*b+c*c)
hx=a/Q0h
hy=b/Q0h
hz=c/Q0h

a=x[2]-x[0]
b=y[2]-y[0]
c=z[2]-z[0]
Q02=sqrt(a*a+b*b+c*c)
ux=a/Q02
uy=b/Q02
uz=c/Q02

a=x[1]-x[0]
b=y[1]-y[0]
c=z[1]-z[0]
Q01=sqrt(a*a+b*b+c*c)
vx=a/Q01
vy=b/Q01
vz=c/Q01

a=uy*vz-uz*vy
b=uz*vx-ux*vz
c=ux*vy-uy*vx
Quxv=sqrt(a*a*b*b+c*c) #--- normalize uxv
nx=a/Quxv
ny=b/Quxv
nz=c/Quxv

uxnx=uy*nz-uz*ny
uxny=uz*nx-ux*nz
uxnz=ux*ny-uy*nx

A=uxnx*hx+uxny*hy+uxnz*hz

nxvx=ny*vz-nz*vy
nxvy=nz*vx-nx*vz
nxvz=nx*vy-ny*vx

B=nxvx*hx+nxvy*hy+nxvz* hz

hitcolor='r'
if A>0:             #---out
    hitcolor='b'
    
if B>0:             #---out
    hitcolor='b'
  
if rh>r:            #---out
    hitcolor='b'
    
print('rh=',rh)
print('r=',r)

plt.scatter(x[3]+xc,y[3]+yc,s=20,color=hitcolor) 
#-----------------------------------------
r=40
phi1=0
phi2=-radians(60)
dphi=(phi2-phi1)/180
xlast=xc+r
ylast=yc+0
for phi in np.arange(phi1,phi2,dphi):
    x=xc+r*cos(phi)
    y=yc+r*sin(phi)
    plt.plot([xlast,x],[ylast,y],color='k')
    xlast=x
    ylast=y

plt.arrow(xc,yc,40,0)

plt.arrow(xc,yc,20,-35,linewidth=.5,color='k')

plt.text(33,61,'0')
plt.text(52,27,'1')
plt.text(82,65,'2')

plt.show()

