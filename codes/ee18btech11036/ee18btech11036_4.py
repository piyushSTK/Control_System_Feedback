# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:11:25 2020

@author: Piyush Kumar Uttam
Released under GNU-GPl 
"""


import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if
p1= 2*np.pi*1e4
p2= 2*np.pi*1e5
H= ((p1-p2)**2)/(4000*p1*p2)
num = [1000]
den = [(1/(p1*p2)), ((1/p1)+(1/p2)), (1000*H+1)]
Transfer_function = signal.lti(num, den)
T, ystep = signal.step(Transfer_function)	
plt.plot(T,(ystep))
plt.grid()
plt.title("Step response")
plt.xlabel("Time")
plt.ylabel("y(t)")
plt.grid()
#if using termux
plt.savefig('./figs/ee18btech11036/ee18btech11036_4.pdf')
plt.savefig('./figs/ee18btech11036/ee18btech11036_4.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11036/ee18btech11036_4.pdf"))
#else
#plt.show()