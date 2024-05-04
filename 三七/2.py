# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/9/13 8:06
# @Author :yujunyu
# @Site :
# @File :2.py
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
# 导入需要的包
import requests # 请求包
from lxml import etree
import os, csv  # 文件处理

# 模拟浏览器header
head = {
    # 'cookie': 'ipcountry=US; AVS=jau2jknqshgc14bisalbfkcvsh; cover=1; guide=1; ipm5=21847f988256d779de6591985c7c4822; yuo1=%7B%22objName%22:%22uW2ZwViykbUJ9q%22,%22request_id%22:0,%22zones%22:%5B%7B%22idzone%22:%223714923%22,%22sub%22:%2287%22,%22here%22:%7B%7D%7D,%7B%22idzone%22:%223714923%22,%22sub%22:%2289%22,%22here%22:%7B%7D%7D,%7B%22idzone%22:%222967010%22,%22here%22:%7B%7D%7D,%7B%22idzone%22:%222967010%22,%22here%22:%7B%7D%7D%5D%7D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'

}
# 空列表来存数据，目的是后续统计数据量
data = []
# 循环——有多少页，就循环几次
for j in range(1, 8):
    # url———通过翻页发现，有个值会变，其他保持不变
    url = f'http://sqi.100ppi.com/price/list---{j}.html'
    # 请求
    resp = requests.get(url, headers=head, timeout=20)
    # print(resp.text)      # 打印源码

    # 利用etree解析网页（参考资料：https://blog.csdn.net/qq_35208583/article/details/89041912）
    html = etree.HTML(resp.text)
    # 使用xpath解析，获取到数据所在位置
    tr_list = html.xpath("/html/body/div/div[3]/div[1]/table/tr")
    tr_list = tr_list[1:]
    # 遍历，然后使用xpath解析
    for i in tr_list:
        address = i.xpath('./td[1]/div/a/text()')[0].strip()
        type = i.xpath('./td[2]/text()')[0].strip()
        price = i.xpath('./td[3]/text()')[0].strip() + ' ' + i.xpath('./td[3]/text()')[1].strip()
        peo = i.xpath('./td[4]/@title')[0]
        time = i.xpath('./td[5]/text()')[0]
        # data.append(i.xpath('./td[4]/@title')[0])
        print(address, type, price, peo, time)

        # 保存数据
        path_file_name = './data.csv'
        # 如果没有csv文件，就新建文件，并写入
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['产地', '规格', '价格', '公司', '时间'])
                writer.writerow([address, type, price, peo, time])
        # 如果有csv文件，直接追加写入
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow([address, type, price, peo, time])


# print(len(data))
