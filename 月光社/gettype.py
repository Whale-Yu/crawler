# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/27 16:05
# @Author :yujunyu
# @Site :
# @File :gettype.py
# @software: PyCharm

import requests
from lxml import etree

url="http://www.3rdguide.com/web/arm/index"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71"

}
response = requests.get(url,headers=head)
html=etree.HTML(response.text)
amrs_type_list =html.xpath('/html/body/div[2]/div[3]/div/div[2]/div/a')
types=[]
for arm in amrs_type_list:
    types.append(arm.xpath('./@title')[0])

