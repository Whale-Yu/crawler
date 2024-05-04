import os
import requests
import json
import time
from fake_useragent import FakeUserAgent
from csv import writer
# from datamanage import DataManager
# import pymongo
# import lxml
# # DM = DataManager()

with open('myViewHistoryyjy.csv','w',encoding='utf-8',newline='') as f:
    csvwriter = writer(f)
    csvwriter.writerow(['标题','up主名称','视频时长','视频标签','bvid','视频封面标签','up主封面标签'])
headers = {
    "referer": "https://www.bilibili.com/account/history?spm_id_from=333.788.0.0",
    "User-Agent":FakeUserAgent().random,
    "cookie": "buvid3=E9572746-7B56-45A8-6643-D8D8D6CA802E87585infoc; b_nut=1677634887; i-wanna-go-back=-1; _uuid=B833E47F-C837-E579-1C106-C293EAA7EB4988275infoc; buvid_fp=c97e4f1bb8257c92c4d9a4aea74c298c; buvid4=A1C43FCC-51AD-B2BC-C923-6D33FD64B22E88858-023030109-VTvxRhWfju8Dnyw9yisJOw%3D%3D; header_theme_version=CLOSE; DedeUserID=615998733; DedeUserID__ckMd5=25ecfbe552c1d7b3; CURRENT_FNVAL=4048; rpdid=|(u|umkuR~)u0J'uY~~YJlYuu; b_ut=5; nostalgia_conf=-1; is-2022-channel=1; CURRENT_QUALITY=0; SESSDATA=5f90a07e%2C1693877477%2C6cb73%2A31; bili_jct=a2955a85ee76fb423d33201c8eba4d8b; PVID=3; bp_video_offset_615998733=770963659385995300; innersign=0; b_lsid=7CE9F7E9_186C5371243; home_feed_column=4"
}
url = 'https://api.bilibili.com/x/web-interface/history/cursor'
if os.path.exists('jilu.txt'):
    nextMax, nextView_at,count,sumnum = list(map(int,open('jilu.txt').read().split(' ')))
else:
    nextMax = 0
    nextView_at = 0
    count = 0
    sumnum = 0
while True:
    try:
        params = {
            "max": f"{nextMax}",
            "view_at": f"{nextView_at}", # 0 今天
            "business": "archive", #archive 视频 live 直播 article 专栏
        }
        resp = requests.get(url=url,headers=headers,params=params)
        html = json.loads(resp.text)
        nextMax, nextView_at = html['data']['cursor']['max'], html['data']['cursor']['view_at']
        if nextMax == 0 & nextView_at == 0:
            print(f'第{count}部分结束,共有{sumnum}条记录')
            break
        with open('jilu.txt','w',encoding='utf-8') as fj:
            fj.write(str(nextMax) + ' ' + str(nextView_at) + ' ' + str(count) + ' ' + str(sumnum))
        data_list = html['data']['list']
        for data in data_list:
            title = data['title'] #标题
            cover = data['cover'] #视频封面链接
            bvid = data['history']['bvid'] #bvid
            author_name = data['author_name']
            up_cover = data['author_face'] #up主封面链接
            tag_name = data['tag_name'] #视频标签
            duration = time.strftime("%H:%M:%S", time.gmtime(data['duration'])) #视频时长
            data1 = (title,cover,bvid,author_name,up_cover,tag_name,duration)
            with open('myViewHistoryyjy.csv', 'a', encoding='utf-8', newline='') as f:
                csvwriter = writer(f)
                csvwriter.writerow([title,author_name,duration,tag_name,bvid,cover,up_cover])
            # DM.save_data(data1)

            sumnum += 1

        count += 1
        print(f'已爬取第{count}部分')
    except Exception as e:
        print(f"第{count}部分有误,已爬取{sumnum}条记录")
        print(e)
        break

