 # -*- coding: utf-8 -*-
"""
Listing 9-1. SPLINE3D
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
        if i==0:
            plt.scatter(g[0],g[1],s=25,color='r')
        else:
            plt.scatter(g[0],g[1],s=25,color='g')
        #-----------------plot vertical lines from data points to the x,y plane
        xt=g[0]  #---global line top plotting coords=rotated data point coords 
        yt=g[1]  
        xp=x[i]  #---coords of line bottom (zp=0) before rotation)
        yp=y[i]  #
        zp=0     #
        rotx(xp,yp,zp,Rx)  #---rotate bottom coords
        xp=g[0]-xc
        yp=g[1]-yc
        zp=g[2]-zc
        roty(xp,yp,zp,Ry)
        xp=g[0]-xc
        yp=g[1]-yc  
        zp=g[2]-zc
        rotz(xp,yp,zp,Rz)
        if i==0:     #------------------------------plot first bottom point red
            plt.scatter(g[0],g[1],s=25,color='r')
        else:
            plt.scatter(g[0],g[1],s=25,color='k')
        plt.plot([xt,g[0]],[yt,g[1]],color='grey')   #-----plot line
        
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
    
    #-------------------------------------------plot spline between data points
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
                
#============================================================plot bottom spline
def plotbottomspline(x,y,z,Rx,Ry,Rz,clr):
    xbottom=[0]*nop
    ybottom=[0]*nop
    zbottom=[0]*nop 
    for i in range(0,nop):
        xbottom[i]=x[i]
        ybottom[i]=y[i]
        zbottom[i]=0
    plotspline(xbottom,ybottom,zbottom,Rx,Ry,Rz,  clr)        

#=======================================================================control                     
#x=[20,40,60,80]              #---LOCAL coords-Fig 3D Spline 1
#y=[30,30,30,30]
#z=[15,33,28,17]  

#x=[10,30,65,60,80,95,130,140] #--LOCAL coordinates-Figs 3D Spline 2,3 and 4
#y=[20,35,50,32,60,50,65,60]
#z=[42,30,22,28,45,55,55,55] 
 
nop=len(x)   #---number of data points

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

#--------------------------------------------------------plot X,Y,Z axes
plotaxis(30,0,0,Rx,Ry,Rz)   #---plot X axis
plt.plot([xc,g[0]],[yc,g[1]],linewidth=2,color='k')
plt.text(g[0]-5,g[1]-1,'X')

plotaxis(0,30,0,Rx,Ry,Rz)   #---plot Y axis
plt.plot([xc,g[0]],[yc,g[1]],linewidth=2,color='k')
plt.text(g[0],g[1]-5,'Y') 

plotaxis(0,0,30,Rx,Ry,Rz)   #---plot Z axis
plt.plot([xc,g[0]],[yc,g[1]],linewidth=2,color='k')
plt.text(g[0]-2,g[1]+3,'Z') 
         
#---------------------------------------------------------plot data
plotdata(x,y,z,Rx,Ry,Rz)

#---------------------------------------------------------plot spline
clr='g'  #-----------------------------spline color
plotspline(x,y,z,Rx,Ry,Rz,clr)

#---------------------------------------------------------plot bottom spline
clr='b'  #-----------------------------bottom spline color
plotbottomspline(x,y,z,Rx,Ry,Rz,clr)   

#------------------------------------------------------------labels
plt.text(120,90,'Rx=')
Rxd='%7.1f'%(Rxd)
plt.text(130,90,Rxd)

plt.text(120,85,'Ry=')
Ryd='%7.1f'%(Ryd)
plt.text(130,85,Ryd)

plt.text(120,80,'Rz=')
Rzd='%7.1f'%(Rzd)
plt.text(130,80,Rzd)

plt.text(90,90,'xc=')
xc='%7.1f'%(xc)
plt.text(100,90,xc)

plt.text(90,85,'yc=')
Ryc='%7.1f'%(yc)
plt.text(100,85,yc)

plt.text(90,80,'zc=')
zc='%7.1f'%(zc)
plt.text(100,80,zc)

plt.text(4,90,'x')
plt.text(7,90,x)
plt.text(4,85,'y')
plt.text(7,85,y)
plt.text(4,80,'z')
plt.text(7,80,z)

plt.title('3D Spline 1 ')

plt.show()


