# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 07:14:07 2014

@author: pdiehm
"""

nsteps1 = 50
nsteps2 = 53

for idx in range(0,nsteps1):
    r = nsteps2/float(nsteps1)
    idx2 = int(round(idx*r))
    
    print "{} = {}".format(idx,idx2)