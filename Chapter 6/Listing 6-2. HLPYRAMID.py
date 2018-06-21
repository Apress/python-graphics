# -*- coding: utf-8 -*-
"""
Listing 6-2. HLPYRAMID
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians
#==================================================================define lists
x=[0,-10,0,10]
y=[-20,0,0,0]
z=[0,10,-15,10]

xg=[0]*len(x)
yg=[0]*len(x)
zg=[0]*len(x)

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

#===============================================define box plotting function 
def plotbox(xg,yg,zg):
    v01x=x[1]-x[0]    #---0,1,2 face
    v01y=y[1]-y[0]
    v01z=z[1]-z[0]
    v02x=x[2]-x[0]
    v02y=y[2]-y[0]
    v02z=z[2]-z[0]
    nz=v01x*v02y-v01y*v02x
    if nz<=0 :
        plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k',linewidth=2)
        plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k',linewidth=2)
        plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k',linewidth=2)
    else:    
        plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k',linestyle=':')
        plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k',linestyle=':')
        plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k',linestyle=':')
            
    v03x=x[3]-x[0]  #---0,2,3 face
    v03y=y[3]-y[0]
    v03z=z[3]-z[0]
    nz=v02x*v03y-v02y*v03x
    if nz<=0 :
        plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='k',linewidth=2)
        plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='k',linewidth=2)
        plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='k',linewidth=2)
    else:
        plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='k',linestyle=':')
        plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='k',linestyle=':')
        plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='k',linestyle=':')
                
    nz=v03x*v01y-v03y*v01x  #---0,2,3 face
    if nz<=0 :
        plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k',linewidth=2)
        plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='k',linewidth=2)
        plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='k',linewidth=2)
    else:
        plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k',linestyle=':')
        plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='k',linestyle=':')
        plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='k',linestyle=':')
       
        
    v21x=x[1]-x[2]  #---1,2,3 face
    v21y=y[1]-y[2]
    v21z=z[1]-z[2]
    v23x=x[3]-x[2]
    v23y=y[3]-y[2]
    v23z=z[3]-z[2]
    nz=v21x*v23y-v21y*v23x
    if nz<0:
        plt.plot([xg[2],xg[1]],[yg[2],yg[1]],color='k',linewidth=2)
        plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='k',linewidth=2)
        plt.plot([xg[3],xg[2]],[yg[3],yg[2]],color='k',linewidth=2)
    else:
        plt.plot([xg[2],xg[1]],[yg[2],yg[1]],color='k',linestyle=':')
        plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='k',linestyle=':')
        plt.plot([xg[3],xg[2]],[yg[3],yg[2]],color='k',linestyle=':')

    plt.scatter(xc,yc,s=5,color='k')   #--plot a dot at the center
    plt.axis([0,150,100,0])            #--replot axes and grid
    plt.axis('on')
    plt.grid(True)
    plt.show()                         #--plot latest rotation

#================================================transform coordinates and plot   
def plotboxx(xc,yc,zc,Rx):  #----------------transform & plot Rx circle
    for i in range(len(x)): 
        [xg[i],yg[i],zg[i]]=rotx(xc,yc,zc,x[i],y[i],z[i],Rx) #--transform
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]        #--replace
        
    plotbox(xg,yg,zg)  #---------------plot
              
def plotboxy(xc,yc,zc,Ry):
    for i in range(len(x)): #-----------------transform & plot Ry circle
        [xg[i],yg[i],zg[i]]=roty(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
        
    plotbox(xg,yg,zg)
                
def plotboxz(xc,yc,zc,Rz):
    for i in range(len(x)): #-----------------transform & plot Rz circle
        [xg[i],yg[i],zg[i]]=rotz(xc,yc,zc,x[i],y[i],z[i],Rz)        
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
        
    plotbox(xg,yg,zg)
        
#==================================================================plot circles
xc=75             #--center coordinates
yc=50
zc=50

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



