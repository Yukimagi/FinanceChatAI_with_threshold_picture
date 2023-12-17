#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
import sys

csv_file_path = ["forecast/news_now.csv"]
# 從命令列參數取得關鍵字
keyword = sys.argv[1]
output_csv_file_path = "forecast/news_now_filter.csv"

i=0   
# 儲存含有關鍵字的資料的列表
#如果要個別月要放裡面
filtered_data = []

for f in csv_file_path:
    # 儲存含有關鍵字的資料的列表
    #如果要個別月要放裡面
    #filtered_data = []
    # 使用 UTF-8 編碼讀取 CSV 檔案
    with open(f, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            if keyword in row['title']:
                filtered_data.append({'date': row['date'], 'title': row['title']})

    # 使用 UTF-8 編碼寫入新的 CSV 檔案
    #將all改成output_csv_file_path[i]就可以按月輸出.csv
    with open(output_csv_file_path, mode='w', encoding='utf-8', newline='') as csvfile:
        # 定義欄位
        fieldnames = ['date', 'title']

        # 將 dictionary 寫入 CSV 檔
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 寫入第一列的欄位名稱
        writer.writeheader()

        # 寫入篩選後的資料
        for data in filtered_data:
            writer.writerow({'date': data['date'], 'title': data['title']})
    i+=1

