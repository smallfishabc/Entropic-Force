# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:22:07 2019

@author: ShaharGroup-fyu
"""

import matplotlib.pyplot as plt
import mdtraj as md
import os, sys
import statistics as st
import numpy as np
import pandas as pd
def compute():
    t = md.load('__traj.xtc',top='__START.pdb')
    topology=t.topology
    r=topology.select_atom_indices(selection='alpha')
    j=0
    k=0
    while j<5500:
        for i in r:
            value=1
            standard=t.xyz[j,r[0],:]
            standardvector=t.xyz[j,r[1],:]
            a=t.xyz[j,r[-1],:]
            valuea=(standardvector[0]-standard[0])*(standardvector[0]-standard[0])+(standardvector[1]-standard[1])*(standardvector[1]-standard[1])+(standardvector[2]-standard[2])*(standardvector[2]-standard[2])
            valueb=(a[0]-standard[0])*(a[0]-standard[0])+(a[1]-standard[1])*(a[1]-standard[1])+(a[2]-standard[2])*(a[2]-standard[2])
            valuedot=(standardvector[0]-standard[0])*(a[0]-standard[0])+(standardvector[1]-standard[1])*(a[1]-standard[1])+(standardvector[2]-standard[2])*(a[2]-standard[2])
            value=np.sqrt(valueb-valuedot*valuedot/valuea)
        j+=1   
    return(k)
arrange=0
col=0
pwd=os.getcwd()
print(np.cos(np.pi/6))
k = ['S_-3.0','S_-2.5','S_-2.0','S_-1.5','S_-1.0','S_-0.5','S_0.0','S_0.5','S_1.0','S_1.5','S_2.0','S_2.5','S_3.0']
q =[-3.0,-2.5,-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0,2.5,3.0]
l = ['BB']
color = ['#800080']
tit=['Backbone']
for h in l:
    forbiden=[]
    for p in k:
        string = str(pwd)+'/'+h+'/'+p
        os.chdir(string)
        temp=compute()
    os.chdir(pwd)
    dataframe = pd.DataFrame({'MTFE':q,'forbidden':forbiden})
    pcsv=h+'cforbid1.csv'
    dataframe.to_csv(pcsv,index=False,sep=',')
        
