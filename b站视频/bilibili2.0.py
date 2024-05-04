# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/4 20:57
# @Author :yujunyu
# @Site :
# @File :bilibili1.0.py
# @software: PyCharm

"""
实现b站视频的爬取

"""

import requests
import re
import json
from pprint import pprint
import os
import time

b_time = time.time()

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

keyword = input("请输入爬取视频的关键字(如美女):")
page = int(input("请输入爬取的页数:"))
times = int(input("请输入爬取视频的时长(如时长小于5分钟输入5即可):"))

try:
    os.mkdir(f"{keyword}")
except:
    pass

offset = 30
for k in range(2, page + 2):
    baseurl = f"https://search.bilibili.com/all?vt=47304613&keyword={keyword}&from_source=webtop_search&spm_id_from=333.851&page={k}&o={offset}"
    print("第{}页".format(k))
    print("offset:{}".format(offset))
    print("baseurl:{}".format(baseurl))

    apiurl = f"https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page={k}&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword={keyword}&category_id=&search_type=video&dynamic_offset={offset}&preload=true&com2co=true"
    resp2 = requests.get(apiurl, headers=head)
    # pprint(resp2.text)
    res2 = json.loads(resp2.text)
    # print(len(res2['data']['result']))
    url_list = []
    video_time = []
    for i in range(len(res2['data']['result'])):
        url_list.append(res2['data']['result'][i]['arcurl'])
        video_time.append(res2['data']['result'][i]['duration'])
    print("videc_url_nums:{}".format(len(url_list)))
    print(url_list)
    print(video_time)
    for i, j in enumerate(url_list):
        url = f"{j}"
        videot = video_time[i]
        # print(type(videot))
        if int(videot.split(':')[0]) >= times:
            continue
        print("视频地址:" + url)
        video_name = url.split("/")[-1]
        # print(video_name)

        head = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            "referer": url
        }
        resp = requests.get(url, headers=head)
        # print(resp.text)
        video = re.findall('<script>window\.__playinfo__=(.*?)</script>', resp.text)[0]
        # print(video)
        result = json.loads(video)
        # pprint(result)

        try:
            video_download_url = result['data']['dash']['video'][0]['backupUrl'][0]
            print("视频下载url:" + video_download_url)
            print("{}正在下载".format(video_name))
            video_res = requests.get(video_download_url, headers=head)
            with open(f'{keyword}/' + video_name + '.mp4', mode='wb') as f:
                f.write(video_res.content)
            print("{}下载完成".format(video_name))
        except:
            print("该视频下载地址不存在，跳过")
    print("第{}页下载完成".format(k))

    offset += 30

e_time = time.time()
print("爬取时间:{:.2f}s".format(e_time - b_time))
