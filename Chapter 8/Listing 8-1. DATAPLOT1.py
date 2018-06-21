# -*- coding: utf-8 -*-
"""
Listing 8-1. DATAPLOT1
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sin,cos,radians,sqrt

plt.axis([0,150,0,100])
plt.axis('on')
plt.grid(True)

x=np.arange(0,150,1)
y1=10+np.exp(.035*x)

plt.plot(x, y1,'b', label='temperature')

plt.legend(loc='upper left')
      
plt.show()