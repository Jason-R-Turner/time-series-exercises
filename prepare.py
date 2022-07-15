#!/usr/bin/env python
# coding: utf-8

# # Exercises

# In[1]:


import matplotlib.pyplot as plt
import os
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from datetime import timedelta, datetime
import acquire


# In[2]:


# plotting defaults
plt.rc('figure', figsize=(13, 7))
plt.style.use('seaborn-whitegrid')
plt.rc('font', size=16)


# Using your store items data:

# ## Acquire

# In[3]:


df = acquire.get_store_item_demand_data()
df.head(3)


# # Go back and make/use utility modules to summarize data

# In[4]:


df.dtypes


# 1. Convert date column to datetime format.

# In[5]:


# convert our date column to datetime type
df.sale_date = pd.to_datetime(df.sale_date)
df.dtypes


# 2. Plot the distribution of sale_amount and item_price.

# In[6]:


df['sale_amount'].hist()

plt.show()


# In[7]:


df.item_price.hist()

plt.show()


# In[8]:


# printing all columns of the dataframe
print(df.columns.tolist())


# 3. Set the index to be the datetime variable.

# In[9]:


df = df.set_index('sale_date').sort_index()
df.head(3)


# 4. Add a 'month' and 'day of week' column to your dataframe.

# In[10]:


# printing all columns of the dataframe
print(df.columns.tolist())
df.columns.tolist()


# In[11]:


df['month'] = df.index.month
df['day_of_week'] = df.index.strftime('%A')

df.head(3)


# 5. Add a column to your dataframe, sales_total, which is a derived from sale_amount (total items) and item_price.

# In[12]:


df['sales_total'] = df.sale_amount * df['item_price']
df.head(3)


# 6. Make sure all the work that you have done above is reproducible. That is, you should put the code above into separate functions and be able to re-run the functions and get the same results.

# In[13]:


def prep_store_data(df):
    df.sale_date = pd.to_datetime(df.sale_date)
    df = df.set_index('sale_date').sort_index()
    df['month'] = df.index.month
    df['day_of_week'] = df.index.strftime('%A')
    df['sales_total'] = df.sale_amount * df['item_price']
    return df


# In[14]:


prep_store_data(df)


# In[ ]:


df


# # Data Splitting

# In[15]:


acquire.get_opsd_data()


# Using the OPS data acquired in the Acquire exercises opsd_germany_daily.csv, complete the following:

# 1. Convert date column to datetime format.

# 2. Plot the distribution of each of your variables.

# 3. Set the index to be the datetime variable.

# 4. Add a month and a year column to your dataframe.

# 5. Fill any missing values.

# 6. Make sure all the work that you have done above is reproducible. That is, you should put the code above into separate functions and be able to re-run the functions and get the same results.

# In[ ]:




