# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/9/22 16:13
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
from bs4 import BeautifulSoup
import csv, os

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}
i = 1
while i > 0:
    # https://www.037hdmovie.com/page/3/
    print(f'第{i}页')
    url = f'https://www.037hdmovie.com/page/{i}/'
    while True:
        try:
            resp1 = requests.get(url, headers=head, timeout=20)
            break
        except:
            print('重试11')
    # print(resp1.text)

    Soup = BeautifulSoup(resp1.text, 'lxml')
    divs = Soup.find_all("div", class_="moviefilm")
    # print(divs)
    print(f'当前页数量:{len(divs)}')
    for d in divs:
        div = d.find_all('a')
        # print(div)
        # print(len(div))
        name = div[1].text
        url = div[1].get('href')
        print(name, url)

        path_file_name = './data.csv'
        # 如果没有csv文件，就新建文件，并写入
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['页数', '电影名', '详情网址'])
                writer.writerow([i, name, url])
        # 如果有csv文件，直接追加写入
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow([i, name, url])
    i += 1
