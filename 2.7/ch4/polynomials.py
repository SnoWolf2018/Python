#!/usr/bin/env python2
import numpy as np
import os
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

script_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(script_path)
parent_parent_path = os.path.dirname(parent_path)
print parent_parent_path
filename_VALE=parent_parent_path + '/Code/ch4code/ch4code/VALE.csv'
filename_BHP=parent_parent_path+ '/Code/ch4code/ch4code/BHP.csv'
bhp = np.loadtxt(filename_BHP,delimiter=',',usecols=(6,),unpack=True)
bhp_returns = np.diff(bhp) / bhp[:-1]
vale = np.loadtxt(filename_VALE,delimiter=',',usecols=(6,),unpack=True)
vale_returns = np.diff(vale) / vale[:-1]

t = np.arange(len(bhp))
poly = np.polyfit(t,bhp-vale,int(sys.argv[1]))
print "Polynomial fit",poly

print "Next value",np.polyval(poly,t[-1]+1)

print "Roots",np.roots(poly)
der = np.polyder(poly)
print "Derivative",der

print "Extremas",np.roots(der)
vals = np.polyval(poly,t)
print np.argmax(vals)
print np.argmin(vals)

plot(t,bhp-vale,lw=1)
plot(t,vals,lw=1)
show()

