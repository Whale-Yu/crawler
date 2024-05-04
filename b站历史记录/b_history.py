# -*- codeing = utf-8 -*-
# @Time :2023/3/6 11:06
# @Author :yujunyu
# @Site :
# @File :b_history.py
# @software: PyCharm

# 导入库
import requests
import json
import os
import csv
import time

headers = {
    'cookie': "buvid3=E9572746-7B56-45A8-6643-D8D8D6CA802E87585infoc; b_nut=1677634887; i-wanna-go-back=-1; _uuid=B833E47F-C837-E579-1C106-C293EAA7EB4988275infoc; buvid_fp=c97e4f1bb8257c92c4d9a4aea74c298c; buvid4=A1C43FCC-51AD-B2BC-C923-6D33FD64B22E88858-023030109-VTvxRhWfju8Dnyw9yisJOw%3D%3D; header_theme_version=CLOSE; DedeUserID=615998733; DedeUserID__ckMd5=25ecfbe552c1d7b3; CURRENT_FNVAL=4048; rpdid=|(u|umkuR~)u0J'uY~~YJlYuu; b_ut=5; nostalgia_conf=-1; is-2022-channel=1; CURRENT_QUALITY=0; SESSDATA=5f90a07e%2C1693877477%2C6cb73%2A31; bili_jct=a2955a85ee76fb423d33201c8eba4d8b; bp_video_offset_615998733=770963659385995300; innersign=0; b_lsid=94156F4D_186C5389C7D; home_feed_column=5; LIVE_BUVID=AUTO6116783465412799; _dfcaptcha=bd001afe5eb75e2d6764248adaeb3f74; PVID=2",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# url1 = 'https://api.bilibili.com/x/web-interface/history/cursor?max=0&view_at=0&business='


max = 0
view_at = 0
business = ''
while True:
    url1 = f'https://api.bilibili.com/x/web-interface/history/cursor?max={max}&view_at={view_at}&business={business}'

    # 获取响应信息
    resp1 = requests.get(url=url1, headers=headers, timeout=4)
    resp1 = json.loads(resp1.text)
    # print(resp1)

    # 获取三个参数值
    max = resp1['data']['cursor']['max']
    view_at = resp1['data']['cursor']['view_at']
    business = resp1['data']['cursor']['business']
    print(max, view_at, business)  # 14625145 1676937897 archive
    print('-' * 150)
    if max == 0:
        break

    # 遍历list
    for i in range(len(resp1['data']['list'])):
        title = resp1['data']['list'][i]['title']
        author_name = resp1['data']['list'][i]['author_name']
        duration = resp1['data']['list'][i]['duration']

        if resp1['data']['list'][i]['history']['bvid'] == '':
            url = None
        else:
            url = "https://www.bilibili.com/video/" + f"{resp1['data']['list'][i]['history']['bvid']}"
        print(title, author_name, url)

        path_file_name = 'outputs/data1.csv'
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['title', 'author_name', 'url'])
                writer.writerow([title, author_name, url])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow([title, author_name, url])
