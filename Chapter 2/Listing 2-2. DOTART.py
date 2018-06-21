# -*- coding: utf-8 -*-
"""
Listing 2-2. DOTART
"""

import matplotlib.pyplot as plt
import numpy as np
import random

plt.axis([-10,140,90,-10])

plt.axis('off')
plt.grid(False)

plt.arrow(0,0,20,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,20,head_length=4,head_width=3,color='k')
plt.text(15,-3,'x')
plt.text(-5,15,'y')

#----------------------------------------------------------------plot Seurat
for x in np.arange(20,40,4):
    for y in np.arange(10,60,4):
        plt.scatter(x,y,s=8,color='b')

#--------------------------------------------------------------plot Mondrian    
for x in np.arange(60,80,1):
    for y in np.arange(10,40,1):
        plt.scatter(x,y,s=8,color='y')
    
for x in np.arange(60,80,1):
    for y in np.arange(40,60):
        plt.scatter(x,y,s=8,color='g')
            
for x in np.arange(65,80,1):
    for y in np.arange(25,30,1):
        plt.scatter(x,y,s=8,color='b')
            
plt.scatter(70,30,s=50,color='r')
            
#------------------------------------------------------------------plot Klee
for x in np.arange(100,120,2):
    for y in np.arange(10,60,2):
        rr=random.randrange(0,100,1)/100
        rg=random.randrange(0,100,1)/100
        rb=random.randrange(0,100,1)/100
        plt.scatter(x,y,s=25,color=(rr,rg,rb))
               
#---------------------------------------------------------------------labels
plt.text(105,67,'Klee')
plt.text(60,67,'Mondrian')
plt.text(21,67,'Seurat')

plt.show()


