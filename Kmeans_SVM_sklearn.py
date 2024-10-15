#!/usr/bin/env python
# coding: utf-8

# In[6]:


# using nearest neguhbour classification
import numpy as np
import pandas as pd
from sklearn import neighbors,metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# In[7]:


data=pd.read_csv("D:\\ml_data\\car.data")
print(data)
X=data[['buying','maint','safety']]
print(data.columns)
Y=data[['typ']]
# for i in range(lenX[0]):
#     X[:,i]=Le.fit_traansform(X[:,i])
X=pd.get_dummies(X)
label_mapping={
    'unacc':0,
    'acc':1,
    'good':2,
    'vgood':3
    }
Y['typ']=Y['typ'].map(label_mapping)
Y=np.array(Y)
print(Y)
print(X.head)


# In[8]:


xtrai,xtes,ytrai,ytes=train_test_split(X,Y,test_size=0.2)
model=neighbors.KNeighborsClassifier(n_neighbors=25,weights='uniform')
model.fit(xtrai,ytrai)
ypred=model.predict(xtes)
accuracy=metrics.accuracy_score(ytes,ypred)
print(ypred)
print(accuracy)


# In[15]:


from sklearn import datasets
from sklearn import svm
iris=datasets.load_iris()
X=iris.data
Y=iris.target
xtra,xtes,ytrai,ytes=train_test_split(X,Y,test_size=0.2)
# print(type(X))
# print(Y)
model=svm.SVC()
model.fit(xtra,ytrai)
ypred=model.predict(xtes)
accscore=metrics.accuracy_score(ytes,ypred)
print(ypred,ytes)
print(accscore)


# In[1]:




