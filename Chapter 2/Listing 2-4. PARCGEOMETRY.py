#dotlines

"""
Listing 2-4. PARCGEOMETRY
"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([-10,140,90,-10])

plt.axis('off')
plt.grid(False)

#---------------------------------------------------coordinate axes
plt.arrow(0,0,20,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,20,head_length=4,head_width=3,color='k')

#------------------------------------------------------------labels
plt.text(16,-3,'x')   
plt.text(-5,17,'y') 
       
#----------------------------------------------------------main arc
xc=20
yc=20
r=40
plt.scatter(xc,yc,color='b',s=5) 

phi1=20*np.pi/180.
phi2=70*np.pi/180.
dphi=(phi2-phi1)/20.
for phi in np.arange(phi1,phi2,dphi):
    x=xc+r*np.cos(phi)
    y=yc+r*np.sin(phi)
    plt.scatter(x,y,s=2,color='g')  
    
plt.plot([xc,xc+r*np.cos(phi1)],[yc,yc+r*np.sin(phi1)],color='k')

x1=xc+(r+3)*np.cos(phi1)
x2=xc+(r+10)*np.cos(phi1)
y1=yc+(r+3)*np.sin(phi1)
y2=yc+(r+10)*np.sin(phi1)
plt.plot([x1,x2],[y1,y2],color='k')

x1=xc+(r+3)*np.cos(phi2)
x2=xc+(r+30)*np.cos(phi2)
y1=yc+(r+3)*np.sin(phi2)
y2=yc+(r+30)*np.sin(phi2)
plt.plot([x1,x2],[y1,y2],color='k')

plt.plot([xc,xc+r*np.cos(phi2)],[yc,yc+r*np.sin(phi2)],color='k')

phihalf=(phi1+phi2)*.5
phi3=phihalf-dphi/2
phi4=phihalf+dphi/2

plt.plot([xc,xc+r*np.cos(phi3)],[yc,yc+r*np.sin(phi3)],color='k')
plt.plot([xc,xc+r*np.cos(phi4)],[yc,yc+r*np.sin(phi4)],color='k')

x1=xc+(r+3)*np.cos(phi3)
x2=xc+(r+15)*np.cos(phi3)
y1=yc+(r+3)*np.sin(phi3)
y2=yc+(r+15)*np.sin(phi3)
plt.plot([x1,x2],[y1,y2],color='k')

x1=xc+(r+3)*np.cos(phi4)
x2=xc+(r+15)*np.cos(phi4)
y1=yc+(r+3)*np.sin(phi4)
y2=yc+(r+15)*np.sin(phi4)
plt.plot([x1,x2],[y1,y2],color='k')

#---------------------------------------------------------P1 arc
dphi=(phi3)/100.
for phi in np.arange(0,phi1/2-3.2*np.pi/180,dphi):
    x=xc+(r+5)*np.cos(phi)
    y=yc+(r+5)*np.sin(phi)
    plt.scatter(x,y,s=.1,color='k')  
    
for phi in np.arange(phi1/2+3.3*np.pi/180,phi1,dphi):
    x=xc+(r+5)*np.cos(phi)
    y=yc+(r+5)*np.sin(phi)
    plt.scatter(x,y,s=.1,color='k')  
    
#---------------------------------------------------------P2 arc
dphi=(phi3)/100.
for phi in np.arange(0,phi2/2-3.2*np.pi/180,dphi):
    x=xc+(r+25)*np.cos(phi)
    y=yc+(r+25)*np.sin(phi)
    plt.scatter(x,y,s=.1,color='k') 
    
    dphi=(phi3)/100.
for phi in np.arange(phi2/2+3.2*np.pi/180,phi2,dphi):
    x=xc+(r+25)*np.cos(phi)
    y=yc+(r+25)*np.sin(phi)
    plt.scatter(x,y,s=.1,color='k')  
    
#----------------------------------------------------------P arc
dphi=(phi3)/100.
for phi in np.arange(0,phi3/2-.5*np.pi/180,dphi):
    x=xc+(r+13)*np.cos(phi)
    y=yc+(r+13)*np.sin(phi)
    plt.scatter(x,y,s=.1,color='k')      
    
dphi=(phi3)/100.
for phi in np.arange(phi3/2+9.*np.pi/180,phi3,dphi):
    x=xc+(r+13)*np.cos(phi)
    y=yc+(r+13)*np.sin(phi)
    plt.scatter(x,y,s=.1,color='k')    

#--------------------------------------------------------dp arc
dphi=(phi3)/100.
for phi in np.arange(phi3+5*dphi,phi3+25*dphi,dphi):
    x=xc+(r+13)*np.cos(phi)
    y=yc+(r+13)*np.sin(phi)
    plt.scatter(x,y,s=.1,color='k')    
    
plt.plot([xc,100],[yc,yc],'k')
plt.plot([xc,xc],[yc,80],'k')

#--------------------------------------------------------labels
plt.text(71,58,'p2',size='small')
plt.text(66,44,'p',size='small')
plt.text(63,29,'p1',size='small')
plt.text(45,66,'dp',size='small')
plt.text(41,26,'r')
plt.text(3,17,'(xc,yc)',size='small')
plt.plot([xc+r*np.cos(phi3),xc+r*np.cos(phi3)],[yc-8,yc+r*np.sin(phi3)],'k:')
plt.plot([xc,xc],[yc-2,yc-8],'k:')
plt.text(25,17,'R*cos(p)',size='small')

plt.plot([xc-8,xc+r*np.cos(phi3)],[yc+r*np.sin(phi3),yc+r*np.sin(phi3)],'k:')
plt.plot([xc-2,xc-8],[yc,yc],'k:')
plt.text(13,27,'R*sin(p)',size='small',rotation=90)

plt.text(49,30,'(x1,y1)',size='small')
plt.text(20,62,'(x2,y2)',size='small')
plt.text(51,49,'(xp,yp)',size='small')

#---------------------------------------------------arrow heads
plt.arrow(47,79,-2,1,head_length=3,head_width=2,color='k')
plt.arrow(62,53,-2,2,head_length=2.9,head_width=2,color='k')
plt.arrow(64,31,-.9,3,head_length=2,head_width=2,color='k')
plt.arrow(52,63,3,-3,head_length=2,head_width=2,color='k')


plt.show()