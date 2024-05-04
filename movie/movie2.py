# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/23 13:20
# @Author :yujunyu
# @Site :
# @File :movie.py
# @software: PyCharm

"""
标题名	影片名	格式	音频	属性	年份	时长	IMDB值	简介	影片海报	影片下载地址
Movie Name	Título	Formato	Áudio	Gênero	Ano de Lançamento	Duração	IMDb	SINOPSE	PIC URL	Download Torrent
O Último Dragão Torrent (2022) Dual Áudio / Dublado WEB-DL 1080p – Download	O Ultimo Dragao	MKV	Português	Ação,Fantasia	2022	1h 38 Min.		Quando uma força malévola toma conta dos reinos de Agonos, um cavaleiro solitário deve embarcar numa perigosa busca para encontrar o último dragão e salvar o mundo deste grande e crescente mal.	https://filmestorrents.site/wp-content/uploads/2022/07/O-Ultimo-Dragao-filmestorrents-net.jpg	下载地址URL

"""
import requests
from lxml import etree
import os
import csv

pages =1000
head={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
}
for j in range(1,pages+1):
    print("当前写入页数为：{}".format(j))
    url="https://filmestorrents.site/page/{}/".format(j)
    print(url)
    resp=requests.get(url,headers=head,timeout=20)
    html=etree.HTML(resp.text)
    divs=html.xpath('//*[@id="content"]/article')
    print(len(divs))
    detail_url_list = []
    # 得到详情页的url
    for i in divs:
        try:
            detailUrl=i.xpath('./div[2]/p[2]/a/@href')
            if detailUrl==[]:
                detailUrl=i.xpath('./div[2]/p[3]/a/@href')
            # print(detailUrl[0])
            detail_url_list .append(detailUrl[0])
        except:
            pass
    # print(urllist)
    # 遍历各个详情页
    for k in detail_url_list :
        resp1= requests.get(url=k, headers=head, timeout=20)
        # print(resp1)
        html1 = etree.HTML(resp1.text)
        detail = html1.xpath('//*[@id="content"]/article')
        for m in detail:
            try:
                # 标题名
                title = m.xpath('./header[1]/h1/a/text()')[0].strip()
                print(title)
                # 影片名
                movieName1 = m.xpath('./div[2]/p[1]/text()')[1].strip()
                # 格式
                format = m.xpath('./div[2]/p[1]/text()')[3].strip()
                # 音频
                audio = m.xpath('./div[2]/p[1]/text()')[7].strip().strip(': ')
                # 年份
                year = m.xpath('./div[2]/p[1]/a[1]/text()')[0].strip()
                # imdb值
                imdb = m.xpath('./div[2]/p[1]/a[2]/text()')[0].strip()
                # 影片海报
                pic = m.xpath('./div[2]/p[1]/b/img/@src')[0]

                # 时长、属性
                movieName = m.xpath('./div[2]/p[1]/text()')
                # print(len(movieName))
                # print(movieName)
                if len(movieName) == 25:
                    attribute = m.xpath('./div[2]/p[1]/text()')[12].strip()
                    time = m.xpath('./div[2]/p[1]/text()')[22].strip()
                else:
                    attribute = m.xpath('./div[2]/p[1]/text()')[13].strip()
                    time = m.xpath('./div[2]/p[1]/text()')[23].strip()
                if attribute == '\n':
                    attribute = m.xpath('./div[2]/p[1]/text()')[13]

                # 简介
                content = m.xpath('./div[2]/p[2]/text()')
                if content == [':']:  # 处理内容为[':']
                    content = m.xpath('./div[2]/p[3]/text()')[0]
                elif content == []:  # 处理内容空
                    content = m.xpath('./div[2]/p[3]/text()')[0]
                elif len(content) > 1:  # 处理内容前面多余的，保留最后的简介
                    content = content[-1]
                else:
                    content = m.xpath('./div[2]/p[2]/text()')[0]
                # print("________________________________________________________________")
                # print(content)

                # 影片下载地址
                downloadUrl = m.xpath('./div[2]/div/p[2]/a/@href')
                if downloadUrl == []:
                    downloadUrl = m.xpath('./div[2]/div[1]/div[1]/div[2]/a/@href')
                elif downloadUrl == []:
                    downloadUrl = m.xpath('./div[2]/div[1]/div[1]/div/p/a/@href')
                # print(len(downloadUrl))
                # print(downloadUrl)
                # print("________________________________________________________________")

                path_file_name = './movieData.csv'
                if not os.path.exists(path_file_name):
                    print('新建并且写入')
                    with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(
                            ['标题名', '影片名', '格式', '音频', '属性', '年份', '时长', 'IMDB值', '简介', '影片海报', '影片下载web_url',
                             '影片下载url之一'])
                        writer.writerow([title, movieName1, format, audio, attribute, year, time, imdb, content, pic, k,
                                         downloadUrl[0]])
                else:
                    with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                        print('新建完成后写入')
                        writer = csv.writer(csvfile)
                        writer.writerow([title, movieName1, format, audio, attribute, year, time, imdb, content, pic, k,
                                         downloadUrl[0]])

            except:
                pass














