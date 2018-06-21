# -*- coding: utf-8 -*-
"""
Listing 6-1. HLBOX
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians
#==================================================================define lists
x=[-20,20,20,-20,-20,20,20,-20]
y=[-10,-10,-10,-10,10,10,10,10]
z=[5,5,-5,-5,5,5,-5,-5]

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
    v01x=x[1]-x[0]    #---0,1,2,3 face
    v01y=y[1]-y[0]
    v01z=z[1]-z[0]
    v03x=x[3]-x[0]
    v03y=y[3]-y[0]
    v03z=z[3]-z[0]
    nz=v03x*v01y-v03y*v01x
    if nz<=0 :
        plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k',linewidth=2)
        plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k',linewidth=2)
        plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='k',linewidth=2)
        plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='k',linewidth=2)
    else:
        #----plot the other side
        plt.plot([xg[4],xg[5]],[yg[4],yg[5]],color='k',linewidth=2)
        plt.plot([xg[5],xg[6]],[yg[5],yg[6]],color='k',linewidth=2)
        plt.plot([xg[6],xg[7]],[yg[6],yg[7]],color='k',linewidth=2)
        plt.plot([xg[7],xg[4]],[yg[7],yg[4]],color='k',linewidth=2)
    
    v04x=x[4]-x[0]    #---0,3,7,4 face
    v04y=y[4]-y[0]
    v04z=z[4]-z[0]
    v03x=x[3]-x[0]
    v03y=y[3]-y[0]
    v03z=z[3]-z[0]
    nz=v04x*v03y-v04y*v03x
    if nz<=0 :
        plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='k',linewidth=2)
        plt.plot([xg[3],xg[7]],[yg[3],yg[7]],color='k',linewidth=2)
        plt.plot([xg[7],xg[4]],[yg[7],yg[4]],color='k',linewidth=2)
        plt.plot([xg[4],xg[0]],[yg[4],yg[0]],color='k',linewidth=2)
    else:
        #----plot the other side
        plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k',linewidth=2)
        plt.plot([xg[2],xg[6]],[yg[2],yg[6]],color='k',linewidth=2)
        plt.plot([xg[6],xg[5]],[yg[6],yg[5]],color='k',linewidth=2)
        plt.plot([xg[5],xg[1]],[yg[5],yg[1]],color='k',linewidth=2)
    
    v01x=x[1]-x[0]    #---0,1,5,4 face
    v01y=y[1]-y[0]
    v01z=z[1]-z[0]
    v04x=x[4]-x[0]
    v04y=y[4]-y[0]
    v04z=z[4]-z[0]
    nz=v01x*v04y-v01y*v04x
    if nz<=0 :
        plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k',linewidth=2)
        plt.plot([xg[1],xg[5]],[yg[1],yg[5]],color='k',linewidth=2)
        plt.plot([xg[5],xg[4]],[yg[5],yg[4]],color='k',linewidth=2)
        plt.plot([xg[4],xg[0]],[yg[4],yg[0]],color='k',linewidth=2)
    else:
        #----plot the other side
        plt.plot([xg[3],xg[2]],[yg[3],yg[2]],color='k',linewidth=2)
        plt.plot([xg[2],xg[6]],[yg[2],yg[6]],color='k',linewidth=2)
        plt.plot([xg[6],xg[7]],[yg[6],yg[7]],color='k',linewidth=2)
        plt.plot([xg[7],xg[3]],[yg[7],yg[3]],color='k',linewidth=2 )
    
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


