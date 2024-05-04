# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/4 17:07
# @Author :yujunyu
# @Site :
# @File :car1.0.py
# @software: PyCharm


"""
https://so.iautos.cn/quanguo/p1asdsvepcatcpbnscac/#buyCars
"""

# 二手车辆信息
import requests
from lxml import etree
import csv
import os

pages=int(input("请输入爬取页数:"))

f = open("二手车信息.csv", mode='a+', encoding='utf_8_sig',newline="")
csvwriter = csv.writer(f)
csvwriter.writerow(['车辆品牌', '价格', '上牌时间', '里程', '所在地', '图片链接'])

try:
    os.mkdir('img')
except:
    pass
num=0
for j in range(1,pages+1):
    print("第一页{}".format(j))
    url = f"https://so.iautos.cn/quanguo/p{j}asdsvepcatcpbnscac/#buyCars"
    j=j+1
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=head)
    # print(resp.text)

    html = etree.HTML(resp.text)
    lis = html.xpath('/html/body/div[5]/div[2]/ul[2]/li')

    for i in lis:
        car_name = i.xpath('./a/h6/text()')[0]
        price = i.xpath('./a/div[4]/strong/text()')[0]
        time = i.xpath('./a/div[3]/span[1]/text()')[0]
        mileage = i.xpath('./a/div[3]/span[2]/text()')[0]
        location = i.xpath('./a/div[3]/span[3]/text()')[0]

        img_href = i.xpath('./a/div[2]/img/@src')[0]
        if img_href == "https://static.iautos.cn/www/iautos/dist/image/v3-public/car-default.jpg?v=20190617":
            img_href = i.xpath('./a/div[2]/img/@data-original')[0]

        print(img_href)
        # print(location)
        # print(mileage)
        # print(time)
        # print(detail)
        # print(price)
        # print(car_name)

        img_resp = requests.get(img_href)
        img_name = img_href.split("/")[-1].strip("-mediumpic")
        # print(img_name)
        num+=1

        with open("img/" + img_name, mode='wb') as f:
            f.write(img_resp.content)
        print("第{}张爬取成功！".format(num))

        csvwriter.writerow((car_name, price, time, mileage, location, img_href))
    f.close()


