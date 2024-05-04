# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/23 10:23
# @Author :yujunyu
# @Site :
# @File :wishData.py
# @software: PyCharm

"""
一个纠结的昵称:
https://www.wish.com/?source_feed_page_view_id=1658541396_808ba62351ab4dc5b86c72f327eb321d_FeedPage

一个纠结的昵称:
cyn76897@163.com
Dq112233..

"""

import requests
import os
import csv

path_file_name = './wishData.csv'
proxy = {
    "https": "http://127.0.0.1:10809"
}
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
    'cookie': 'visitor_id=5e38ad66ed094e629002e4a64c79f771; _gcl_au=1.1.1250585480.1658542523; notice_gdpr_prefs=0,1,2:; notice_poptime=1656720000000; notice_preferences=2:; cmapi_cookie_privacy=permit 1,2,3; cmapi_gtm_bl=; __stripe_mid=7e263c56-eac5-4dec-969c-c63986b99645471387; G_ENABLED_IDPS=google; authentication_id=1c1277bc01bb5b20e75ba0c3f9f1db75; _dcmn_p=u0QkY2lkPVA2enl4bUxiWnN4SXZsVXBBUkk; _dcmn_p=u0QkY2lkPVA2enl4bUxiWnN4SXZsVXBBUkk; rskxRunCookie=0; rCookie=d5cajgezs9thkb8yxm326fl5xbdzjm; lastRskxRun=1658552692948; logged_out_locale=en; notice_behavior=expressed,eu; IR_gbd=wish.com; __stripe_sid=e969d880-b94f-4d38-8adf-2faa795b5a437cccf9; IR_12396=1658969346611%7C0%7C1658969346611%7C%7C; IR_PI=a6ca800c-0587-3a00-b864-3ee5c16ded47%7C1659055746611; _xsrf=2|28f0cb19|505ce5787b2a32874bebf6aace37e1b9|1658970708; bsid=2579227375aa471abfd81a5dd3a768cc; _is_desktop=true; _timezone=8; sessionRefreshed_62e1e25453aa9505de48b149=true; vendor_user_tracker=91c23710d639c9ac8f6994db41eb21e91f21c8f5dce0bf4e95f480d1dab6d617; sweeper_uuid=bcab747d3fdb436c9383742a35ea6eca; sweeper_session="2|1:0|10:1658971254|15:sweeper_session|84:OGMxY2E2MDktZjYyYS00ZGM1LWE0YmItMTBlYWQ3ZTFlOWMwMjAyMi0wNy0yOCAwMToyMDo1MS41MjY2NDk=|cb8cb05e661f64d4ac580952ecb91da1fa536cf9d963d91c91a0626e57d1cebe"; sessionRefreshed_5c204839abe5f15fdc4ca1c2=true; number_of_product_per_row=3; _dd_s=rum=2&id=f4279499-5a8f-4f15-bd87-529a9e8b60aa&created=1658970711619&expire=1658972183436',
    'x-xsrftoken': '2|28f0cb19|505ce5787b2a32874bebf6aace37e1b9|1658970708'
}
page = int(input("请输入页数:"))
offsets = 16 + 30 * (page - 1)
offset = 16
for j in range(16, offsets + 1, 30):
    data = {
        "count": 30,
        "offset": j,
        "request_categories": "false",
        "request_id": "tabbed_feed_latest",
        "request_branded_filter": "false"
    }
    resp = requests.post("https://www.wish.com/api/feed/get-filtered-feed", headers=head, data=data, proxies=proxy).json()
    print(len(resp['data']['products']))
    for i in range(len(resp['data']['products'])):
        pro_name = (resp['data']['products'][i]['name']).strip()
        try:
            pro_url = resp['data']['products'][i]['product_url']
        except:
            pro_url = ""
        try:
            pro_price = resp['data']['products'][i]['commerce_product_info']['logging_fields']['log_local_price']
        except:
            pro_price = ""
        try:
            pro_sell = resp['data']['products'][i]['commerce_product_info']['logging_fields']['log_feed_tile_text']
        except:
            pro_sell = ""
        print(pro_url)
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['商品名', '商品价格/$', '销量', '商品详情url'])
                writer.writerow([pro_name, pro_price, pro_sell, pro_url])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow([pro_name, pro_price, pro_sell, pro_url])
