# -*- coding: utf-8 -*-
"""
Listing 8-5. DATAPLOT5
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
plt.text(151,65,'Pressure (psi)',rotation=90,color='b')

for y in np.arange(100,-1,-20):
    a=y/100
    a=str(a)
    plt.text(162,y,a,color='g')
    plt.text(159,y+2,'_',color='g')
    
for y in np.arange(1,99,3):
    plt.text(157,y,'|',color='g')
    
plt.text(170,65,r'Volume (cm$^{3})$',rotation=90,color='g')
    
plt.title('Compression Test Results')

plt.show()