# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 11:30:14 2018
version 1.01 Make a title and have a figure clear line
version 1.02 Changed the file name of figure
@author: small
"""
import mdtraj as md
import os, sys
import statistics as st
import numpy as np
import pandas as pd
pwd=os.getcwd()
print (pwd)
k = ['S_-3','S_-2','S_-1','S_0','S_1','S_2','S_3']
q =[-3,-2,-1,0,1,2,3]
l = ['BB']
for h in l:
    mean=[]
    sd=[]
    for p in k:
        string = str(pwd)+'/'+h+'/'+p
        os.chdir(string)
        test = os.getcwd()
        print (test)
        t = md.load('__traj.xtc',top='__START.pdb')
        u=t.top.select('protein')
        r=t.atom_slice(u)
        j = r.n_frames
        d = md.compute_rg(r)        
        m = st.mean(d)
        n = np.std(d)
        sd.append(n)
        mean.append(m) 
        f = open('rgdata','w')
        i = 0
        while i<j:
            x=str(d[i])
            f.write(x)
            f.write('\n')
            i+=1
        f.close()
    os.chdir(pwd)    
    dataframe = pd.DataFrame({'MTFE':q,'Rs':mean,'Sd':sd})
    pcsv=h+'.csv'
    dataframe.to_csv(pcsv,index=False,sep=',')


    
