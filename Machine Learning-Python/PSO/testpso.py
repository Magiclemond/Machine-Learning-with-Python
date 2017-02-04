# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 21:36:40 2017

@author: Administrator
"""
import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
'''
Global Variable setting
'''
c1,c2 = 1.4,1.4
iteration = 200
Vmax,Vmin = 1,-1
Xmax,Xmin = 3,-1
Ymax,Ymin = 2,-2
swarmsize = 20
#Global best point: [-0.54719 , -1.54719]
def fun(x,y):
    
    return np.sin(x+y)+(x-y)**2-1.5*x+2.5*y+1+1.9133

def fig(swarm,fit):
    x = np.arange(-1,3,0.01)
    y = np.arange(-2,2,0.01)
    fig = plt.figure()
    ax = Axes3D(fig)
    x,y = np.meshgrid(x,y)
    
    x1 = [];y1 = []
    x1 = swarm[:,0];y1 = swarm[:,1]
    #ax=plt.subplot(111,projection='3d') 
    #ax.plot_surface(x,y,z,cmap='winter')
    ax.scatter(x1,y1,fit,s=40,c='y') 
    plt.show()
    

def pso(swarm,fit,V,loc_f):
    g_b = swarm[loc_f,:]
    i_b = swarm
    fit_ib = fit
    fitbest = []
    fitbest.append(fun(g_b[0],g_b[1]))
    w = 0.6
    
    for i in range(iteration):
        for j in range(swarmsize):
            w = w - 0.2/200 * i
            V[j,:]=w*V[j,:]+c1*random.random()*(i_b[j,:]-swarm[j,:])+c2*random.random()*(g_b-swarm[j,:])
            
            V[j,np.argwhere(V[j,:]>Vmax)] = Vmax
            V[j,np.argwhere(V[j,:]<Vmin)] = Vmin
            
            swarm[j,:] = swarm[j,:] + 0.5 * V[j,:]
            
            if swarm[j,0] > Xmax:
                swarm[j,0] = Xmax
            elif swarm[j,0] < Xmin:
                swarm[j,0] = Xmin
                     
            if swarm[j,1] > Ymax:
                swarm[j,1] = Ymax
            elif swarm[j,1] < Ymin:
                swarm[j,1] = Ymin
                     
            fit[j] = fun(swarm[j,0],swarm[j,1])
            
            if fit[j] < fit_ib[j]:
                i_b[j,:] = swarm[j,:]
                
        g = swarm[fit.index(min(fit)),:]
            
        if fun(g[0],g[1]) < fitbest[i]:  
            fitbest.append(fun(g[0],g[1]))  
            g_b = g
        else:
            fitbest.append(fitbest[i])
        if i < 25 :
            print("figure")                  
            fig(swarm,fit)            
            
    plt.plot(fitbest)
    print(g)
    print(fun(g[0],g[1]))
    
def initi():
    swarm=np.zeros([swarmsize,2])
    V = np.zeros([swarmsize,2])
    fit = []
    for i in range(swarmsize):
        swarm[i,0] = 4*random.random()-1
        swarm[i,1] = 4*random.random()-2
        a,b = swarm[i,:]
        fit.append(fun(a,b))
        V[i,0] = random.random()
        V[i,1] = random.random()
    min_f = min(fit)
    loc_f = fit.index(min_f)
    return swarm,fit,V,loc_f


swarm,fit,V,loc_f = initi()
pso(swarm,fit,V,loc_f)