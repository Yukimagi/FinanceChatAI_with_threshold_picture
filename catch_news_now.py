#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager #edge時(預設瀏覽器)
from selenium.webdriver.edge.service import Service

import time
import csv
import datetime

data_list = []
data={}#使用大刮號{}創建字典
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

#模擬向下捲動，以確保載入更多內容
scrolls = 10
for _ in range(scrolls):
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    time.sleep(2)  # 等待頁面載入
            
#找到當前頁面
page_content=driver.page_source

# 使用 BeautifulSoup 解析頁面内容
soup = BeautifulSoup(page_content, "html.parser")
# 抓取日期元素
date_elements = soup.select("div._67tN.theme-meta time")

# 抓取標題元素
title_elements = soup.select("div._1xc2 h3")

# 將日期和標題對應成字典，然後添加到列表中
for date_element, title_element in zip(date_elements, title_elements):
    # 獲取現在的日期
    current_date = datetime.datetime.today().strftime('%m/%d')
    try:
        # 嘗試解析時間，並將其轉換成現在的日期格式
        time_obj = datetime.datetime.strptime(date_element.text, '%H:%M')
        data = {
            'date': current_date,
            'title': title_element.text
        }
        data_list.append(data)
    except ValueError:
        # 如果解析失敗，保留原樣
        data = {
            'date': date_element.text,
            'title': title_element.text
        }
        data_list.append(data)

driver.close()
# 輸出所有日期和標題對應的資料
for data in data_list:
    print(data['date'], data['title'])
            
with open('forecast/news_now.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data in data_list:
        # 寫入資料
        writer.writerow({'date': data['date'], 'title': data['title']})

