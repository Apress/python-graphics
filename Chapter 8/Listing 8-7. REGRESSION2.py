# -*- coding: utf-8 -*-
"""
Listing 8-7. REGRESSION2
"""

import matplotlib.pyplot as plt
import numpy as np

plt.axis([0,140,0,100])
plt.axis('on')
plt.grid(True)

t=[20,40,60,80,100,120]
T=[30,35,43,55,70,85]
p=[2,3,4,5.3,7.3,9.6]
v=[.6,.58,.54,.46,.35,.2]

pp=[]
for i in np.arange(0,len(p),1):
    pp.append(p[i]*10)
    
vv=[]
for i in np.arange(0,len(v),1):
    vv.append(v[i]*100)

plt.plot(t,T,color='r',label='Temperature',marker='o')
plt.plot(t,pp,color='b',label='Pressure',marker='s')
plt.plot(t,vv,color='g',label='Volume',marker='d')
plt.legend(loc='upper left')

for y in np.arange(0,100+1,20):
    a=y/10
    a=str(a)
    plt.text(142,y,a,color='b')
    
plt.xlabel('time (hrs)')
plt.ylabel('Temperature ($^{\circ}$K )',color='r')
plt.text(151,65,'Pressure (Pa)',rotation=90,color='b')

for y in np.arange(100,-1,-20):
    a=y/100
    a=str(a)
    plt.text(162,y,a,color='g')
    plt.text(159,y+2,'_',color='g')
    
for y in np.arange(1,99,3):
    plt.text(157,y,'|',color='g')
    
plt.text(170,65,r'Volume (cm$^{3})$',rotation=90,color='g')
    
plt.title('Compression Test Results')

#---------------------------------------parabolic fit to v vs t
n=len(v)

eemin=10**10

B1=.5
B2=.7
dB=.001
A1=-.001
A2=0.
dA=.0000001

for B in np.arange(B1,B2,dB):
    for A in np.arange(A1,A2,dA):
        sumee=0
        for i in range(len(t)):
            e=(v[i]-(A*t[i]*t[i]+B))   #error at each A
            ee=e*e
            sumee=sumee+ee   #sum of error squared at each A
        if sumee < eemin:    #if sum < present minimum
            eemin=sumee      #new minimum=sum
            Amin=A           #new Amin=A
            Bmin=B
         
for tp in np.arange(t[0],t[5],2):   #---plot curve with scatter dots
    vp=Amin*tp*tp+Bmin
    vp=vp*100
    plt.scatter(tp,vp,color='g',s=1)
   
#-------------------------------------------------Calculate RMS Error
sumee=0 
for i in range(len(v)):
    e=(v[i]-(Amin*t[i]*t[i]+Bmin))
    ee=e*e
    sumee=sumee+ee
    rms=np.sqrt(sumee/n)
    
#-------------------------------------------------labels
plt.text(100,50,r'v=At$^{2}$+B',color='g')
plt.arrow(99,50,-6.5,-6.5,head_length=3,head_width=1.5,color='g',linewidth=.5)

A=Amin
B=Bmin

vp1=A*t[0]*t[0]+B
vp1='%7.3f'%(vp1)
plt.text(2,63,vp1,color='g')

vp2=A*t[5]*t[5]+B
vp2='%7.3f'%(vp2)
plt.text(119,22,vp2,color='g')

Ap='%8.6f'%(A)
plt.text(59,18,'Amin=',color='g')
plt.text(74,18,Ap,color='g')

Bp='%8.6f'%(B)
plt.text(59,12,'Bmin=',color='g')
plt.text(75.2,12,Bp,color='g')

rms='%7.4f'%(rms)
plt.text(95,3,'RMS error=',color='g')
plt.text(120,3,rms,color='g')

A1='%8.6f'%(A1)
plt.text(60,90,'A1=')
plt.text(69,90,A1)

A2='%8.6f'%(A2)
plt.text(60,85,'A2=')
plt.text(70.2,85,A2)

B1='%8.6f'%(B1)
plt.text(60,75,'B1=')
plt.text(70.2,75,B1)

B2='%8.6f'%(B2)
plt.text(60,70,'B2=')
plt.text(70.2,70,B2)

plt.show()
