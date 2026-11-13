#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


data = {
    "salary" : [25000,30000,37000,28000,39000,48000,55000,52000,35000,57000,58000,60000,63000
               ]}


# In[4]:


import pandas as pd
df = pd.DataFrame(data)
df.head()


# In[5]:


df.info()


# In[6]:


df["dept"] = ['HR','IT','Finance','HR','IT','Finance','HR','IT','Finance','HR','IT','Finance','HR']


# In[7]:


df.head()


# In[8]:


df.info()


# # bivriate : numerical - numerical

# In[9]:


df["age"] = [21,22,23,34,33,49,50,51,59,37,39,40,45]


# In[10]:


df.head()


# # scatter plot:

# #analyese direct relationship weather salary increarese with age or not 

# In[11]:


plt.scatter(df["age"],df["salary"], color = "orange")
plt.show()


# #when age and salary itnccreases together is kn +ive relation
# 

# #line plot

# In[12]:


sort_age = df.sort_values("age")


# In[13]:


plt.plot(df["age"],df["salary"], color = "red", marker = "*", linewidth = "2")
plt.grid()
plt.show()


# In[14]:


plt.plot(sort_age["age"],df["salary"], color = "red", marker = "*", linewidth = "2")
plt.grid()
plt.show()


# # bar chart

# In[15]:


plt.bar(df["age"],df["salary"], color = "green")
plt.show()


# # bivariate : numerical - categorical

# In[16]:


hr_sal = df[df["dept"] == "HR"]["salary"]
hr_sal


# In[17]:


it_sal = df[df["dept"] == "IT"]["salary"]
it_sal


# In[18]:


fin_sal = df[df["dept"] == "Finance"]["salary"]
fin_sal


# #boxplot:

# In[19]:


plt.boxplot([hr_sal,it_sal,fin_sal], labels = ["HR","IT","FINANCE"])
plt.show()


# #piechart

# In[20]:


#piechart

salary_by_dept = df.groupby("dept")["salary"].sum()
salary_by_dept


# In[21]:


plt.pie(salary_by_dept, labels = salary_by_dept.index, autopct = "%1.2f", shadow = True , explode = [0.1,0,0.1])
plt.axis("equal")
plt.show()


# In[22]:


hr_mean = sum(hr_sal)/len(hr_sal)
it_mean = sum(it_sal)/len(it_sal)
fin_mean = sum(fin_sal)/len(fin_sal)


# In[23]:


plt.bar(["HR", "IT", "Finance"], [hr_mean, it_mean, fin_mean], color = ["green", "black", "red"])
plt.grid()
plt.show()


# # multivariate analysis 

# #3numerical columns

# In[24]:


df.head


# In[25]:


df["experience"] = [1,2,3,1.5,3,5,6,12,10,1,4,6,8]
df


# # bubble plot

# #3 numerical column

# In[26]:


plt.scatter(df["age"], df["salary"], s = df["experience"]*20, color = "skyblue", edgecolors = "black")
plt.show()


# In[27]:


plt.scatter(df["age"], df["salary"], s = df["experience"]*20, color = "skyblue", edgecolors = "black")
plt.title("Age vs Salary vs Experience")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid()
plt.show()


# #2numerical and 1 catagorical column

# In[28]:


plt.scatter(df["age"], df["salary"], c = df["dept"].map({"HR": "yellow","IT":"blue", "Finance": "orange"}), )
plt.title("Age vs Salary vs Experience")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.show()


# In[29]:


color ={"HR": "yellow","IT":"blue", "Finance": "orange"}
for dept, color in color.items():
    df_dept = df[df["dept"] == dept]
    plt.scatter(df_dept["age"], df_dept["salary"], c = color, label = dept)
plt.legend()


# # object oriented api

# In[ ]:





# In[30]:


fig, axs = plt.subplots(1,3, figsize = (10,5))

#line plot:

axs[0].plot(sort_age["age"], df["salary"], color = "red", marker = "*", linewidth = "2", markersize = 2)
axs[0].grid()
axs[0].set_title("Line Plot")
axs[0].set_xlabel("Age")
axs[0].set_ylabel("Salary")

#histogram:

axs[1].hist(df["salary"], bins = 5, color = "skyblue")
axs[1].set_title("histogram")
axs[1].set_xlabel("Salary")
axs[1].set_ylabel("Frequency")

#boxplot:

axs[2].boxplot(df["salary"])
axs[2].set_title("boxplot")
axs[2].set_xlabel("Salary")
plt.savefig("multipleplots.png")
plt.show()


# In[31]:


#multiple numerical values


# In[43]:


data2 = {
    'Year': [2020,2021,2022,2023],
    'sales':[100,150,200,250],
    'profit': [20,30,40,50],
    'expenses': [80,120,160,200]
}


# In[44]:


import pandas as pd
df2 = pd.DataFrame(data2)


# In[45]:


plt.plot(df2["Year"], df2["sales"], label = "sales")
plt.plot(df2["Year"], df2["profit"], label = "profit")
plt.plot(df2["Year"], df2["expenses"], label = "expenses")

plt.title("Financial Analysis")
plt.xlabel("Year")
plt.ylabel("amount")
plt.legend()
plt.show()


# # 3d plot
# 

# In[47]:


df.head


# In[52]:


ax = plt.axes(projection = "3d")
ax.scatter(df["age"], df["salary"], df["experience"])
ax.set_xlabel("Age")
ax.set_ylabel("Salary")
ax.set_zlabel("Experience")
plt.show()


# In[53]:


import plotly.express as px


# In[56]:


fig = px.scatter_3d(df, x='age', y='salary', z='experience',title='2d scatter plot')
fig.show()


# In[ ]:




