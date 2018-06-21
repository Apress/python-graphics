# -*- coding: utf-8 -*-
"""
Listing 9-3. SHADEDSURFACE3D
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, radians, sin, cos
from mpl_toolkits.mplot3d import Axes3D

plt.axis([0,150,0,100])
plt.axis('on')
plt.grid(True)
  
#======================================================rotation transformations 
def rotx(xp,yp,zp,Rx):
    g[0]=xp+xc
    g[1]=yp*cos(Rx)-zp*sin(Rx)+yc
    g[2]=yp*sin(Rx)+zp*cos(Rx)+zc
    return[g]      
        
def roty(xp,yp,zp,Ry):
    g[0]=xp*cos(Ry)+zp*sin(Ry)+xc
    g[1]=yp+yc
    g[2]=-xp*sin(Ry)+zp*cos(Ry)+zc
    return[g]      
    
def rotz(xp,yp,zp,Rz):
    g[0]=xp*cos(Rz)-yp*sin(Rz)+xc
    g[1]=xp*sin(Rz)+yp*cos(Rz)+yc
    g[2]=zp+zc
    return[g]   
    
#=====================================================================plot axis                          
def plotaxis(xp,yp,zp,Rx,Ry,Rz):    
    rotx(xp,yp,zp,Rx)  #---Rx rotation
    xp=g[0]-xc
    yp=g[1]-yc
    zp=g[2]-zc
    roty(xp,yp,zp,Ry)   #---Ry rotation
    xp=g[0]-xc
    yp=g[1]-yc
    zp=g[2]-zc
    rotz(xp,yp,zp,Rz)   #---Rz rotation
    return[g]
        
#===================================================================plot point
def plotpoint(xp,yp,zp,Rx,Ry,Rz,clr):
     rotx(xp,yp,zp,Rx)
     xp=g[0]-xc
     yp=g[1]-yc
     zp=g[2]-zc
     roty(xp,yp,zp,Ry)
     xp=g[0]-xc
     yp=g[1]-yc 
     zp=g[2]-zc
     rotz(xp,yp,zp,Rz)
     plt.scatter(g[0],g[1],s=10,color=clr) 
        
#===================================================================plot line
def plotline(xb,yb,zb,xe,ye,ze,Rx,Ry,Rz,clr):
    rotx(xb,yb,zb,Rx)  #---rotate line beginning coordinates
    xb=g[0]-xc
    yb=g[1]-yc
    zb=g[2]-zc
    roty(xb,yb,zb,Ry)   
    xb=g[0]-xc
    yb=g[1]-yc
    zb=g[2]-zc
    rotz(xb,yb,zb,Rz)   
    xb=g[0]
    yb=g[1]
    zb=g[2]
    
    rotx(xe,ye,ze,Rx)  #---rotate line end coordinates
    xe=g[0]-xc
    ye=g[1]-yc
    ze=g[2]-zc
    roty(xe,ye,ze,Ry)   
    xe=g[0]-xc
    ye=g[1]-yc
    ze=g[2]-zc
    rotz(xe,ye,ze,Rz)   
    xe=g[0]
    ye=g[1]
    ze=g[2]
    
    plt.plot([xb,xe],[yb,ye],linewidth=.7,color=clr)
    
#=========================================================================shade
def shade(x0,y0,z0,x1,y1,z1,x2,y2,z2,x3,y3,z3,Rx,Ry,Rz,clr):
    a=x3-x0
    b=y3-y0
    c=z3-z0                           
    q03=np.sqrt(a*a+b*b+c*c)
    ux=a/q03
    uy=b/q03
    uz=c/q03
    
    a=x1-x0
    b=y1-y0
    c=z1-z0
    q02=sqrt(a*a+b*b+c*c)
    vx=a/q02
    vy=b/q02
    vz=c/q02
    
    a=x2-x1
    b=y2-y1
    c=z2-z1
    q12=np.sqrt(a*a+b*b+c*c)
    wx=a/q12
    wy=b/q12
    wz=c/q12
    
    nx=uy*vz-uz*vy
    ny=uz*vx-ux*vz
    nz=ux*vy-uy*vx
    
    lx=0
    ly=-.7
    lz=0
    
    ndotl=nx*lx+ny*ly+nz*lz
       
    IA=.01
    IB=1
    n=2.8
    I=IA+(IB-IA)*((1-ndotl)/2)**n 
    
    clr=(1-I,.4*(1-I),.6*(1-I))
    
    r=q12/q03
    dq=q03/50
    for q in np.arange(0,q03+1,dq):
        xb=x0+ux*q
        yb=y0+uy*q
        zb=z0+uz*q
        xe=x1+wx*q*r
        ye=y1+wy*q*r
        ze=z1+wz*q*r
        
        plotline(xb,yb,zb,xe,ye,ze,Rx,Ry,Rz,clr)
        
    plt.text(121,70,'lx=')
    lx='%7.3f'%(lx)
    plt.text(130,70,lx)
    
    plt.text(121,65,'ly=')
    ly='%7.3f'%(ly)
    plt.text(130,65,ly)
    
    plt.text(121,60,'lz=')
    lz='%7.3f'%(lz)
    plt.text(130,60,lz)
    
    plt.text(121,50,'IA=')
    IA='%7.3f'%(IA)
    plt.text(130,50,IA)
    
    plt.text(121,45,'IB=')
    IB='%7.3f'%(IB)
    plt.text(130,45,IB)
    
    plt.text(121,40,'n=')
    n='%7.3f'%(n)
    plt.text(130,40,n)
    
#=======================================================================control  
g=[0]*3      #---global plotting coords returned by rotx, roty and rotz 

xc=80                       #---origin of X,Y,Z coordinate system
yc=20
zc=10

Rxd=-100     #--rotations of X,Y,Z system degrees
Ryd=-135
Rzd=8

Rx=radians(Rxd)    #---rotations of X,Y,Z system radians
Ry=radians(Ryd)
Rz=radians(Rzd)

#---------------------------------------------------------------plot X,Y,Z axes
plotaxis(60,0,0,Rx,Ry,Rz)   #---plot X axis
plt.plot([xc,g[0]],[yc,g[1]],linewidth=2,color='k')
plt.text(g[0]-5,g[1]-1,'X')

plotaxis(0,60,0,Rx,Ry,Rz)   #---plot Y axis
plt.plot([xc,g[0]],[yc,g[1]],linewidth=2,color='k')
plt.text(g[0],g[1]-5,'Y') 

plotaxis(0,0,60,Rx,Ry,Rz)   #---plot Z axis
plt.plot([xc,g[0]],[yc,g[1]],linewidth=2,color='k')
plt.text(g[0]-2,g[1]+3,'Z') 
 
#-------------------------define 4 sets of data points at different values of X           
A=np.array([ [0,0,50], [0,10,43], [0,20,30], [0,30,14],
             [20,0,25],[20,10,23],[20,20,19],[20,30,12],
             [40,0,14],[40,10,15],[40,20,13],[40,30,9],
             [60,0,7],[60,10,10],[60,20,10],[60,30,9] ])
             
nop=len(A)

#--------------------------------------------------------------plot data points
clr='k'
for i in range(0,16):
    plotpoint(A[i,0],A[i,1],A[i,2],Rx,Ry,Rz,clr)

#--------------------------------------------connect data points in Y direction
clr='k'  #-----------------------------line color
for i in range(0,3):
   plotline(A[i,0],A[i,1],A[i,2],A[i+1,0],A[i+1,1],A[i+1,2],Rx,Ry,Rz,clr)
for i in range(4,7):
    plotline(A[i,0],A[i,1],A[i,2],A[i+1,0],A[i+1,1],A[i+1,2],Rx,Ry,Rz,clr)
for i in range(8,11):
    plotline(A[i,0],A[i,1],A[i,2],A[i+1,0],A[i+1,1],A[i+1,2],Rx,Ry,Rz,clr)
for i in range(12,15):
    plotline(A[i,0],A[i,1],A[i,2],A[i+1,0],A[i+1,1],A[i+1,2],Rx,Ry,Rz,clr)

#--------------------------------------------connect data points in X direction
clr='k'   #----------------------------line color
for i in range(0,4):
    plotline(A[i,0],A[i,1],A[i,2],A[i+4,0],A[i+4,1],A[i+4,2],Rx,Ry,Rz,clr)
for i in range(4,8):
    plotline(A[i,0],A[i,1],A[i,2],A[i+4,0],A[i+4,1],A[i+4,2],Rx,Ry,Rz,clr)
for i in range(8,12):
    plotline(A[i,0],A[i,1],A[i,2],A[i+4,0],A[i+4,1],A[i+4,2],Rx,Ry,Rz,clr)

#-----------------------------------------------------------------shade patches
for i in range(0,3):
    shade(A[i,0],A[i,1],A[i,2],A[i+1,0],A[i+1,1],A[i+1,2],A[i+5,0],A[i+5,1],
          A[i+5,2],A[i+4,0],A[i+4,1],A[i+4,2],Rx,Ry,Rz,clr)
for i in range(4,7):
    shade(A[i,0],A[i,1],A[i,2],A[i+1,0],A[i+1,1],A[i+1,2],A[i+5,0],A[i+5,1],
          A[i+5,2],A[i+4,0],A[i+4,1],A[i+4,2],Rx,Ry,Rz,clr)          
for i in range(8,11):
    shade(A[i,0],A[i,1],A[i,2],A[i+1,0],A[i+1,1],A[i+1,2],A[i+5,0],A[i+5,1],
          A[i+5,2],A[i+4,0],A[i+4,1],A[i+4,2],Rx,Ry,Rz,clr)  

#------------------------------------------------------------------------labels
plt.text(121,90,'Rx=')
Rxd='%7.1f'%(Rxd)
plt.text(130,90,Rxd)

plt.text(121,85,'Ry=')
Ryd='%7.1f'%(Ryd)
plt.text(130,85,Ryd)

plt.text(121,80,'Rz=')
Rzd='%7.1f'%(Rzd)
plt.text(130,80,Rzd)

plt.title('Shaded 3D Surface')

plt.show()






