# -*- coding: utf-8 -*-
"""
Listing 10-1. SATURN
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians, sqrt

plt.axis([0,150,100,0])
plt.axis('off')
plt.grid(False)

print('running')
#-------------------------------------------------------------------------lists
g=[0]*3

xc=80               #---sphere center
yc=50
zc=0

rs=25               #---sphere radius

lx=1             #---light ray unit vector components
ly=0
lz=0

IA=0
IB=.8
n=2

Rx=radians(-20) 
Ry=radians(0)
Rz=radians(-20)

#--------------------------------------------------------------background color
print('background color')

clrbg='midnightblue'

for x in range(0,150,1):
    for y in range(0,100,1):
        plt.scatter(x,y,s=50,color='midnightblue')
        
#============================================================rotation functions
def rotx(xc,yc,zc,xp,yp,zp,Rx):
    g[0]=xp+xc
    g[1]=yp*cos(Rx)-zp*sin(Rx)+yc
    g[2]=yp*sin(Rx)+zp*cos(Rx)+zc
    return[g]
    
def roty(xc,yc,zc,xp,yp,zp,Ry):
    g[0]=xp*cos(Ry)+zp*sin(Ry)+xc
    g[1]=yp+yc
    g[2]=-xp*sin(Ry)+zp*cos(Ry)+zc
    return[g]
    
def rotz(xc,yc,zc,xp,yp,zp,Rz):
    g[0]=xp*cos(Rz)-yp*sin(Rz)+xc
    g[1]=xp*sin(Rz)+yp*cos(Rz)+yc
    g[2]=zp+zc
    return[g]
    
#----------------------------------------------------------longitudes
print('longitudes')

phi1=radians(-92)
phi2=radians(92)
dphi=radians(2)

alpha1=radians(0)
alpha2=radians(360)
dalpha=radians(.5)

for alpha in np.arange(alpha1,alpha2+dalpha,dalpha):  #----longitudes
    for phi in np.arange(phi1,phi2+dphi,dphi):
        xp=rs*cos(phi)*cos(alpha)
        yp=rs*sin(phi)
        zp=-rs*cos(phi)*sin(alpha)
        rotx(xc,yc,zc,xp,yp,zp,Rx)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        roty(xc,yc,zc,xp,yp,zp,Ry)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        rotz(xc,yc,zc,xp,yp,zp,Rz)
        xpg=g[0]
        ypg=g[1]
        zpg=g[2]
        a=xpg-xc
        b=ypg-yc
        c=zpg-zc
        qp=sqrt(a*a+b*b+c*c)
        nx=a/qp
        ny=b/qp
        nz=c/qp
        ndotl=nx*lx+ny*ly+nz*lz
        I=IA+(IB-IA)*((1+ndotl)/2)**n
        if phi == phi1:
            xpglast=xpg
            ypglast=ypg
        if nz < 0:
            plt.plot([xpglast,xpg],[ypglast,ypg],linewidth=4,color=(.95*(1-I),.85*(1-I),.1*(1-I)))
        xpglast=xpg
        ypglast=ypg

print('latitudes')

for phi in np.arange(phi1,phi2+dphi,dphi):   #----latitudes
    r=rs*cos(phi)
    for alpha in np.arange(alpha1,alpha2+dalpha,dalpha):
        xp=r*cos(alpha)
        yp=rs*sin(phi)
        zp=-rs*cos(phi)*sin(alpha)        
        rotx(xc,yc,zc,xp,yp,zp,Rx)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        roty(xc,yc,zc,xp,yp,zp,Ry)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        rotz(xc,yc,zc,xp,yp,zp,Rz)
        xpg=g[0]
        ypg=g[1]
        zpg=g[2]
        a=xpg-xc
        b=ypg-yc   
        c=zpg-zc
        qp=sqrt(a*a+b*b+c*c)
        nx=a/qp
        ny=b/qp
        nz=c/qp
        ndotl=nx*lx+ny*ly+nz*lz
        I=IA+(IB-IA)*((1+ndotl)/2)**n
        if alpha == alpha1:
            xpglast=xpg
            ypglast=ypg
        if nz < 0:
            plt.plot([xpglast,xpg],[ypglast,ypg],linewidth=4,color=(.95*(1-I),.85*(1-I),.1*(1-I)))
        xpglast=xpg
        ypglast=ypg  

#------------------------------------------------------rings
print('rings and shadow')

alpha1=radians(-10)
alpha2=radians(370)
dalpha=radians(.5)

r1=rs*1.5
r2=rs*2.2
dr=rs*.02
deltar=(r2-r1)/7

for r in np.arange(r1,r2,dr): 
    for alpha in np.arange(alpha1,alpha2,dalpha):
        xp=r*cos(alpha)
        yp=0
        zp=-r*sin(alpha)
        rotx(xc,yc,zc,xp,yp,zp,Rx)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        roty(xc,yc,zc,xp,yp,zp,Ry)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        rotz(xc,yc,zc,xp,yp,zp,Rz)
        xpg=g[0]
        ypg=g[1]
        zpg=g[2]

#-------------------------------------------------------------------ring colors  
        if r1 <= r < r1+1*deltar:
            clr=(.63,.54,.18)
        if r1+1*deltar <= r <= r1+2*deltar:
            clr=(.78,.7,.1)
        if r1+2*deltar <= r <= r1+3*deltar:
            clr=(.95,.85,.1)
        if r1+3*deltar <= r <= r1+4*deltar:
            clr=(.87,.8,.1)
        if r1+5*deltar <= r <= r1+7*deltar:
            clr=(.7,.6,.2)

#-------------------------------------------------------------------shadow                
        magu=sqrt(lx*lx+ly*ly+lz*lz)
        ux=-lx/magu
        uy=-ly/magu
        uz=-lz/magu
        vx=xc-xpg
        vy=yc-ypg
        vz=zc-zpg
        Bx=uy*vz-uz*vy
        By=uz*vx-ux*vz
        Bz=ux*vy-uy*vx
        magB=sqrt(Bx*Bx+By*By+Bz*Bz)
        if magB < rs:   #-------------------------if in the shadow region
            if vx*lx+vy*ly+vz*lz <= 0:    #---if v pointing toward light source
               clr=(.5,.5,.2)             #---shadow color
                
        if r1+4*deltar <= r <= r1+5*deltar:  #---overplot with background color
            clr='midnightblue'
        
#--------------------------------------------------------plot line segment 
        if alpha == alpha1:
            xstart=xpg
            ystart=ypg            
        if zpg <= zc:        #---front
            plt.plot([xstart,xpg],[ystart,ypg],linewidth=2,color=clr)  
        if zpg >= zc:        #--back
            a=xpg-xc
            b=ypg-yc
            c=sqrt(a*a+b*b)
            if c > rs*1.075: #------plot only visible portion of rings
                 plt.plot([xstart,xpg],[ystart,ypg],linewidth=2,color=clr)
        xstart=xpg
        ystart=ypg
        
plt.show()                        





