import time

import requests

for page in range(2,10):
    url=f'https://www.shixiseng.com/app/interns/search/v2' \
        '?build_time=1700226759219&page={page}&type=intern&keyword=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='
    proxy = {
        'http': 'http://127.0.0.1:7890',
        "https": "http://127.0.0.1:7890"
    }
    resp=requests.get(url,proxies=proxy).json()
    # print(resp)
    for i in resp['msg']['data']:
        # job_name
        job_name=i['name']
        degree=i['degree']
        city=i['city']
        cname=i['cname']
        industry=['industry']
        i_tags=''
        for j in i['i_tags']:
            i_tags+=j+'/'
        # 打印蓝色
        print(f'\033[1;34m【{job_name}】【{degree}】【{city}】【{cname}】【{industry}】【{i_tags}】\033[0m')
        # print(f'【{job_name}】【{degree}】【{city}】【{cname}】【{industry}】【{i_tags}】')
        time.sleep(0.3)