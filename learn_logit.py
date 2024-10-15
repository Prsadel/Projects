#!/usr/bin/env python
# coding: utf-8

# In[133]:


from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

def genco(Sex):
    if Sex==b'male':
        return 0
    else:
        return 1

def catco(Parch):
    if Parch==b'S':
        return 1
    elif Parch==b'P':
        return 2
    else:
        return 0

ddtype=[('Pclass',float),('Sex',int),('Age',float),('SibSp',float),('Parch',float),('Ticket','U6'),('Fare',float),('Cabin','U6'),('Embarked',float),('Survived',int)]
trainu=np.genfromtxt("C:\\Users\\hp\\Downloads\\0000000000002429_training_titanic_x_y_train.csv",delimiter=',',dtype=ddtype,converters={1: genco,8:catco},skip_header=1)


# In[80]:


df=pd.DataFrame(trainu)
df


# In[81]:


print(df[1:10])
df['Age']=df.Age.fillna(df.Age.mean())
print(df)


# In[82]:


print(df)


# In[83]:


df.describe()


# In[84]:


df=df.drop(columns=['Ticket','Cabin'])
df


# In[126]:


a1=df.iloc[:,0:7]
a2=df.iloc[:,-1]
print(a1)


# In[127]:


clf=LogisticRegression(max_iter=1000)
clf.fit(a1,a2)


# In[128]:


clf.predict(a1)


# In[129]:


clf.score(a1,a2)


# In[116]:


def genco2(Sex):
    if Sex==b'male':
        return 0
    else:
        return 1

def catco2(Parch):
    if Parch==b'S':
        return 1
    elif Parch==b'P':
        return 2
    else:
        return 0


dd4type=[('Pclass',float),('Sex',int),('Age',float),('SibSp',float),('Parch',float),('Ticket','U6'),('Fare',float),('Cabin','U6'),('Embarked',float)]
testu=np.genfromtxt("C:\\Users\\hp\\Downloads\\0000000000002429_test_titanic_x_test.csv",delimiter=',',dtype=dd4type,converters={1: genco2,8:catco2},skip_header=1)


# In[117]:


testu


# In[118]:


testuu=pd.DataFrame(testu)
testuu=testuu.drop(columns=['Ticket','Cabin'])
testuu['Age']=testuu.Age.fillna(df.Age.mean())
testuu['Parch']=testuu.Parch.fillna(df.Parch.mean())
print(testuu)


# In[124]:


print(a1)


# In[134]:


tpreu=clf.predict(testuu)
fpreduu=np.array(tpreu)
np.savetxt("foou.csv",fpreduu,delimiter=',')


# In[119]:


df


# In[120]:


testuu.describe()


# In[ ]:




