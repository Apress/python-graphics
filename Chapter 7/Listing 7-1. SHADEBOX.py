# -*- coding: utf-8 -*-
"""
Listing 7-1. SHADEBOX
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians, sqrt

#-------------------------------------------------------------------------lists
x=[-20,20,20,-20,-20,20,20,-20]
y=[-10,-10,-10,-10,10,10,10,10]
z=[5,5,-5,-5,5,5,-5,-5]

xg=[0]*len(x)
yg=[0]*len(x)
zg=[0]*len(x)

#--------------------------------------------------------------------parameters
xc=75             #--center coordinates
yc=50
zc=50

lx=.707           #--light ray unit vector components
ly=.707
lz=0

clr='k'         #----use this for black monochrome images, or use another color
#clr=(.5,0,.5)  #----use this to mix colors, this mix produces purple
Io=.8           #----max intensity, must be 0 < 1

#=====================================================define rotation functions
def rotx(xc,yc,zc,xp,yp,zp,Rx):
    xpp=xp
    ypp=yp*cos(Rx)-zp*sin(Rx)
    zpp=yp*sin(Rx)+zp*cos(Rx)
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
    return[xg,yg,zg]
    
def roty(xc,yc,zc,xp,yp,zp,Ry):
    xpp=xp*cos(Ry)+zp*sin(Ry)
    ypp=yp
    zpp=-xp*sin(Ry)+zp*cos(Ry) 
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
    return[xg,yg,zg]
    
def rotz(xc,yc,zc,xp,yp,zp,Rz):
    xpp=xp*cos(Rz)-yp*sin(Rz)
    ypp=xp*sin(Rz)+yp*cos(Rz)
    zpp=zp
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
    return[xg,yg,zg]
    
#==============================================================shading function  
def shade(ax,ay,az,bx,by,bz,cx,cy,cz,dx,dy,dz):
    a=dx-ax
    b=dy-ay
    c=dz-az
    qad=sqrt(a*a+b*b+c*c)
    ux=a/qad
    uy=b/qad
    uz=c/qad
    a=bx-ax
    b=by-ay
    c=bz-az
    qab=sqrt(a*a+b*b+c*c)
    vx=a/qab
    vy=b/qab
    vz=c/qab
    nx=uy*vz-uz*vy
    ny=uz*vx-ux*vz
    nz=ux*vy-uy*vx
    ndotl=nx*lx+ny*ly+nz*lz
    I=.5*Io*(1+ndotl)
    if nz<=0:
        plt.plot([ax,bx],[ay,by],color='k',linewidth=1)
        plt.plot([bx,cx],[by,cy],color='k',linewidth=1)
        plt.plot([cx,dx],[cy,dy],color='k',linewidth=1)
        plt.plot([dx,ax],[dy,ay],color='k',linewidth=1)
        for h in np.arange(0,qad,1):
            xls=ax+h*ux
            yls=ay+h*uy
            xle=bx+h*ux
            yle=by+h*uy
            plt.plot([xls,xle],[yls,yle],linewidth=2,alpha=I,color=clr)
            
#=============================================================plotting function         
def plotbox(xg,yg,zg):
    shade(xg[0],yg[0],zg[0],xg[1],yg[1],zg[1],xg[2],yg[2],zg[2],xg[3],yg[3],zg[3])
    shade(xg[7],yg[7],zg[7],xg[6],yg[6],zg[6],xg[5],yg[5],zg[5],xg[4],yg[4],zg[4])
    shade(xg[0],yg[0],zg[0],xg[3],yg[3],zg[3],xg[7],yg[7],zg[7],xg[4],yg[4],zg[4])
    shade(xg[1],yg[1],zg[1],xg[5],yg[5],zg[5],xg[6],yg[6],zg[6],xg[2],yg[2],zg[2])
    shade(xg[3],yg[3],zg[3],xg[2],yg[2],zg[2],xg[6],yg[6],zg[6],xg[7],yg[7],zg[7])
    shade(xg[4],yg[4],zg[4],xg[5],yg[5],zg[5],xg[1],yg[1],zg[1],xg[0],yg[0],zg[0])
    
    plt.axis([0,150,100,0])            #--plot axes and grid
    plt.axis('off')
    plt.grid(False)
    plt.show()                         #--plot latest rotation

#============================================================rotation functions   
def plotboxx(xc,yc,zc,Rx):  #----------------transform & plot Rx 
    for i in range(len(x)): 
        [xg[i],yg[i],zg[i]]=rotx(xc,yc,zc,x[i],y[i],z[i],Rx) #--transform
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]        #--replace
        
    plotbox(xg,yg,zg)  #---------------plot
              
def plotboxy(xc,yc,zc,Ry):
    for i in range(len(x)): #-----------------transform & plot Ry 
        [xg[i],yg[i],zg[i]]=roty(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
        
    plotbox(xg,yg,zg)
                
def plotboxz(xc,yc,zc,Rz):
    for i in range(len(x)): #-----------------transform & plot Rz  
        [xg[i],yg[i],zg[i]]=rotz(xc,yc,zc,x[i],y[i],z[i],Rz)        
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
        
    plotbox(xg,yg,zg)
        
#-------------------------------------------------------------------------input
while True:
    axis=input('x, y or z?: ')           #--input axis of rotation (lower case)
    if axis == 'x':                      #--if x axis
        Rx=radians(float(input('Rx Degrees?: ')))    #--input degrees of rotation
        plotboxx(xc,yc,zc,Rx)          #--call function plotboxx
    if axis == 'y':
        Ry=radians(float(input('Ry Degrees?: ')))    #--input degrees of rotation
        plotboxy(xc,yc,zc,Ry)
    if axis == 'z':
        Rz=radians(float(input('Rz Degrees?: ')))    #--input degrees of rotation        
        plotboxz(xc,yc,zc,Rz)
    if axis == '':
        break


