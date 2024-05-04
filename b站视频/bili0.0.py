# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/13 10:45
# @Author :yujunyu
# @Site :
# @File :bili0.0.py
# @software: PyCharm
"""
指定页视频的爬取(仅视频，无音频）
"""
from email.mime import audio
from turtledemo.minimal_hanoi import play

import requests
import re
import json
import pprint

url="https://www.bilibili.com/video/BV14q4y1W76B"

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "referer": "https://www.bilibili.com/video/BV11S4y1a7X9?spm_id_from=333.337.search-card.all.click"
}
res=requests.get(url,headers=headers)
# print(res.text)
video = re.findall('<script>window\.__playinfo__=(.*?)</script>', res.text)[0]
# print(video)
result = json.loads(video)

# pprint.pprint(result)


video_download_url = result['data']['dash']['video'][0]['backupUrl'][0]
audio_download_url = result['data']['dash']['audio'][0]['backupUrl'][0]
# print(video_download_url)
video_res = requests.get(video_download_url, headers=headers)
audio_res = requests.get(audio_download_url, headers=headers)
video_name = url.split("/")[-1]
print(video_name)
with open('' + video_name + '.mp4', mode='wb') as f:
    f.write(video_res.content)
with open('' + video_name + '.mp3', mode='wb') as f:
    f.write(audio_res.content)

