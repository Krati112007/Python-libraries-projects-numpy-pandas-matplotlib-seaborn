#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np


# In[3]:


sns.get_dataset_names()


# In[3]:


penguins = sns.load_dataset('penguins')
penguins.head()


# In[4]:


penguins['species'].value_counts()


# In[5]:


penguins['island'].value_counts()


# In[6]:


penguins = sns.load_dataset('penguins')
penguins.head()


# In[7]:


sns.scatterplot(data = penguins, x = "flipper_length_mm", y= "body_mass_g", hue = 'island')


# In[8]:


#the way of styling theams are as :
# dark
# white
#whitegrid
# darkgrid
# ticks 


# In[9]:


sns.set_style("ticks")
sns.scatterplot(data = penguins, x = "flipper_length_mm", y= "body_mass_g", hue = 'island')


# In[10]:


sns.set_style("whitegrid")
sns.scatterplot(data = penguins, x = "flipper_length_mm", y= "body_mass_g", hue = 'island')


# In[11]:


sns.set_style("darkgrid")
sns.scatterplot(data = penguins, x = "flipper_length_mm", y= "body_mass_g", hue = 'island')


# In[12]:


sns.set_style("dark")
sns.scatterplot(data = penguins, x = "flipper_length_mm", y= "body_mass_g", hue = 'island')


# In[13]:


#seaborns has 4 diff. type of workdone 
#context() allows us to override default parameters. this affects size of label, line 
#paper
#notebook
#talk
#poster


# In[14]:


sns.set_style("dark")
sns.set_context("poster")
sns.scatterplot(data = penguins, x = "flipper_length_mm", y= "body_mass_g", hue = 'island')


# In[15]:


sns.set_style("dark")
sns.set_context("talk")
sns.scatterplot(data = penguins, x = "flipper_length_mm", y= "body_mass_g", hue = 'island')


# In[16]:


sns.set_style("dark")
sns.set_context("notebook")
sns.scatterplot(data = penguins, x = "flipper_length_mm", y= "body_mass_g", hue = 'island')


# In[17]:


sns.set_style("dark")
sns.set_context("paper")
sns.scatterplot(data = penguins, x = "flipper_length_mm", y= "body_mass_g", hue = 'island')
sns.despine()


# In[18]:


#PALETTE

#set 1 bright and high contrast color
#set 2 soft and pastel color
#set 3 mix of soft and bold


#palette 
# deep, muted, 'bright', 'pastel', 'dark', 'colorblind'

#palette depending on graph 
#Qualitative: the color assigned to each group need to be distinct 
#sequential: data with ordered progression(low -> high)
#diverging: data with meaningful midpoint or mixed value like+ve,-ve 


# In[19]:


sns.set_style("dark")
sns.set_context("paper")
sns.scatterplot(data = penguins, x = "flipper_length_mm", y= "body_mass_g", hue = 'island', palette = "Set1")
sns.despine()


# In[20]:


sns.scatterplot(data = penguins,x ="species",y = "body_mass_g", hue = "island", style = "sex") 


# In[21]:


sns.stripplot(data = penguins, x = "species", y = "body_mass_g" , hue = "island", dodge = "true", jitter = True)


# In[ ]:


#histogram
sns.
sns.histplot(data = penguins, x = "body_mass_g" )


# In[4]:


diamonds = sns.load_dataset('diamonds')
diamonds.head()


# In[ ]:





# In[ ]:




