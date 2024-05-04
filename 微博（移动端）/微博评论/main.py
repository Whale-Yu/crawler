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


pages = int(input("请输入爬取的页数："))

keyword_list = [
    '胖海'
    # '小敏家'
    # '辛巴发长文爆料刘耕宏夫妇卖假货',
    # '小鹿 淘汰',
    # '我国太阳探测卫星科学数据全国共享',
    # '我国结婚年龄越来越迟',
    # 'HPV九价疫苗扩龄至9-45岁',
    # '欢乐颂4',
    # '亚洲人首次进入全球富豪前三',
    # '23岁女子上班时突发脑出血',
    # '结婚人数首次低于800万对',
    # '刘耕宏 哭了',
    # '网传章子怡赵丽颖合作双女主剧',
    # '吴磊晒plog告别星汉灿烂',
    # '戈尔巴乔夫去世',
    # '开学',
    # '六公主评苍兰诀',
    # '陕西蓝田通报老人被群嘲事件',
    # 'LV开卖乒乓球拍售价1.8万元',
    # '顾客买酸奶过期1分钟索赔1000元',
    # '台海局势',
    # '比亚迪',
    # '思文 程璐',
    # '女子坐高铁把娃装进手提袋',
    # '200斤爸爸抱6斤女儿直犯难',
    # '女孩猛推扭扭车致2岁宝宝摔落',
    # '家暴',
    # '性骚扰',
    # '大陆无人机拍摄金门岗哨',
    # '巴基斯坦 洪灾',
    # '叙利亚局势',
    # '超市员工脱袜子光脚踩冷藏牛奶',
    # '苍兰诀 细节',
    # '离职前一定要删的东西',
    # '广州地铁',
    # 'AI虚拟歌手入学上海音乐学院',
    # '乌克兰局势',
    # '重庆山火',
    # '四川洪灾',
    # '裸眼3D',
    # '恋爱脑',
    # '村BA 贵州',
    # '疫情的虚假信息',
    # '四川疫情防控',
    # '王源南京演唱会三周年',
    # 'iphone14',
    # '吴亦凡',
    # 'google'
]
# print(len(keyword_list))

for key in range(len(keyword_list)):
    # print(keyword_list[key])
    keyword = keyword_list[key]
    # keyword = input("请输入爬取的关键字：")

    # path_file_name = './{}_相关信息.csv'.format(keyword)
    path_file_name_1 = './data/{}_评论.csv'.format(keyword)

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
        # print(len(resp['data']['cards']))
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
                resp3 = requests.get('https://m.weibo.cn/statuses/extend', params=parms3, headers=head,
                                     timeout=20).json()
                content = resp3['data']['longTextContent']
                dr = re.compile(r'<[^>]+>', re.S)  # 解析text内容
                content1 = dr.sub('', content)
                # print(content1)
                # if not os.path.exists(path_file_name):
                #     print('新建并且写入')
                #     with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as f:
                #         writer = csv.writer(f)
                #         writer.writerow(['页码', '微博id',  '微博作者', '发布时间','微博内容', '微博正文url','转发数','评论数','点赞数','用户粉丝数'])
                #         writer.writerow([page, id, user, time1, content1, web_url, reposts_count, comments_count, attitudes_count,like_count])
                # else:
                #     with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as f:
                #         print('新建完成后写入')
                #         writer = csv.writer(f)
                #         writer.writerow([page, id, user, time1, content1, web_url, reposts_count, comments_count, attitudes_count,like_count])

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
                            writer.writerow(['用户id', '用户昵称', '评论时间', 'IP地址', '评论内容', '评论人粉丝数', '评论点赞数'])
                            writer.writerow(
                                [comment_id, comment_name, comment_time_1, comment_source, comment_text_1,
                                 followers_conunt,
                                 comment_like_count])
                    else:
                        with open(path_file_name_1, "a+", encoding='utf_8_sig', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(
                                [comment_id, comment_name, comment_time_1, comment_source, comment_text_1,
                                 followers_conunt,
                                 comment_like_count])

            except:
                pass
    print("爬取结束！！！")
