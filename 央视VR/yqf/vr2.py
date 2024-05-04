import requests
from lxml import etree
import csv
import os

path_file_name = './vr内容2.csv'
csvfile = open(path_file_name, "w", encoding='utf_8_sig', newline='')
writer = csv.writer(csvfile)
writer.writerow(['报道链接', '报道标题', '报道引言', '报道形式', '报道封面图片'])
main_url = 'https://news.cctv.com/yuanchuang/VR/index.shtml'
resp = requests.get(main_url)
resp.encoding = 'utf-8'
html = etree.HTML(resp.text)
VR_warm_story = html.xpath('//*[@id="SUBD1492566934252980"]/div/ul/li')
for warm_story in VR_warm_story:
    img_url = 'https://' + str(warm_story.xpath('./div/div[1]/div[2]/img/@src')[0])
    print(img_url)
    url = warm_story.xpath('./div/div[1]/div[1]/a/@href')[0]
    title = warm_story.xpath('./div/div[2]/h3//text()')[0]
    content = warm_story.xpath('./div/div[2]/p//text()')[0]
    if not os.path.exists(path_file_name):
        print('新建并且写入')
        if not url.split('.')[-1] == 'html':
            geshi = '视频'
        else:
            geshi = '图片'
        writer.writerow([url, title, content, geshi,img_url])
    else:
        if not url.split('.')[-1] == 'html':
            geshi = '视频'
        else:
            geshi = '图片'
        writer.writerow([url, title, content, geshi,img_url])

csvfile.close()
