 # -*- coding: utf-8 -*-
"""
Listing 1-4. COLORS
"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0,100,0,10])

for x in np.arange(1,100,1):
    r=x/100
    g=0
    b=0
    plt.plot([x,x],[0,10],linewidth=5,color=(r,g,b))
    
plt.show()