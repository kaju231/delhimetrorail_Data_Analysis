#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as  pd


# In[3]:


df=pd.read_csv("delhimetrorail.csv")


# In[4]:


df


# In[5]:


df.head(30)


# In[6]:


df.shape


# In[7]:


df.index


# In[8]:


df.columns


# In[9]:


df.dtypes


# In[10]:


df["item_quantity"].unique()


# In[11]:


df.nunique()


# In[12]:


df.count()


# In[13]:


df["item_name"].value_counts


# In[14]:


df.info()


# In[15]:


df["receiving_date"][df['item_name']=='POLY BAG']


# In[16]:


df['receiving_date'][df['item_name']=='MOBILE']


# In[17]:


df['item_name'][df['item_quantity']=='2']


# In[23]:


import plotly.express as px # for  data visualization i.e provides functions to visualize a variety of types of dataimport matplotlib.pyplot as plt # to plot  diffrent charts
import matplotlib.pyplot as plt # to plot  diffrent charts


# In[ ]:





# In[29]:


station_counts = df['station_name'].value_counts()

# Now you can plot station_counts
plt.figure(figsize=(10, 6))
station_counts.plot(kind='bar')
plt.title('Number of Items Received per Station')
plt.xlabel('Station Name')
plt.ylabel('Number of Items Received')
plt.show()


# In[30]:


plt.figure(figsize=(10, 6))
station_counts.plot(kind='bar', color='skyblue')
plt.title('Total Quantity of Items Received per Station')
plt.xlabel('Station Name')
plt.ylabel('Total Quantity of Items Received')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


# In[ ]:


plt.subplot(2, 1, 2)
plt.pie(station_counts, labels=station_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Distribution of Items Received by Station')
plt.tight_layout()


# In[ ]:


# Pie chart
plt.subplot(2, 1, 2)
plt.pie(station_counts, labels=station_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Distribution of Items Received by Station')
plt.tight_layout()

plt.show()


# In[31]:


plt.figure(figsize=(8, 8))
plt.pie(station_counts, labels=station_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Total Quantity of Items Received per Station')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




