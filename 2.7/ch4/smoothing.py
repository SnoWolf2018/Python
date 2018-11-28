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
N = int(sys.argv[1])

#weights = np.blackman(N)
#weights = np.bartlett(N)
weights = np.kaiser(N,0)
#weights = np.hanning(N)
print "Weights",weights

bhp = np.loadtxt(filename_BHP,delimiter=',',usecols=(6,),unpack=True)
bhp_returns = np.diff(bhp) / bhp[:-1]
smooth_bhp = np.convolve(weights/weights.sum(),bhp_returns)[N-1:-N+1]

vale = np.loadtxt(filename_VALE,delimiter=',',usecols=(6,),unpack=True)
vale_returns = np.diff(vale) / vale[:-1]
smooth_vale= np.convolve(weights/weights.sum(),vale_returns)[N-1:-N+1]

k = int(sys.argv[1])
t = np.arange(N-1,len(bhp_returns))
poly_bhp = np.polyfit(t,smooth_bhp,k)
poly_vale= np.polyfit(t,smooth_vale,k)
poly_sub = np.polysub(poly_bhp,poly_vale)
xpoints = np.roots(poly_sub)
print "Intersection points",xpoints

reals = np.isreal(xpoints)
print "Real number?",reals

xpoints = np.select([reals],[xpoints])
xpoints = xpoints.real
print "Real intersection points",xpoints
print "Sans 0s",np.trim_zeros(xpoints)

plot(t,bhp_returns[N-1:],lw=1.0)
plot(t,smooth_bhp,lw=2.0)

plot(t,vale_returns[N-1:],lw=1.0)
plot(t,smooth_vale,lw=2.0)
show()

