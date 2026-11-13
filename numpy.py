#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


myarr=np.array([3,4])


# In[3]:


myarr


# In[4]:


myarr.shape


# In[5]:


listarry=np.array([[1,2,3],[2,3,4],[4,5,6]])


# In[6]:


listarry


# In[10]:


zeros = np.zeros((2,5))


# In[11]:


zeros


# In[12]:


rng = np.arange(15)


# In[13]:


rng


# In[14]:


lspace = np.linspace(1,5,5)


# In[15]:


lspace


# In[16]:


lspace = np.linspace(1,5,10)


# In[17]:


lspace


# In[18]:


emp = np.empty((4,6))


# In[19]:


emp


# In[20]:


emp_like = np.empty_like(lspace)


# In[21]:


emp_like


# In[22]:


ide = np.identity(45)


# In[23]:


ide


# In[24]:


ide.shape


# In[25]:


arr = np.arange(99)


# In[26]:


arr


# In[27]:


arr.reshape(3,33)


# In[34]:


#data


# In[33]:


data=np.array([23,11,23,34,56,6,55,43,32,0,0,22])


# In[35]:


data


# In[42]:


# mean


# In[36]:


np.mean(data)


# In[40]:


d=np.sum(data) / len(data)


# In[41]:


d


# In[47]:


def mean(data):
    return np.sum(data) / len(data)

print("Mean:", mean(data))


# In[43]:


# median


# In[44]:


np.median(data)


# In[48]:


print("Median:", np.median(data))


# In[49]:


# Mode


# In[50]:


from scipy import stats

print(stats.mode(data, keepdims=False).mode)


# In[52]:


# VARIANCE


# In[53]:


def variance(data):
    m = mean(data)
    return np.sum((data - m) ** 2) / len(data)


# In[54]:


print("Population Variance:", variance(data))


# In[51]:


# STANDARD DEVIATION


# In[55]:


std=np.sqrt(variance(data))


# In[56]:


std


# In[59]:


# COVARIANCE AND CORRELATION


# In[61]:


X = np.array([[10, 100],[20, 150],[30, 200],[40, 250],[50, 300]])


# In[63]:


Covariance = np.cov(X, rowvar=False)
Correlation = np.corrcoef(X, rowvar=False)


# In[64]:


Covariance,Correlation


# In[89]:


# PERCENTILE AND QUARTILES


# In[66]:


data1 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
p = 25


# In[68]:


data1 = np.sort(data)


# In[69]:


data1


# In[74]:


index = (p / 100) * (len(data1) - 1)


# In[75]:


index


# In[76]:


lower = int(np.floor(index))


# In[77]:


upper = int(np.ceil(index))


# In[78]:


lower,upper


# In[82]:


data1[lower] , data1[upper]


# In[83]:


result = data[lower] + (data[upper] - data[lower]) * (index - lower)


# In[84]:


result


# In[85]:


q1 = np.percentile(data, 25)
q1


# In[87]:


q2 = np.percentile(data, 50)
q2


# In[88]:


q3 = np.percentile(data, 75)
q3


# In[91]:


# OUTLIERS BY IQR


# In[92]:


q1, q3 = np.percentile(data, [25, 75])


# In[93]:


iqr = q3 - q1


# In[94]:


iqr


# In[95]:


lower = q1 - 1.5 * iqr


# In[96]:


lower


# In[97]:


upper = q3 + 1.5 * iqr


# In[98]:


upper


# In[99]:


outliers = data[(data < lower) | (data > upper)]


# In[100]:


outliers


# In[ ]:




