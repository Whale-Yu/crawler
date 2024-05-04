# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/22 14:03
# @Author :yujunyu
# @Site :
# @File :weibo1.0.py
# @software: PyCharm

import re
import requests
import datetime
import os
import csv

def trans_time(v_str):
    """转换GMT时间为标准格式"""
    GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
    timeArray = datetime.datetime.strptime(v_str, GMT_FORMAT)
    ret_time = timeArray.strftime("%Y-%m-%d %H:%M:%S")
    return ret_time

page=1
head={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
    "cookie": "SUB=_2A25P3kqVDeRhGeNG6lQZ-SvOyziIHXVtIVbdrDV6PUJbktAKLUjGkW1NS26xPCiTVnTe52osGVe_d0ARTlDo2BXg; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWOHp8SW4P9S9xTrh2V2L1e5NHD95Qf1h2c1h.feo5XWs4Dqcjci--fi-82i-2ci--4iKLhi-zRi--Xi-isiKyWi--Xi-zRiKn7i--NiKLFi-zXi--fiKLhi-2R; _T_WM=51018460898; MLOGIN=1; XSRF-TOKEN=e50821; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E8%25A3%25B8%25E7%259C%25BC3D%26fid%3D100103type%253D1%2526q%253D%25E8%25A3%25B8%25E7%259C%25BC3D%26uicode%3D10000011"
}
parm={
    "containerid": "100103type=1&q=裸眼3D",
    "page_type": "searchall",
    "page": page
}
resp=requests.get("https://m.weibo.cn/api/container/getIndex",headers=head,params=parm,timeout=20).json()
# print(len(resp['data']['cards']))
for i in range(len(resp['data']['cards'])):
    try:
        # 页码
        page = page
        # 微博id
        id=resp['data']['cards'][i]['card_group'][0]['mblog']['id']
        # 微博作者
        user = resp['data']['cards'][i]['card_group'][0]['mblog']['user']['screen_name']
        # 发布时间
        time = resp['data']['cards'][i]['card_group'][0]['mblog']['created_at']
        time1 = trans_time(time)  # 转换时间
        # 微博内容
        content = resp['data']['cards'][i]['card_group'][0]['mblog']['text']
        # print(content)
        dr = re.compile(r'<[^>]+>', re.S)  # 解析text的内容
        content1 = dr.sub('', content)
        print(content1)
        # 微博正文url
        web_url ="https://m.weibo.cn/detail/"+id
        print(web_url)
        # print(content2)
        # 转发数
        reposts_count = (resp['data']['cards'][i]['card_group'][0]['mblog']['reposts_count'])
        # 评论数
        comments_count = resp['data']['cards'][i]['card_group'][0]['mblog']['comments_count']
        # 点赞数
        attitudes_count = resp['data']['cards'][i]['card_group'][0]['mblog']['attitudes_count']

        path_file_name = './weiboData.csv'
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['页码', '微博id',  '微博作者', '发布时间','微博内容', '微博正文url','转发数','评论数','点赞数'])
                writer.writerow([page,id,user,time1,content1,web_url,reposts_count,comments_count,attitudes_count])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow([page, id, user, time1, content1, web_url, reposts_count, comments_count, attitudes_count])
    except:
        pass


