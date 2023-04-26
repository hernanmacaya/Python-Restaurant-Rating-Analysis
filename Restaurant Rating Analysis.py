#!/usr/bin/env python
# coding: utf-8

# ## Packages

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[2]:


#load data enconding the special characters
df = pd.read_csv('C:/Users/herna/Documents/HERNÁN/Data Analysis/PGP Data Analytics/3_Courses (7)/7_Data Analyst Capstone/Project 3 - Marketing/Zomato Data.csv', encoding='latin-1')


# ## EDA

# In[3]:


#top 5
df.head()


# In[4]:


#data types and columns names
df.info()


# In[5]:


#data shape (rows, columns)
df.shape


# In[6]:


#unique values --> only ID as it should be
df.nunique(axis=0)


# In[7]:


#nulls
df.isna().sum()


# In[8]:


#drop any row with null values (9)
df = df.dropna(how = 'any', axis = 0)


# In[9]:


#new shape, with 9 rows deleted
df.shape


# In[10]:


#summary of count, min, max, mean, st dev for numerical values
df.describe()


# In[11]:


#duplicates
df.duplicated().sum()


# In[12]:


# df[(df['Aggregate rating'] == 0)]


# In[13]:


#eliminate 0.0 ratings
#inplace to make it permanent

df.drop(df[df['Aggregate rating'] ==0].index, inplace = True)


# In[14]:


#new shape, with 0.0 rating deleted
df.shape


# ## Geographical Distribution

# In[15]:


df['Country Code'].value_counts()


# #### country code = 1 --> India
# #### country code = 216 --> USA

# In[16]:


df['City'].value_counts()


# #### as presumed, most of them are Indian cities

# ## Ratings Distribution

# In[17]:


df['Aggregate rating'].value_counts()


# #### Rating moves between 3.0 and 3.7 mostly

# In[18]:


df['Rating color'].value_counts()


# #### Orange rating color gets the most frequency

# In[19]:


df.groupby(['Rating color'])['Aggregate rating'].mean()


# #### Rating average per Rating color

# ## Restaurant Presence

# In[20]:


#top 10 restaurants
df['Restaurant Name'].value_counts().head(10)


# In[21]:


#use rest name as index, presence as values
sns.barplot(y = df['Restaurant Name'].value_counts().head(10).index, x = df['Restaurant Name'].value_counts().head(10).values)


# ## Delivery Providers

# In[22]:


df['Has Online delivery'].value_counts()


# ## Table Booking

# In[23]:


df['Has Table booking'].value_counts()


# ## Both delivery and table booking

# In[24]:


df.value_counts(['Has Online delivery', 'Has Table booking'])


# ## Comparison of no. of votes for delivery and table booking

# In[25]:


pd.crosstab(df['Aggregate rating'], df['Has Online delivery']).plot.bar()


# ## Cuisines Presence

# In[26]:


#top 10 cuisines combinations
df['Cuisines'].value_counts().head(10)


# In[27]:


sns.barplot(y = df['Cuisines'].value_counts().head(10).index, x = df['Cuisines'].value_counts().head(10).values)


# ## Max and Min no. of cuisines provided

# In[28]:


df['Cuisines'].str.split(',').apply(len).value_counts()


# In[29]:


sns.barplot(x = df['Cuisines'].str.split(',').apply(len).value_counts().index, y = df['Cuisines'].str.split(',').apply(len).value_counts().values)


# ## No. of Cuisines and Avg. Rating

# In[30]:


df.groupby([df['Cuisines'].str.split(',').apply(len)])['Aggregate rating'].mean()


# In[31]:


sns.barplot(x = df.groupby([df['Cuisines'].str.split(',').apply(len)])['Aggregate rating'].mean().index, y = df.groupby([df['Cuisines'].str.split(',').apply(len)])['Aggregate rating'].mean().values)


# ##### No. of cuisines offered affect directly the rating

# ## Agg Rating and Votes

# In[32]:


df.groupby([df['Votes'].value_counts()])['Aggregate rating'].mean()


# In[33]:


df.groupby([df['Votes'].value_counts()])['Aggregate rating'].mean().plot()


# ##### It looks like there is no relation between the amount of votes and the aggregate rating

# ## Save clean file

# In[34]:


df.to_csv('C:/Users/herna/Documents/HERNÁN/Data Analysis/PGP Data Analytics/3_Courses (7)/7_Data Analyst Capstone/Project 3 - Marketing/Zomato Data Clean.csv', index = False)

