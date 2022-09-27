#!/usr/bin/env python
# coding: utf-8

# In[10]:


#pip install streamlit


# In[11]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# In[12]:


HairEye = pd.read_csv("HairEyeColor.csv")


# In[13]:


HairEye.head()


# In[14]:


st.title("Hair Eye Colour Database")


# In[15]:


InputHair = st.sidebar.selectbox("Select Hair Colour", ("Brown", "Black", "Blond", "Red"))


# In[20]:


HairEyeSelect = HairEye[HairEye["Hair"] == InputHair]


# In[21]:


st.dataframe(HairEyeSelect)


# In[18]:


fig = px.histogram(HairEye, x='Hair')


# In[19]:


st.plotly_chart(fig)


# In[ ]:




