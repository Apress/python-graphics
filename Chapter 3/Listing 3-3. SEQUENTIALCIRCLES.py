# -*- coding: utf-8 -*-
"""
Listing 3-3. SEQUENTIALCIRCLES
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians

plt.axis([0,150,100,0])
plt.axis('on')
plt.grid(True)

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

r=10                #--circle's radius

for phi in np.arange(phi1,phi2+dphi,dphi): #--establish coordinates of circle's
    xp=r*cos(phi)                       #--circumferential points.
    yp=r*sin(phi)
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
 
    plt.scatter(xc,yc,s=5)   #--plot a dot at the center
      
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
#---------------------------------------------------starting circle, un-rotated
xc=25  #---------------circle (a) center coordinates
yc=40
zc=20
Rx=radians(0)
plotcirclex(xc,yc,zc,Rx)  #--since R=0 we could use plotcircley or plotcirclez

#-----------------------------------------------------------------Rx circle (b)
Rx=radians(45)
xc=55
yc=40
zc=20
plotcirclex(xc,yc,zc,Rx)

#-----------------------------------------------------------------Ry circle (c)
Ry=radians(70)
xc=85
yc=40
zc=20
plotcircley(xc,yc,zc,Ry)
    
#-----------------------------------------------------------------Rz circle (d)
Rz=radians(90)
xc=115
yc=40
zc=20
plotcirclez(xc,yc,zc,Rz)

#=========================================================================notes
plt.text(23,63,'(a)')
plt.text(53,63,'(b)')
plt.text(83,63,'(c)')
plt.text(112,63,'(d)')
plt.text(21,73,'R=0')
plt.text(47,73,'Rx=45$^{\circ}$')
plt.text(77,73,'Ry=70$^{\circ}$')
plt.text(107,73,'Rz=90$^{\circ}$')
plt.arrow(42,40,25,0,head_width=2,head_length=3,color='r') #--red arrows
plt.arrow(42,40,28,0,head_width=2,head_length=3,color='r')
plt.arrow(85,25,0,27,head_width=2,head_length=2,color='r')
plt.arrow(85,25,0,29,head_width=2,head_length=2,color='r')
plt.plot([8,130],[8,8],color='k')                          #--axes
plt.plot([8,8],[8,85],color='k')
plt.text(120,6,'X')  #X and Y indicate directions, grid gives coordinate values
plt.text(3,80,'Y')
plt.scatter(115,40,s=30,color='r') #-----------red dot center of box (d)

plt.show()





