# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 19:54:01 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:57:42 2016

@author: sherlock
"""
from numpy import *
from math import *
import matplotlib.pyplot as plt


def fun1(x):
    y = -20*exp(-0.2*sqrt((x[0]**2+x[1]**2)/2))-exp((cos(2*pi*x[0])+cos(2*pi*x[1]))/2)+20+2.71289
    return y

    
c1 = 1.49445
c2 = 1.49445
w = 0.8

maxg = 200
sizepop = 20

Vmax=1
Vmin=-1
popmax = 5
popmin = -5

pop = zeros([sizepop,2])
V = zeros([sizepop,2])
fitness = []
yy = []


for i in range(sizepop):
    pop[i,:] = random.rand(1,2)
    V[i,:] = random.rand(1,2)
    fitness.append(fun1(pop[i,:]))
    
bestfitness = min(fitness)
bestindex = fitness.index(bestfitness)
gbest = pop[bestindex,:]
ibest = pop
fitnessibest = fitness
fitnessgbest = bestfitness

for i in range(maxg):
    for j in range(sizepop):
        w = w - 0.3/199 * i
        V[j,:] = w * V[j,:] + c1*random.rand()*(ibest[j,:] - pop[j,:]) + c2*random.rand()*(gbest - pop[j,:])
        V[j,argwhere(V[j,:] > Vmax)] = Vmax
        V[j,argwhere(V[j,:] < Vmin)] = Vmin
        
        
        pop[j,:] = pop[j,:] + 0.5*V[j,:]
        pop[j,argwhere(pop[j,:] > popmax)] = popmax
        pop[j,argwhere(pop[j,:] < popmin)] = popmin
        

        if random.rand() > 0.8:
            k = ceil(2 * random.rand() - 1)
            pop[j,k] = random.rand()

        fitness[j] = fun1(pop[j,:])
        
        if fitness[j] < fitnessibest[j]:
            ibest[j,:] = pop[j,:]
            fitnessibest[j] = fitness[j]
            
            
        if fitness[j] < fitnessgbest:
            gbest = pop[j,:]
            fitnessgbest = fitness[j]
            
    yy.append(fitnessgbest)
    
print(gbest)


    
plt.plot(yy)
    
    