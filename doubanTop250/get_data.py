import requests
from lxml import etree  # 就是xpath解析用到的库
import csv
import os

# 然后现在是一页，如果多页呢？？————先去网页观察是怎么变化的——可以得出第一页从0开始，每加一页加25——那么直接使用循环既可以实现爬取多页
# 1：请求url，获取数据
# url='https://movie.douban.com/top250'
start=0
for i in range(10):
    url=f'https://movie.douban.com/top250?start={start}&filter='
    print(url)
    head={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    resp=requests.get(url,headers=head)
    # print(resp.text)

    # 2：解析数据（我一般首先xpath解析，因为最快、最方便。具体的可以去学习下）
    html=etree.HTML(resp.text)
    li_list=html.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for i in li_list:
        # 标题
        title=i.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0] # text()获取文本
        # 导演
        director=i.xpath('./div/div[2]/div[2]/p[1]/text()[1]')[0]
        # 以此类推，几乎所以页面上的都可以拿到
        # 时间+类型
        # time_type=i.xpath('./div/div[2]/div[2]/p[1]/text()')    # 有点小问题，处理下就好了，这里就不处理了
        print(title,director)
        # 其他都是类似的操作，就不演示了

        # 3:需要保存数据——直接用这个就行了，针对是保存为csv，也就是excel
        # 保存数据
        path_file_name = './douban-top250.csv'
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['标题', '导演'])
                writer.writerow([title,director])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow([title,director])

                # 基本爬虫就整个流程，所有的爬虫大致分三步，细节需要去学
    start+=25

    # 完成了！！！