# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/8/31 9:45
# @Author :yujunyu
# @Site :
# @File :test1.py
# @software: PyCharm

import pandas as pd
import os

basePath = './data1'
num = 0
for i, j, k in os.walk(basePath):
    # print(k)#直接输出文件名
    print(len(k))
    for file in range(len(k)):
        # print(k[file])
        path_file_name = k[file]

        df = pd.read_csv(basePath+'/'+path_file_name)

        # 删除缺失值
        df.dropna(subset=['评论内容'],inplace=True)
        df.to_csv(basePath+'/'+path_file_name, index=False, encoding='utf_8_sig')

        # 统计数量
        print(k[file],len(df['用户id']))

        num += len(df['用户id'])
print(f'总数据量:{num}')
# 总数据量:102166
