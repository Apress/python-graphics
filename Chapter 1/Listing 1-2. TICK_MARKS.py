# -*- coding: utf-8 -*-
"""
Listing 1-2. TICK_MARKS
"""

import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------plotting area
x1=-10
x2=140
y1=90
y2=-10
plt.axis([x1,x2,y1,y2])
plt.axis('on')

#------------------------------------------------------grid
plt.grid(True,color='b')
plt.title('Tick Mark Sample')

#------------------------------------------------tick marks
xmin=x1
xmax=x2
dx=10
ymin=y1
ymax=y2
dy=-5
plt.xticks(np.arange(xmin, xmax, dx))
plt.yticks(np.arange(ymin, ymax, dy))

plt.show()

