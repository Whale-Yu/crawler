# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/9/6 21:35
# @Author :yujunyu
# @Site :
# @File :美团.py
# @software: PyCharm

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
import csv,os
head={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
    'Cookie': '__mta=188134935.1662471272271.1662471373661.1662472102592.4; _lxsdk_cuid=18311cf55c7c8-047e166b6a79a5-26021a51-144000-18311cf55c7c8; mtcdn=K; lt=0b2ZGzo8lSyKO-AQchJqBlkS7R4AAAAAxhMAABJ5kbZ4FwFubAcGIawMO7i5BL5Obs3l1SIG3we6zdvawOpwC89RkBu4bVjXATiBqA; u=2956586420; n=IFe785281749; token2=0b2ZGzo8lSyKO-AQchJqBlkS7R4AAAAAxhMAABJ5kbZ4FwFubAcGIawMO7i5BL5Obs3l1SIG3we6zdvawOpwC89RkBu4bVjXATiBqA; unc=IFe785281749; ci=59; rvct=59; __mta=188134935.1662471272271.1662471272271.1662471272271.1; IJSESSIONID=node0123ea9bgmmb661q3qm5x43qh86175936278; iuuid=C7F7979DD6DBF607CBE1CF98A8B24DCBC40C6B13712DFDBB8D8572F90C1623AB; isid=0b2ZGzo8lSyKO-AQchJqBlkS7R4AAAAAxhMAABJ5kbZ4FwFubAcGIawMO7i5BL5Obs3l1SIG3we6zdvawOpwC89RkBu4bVjXATiBqA; oops=0b2ZGzo8lSyKO-AQchJqBlkS7R4AAAAAxhMAABJ5kbZ4FwFubAcGIawMO7i5BL5Obs3l1SIG3we6zdvawOpwC89RkBu4bVjXATiBqA; mt_c_token=0b2ZGzo8lSyKO-AQchJqBlkS7R4AAAAAxhMAABJ5kbZ4FwFubAcGIawMO7i5BL5Obs3l1SIG3we6zdvawOpwC89RkBu4bVjXATiBqA; logintype=normal; cityname=%E6%88%90%E9%83%BD; _lxsdk=C7F7979DD6DBF607CBE1CF98A8B24DCBC40C6B13712DFDBB8D8572F90C1623AB; webp=1; __utma=74597006.1719390922.1662471811.1662471811.1662471811.1; __utmc=74597006; __utmz=74597006.1662471811.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; latlng=29.062536,119.631279,1662471811049; idau=1; ci3=1; _hc.v=92039f28-f7bc-6b49-565c-575bbc59a6a1.1662471850; i_extend=C_b0E244242949693730004617997155212830616546_e457395092761097213_v6268586482535154557_a%e8%b6%85%e5%b8%82GimthomepagesearchH__a100002__b1; __utmb=74597006.17.9.1662472001994; cssVersion=c3497ddf; wm_order_channel=default; request_source=openh5; au_trace_key_net=default; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; openh5_uuid=C7F7979DD6DBF607CBE1CF98A8B24DCBC40C6B13712DFDBB8D8572F90C1623AB; uuid=C7F7979DD6DBF607CBE1CF98A8B24DCBC40C6B13712DFDBB8D8572F90C1623AB; isIframe=false; WEBDFPID=xz338yu5u12850xu16v0w9710v722wzw816869v865x979586x3u1v77-1662558433981-1662472033483GOQOGGAfd79fef3d01d5e9aadc18ccd4d0c95078437; firstTime=1662472099206; _lxsdk_s=1831300fc8f-16f-b9e-0b6%7C%7C140'
}

url='https://cd.meituan.com/s/%E8%B6%85%E5%B8%82/'

resp=requests.get(url,headers=head,timeout=20)
# print(resp.text)

html = etree.HTML(resp.text)
lis = html.xpath('//*[@id="react"]/div/div/div[2]/div[1]/div[2]/div[2]/div')
print(len(lis))
for i in lis:
    url1 ='https:' +i.xpath('./div[1]/div[1]/a/@href')[0]
    name=i.xpath('./div[1]/div[1]/div[1]/div[1]/a/text()')[0]
    score=i.xpath('./div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/text()')[0]\
          +i.xpath('./div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/text()')[1]
    try:
        price=i.xpath('./div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span/text()')[0]\
              +i.xpath('./div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span/text()')[1]
    except:
        price = i.xpath('./div[1]/div[1]/div[1]/div[1]/div[3]/div/text()')[0]
    # print(price)
    # print(score)
    print(name)
    print(url1)
    resp1=requests.get(url1,headers=head,timeout=20)
    # print(resp1.status_code)
    html1=etree.HTML(resp1.text)
    address=html1.xpath('//*[@id="react"]/div/div/div[2]/div[1]/div[2]/div[1]/a/span/text()')[0]
    # print(address)

    path_file_name = './data.csv'
    if not os.path.exists(path_file_name):
        print('新建并且写入')
        with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['店名','地址','评分','人均价格','详情url'])
            writer.writerow([name,address,score,price,url1])
    else:
        with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
            print('新建完成后写入')
            writer = csv.writer(csvfile)
            writer.writerow([name,address,score,price,url1])

