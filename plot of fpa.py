import matplotlib.pyplot as plot

import numpy as np
import math
#sol=[8.016538978270201,79.17992732485537,95.25569854648549,3.4864579125954207,0.10739386797886415,14.337467343889317,96.11686098087182,75.47886707855268]
sol=[6.124403774517331,61.3930464127401,75.26889360707568,2.6789912020912485,0.08274731375749096,10.976158247405593,74.85275651744634,59.37927815661285]
#paper values
#sol=[19.85,70.65,29.35,0.7104,0.6191,29.87,70.50,19.48]
#u=np.arange(10,10**5,100)
u=np.arange(100,10**4,1000)
val=[0 for i in range(len(u))]
k=0
for i,j in zip(u,range(len(u))):
    a=i*1j
    val[j]=10*math.log10(abs((a**0.82 - (a**3*sol[0]+a**2*sol[1]+a**1*sol[2]+a**0*sol[3])/(a**3*sol[4]+a**2*sol[5]+a**1*sol[6]+a**0*sol[7]+1))**2))
    k=k+val[j]

print(k)    
plot.semilogx(u,val)
plot.ylim([-50,200])
plot.xlim([5,10**5])
plot.xlabel("frequency")
plot.ylabel("error")

plot.show()

