#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


# In[2]:


stockList = []
for i in range(1, 25):
    url = "https://vn.investing.com/stock-screener/?sp=country::178|sector::a|industry::a|equityType::a%3Ceq_market_cap;1" + str(i)
    driver = webdriver.Firefox()
    driver.get(url)
    # Wait for the page to fully load
    driver.implicitly_wait(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    tables = soup.find_all('table')
    dfs = pd.read_html(str(tables))
    df = dfs[-1]
    stockList.extend(df['Ký hiệu'].tolist())  


# In[3]:


print(stockList)


# In[4]:


len(stockList)


# In[ ]:




