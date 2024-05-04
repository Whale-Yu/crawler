import requests
from lxml import etree
import csv
import os

resp = requests.get("https://news.cctv.com/yuanchuang/VR/index.shtml")
resp.encoding = 'utf-8'
html = etree.HTML(resp.text)
VR_warm_story = html.xpath('//*[@id="SUBD1492507820680830"]/div/ul/li')
for warm_story in VR_warm_story:
    title = warm_story.xpath('./div/div[2]/h3//text()')[0]
    content = warm_story.xpath('./div/div[2]/p//text()')[0]
    print(title)
    # 保存数据
    path_file_name = './vr内容.csv'
    if not os.path.exists(path_file_name):
        print('新建并且写入')
        with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['标题','简介'])
            writer.writerow([title,content])
    else:
        with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
            print('新建完成后写入')
            writer.writerow(['标题', '简介'])
            writer.writerow([title, content])
