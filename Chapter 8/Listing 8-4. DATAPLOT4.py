# -*- coding: utf-8 -*-
"""
Listing 8-4. DATAPLOT4
"""

import matplotlib.pyplot as plt
import numpy as np

t=[0,20,40,60,80,100,120]
T=[28,30,35,43,55,70,85]
p=[1.8,2.3,3,4,5.4,7.3,9.6]
v=[.8,.6,.58,.54,.46,.35,.3]

fig, ax1 = plt.subplots()

plt.grid(True)

ax1.set_xlabel('time (hrs)')

l1=plt.plot(t,T,'r',label='Temperature')

ax1.set_ylim([0,100])
ax1.set_ylabel(r'Temperature ($^{\circ}$K)', color='r')

ax2 = ax1.twinx()
l2=plt.plot(t, p, 'b',label='Pressure')
ax2.set_ylim([0,10])

ax2.set_ylabel('pressure (psi)', color='b')

line1,=plt.plot([1],label='Temperature',color='r')
line2,=plt.plot([2],label='Pressure ',color='b')
plt.legend(handles=[line1,line2],loc='upper left')

plt.title('Test Data')



