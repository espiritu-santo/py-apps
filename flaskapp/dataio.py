#!/venv/bin python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:25:51 2023

@author: jen
"""
import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use ("QtAgg")
from function1 import x_section
from function2 import interp_xsection

f = []

if f == []:
   
    upload_folder = '~/flaskapp/uploads/'
    fname = glob.glob1('./uploads/', '*')
    # files = os.walk(top=upload_folder)
    # for file in files:
    #      names = file[2]
    #      for name in names:
    #          name.split(', ')
    # fpath = upload_folder + name
    fpath = upload_folder + fname[0]

f = pd.read_csv(fpath)
lines = np.asarray(f)
a = np.hsplit(lines,3)

x = np.array(a[0])
y = np.array(a[1])
z = np.array(a[2])

if (z[0]>0):
    z = z * -1
    
def scatter(x,y,z,ax=None):
    if ax is None:
        p = plt.scatter(x,y,c=z)
        ax = p.axes
        fig = p.figure
        fig.show()
        plt.ion
        
        return ax

scatter(x,y,z)

get_dir = os.path.join('')
with open('./static/coords.txt') as b:
    results = b.read()

result1 = results.split('\n')
coords1 = result1[0]
coords1 = coords1.split(',')
X1 = coords1[0]
Y1 = coords1[1]
Y1 = Y1.strip(' ')
coords2 = result1[1]
coords2 = coords2.rsplit(', ')
X2 = coords2[0]
Y2 = coords2[1]

x_section(X1, Y1, X2, Y2)

fx = []
fx = open("xlist_out.txt", 'r')
data = fx.read()
fx.close()
xlist = data.split(", ")

fy = []
fy = open("ylist_out.txt", 'r')
data = fy.read()
fy.close()
ylist = data.split(", ")

interp_xsection(x, y, z, xlist, ylist)

xspace = open("xspace_out.txt", 'r')
data = xspace.read()
xspace.close()
x_space = data.replace('\n', ', ')
x_space = x_space.strip('[]')

zspace = open("zspace_out.txt", 'r')
data = zspace.read()
zspace.close()
z_space = data.replace('\n', ', ')
z_space = z_space.strip('[]')

p2 = plt.scatter(x,y,c=z)
ax = p2.axes
fig = p2.figure
fig.show()

plt.scatter(np.asarray(xlist, dtype=float),np.asarray(ylist, dtype=float),c='red')

axin = ax.inset_axes([0.8, 0.1, 0.2, 0.2])

x_space = [int(x) for x in x_space.split(",")]
z_space = [int(x) for x in z_space.split(",")]
axin.plot(x_space, z_space)


