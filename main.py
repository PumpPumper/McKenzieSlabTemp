#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 14:50:55 2017

@author: JoeRippke

This module exists to run the McKenzie sinking slab thermal structure model
"""
import slabcalc as sc

# Set Values

rho = 3 # g/cm^3               set value of rock density
Cp = 0.35 # cal/(g °C)         set value of heat capacity
vx = 10 # cm/yr                set value of slab velocity
l = 50 # km                    set value of slab thickness
kappa = 0.01 # cal/(cm °C s)   set value of thermal conductivity
xmax = 1000 # km               set maximum slab length (arbitrary)

sc.slabmodel(xmax,l,rho,Cp,vx,kappa)
