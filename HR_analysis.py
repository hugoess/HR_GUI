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



filename = "20170904"

f = open(filename + '.txt')
line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)
