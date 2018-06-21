# -*- coding: utf-8 -*-

"""
Listing 2-9. 2DTRANSLATION
"""

import numpy as np
import matplotlib.pyplot as plt

x1=-10
x2=140
y1=90
y2=-10
plt.axis([x1,x2,y1,y2])

plt.axis('on')
plt.grid(True)

plt.title('Translation')

#-----------------------------------------------------------------------pyramid
x=[20,30,40,20]
y=[40,20,40,40]
plt.plot(x,y,color='k')
plt.plot(x,y,color='k')
plt.plot(x,y,color='k')

#-------------------------------------------------------translate pyramid dx=60
x=[60,70,80,60]
plt.plot(x,y,color='g')
plt.plot(x,y,color='g')
plt.plot(x,y,color='g')

#-------------------------------------------------------translate pyramid dy=40
y=[80,60,80,80]
plt.plot(x,y,color='r')
plt.plot(x,y,color='r')
plt.plot(x,y,color='r')

#---------------------------------------------------------------------------box
x=[0,0,5,5,0]
y=[55,50,50,55,55]
plt.plot(x,y,'b')

#-----------------------------------------------------------------translate box
y=[55,50,50,55,55]
for x in np.arange(0,130,10):
    x=[x,x,x+5,x+5,x]
    plt.plot(x,y,'b')

plt.show()

