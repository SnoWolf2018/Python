import sys
import os
import numpy as np

'''path tests'''
#print 'current path'
#print os.getcwd()
#'''Your Shell Path'''
#print os.path.abspath(os.path.dirname(__file__))
#'''Your script Path'''
#
#print 'get upper path'
#print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#print os.path.abspath(os.path.dirname(os.getcwd()))
#print os.path.abspath(os.path.join(os.getcwd(),".."))
#
#print 'get upper upper path'
#print os.path.abspath(os.path.join(os.getcwd(),"../.."))

#script_path=os.path.dirname(__file__)

'''The code upper line cannot run in the script_path'''
script_path=os.path.abspath(os.path.dirname(__file__))
#print script_path
parent_path=os.path.dirname(script_path)
#print parent_path
filename=parent_path+'/Code/ch3code/data.csv'
#print filename


'''Run anywhere in any Linux PC'''
h,l=np.loadtxt(filename,delimiter=',',usecols=(4,5),unpack=True)
'''Run everywhere in Archlinux PC'''
#h,l=np.loadtxt('/home/archlinux/git/python/Code/ch3code/data.csv',delimiter=',',usecols=(4,5),unpack=True)
'''Run in Script Path'''
#h,l=np.loadtxt('../Code/ch3code/data.csv',delimiter=',',usecols=(4,5),unpack=True)
'''Run in Script Upper Path'''
#h,l=np.loadtxt('./Code/ch3code/data.csv',delimiter=',',usecols=(4,5),unpack=True)
print "highest =",np.max(h)
print "lowest =",np.min(l)
print (np.max(h)+np.min(l))/2
print "Spead high price",np.ptp(h)
print "Spead low price",np.ptp(l)

