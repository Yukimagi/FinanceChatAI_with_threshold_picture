#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
from PIL import Image, ImageFilter, ImageEnhance
# 創建一個空的DataFrame，用於存放每個月份的結果
all_results = pd.DataFrame()


file_name = 'ask/ans_ask.csv'
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

# 將最終結果寫入一個結果檔案
all_results.to_csv('ask/point_ask.csv', index=False)


# In[ ]:


# 讀取所有結果
all_results = pd.read_csv('ask/point_ask.csv')

# 計算所有日期的平均分數
average_point = all_results['point'].mean()

# 將平均分數轉換為百分比
average_point_percent = round(average_point * 100, 2)

print(f'平均結論值：{average_point_percent}')

if average_point_percent>50:
    image=Image.open('股市指標圖/正正.png')
    image.show()
    print('股市指標圖/正正.png')
elif average_point_percent<50 and average_point_percent>0:
    image=Image.open('股市指標圖/正.png')
    image.show()
    print('股市指標圖/正.png')
elif average_point_percent==0:
    image=Image.open('股市指標圖/普通.png')
    image.show()
    print('股市指標圖/普通.png')
elif average_point_percent<0 and average_point_percent>-50:
    image=Image.open('股市指標圖/負.png')
    image.show()
    print('股市指標圖/負.png')
elif average_point_percent<-50:
    image=Image.open('股市指標圖/負負.png')
    image.show()
    print('股市指標圖/負負.png')
