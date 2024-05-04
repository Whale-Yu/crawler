"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃CREATE BY SNIPER┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛

"""

import requests
from lxml import etree
import lxml
import os, csv
from bs4 import BeautifulSoup

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}


for i in range(1,36):
    print(f'第{i}页')
    url = f'http://www.kanmogu.com/price_trend_list.aspx?category_id=172&page={i}'
    resp = requests.get(url=url, headers=head, timeout=20)
    # print(resp.text)

    Soup = BeautifulSoup(resp.text, 'lxml')
    table = Soup.find("table", class_="m-table")
    trs = table.find_all("tr")[1:]
    # print(table)
    # print(trs)
    for tr in trs:
        tds = tr.find_all("td")
        # print(tds)
        name = tds[0].text  # .text 表示拿到被标签标记的内容
        type = tds[1].text
        good = tds[2].text
        market = tds[3].text
        price = tds[4].text
        time = tds[5].text
        print(name, type,good, market, price, time)
        # 保存数据
        path_file_name = './data3.csv'
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['商品名称', '种类', '鲜(干)货', '市场名称', '价格', '采集时间'])
                writer.writerow([name, type, good, market, price, time])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow([name, type, good, market, price, time])

# html = etree.HTML(resp.text)
# tr_list = html.xpath("/html/body/div[5]")
# print(tr_list)
# tr_list = tr_list[1:]
# for i in tr_list:
#     address = i.xpath('./td[1]/a/text()')[0].strip()
#     print(address)
