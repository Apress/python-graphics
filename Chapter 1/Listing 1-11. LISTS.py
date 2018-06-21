# -*- coding: utf-8 -*-
"""
Listing 1-11. LISTS
"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([-75,75,50,-50])

plt.axis('on')
plt.grid(True)

plt.arrow(0,0,20,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,20,head_length=4,head_width=3,color='k')

plt.text(22,-3,'x')
plt.text(-5,25,'y')

#----------red box
plt.plot([-20,20],[-20,-20],linewidth=2,color='r')
plt.plot([20,20],[-20,20],linewidth=2,color='r')
plt.plot([20,-20],[20,20],linewidth=2,color='r')
plt.plot([-20,-20],[-20,20],linewidth=2,color='r')

#----------green box
x=[-30,30,30,-30,-30]
y=[-30,-30,30,30,-30]
plt.plot(x,y,linewidth=2,color='g')

plt.show()