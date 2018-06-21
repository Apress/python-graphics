# -*- coding: utf-8 -*-
"""
Listing 3-2. 4BOXESUPDATE
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians

plt.axis([0,150,100,0])
plt.axis('on')
plt.grid(True)

#=========================================================================lists 
x=[-10,-10,10,10,-10,-10,10,10] #--unrotated corner coordinates
y=[-10,-10,-10,-10,10,10,10,10] #--relative to box's center
z=[ -3,  3,  3, -3,-3, 3, 3,-3]

xg=[0,1,2,3,4,5,6,7]  #--define global coordinates
yg=[0,1,2,3,4,5,6,7]
zg=[0,1,2,3,4,5,6,7]

#===============================================define rotation transformations
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
    
def plotbox(xg,yg,zg):
    for i in (0,1,2):   #----------------------------------------------plot top
        plt.plot([xg[i],xg[i+1]],[yg[i],yg[i+1]],linewidth=3,color='k')
 
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],linewidth=3,color='k') #-close top

    for i in (4,5,6):   #-------------------------------------------plot bottom
        plt.plot([xg[i],xg[i+1]],[yg[i],yg[i+1]],linewidth=3,color='k')
        
    plt.plot([xg[7],xg[4]],[yg[7],yg[4]],linewidth=3,color='k') #--close bottom

    for i in (0,1,2,3):   #------------------------------------------plot sides  
       plt.plot([xg[i],xg[i-4]],[yg[i],yg[i-4]],linewidth=1,color='k') 
 
    plt.scatter(xc,yc,s=5)   #--plot a dot at the center
    
def plotboxx(xc,yc,zc,Rx):
    for i in (0,1,2,3,4,5,6,7): #--------------------------rotate eight corners
        [xg[i],yg[i],zg[i]]=rotx(xc,yc,zc,x[i],y[i],z[i],Rx)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
        
    plotbox(xg,yg,zg)
           
def plotboxy(xc,yc,zc,Ry):
    for i in (0,1,2,3,4,5,6,7): #--------------------------rotate eight corners
        [xg[i],yg[i],zg[i]]=roty(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
        
    plotbox(xg,yg,zg)
            
def plotboxz(xc,yc,zc,Rz):
    for i in (0,1,2,3,4,5,6,7): #--------------------------rotate eight corners
        [xg[i],yg[i],zg[i]]=rotz(xc,yc,zc,x[i],y[i],z[i],Rz)    
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
           
    plotbox(xg,yg,zg)

#====================================================================R=0 box(a)
Rx=radians(0)
xc=25  #---------------box (a) center coordinates
yc=40
zc=20
plotboxx(xc,yc,zc,Rx)  #--since R=0 we could use plotboxy or plotboxz

#---------------------------------------------------------------------Rx box(b)
Rx=radians(45)
xc=55
yc=40
zc=20
plotboxx(xc,yc,zc,Rx)

#--------------------------------------------------------------------Ry box (c)
Ry=radians(30)
xc=85
yc=40
zc=20
plotboxy(xc,yc,zc,Ry)
    
#--------------------------------------------------------------------Rz box (d)
Rz=radians(30)
xc=115
yc=40
zc=20
plotboxz(xc,yc,zc,Rz)

#=========================================================================notes
plt.text(23,63,'(a)')
plt.text(53,63,'(b)')
plt.text(83,63,'(c)')
plt.text(112,63,'(d)')
plt.text(21,73,'R=0')
plt.text(47,73,'Rx=45$^{\circ}$')
plt.text(77,73,'Ry=30$^{\circ}$')
plt.text(107,73,'Rz=30$^{\circ}$')
plt.arrow(42,40,25,0,head_width=2,head_length=3,color='r') #--red arrows
plt.arrow(42,40,28,0,head_width=2,head_length=3,color='r')
plt.arrow(85,25,0,27,head_width=2,head_length=2,color='r')
plt.arrow(85,25,0,29,head_width=2,head_length=2,color='r')
plt.plot([8,130],[8,8],color='k')                          #--axes
plt.plot([8,8],[8,85],color='k')
plt.text(120,6,'X')
plt.text(3,80,'Y')
plt.scatter(115,40,s=30,color='r') #-----------red dot center of box (d)

plt.show()


