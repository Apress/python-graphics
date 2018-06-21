# -*- coding: utf-8 -*-
"""
Listing 8-8. SPLINE2D
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

plt.axis([0,140,0,100])
plt.axis('on')
plt.grid(True)

plt.xlabel('x')
plt.ylabel('y')
plt.title('2D Splines')

def spline(x,y,clr,ls):
    nop=len(x)
    plt.scatter(x,y,s=30,color=clr)
    q=[0]*nop
    mx=[0]*nop
    my=[0]*nop
    cx=[0]*nop
    cy=[0]*nop
    dx=[0]*nop
    dy=[0]*nop
    bx=[0]*nop
    by=[0]*nop
    ax=[0]*nop
    ay=[0]*nop

    for i in range(1,nop):            #---chords q(i); nop=6 gives q[5]
        a=x[i]-x[i-1]
        b=y[i]-y[i-1]
        q[i-1]=sqrt(a*a+b*b)
    
    mx[0]=(x[1]-x[0])/q[0]            #---mx[0]
    my[0]=(y[1]-y[0])/q[0]            #---my[0]

    for i in range(1,nop-1):                  #---average m[i] 
        mx[i]=((x[i]-x[i-1])/q[i-1]+(x[i+1]-x[i])/q[i])*.5
        my[i]=((y[i]-y[i-1])/q[i-1]+(y[i+1]-y[i])/q[i])*.5
     
    mx[nop-1]=(x[nop-1]-x[nop-2])/q[nop-2]   #---mx[nop-1] 
    my[nop-1]=(y[nop-1]-y[nop-2])/q[nop-2]   #---my[nop-1]

    #----------------------------------calculate coefficients   
    for i in range(0,nop-1):
        dx[i]=x[i]
        dy[i]=y[i]
        cx[i]=mx[i]
        cy[i]=my[i]
        bx[i]=(3*x[i+1]-2*cx[i]*q[i]-3*dx[i]-mx[i+1]*q[i])/(q[i]*q[i])
        by[i]=(3*y[i+1]-2*cy[i]*q[i]-3*dy[i]-my[i+1]*q[i])/(q[i]*q[i])
        ax[i]=(mx[i+1]-2*bx[i]*q[i]-cx[i])/(3*q[i]*q[i])
        ay[i]=(my[i+1]-2*by[i]*q[i]-cy[i])/(3*q[i]*q[i])
   
    #-----------------------------------plot the spline
    xplast=x[0]
    yplast=y[0]
    for i in range(0,nop-1):
       for qq in np.arange(0,q[i],4):
           xp=ax[i]*qq*qq*qq+bx[i]*qq*qq+cx[i]*qq+dx[i]
           yp=ay[i]*qq*qq*qq+by[i]*qq*qq+cy[i]*qq+dy[i]
           plt.plot([xplast,xp],[yplast,yp],linewidth=1,color=clr,linestyle=ls)
           xplast=xp
           yplast=yp
           if i==2:
               print(xp,yp)

#--------------------------------------------------control
x=[20,40,60,80,100,120]
y=[80,35,70,30,60,40]
clr='b'
ls='--'
spline(x,y,clr,ls)

x=[20,40,60,80,100,120]
y=[30,45,18,65,50,80]
clr='g'
ls='-'       
spline(x,y,clr,ls)


plt.show()