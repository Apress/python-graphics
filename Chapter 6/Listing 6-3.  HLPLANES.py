# -*- coding: utf-8 -*-
"""
Listing 6-3. HLPLANES
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, sin, cos, radians

plt.axis([0,150,100,0])
plt.axis('on')
plt.grid(True)

#--------------------------------------------------------------- -define planes
axg=[40,70,70,40]
ayg=[25,25,60,60]

bxg=[55,85,85,55]
byg=[35,35,70,70]

#========================================================define function dlinea
def dlinea(x1,x2,y1,y2):
    q=sqrt((x2-x1)**2+(y2-y1)**2)
    uxa=(x2-x1)/q
    uya=(y2-y1)/q
    hxstart=x1
    hystart=y1
    for l in np.arange(0,q,.2):
        hx=x1+l*uxa                 #---global hit coordinates along the line
        hy=y1+l*uya  
        plt.plot([hxstart,hx],[hystart,hy],linewidth=2,color='k')
        hxstart=hx
        hystart=hy
        
#---------------------------------------------------------------plane a
dlinea(axg[0],axg[1],ayg[0],ayg[1])    #---plot plane (a)
dlinea(axg[1],axg[2],ayg[1],ayg[2])  
dlinea(axg[2],axg[3],ayg[2],ayg[3]) 
dlinea(axg[3],axg[0],ayg[3],ayg[0]) 
    
a=axg[3]-axg[0]    #---unit vector u plane (a)
b=ayg[3]-ayg[0]
qa03=sqrt(a*a+b*b)
uxa=a/qa03
uya=b/qa03

a=axg[1]-axg[0]    #---unit vector v plane (a)
b=ayg[1]-ayg[0]
qa01=sqrt(a*a+b*b)
vxa=a/qa01
vya=b/qa01

#----------------------------------------------------------------plane b
def dlineb(x1,x2,y1,y2,ax0,ay0):
    a=x2-x1      #---unit vector line
    b=y2-y1
    ql=sqrt(a*a+b*b)
    uxl=a/ql             
    uyl=b/ql
    hxglast=x1
    hyglast=y1
    for l in np.arange(0,ql,.5):
        hxg=x1+l*uxl
        hyg=y1+l*uyl
        a=hxg-ax0                          #---inside/outside check
        b=hyg-ay0
        up=a*uxa+b*uya
        vp=a*vxa+b*vya
        if 0<up<qa03 and 0<vp<qa01:   #---is it inside (a)?
            plt.plot([hxglast,hxg],[hyglast,hyg],color='white')
        else:
            plt.plot([hxglast,hxg],[hyglast,hyg],linewidth=2,color='b')
        hxglast=hxg
        hyglast=hyg
        
dlineb(bxg[0],bxg[1],byg[0],byg[1],axg[0],ayg[0])    #---plot plane (a)
dlineb(bxg[1],bxg[2],byg[1],byg[2],axg[0],ayg[0])  
dlineb(bxg[2],bxg[3],byg[2],byg[3],axg[0],ayg[0]) 
dlineb(bxg[3],bxg[0],byg[3],byg[0],axg[0],ayg[0])    
        
plt.show()







