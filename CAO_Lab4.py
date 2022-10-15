#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
from datetime import date
import json as json
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd


# In[15]:


# Pick a stock 
ticker_name = input("Stock's ticker: ")
ticker = yf.Ticker(ticker_name)


# In[16]:


name = ticker.info['longName']


# In[17]:


current_price = ticker.info["regularMarketPreviousClose"]


# In[18]:


target_mean_price = ticker.info["targetMeanPrice"]


# In[19]:


cash = ticker.info["totalCash"]


# In[20]:


margin = ticker.info["profitMargins"]


# In[21]:


today = date.today()


# In[22]:


print(ticker_name)
print(name)
print(current_price)
print(target_mean_price)
print(cash)
print(margin)
print(today)


# In[23]:


dictionary = {
    "Date": today,
    "Ticker": ticker_name,
    "Company Name": name,
    "Current Price": current_price,
    "Target Mean Price": target_mean_price,
    "Cash On Hand": cash,
    "Profit Margins": margin
}

with open("stock.json", "w") as outfile:
    json.dump(dictionary, outfile, indent=7, sort_keys=False, default=str)


# In[24]:


with open('stock.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(json_object)
print(type(json_object))


# In[25]:


df = ticker.history()
df2 = df["High"]
df3 = df2.head(5)


# In[26]:


plt.plot(df3)
plt.show()


# In[ ]:




