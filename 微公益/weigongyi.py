
import requests
import math
import os
import csv

head={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
    # "cookie":'UOR=cn.bing.com,weibo.com,cn.bing.com; SINAGLOBAL=923607874180.2389.1641879129769; SUB=_2A25P3kqVDeRhGeNG6lQZ-SvOyziIHXVtIVbdrDV8PUJbkNAKLRH9kW1NS26xPAOftQCtH5uwgpmVuMpH6qAB_yxZ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWOHp8SW4P9S9xTrh2V2L1e5NHD95Qf1h2c1h.feo5XWs4Dqcjci--fi-82i-2ci--4iKLhi-zRi--Xi-isiKyWi--Xi-zRiKn7i--NiKLFi-zXi--fiKLhi-2R; UPSTREAM-GONGYI=ecafb827affab61986c56a3aebc5fe0d; _s_tentry=-; Apache=7457821730055.447.1658634558140; ULV=1658634558193:4:3:2:7457821730055.447.1658634558140:1658632557038; PC_TOKEN=9db4582182; WBStorage=4d96c54e|undefined',
    "referer": "https://gongyi.weibo.com/r/226485"
}

parms ={
        "pageSize": 10,
        "page": 1,
        "regular_id": 226485
    }
# 找到页数
resp=requests.get("https://gongyi.weibo.com/aj_regular_getdonatelist",headers=head,params=parms).json()
pages= math.ceil((resp['data']['total']) // 10)
# print(total_num)
# 遍历每一页
for page in range(1,pages+1):
    print("当前页数为{}".format(page))
    parms = {
        "pageSize": 10,
        "page": page,
        "regular_id": 226485
    }
    resp=requests.get("https://gongyi.weibo.com/aj_regular_getdonatelist",headers=head,params=parms).json()
    # print(resp.status_code)
    # print(resp)
    data_list=resp['data']['donate_list']
    # print(len(data_list))
    for data in range(len(data_list)):
        id=resp['data']['donate_list'][data]['id']
        nickname=resp['data']['donate_list'][data]['screen_name']
        money=resp['data']['donate_list'][data]['money']
        time=resp['data']['donate_list'][data]['ctime']
        comment=resp['data']['donate_list'][data]['msg']
        print(comment)
        # 保存数据
        path_file_name = './微公益Data.csv'
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['id', '昵称', '捐款金额/元', '时间', '评论内容'])
                writer.writerow([id, nickname, money, time, comment])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow([id, nickname, money, time, comment])



