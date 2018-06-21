# -*- coding: utf-8 -*-
"""
Listing 9-2. SURFACE3D   
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, radians, sin, cos

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

#==============================================================plot data points
def plotdata(x,y,z,Rx,Ry,Rz):
    for i in range(0,nop):
        xp=x[i]
        yp=y[i]
        zp=z[i]            
        rotx(xp,yp,zp,Rx)
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        roty(xp,yp,zp,Ry)
        xp=g[0]-xc
        yp=g[1]-yc 
        zp=g[2]-zc
        rotz(xp,yp,zp,Rz)
        xp=g[0]-xc
        yp=g[1]-yc 
        zp=g[2]-zc
        plt.scatter(g[0],g[1],s=25,color='g') 
        
#===================================================================plot spline
def plotspline(x,y,z,Rx,Ry,Rz,clr):
    q=[0]*nop
    mx=[0]*nop
    my=[0]*nop
    mz=[0]*nop
    cx=[0]*nop
    cy=[0]*nop
    cz=[0]*nop
    dx=[0]*nop
    dy=[0]*nop
    dz=[0]*nop
    bx=[0]*nop
    by=[0]*nop
    bz=[0]*nop
    ax=[0]*nop
    ay=[0]*nop
    az=[0]*nop
    
    for i in range(1,nop):            #---chords q(i)
        a=x[i]-x[i-1]
        b=y[i]-y[i-1]
        c=z[i]-z[i-1]
        q[i-1]=sqrt(a*a+b*b+c*c)      #---nop=6 gives q[5]
    
    mx[0]=(x[1]-x[0])/q[0]            #---mx[0]
    my[0]=(y[1]-y[0])/q[0]            #---my[0]
    mz[0]=(z[1]-z[0])/q[0]            #---mx[0]

    for i in range(1,nop-1):                  #---average m[i] 
        mx[i]=((x[i]-x[i-1])/q[i-1]+(x[i+1]-x[i])/q[i])*.5
        my[i]=((y[i]-y[i-1])/q[i-1]+(y[i+1]-y[i])/q[i])*.5
        mz[i]=((z[i]-z[i-1])/q[i-1]+(z[i+1]-z[i])/q[i])*.5
     
    mx[nop-1]=(x[nop-1]-x[nop-2])/q[nop-2]   #---mx[nop-1] 
    my[nop-1]=(y[nop-1]-y[nop-2])/q[nop-2]   #---my[nop-1]
    mz[nop-1]=(z[nop-1]-z[nop-2])/q[nop-2]   #---mz[nop-1]

    #----------------------------------calculate coefficients   
    for i in range(0,nop-1):
        dx[i]=x[i]
        dy[i]=y[i]
        dz[i]=z[i]
        cx[i]=mx[i]
        cy[i]=my[i]
        cz[i]=mz[i]
        bx[i]=(3*x[i+1]-2*cx[i]*q[i]-3*dx[i]-mx[i+1]*q[i])/(q[i]*q[i])
        by[i]=(3*y[i+1]-2*cy[i]*q[i]-3*dy[i]-my[i+1]*q[i])/(q[i]*q[i])
        bz[i]=(3*z[i+1]-2*cz[i]*q[i]-3*dz[i]-mz[i+1]*q[i])/(q[i]*q[i])
        ax[i]=(mx[i+1]-2*bx[i]*q[i]-cx[i])/(3*q[i]*q[i])
        ay[i]=(my[i+1]-2*by[i]*q[i]-cy[i])/(3*q[i]*q[i])
        az[i]=(mz[i+1]-2*bz[i]*q[i]-cz[i])/(3*q[i]*q[i])
    
    #------------------------------------------plot splines between data points
        for i in range(0,nop-1):
            for qq in np.arange(0,q[i],2):
                xp=ax[i]*qq*qq*qq+bx[i]*qq*qq+cx[i]*qq+dx[i]
                yp=ay[i]*qq*qq*qq+by[i]*qq*qq+cy[i]*qq+dy[i]
                zp=az[i]*qq*qq*qq+bz[i]*qq*qq+cz[i]*qq+dz[i]
                rotx(xp,yp,zp,Rx)  #---Rx rotation
                xp=g[0]-xc
                yp=g[1]-yc
                zp=g[2]-zc
                roty(xp,yp,zp,Ry)   #---Ry rotation
                xp=g[0]-xc
                yp=g[1]-yc
                zp=g[2]-zc
                rotz(xp,yp,zp,Rz)   #---Rz rotation
                if qq==0:
                    xplast=g[0]
                    yplast=g[1]
                plt.plot([xplast,g[0]],[yplast,g[1]],linewidth=.7,color=clr)
                xplast=g[0]
                yplast=g[1]
                
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
plotaxis(65,0,0,Rx,Ry,Rz)   #---plot X axis
plt.plot([xc,g[0]],[yc,g[1]],linewidth=2,color='k')
plt.text(g[0]-5,g[1]-1,'X')

plotaxis(0,65,0,Rx,Ry,Rz)   #---plot Y axis
plt.plot([xc,g[0]],[yc,g[1]],linewidth=2,color='k')
plt.text(g[0],g[1]-5,'Y') 

plotaxis(0,0,65,Rx,Ry,Rz)   #---plot Z axis
plt.plot([xc,g[0]],[yc,g[1]],linewidth=2,color='k')
plt.text(g[0]-2,g[1]+3,'Z') 
 
#-------------------------define 4 sets of data points at different values of X           
x1=[0,0,0,0]              #---LOCAL coords
y1=[0,10,20,30]
z1=[50,43,30,14]

x2=[20,20,20,20]
y2=y1
z2=[25,23,19,12]

x3=[40,40,40,40]
y3=y1
z3=[14,15,13,9]

x4=[60,60,60,60]
y4=y1
z4=[7,10,10,9]

nop=len(x1)   #---number of data points
       
#--------------------------------------------------------------plot data points
plotdata(x1,y1,z1,Rx,Ry,Rz)
plotdata(x2,y2,z2,Rx,Ry,Rz)
plotdata(x3,y3,z3,Rx,Ry,Rz)
plotdata(x4,y4,z4,Rx,Ry,Rz)

#------------------------------------------------------plot Y direction splines
clr='g'  #-----------------------------spline color
plotspline(x1,y1,z1,Rx,Ry,Rz,clr)
plotspline(x2,y2,z2,Rx,Ry,Rz,clr)
plotspline(x3,y3,z3,Rx,Ry,Rz,clr)
plotspline(x4,y4,z4,Rx,Ry,Rz,clr)

#-----------------------------redefine the data points at different values of y
xx1=[0,20,40,60]  
yy1=[y1[3],y2[3],y3[3],y4[3]]
zz1=[z1[3],z2[3],z3[3],z4[3]]

xx2=xx1
yy2=[ y1[2],y2[2],y3[2],y4[2] ]
zz2=[ z1[2],z2[2],z3[2],z4[2] ]

xx3=xx1 
yy3=[ y1[1],y2[1],y3[1],y4[1] ]
zz3=[ z1[1],z2[1],z3[1],z4[1] ]

xx4=xx1
yy4=[ y1[0],y2[0],y3[0],y4[0] ]
zz4=[ z1[0],z2[0],z3[0],z4[0] ]

#------------------------------------------------------plot X direction splines
clr='b'  #-----------------------------spline color
plotspline(xx1,yy1,zz1,Rx,Ry,Rz,clr)
plotspline(xx2,yy2,zz2,Rx,Ry,Rz,clr)
plotspline(xx3,yy3,zz3,Rx,Ry,Rz,clr)
plotspline(xx4,yy4,zz4,Rx,Ry,Rz,clr)

#------------------------------------------------------------------------labels
plt.text(120,90,'Rx=')
Rxd='%7.1f'%(Rxd)
plt.text(130,90,Rxd)

plt.text(120,85,'Ry=')
Ryd='%7.1f'%(Ryd)
plt.text(130,85,Ryd)

plt.text(120,80,'Rz=')
Rzd='%7.1f'%(Rzd)
plt.text(130,80,Rzd)

plt.text(81,70,'0')
plt.text(89,62,'1')
plt.text(97,48,'2')
plt.text(103,34,'3')
plt.text(60,43,'4')
plt.text(87,30,'7')
plt.text(46,30,'8')
plt.text(72,25,'11')
plt.text(31,22,'12')
plt.text(61,22,'15')

plt.text(89,73,'A[0]')
plt.text(96,64,'A[1]')
plt.text(105,50,'A[2]')
plt.text(112,33,'A[3]')
plt.text(46,45,'A[4]')

plt.title('3D Surface')

plt.show()




