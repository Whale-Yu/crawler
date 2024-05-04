# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/8/15 18:08
# @Author :yujunyu
# @Site :
# @File :baozhangge.py
# @software: PyCharm

import requests

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71",
}
params1 = {
    'callback': 'jQuery33109623292487819202_1660559706096',
    'act': 'recommd_by_role',
    'search_type': 'role',
    'count': 15,
    'view_loc': 'search_cond',
    'change_sch_list_logic': 'and',
    'change_icon_list_logic': 'and',
    'summon_skill_logic': 'and',
    'shen_shou_logic': 'and',
    'ling_shou_logic': 'and',
    'zhen_shou_logic': 'and',
    'mount_list_logic': 'and',
    'equip_special_skill_logic': 'and',
    'equip_special_effect_logic': 'and',
    'fashion_list_logic': 'and',
    'own_sch_fabaos_logic': 'or',
    'own_fabaos_logic': 'or',
    'order_by': '',
    'page': 1,
    'page_session_id': '0182A112-254B-1111-23E9-845DD11D5177',
    '_': '1660559706097'
}
# 1 (报错
# resp1 = requests.get("https://my.cbg.163.com/cgi-bin/recommend.py", headers=head,params=params1,timeout=20).json()
# print(resp1)

# 2（可行
resp1 = requests.get("https://my.cbg.163.com/cgi-bin/recommend.py", headers=head,params=params1,timeout=20)
print(resp1.status_code)
print(resp1.text)
