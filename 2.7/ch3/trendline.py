#!/usr/bin/env python2
import os
import numpy as np

script_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(script_path)
parent_parent_path = os.path.dirname(parent_path)
filename = parent_parent_path+'/Code/ch3code/data.csv'

from matplotlib.pyplot import plot
from matplotlib.pyplot import show

def fit_line(t,y):
    A = np.vstack([t,np.ones_like(t)]).T
    return np.linalg.lstsq(A,y)[0]

h,l,c = np.loadtxt(filename,delimiter=',',usecols=(4,5,6,),unpack=True)
pivots = (h+l+c)/3
print "Pivots",pivots

t = np.arange(len(c))
sa,sb = fit_line(t,pivots-(h-l))
ra,rb = fit_line(t,pivots+(h-l))
support = sa * t + sb
resistance = ra * t + rb
condition = (c>support) & (c<resistance)
print "Condition",condition
between_bands = np.where(condition)
print support[between_bands]
print c[between_bands]
print resistance[between_bands]
between_bands = len(np.ravel(between_bands))
print "Number points between_bands",between_bands
print "Radio between_bands",float(between_bands)/len(c)

print "Tomorrows support",sa * (t[-1] + 1) + sb
print "Tomorrows resistance",ra * (t[-1] + 1) + rb

a1 = c[c > support]
a2 = c[c < resistance]
print "Number of points between bands 2nd approach",len(np.intersect1d(a1,a2))
plot (t,c)
plot (t,support)
plot (t,resistance)
show ()
