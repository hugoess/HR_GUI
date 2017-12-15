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

# =============================================================================
# いろいろインポートImport
# =============================================================================


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





#--------------------------------------------------------------
#%%
filename = "20171020_64(vs 66)"

f = open(filename + '.lvm')
line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)

v_time          = []
v_time_1        = []
v_volt_hb       = []
v_volt_hb_1     = []
v_volt_on_off   = []
v_volt_on_off_1 = []

# =============================================================================
# ファイル読み込みと正規表現でデータを取り出す
# =============================================================================

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
# =============================================================================
# #HighとLowデータの変わり目の番号を算出してここでLow時とHigh時の心拍電圧データに分けた
# =============================================================================

v_time = np.array(v_time)

v_volt_hb = np.array(v_volt_hb)
v_volt_on_off = np.array(v_volt_on_off)

v_data_1=[]   #この配列の0番、2番、4番などの偶数インデックスが対応する値の後がOn_OFFのHighの時、2番が２２２で、3番が３３３の場合、222から３３２までが
v_data_2=[]

for n in range(len(v_volt_on_off)):

    if ((v_volt_on_off[n-1] <= 7.9) and (v_volt_on_off[n] >= 8)) or ((v_volt_on_off[n-1] >= 8) and (v_volt_on_off[n] <= 7.9)):
        v_data_1.append(n) 

volt_hb_splitted = np.split(v_volt_hb, v_data_1)
volt_time_splitted = np.split(v_time, v_data_1)


volt_hb_low =[]
volt_hb_high=[]
v_time_low=[]
v_time_high=[]


HR_computation_low_xdata = []
HR_computation_low_ydata = []

HR_computation_high_xdata = []
HR_computation_high_ydata = []

listname = 'blank'
listname_2 = 'blank'

def is_guusuu(xx:list, yy:list, zz:list):

    for x in range(len(zz)):
        if x % 2 == 0:            
            xx.extend(zz[x])
            if x+1 < len(zz):
                zerosx = np.zeros_like(zz[x+1])
                zerosx = zerosx + 5.5
                xx.extend(zerosx)
        if x % 2 == 1:
            zerosy = np.zeros_like(zz[x-1])
            zerosy = zerosy + 5.5
            yy.extend(zerosy)
            yy.extend(zz[x])
            if x+1 == len(zz)-1:
                zerosy = np.zeros_like(zz[x+1])
                zerosy = zerosy + 5.5
                yy.extend(zerosy)


is_guusuu(volt_hb_low, volt_hb_high, volt_hb_splitted)

volt_hb_low = np.array(volt_hb_low)
volt_hb_high = np.array(volt_hb_high)



#%%
# =============================================================================
# 変数の初期化
#　Figureのサイズの指定
# =============================================================================

t2 = v_time[1:200]
v2 = v_volt_hb[1:200]
v_current = np.array([])
v_time_current = np.array([])
v_output_name = 'Hi'
v_output_high = 'High'
v_output_low = 'Low'

i = 1
fig = Figure(figsize=(12,6))
ax = fig.add_subplot(111)




#%%

def on_pick(event):
    '''Pick eventとText fileへの書き込み'''
    global v_output_name, v_output_high, v_output_low

    line = event.artist
    xdata, ydata = line.get_data()
    ind = event.ind

    print([xdata[ind], ydata[ind]])

    
    
    f = open(filename + '__' + v_output_name +'.txt', 'a')

    f.write(str(xdata[ind][0]) + '\t' + str(ydata[ind][0]) + '\n')
    f.close()
    
    radSel = qqq.get()
    if radSel == 1:
        HR_computation_low_xdata.append(xdata[ind][0])
        HR_computation_low_ydata.append(ydata[ind][0])
        print('Low_append_data')
    elif radSel == 2:
        HR_computation_high_xdata.append(xdata[ind][0])
        HR_computation_high_ydata.append(ydata[ind][0])
        print('High_append_data')
    



def add_nan(event):
    '''Right clickでnanを書き込む機能、心拍計算時のノイズ対策のために作った'''
    global v_output_name, v_output_high, v_output_low


    f = open(filename + '__' + v_output_name +'.txt', 'a')
    f.write('nan'+ '\t' +'nan'+'\n')
    f.close()
    
    radSel = qqq.get()
    if radSel == 1:
        HR_computation_low_xdata.append('nan')
        HR_computation_low_ydata.append('nan')
        print('Low_append_nan')
    elif radSel == 2:
        HR_computation_high_xdata.append('nan')
        HR_computation_high_ydata.append('nan')
        print('High_append_nan')
    print('nan')


def next_page():
    '''ボタンクリックで次のページ'''
    global ax, fig, canvas, t2, v2, window, i_200, i_400, i,volt_hb_high, volt_hb_low, v_current
    global v_time_current, v_time_low, v_output_name, v_output_high, v_output_low
    i = i+1
    i_200 = (i-1)*200+1
    i_400 = i*200
    t2 = v_time[i_200:i_400]
    v2 = v_current[i_200:i_400]
    print('%d ~ %d' % (i_200,i_400))
    ax.clear()
    plot()
    
def previous_page():
    
    '''ボタンクリックで前のページ'''
    global v_time_current, v_time_low, v_output_name, v_output_high, v_output_low
    global ax, fig, canvas, t2, v2, window, i_200, i_400, i,volt_hb_high, volt_hb_low, v_current
    i = i -1
    i_200 = (i-1)*200+1
    i_400 = i*200
    t2 = v_time[i_200:i_400]
    v2 = v_current[i_200:i_400]
    print('%d ~ %d' % (i_200,i_400))
    ax.clear()
    plot()
  
def low_or_high():

    global ax, fig, canvas, t2, v2, window, i_200, i_400, i,volt_hb_high, volt_hb_low, v_current
    global v_time_current, v_time_low, v_output_name, v_output_high, v_output_low
    radSel = qqq.get()
    if radSel == 1:
        window.configure(background = COLOR1)
        v_current = volt_hb_low
        v_time_current = v_time_low
        v_output_name = v_output_low
#        label_1.configure(text = 'Heartrate Low')
        print('Low')
        
    elif radSel == 2:
        window.configure(background = COLOR2)
        v_current = volt_hb_high
        v_time_current = v_time_high
        v_output_name = v_output_high
#        label_1.configure(text = 'Heartrate High')
        print('High')

    print(radSel)

def plot():  
    '''FigのSubplotであるaxを指定されているt2,v2でPlotする。
    タイトルやラベルなどの設定、
    FigをFigureCanvasTkAggというTypeにしてCanvasと名付けているので、Canvasで描画する指令、
    及びPick eventのActivation
    '''
    global ax, fig, canvas, t2, v2, window, i_200, i_400, i,volt_hb_high, volt_hb_low, v_current
    ax.plot(t2, v2, 'o-', picker=1)
    pretitle =('%d ~ %d' % (i_200,i_400))
    ax.set_title (str(pretitle), fontsize=16)
    ax.set_ylabel("Voltage", fontsize=14)
    ax.set_xlabel("Time(s)", fontsize=14)
    canvas.draw()
    fig.canvas.mpl_connect('pick_event', on_pick)


window= Tk()

button = Button(window, text="check", command=plot)
button.grid(row = 0)
button_2 = Button(window, text='Previous Page', command = previous_page)
button_2.grid(row = 1, column = 0, sticky = W)
button_1 = Button(window, text='Next Page', command = next_page)
button_1.grid(row = 1, column = 0, sticky = E)

qqq = IntVar()
COLOR1 = 'Blue'
COLOR2 = 'Gold'
COLOR3 = 'Red'





radio_1 = Radiobutton(window, text = 'Low', variable = qqq, value = 1, command=low_or_high)
radio_1.grid(row=0, column= 0, sticky = W)

radio_2 = Radiobutton(window, text = 'High', variable = qqq, value = 2, command=low_or_high)
radio_2.grid(row=0, column= 0, sticky = E)

quitbtn = Button(window, text = 'Quit', command = window.destroy)
quitbtn.grid(row = 2)

canvas = FigureCanvasTkAgg(fig, master=window)      #FigをFigureCanvasTkAggというTypeにしてできたObjectをCanvasと名付けている。また、Windowが親であるというOptionも
canvas.get_tk_widget().bind('<Button-3>', add_nan)
canvas.get_tk_widget().grid(row = 3, columnspan = 4)  #canvas.get_tk_widget()でcanvas = FigureCanvasTkAggをｔｋのwidgetにする。でないと、Bindメソッドが使えない

window.title('HR Counter')
window.geometry('1200x700')      #横ｘ縦
#start= mclass (window)



label_low = Label(window, text = 'Heartrate    low')
label_low.grid(column = 3, row = 0, sticky = W)
label_high = Label(window, text = 'high')
label_high.grid(column = 3, row = 0, sticky = E)

#def chkprint(*args):
#    flg = 1
#    for obj in args:
#        for k, v in globals().items():
#            if id(v) == id(obj):
#                target = k
#                break
#        if flg == 1:
##            out = target+' = '+str(obj)
#            out = target
#            flg = 0
#        else:
##            out += ', '+target+' = '+str(obj)           
#            out += ', '+target
#    return out
#    print(out)

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

#            
#            
#            
#              .append('nan')
#        HR_computation_low_ydata.append('nan')
#  
#        
#        for n in range(len(v_volt_on_off)):
#
#    if ((v_volt_on_off[n-1] <= 5) and (v_volt_on_off[n] >= 8)) or ((v_volt_on_off[n-1] >= 8) and (v_volt_on_off[n] <= 5)):
#        v_data_1.append(n) 
#
#volt_hb_splitted = np.split(v_volt_hb, v_data_1)
#volt_time_splitted = np.split(v_time, v_data_1)
#    
    
    
#    pass
#    label_2 = Label(window, text = 'A Label')
#    label_2.grid(column = 3, row = 1)

window.mainloop()


