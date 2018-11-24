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
c,v= np.loadtxt(filename_BHP,delimiter=',',usecols=(6,7),unpack=True)

change = np.diff(c)
print "Change",change

signs = np.sign(change)
print "Signs",signs

pieces = np.piecewise(change,[change<0,change>0],[-1,1])
print "Pieces",pieces

print "Arrays equal?",np.array_equal(signs,pieces)
print "On balance volume",v[1:] * signs
