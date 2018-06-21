# -*- coding: utf-8 -*-
"""
Listing 8-6. REGRESSION1
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

#---------------------------------------straight line fit to Volume v vs t
n=len(v)

c1=np.sum(t)/n
c2=np.sum(v)/n
a=np.multiply(v,t)   #---multiplies list v by t element by element = list a
c3=np.sum(a)         #---add the elements in a
a=np.multiply(t,t)
c4=np.sum(a)

A=(c3-n*c1*c2)/(c4-n*c1*c1)   #---line coefficients
B=c2-A*c1

for tp in np.arange(t[0],t[5],2):   #---plot line with scatter dots
    vp=A*tp+B
    vp=vp*100
    plt.scatter(tp,vp,color='g',s=1)

#-------------------------------------------------Calculate RMS Error
sumee=0
for i in range(len(t)):
    e=(v[i]-(A*t[i]+B))
    ee=e*e
    sumee=sumee+ee
    rms=np.sqrt(sumee/n)
    
#-------------------------------------------------labels
plt.text(60,28,'v=At+B',color='g')
plt.arrow(78,30,6,6,head_length=3,head_width=1.5,color='g',linewidth=.5)

vp1=A*t[0]+B
vp1='%7.4f'%(vp1)
plt.text(2,64,vp1,color='g')

vp2=A*t[5]+B
vp2='%7.4f'%(vp2)
plt.text(122,25,vp2,color='g')

Ap='%7.5f'%(A)
plt.text(65,18,'A=',color='g')
plt.text(72,18,Ap,color='g')

Bp='%7.5f'%(B)
plt.text(65,12,'B=',color='g')
plt.text(73,12,Bp,color='g')

rms='%7.3f'%(rms)
plt.text(95,3,'RMS error=',color='g')
plt.text(120,3,rms,color='g')


plt.show()
