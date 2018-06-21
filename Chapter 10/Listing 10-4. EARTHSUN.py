# -*- coding: utf-8 -*-
"""
Listing 10-4. EARTHSUN
"""

import matplotlib.pyplot as plt
import numpy as np
from math import radians, sin, cos, sqrt

plt.axis([-100,150,-100,150])

plt.grid(False)
plt.axis('off')
sfx=2.5/3.8

#-------------------------------------------------------------------background
for x in range(-100,150,2):
    for y in range(-100,150,2):
        plt.scatter(x,y,s=40,color='midnightblue')

phimin=0.
phimax=2.*np.pi
dphi=phimax/100.

rs=40.
re=20. 

ys=15.
ye=2.

xos=50.
yos=0.
zos=0.

#---------------------------------------------------------Sun's core
plt.scatter(xos,yos,s=4300,color='yellow')

#---------------------------------------------------------Sun horizontals
rx=radians(20)

for ys in np.arange(-rs,rs,5): 
    for phi in np.arange(phimin,phimax,dphi):
        rp=np.sqrt(rs*rs-ys*ys)
        xp=rp*np.sin(phi)        
        yp=ys
        zp=rp*np.cos(phi)
        px=xos   +sfx*xp*1.     +yp*0.              +zp*0.
        py=yos   +xp*0.        +yp*np.cos(rx)      -zp*np.sin(rx)
        pz=zos   +xp*0.        +yp*np.sin(rx)      +zp*np.cos(rx)
        if pz > 0 :
            plt.scatter(px,py,s=1,color='red')
        
#-----------------------------------------------------------Sun verticals          
alphamin=0.
alphamax=2.*np.pi
dalpha=alphamax/30.

for alpha in np.arange(alphamin,alphamax,dalpha): 
    for phi in np.arange(phimin,phimax,dphi):
        xp=rs*np.sin(phi)*np.sin(alpha)
        yp=rs*np.cos(phi)
        zp=rs*np.sin(phi)*np.cos(alpha)
        px=xos   +sfx*(xp*1.   +yp*0.              +zp*0.)
        py=yos   +xp*0.   +yp*np.cos(rx)     -zp*np.sin(rx)
        pz=zos   +xp*0.   +yp*(np.sin(rx))   +zp*np.cos(rx)
        if pz > 0 :
             plt.scatter(px,py,s=1,color='red')
             
#----------------------------------------------------------------Earth's clouds
xoe=-50.
yoe=20.
zoe=-10.   
           
plt.scatter(xoe,yoe,s=800,color='white')
             
#------------------------------------------------------------ Earth horizontals
rx=20.*np.pi/180.   
dphi=phimax/100.

for ys in np.arange(-re,re,2): 
    for phi in np.arange(phimin,phimax,dphi):
        rp=np.sqrt(re*re-ys*ys)
        xp=rp*np.sin(phi)        
        yp=ys
        zp=rp*np.cos(phi)
        px=xoe   +sfx*(+xp*1.   +yp*0.              +zp*0.)
        py=yoe   +xp*0.   +yp*np.cos(rx)     -zp*np.sin(rx)
        pz=zoe   +xp*0.   +yp*(np.sin(rx))   +zp*np.cos(rx)
        if pz > 0 :
            plt.scatter(px,py,s=.1,color='#add8e6')
        
#-------------------------------------------------------------Earth verticals          
alphamin=0.
alphamax=2.*np.pi
dalpha=alphamax/30.

for alpha in np.arange(alphamin,alphamax,dalpha):
    for phi in np.arange(phimin,phimax,dphi):
        xp=re*np.sin(phi)*np.sin(alpha)
        yp=re*np.cos(phi)
        zp=re*np.sin(phi)*np.cos(alpha)
        px=xoe   +sfx*(xp*1.   +yp*0.              +zp*0.)
        py=yoe   +xp*0.   +yp*np.cos(rx)      -zp*np.sin(rx)
        pz=zoe   +xp*0.   +yp*(np.sin(rx))   +zp*np.cos(rx)
        if pz > 0 :
             plt.scatter(px,py,s=.1,color='#add8e6')       
             
plt.arrow(xos-rs*sfx-3,yos+2,xoe-(xos-rs*sfx)+re+3,yoe-yos-6.2,color='r',head_length=4.,head_width=3.)
plt.text(-14,16,'1 AU',color='white')
plt.text(80,-29,'Sun',color='white')
plt.text(-84,10,'Earth',color='white')

#-------------------------------------------------------------------front orbit
deltamin=0.*np.pi/180.
deltamax=195.*np.pi/180.
ddelta=deltamax/60.

for delta in np.arange(deltamin,deltamax,ddelta):
    r=108./sfx
    xp=r*np.cos(delta)
    yp=0.
    zp=r*np.sin(delta)
    px=xos   +sfx*(xp*1.   +yp*0.              +zp*0.)
    py=yos   +xp*0.   +yp*np.cos(rx)      -zp*np.sin(rx)
    pz=zos   +xp*0.   +yp*(np.sin(rx))   +zp*np.cos(rx)
    plt.scatter(px,py,s=1,color='white')

#--------------------------------------------------------------------back orbit
deltamin=220.*np.pi/180.
deltamax=360.*np.pi/180.

for delta in np.arange(deltamin,deltamax,ddelta):
    r=108./sfx
    xp=r*np.cos(delta)
    yp=0.
    zp=r*np.sin(delta)
    px=xos   +sfx*xp*1.   +yp*0.              +zp*0.
    py=yos   +xp*0.   +yp*np.cos(rx)     -zp*np.sin(rx)
    pz=zos   +xp*0.   +yp*(np.sin(rx))   +zp*np.cos(rx)
    plt.scatter(px,py,s=1,color='white')
  
#-----------------------------------------------------------------------Ap disc
xoc=xoe+re*sfx
yoc=yoe-2.5
zoc=zoe
rc=.83*re
phi1=0
phi2=2*np.pi
dphi=(phi2-phi1)/200
ry=-25*np.pi/180

for phi in np.arange(phi1,phi2,dphi):
    xc=xoc
    yc=rc*np.sin(phi)    
    zc=rc*np.cos(phi)
    px=xoc+zc*np.sin(ry)
    py=yoc+yc
    pz=zoc+zc*np.cos(ry)
    plt.scatter(px,py,s=.03 ,color='white')
    
plt.scatter(xoe+re*sfx,yoe-2,s=6,color='white')

plt.arrow(-20,60,(xoe+re*sfx)+24,(yoe+re/2)-60-2,color='white',linewidth=.5,head_width=2.,head_length=3)
plt.text(-18,60,'A$_{p}$',color='white')
    
plt.show()