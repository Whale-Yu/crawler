import re
import requests
import datetime
import os
import csv
import pandas as pd

def trans_time(v_str):
    GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
    timeArray = datetime.datetime.strptime(v_str, GMT_FORMAT)
    ret_time = timeArray.strftime("%Y-%m-%d %H:%M:%S")
    return ret_time

pages=int(input("请输入爬取的页数："))
keyword=input("请输入爬取的关键字：")

path_file_name = './{}_相关信息.csv'.format(keyword)

head={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
}

for page in range(1,pages+1):
    print("正在写入页数为{}".format(page))
    parm={
        "containerid": "100103type=1&q={}".format(keyword),
        "page_type": "searchall",
        "page": page
    }
    resp = requests.get("https://m.weibo.cn/api/container/getIndex", headers=head, params=parm, timeout=20).json()
    # print(len(resp['data']['cards']))
    for i in range(len(resp['data']['cards'])):
        # try为了解决第一页中不规则的地方
        try:
            # 页码
            page = page
            # 微博id
            id = resp['data']['cards'][i]['card_group'][0]['mblog']['id']
            # 微博作者
            user = resp['data']['cards'][i]['card_group'][0]['mblog']['user']['screen_name']
            # 发布时间
            time = resp['data']['cards'][i]['card_group'][0]['mblog']['created_at']
            time1 = trans_time(time)  # 转换时间
            # 微博内容
            content = resp['data']['cards'][i]['card_group'][0]['mblog']['text']
            # print(content)
            dr = re.compile(r'<[^>]+>', re.S)  # 解析text内容
            content1 = dr.sub('', content)
            print(content1)
            # 微博正文url
            web_url = "https://m.weibo.cn/detail/" + id
            print(web_url)
            # print(content2)
            # 转发数
            reposts_count = (resp['data']['cards'][i]['card_group'][0]['mblog']['reposts_count'])
            # 评论数
            comments_count = resp['data']['cards'][i]['card_group'][0]['mblog']['comments_count']
            # 点赞数
            attitudes_count = resp['data']['cards'][i]['card_group'][0]['mblog']['attitudes_count']


            if not os.path.exists(path_file_name):
                print('新建并且写入')
                with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['页码', '微博id',  '微博作者', '发布时间','微博内容', '微博正文url','转发数','评论数','点赞数'])
                    writer.writerow([page, id, user, time1, content1, web_url, reposts_count, comments_count, attitudes_count])
            else:
                with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as f:
                    print('新建完成后写入')
                    writer = csv.writer(f)
                    writer.writerow([page, id, user, time1, content1, web_url, reposts_count, comments_count, attitudes_count])
        except:
            pass
print("爬取结束！！！")

# 去重
# df = pd.read_csv(path_file_name)
# df.drop_duplicates(subset=['微博id'], inplace=True, keep='first')
# df.to_csv(path_file_name, index=False, encoding='utf_8_sig')



