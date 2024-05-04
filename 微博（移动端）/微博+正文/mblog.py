import re
import requests
import datetime
import os
import csv


def trans_time(v_str):
    GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
    timeArray = datetime.datetime.strptime(v_str, GMT_FORMAT)
    ret_time = timeArray.strftime("%Y-%m-%d %H:%M:%S")
    return ret_time


pages = int(input("请输入爬取的页数："))
keyword = input("请输入爬取的关键字：")

path_file_name = './{}_相关信息.csv'.format(keyword)
path_file_name_1 = './{}_评论信息.csv'.format(keyword)

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
}

for page in range(1, pages + 1):
    print("正在写入页数为{}".format(page))
    parm = {
        "containerid": "100103type=1&q={}".format(keyword),
        "page_type": "searchall",
        "page": page
    }
    resp = requests.get("https://m.weibo.cn/api/container/getIndex", headers=head, params=parm, timeout=20).json()
    print(resp)

    print(len(resp['data']['cards']))
    for i in range(len(resp['data']['cards'])):
        # try为了解决第一页中不规则的地方
        try:
            # 页码
            page = page
            # 微博id
            id = resp['data']['cards'][i]['card_group'][0]['mblog']['id']
            mid = resp['data']['cards'][i]['card_group'][0]['mblog']['mid']
            # 微博作者
            user = resp['data']['cards'][i]['card_group'][0]['mblog']['user']['screen_name']
            # 发布时间
            time = resp['data']['cards'][i]['card_group'][0]['mblog']['created_at']
            time1 = trans_time(time)  # 转换时间
            # 微博内容
            # content = resp['data']['cards'][i]['card_group'][0]['mblog']['text']
            # # print(content)
            # dr = re.compile(r'<[^>]+>', re.S)  # 解析text内容
            # content1 = dr.sub('', content)
            # # print(content1)
            # 微博正文url
            web_url = "https://m.weibo.cn/detail/" + id
            print(web_url)
            # print(content2)
            # 转发数
            reposts_count = (resp['data']['cards'][i]['card_group'][0]['mblog']['reposts_count'])
            # 评论数
            comments_count = resp['data']['cards'][i]['card_group'][0]['mblog']['comments_count']
            print(f'评{comments_count}')
            # 点赞数
            attitudes_count = resp['data']['cards'][i]['card_group'][0]['mblog']['attitudes_count']
            # 用户粉丝数
            like_count = resp['data']['cards'][i]['card_group'][0]['mblog']['user']['followers_count']

            parms3 = {
                'id': id
            }
            resp3 = requests.get('https://m.weibo.cn/statuses/extend', params=parms3, headers=head, timeout=20).json()
            content = resp3['data']['longTextContent']
            dr = re.compile(r'<[^>]+>', re.S)  # 解析text内容
            content1 = dr.sub('', content)
            print(content1)

            if not os.path.exists(path_file_name):
                print('新建并且写入')
                with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['页码', '微博id', '微博作者', '发布时间', '微博内容', '微博正文url', '转发数', '评论数', '点赞数', '用户粉丝数'])
                    writer.writerow(
                        [page, id, user, time1, content1, web_url, reposts_count, comments_count, attitudes_count,
                         like_count])
            else:
                with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as f:
                    print('新建完成后写入')
                    writer = csv.writer(f)
                    writer.writerow(
                        [page, id, user, time1, content1, web_url, reposts_count, comments_count, attitudes_count,
                         like_count])

            # 以下是评论的获取
            url = "https://m.weibo.cn/comments/hotflow"
            parms2 = {
                "id": id,
                "mid": mid,
                "max_id_type": 0
            }
            resp2 = requests.get(url, params=parms2, headers=head, timeout=20).json()
            print(len(resp2['data']['data']))
            for j in range(len(resp2['data']['data'])):
                # 评论内容
                comment_text = resp2['data']['data'][j]['text']
                comment_text_1 = dr.sub('', comment_text)
                print(comment_text_1)
                # 用户id
                comment_id = resp2['data']['data'][j]['id']
                # 用户昵称
                comment_name = resp2['data']['data'][j]['user']['screen_name']
                # 用户粉丝数
                followers_conunt = resp2['data']['data'][j]['user']['followers_count']
                # 评论时间
                comment_time = resp2['data']['data'][j]['created_at']
                comment_time_1 = trans_time(time)  # 转换时间
                # IP地址
                comment_source = (resp2['data']['data'][j]['source']).strip('来自')
                # 评论点赞数
                comment_like_count = resp2['data']['data'][j]['like_count']

                if not os.path.exists(path_file_name_1):
                    with open(path_file_name_1, "a+", encoding='utf_8_sig', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(
                            ['微博id(评论来自于这)', '微博标题', '正文url', '评论人id', '评论人昵称', '评论时间', 'IP地址', '评论内容', '评论人粉丝数',
                             '评论点赞数'])
                        writer.writerow(
                            [id, content1, web_url, comment_id, comment_name, comment_time_1, comment_source,
                             comment_text_1, followers_conunt, comment_like_count])
                else:
                    with open(path_file_name_1, "a+", encoding='utf_8_sig', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(
                            [id, content1, web_url, comment_id, comment_name, comment_time_1, comment_source,
                             comment_text_1, followers_conunt, comment_like_count])




        except:
            pass
print("爬取结束！！！")
