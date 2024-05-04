# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/9/7 16:55
# @Author :yujunyu
# @Site :
# @File :美容店.py
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

import json
with open('city.json',encoding='utf-8') as json_file:
	data1 = json.load(json_file)
print(len(data1['cityList']))
for c in range(len(data1['cityList'])):
    city_id=data1['cityList'][c]['cityId']
    city_name=data1['cityList'][c]['cityName']
    print(city_id,city_name)

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    'Cookie': 's_ViewType=10; _hc.v=6619f80b-058c-3150-f2cc-3e80c35a5e6e.1662540464; fspop=test; _lxsdk_cuid=1831726e345c8-0acbed5388d2f3-26021a51-144000-1831726e345c8; _lxsdk=1831726e345c8-0acbed5388d2f3-26021a51-144000-1831726e345c8; WEBDFPID=6u7zwy2z489w5z03yv06z6035599914y81682728uxv979588w24x969-1977900784090-1662540784090SMMCMQUfd79fef3d01d5e9aadc18ccd4d0c95073195; dplet=acdc4236c285c56ff2ce7488fd903869; dper=af9882cb131b480ea0deeeb785e8f9dc06d0304e07eccff2adff411a73d13657631a883767b0518f578d126cdaa37de4ea1cafbdb701b0cbc1511c20e58d9354c46dca47221fe6c18123f80e3b3f860600a5fd8515b43dfb4e6a08a626659a0e; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_4246847684; ctu=913810b1612ceb2d7be889b833132ca0adb51aee2b1b840f870a1d76b584ed96; cy=117; cye=anqing; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1662541245; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1662543145; _lxsdk_s=1831726e346-1d6-a6a-599%7C%7C32'
}

pages=50
for p in range(1,pages+1):
    print(f'正在写入第{p}页')
    url=f'https://www.dianping.com/search/keyword/120/0_%E7%BE%8E%E5%AE%B9%E5%BA%97/p{p}'
    while True:
        try:
            resp1=requests.get(url,headers=head,timeout=20)
            break
        except:
            print('重试1！')
    # print(resp1.text)
    html1=etree.HTML(resp1.text)
    lis=html1.xpath('//*[@id="shop-all-list"]/ul/li')
    print(len(lis))
    for li in lis:
        shop_name=li.xpath('./div[2]/div[1]/a/h4/text()')[0]
        shop_url=li.xpath('./div[2]/div[1]/a/@href')[0]

        print(shop_name, shop_url)
        while True:
            try:
                resp2=requests.get(shop_url,headers=head,timeout=20)
                break
            except:
                print('重试2！')
        html2=etree.HTML(resp2.text)
        try:
            shop_address=html2.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/a/span/text()')[0]+html2.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/span[2]/text()')[0]
        except:
            shop_address=''

        try:
            shop_phone=html2.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/p[1]/span[2]/text()')[0]
        except:
            shop_phone=''

        print(shop_phone,shop_address.replace(' ','').strip('\n').strip('\t').strip('\r'))

        path_file_name='shop_messages.csv'
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['店名', '地址', '联系方式', '详情url'])
                writer.writerow([shop_name, shop_address.replace(' ','').strip('\n').strip('\t').strip('\r'),shop_phone,shop_url])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow([shop_name, shop_address.replace(' ','').strip('\n').strip('\t').strip('\r'),shop_phone,shop_url])



