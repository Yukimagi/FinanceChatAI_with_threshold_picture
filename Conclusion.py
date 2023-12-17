#!/usr/bin/env python
# coding: utf-8

# In[5]:


from datetime import datetime, timedelta
from workalendar.asia import Taiwan

# 创建台湾的工作日历
cal = Taiwan()

# 设置起始日期和结束日期
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 6, 30)

# 创建一个列表来存储周休二日和国定假日的日期
holidays = []

# 遍历指定时间范围内的每一天
current_date = start_date
while current_date <= end_date:
    # 检查是否为周末（周六或周日）或国定假日
    if cal.is_working_day(current_date):
        current_date += timedelta(days=1)
        continue

    # 如果不是工作日，则将其添加到列表中
    holidays.append(current_date.strftime('%Y-%m-%d'))

    current_date += timedelta(days=1)

# 打印所有的周休二日和国定假日日期
for holiday in holidays:
    print(holiday)


# In[6]:


import pandas as pd
import sys

# 創建一個空的DataFrame，用於存放每個月份的結果
all_results = pd.DataFrame()
keyword=sys.argv[1]

j=2

# 處理每個月份的原始檔案
for month in range(1, 13):
    file_name = f'{keyword}ans/{keyword}ans_{month}.csv'
    try:
        df = pd.read_csv(file_name)

        # 將 Y/N 轉換為數字
        df[' Y/N'] = df[' Y/N'].map({'#yes': 1, '#no': -1, '#unknown': 0})

        # 進行分組計算並計算平均分數
        grouped = df.groupby('date')[' Y/N'].mean().reset_index()
        grouped.rename(columns={' Y/N': 'point'}, inplace=True)

        # 計算小數點後第二位的平均分數
        grouped['point'] = grouped['point'].apply(lambda x: round(x, 2))
        # 將處理後的結果合併到 all_results DataFrame 中
        all_results = pd.concat([all_results, grouped])
    except FileNotFoundError:
        # 如果文件不存在
        print(f'{file_name}不存在')


# In[7]:


# 處理每個月份的原始檔案
for month in range(1, 7):
    file_name = f'{keyword}ans/{keyword}ans_23_{month}.csv'
    try:
        df = pd.read_csv(file_name)

        # 將 Y/N 轉換為數字
        df[' Y/N'] = df[' Y/N'].map({'#yes': 1, '#no': -1, '#unknown': 0})

        # 進行分組計算並計算平均分數
        grouped = df.groupby('date')[' Y/N'].mean().reset_index()
        grouped.rename(columns={' Y/N': 'point'}, inplace=True)

        # 計算小數點後第二位的平均分數
        grouped['point'] = grouped['point'].apply(lambda x: round(x, 2))
        # 將處理後的結果合併到 all_results DataFrame 中
        all_results = pd.concat([all_results, grouped])
    except FileNotFoundError:
        # 如果文件不存在
        print(f'{file_name}不存在')
# 將最終結果寫入一個結果檔案
all_results.to_csv(f'{keyword}_conclusion/point_{keyword}.csv', index=False)


# In[8]:


# 讀取兩個CSV檔案
point_df = pd.read_csv(f'{keyword}_conclusion/point_{keyword}.csv')
intraday_return_df = pd.read_csv(f'Intraday return/{keyword}_Intraday_Return.csv')

# 將point_df的日期轉換成datetime格式
point_df['date'] = pd.to_datetime(point_df['date'])

# 將intraday_return_df的日期轉換成datetime格式
intraday_return_df['Date'] = pd.to_datetime(intraday_return_df['Date'])

# 初始化結果列表
results = []

profits=[]
profits2=[]

# 比較每一個日期的點數和隔日的Intraday_Return
for index, row in point_df.iterrows():
    date = row['date']
    point = row['point']
    
    # 找到隔日的日期
    next_date = date + pd.DateOffset(days=1)
    #print(f"Date: {date}, Next Date: {next_date}")
    while next_date.strftime('%Y-%m-%d') in holidays:
        next_date = next_date + pd.DateOffset(days=1)
        #print(f"Date: {date}, Next Date: {next_date}")
        
    # 在intraday_return_df中尋找隔日的Intraday_Return
    next_day_row = intraday_return_df[intraday_return_df['Date'] == next_date]
    #print("Next Day Row:")
    #print(next_day_row)
    
    # 如果找到了相應的隔日資料
    if not next_day_row.empty:
        intraday_return = next_day_row.iloc[0]['Intraday_Return']
        open_price = next_day_row.iloc[0]['Open']
        close_price = next_day_row.iloc[0]['Close']
        
        #if(point>=0):
            #profit1=close_price-open_price#-(0.000228*open_price)-(0.000228*close_price)-(0.0015*close_price)
            #profits.append({'date':next_date.strftime('%Y-%m-%d'),'profit':profit1})
        if(point>0):
            profit2=close_price-open_price#-(0.000228*open_price)-(0.000228*close_price)-(0.0015*close_price)
            profits2.append({'date':next_date.strftime('%Y-%m-%d'),'profit':profit2})
        # 根據條件判斷並記錄conclusion
        #if(point<0):
            #profits.append({'date':next_date.strftime('%Y-%m-%d'),'profit':0})
            #profits2.append({'date':next_date.strftime('%Y-%m-%d'),'profit':0})
        if (point >= 0 and intraday_return >= 0) or (point <= 0 and intraday_return <= 0):
            conclusion = 1
        else:
            conclusion = 0
        
        results.append({'date': date.strftime('%Y-%m-%d'), 'conclusion': conclusion})

# 將結果列表轉換成DataFrame
results_df = pd.DataFrame(results)

# 將結果列表轉換成DataFrame
#profits_df = pd.DataFrame(profits)
profits2_df = pd.DataFrame(profits2)

# 計算所有conclusion的總和/資料筆數
average_conclusion = (results_df['conclusion'].sum() / len(results_df))*100

# 計算所有profits的總和
#if not profits_df.empty:
    #all_profits = profits_df['profit'].sum()#/ len(profits_df)
#else:
    #all_profits=0.0;
if not profits2_df.empty:
    all_profits2 = profits2_df['profit'].sum()/ len(profits2_df)
else:
    all_profits2=0.0

# 將結果寫入新的CSV檔案
results_df.to_csv('conclusion_2022_2330.csv', index=False)

#if(all_profits>all_profits2):               
    # 將結果寫入新的CSV檔案
    #profits_df.to_csv(f'{keyword[j]}_conclusion/profit_{keyword[j]}.csv', index=False)
    #print(f"總獲利期望值：{all_profits}元")
#else:
profits2_df.to_csv(f'{keyword}_conclusion/profit_{keyword}.csv', index=False)
print(f"總獲利期望值：{all_profits2}元")

print(f"平均結論值：{average_conclusion}%")


# In[ ]:




