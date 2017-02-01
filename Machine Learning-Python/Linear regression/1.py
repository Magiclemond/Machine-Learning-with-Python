# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:03:12 2016

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

datas = pd.read_excel("datas.xls")
datas = np.array(datas)

def line(datas):
    
    fig = plt.figure()
    
    train_time = 30
    w = random.random()
    b = random.random()
    a = 0.3
    m = np.size(datas,0)
    J_a = []
    r_w = 0
    
    for t in range(train_time):
        
        J = 0
        for i in range(m):
            
            J = J + (w*datas[i,0]+b-datas[i,1])**2/(2*m)           
            r_w = w
            w = w - a*(w*datas[i,0]+b-datas[i,1])*datas[i,0]/m
            b = b - a*(r_w*datas[i,0]+b-datas[i,1])/m
        print(w,b)
        J_a.append(J)
        
    x_data=[];y_data=[]    
    for l in range(m):
        x_data.append(datas[l,0])
        y_data.append(datas[l,1])
        
    ax = fig.add_subplot(211)
    ax.scatter(x_data,y_data,s=30,c='red')
        
    x_1=[];y_1=[]    
    for k in range(50):
        x_1.append(k*0.1)
        y_1.append(w*k*0.1+b)
    plt.plot(x_1,y_1)
    fig.add_subplot(212)
    plt.plot(J_a)
    
line(datas)
        

        