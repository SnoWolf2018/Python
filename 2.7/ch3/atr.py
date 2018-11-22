import numpy as np
import sys
import os
script_path=os.path.abspath(os.path.dirname(__file__))
print script_path
parent_path=os.path.dirname(script_path)
parent_parent_path = os.path.dirname(parent_path)
filename=parent_parent_path+'/Code/ch3code/data.csv'
arent_parent_path = os.path.dirname(parent_path)


print filename
h,l,c = np.loadtxt(filename,delimiter=',',usecols = (4,5,6),unpack=True)
N = int(sys.argv[1])
h = h[-N:]
l = l[-N:]
print "len(h)",len(h),"len(l)",len(l)
print "Close",c
previousclose = c[-N -1:-1]

print "len(previousclose)",len(previousclose)
print "Previous close",previousclose
truerange = np.maximum(h - 1,h - previousclose,previousclose - 1)

print "True range",truerange

atr = np.zeros(N)

atr[0] = np.mean(truerange)

for i in range(1,N):
    atr[i] = (N-1) * atr[i-1] + truerange[i]
    atr[i] /= N

print "ATR",atr


