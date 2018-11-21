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
#dates,close=np.loadtxt(filename,delimiter=',',usecols=(1,6),converters={1:datestr2num},unpack=True)
dates,open,high,low,close=np.loadtxt(filename,delimiter=',',usecols=(1,3,4,5,6),converters={1:datestr2num},unpack=True)
print "Dates =",dates
averages = np.zeros(5)
for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close,indices)
    avg = np.mean(prices)
    print "Day",i,"prices",prices,"Average",avg
    averages[i] = avg
top = np.max(averages)
print "Highest average",top
print "Top day of the week",np.argmax(averages)
bottom = np.min(averages)
print "Lowest average",bottom
print "Bottom day of the week",np.argmin(averages)

#Get four week datas
close = close[:16]
dates = dates[:16]
#Get first Monday
first_monday = np.ravel(np.where(dates == 0))[0]
print "The first Monday index is",first_monday
#Get last Friday
last_friday = np.ravel(np.where(dates == 4))[-1]
print "The last Friday index is",last_friday

weeks_indices = np.arange(first_monday,last_friday + 1)
print "Weeks indices initial",weeks_indices
weeks_indices = np.split(weeks_indices,3)
print "Weeks indices after split",weeks_indices

def summarize(a,o,h,l,c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h,a))
    week_low = np.min(np.take(l,a))
    friday_close = c[a[-1]]
    return ("APPL",monday_open,week_high,week_low,friday_close)
weeksummary = np.apply_along_axis(summarize,1,weeks_indices,open,high,low,close)
print "Week weeksummary",weeksummary
np.savetxt("Weeksummary.csv",weeksummary,delimiter=",",fmt="%s")
