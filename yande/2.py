# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/9/7 12:15
# @Author :yujunyu
# @Site :
# @File :1.py
# @software: PyCharm

"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃CREATE BY SNIPER┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛

"""
import requests
from lxml import etree
import os,csv

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
}

proxy = {
    "https": "185.162.228.1"
}

# 22071
pages = 22071
for page in range(271, pages + 1):
    print(f'正在写入第{page}页')
    url = f'https://yande.re/post?page={page}'
    while True:
        try:
            resp = requests.get(url, headers=head, proxies=proxy, timeout=20)
            break
        except:
            print('重试1！')
    # print(resp.status_code)
    html = etree.HTML(resp.text)
    lis = html.xpath('/html/body/div[8]/div[1]/div[2]/div[4]/ul/li')
    print(f'{len(lis)}张图片')
    num=0
    for i in lis:
        url1 = i.xpath('./a/@href')[0]
        id=str(page)+'-'+str(num)
        print(url1)

        num+=1

        # 保存图片url
        path_file_name='pic_url11111.csv'
        if not os.path.exists(path_file_name):
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['id','url'])
                writer.writerow([id,url1])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([id,url1])
