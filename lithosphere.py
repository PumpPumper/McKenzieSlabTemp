#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:32:16 2017

@author: JoeRippke
"""
import numpy as np
import matplotlib.pyplot as plt
import slabtemp as st

plt.close('all')


def slabmodel(xmax,l,rho,Cp,vx,kappa,dip):
    output = np.zeros((int(xmax/4),xmax))
    diprads = (dip)*np.pi/180 # convert slab dip degrees to radians
    slope = np.tan(diprads) # calculate slope
    for x in range(xmax):
        for z in range(int(xmax/4)):
            zl1 = (x-100)*slope-100*slope+l # line equation for the bottom of the slab
            #zl2 = slope*((x-100)-100-l*np.sin(diprads))+l*(1+np.cos(diprads)) # line equation for the top of the slab
            start = [-100,-200*slope-100*slope+l,0]
            end = [1500,1400*slope-100*slope+l,0]
            dist = st.pnt2line((x,z,0),start,end)
            if z >= zl1 and dist[0] <= l:
                output[z,x] = 0
            elif z <= l and z >= zl1:
                output[z,x] = 0
            elif z <= l:
                output[z,x] = 2
            else:
                output[z,x] = 1
#            if z <= l and z >= zl2:
#                output[z,x] = 0
#            elif z >= zl1 and z <= zl2:
#                output[z,x] = 0
#            elif z <= l:
#                output[z,x] = 2
#            else:
#                output[z,x] = 1
    plt.figure(1)
    plt.contourf(output)
    plt.ylim((int(xmax/4),1))
    plt.axes().set_aspect('equal')
    #zl2int = slope*(-200-l*np.sin(diprads))+l*(1+np.cos(diprads))
    for x1 in range(xmax):
        for z1 in range(int(xmax/4)):
            #start = [-100,-200*slope-100*slope-l*slope*np.sin(diprads)+l+l*np.cos(diprads),0]
            #end = [1500,1400*slope-100*slope-l*slope*np.sin(diprads)+l+l*np.cos(diprads),0]
            start = [-100,-200*slope-100*slope+l,0]
            end = [1500,1400*slope-100*slope+l,0]
            #iterm = ((x1+slope*z1-slope*zl2int)/((slope**2)+1))
            #dist = np.sqrt((iterm**2)+((slope*iterm+zl2int-z1)**2))
            #dist = np.abs(slope*x1-1*z1+l*(1+np.cos(diprads))-slope*(100+l*np.sin(diprads)))
            dist = st.pnt2line((x1,z1,0),start,end)
            xint = 100 + ((100*slope-l)/slope)
            if output[z1,x1] == 0 and x1 > xint:
                output[z1,x1] = dist[0]/l
            elif output[z1,x1] == 0 and x1 <= xint:
                output[z1,x1] = z1/l
            elif output[z1,x1] == 2:
                output[z1,x1] = z1/l
            if output[z1,x1] > 1:
                output[z1,x1] = 1
    plt.figure(2)
    plt.contourf(output,20)
    plt.ylim((int(xmax/4),1))
    plt.axes().set_aspect('equal')
    plt.colorbar()
    plt.title('Slab Thermal Structure')
    plt.ylabel('Depth (km)')
    plt.xlabel('Distance(km)')
