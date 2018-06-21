"""
Listing 5-3. LTP
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

x=[-10,-30,20,-60,40]
y=[0,0,0,-20,5]
z=[0,30,0,15,0]

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
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')
    plt.plot([xg[3],xg[4]],[yg[3],yg[4]],color='g')   #--------plot line
    plt.scatter(xc,yc,s=10,color='k')    #---plot center of rotation     
    
    if hitcolor=='g':
        plt.scatter(xg[4],yg[4],s=20,color=hitcolor)
    else:               
        plt.scatter(xhg,yhg,s=20,color=hitcolor)    #----------------plot hit point
    
    plt.axis([0,150,100,0])            #--replot axes and grid
    plt.axis('on')
    plt.grid(True)
    plt.show()                         #--plot latest rotation
 
#-------------------------------------calculate hit point coordinates and color  
def hitpoint(x,y,z):
    a=x[4]-x[3]
    b=y[4]-y[3]
    c=z[4]-z[3]
    Q34=sqrt(a*a+b*b+c*c)  #-------distance point 3 to 4
    
    lx=a/Q34               #----unit vector components point 3 to 4
    ly=b/Q34
    lz=c/Q34
    
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    Q02=sqrt(a*a+b*b+c*c)  #---distance 0 to 3
    
    ux=a/Q02               #---unit vector 0 to 3
    uy=b/Q02
    uz=c/Q02
    
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
 #----------------------------------------------  
    magn=sqrt(nx*nx+ny*ny+nz*nz)
    nx=nx/magn
    ny=ny/magn
    nz=nz/magn
   
 #----------------------------------------------   
    a=x[3]-x[0]         #---vector components 0 to 3
    b=y[3]-y[0]
    c=z[3]-z[0]
    
    Qn=(a*nx+b*ny+c*nz)   #---perpendicular distance 3 to plane
        
    cosp=lx*nx+ly*ny+lz*nz    #---cos of angle p
    Qh=abs(Qn/cosp)           #---distance 4 to hit point
    
    xh=x[3]+Qh*lx           #---hit point coordinates
    yh=y[3]+Qh*ly
    zh=z[3]+Qh*lz
    
    xhg=xh+xc               #----global hit point coordinates
    yhg=yh+yc
    zhg=zh+zc

#-----------------------------------------------------------out of bounds check
    a=x[1]-x[2]
    b=y[1]-y[2]    
    c=z[1]-z[2]
    Q12=sqrt(a*a+b*b+c*c)    
    
    a=x[1]-xh
    b=y[1]-yh
    c=z[1]-zh
    Q1h=sqrt(a*a+b*b+c*c)
    
    a=x[2]-xh
    b=y[2]-yh
    c=z[2]-zh
    Q2h=sqrt(a*a+b*b+c*c)

    a=x[0]-xh
    b=y[0]-yh
    c=z[0]-zh
    Q0h=sqrt(a*a+b*b+c*c)
    
    s=(Q01+Q12+Q02)/2    #---area A
    A=sqrt(s*(s-Q01)*(s-Q12)*(s-Q02))
    
    s1=(Q01+Q0h+Q1h)/2   #---area A1
    A1=sqrt(s1*(s1-Q01)*(s1-Q0h)*(s1-Q1h))
    
    s2=(Q02+Q2h+Q0h)/2#---area A2
    A2=sqrt(s2*(s2-Q02)*(s2-Q2h)*(s2-Q0h))
    
    hitcolor='r'          #---if within bounds plot red hit point
    
    if A1+A2>A:              #---if out of bounds plot blue hit point  
        hitcolor='b'      
              
    a=x[4]-x[3]
    b=y[4]-y[3]
    c=z[4]-z[3]
    Q34=sqrt(a*a+b*b+c*c)
    if Q34 < Qh:          #---if line too short plot green at end of line
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


