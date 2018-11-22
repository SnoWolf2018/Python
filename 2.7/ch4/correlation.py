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

covariance = np.cov(bhp_returns,vale_returns)
print "Convariance",covariance

print "Covariance diagonal",covariance.diagonal()
print "Covariance trace",covariance.trace()

print covariance/(bhp_returns.std() * vale_returns.std())

print "Covariance coefficient",np.corrcoef(bhp_returns,vale_returns)

difference = bhp -vale
avg = np.mean(difference)
dev = np.std(difference)

print "Out of sync",np.abs(difference[-1] - avg) > 2 * dev

t = np.arange(len(bhp_returns))
plot(t,bhp_returns,lw=1)
plot(t,vale_returns,lw=1)
show()

