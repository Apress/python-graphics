# -*- coding: utf-8 -*-
"""
Listing 10-2. BANDINTEGRAL
"""

import numpy as np, matplotlib.pyplot as plt

plt.close('all')

#----------------------------------------------setup axes
ymax=20
plt.axis([1.,2.,0,ymax])
plt.xlabel('Wavelength $\lambda$ ($\mu$m)')
plt.ylabel('S($\lambda$) (MW/m$^{3}$) x 10^-6')
plt.grid(True)
plt.title('Max Plancks Solar Spectrum - Band Integral')

#------------------------------------establish parameters
c=2.9979*(10.**8)      # speed of light in a vacuum m/s
h=6.63*(10.**-34)      # Planck's constant J.s
kb=1.38*(10**-23)      # Boltzmann's constant J/K

t=5800.
e=1.                   # emissivity
lamin=.01*10**-6      # starting wavelength m
lamax=2.*10**-6        # ending wavelength m
dla=.01*10**-6         # incremental wavelength m

#------------------------------------------- plot sl curve
for la in np.arange(lamin,lamax,dla):   
    a1=2.*np.pi*c*c*h/(la**5.)
    a2=h*c/(la*kb*t)
    sl=e*a1/(np.exp(a2)-1.)   # J/s/m^3 = W/m^3
    sl=sl*10**-6              # MW/m^3
    slg=sl*10**-6             # scale to plot at 10^-6 scale
    lag=la*10**6              # scale to plot at 10^+6 scale
    plt.scatter(lag,slg,s=1,color='r') 
     
#---------------------------------------------- plot band
plt.plot([1.495,1.495],[0.,11.64],color='g') 
plt.plot([1.4975,1.4975],[0.,11.64],color='g')           
plt.plot([1.5,1.5],[0,11.64],color='g')  
plt.plot([1.5025,1.5025],[0.,11.64],color='g')
plt.plot([1.5050,1.505],[0.,11.64],color='g')  

#------------------------ plot temperature and emissivity
d=str(t)    
plt.text(1.6,15,'T=')
plt.text(1.65,15,d)
plt.text(1.6,14,'e=')
d=str(e)
plt.text(1.65,14,d)

#---------------calculate s and power pl at lambda=1.5 um
la=1.5*10**-6
a1=2.*np.pi*c*c*h/(la**5.)
a2=h*c/(la*kb*t)
sl=e*a1/(np.exp(a2)-1.) # J/s/m^3 = W/m^3
sl=sl*10**-6            # MW/m^3
dl=.01*10**-6           # band width m
pl=sl*dl                # band power output MW/m^2

#---------------------------------plot results and labels
plt.plot([1.53,1.59],[11.6,11.6],'k')
plt.text(1.6,11.5,'s$_{i}$=')
d='%7.3e'%(sl)
plt.text(1.65,11.5,d)
plt.text(1.83,11.5,'MW/m^3')
    
plt.arrow(1.4,5,.085,0,head_width=.5,head_length=.01,linewidth=.2)
plt.arrow(1.6,5,-.085,0,head_width=.5,head_length=.01,linewidth=.2)

plt.text(1.1,5,'$\Delta \lambda$=')
dle='%7.3e'% (dl)
dls=str(dle)
plt.text(1.18,5,dls)
plt.text(1.35,5,'m')

plt.text(1.145,4,'=')
dl=dl*10**6
dle='%7.3e'%(dl)
dls=str(dle)
plt.text(1.18,4,dls)
plt.text(1.35,4,'um')

plt.text(1.35,16.5,'s($\lambda$)')
plt.text(1.52,2.5,'power$_{i}$=')
pl='%7.3e'% (pl)
pl=str(pl)
plt.text(1.65,2.5,pl)
plt.text(1.823,2.5,'MW/m^2')
plt.text(1.45,-1.1,'$\lambda_{i}$=1.5')
   
plt.show()