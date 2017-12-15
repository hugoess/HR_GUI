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
from statistics import mean, median,variance,stdev




filedate = ['20171023_64(vs 00)', '20171023_64(vs 66)']


#file_high_or_low = '__High.txt'
file_high_or_low = ['__Low.txt', '__High.txt']


#filename = "20170904" + '.txt'
#filename = filedate1 + file_high_or_low1
def shinpaku(filename):
    #f = open(filename + '.txt')
    #line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)
    
    data = np.genfromtxt(filename)
    
    
    #print(data)
    delta_time_list = []
    #delta_time_average = np.array(delta_time_average)
    
    for a in range(len(data)):
        if a+1 < len(data):
            if str(data[a][0]) != 'nan' and str(data[a+1][0]) != 'nan':
                delta_time = data[a+1][0] - data[a][0]
                delta_time_list.append(delta_time)
    
    #        if data[a][0] != 'nan' and data[a+1][0] == 'nan':
    #            continue
    #delta_time_average = []
    #        if data[a][0] == 'nan':
    #            continue
    
    delta_time_list = np.array(delta_time_list)
    
    m = mean(delta_time_list)
    median1 = median(delta_time_list)
    variance1 = variance(delta_time_list)
    stdev1 = stdev(delta_time_list)
    
    
    print(filename)
    print('平均: {0:.4f}'.format(m))
    print('中央値: {0:.4f}'.format(median1))
    print('分散: {0:.4f}'.format(variance1))
    print('標準偏差: {0:.4f}'.format(stdev1) + '\n')
    
    filename_date = filename[:]
    f = open(, 'a')
    f.write(filename+ '\n'\
            '平均: {0:.4f}'.format(m) + '\n'\
            '中央値: {0:.4f}'.format(median1) + '\n'\
            '分散: {0:.4f}'.format(variance1) + '\n'\
            '標準偏差: {0:.4f}'.format(stdev1) + '\n')
    f.close()
    
    
    
#
for a in filedate:
    filedate1 = a
    for b in file_high_or_low:
        file_high_or_low1 = b
        filename = filedate1 + file_high_or_low1
        shinpaku(filename)        



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
