#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd 
import seaborn as sns
import matplotlib. pyplot as plt
import numpy as ns
df = pd.read_csv( 'covid_19_india.csv')


# In[37]:


print(df.info())


# In[38]:


import matplotlib. pyplot as plt
plt.figure(figsize=(20, 12))
plt.plot(df['Date'],df['Confirmed'])
plt.title('covid cases over time',size=30)
plt.xlabel( 'Time' ,size=30)
plt.ylabel( 'cases' ,size=10)
plt.show()


# In[39]:


import matplotlib. pyplot as plt
plt.figure(figsize=(20, 12))
plt.plot(df['Date'],df['Deaths'])
plt.title('covid death cases over time',size=30)
plt.xlabel( 'Time' ,size=30)
plt.ylabel( 'death' ,size=10)
plt.show()


# In[40]:


import matplotlib. pyplot as plt
plt.figure(figsize=(20, 12))
plt.plot(df['Date'],df['Cured'])
plt.title('covid cured over time',size=30)
plt.xlabel( 'Time' ,size=30)
plt.ylabel( 'cured' ,size=30)
plt.show()


# In[41]:


import matplotlib. pyplot as plt
plt.figure(figsize=(50, 5))
plt.scatter(df['State/UnionTerritory'],df['Confirmed'])
plt.show()


