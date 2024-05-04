import requests
from lxml import etree
from urllib.parse import quote
import os
import csv

url="http://www.youxige.com/showkinds.aspx"

head={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
}
# 获取全部类型的游戏
resp=requests.get(url,headers=head,timeout=20)
html=etree.HTML(resp.text)
li_list=html.xpath("/html/body/div[3]/div/div/ul[2]/li")
# print(len(lis))
for ls in li_list:
    game_name=ls.xpath('./a/p[2]/text()')[0]
    print(game_name)
    new_url="http://www.youxige.com"+ls.xpath('./a/@href')[0]
    # print(new_url)
    resp2=requests.get(new_url,headers=head,timeout=20)
    html2=etree.HTML(resp2.text)
    pages_div=(html2.xpath('/html/body/div[5]/div/div[3]/div/div'))[-1]
    try:
        pages=pages_div.xpath('./div/a[3]/text()')[0]
    except:
        pages=1
    print(pages)
    for page in range(1,int(pages)+1):
        # "http://www.youxige.com/ysgoods_list.aspx?2022072409&category_id=0&page=3"
        all_url="http://www.youxige.com"+ls.xpath('./a/@href')[0]+"&category_id=0&page={}".format(page)
        print(all_url)

        resp1 = requests.get(all_url,headers=head,timeout=20)
        html1 = etree.HTML(resp1.text)
        divs = (html1.xpath('/html/body/div[5]/div/div[3]/div/div'))[:-1]
        print(len(divs))
        for i in divs:
            # 标题
            title=i.xpath('./a[1]/div[2]/div[1]/p/text()')[0].strip()
            print(title)
            # 详情网址
            detail_url='http://www.youxige.com/'+i.xpath('./a[1]/@href')[0]
            print(detail_url)
            # 封面图片
            pic_url='http://www.youxige.com'+quote(i.xpath('./a[1]/div[1]/img/@src')[0])    # 解决url中出现的中文
            # 商品编号
            id=i.xpath('./a[1]/div[2]/div[2]/p/text()')[0]
            # 区服
            try:
                area = i.xpath('./a[1]/div[2]/div[3]/p[1]/text()')[0]
            except:
                area=""
            # 浏览数
            try:
                view_count = i.xpath('./a[1]/div[2]/div[3]/p[2]/text()')[0]
            except:
                view_count = i.xpath('./a[1]/div[2]/div[4]/p/text()')
            # 价格
            price=i.xpath('./a[1]/div[3]/p/text()')[0]

            path_file_name = './gameData.csv'
            if not os.path.exists(path_file_name):
                print('新建并且写入')
                with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['页数', '游戏名', '标题', '商品编号', '区服', '浏览数', '价格', '游戏详情url', '封面图片'])
                    writer.writerow([page, game_name, title, id, area, view_count, price,  detail_url, pic_url])
            else:
                with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                    print('新建完成后写入')
                    writer = csv.writer(csvfile)
                    writer.writerow([page, game_name, title, id, area, view_count, price,  detail_url, pic_url])