# -*- coding: utf-8 -*-
"""
Listing 8-3. DATAPLOT3
"""

import matplotlib.pyplot as plt
import numpy as np

plt.axis([0,140,0,100])
plt.axis('on')
plt.grid(True)

#--------------------define the data points
t=[20,40,60,80,100,120,140]
T=[30,33,37.5,44,55,70,86]
p=[1.8,2.3,3,4,5.4,7.3,9.6]

#------------------plot T vs t in red on the left vertical axis
plt.plot(t,T,color='r',label='Temperature')
plt.xlabel('time')
plt.ylabel('Temperature',color='r')
plt.tick_params(axis='y',labelcolor='r')
plt.legend(loc='upper left')

#------------------plot p vs t in blue on the right vertical axis
plt.twinx()
plt.plot(t,p,color='b',label='pressure')
plt.ylabel('Pressure',color='b')
plt.tick_params(axis='y',labelcolor='b')

#------------------plot the legend
plt.legend(loc='upper right')

#------------------label the plot
plt.title('Test Results')

plt.show()