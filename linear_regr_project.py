#!/usr/bin/env python
# coding: utf-8

# In[108]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def updu(x1,y1,s2,c2,a1):
    a=len(x1)
    for i in range(len(s2)):
        tempu1=0
        cu1=0
        for j in range(a):
            tempu3=0
            for l in range(len(s2)):
                tempu3=tempu3+s2[l]*x1[j][l]
            tempu3=(y1[j]-tempu3-c2)*(-2/a)
            cu1=cu1+tempu3;
            tempu1=tempu1+(tempu3*x1[j][i])
        if(a1<500):
            s2[i]=s2[i]-0.5*tempu1
            c2=c2-0.5*cu1
        else if(a1>900):
            s2[i]=s2[i]-0.001*tempu1
            c2=c2-0.001*cu1
        else:
            s2[i]=s2[i]-0.1*tempu1
            c2=c2-0.1*cu1
            
    print(s2,c2)
    return s2,c2
            
trainu=np.genfromtxt("C:\\Users\\hp\\Downloads\\0000000000002419_training_ccpp_x_y_train.csv",delimiter=',')
x=trainu[:,0:4]
y=trainu[:,4]
df=pd.DataFrame(x)
# print(type(df))
df.columns=["a1","a2",'a3','a4']
b1=min(df.a1) 
b2=max(df.a1)
df['a1']=(df.a1-b1)/(b2-b1)
b1=min(df.a2) 
b2=max(df.a2)
df['a2']=(df.a2-b1)/(b2-b1)
b1=min(df.a3) 
b2=max(df.a3)
df['a3']=(df.a3-b1)/(b2-b1)
b1=min(df.a4) 
b2=max(df.a4)
df['a4']=(df.a4-b1)/(b2-b1)
x2=np.array(df)
s1=[1,1,1,1]
c1=0
for i in range(500):
    s1,c1=updu(x2,y,s1,c1,i)
for i in range(400):
    s1,c1=updu(x2,y,s1,c1,i+500)


# In[112]:


s1=[-58.17349095034874, -19.087773941013996, 5.771966690509746, -8.116896403319922] 
c1=497.05679251684865
for i in range(100):
    s1,c1=updu(x2,y,s1,c1,i+900)


# In[113]:


x_testu=np.genfromtxt("C:\\Users\\hp\\Downloads\\0000000000002419_test_ccpp_x_test.csv",delimiter=',')
ypreuu=[]
df1=pd.DataFrame(x_testu)
# print(type(df))
df1.columns=["a1","a2",'a3','a4']
b1=min(df1.a1) 
b2=max(df1.a1)
df1['a1']=(df1.a1-b1)/(b2-b1)
b1=min(df1.a2)
b2=max(df1.a2)
df1['a2']=(df1.a2-b1)/(b2-b1)
b1=min(df1.a3)
b2=max(df1.a3)
df1['a3']=(df1.a3-b1)/(b2-b1)
b1=min(df1.a4)
b2=max(df1.a4)
df1['a4']=(df1.a4-b1)/(b2-b1)
x3=np.array(df1)
for i in range(len(x3)):
    tempu4=0
    for l in range(len(s1)):
        tempu4=s1[l]*x3[i][l]
    tempu4=tempu4+c1
    ypreuu.append(tempu4)
yfpruu=np.array(ypreuu)
roundarr = np.round(yfpruu, decimals=2)
print(roundarr.shape,roundarr)
# Convert the NumPy array to a pandas DataFrame
# df = pd.DataFrame(roundarr)

# Specify the desired format string to avoid exponential notation
# format_str = {:.2f}  # This formats the numbers to have two decimal places
# Save the DataFrame to a CSV file with the specified format string
# df.to_csv("foo2.csv", index=False, header=False)

# np.savetxt("foo2.csv",roundarr, delimiter=",")


# print(type(x))
# ypred=[]
# for j in range(len(x)):
#     tempu4=0
#     l1=[0,0,0,0]
#     for l in range(len(s1)):
#         tempu4=tempu4+s1[l]*x[j][l]
#         l1[l]=x[j][l]
#     tempu4=tempu4+c1
#     ypred.append(tempu4)
    
# import matplotlib.pyplot as plt
# tp=np.arange(420,500)
# plt.scatter(y,ypred)
# plt.plot(tp,tp,"b--")
# df=pd.DataFrame(x)
# # print(type(df))
# df.columns=["a1","a2",'a3','a4']
# df['b1']=df.a1**2
# df['b2']=df.a2**2
# df['b3']=df.a3**2
# df['b4']=df.a4**2
# x2=np.array(df)
# x2


# In[54]:


# ypru=pd.DataFrame(yfpruu)
# ypru.columns=['a1']
# b0=min(ypru.a1) 
# bo=max(ypru.a1)
# ypru['a1']=((ypru.a1)*(bo-b0)+b0)
# yfprauu=np.array(ypru)
# print(yfprauu)
# # np.savetxt("foo2.csv", yfprauu, delimiter=",")


# In[116]:


print(x_testu.shape)
ypreuu1=[]
for i in range(len(x2)):
    tempu4=0
    for l in range(len(s1)):
        tempu4=s1[l]*x2[i][l]
    tempu4=tempu4+c1
    ypreuu1.append(tempu4)
yfpruu1=np.array(ypreuu1)
# # ypru1=pd.DataFrame(yfpruu1)
# # ypru1.columns=['a1']
# # b0=min(ypru1.a1) 
# # bo=max(ypru1.a1)
# # ypru1['a1']=((ypru1.a1)*(bo-b0)+b0)
# # yfprauu1=np.array(ypru1)
# print(y)
# print(yfpruu1)


# In[99]:


print(x_testu.shape)
print(type(roundarr))
print(x2)
x2=np.random.shuffle(x2)
print(x2)
print(s1,c1)


# In[117]:


print(y)
print(yfpruu)

