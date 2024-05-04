
import requests
import csv

import re
num = 0
for i in range(10):
    url = f"https://movie.douban.com/top250/?start={num}&filter="
    num += 25
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
    }
    resp = requests.get(url,headers=headers)
    page_content = resp.text
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">'
                     r'.*?<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                     r'<span>(?P<num>.*?)人评价</span>',re.S)
    result = obj.finditer(page_content)
    resp.close()
    f = open("data.csv",mode='a+',encoding='utf-8')
    csvwriter = csv.writer(f)
    for it in result:
    # print(it.group("name"))
    # print(it.group("score"))
    # print(it.group("year").strip())
    # print(it.group("num"))
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
    f.close()
print("over")