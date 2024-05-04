"""
微博pc端 高级搜索（方舱+原创+2022/4/1-2022/6-15）
https://s.weibo.com/weibo?q=%E6%96%B9%E8%88%B1&scope=ori&suball=1&timescope=custom:2022-04-01-0:2022-06-15-0&Refer=g&page=1
"""

import requests
from lxml import etree
import os, csv

path_file_name = '方舱-6月1111.csv'

head1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
    # 'cookie': 'SINAGLOBAL=9710946401573.262.1643976011591; UOR=www.miguvideo.com,service.weibo.com,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF5qx5FzYCvKUNG1C4SUREy5JpX5KMhUgL.FoMfSoec1hB71h52dJLoIE5LxKML1KBLBKnLxKqL1hnLBoMNSKq0SonXehn7S0q7Sntt; PC_TOKEN=4c2d96812d; ALF=1693624933; SSOLoginState=1662088934; SCF=ApabMJh2oPNunmvq6U9pk1lLsTQSNlDWN6-5PXfK_Q9YAplUL0WK8h1mo5YtFY3RxUivGgHaZvrX44B_KagXip4.; SUB=_2A25OFQa4DeRhGeFL7VEX-CrMwzyIHXVtY39wrDV8PUNbmtANLU_VkW9Nfc_ZVTX2EO753wbqCYzZWJws8QIPOxlp; _s_tentry=weibo.com; Apache=5822964900923.373.1662088957709; ULV=1662088957786:11:8:8:5822964900923.373.1662088957709:1662087025289'
    'cookie': 'UOR=cn.bing.com,weibo.com,cn.bing.com; SINAGLOBAL=923607874180.2389.1641879129769; PC_TOKEN=ff929ec4b7; SCF=Agp76rpJWVABCHE4fpDONux_ABv7wh5d9VBe0n_Yb6hNejoDqfaeeSY5oc_piRFU5B5q8gK9zVz37Sy7RNOiSeU.; XSRF-TOKEN=fzUFF6r-yBfTAPyRx2YlK80j; _s_tentry=weibo.com; Apache=1676932561427.722.1662103851568; ULV=1662103851633:7:2:3:1676932561427.722.1662103851568:1662100231819; SUB=_2A25OFcFsDeRhGeFJ41UR-SzKzz2IHXVtYrWkrDV8PUNbmtANLXjjkW9NfvrU0lSqazzKHyMV596dmZPkS21rn56e; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56yOIrp8dNgxKucoaz8idr5JpX5KzhUgL.FoMN1hM71KzcSh22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0nNeh.ESoBp; ALF=1693639867; SSOLoginState=1662103868; WBPSESS=Dt2hbAUaXfkVprjyrAZT_KvoecOqaKgJLH_vevTLGdmexi_LGCxO3x5QWky5H3prZpFbPFMrvo1038hjPC15m_FsBHKho-VGnxadD8ozJf9pjjXUK7PhOgMkJwbLJeDaCERS7e7Rtgju9F06S2S6LmIPiP4g8S_q68kmQvcVozN5Cg16YlaUoLqH43oEqh6_c5VVj89iYe6LL_UnTuFNJw=='
}
"""
改变月和日 可以获取指定某一天的数据
"""
# 月
month = 6
month = str(month).zfill(2)
# 日
day = 4
day = str(day).zfill(2)

# 限制hour
s_hour = 12
e_hour = 23
# 限制页数
page = 50
# 遍历一天的前12、后11小时
for j in range(2):
    # 遍历50页
    for i in range(1, page + 1):
        # print(i)
        url1 = f'https://s.weibo.com/weibo?q=%E6%96%B9%E8%88%B1&scope=ori&suball=1&timescope=custom:2022-{month}-{day}-{s_hour}:2022-{month}-{day}-{e_hour}&Refer=g&page={i}'
        resp1 = requests.get(url=url1, headers=head1, timeout=20)
        html = etree.HTML(resp1.text)
        divs = html.xpath('//*[@id="pl_feedlist_index"]/div[2]/div')
        print(f'第{i}页数量:{len(divs)}——正在写入')
        for div in divs:
            # 用户名
            name = div.xpath('./div/div[1]/div[2]/div[1]/div[2]/a/text()')[0]
            # 时间
            time = div.xpath('./div/div[1]/div[2]/div[2]/a[1]/text()')[0].strip()
            # print(name)
            print(time)
            # 正文
            text = div.xpath('./div/div[1]/div[2]/p/text()')
            print(text)
            text11 = ''
            for k in range(len(text)):
                text11 += text[k]
                print(text[k])
            text111 = text11.replace('\n', '').replace('\u200b', '').strip()
            if ' ' in text111:
                p1, p2, p3 = text111.partition(' ')
            else:
                p3 = text111
            main_text = p3.strip().replace('\n', '').replace('\u200b', '').replace(' ','')
            print(main_text)
            # print(text111)

            # 写入数据
            if not os.path.exists(path_file_name):
                with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['用户', '时间', '正文'])
                    writer.writerow([name, time, main_text])
            else:
                with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([name, time, main_text])
    s_hour -= 12
    e_hour -= 11
