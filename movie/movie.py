# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/23 13:20
# @Author :yujunyu
# @Site :
# @File :movie.py
# @software: PyCharm
import requests
from bs4 import BeautifulSoup
from lxml import etree


pages =10
head={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
}
for j in range(1,pages+1):
    url="https://filmestorrents.site/page/{}/".format(pages)
    print(url)
    resp=requests.get(url,headers=head,timeout=10)

    html=etree.HTML(resp.text)
    divs=html.xpath('//*[@id="content"]/article')
    print(len(divs))
    urllist = []
    for i in divs:
        title=i.xpath('./header[1]/h2/a/text()')[0]
        movieName1=i.xpath('./div[2]/p[1]/text()')[1]
        format=i.xpath('./div[2]/p[1]/text()')[3]
        audio=i.xpath('./div[2]/p[1]/text()')[7].strip(":")
        print(audio)
        movieName = i.xpath('./div[2]/p[1]/text()')
        # print(len(movieName))
        # print(movieName)
        if len(movieName)==25:
            attribute=i.xpath('./div[2]/p[1]/text()')[12]
            time = i.xpath('./div[2]/p[1]/text()')[22]
        else:
            attribute = i.xpath('./div[2]/p[1]/text()')[13]
            time = i.xpath('./div[2]/p[1]/text()')[23]
        if attribute=='\n':
            attribute = i.xpath('./div[2]/p[1]/text()')[13]
        # print(attribute)
        year=i.xpath('./div[2]/p[1]/a[1]/text()')[0]
        imdb=i.xpath('./div[2]/p[1]/a[2]/text()')[0]
        pic=i.xpath('./div[2]/p[1]/b/img/@src')[0]

        detailUrl=i.xpath('./div[2]/p[2]/a/@href')
        if detailUrl==[]:
            detailUrl=i.xpath('./div[2]/p[3]/a/@href')
        # print(detailUrl[0])
        urllist.append(detailUrl[0])
    # print(urllist)
    # for k in urllist:
    #     resp1=requests.get(url=k,headers=head,timeout=10)
    #     # print(resp2)
    #     html1 = etree.HTML(resp1.text)
    #     detail = html1.xpath('//*[@id="content"]/article')
    #     print(len(detail))
    #     for m in detail:
    #         content=m.xpath('./div[2]/p[2]/text()')
    #         print(content)


