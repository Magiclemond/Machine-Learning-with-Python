u# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:19:05 2016

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math 

datas = pd.read_excel("data1.xls")
datas = np.array(datas)

def log(theta,x):
    
    s = [1]
    s.append(x[0])
    s.append(x[1])
    sz = np.dot(theta,s)
    
    return 1/(1+math.exp(-sz))    
    
def line(data):    
    
    x_data0=[];y_data0=[]
    x_data1=[];y_data1=[]
    label=[]
    m = np.size(datas,0)
    
    for i in range(m):
        if datas[i,2]==0:
            x_data0.append(datas[i,0])
            y_data0.append(datas[i,1])
            label.append(datas[i,2])
        else:
            x_data1.append(datas[i,0])
            y_data1.append(datas[i,1])
            label.append(datas[i,2])
    
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax.scatter(x_data0,y_data0,s=30,c='red')
    ax.scatter(x_data1,y_data1,s=30,c='blue')
    
  
    train_time = 500
    theta = []
    theta.append(random.random())#t0
    theta.append(random.random())#t1
    theta.append(random.random())#t2
    theta = np.array(theta)
    a = 0.06
    m = np.size(datas,0)
    J_a = []
    
    for t in range(train_time):
        
        J = 0
        for i in range(m):
            
            J = J + (log(theta,datas[i,0:2])-label[i])**2/(2*m)           
            x = a*(log(theta,datas[i,0:2])-label[i])/m
            y = a*(log(theta,datas[i,0:2])-label[i])*datas[i,0]/m
            z = a*(log(theta,datas[i,0:2])-label[i])*datas[i,1]/m
            theta[0] = theta[0] - x
            theta[1] = theta[1] - y
            theta[2] = theta[2] - z

        J_a.append(J)
        #print(J)
        
    x_data=[];y_data=[]    
    for k in np.linspace(35,40,50):
        x_data.append(k)
        y_data.append(-theta[0]/theta[2]-theta[1]*k/theta[2])
    plt.plot(x_data,y_data)
    fig.add_subplot(212)
    plt.plot(J_a)
    print(theta)
    

line(datas)