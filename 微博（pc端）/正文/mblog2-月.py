"""
微博pc端 高级搜索（方舱+原创+2022/4/1-2022/6-15）
    https://s.weibo.com/weibo?q=%E6%96%B9%E8%88%B1&scope=ori&suball=1&timescope=custom:2022-04-01-0:2022-06-15-0&Refer=g&page=1

实现：#  该程序只能获取某一年中的某一个月的所有数据

注意：#  没数据基本就是账号被封了（也就是cookie无效），只要自己登录新的账号，找的登陆后的cookie即可并换掉——————简而言之就是换账号（换cookie）接着爬

"""

import requests
from lxml import etree
import os, csv
import calendar  # 获取某月的天数

print('----特别说明:该程序只能获取某一年中的某一个月的所有数据，比如输入2022和6  只能获取2022年6月份的全部数据---')

# 注意cookie
head1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
    # 'cookie': 'SINAGLOBAL=9710946401573.262.1643976011591; wb_view_log=1536*8641.25; wb_view_log_7787092641=1536*8641.25; UOR=www.miguvideo.com,service.weibo.com,cn.bing.com; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; webim_unReadCount=%7B%22time%22%3A1662103821202%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D; SCF=ApabMJh2oPNunmvq6U9pk1lLsTQSNlDWN6-5PXfK_Q9Yov8b4NIAEmYq5jAExA6D0i5BmYacrPjZRM4yZPcA0SE.; XSRF-TOKEN=6cP-t0CSrIq-sdnnmDLkXvoh; PC_TOKEN=511d38491d; login_sid_t=4463030ae217e29963267ea3f37985e4; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=cn.bing.com; Apache=2954442257948.997.1662112371260; ULV=1662112371263:18:15:15:2954442257948.997.1662112371260:1662110337092; SUB=_2A25OFaLRDeRhGeFJ41UR-SzKzz2IHXVtYpMZrDV8PUNbmtAfLVLwkW9NfvrU0pa8oQgDtBTr-7lhQ1txq5nC1e33; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56yOIrp8dNgxKucoaz8idr5JpX5KzhUgL.FoMN1hM71KzcSh22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0nNeh.ESoBp; ALF=1693648384; SSOLoginState=1662112385; WBPSESS=Dt2hbAUaXfkVprjyrAZT_KvoecOqaKgJLH_vevTLGdmexi_LGCxO3x5QWky5H3prZpFbPFMrvo1038hjPC15m_FsBHKho-VGnxadD8ozJf9pjjXUK7PhOgMkJwbLJeDaDavEnZidaQRrTgdYIll1n47tyjripYqlxiklpbmIiINvEuV6bvvigjoT9aE0IX8ACeYve-i7vDZ3BScM4sNqZw==',
    # 'cookie': 'SINAGLOBAL=9710946401573.262.1643976011591; wb_view_log=1536*8641.25; wb_view_log_7787092641=1536*8641.25; UOR=www.miguvideo.com,service.weibo.com,cn.bing.com; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; webim_unReadCount=%7B%22time%22%3A1662103821202%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D; SCF=ApabMJh2oPNunmvq6U9pk1lLsTQSNlDWN6-5PXfK_Q9YEbUMgVM-DycBKvBuEQthvK3geZSBjzatwLniUjogV6Y.; XSRF-TOKEN=5mqTzOvjYEwDa7LLNEpwQtTq; PC_TOKEN=27d0b3a866; login_sid_t=ddf62f3c273b7ebe2b7ef7629900bbe8; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=weibo.com; Apache=457367295910.89984.1662116144506; ULV=1662116144510:19:16:16:457367295910.89984.1662116144506:1662112371263; SUB=_2A25OFZHmDeRhGeNG6lQZ-SvOyziIHXVtYoQurDV8PUNbmtAfLVrRkW9NS26xPHrs71MZbyRgNHAj8MYXlphm9Vte; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWOHp8SW4P9S9xTrh2V2L1e5JpX5KzhUgL.Fo-ReKqR1K-EehB2dJLoI0qLxK-LB-BLBKqLxK.L1-eLBonLxKBLB.qL122LxKBLBonL1h5LxKML1-zLBoBLxK-L1-eLBKnt; ALF=1693652278; SSOLoginState=1662116279; WBPSESS=Dt2hbAUaXfkVprjyrAZT_IYgVRXPvw4BwYONrFuFMuKhNf2Shq0mjYujUYIVpd7Op9GDyrv7ZIK6R7joZaSgcJRp4O8jP76xgfOdlPST4rOW2qJX40nD_srVAn8RbEJZt6LHHx8lxd_qkoBr-i8cXPBg_jHS4I-CxMtq0yUqWCU9vNl1sassNGRl0BAVBZaRm6PJCc0fR91Kq-t_rVfAUQ=='
    # 'cookie': 'SINAGLOBAL=9710946401573.262.1643976011591; UOR=www.miguvideo.com,service.weibo.com,cn.bing.com; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; webim_unReadCount=%7B%22time%22%3A1662103821202%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D; SCF=ApabMJh2oPNunmvq6U9pk1lLsTQSNlDWN6-5PXfK_Q9YEbUMgVM-DycBKvBuEQthvK3geZSBjzatwLniUjogV6Y.; login_sid_t=ddf62f3c273b7ebe2b7ef7629900bbe8; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=457367295910.89984.1662116144506; ULV=1662116144510:19:16:16:457367295910.89984.1662116144506:1662112371263; SUB=_2A25OFZ4IDeRhGeFJ41UR-SzKzz2IHXVtYojArDV8PUNbmtANLVPgkW9NfvrU0lUkPmZ-d8etFV12dlptl6ttHIv1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56yOIrp8dNgxKucoaz8idr5JpX5KzhUgL.FoMN1hM71KzcSh22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0nNeh.ESoBp; ALF=1693655511; SSOLoginState=1662119511'
    'cookie': 'SINAGLOBAL=9710946401573.262.1643976011591; UOR=www.miguvideo.com,service.weibo.com,cn.bing.com; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; webim_unReadCount=%7B%22time%22%3A1662103821202%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D; SCF=ApabMJh2oPNunmvq6U9pk1lLsTQSNlDWN6-5PXfK_Q9YEbUMgVM-DycBKvBuEQthvK3geZSBjzatwLniUjogV6Y.; login_sid_t=ddf62f3c273b7ebe2b7ef7629900bbe8; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=457367295910.89984.1662116144506; ULV=1662116144510:19:16:16:457367295910.89984.1662116144506:1662112371263; SUB=_2A25OFYAYDeRhGeNJ61MY8inIzj2IHXVtYvbQrDV8PUNbmtAfLWvkkW9NSB9btp6ZUgYxVrzSTw11Yv36k0F5XjeE; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFOKKNVmPSuGZvph.rwfOXH5JpX5KzhUgL.Fo-Neh24eoMXSK22dJLoI7yCdc4DdLY41Btt; ALF=1693656007; SSOLoginState=1662120008; PC_TOKEN=3bb6123011'
}
# 年
year = int(input('请输入年份(如2022年,输入数字2022):'))
# 月
month = int(input('请输入月份(如1月份,输入数字1):'))
# 日（一个月有多少天
day = calendar._monthlen(year, month)  # 某月的天数
print(f'{year}年 {month}月份一共有{day}天')

path_file_name = f'方舱-{year}-{month}.csv'

while True:
    try:
        # 遍历日
        for d in range(1, day + 1):
            print(f'日:{d}')
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
                    url1 = f'https://s.weibo.com/weibo?q=%E6%96%B9%E8%88%B1&scope=ori&suball=1&timescope=custom:{year}-{str(month).zfill(2)}-{str(d).zfill(2)}-{s_hour}:{year}-{str(month).zfill(2)}-{str(d).zfill(2)}-{e_hour}&Refer=g&page={i}'
                    while True:
                        try:
                            resp1 = requests.get(url=url1, headers=head1, timeout=20)
                            break
                        except:
                            print('重试1')
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
                        # print(text)
                        text11 = ''
                        for k in range(len(text)):
                            text11 += text[k]
                            # print(text[k])
                        text111 = text11.replace('\n', '').replace('\u200b', '').strip()
                        if ' ' in text111:
                            p1, p2, p3 = text111.partition(' ')
                        else:
                            p3 = text111
                        main_text = p3.strip().replace('\n', '').replace('\u200b', '').replace(' ', '')
                        # print(main_text)

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
        break
    except:
        print('重试2')
print('over!')
