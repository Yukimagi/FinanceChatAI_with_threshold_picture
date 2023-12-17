#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
# 最大化瀏覽器視窗
driver.maximize_window()
#________________________________________________________________________________

data_list1 = []
data1={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=7 #1~7
i=0
# 初始化列表用於存儲日期和標題

#日期往前按20頁
for i in range(20):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#1月
for i in range(31):
    try:
        print(f"{div_1}{div_2}{div_3}")
            
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
            
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇1/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
#日期往後按10頁
#for i in range(10):
    #nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()

        # 選擇1/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data1 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list1.append(data1)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data1 in data_list1:
    print(data1['date'], data1['title'])
            
with open('新聞標題(2022~2023)/news_1.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data1 in data_list1:
        # 寫入資料
        writer.writerow({'date': data1['date'], 'title': data1['title']})


# In[22]:


#2月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list2 = []
data2={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=3 #1~7
i=0;
#日期往前按19頁
for i in range(19):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#2月
for i in range(28):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇2/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇2/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data2 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list2.append(data2)
        

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data2 in data_list2:
    print(data2['date'], data2['title'])
            
with open('新聞標題(2022~2023)/news_2.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data2 in data_list2:
        # 寫入資料
        writer.writerow({'date': data2['date'], 'title': data2['title']})


# In[23]:


#3月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list3 = []
data3={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=3 #1~7
i=0;
#日期往前按18頁
for i in range(18):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#3月
for i in range(31):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇3/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇3/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data3 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list3.append(data3)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data3 in data_list3:
    print(data3['date'], data3['title'])
            
with open('新聞標題(2022~2023)/news_3.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data3 in data_list3:
        # 寫入資料
        writer.writerow({'date': data3['date'], 'title': data3['title']})


# In[24]:


#4月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list4 = []
data4={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=6 #1~7
i=0;
#日期往前按17頁
for i in range(17):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#4月
for i in range(30):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇4/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇4/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data4 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list4.append(data4)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data4 in data_list4:
    print(data4['date'], data4['title'])
            
with open('新聞標題(2022~2023)/news_4.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data4 in data_list4:
        # 寫入資料
        writer.writerow({'date': data4['date'], 'title': data4['title']})


# In[25]:


#5月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list5 = []
data5={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=1 #1~7
i=0;
#日期往前按16頁
for i in range(16):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#5月
for i in range(31):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇3/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇3/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data5 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list5.append(data5)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data5 in data_list5:
    print(data5['date'], data5['title'])
            
with open('新聞標題(2022~2023)/news_5.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data5 in data_list5:
        # 寫入資料
        writer.writerow({'date': data5['date'], 'title': data5['title']})


# In[27]:


#6月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list6 = []
data6={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=4 #1~7
i=0;
#日期往前按15頁
for i in range(15):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#6月
for i in range(30):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇6/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇6/1
        end =(By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data6 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list6.append(data6)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data6 in data_list6:
    print(data6['date'], data6['title'])
            
with open('新聞標題(2022~2023)/news_6.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data6 in data_list6:
        # 寫入資料
        writer.writerow({'date': data6['date'], 'title': data6['title']})


# In[28]:


#7月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list7 = []
data7={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=6 #1~7
i=0;
#日期往前按14頁
for i in range(14):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#7月
for i in range(31):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇7/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇7/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data7 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list7.append(data7)
            
        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data7 in data_list7:
    print(data7['date'], data7['title'])
            
with open('新聞標題(2022~2023)/news_7.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data7 in data_list7:
        # 寫入資料
        writer.writerow({'date': data7['date'], 'title': data7['title']})


# In[29]:


#8月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list8 = []
data8={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=2 #1~7
i=0;
#日期往前按13頁
for i in range(13):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#8月
for i in range(31):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇8/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇8/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data8 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list8.append(data8)
            
        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data8 in data_list8:
    print(data8['date'], data8['title'])
            
with open('新聞標題(2022~2023)/news_8.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data8 in data_list8:
        # 寫入資料
        writer.writerow({'date': data8['date'], 'title': data8['title']})


# In[30]:


#9月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list9 = []
data9={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=5 #1~7
i=0;
#日期往前按12頁
for i in range(12):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#9月
for i in range(30):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇9/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 =driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇9/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data9 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list9.append(data9)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data9 in data_list9:
    print(data9['date'], data9['title'])
            
with open('新聞標題(2022~2023)/news_9.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data9 in data_list9:
        # 寫入資料
        writer.writerow({'date': data9['date'], 'title': data9['title']})


# In[31]:


#10月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list10 = []
data10={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=7 #1~7
i=0;
#日期往前按11頁
for i in range(11):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#10月
for i in range(31):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇10/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇10/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data10 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list10.append(data10)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data10 in data_list10:
    print(data10['date'], data10['title'])
            
with open('新聞標題(2022~2023)/news_10.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data10 in data_list10:
        # 寫入資料
        writer.writerow({'date': data10['date'], 'title': data10['title']})


# In[32]:


#11月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list11 = []
data11={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=3 #1~7
i=0;
#日期往前按10頁
for i in range(10):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#11月
for i in range(30):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇11/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇11/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data11 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list11.append(data11)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data11 in data_list11:
    print(data11['date'], data11['title'])
            
with open('新聞標題(2022~2023)/news_11.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data11 in data_list11:
        # 寫入資料
        writer.writerow({'date': data11['date'], 'title': data11['title']})


# In[33]:


#12月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list12 = []
data12={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=5 #1~7
i=0;
#日期往前按9頁
for i in range(9):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#12月
for i in range(31):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇12/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇12/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data12 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list12.append(data12)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data12 in data_list12:
    print(data12['date'], data12['title'])
            
with open('新聞標題(2022~2023)/news_12.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data12 in data_list12:
        # 寫入資料
        writer.writerow({'date': data12['date'], 'title': data12['title']})


# In[5]:


#2023 1月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list23_1 = []
data23_1={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=1 #1~7
i=0;
#日期往前按9頁
for i in range(9):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#1月
for i in range(31):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇1/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇1/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data23_1 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list23_1.append(data23_1)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data23_1 in data_list23_1:
    print(data23_1['date'], data23_1['title'])
            
with open('新聞標題(2022~2023)/news_23_1.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data23_1 in data_list23_1:
        # 寫入資料
        writer.writerow({'date': data23_1['date'], 'title': data23_1['title']})


# In[10]:


#2023 2月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list23_2 = []
data23_2={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=4 #1~7
i=0;
#日期往前按8頁
for i in range(8):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#2月
for i in range(28):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇2/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇2/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data23_2 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list23_2.append(data23_2)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data23_2 in data_list23_2:
    print(data23_2['date'], data23_2['title'])
            
with open('新聞標題(2022~2023)/news_23_2.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data23_2 in data_list23_2:
        # 寫入資料
        writer.writerow({'date': data23_2['date'], 'title': data23_2['title']})


# In[11]:


#2023 3月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list23_3 = []
data23_3={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=4 #1~7
i=0;
#日期往前按7頁
for i in range(7):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#3月
for i in range(31):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇3/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇3/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data23_3 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list23_3.append(data23_3)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data23_3 in data_list23_3:
    print(data23_3['date'], data23_3['title'])
            
with open('新聞標題(2022~2023)/news_23_3.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data23_3 in data_list23_3:
        # 寫入資料
        writer.writerow({'date': data23_3['date'], 'title': data23_3['title']})


# In[12]:


#2023 4月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list23_4 = []
data23_4={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=7 #1~7
i=0;
#日期往前按6頁
for i in range(6):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#4月
for i in range(30):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇4/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇4/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data23_4 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list23_4.append(data23_4)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data23_4 in data_list23_4:
    print(data23_4['date'], data23_4['title'])
            
with open('新聞標題(2022~2023)/news_23_4.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data23_4 in data_list23_4:
        # 寫入資料
        writer.writerow({'date': data23_4['date'], 'title': data23_4['title']})


# In[14]:


#2023 5月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list23_5 = []
data23_5={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=2 #1~7
i=0;
#日期往前按5頁
for i in range(5):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#5月
for i in range(31):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇5/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇5/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data23_5 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list23_5.append(data23_5)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data23_5 in data_list23_5:
    print(data23_5['date'], data23_5['title'])
            
with open('新聞標題(2022~2023)/news_23_5.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data23_5 in data_list23_5:
        # 寫入資料
        writer.writerow({'date': data23_5['date'], 'title': data23_5['title']})


# In[15]:


#2023 6月
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
data_list23_6 = []
data23_6={}#使用大刮號{}創建字典
url='https://news.cnyes.com/news/cat/tw_stock_news?exp=a'
driver.get(url)

date=driver.find_element(By.CLASS_NAME,'_Qfx4')
date.click()
div_1=2 #1or2
div_2=2 #2~7
div_3=5 #1~7
i=0;
#日期往前按4頁
for i in range(4):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[1]/div[1]/div[1]'))).click()
#6月
for i in range(30):
    try:
        # 初始化列表用於存儲日期和標題
        data_list = []
        print(f"{div_1}{div_2}{div_3}")
        if(i!=0):
            # 使用 JavaScript 進行滾動
            driver.execute_script("window.scrollBy(0, 300);")
            # 選擇日期選擇器
            date_selector = driver.find_element(By.CLASS_NAME, '_Qfx4')
            date_selector.click()
        # 暫時的變數
        temp_div_1 = div_1
        temp_div_2 = div_2
        temp_div_3 = div_3

        # 選擇6/1    
        start = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start))
        start2 = driver.find_element(*start)
        action = ActionChains(driver)
        action.move_to_element(start2).click().perform()
        # 選擇6/1
        end = (By.XPATH, f'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[{temp_div_1}]/div[{temp_div_2}]/div[{temp_div_3}]/div')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(end))
        end2 = driver.find_element(*end)
        action2 = ActionChains(driver)
        action2.move_to_element(end2).click().perform()
        #確定按鈕
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[2]/button[1]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)

    
#模擬向下捲動，以確保載入更多內容
        scrolls = 3
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
            data23_6 = {
                'date': date_element.text,
                'title': title_element.text
            }
            data_list23_6.append(data23_6)

        i=i+1
        if temp_div_3 == 7:
            temp_div_3 = 1
            if temp_div_2 == 7:
                temp_div_2 = 2
                if temp_div_1 == 2:
                    nextpage = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]')
                    nextpage.click()
                    temp_div_1 = 1
                else:
                    temp_div_1 = temp_div_1 + 1
            else:
                temp_div_2 = temp_div_2 + 1
        else:
            temp_div_3 = temp_div_3 + 1

        # 此輪迴圈結束後，將暫時的變數賦值給 div_1、div_2 和 div_3
        div_1 = temp_div_1
        div_2 = temp_div_2
        div_3 = temp_div_3
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except NoSuchElementException:
        if(div_3==7):
            div_3=1
            if(div_2==7):
                div_2=2
                if(div_1==2):
                    nextpage=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/main/div[3]/div[1]/nav/div/div/div[1]/div[2]/div[1]/div[3]').click()
                    div_1=1
                else:
                    div_1=div_1+1
            else:
                div_2=div_2+1
        else:
            div_3=div_3+1
        date3=driver.find_element(By.CLASS_NAME,'_Qfx4')
        date3.click()
        # 滾動網頁到最上層
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
driver.close()
# 輸出所有日期和標題對應的資料
for data23_6 in data_list23_6:
    print(data23_6['date'], data23_6['title'])
            
with open('新聞標題(2022~2023)/news_23_6.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['date', 'title']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()
    for data23_6 in data_list23_6:
        # 寫入資料
        writer.writerow({'date': data23_6['date'], 'title': data23_6['title']})


# In[ ]:




