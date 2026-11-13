#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# ## Series

# In[6]:


x = [1,2,3,4]
var = pd.Series(x)
var


# In[10]:


x = [1,2,3,4]
var = pd.Series(x,index = ['a','c','e','g'])
var


# In[13]:


x = [1,2,3,4]
var = pd.Series(x,index = ['a','c','e','g'], dtype = "float", name = 'kk')
var


# In[3]:


s1 = pd.Series(12,index=[1,2,3,4,5,6])
s2 = pd.Series(12,index=[1,2,3,4])
print(s1+s2)


# ## datafram

# In[4]:


l =[1,2,3,4,5,6]
var = pd.DataFrame(l)
print(type(var))


# In[5]:


d = {"a":[1,2,3,4,5],"s":[1,2,3,4,5]}
var1 = pd.DataFrame(d)
print(type(var1))
print(var1)


# In[8]:


d = {"a":[1,2,3,4,5],"s":[1,2,3,4,5]}
var1 = pd.DataFrame(d,columns=["a"])

print(type(var1))
print(var1)


# In[13]:


d = {"a":[1,2,3,4,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5],1:[1,2,3,4,5]}
var1 = pd.DataFrame(d,columns=["a",1],index=["a","b","d","e","z"])

print(type(var1))
print(var1)


# In[14]:


d = {"a":[1,2,3,4,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5],1:[1,2,3,4,5]}
var1 = pd.DataFrame(d)

print(type(var1))
print(var1)


# #to get the value from column and row

# In[16]:


d = {"a":[1,23,3,4,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5],1:[1,2,3,4,5]}
var1 = pd.DataFrame(d)

print(type(var1))
print(var1)
print(var1["a"][1])


# In[18]:


list_1 =[[1,2,3,4,5],[11,12,13,14,15]]
var2 = pd.DataFrame(list_1)

print(type(var2))
print(var2)


# In[19]:


sr = {"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}
var3 = pd.DataFrame(sr)

print(type(var3))
print(var3)


# ## Arithmetic operations

# In[5]:


import pandas as pd
var = pd.DataFrame({"a":[1,2,3,4],"b":[1,2,3,4]})

var


# In[7]:


var["c"] = var ["a"] - var ["b"]

var


# In[8]:


var["c"] = var ["a"] + var ["b"]

var


# In[9]:


var["c"] = var ["a"] * var ["b"]

var


# In[10]:


var["c"] = var ["a"] / var ["b"]

var


# In[12]:


var1 = pd.DataFrame({"a":[10,20,30,40],"b":[11,12,13,14]})

var1


# In[15]:


var1["python"] = var1["a"] <= 20
var1["python_1"] = var1["b"] >= 13

var1


# # insert

# In[17]:


var = pd.DataFrame({"a":[1,2,3,4,5],"b":[9,8,7,6,5]})

var


# #var.insert( position , with which name, what need to insert

# In[19]:


var.insert(1,"python",var["a"])
var


# In[22]:


var.insert(1,"python_1",[11,21,31,41,51])
var


# In[24]:


var.insert(1,"python_12",var["a"][:3])
var


# # delete

# In[25]:


var = pd.DataFrame({"a":[1,2,3,4,5],"b":[9,8,7,6,5], "c":[11,12,13,14,15]})

var


# In[26]:


var1 = var.pop("b")
var1


# In[27]:


var


# In[28]:


del var["a"]
var


# # READ CSV File

# In[22]:


dfa = pd.read_csv("Desktop/Superstore_Sales_Analysis/datascience/a_data.csv")


# # Function

# In[24]:


dfa.index


# In[25]:


dfa.columns


# In[26]:


dfa.describe


# In[27]:


dfa.head()


# In[28]:


dfa.tail(2)


# In[29]:


dfa[:4]


# In[30]:


dfa[5:12]


# In[31]:


dfa.index.array


# In[32]:


dfa.to_numpy()


# # Dropna & Fillna

# In[34]:


df= pd.read_csv("Desktop/Superstore_Sales_Analysis/dataset/Book1.csv")


# In[35]:


df.dropna(axis=0)


# In[36]:


df.head()


# In[37]:


df.shape


# In[38]:


df.isnull().sum()


# In[39]:


(df.isnull().sum()/df.shape[0])*100


# In[40]:


df.isnull().sum().sum()


# In[41]:


(df.isnull().sum().sum()/df.shape[0]*df.shape[1])*100


# In[42]:


# value dropping


# In[43]:


df.drop(columns=['Salary'], inplace=True)


# In[44]:


df.dropna()


# In[45]:


df.dropna(inplace= True)


# In[46]:


df.isnull().sum()


# 
