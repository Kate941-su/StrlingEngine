# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:05:05 2021

@author: valle
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker
fp = FontProperties(fname=r'C:\WINDOWS\Fonts\YuGothR.ttc', size=14)

ome=np.loadtxt("./plotdata/billdata/delta3.dat",comments="!",usecols=1)
ome_=np.loadtxt("./plotdata/billdata/omega.dat",comments="!",usecols=1)
ome_0=np.loadtxt("./plotdata/billdata/omega_noreg.dat",comments="!",usecols=1)
ome_4=np.loadtxt("./plotdata/billdata/omega4_noreg.dat",comments="!",usecols=1)
t=[]

ome2=[]
for i in range(len(ome)):
    if i%10 == 0 and i<75000 :
        ome2.append(ome[i])

ome2=-np.array(ome2)
ome_=-ome_

ome__=[]
ome_00=[]
ome_44=[]
for i in range(len(ome_)):
    if i<7500:
        ome__.append(ome_[i])
        ome_00.append(ome_0[i])
        ome_44.append(ome_4[i])
ome__=np.array(ome__)
ome_00=-np.array(ome_00)
#ome_00=-ome_00
ome_44=-np.array(ome_44)
#ome_44=-ome_44
for i in range(1,len(ome)+2):
    if i<=7500 :
        t.append(100*i)    


plt.xlabel("Time t", fontsize=20)
plt.ylabel("Angular velocity ω", fontsize=18)
plt.plot(t,ome__,label="モデルⅠ")
plt.plot(t,ome_44,label="モデルⅠ")

plt.plot(t,ome_00,label="モデルⅡ")
plt.plot(t,ome2,label="モデルⅡ")
#label="モデルⅡ"


plt.gca().ticklabel_format(style="sci", scilimits=(0,0), axis="x")


#plt.legend(prop=fp,fontsize=20,loc="lower left")

plt.legend(bbox_to_anchor=(1.05, 1),prop=fp,fontsize=20,loc="upper left")

plt.tick_params(labelsize=12)


plt.savefig("./omega.png")
plt.show()


