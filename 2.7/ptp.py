import sys
import os
import numpy as np
#h,l=np.loadtxt('/home/archlinux/git/python/Code/ch3code/data.csv',delimiter=',',usecols=(4,5),unpack=True)

print 'current path'
print os.getcwd()
'''Your Shell Path'''
print os.path.abspath(os.path.dirname(__file__))
'''Your script Path'''

print 'get upper path'
print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print os.path.abspath(os.path.dirname(os.getcwd()))
print os.path.abspath(os.path.join(os.getcwd(),".."))

print 'get upper upper path'
print os.path.abspath(os.path.join(os.getcwd(),"../.."))

h,l=np.loadtxt('../Code/ch3code/data.csv',delimiter=',',usecols=(4,5),unpack=True)
print "highest =",np.max(h)
print "lowest =",np.min(l)
print (np.max(h)+np.min(l))/2
print "Spead high price",np.ptp(h)
print "Spead low price",np.ptp(l)

