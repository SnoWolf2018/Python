import sys
import os
import numpy as np

script_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(script_path)
parent_parent_path = os.path.dirname(parent_path)
filename = parent_parent_path+'/Code/ch3code/data.csv'

from matplotlib.pyplot import plot
from matplotlib.pyplot import show
x = np.arange(5)
print "Exp",np.exp(x)
print "Linespace",np.linspace(-1,0,5)

N = int(sys.argv[1])

#weights = np.ones(N)/N
weights = np.exp(np.linspace(-1.,0.,N))
weights /=weights.sum()
print "Weights",weights

c=np.loadtxt(filename,delimiter=',',usecols=(6,),unpack=True)
sma = np.convolve(weights,c)[N-1:-N+1]
t = np.arange(N-1,len(c))
plot(t,c[N-1:],lw=1.0)
plot(t,sma,lw=2.0)
show()


