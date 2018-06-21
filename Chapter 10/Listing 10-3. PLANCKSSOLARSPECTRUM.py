# -*- coding: utf-8 -*-
"""
Listing 10-3. PLANCKSSOLARSPECTRUM
"""

import numpy as np, matplotlib.pyplot as plt

plt.close('all')

plt.axis([0,3,0,100])
plt.xlabel('Wavelength $\lambda$ ($\mu$m)')
plt.ylabel('S($\lambda$) (MW/m$^{3}$) x 10^-6')
plt.grid(True)
plt.title('Max Plancks Solar Spectrum')

c=2.9979*(10.**8)     #m/s - speed of light in a vacuum
h=6.63*(10.**-34)     #Js  - Planck's constant
kb=1.38*(10**-23)     #J/K - Boltzmann's constant
e=.985                #emissivity

t=5800.
e=.984
lamin=.01*10**-6
lamax=10.*10**-6
dla=.01*10**-6
st=0.

for la in np.arange(lamin,lamax,dla):
    a1=2.*np.pi*c*c*h/(la**5.)
    a2=h*c/(la*kb*t)
    sl=e*a1/(np.exp(a2)-1.) 
    sl=sl*10**-6
    st=st+sl*dla  #calculate area under the slcurve MW/m^2
    slg=sl*10**-6                #scale to plot 
    lag=la*10**6
    plt.scatter(lag,slg,s=1,color='r')  
             
       
ds=1.39*10**9           #suns diameter m
spas=np.pi*ds**2.       #suns spherical area m2
to=spas*st              #suns total output MW
to=to*10**6             # W
        
plt.text(.8,58.,'5800')
plt.text(1.05,58, '$^{\circ}$K') 
plt.plot([.39,.39],[-0.,100.],'b--')
plt.plot([.7,.7],[-0.,100.],'b--')
plt.text(.3,-10,'.390')
plt.text(.6,-10,'.700')
plt.text(.15,90.,'UV')
plt.text(.8,90.,'long wave infrared')
plt.arrow(1.75,91.,.8,0.,head_width=1.,head_length=.1,color='r')
plt.text(1.2,40.,'total solar output =')
so='%7.3e'% (to)
dd=str(so)
plt.text(2.1,40,dd)
plt.text(2.7,40,'W')
plt.text(1.2,34,'emissivity =')
e=str(e)
plt.text(1.8,34,e)

plt.text(.5,75.,'v')
plt.text(.53,70.,'i')
plt.text(.5,65.,'s')
plt.text(.53,60.,'i')
plt.text(.5,55.,'b')
plt.text(.53,50.,'l')
plt.text(.5,45.,'e')

plt.plot([1.49,1.49],[0.,11.61],color='g')
plt.plot([1.5,1.5],[0.,11.61],color='g')
plt.plot([1.51,1.51],[0.,11.61],color='g')

laband=1.5*10**-6
a1=2.*np.pi*c*c*h/(laband**5.)
a2=h*c/(laband*kb*t)
sband=a1/(np.exp(a2)-1.)
sband=sband*10**-12
pband=sband*dla                                       #MW/sq meter
pband=pband*10**6                                     #W/sq meter

plt.plot([1.55,1.7],[12.5,15.],color='k')
plt.text(1.72,14.,' p=')
pband='%7.3e'%(pband)
pband=str(pband)
plt.text(1.9,14,pband)
plt.text(2.4,14,'MW/m^2')

plt.arrow(1.35,5,.1,0,head_width=1, head_length=.05, ec='k', fc='k')
plt.arrow(1.65,5,-.1,0,head_width=1, head_length=.05, ec='k', fc='k')
plt.text(.82,4.9,'$\Delta \lambda=.01\mu m$' )




plt.show()