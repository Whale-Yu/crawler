# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/11/8 14:08
# @Author :yujunyu
# @Site :
# @File :短信轰炸.py
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


# coding=utf-8
"""
    @project: automation_tools
    @Author：gaojs
    @file： test010.py
    @date：2022/10/19 16:12
    @blogs: https://www.gaojs.com.cn
"""
import time

import requests
from faker import Factory


class SMS:
    """短信发送功能"""

    def __init__(self, account, password):
        """account:APIID(用户中心【验证码通知短信】-【产品纵览】查看)
           password：APIKEY(用户中心【验证码通知短信】-【产品纵览】查看)
           self.url:接口请求地址
           接口网站：https://www.ihuyi.com/
        """
        self.accout = account
        self.passwod = password
        self.url = 'https://106.ihuyi.com/webservice/sms.php?method=Submit'
        randon_ua = Factory.create()
        self.ua = randon_ua.user_agent()

    def send_sms(self, mobile, content):
        """
            发短信
            :param mobile: 手机号
            :param content: 短信内容
            :return:None
        """
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain",
            "User-Agent": self.ua
        }

        data = {'account': self.accout,
                'password': self.passwod,
                'mobile': mobile,
                'content': content
                }
        # 发起请求：
        response = requests.post(self.url, headers=headers, data=data)
        print(response.content.decode())


if __name__ == '__main__':
    sms = SMS('xxxxxxxxx', 'xxxxxxxxxxxxxxxxxx')
    for i in range(3):
        time.sleep(2)
        print(f"********************* 短信轰炸第 {i + 1} 次成功！！！")
        sms.send_sms('1380000000', '您的验证码是：8888。 请不要把验证码泄露给其他人。')