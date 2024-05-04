# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/11/15 21:32
# @Author :yujunyu
# @Site :
# @File :vr.py
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

resp=requests.get('https://news.cctv.com/yuanchuang/VR/index.shtml',timeout=20)

resp.encoding = 'utf-8'  # 处理中文乱码
print(resp.text)
html = etree.HTML(resp.text)
print(html)
