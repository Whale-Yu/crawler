# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/27 11:38
# @Author :yujunyu
# @Site :
# @File :yueguangshe.py
# @software: PyCharm
import requests
import csv
import os
from gettype import types  # 引入gettype.py文件

url="http://www.3rdguide.com/web/arm/index"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71",
    "X-Requested-With":"XMLHttpRequest"     # 注意这里是ajax异步请求，所以才会出现页面不刷新
}
print(type)
for type in range(1,len(types)+1):
    print(f"第{type}类武器:{types[type-1]}")
    parm={
        "page": 1,
        "pageSize": 1,
        "type": type
    }
    resp=requests.get(url,headers=head,params=parm).json()
    # print(resp)
    print(f"总页数为:{resp['totalPage']}")
    for page in range(1,(resp['totalPage'])+1):
        parm = {
            "page": page,
            "pageSize": 1,
            "type": type
        }
        resp1=requests.get(url,params=parm,headers=head).json()
        print(f"当前页数的武器数量{len(resp1['data'])}")
        for i in range(len(resp1['data'])):
            arms_name=resp1['data'][i]['armsName']
            weapon_intro = resp1['data'][i]['weapon_intro']
            weapon_star = resp1['data'][i]['weapon_star']
            arms_gj=resp1['data'][i]['armsgj']
            arms_hx=resp1['data'][i]['armshx']
            arms_url="http://www.3rdguide.com"+resp1['data'][i]['armsurl']
            arms_img="http:"+resp1['data'][i]['armsImg']

            path_file_name = './armsData.csv'
            if not os.path.exists(path_file_name):
                print('新建并且写入')
                with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['类别','类别名','页数','武器名', '武器介绍', '武器星级', '攻击', '会心', '武器详情url', '武器图片url'])
                    writer.writerow([type, types[type-1], page, arms_name, weapon_intro, weapon_star, arms_gj, arms_hx ,arms_url, arms_img])
            else:
                with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                    print('新建完成后写入')
                    writer = csv.writer(csvfile)
                    writer.writerow([type, types[type-1], page,  arms_name, weapon_intro, weapon_star, arms_gj, arms_hx, arms_url, arms_img])



