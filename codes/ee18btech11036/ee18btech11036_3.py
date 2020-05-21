#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:47:49 2020


@author: Piyush Kumar Uttam
Released under GNU-GPl 
"""

import numpy as np
import matplotlib.pyplot as plt
import control
from scipy import signal
import cmath
#if using termux
import subprocess
import shlex
#end if

p1= 2*np.pi*1e4
p2= 2*np.pi*1e5
H= 10*((p1-p2)**2)/(4000*p1*p2)


num = [1000]
den = [(1/(p1*p2)), ((1/p1)+(1/p2)), (1000*H+1)]
#den=[(1e-9), (11*1e-5), 3.025]
sys=control.tf(num,den)



pole, zero = control.pzmap(sys, Plot=False)
print ("Poles are :",pole)
x=(pole.real)
y=(pole.imag)
plt.plot(x,y)
plt.plot( x[0], y[0], marker="X")
plt.plot( x[1], y[1], marker="X")
plt.grid()
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.savefig('./figs/ee18btech11036/ee18btech11036_3.pdf')
plt.savefig('./figs/ee18btech11036/ee18btech11036_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11036/ee18btech11036_3.pdf"))
#else
#plt.show()