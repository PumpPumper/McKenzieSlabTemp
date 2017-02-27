#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:21:52 2017

@author: JoeRippke

This module exists to control how the slab model is calculated and how the
output is stored and/or displayed.
"""
import numpy as np
import slabtemp as st
import matplotlib.pyplot as plt

def slabmodel(xmax,l,rho,Cp,vx,kappa,dip):
    output = np.zeros((xmax,xmax))
    for distance in range(xmax):
        for depth in range(xmax):
            slope = -1*np.tan(dip)
            SlabDep = distance*slope
            innerterm = (distance+slope*depth)/((slope**2)+1)
            term1 = (innerterm-distance)**2
            term2 = (slope*innerterm-depth)**2
            ztest = np.sqrt([term1+term2])
            if depth >= SlabDep and ztest <= l:
                output[distance,depth] = st.slabtemp(distance,depth,xmax,rho,Cp,vx,l,kappa,dip,ztest)
            else:
                output[distance,depth] = 1
    plt.close('all')
    plt.figure(1)
    CS = plt.contour(output)
    plt.ylim((xmax,0))
    plt.clabel(CS, inline=1, fontsize=10)
    plt.title('Slab Thermal Structure')
    plt.ylabel('Depth (km)')
    plt.xlabel('Distance(km)')
    plt.savefig('Slabfig')
