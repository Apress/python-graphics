# -*- coding: utf-8 -*-
"""
Listing 3-5. KEYBOARDDATAENTRY
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians
#==================================================================define lists
x=[]
y=[]
z=[]

xg=[]
yg=[]
zg=[]

#------------------------------------------fill lists with starting coordinates
phi1=radians(0)
phi2=radians(360)
dphi=radians(5)    #--circumferential points spaced 5 degrees

radius=15                #--circle's radius

for phi in np.arange(phi1,phi2+dphi,dphi): #--establish coordinates of circle's
    xp=radius*cos(phi)                       #--circumferential points.
    yp=radius*sin(phi)
    zp=0
    x.append(xp)           #--fill lists
    y.append(yp)
    z.append(zp)
    xg.append(xp)
    yg.append(yp)
    zg.append(zp)

#=====================================================define rotation functions
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

#===============================================define circle plotting function 
def plotcircle(xg,yg,zg):
    lastxg=xg[0]
    lastyg=yg[0]
    for i in range(len(x)):   #--for i in range(len(x)): ok too
        if i < len(x)/2:        #-----half green
            plt.plot([lastxg,xg[i]],[lastyg,yg[i]],linewidth=1 ,color='g')
        else:                   
            plt.plot([lastxg,xg[i]],[lastyg,yg[i]],linewidth=1 ,color='r')
        lastxg=xg[i]
        lastyg=yg[i]
 
    plt.scatter(xc,yc,s=5,color='k')   #--plot a dot at the center
    plt.axis([0,150,100,0])            #--replot axes and grid
    plt.axis('on')
    plt.grid(True)
    plt.show()                         #--plot latest rotation

#================================================transform coordinates and plot   
def plotcirclex(xc,yc,zc,Rx):  #----------------transform & plot Rx circle
    for i in range(len(x)): 
        [xg[i],yg[i],zg[i]]=rotx(xc,yc,zc,x[i],y[i],z[i],Rx) #--transform
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]        #--replace
        
    plotcircle(xg,yg,zg)  #---------------plot
              
def plotcircley(xc,yc,zc,Ry):
    for i in range(len(x)): #-----------------transform & plot Ry circle
        [xg[i],yg[i],zg[i]]=roty(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
        
    plotcircle(xg,yg,zg)
                
def plotcirclez(xc,yc,zc,Rz):
    for i in range(len(x)): #-----------------transform & plot Rz circle
        [xg[i],yg[i],zg[i]]=rotz(xc,yc,zc,x[i],y[i],z[i],Rz)        
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
        
    plotcircle(xg,yg,zg)
        
#==================================================================plot circles
xc=75             #--center coordinates
yc=50
zc=50

while True:
    axis=input('x, y or z?: ')           #--input axis of rotation (lower case)
    if axis == 'x':                      #--if x axis
        Rx=radians(float(input('Rx Degrees?: ')))    #--input degrees of rotation
        plotcirclex(xc,yc,zc,Rx)          #--call function plotcirclex
    if axis == 'y':
        Ry=radians(float(input('Ry Degrees?: ')))    #--input degrees of rotation
        plotcircley(xc,yc,zc,Ry)
    if axis == 'z':
        Rz=radians(float(input('Rz Degrees?: ')))    #--input degrees of rotation        
        plotcirclez(xc,yc,zc,Rz)
    if axis == '':
        break
