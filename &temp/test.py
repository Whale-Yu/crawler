# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author:suifeng
# import requests
# import execjs
# import re
# # word = input()
# head = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#     'Referer': 'https://fanyi.baidu.com/',
#     'Host': 'fanyi.baidu.com',
#     'Cookie': 'BAIDUID=932C78DC1026815A7C1A25A0B86ACE7C:FG=1; BAIDUID_BFESS=932C78DC1026815A7C1A25A0B86ACE7C:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1663805059; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1663805059; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_MDllZjlhOTllOTU2MDYyM2Y3OWZiZjZiNDI3NDE5NzY4NjcyMWVmYTE2NDhmZWE0NDc1OTk2NDMyMDZiODljNzBhZDhhMjljYzQ5YjYzYTQyZGY4M2YwY2IxYjIzOTE0OGFiMDE3YzNiMjI4ZTRiMWI3MTdmMGU5NGI2NTEzZGNiMGE5NzQ2M2EzMGI1NzYyNGZjODI3OTM3ZmJlODc1Mg=='
# }
# resp = requests.get('https://fanyi.baidu.com/',headers=head,timeout=10)
# print(resp.text)
# head.update({'cookie':f"BAIDUID={resp.cookies['BAIDUID']}"})
# token = re.search(r"token:'(.*?)',",resp.text).group(1)
# print(token)
# # b = execjs.compile(open(r'baidu.js').read())
# # sign = b.call('a',f'{word}')
# # data = {
# #     'from': 'zh',
# #     'to': 'en',
# #     'query': f'{word}',
# #     'transtype': 'translang',
# #     'simple_means_flag': 3,
# #     'sign': f'{sign}',
# #     'token': f'{token}',
# #     'domain': 'common'
# # }
# # headers = {
# #     'Referer': 'https://fanyi.baidu.com/',
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
# #     'X-Requested-With': 'XMLHttpRequest',
# #     'Host': 'fanyi.baidu.com',
# #     'Origin': 'https://fanyi.baidu.com',
# # }
# # resp = requests.post('https://fanyi.baidu.com/v2transapi?from=zh&to=en',headers=headers,data=data)
# # print(resp.json())

#
# import requests
#
# resp = requests.get('https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=0&limit=20&strategy=1&ext={%22pool%22:[%22top%22,%22hot%22],%22is_filter%22:7,%22check_type%22:true}').json()
#
#
# print(resp['data'])

# import math  #引入math函数库
# comp=int(input("请随机输入一个数"))
# if comp>=90:
#    print("grade:优秀")
# elif comp>=75 and comp<90:
#    print("grade:良好")
# elif comp>=60 and comp<75:
#     print("grade:合格")
# else:
#     print("grade:不合格")
import requests

url='https://cdn.pixabay.com/photo/2018/04/26/17/34/poppy-3352517_640.jpg'
resp=requests.get(url)
print(resp)