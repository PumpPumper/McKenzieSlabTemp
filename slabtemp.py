#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:33:36 2017

@author: JoeRippke

This module exists to contain functions needed to calculate slab temperature.
In the future I may add functions to calculate other slab attributes.
"""
import numpy as np

def slabtemp(x,z,xm,rho,Cp,vx,l,kappa,dip,ztest):
    v1 = vx / 31536000 #           convert cm/yr to cm/sec
    l1 = l * 100000 #              convert km to cm
    xp = (x/np.cos(dip))/xm #                    nondimensionalize x
    zp = ztest/l #                     nondimensionalize z
    R = (rho*Cp*v1*l1)/(2*kappa) #  calculate Reynolds number
    Tprime = 1-(2/np.pi)*np.exp(-1*((np.pi**2)*xp)/(2*R))*np.sin(np.pi*zp)
    return Tprime