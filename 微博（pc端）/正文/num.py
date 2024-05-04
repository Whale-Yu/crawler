# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/9/2 12:54
# @Author :yujunyu
# @Site :
# @File :num.py
# @software: PyCharm
"""
统计每个cvs的数据量、去重
"""
import pandas as pd
import os

basePath = './data_1'
num = 0
for i, j, k in os.walk(basePath):
    # print(k)#直接输出文件名
    print(len(k))
    for file in range(len(k)):
        # print(k[file])
        path_file_name = k[file]

        df = pd.read_csv(basePath+'/'+path_file_name)

        # 删除缺失值
        # df.dropna(subset=['正文'],inplace=True)
        # df.to_csv(basePath+'/'+path_file_name, index=False, encoding='utf_8_sig')

        # 去重
        # df.drop_duplicates(subset=['正文'], inplace=True, keep='first')  # subset:按什么去重，
        # df.to_csv('2.csv', index=False, encoding='utf_8_sig')

        # 统计数量
        print(k[file],len(df['用户']))

        num += len(df['用户'])
print(f'总数据量:{num}')
# 总数据量:102166
