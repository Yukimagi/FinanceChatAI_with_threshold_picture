#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 第三方套件 yfinance, 可用來串接 Yahoo Finance API 下載股票的價量資訊. 而且拿到的資料就是 Pandas 的 DataFrame
import yfinance as yf
import pandas as pd
import csv
import sys


# In[2]:

# 從命令列參數取得股票代號
stock_symbol = sys.argv[1]

# Download intraday data for 2330.TW
data = yf.download(stock_symbol, start="2022-01-01", end="2023-06-30", interval="1d")


# In[3]:


# Calculate intraday returns
data["Intraday_Return"] = (data["Close"] - data["Open"]) / data["Open"] * 100


# In[4]:


# Save the intraday return data to a CSV file
data.to_csv(f'Intraday return/{stock_symbol[0]}{stock_symbol[1]}{stock_symbol[2]}{stock_symbol[3]}_Intraday_Return.csv', encoding='utf-8')

