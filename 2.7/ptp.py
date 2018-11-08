import numpy as np
h,l=np.loadtxt('/home/archlinux/git/python/Code/ch3code/data.csv',delimiter=',',usecols=(4,5),unpack=True)
print "highest =",np.max(h)
print "lowest =",np.min(l)
print (np.max(h)+np.min(l))/2
print "Spead high price",np.ptp(h)
print "Spead low price",np.ptp(l)

