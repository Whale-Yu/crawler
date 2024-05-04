# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/11/10 8:49
# @Author :yujunyu
# @Site :
# @File :jhc_news.py
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
import os, csv

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}

# 找到all_pages
url1 = f'https://www.jhc.cn/4548/list.htm'
while True:
    try:
        resp1 = requests.get(url1, headers=head)
        break
    except:
        print('重试1')
resp1.encoding = 'utf-8'  # 处理中文乱码
html1 = etree.HTML(resp1.text)
all_pages = html1.xpath('//*[@id="wp_paging_w9"]/ul/li[3]/span[1]/em[2]/text()')[0]
print(all_pages)

for page in range(1, int(all_pages) + 1):
    print(f'正在爬取：第{page}页')
    url2 = f'https://www.jhc.cn/4548/list{page}.htm'

    resp2 = requests.get(url2, headers=head, timeout=50)
    resp2.encoding = 'utf-8'  # 处理中文乱码
    # print(resp.text)

    html2 = etree.HTML(resp2.text)
    li_list = html2.xpath('//*[@id="wp_news_w9"]/ul/li')
    # print(li_list)
    print(f'当前页记录:{len(li_list)}条')

    for i in li_list:
        # 标题
        title = i.xpath('./div[1]/span[2]/a/@title')[0]
        # 时间
        time = i.xpath('./div[2]/span/text()')[0]
        # 详情页
        # https://www.jhc.cn/2022/1109/c4548a149654/page.htm
        if 'https' in (i.xpath('./div[1]/span[2]/a/@href')[0]):  # 处理部分href直接引用微信或其他的url
            href = i.xpath('./div[1]/span[2]/a/@href')[0]
        else:
            href = 'https://www.jhc.cn' + i.xpath('./div[1]/span[2]/a/@href')[0]
        print(title, time, href)

        # 详情页细节（不包括微信引用来的）
        resp3 = requests.get(href, headers=head, timeout=50)
        resp3.encoding = 'utf-8'
        html3 = etree.HTML(resp3.text)
        # print(resp2)
        # 来源
        try:
            source = html3.xpath('/html/body/div[2]/div/div[1]/div/p/span[1]/text()')[0].strip('来源：')
        except:
            source = ''
        # 作者
        try:
            author = html3.xpath('/html/body/div[2]/div/div[1]/div/p/span[2]/text()')[0].strip('作者：')
        except:
            author = ''
        # 浏览
        try:
            read_num = html3.xpath('/html/body/div[2]/div/div[1]/div/p/span[4]/span/text()')[0]
        except:
            read_num = ''
        # print(read_num)

        # # 保存数据
        # path_file_name = './学校要闻23-3-20.csv'
        # if not os.path.exists(path_file_name):
        #     print('新建并且写入')
        #     with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
        #         writer = csv.writer(csvfile)
        #         writer.writerow(['页数', '文章链接','文章标题', '时间',  '来源', '作者', '浏览量'])
        #         writer.writerow([page, href, title, time, source,author,read_num])
        # else:
        #     with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
        #         print('新建完成后写入')
        #         writer = csv.writer(csvfile)
        #         writer.writerow([page, href, title, time, source,author,read_num])
