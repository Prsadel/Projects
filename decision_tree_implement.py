#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
iris=datasets.load_iris()
x_train=iris.data
y_train=iris.target
features=[0,1,2,3]


# In[ ]:


define entropy()
define gain(x,y,a,old_entropy):
    maxu=np.max(arr[:,a])
    minu=np.min(arr[:,a])
    value=(maxu+minu)/2
    count_l=np.sum(arr[:,a] <= value)
    count_r=np.sum(arr[:,a] > value)
    d1=count_l/(y.shape[0])
    d2=count_l/(y.shape[0])
    greater_than_midpoint = x_train[:, 0] > value

# Extract corresponding Y values
    corresponding_Y = y_train[greater_than_midpoint]

# Find unique values and their counts
    unique_Y, counts = np.unique(corresponding_Y, return_counts=True)

# Find the index of the category with the maximum count
    max_count_index = np.argmax(counts)

# Find the value with the maximum count
    most_frequent_Y = unique_Y[max_count_index]

# Find the maximum count
    max_count1 = counts[max_count_index]
    p1=max_count1/(y.shape[0])
    
    # Boolean indexing to filter rows where feature <= midpoint
    less_than_equal_midpoint = x_train[:, 0] <= midpoint

# Extract corresponding Y values
    corresponding_Y = y_train[less_than_equal_midpoint]

# Find unique values and their counts
    unique_Y, counts = np.unique(corresponding_Y, return_counts=True)

# Find the index of the category with the maximum count
    max_count_index = np.argmax(counts)

# Find the value with the maximum count
    most_frequent_Y = unique_Y[max_count_index]

# Find the maximum count
    max_count2 = counts[max_count_index]
    p2=max_frequent_Y/(y.shape[0])
    new_entropy=(d1*(-1*p1*log(p1)))+(d2*(-1*p2*log(p2)))
    ig=new_entropy-old_entropy
    split_info=(-1*d1)*log(d1)+(-1*d2)*log(d2)
    return (ig/split_info,value,new_entropy)


# In[20]:


define splitter(x,y,fe):
    feture_split=0
    gain_value=0
    value_to=0
    node_entropy=0
    for i in range(len(fe)):
        a=gain(x,y,fe[i])
        if(a[0]>gain_value):
            gain_value=a[0]
            value_to=a[1]
            node_entropy=a[2]
    


# In[21]:


x_train.shape

