#!/usr/bin/env python2
#_*_ coding:utf-8 _*_
import numpy as np
import os
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

script_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(script_path)
parent_parent_path = os.path.dirname(parent_path)
#print parent_parent_path
filename_VALE=parent_parent_path + '/Code/ch4code/ch4code/VALE.csv'
filename_BHP=parent_parent_path+ '/Code/ch4code/ch4code/BHP.csv'
o,h,l,c= np.loadtxt(filename_BHP,delimiter=',',usecols=(3,4,5,6),unpack=True)

def calc_profit(open,high,low,close):
    #以比开盘价稍低的价格买入
    buy = open * float(sys.argv[1])
    #daily range
    if low < buy < high:
        return (close - buy) / buy
    else:
        return 0
func = np.vectorize(calc_profit)
profits = func(o,h,l,c)
print "profits",profits

real_trades = profits[profits != 0]
print "Number of trades",len(real_trades),round(100.0 * len(real_trades)/len(c),2),"%"
print "Average profits/loss %",round(np.mean(real_trades) * 100,2)

winning_trades = profits[profits > 0]
print "Number of winning_trades",len(winning_trades),round(100.0 * len(winning_trades)/len(c),2),"%"
print "Average profit %",round(np.mean(winning_trades) *100,2)

losing_trades = profits[profits < 0]
print "Number of losing_trades",len(losing_trades),round(100.0 * len(losing_trades)/len(c),2),"%"
print "Average profit %",round(np.mean(losing_trades) *100,2)
