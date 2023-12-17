#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
import sys
stockCode=sys.argv[2]
csv_file_path = ["news_1.csv","news_2.csv","news_3.csv","news_4.csv","news_5.csv",
                "news_6.csv","news_7.csv","news_8.csv","news_9.csv","news_10.csv",
                "news_11.csv","news_12.csv"]
csv_file_path2=["news_23_1.csv","news_23_2.csv","news_23_3.csv",
                 "news_23_4.csv","news_23_5.csv","news_23_6.csv"]
keyword = sys.argv[1]
output_csv_file_path = ["_1.csv","_2.csv","_3.csv","_4.csv","_5.csv",
                           "_6.csv","_7.csv","_8.csv","_9.csv","_10.csv",                                          "_11.csv","_12.csv","_23_1.csv","_23_2.csv","_23_3.csv",
                        "_23_4.csv","_23_5.csv","_23_6.csv"]
i=0
j=0
# 儲存含有關鍵字的資料的列表
#如果要個別月要放裡面
filtered_data = []

for f in csv_file_path:

    # 儲存含有關鍵字的資料的列表
    #如果要個別月要放裡面
    filtered_data = []
    # 使用 UTF-8 編碼讀取 CSV 檔案
    with open(f'新聞標題(2022~2023)/{f}', mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            if keyword in row['title']:
                filtered_data.append({'date': row['date'], 'title': row['title']})
    if filtered_data:
    # 使用 UTF-8 編碼寫入新的 CSV 檔案
    #將all改成output_csv_file_path[i]就可以按月輸出.csv
        with open(f'{keyword}過濾新聞/{stockCode}{output_csv_file_path[i]}', mode='w', encoding='utf-8', newline='') as csvfile:
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
    else:
        print(f'no output {output_csv_file_path[i]}')
        i+=1


# In[11]:


for f in csv_file_path2:
    # 儲存含有關鍵字的資料的列表
    #如果要個別月要放裡面
    filtered_data = []
    # 使用 UTF-8 編碼讀取 CSV 檔案
    with open(f'新聞標題(2022~2023)/{f}', mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            if keyword in row['title']:
                filtered_data.append({'date': '2023/'+row['date'], 'title': row['title']})

    if filtered_data:
    # 使用 UTF-8 編碼寫入新的 CSV 檔案
    #將all改成output_csv_file_path[i]就可以按月輸出.csv
        with open(f'{keyword}過濾新聞/{stockCode}{output_csv_file_path[i]}', mode='w', encoding='utf-8', newline='') as csvfile:
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
    else:
        print(f'no output {output_csv_file_path[i]}')
        i+=1


# In[ ]:




