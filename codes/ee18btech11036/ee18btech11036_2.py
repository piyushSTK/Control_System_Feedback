#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:24:48 2020

@author: Piyush Kumar Uttam
Released under GNU-GPl 
"""

import numpy as np
import matplotlib.pyplot as plt
import control
from scipy import signal

#if using termux
import subprocess
import shlex
#end if

p1= 2*np.pi*1e4
p2= 2*np.pi*1e5
H= ((p1-p2)**2)/(4000*p1*p2)


num = [1000]
den = [(1/(p1*p2)), ((1/p1)+(1/p2)), (1000*H+1)]
#den=[(1e-9), (11*1e-5), 3.025]
sys=control.tf(num,den)
s = signal.lti(num,den)
w, mag, phase =signal.bode(s)


pole, zero = control.pzmap(sys, Plot=True, title='Pole Zero Map')
print ("Poles are :",pole)
gain_y=np.full((len(w)),44.3866)
x_val= abs(pole[0])
y_val= 44.3866

plt.figure()
plt.plot(w,mag)
plt.plot(w, gain_y)
plt.plot(x_val, y_val, 'ro')
plt.text(x_val, y_val, "(345575, 44.3866)")
plt.grid()

print ("Low frequency Gain ",mag[0])
print("Gain at crossover frequency dB ", 44.3866)

plt.savefig('./figs/ee18btech11036/ee18btech11036_2.pdf')
plt.savefig('./figs/ee18btech11036/ee18btech11036_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11036/ee18btech11036_2.pdf"))
#else
#plt.show()
