# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:48:10 2019

@author: ShaharGroup-fyu
"""

import matplotlib.pyplot as plt
import mdtraj as md
import os, sys
import statistics as st
import numpy as np
import pandas as pd
pwd=os.getcwd()
print (pwd)
arrange=0
k = ['S_0.0']
q =[0.0]
l = ['BB']
for h in l:
    mean=[]
    sd=[]
    for p in k:
        string = str(pwd)+'\\'+h+'\\'+p
        os.chdir(string)
        test = os.getcwd()
        print (test)
        t = md.load('__traj.xtc',top='__START.pdb')
        u=t.top.select('protein')
        r=t.atom_slice(u)
        j = r.n_frames
        d = md.rmsd(r,r,0)
        print(d[1:1000])
        m = np.mean(d)
        n = np.std(d)
        print(m)
        print(n)
    os.chdir(pwd)    
    dataframe = pd.DataFrame({'RMSD':sigm})
    pcsv=h+'7.csv'
    dataframe.to_csv(pcsv,index=False,sep=',')
    plt.plot(hiii,sigm)
    plt.ylabel('<rmsd(t)*rmsd(t+delta t)>')
    plt.xlabel('blocksize')
    plt.title(h)
    plt.grid(True)
pfig="RMSD"+'.png'
plt.savefig(pfig)
