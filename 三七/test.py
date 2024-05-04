# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/9/11 11:10
# @Author :yujunyu
# @Site :
# @File :test.py
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

url = 'https://18comic.vip/photo/256394'
head = {
    'cookie': 'ipcountry=US; AVS=jau2jknqshgc14bisalbfkcvsh; cover=1; guide=1; ipm5=21847f988256d779de6591985c7c4822; yuo1=%7B%22objName%22:%22uW2ZwViykbUJ9q%22,%22request_id%22:0,%22zones%22:%5B%7B%22idzone%22:%223714923%22,%22sub%22:%2287%22,%22here%22:%7B%7D%7D,%7B%22idzone%22:%223714923%22,%22sub%22:%2289%22,%22here%22:%7B%7D%7D,%7B%22idzone%22:%222967010%22,%22here%22:%7B%7D%7D,%7B%22idzone%22:%222967010%22,%22here%22:%7B%7D%7D%5D%7D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}
proxy = {
    "https": "http://127.0.0.1:10809"
}
while True:
    try:
        resp = requests.get(url=url, headers=head, proxies=proxy, timeout=20)
        break
    except:
        print('重试！！')
print(resp.text)



