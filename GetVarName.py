# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:29:55 2017

@author: yoshino
"""

def getVarsNames( _vars, symboltable ) :
    """
    This is wrapper of getVarName() for a list references.
    """
    return [ getVarName( var, symboltable ) for var in _vars ]

def getVarName( var, symboltable, error=None ) :
    """
    Return a var's name as a string.\nThis funciton require a symboltable(returned value of globals() or locals()) in the name space where you search the var's name.\nIf you set error='exception', this raise a ValueError when the searching failed.
    """
    for k,v in symboltable.iteritems() :
        if id(v) == id(var) :
            return k
    else :
        if error == "exception" :
            raise ValueError("Undefined function is mixed in subspace?")
        else:
            return error

if __name__ == "__main__":
    a = 4
    b = "ahoo"
    print (getVarsNames([a,b,"c"],locals()))
    
#%%


data1 = [12.0 , 13.5 , 12.5]
data2 = [10.0 , 9.0 , 7.5]
data3 = [9.0 , 2.0 , 14.0] 

for data_label, data in data_dic.items():
  print(data_label)
  
#%%
  
var_name = lambda val : [k for k, v in globals().items() if id(v) == id(val)]
a = 1
ssss = var_name(a)[0]

#%%

def chkprint(*args):
    flg = 1
    for obj in args:
        for k, v in globals().items():
            if id(v) == id(obj):
                target = k
                break
        if flg == 1:
#            out = target+' = '+str(obj)
            out = target

            flg = 0
        else:
#            out += ', '+target+' = '+str(obj)           
            out += ', '+target
    return out
    
    
    
#if __name__=="__main__":
#    adddd = 1
#    lst = [3, 1, 4, 1, 5]
#    chkprint(adddd)
#    chkprint(lst)
#    chkprint(adddd, lst)
    
    #%%
    
def Heart_split(high_or_low_data):
    global listname, listname_2
    for a in range(len(high_or_low_data)):
        if high_or_low_data[a] == 'nan':
            listname = chkprint(high_or_low_data) + '_split'
            listname.append(a)
            listname_2 = chkprint(high_or_low_data) + 'ted'
            listname_2 = np.split(high_or_low_data, listname)
            
listname = 'blank'
listname_2 = 'blank'

target = 'eee'
uuu = [1,1,1,1,1,3,3,2,2,4,'nan' ,12,12,2,3,1,'nan',1,2]            
Heart_split(uuu)

#%%

for i in range(10):
  for j in range(20):
    exec("list_" + str(i) + "_" + str(j) + "= [i, j]")
    
    
#%%

def func():
    print('func() is called')
    # ローカルスコープでの globals()
    print(globals())

global_val = 'this is global'

# グローバルスコープでの globals()
print(globals())

# 通常のグローバル関数、変数呼び出し
func()
print(global_val)

# 文字列からグローバル関数、変数呼び出し
globals()['func']()
print(globals()['global_val'])    
    
#%%


def func():
    def local_func():
        print('local_func() is called')

    print('func() is called')
    local_val = 'this is local'

    # ローカルスコープでの locals()
    print(locals())

    # 通常のローカル関数、変数呼び出し
    local_func()
    print(local_val)

    # 文字列からグローバル関数、変数呼び出し
    locals()['local_func']()
    print(locals()['local_val'])


# グローバルスコープでの locals()
print(locals())
func()   

#%%

# exec
''' write file '''
a = [1,2,3,4,5,6]

b = [2,3,4,5,6,7]
with open('test.txt', 'w') as fout:
    fout.write('num_list_a = ' + repr(a))
    fout.write('\n')
    fout.write('num_list_b = ' + repr(b))

''' load file '''
exec(open('test.txt').read())
print('a =', num_list_a, '\nb =', num_list_b)

# eval
''' write file '''
a = [1,2,3,4,5]
with open('test2.txt', 'w') as fout:
     fout.write(repr(a))
del a

''' load file'''
num_list_c = eval(open('test2.txt').read())
print('c =', num_list_c)


#%%
from copy import copy
x = [1, 2, 3]
y = copy(x)  # y = x[:]でも良い (むしろこっちのほうがシンプル)
y[0] = 999

#%%


import datetime
today = datetime.datetime.now()
str(today)

repr(today)


