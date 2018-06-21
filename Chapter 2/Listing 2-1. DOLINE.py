# -*- coding: utf-8 -*-
"""
Listing 2-1. DOTLINE
"""

import matplotlib.pyplot as plt
import numpy as np

plt.axis([0,150,100,0])

plt.axis('on')
plt.grid(True)

plt.arrow(0,0,20,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,20,head_length=4,head_width=3,color='k')

plt.text(15,-3,'x')
plt.text(-5,15,'y')

plt.plot([60,120],[50,20],linewidth=.5,color='k')
plt.arrow(40,60,17,-8.5,head_length=3,head_width=2,color='b')

plt.arrow(44,70,-.5,0,head_length=2,head_width=1.5,color='k')
plt.plot([73,40],[70,70],linewidth=.5,color='k')

plt.arrow(117.5,70,.5,0,head_length=2,head_width=1.5,color='k')
plt.plot([87,118],[70,70],linewidth=.5,color='k')

plt.plot([63,120],[60,60],linewidth=1,color='k')
plt.plot([120,120],[60,20],linewidth=1,color='k')
plt.plot([40,60],[60,60],linewidth=1,color='b')
plt.plot([60,60],[60,50],linewidth=1,color='b')

plt.plot([39,30],[58,40],linewidth=.5,color='k')
plt.plot([119,110],[18,0],linewidth=.5,color='k')

plt.plot([40,40],[62,75],linewidth=1,color='k')
plt.plot([120,120],[62,75],linewidth=1,color='k')

plt.plot([123,135],[60,60],linewidth=1,color='k')
plt.plot([123,135],[20,20],linewidth=1,color='k')
plt.plot([130,130],[45,60],linewidth=1,color='k')
plt.plot([130,130],[35,20],linewidth=1,color='k')
plt.arrow(130,22.5,0,-.5,head_length=2,head_width=1.5,color='k')
plt.arrow(130,58,0,.5,head_length=2,head_width=1.5,color='k')

plt.plot([68,32],[26.5,44.3],linewidth=.5,color='k')
plt.plot([77,112],[22,4],linewidth=.5,color='k')
plt.arrow(36,42.3,-2,1,head_length=2,head_width=1.5,color='k')
plt.arrow(108,6,2,-1,head_length=2,head_width=1.5,color='k')

plt.text(70,25,'Q',rotation=30,color='k')
plt.text(79,72,'A',color='k')
plt.text(128,42,'B',color='k')
plt.text(33,62,'1',color='k',fontweight='bold')
plt.text(122,18,'2',color='k',fontweight='bold')
plt.scatter(40,60,s=30,color='k')
plt.scatter(120,20,s=30,color='k')
plt.text(48,64,'ux',color='k')
plt.text(61,56.5,'uy',color='k')
plt.text(48,52,'u',fontweight='bold',rotation=30,color='k')

plt.show()
