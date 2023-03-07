#!/venv/bin python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:34:49 2022

@author: jen
"""
import numpy as np
from scipy.spatial import cKDTree
from scipy import interpolate
import matplotlib.pyplot as plt
from function1 import x_section

def interp_xsection(x,y,z, xlist, ylist, ax = None):
    if ax is None:
        ax = plt.gca()
        
    xs = x.tolist()
    ys = y.tolist()
    zs = z.tolist()
    XY = list(zip(xs,ys))
    XY = np.reshape(XY,(len(xs),2))
    
    xy = list(zip(xlist,ylist))
    xy = np.reshape(xy,(-1,2))
    
    tree = cKDTree(XY)
    distances, indices = tree.query(xy, k=1)
    z_vals = z[indices]
    
    yarr = np.asarray(ylist, dtype=float)
    xarr = np.asarray(xlist, dtype=float)
    #zarr = np.asarray(z_vals[0::2])     
    zarr = np.array(z_vals).reshape(yarr.size)
    
    x_space = np.linspace(min(xarr), max(xarr))
    z_space = np.interp(x_space, xarr, zarr)
    
    x_space = np.asarray(x_space, dtype = int)
    x_space = np.array2string(x_space, 8)
    
    xspace = open("xspace_out.txt", 'w')
    xspace.write(x_space)
    xspace.close()
   
    z_space = np.asarray(z_space, dtype = int)
    z_space = np.array2string(z_space, 3, sign='-')
    
    zspace = open("zspace_out.txt", 'w')
    zspace.write(z_space)
    zspace.close()
    
    return ax
