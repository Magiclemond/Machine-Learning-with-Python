# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:57:41 2017

@author: Administrator
"""

import scipy.io as sio  

from keras.models import Model
from keras.layers import Dense,Input

from sklearn import preprocessing

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1337)

matfn=u'C:/Users/Administrator/Desktop/Machine Learning-Python/SRBCT/srbct_data_label.mat'  
data = sio.loadmat(matfn)  

srbct_data = data['all_data']
srbct_label = data['all_label']

#data pre-processing
srbct_data = (srbct_data-srbct_data.min())/(srbct_data.max()-srbct_data.min())

#The traning rate for SRBCT is 80%
training_rate = 0.8
training_num = int(srbct_data.shape[0]*training_rate)

x_train = srbct_data[0:training_num,:]
x_label = srbct_label[0:training_num,:]
onehot = preprocessing.OneHotEncoder()  
onehot.fit(x_label) 
x_l = onehot.transform(x_label).toarray()


y_test = srbct_data[training_num:,:]
y_label = srbct_label[training_num:,:]

encoding_dim = 2
#Input placeholder
input_data = Input(shape=(x_train.shape[1],))
#Encoder layers
encoded = Dense(1200,activation='relu')(input_data)
encoded = Dense(512,activation='relu')(encoded)
encoded = Dense(32,activation='relu')(encoded)
encoded_output = Dense(2)(encoded)
#Decoder layers
decoded = Dense(32,activation='relu')(encoded_output)
decoded = Dense(512,activation='relu')(decoded)
decoded = Dense(1200,activation='relu')(decoded)
decoded_output = Dense(x_train.shape[1],activation='sigmoid')(decoded)

#Training encoder
encoder = Model(input = input_data,output = encoded_output)
'''
encoder.compile(optimizer='adam',loss='mse')
encoder.fit(x_train,x_l,nb_epoch=20,batch_size=32,shuffle=True)
'''
#Training autoencoder
autoencoder = Model(input = input_data,output = decoded_output)
autoencoder.compile(optimizer='adam',loss='mse')
autoencoder.fit(x_train,x_train,nb_epoch=20,batch_size=32,shuffle=True)

#Plotting
encoded_imgs = encoder.predict(y_test)
plt.figure()
plt.scatter(encoded_imgs[:,0],encoded_imgs[:,1])
plt.show()