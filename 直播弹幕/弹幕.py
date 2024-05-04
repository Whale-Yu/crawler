import requests
url = 'https://v.douyu.com/wgapi/vod/center/getBarrageList?vid=Bjq4MeYNqLxM5Ea8&start_time=0&end_time=-1'
while True:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    html_data = response.json()
    next_time = html_data['data']['end_time']
    lis = html_data['data']['list']
    for li in lis:
        barrage = li['ctt']
        with open('dy弹幕.txt', mode='a', encoding='utf-8') as f:
            f.write(barrage)
            f.write('\n')
            print(barrage)
    url = f'https://v.douyu.com/wgapi/vod/center/getBarrageList?vid=Bjq4MeYNqLxM5Ea8&start_time={next_time}&end_time=-1'
    if next_time == -1:
        break