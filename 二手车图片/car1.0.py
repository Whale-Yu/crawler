# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/4 17:07
# @Author :yujunyu
# @Site :
# @File :car1.0.py
# @software: PyCharm

# 二手车辆信息
import requests
from lxml import etree
import csv


url = "https://so.iautos.cn/quanguo/p1asdsvepcatcpbnscac/#buyCars"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=head)
# print(resp.text)

html = etree.HTML(resp.text)
lis = html.xpath('/html/body/div[5]/div[2]/ul[2]/li')

f = open("二手车信息.csv", mode='a+', encoding='utf-8')
csvwriter = csv.writer(f)
csvwriter.writerow(['车辆品牌', '价格', '上牌时间','里程','所在地','图片链接'])

num = 1
for i in lis:
    car_name = i.xpath('./a/h6/text()')[0]
    price = i.xpath('./a/div[4]/strong/text()')[0]
    time = i.xpath('./a/div[3]/span[1]/text()')[0]
    mileage=i.xpath('./a/div[3]/span[2]/text()')[0]
    location=i.xpath('./a/div[3]/span[3]/text()')[0]

    img_href =i.xpath('./a/div[2]/img/@src')[0]
    if img_href=="https://static.iautos.cn/www/iautos/dist/image/v3-public/car-default.jpg?v=20190617":
        img_href=i.xpath('./a/div[2]/img/@data-original')[0]

    print(img_href)
    # print(location)
    # print(mileage)
    # print(time)
    # print(detail)
    # print(price)
    # print(car_name)

    img_resp = requests.get(img_href)
    with open("img/" + str(num) + ".jpg", mode='wb') as f:
        f.write(img_resp.content)
    num += 1
    f.close()

    csvwriter.writerow((car_name, price, time,mileage,location,img_href))

f.close()

