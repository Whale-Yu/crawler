# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/11/9 14:00
# @Author :yujunyu
# @Site :
# @File :22.py
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
import os, csv

head = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
}

for page in range(1,100):
    print(f'正在爬取第{page}页')
    url = f'http://old.woniuxy.com/note/page-{page}'

    while True:
        try:
            resp = requests.get(url, headers=head, timeout=20)
            break
        except:
            print('重试1')

    html = etree.HTML(resp.text)
    div_list = html.xpath('/html/body/div[8]/div/div/div[1]/div')
    # print(div_list)

    for i in div_list:
        try:
            title = i.xpath('./div[2]/div[1]/a/text()')[0]
            href = 'http://old.woniuxy.com' + i.xpath('./div[2]/div[1]/a/@href')[0]
            info = i.xpath('./div[2]/div[2]/text()')[0]
            intro = i.xpath('./div[2]/div[3]/text()')[0]
            img_href = i.xpath('./div[1]/img/@href')[0]
            print(title)

            # path_file_name = './data11.csv'
            # if not os.path.exists(path_file_name):
            #     print('新建并且写入')
            #     with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
            #         writer = csv.writer(csvfile)
            #         writer.writerow(['page', 'title', 'info', 'intro', 'href'])
            #         writer.writerow([page, title, info, intro, href])
            # else:
            #     with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
            #         print('新建完成后写入')
            #         writer = csv.writer(csvfile)
            #         writer.writerow([page, title, info, intro, href])
        except:
            # 去除干扰div
            pass
