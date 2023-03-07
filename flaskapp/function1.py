#!/venv/bin/ python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:08:56 2022

@author: jen
"""
import matplotlib.pyplot as plt
import numpy as np


def x_section(X1, Y1, X2, Y2):

    countx = str.__len__(X1)
    county = str.__len__(Y1)
    
    X1 = int(X1[0:countx])
    Y1 = int(Y1[0:county])
    X2 = int(X2[0:countx])
    Y2 = int(Y2[0:county])
        
    xlist = list(np.linspace(X1,X2))
    ylist = list(np.linspace(Y1,Y2))

    xlen = len(xlist)
    ylen = len(ylist)
    
    ylist = np.asarray(ylist, dtype=str)
    ylist = ylist.tolist()
    y_str = ", ".join(ylist)

    xlist = np.asarray(xlist, dtype=str)
    xlist = xlist.tolist()
    x_str = ", ".join(xlist)
        
    fx = open("xlist_out.txt", 'w')
    fx.write(x_str)
    fx.close()
    
    fy = open("ylist_out.txt", 'w')
    fy.write(y_str)
    fy.close()
    
fig = plt.figure()
#plt.show()
    
