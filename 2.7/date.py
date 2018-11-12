#!/usr/bin/env python2
#_*_ coding:utf-8 _*_
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
#dates,close=np.loadtxt(filename,delimiter=',',usecols=(1,6),converters={1,datestr2num},unpack=True)
'''Run everywhere in Archlinux PC'''
#h,l=np.loadtxt('/home/archlinux/git/python/Code/ch3code/data.csv',delimiter=',',usecols=(4,5),unpack=True)
'''Run in Script Path'''
#h,l=np.loadtxt('../Code/ch3code/data.csv',delimiter=',',usecols=(4,5),unpack=True)
'''Run in Script Upper Path'''
#h,l=np.loadtxt('./Code/ch3code/data.csv',delimiter=',',usecols=(4,5),unpack=True)
#print "highest =",np.max(h)
#print "lowest =",np.min(l)
#print (np.max(h)+np.min(l))/2
#print "Spead high price",np.ptp(h)
#print "Spead low price",np.ptp(l)
#vwap=np.average(h,weights=l)
#print "vwap =",vwap
#print "mean =",np.mean(h)
#t=np.arange(len(h))
#print "twap =",np.average(h,weights=t)
#print "median =",np.median(h)
#sorted_close=np.msort(h)
#print "sorted =",sorted_close
#N = len(h)
#print "middle =",sorted_close[(N-1)/2]
#print "middle =",(sorted_close[(N-1)/2]+sorted_close[N/2])/2
#print "variance =",np.var(h)
#print "variance from definition =",np.mean((h-h.mean())**2)

#import datetime
from datetime import datetime
#星期一 0
#星期二 1
#星期三 2
#星期四 3
#星期五 4
#星期六 5
#星期日 6
'''
#星期一 0
#星期二 1
#星期三 2
#星期四 3
#星期五 4
#星期六 5
#星期日 6
'''
def datestr2num(s):
    return datetime.strptime (s,"%d-%m-%Y").date().weekday()
'''Run anywhere in any Linux PC'''
dates,close=np.loadtxt(filename,delimiter=',',usecols=(1,6),converters={1:datestr2num},unpack=True)
print "Dates =",dates
