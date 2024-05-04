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

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
}
url = 'https://yande.re/post?page=2'

proxy = {
    "https":"http://127.0.0.1:10809"
}

resp = requests.get(url, headers=head, proxies=proxy,timeout=20)
# print(resp.status_code)
html = etree.HTML(resp.text)
lis = html.xpath('/html/body/div[8]/div[1]/div[2]/div[4]/ul/li')
print(len(lis))
num=0
for i in lis:
    url1 = i.xpath('./a/@href')[0]
    print(url1)

    img_resp = requests.get(url1,proxies=proxy,headers=head)
    with open("img/" + str(num) + ".jpg", mode='wb') as f:
        f.write(img_resp.content)
    f.close()

    num+=1
