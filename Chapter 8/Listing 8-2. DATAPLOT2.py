 # -*- coding: utf-8 -*-
"""
Listing 8-2. DATAPLOT2
"""

import matplotlib.pyplot as plt
import numpy as np

plt.axis([0,150,0,100])
plt.axis('on')
plt.grid(True)

x=[20,40,60,80,100,120,140]
y1=[30,50,30,45,70,43,80]
y2=[45,35,40,60,60,55,70]

plt.plot(x,y1,color='b',label='Temperature')
plt.plot(x,y2,color='r',label='Pressure')

plt.legend(loc='upper left')

plt.scatter(x,y1,color='b',marker='s')
plt.scatter(x,y2,color='r',marker='*',s=50)
    
plt.show()

