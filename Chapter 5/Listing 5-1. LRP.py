# -*- coding: utf-8 -*-
"""
Listing 5-1. LRP
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians,sqrt

#------------------------------------------fill lists with starting coordinates
xg=[]
yg=[]
zg=[]

xc=80  #-----------------------center coordinates
yc=40
zc=40

x=[-40,-40,40,40,-40,50]
y=[0,0,0,0,-20,+5]
z=[-10,10,10,-10,15,-10]

for i in range(len(x)):
    xg.append(x[i]+xc)
    yg.append(y[i]+yc)
    zg.append(z[i]+zc)
    
#-----------------------------------------------------define rotation functions
def rotx(xc,yc,zc,xp,yp,zp,Rx):
    a=[xp,yp,zp]
    b=[1,0,0] #----------------------------------[cx11,cx12,cx13]
    xpp=np.inner(a,b)  #-----scalar product of a,b=xp*cx11+yp*cx12+ zp*cx13
    b=[0,cos(Rx),-sin(Rx)] #---------------[cx21,cx22,cx23]
    ypp=np.inner(a,b)
    b=[0,sin(Rx),cos(Rx)]  #---------------[cx31,cx32,cx33]
    zpp=np.inner(a,b)  
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
    return[xg,yg,zg]
    
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
    
def rotz(xc,yc,zc,xp,yp,zp,Rz):
    a=[xp,yp,zp]
    b=[cos(Rz),-sin(Rz),0] #-------------------[cx11,cx12,cx13]
    xpp=np.inner(a, b)
    b=[sin(Rz),cos(Rz),0] #---------------[cx21,cx22,cx23]
    ypp=np.inner(a,b) 
    b=[0,0,1]  #---------------[cx31,cx32,cx33]
    zpp=np.inner(a,b)  #---------------------scalar product of a,b
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
    return[xg,yg,zg]

#----------------------------------------------define system plotting functions 
def plotsystem(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')  #--------------plot plane
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='k')
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='k')   
    plt.plot([xg[4],xg[5]],[yg[4],yg[5]],color='b')     #--------plot line
    
    if hitcolor=='g':
        plt.scatter(xg[5],yg[5],s=20,color=hitcolor)
    else:               
        plt.scatter(xhg,yhg,s=20,color=hitcolor)    #----------------plot hit point
    
    plt.axis([0,150,100,0])            #--replot axes and grid
    plt.axis('on')
    plt.grid(False)
    plt.show()                         #--plot latest rotation
 
#-------------------------------------calculate hit point coordinates and color  
def hitpoint(x,y,z):
    a=x[5]-x[4]
    b=y[5]-y[4]
    c=z[5]-z[4]
    Q45=sqrt(a*a+b*b+c*c)  #-------distance point 4 to 5
    
    lx=a/Q45               #----unit vector components point 4 to 5
    ly=b/Q45
    lz=c/Q45
    
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    Q03=sqrt(a*a+b*b+c*c)  #---distance 0 to 3
    
    ux=a/Q03               #---unit vector 0 to 3
    uy=b/Q03
    uz=c/Q03
    
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    Q01=sqrt(a*a+b*b+c*c)  #---distance 0 to 1
    
    vx=a/Q01               #---unit vector 0 to 1
    vy=b/Q01
    vz=c/Q01
    
    nx=uy*vz-uz*vy         #---normal unit vector
    ny=uz*vx-ux*vz
    nz=ux*vy-uy*vx
    
    vx1b=x[4]-x[0]         #---vector components 0 to 4
    vy1b=y[4]-y[0]
    vz1b=z[4]-z[0]
    
    Qn=(vx1b*nx+vy1b*ny+vz1b*nz)   #---perpendiculat distance 4 to plane
        
    cosp=lx*nx+ly*ny+lz*nz    #---cos of angle p
    Qh=abs(Qn/cosp)           #---distance 4 to hit point
    
    xh=x[4]+Qh*lx           #---hit point coordinates
    yh=y[4]+Qh*ly
    zh=z[4]+Qh*lz
    
    xhg=xh+xc               #----global hit point coordinates
    yhg=yh+yc
    zhg=zh+zc

#-----------------------------------------------------------out of bounds check
    a=xh-x[0]            #---components of vector V0h
    b=yh-y[0]
    c=zh-z[0]
    
    up=a*ux+b*uy+c*uz    #---dot products
    vp=a*vx+b*vy+c*vz
           
    hitcolor='r'          #---if inbounds plot red hit point
    if up<0:              #---change color to blue if hit point out of bounds  
        hitcolor='b'      
        
    if up>Q03:
        hitcolor='b'
        
    if vp<0:
        hitcolor='b'
        
    if vp>Q01:
       hitcolor='b'
       
    a=x[5]-x[4]
    b=y[5]-y[4]
    c=z[5]-z[4]
    Q45=sqrt(a*a+b*b+c*c)
    if Q45 < Qh:
        hitcolor='g'
    
    return xh,yh,xhg,yhg,hitcolor      
        
#------------------------------------------------transform coordinates and plot   
def plotx(xc,yc,zc,Rx):   #---transform & plot Rx system
    for i in range(len(x)): 
        [xg[i],yg[i],zg[i]]=rotx(xc,yc,zc,x[i],y[i],z[i],Rx) #---transform
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]        #---replace 
        
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)    #---returns xh,yh,xhg,yhg
    
    plotsystem(xg,yg,zg,xh,yh,xhg,yhg,hitcolor) #---plot plane, line, hit point
                 
def ploty(xc,yc,zc,Ry):   #---transform & plot Ry system
    for i in range(len(x)):
        [xg[i],yg[i],zg[i]]=roty(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
        
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
        
    plotsystem(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)
                
def plotz(xc,yc,zc,Rz):   #---transform & plot Rz system
    for i in range(len(x)): 
        [xg[i],yg[i],zg[i]]=rotz(xc,yc,zc,x[i],y[i],z[i],Rz)        
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
        
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
        
    plotsystem(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)
        
#----------------------------------------------------input data and plot system
while True:
    axis=input('x, y or z?: ')          #---input axis of rotation (lower case)
    if axis == 'x':                     #---if x axis
        Rx=radians(float(input('Rx Degrees?: '))) #---input degrees of rotation
        plotx(xc,yc,zc,Rx)          #--call function plotx
    if axis == 'y':
        Ry=radians(float(input('Ry Degrees?: '))) #---input degrees of rotation
        ploty(xc,yc,zc,Ry)
    if axis == 'z':
        Rz=radians(float(input('Rz Degrees?: '))) #---input degrees of rotation        
        plotz(xc,yc,zc,Rz)
    if axis == '':
        break            #---quit the program
