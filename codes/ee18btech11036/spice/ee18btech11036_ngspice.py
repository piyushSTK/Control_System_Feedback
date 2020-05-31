"""
Created on Sun May 17 14:54:25 2020

@author: Piyush Kumar Uttam
Released under GNU-GPl 
"""
import numpy as np  
from matplotlib import pyplot as plt  

#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11036.dat')  #loading the data from the simulation output
plt.plot(data[:,0],30.31*data[:,1])  
plt.grid()
plt.xlabel("time")
plt.ylabel("unit step response")
plt.title("Output from spice simulation")

#if using termux
plt.savefig('./figs/ee18btech11036/ee18btech11036_spice.pdf')
plt.savefig('./figs/ee18btech11036/ee18btech11036_spice.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11036/ee18btech11036_spice.pdf"))
#else
#plt.show()
