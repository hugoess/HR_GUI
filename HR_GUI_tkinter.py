#from getch import getch, pause
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




#change test for Github 
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

import sys



#dir = "C:\\Users\\lab\\Desktop\\heartrate"
#dir = "C:\\Users\\Hosokawa\\Dropbox\\＜やること＞\\心拍データ処理"
dir = "C:\\Users\\admin\\Desktop\\サルビデオ解析\\heartbeat rate"
import sys; sys.path.append(dir)
#import subfuncs as myfunc

import matplotlib
matplotlib.use('TkAgg')




#--------------------------------------------------------------
#%%
filename = "20171023_64(vs 66).lvm"

f = open(filename)
line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)

v_time          = []
v_time_1        = []
v_volt_hb       = []
v_volt_hb_1     = []
v_volt_on_off   = []
v_volt_on_off_1 = []

# サンプリング間隔
sampling = 0
ptn1 = re.compile(r"Delta_X\t([0-9]+\.[0-9]+)\t([0-9]+\.[0-9]+)")
# データ部分の正規表現（時間<tab>電圧）
ptn2 = re.compile(r"([0-9]+\.[0-9]+)\t([0-9]+\.[0-9]+)\t([0-9]+\.[0-9]+)")
while line:
    matched_list1 = re.findall(ptn1, line)
    if len(matched_list1) > 0:
        sampling = float(matched_list1[0][0])
    matched_list2 = re.findall(ptn2, line)
    if len(matched_list2) > 0:
        v_time.append(float(matched_list2[0][0]))
        v_volt_hb.append(float(matched_list2[0][1]))
        v_volt_on_off.append(float(matched_list2[0][2]))
    line = f.readline()
    
f.close
#%%

v_time = np.array(v_time)
#time_1 = np.array(time)
v_volt_hb = np.array(v_volt_hb)
v_volt_on_off = np.array(v_volt_on_off)

v_data_1=[]   #この配列の0番、2番、4番などの偶数インデックスが対応する値の後がOn_OFFのHighの時、2番が２２２で、3番が３３３の場合、222から３３２までが
v_data_2=[]

for n in range(len(v_volt_on_off)):

    if ((v_volt_on_off[n-1] <= 5) and (v_volt_on_off[n] >= 8)) or ((v_volt_on_off[n-1] >= 8) and (v_volt_on_off[n] <= 5)):
        v_data_1.append(n) 
#    if (v_volt_on_off[n-1] >= 8) and (v_volt_on_off[n] <= 5) :
#        v_data_2.append(n)

volt_hb_splitted = np.split(v_volt_hb, v_data_1)



volt_hb_low =[]
volt_hb_high=[]

def is_guusuu(xx:list, yy:list):
    for x in range(len(volt_hb_splitted)):
        if x % 2 == 0:            
            xx.extend(volt_hb_splitted[x])
            xx.extend(np.array([nan]))
        if x % 2 == 1:
            yy.extend(volt_hb_splitted[x])
            yy.extend(np.array([nan]))


is_guusuu(volt_hb_low, volt_hb_high)

volt_hb_low = np.array(volt_hb_low)
volt_hb_high = np.array(volt_hb_high)



        
        
#        
#        time_1.append(time[n])
#        volt_hb_1.append(volt_hb[n])
#        
        
        
#        volt_on_off_1.append(volt_on_off[n])
        



#%%
t2 = v_time[1:200]
v2 = v_volt_hb[1:200]

#plt.plot(time, volt_hb)
#plt.plot(t2, v2)
#plt.plot(time, high_cut_filter(volt, sampling, 2, 4))

#def a():
#    print(time)
#
#a()

#import pdb; pdb.set_trace();

#%%
#fig, ax = plt.subplots()
#ax.plot(t2, v2, 'o-', picker=2)
#
#def onpick(event):
##    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
##          ('double' if event.dblclick else 'single', event.button,
##           event.x, event.y, event.xdata, event.ydata))
#    thisline = event.artist
#    xdata = thisline.get_xdata()
#    ydata = thisline.get_ydata()
#    ind = event.ind
#    points = tuple(zip(xdata[ind], ydata[ind]))
#    print('onpick points:', points)
#
#
#fig.canvas.mpl_connect('pick_event', onpick)

#def on_pick(event):
#    line = event.artist
#    xdata, ydata = line.get_data()
#    ind = event.ind
#    print('on pick line:', np.array([xdata[ind], ydata[ind]]))

def on_pick(event):
    line = event.artist
    xdata, ydata = line.get_data()
    ind = event.ind
#    print('on pick line:', np.array([xdata[ind], ydata[ind]]).T)
    print([xdata[ind], ydata[ind]])
#    kkk = np.array([xdata[ind], ydata[ind]])
    f = open('result.txt', 'a')
    f.write(str(xdata[ind][0]) + '\t' + str(ydata[ind][0]) + '\n')
    f.close()

i = 1
fig = Figure(figsize=(12,6))
ax = fig.add_subplot(111)
#i_200 = 1
#i_400 = 200


def add_nan(event):
    f = open('result.txt', 'a')
    f.write('nan'+ '\t' +'\n')
    f.close()
    print('nan')


def next_page():

    global ax, fig, canvas, t2, v2, window, i_200, i_400, i,volt_hb_high, volt_hb_low
#    global ax, fig, canvas, t2, v2, window,
#    nonlocal ax, fig, canvas, t2, v2, window, i_200, i_400

    i = i+1
    i_200 = (i-1)*200+1
    i_400 = i*200
    t2 = v_time[i_200:i_400]
    v2 = volt_hb_high[i_200:i_400]
#    if qqq == 1: 
#        t2 = v_time[i_200:i_400]
#        v2 = volt_hb_low[i_200:i_400]
#        print(qqq)
#    else:
#        t2 = v_time[i_200:i_400]
#        v2 = volt_hb_high[i_200:i_400]   
    
    print('%d ~ %d' % (i_200,i_400))
    ax.clear()
    plot()
    
def previous_page():
    
    global ax, fig, canvas, t2, v2, window, i_200, i_400, i,volt_hb_high, volt_hb_low
#    global ax, fig, canvas, t2, v2, window
#    nonlocal ax, fig, canvas, t2, v2, window, i_200, i_400

    i = i -1
    i_200 = (i-1)*200+1
    i_400 = i*200
    t2 = v_time[i_200:i_400]
    v2 = volt_hb_high[i_200:i_400]
#    if qqq == 1: 
#        t2 = v_time[i_200:i_400]
#        v2 = volt_hb_low[i_200:i_400]
#        print(qqq)
#    else:
#        t2 = v_time[i_200:i_400]
#        v2 = volt_hb_high[i_200:i_400]        
        
    print('%d ~ %d' % (i_200,i_400))
    ax.clear()
    plot()

def count_low():
    
    pass
    global ax, fig, canvas, t2, v2, window, i_200, i_400, i

    v2 = volt_hb_low[1:200]
    
    
def count_high():
    
    pass
    global ax, fig, canvas, t2, v2, window, i_200, i_400, i
    





def plot():
#        t2 = v_time[1:200]
#        v2 = v_volt_hb[1:200]
    global ax, fig, canvas, t2, v2, window, i_200, i_400, i,v_volt_high, v_volt_low
#    global ax, fig, canvas, t2, v2, window
#    nonlocal ax, fig, canvas, t2, v2, window, i_200, i_400

#    fig = Figure(figsize=(6,6))
#    ax = fig.add_subplot(111)
    ax.plot(t2, v2, 'o-', picker=1)
#    ax.invert_yaxis()

    
    pretitle =('%d ~ %d' % (i_200,i_400))
    ax.set_title (str(pretitle), fontsize=16)
    ax.set_ylabel("Voltage", fontsize=14)
    ax.set_xlabel("Time(s)", fontsize=14)


#    canvas = FigureCanvasTkAgg(fig, master=window)
#    canvas.get_tk_widget().pack()
    canvas.draw()
#    fig.canvas.draw()
#        fig.canvas.mpl_connect('pick_event', onpick)
    fig.canvas.mpl_connect('pick_event', on_pick)
#    print('hi')
#    print(t2)

window= Tk()
button = Button(window, text="check", command=plot)
button.grid(row = 0)
#button_2 = Button(window, text='Previous Page', accelerator = 'D', command = previous_page)
button_2 = Button(window, text='Previous Page', command = previous_page)

button_2.grid(row = 1, column = 0, sticky = W)
#button_1 = Button(window, text='Next Page', accelerator = 'A', command = next_page)
button_1 = Button(window, text='Next Page', command = next_page)

button_1.grid(row = 1, column = 0, sticky = E)

qqq = IntVar()

radio_1 = Radiobutton(window, text = 'Low', command = count_low, variable = qqq, value = 1)
#radio_1.deselect()
radio_1.grid(row=0, column= 0, sticky = W)
radio_2 = Radiobutton(window, text = 'High', command = count_high, variable = qqq, value = 2)
#radio_2.deselect()
radio_2.grid(row=0, column= 0, sticky = E)
#l = Label(root, text = '')
#l.pack()



quitbtn = Button(window, text = 'Quit', command = window.destroy)
quitbtn.grid(row = 2)
canvas = FigureCanvasTkAgg(fig, master=window)


#canvas.bind('<Button-3>', add_nan)

canvas.get_tk_widget().bind('<Button-3>', add_nan)
canvas.get_tk_widget().grid(row = 3)






window.title('HR Counter')
window.geometry('1200x700')
#start= mclass (window)

window.mainloop()




#cid = fig.canvas.mpl_connect('button_press_event', onclick)

#
#def on_pick(event):
#    line = event.artist
#    xdata, ydata = line.get_data()
#    ind = event.ind
#    print('on pick line:', np.array([xdata[ind], ydata[ind]]).T)
#


#cid = fig.canvas.mpl_connect('pick_event', on_pick)

    
        

#以下ポイントピック
#line, = ax.plot(np.random.rand(100), 'o', picker=5) 
#
#def onpick(event):
#    thisline = event.artist
#    xdata = thisline.get_xdata()
#    ydata = thisline.get_ydata()
#    ind = event.ind
#    points = tuple(zip(xdata[ind], ydata[ind]))
#    print('onpick points:', points)
#
#fig.canvas.mpl_connect('pick_event', onpick)
#
#plt.show()




#class mclass:
#    def __init__(self,  window):
#        self.window = window
#        self.button = Button (window, text="check", command=self.plot)
#        self.button.pack()
#        self.button_1 = Button(window, text='Next Page', command = next_page)
#        self.button_1.pack()
#    
#    def next_page():
#        i = 1
#        i_200 = i*200+1
#        i_400 = (i+1)*200
#        t2 = v_time[i_200:i_400]
#
#    def on_pick(self, event):
#        line = event.artist
#        xdata, ydata = line.get_data()
#        ind = event.ind
#        print('on pick line:', np.array([xdata[ind], ydata[ind]]))
#
#
#    def plot(self):
##        t2 = v_time[1:200]
##        v2 = v_volt_hb[1:200]
#        
#        fig = Figure(figsize=(6,6))
#        ax = fig.add_subplot(111)
#        ax.plot(t2, v2, 'o-', picker=1)
#        ax.invert_yaxis()
#    
#        ax.set_title ("1~1000", fontsize=16)
#        ax.set_ylabel("Voltage", fontsize=14)
#        ax.set_xlabel("Time(s)", fontsize=14)
#    
#        canvas = FigureCanvasTkAgg(fig, master=self.window)
#        canvas.get_tk_widget().pack()
#        canvas.draw()
##        fig.canvas.mpl_connect('pick_event', onpick)
#        fig.canvas.mpl_connect('pick_event', on_pick)



#    def onpick(self, event):
#    #    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
#    #          ('double' if event.dblclick else 'single', event.button,
#    #           event.x, event.y, event.xdata, event.ydata))
#        thisline = event.artist
#        xdata = thisline.get_xdata()
#        ydata = thisline.get_ydata()
#        ind = event.ind
##        xdata = round(xdata, 6)
##        ydata = round(ydata, 6)
#        import pdb; pdb.set_trace();
#        points = tuple(zip(xdata[ind], ydata[ind]))
#        print('onpick points:', points)
#
##        points_1 = round(points[0], 6)
##        points_2 = round(points[1], 6)
##        print('onpick points:', tuple(points_1, points_2))


