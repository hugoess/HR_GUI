# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:43:25 2017

@author: xizhe
"""

import time
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import pylab
from numpy import nan
from tkinter import *
import queue
import sys as _sys
import _thread
import threading
import random



#filename = "20170904" + '.txt'
filename = '20171023_64(vs 66)' + '__High.txt'

#f = open(filename + '.txt')
#line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)

data = np.genfromtxt(filename)


print(data)
delta_time_list = []

for a in data:
    if int(a+1) < len(data):
        if data[a][0] != 'nan' and data[a+1][0] != 'nan':
            delta_time = data[a+1][0] - data[a][0]
            delta_time_list.append(delta_time)
            continue
        if data[a][0] != 'nan' and data[a+1][0] == 'nan':
            continue
        if data[a][0] == 'nan':
            continue

delta_time_list = np.array(delta_time_list)
print(delta_time_list)






#
#
#
#
#
#
#
#def Heart_split(high_or_low_data):
#    global listname, listname_2
#    exec(chkprint(high_or_low_data) + '_split' + '= []')
#    exec(chkprint(high_or_low_data) + '_splitted' + '= []')
##    ttt = eval(chkprint(high_or_low_data) + '_split' + '= []')
#
##    listname = chkprint(high_or_low_data) + '_split'
#
#    for a in range(len(high_or_low_data)):
#        if high_or_low_data[a] == nan:
##            globals()[chkprint(high_or_low_data) + 'global_val']
#            split_number = eval(chkprint(high_or_low_data) + '_split')
#            split_number.append(a)
#        
##        split_number = numpy.array(split_number)
#        numpy_list = np.array(high_or_low_data)
#        splitted_list = eval(chkprint(high_or_low_data) + '_splitted')
#        splitted_list = np.split(numpy_list, split_number)
#            
#
#
#def Heartrate_computation(high_x, high_y, low_x, low_y):
