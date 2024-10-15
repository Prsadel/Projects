#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd

def updu(x,y,s2,c2):
    lenu=len(x)
    for i in range(len(s2)):
        tempu=0
        cu=0
        tempu2=0
        for j in range(lenu):
            tempu1=0
            for l in range(len(s2)):
                tempu1=tempu1+s2[l]*x[j][l]
            tempu2=((y[j]-tempu1-c2))*(-2/lenu)
            cu=cu+tempu2
            tempu=tempu+(tempu2*x[j][i])
        s2[i]=s2[i]-(0.1*tempu)
        c2=c2-(0.1*cu)
    print(s2,c2)
    return s2,c2
                 
trainu=np.genfromtxt("C:\\Users\\hp\\Downloads\\0000000000002417_training_boston_x_y_train.csv",delimiter=",")
x_trainu=trainu[:,0:13]
y_trainu=trainu[:,13]
# print(x_trainu[0:1,12],y_trainu[0:1])
# len(x_trainu)
s1=[1,0,1,0,1,0,1,0,1,0,1,0,1]
c1=0
lt=0.001
for i in range(1000):
    s1,c1=updu(x_trainu,y_trainu,s1,c1)
# print(x_trainu.shape,len(s1))
# now_pred=[]
# testu=[]
# for i in range(len(x_trainu)):
#     tempu1=0
#     testu.append(y_trainu[i])
#     for j in range(len(s1)):
#         tempu1=tempu1+(s1[j]*x_trainu[i][j])
#     tempu1=tempu1+c1
#     now_pred.append(tempu1)
# print(len(now_pred),len(testu))
# import matplotlib.pyplot as plt
# tp=np.arange(-10,15)
# plt.scatter(now_pred,testu)
# plt.plot(tp,tp,"b--")
# plt.show()

# testu=np.genfromtxt("C:\\Users\\hp\\Downloads\\0000000000002417_test_boston_x_test.csv",delimiter=",")
# pred=[]
# for i in range(len(testu)):
#     tempu1=0
#     for j in range(len(s1)):
#         tempu1=tempu1+(s1[j]*testu[i][j])
#     tempu1=tempu1+c1
#     pred.append(tempu1)
# pred1=np.array(pred)
# np.savetxt("foo1.csv", pred1, delimiter=",")


# print(pred1.shape)
# print(pred1)


# In[12]:


testu=np.genfromtxt("C:\\Users\\hp\\Downloads\\0000000000002417_test_boston_x_test.csv",delimiter=",")
pred=[]
for i in range(len(testu)):
    tempu1=0
    for j in range(len(s1)):
        tempu1=tempu1+(s1[j]*testu[i][j])
    tempu1=tempu1+c1
    pred.append(tempu1)
pred1=np.array(pred)
np.savetxt("foo1.csv", pred1, delimiter=",")


# In[ ]:




