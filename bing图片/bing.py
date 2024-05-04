# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/9/19 16:04
# @Author :yujunyu
# @Site :
# @File :bing.py
# @software: PyCharm

s = """
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
          ┗━┻━┛   ┗━┻━┛"""
print(s)

import requests
from lxml import etree
import os, csv
import random
import pandas as pd
import getpass
from faker import Faker

# keyword = 'CG动画人脸'
# nums = 100
keyword = input('请输入爬取图片的关键字(如炸鸡):')
nums = eval(input('请输入爬取图片的数量（如100）:'))

url_api = 'https://cn.bing.com/images/async?'

header = {
    'user-agent': Faker().user_agent()
}
j = 0
while j <= nums // 7:

    v = random.randint(10, 100)

    param = {
        'q': keyword,
        'first': v,
        'count': v,
        'cw': '1177',
        'ch': '729',
        'relp': '35',
        'tsc': 'ImageHoverTitle',
        'datsrc': 'I',
        'layout': 'RowBased_Landscape',
        'apc': '0',
        'mmasync': '1',
        'dgState': 'x*947_y*1152_h*186_c*4_i*36_r*7',
        'IG': '77C0FA2EFE4A4185B823CA742950C9A8',
        'SFX': '2',
        'iid': 'images.5528'
    }

    while True:
        try:
            resp1 = requests.get(url=url_api, headers=header, params=param, timeout=20)
            break
        except:
            print('request failed! retry 1！')
    # print(resp1.text)
    html = etree.HTML(resp1.text)
    ul = html.xpath('//*[@id="mmComponent_images_5528_2_1"]/ul')
    for i in ul:
        try:
            src = i.xpath('./li[1]/div/div[1]/a/div/img/@src')[0]
            print(f'正在获取链接:{src}')
        except:
            print('error')

        path_file_name = f'./{keyword}_src.csv'
        if not os.path.exists(path_file_name):
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['src'])
                writer.writerow([src])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([src])

    print(f'{j}')
    j += 1

user_name = getpass.getuser()  # 获取计算机的用户名
dir_name = f'C:/Users/{user_name}/Desktop/{keyword}/'
data = pd.read_csv(f'./{keyword}_src.csv')
pic_url = data['src']
for i in range(len(pic_url)):
    url = pic_url[i]
    print(f'正在下载图片：{url}')
    while True:
        try:
            pic_resp = requests.get(url)
            break
        except:
            print('request failed! retry 2！')
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
        with open(dir_name + keyword + '_' + str(i) + ".jpg", mode='wb') as f:
            f.write(pic_resp.content)
        f.close()
    else:
        with open(dir_name + keyword + '_' + str(i) + ".jpg", mode='wb') as f:
            f.write(pic_resp.content)
        f.close()

print('爬取结束！！！')

os.remove(f'./{keyword}_src.csv')
