# -*- coding: utf-8 -*-
"""
Listing 1-10. TEXT_SAMPLES
"""

import numpy as np
import matplotlib.pyplot as plt

x1=-10
x2=140
y1=90
y2=-10
plt.axis([x1,x2,y1,y2])

plt.axis('on')
plt.grid(False)

plt.title('Text Samples')

#-------------------------------------------------text samples

plt.text(20,10,'small text',size='small')
plt.text(20,15,'normal text')
plt.text(20,20,'large text',size='large')

plt.text(20,30,'large bold text$',size='large',fontweight='bold')
plt.text(20,35,'large bold, italic text',size='large',fontweight='bold',fontstyle='italic')
plt.text(20,40,'large, purple, bold italic text',size='large',fontweight='bold',fontstyle='italic',color=(.5,0,.5))
plt.text(20,45,'large, light purple, bold italic text',size='large',fontweight='bold',fontstyle='italic',color=(.8,0,.8))
plt.text(20,50,'light purple text',color=(.8,0,.8))

plt.text(100,50,'text at 45 degrees',rotation=45,color='k')
plt.text(90,-3,'text at -60 degrees',rotation=-60,color='g')

plt.text(20,65,r'$P(\lambda)=2 \pi c^{2} h\int_{\lambda1}^{\lambda2}\frac{\lambda^{-5}\epsilon}{e^{\frac{hc}{\lambda k t}}-1}d\lambda$',size='large')

plt.show()

