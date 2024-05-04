# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/28 10:32
# @Author :yujunyu
# @Site :
# @File :boss.py
# @software: PyCharm
import requests
import csv
import os

citys=['101010100','101020100','101280600','101280100','101270100','101040100',
       '101210100','101110100','101200100','101190400','101180100','101190100',
       '101030100','101250100','101281600','101210400','101280800','101220100',
       '101120200','101290100','101070100','101120100','101190200','101230200',
       '101230100','101210700','101210900','101050100','101070200','101260100',
       '101300100','101230500','101090100','101060100','101240100','101280300',
       '101191100','101210300','101190800','101190500','101100100','101090200',
       '101280700','101281700','101160100','101120900','101120600','101120500',
       '101210500']
# head1={
# #        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
# #        'cookie': 'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1654601477; __g=-; wd_guid=9cf0e681-5e9c-4422-a1c6-98493fbeceac; historyState=state; _bl_uid=m4ljn60e44jfOR7RIky89jk8pFp8; toUrl=https%3A%2F%2Fwww.zhipin.com%2F; __fid=4495ae7b6106712dbdb5084993099397; wt2=DwVYZKpqPhueUNWtusT_kPffjPqfJ7YkQ3AvMEmioOk_b2YT9UexUinnFjqJD7DuuZai7C2qPRssnpiH3FO7QGg~~; wbg=0; acw_tc=0a099d9a16589773593821863e0149342668c387c396b4dfa91f6cce5e3696; __c=1658975537; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%26city%3D101010100%26page%3D4&r=https%3A%2F%2Fwww.bing.com%2F&g=&s=3&friend_source=0&s=3&friend_source=0; __a=64454490.1654601475.1654601475.1658975537.33.2.25.33; __zp_stoken__=67beeGlMBO38OaiNzWlI2LgRtVx5%2FfScHMTA3SAFzSDF8Yj1zJhB4KDwvOGFMJT0FWi5KAz8IIn1eOkosADcIY25bdS9ibhUeOjgdYzg3IBNgSQ5SVSQ8DSI2Qy9%2FQXtOGBd4fT93SAUJYTk%3D'
# #
# # }
# #
# # resp=requests.get("https://www.zhipin.com/wapi/zppassport/get/zpToken",headers=head1).json()
# # token=resp['zpData']['token']
# # print(token)
head = {
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
       'cookie': 'wd_guid=9cf0e681-5e9c-4422-a1c6-98493fbeceac; historyState=state; _bl_uid=m4ljn60e44jfOR7RIky89jk8pFp8; lastCity=101210100; __zp_seo_uuid__=099cabb0-87fd-46fb-a642-d752d1be2379; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1659015784,1659016742,1659935320,1660382529; __zp_stoken__=6dd8eVzNpUjd5UlNcdxkSbVAeD3YsU1cHLz0jFQZtV10%2Bd15SV3ZRH2dGDX1bIjJ0NRdGIyMMK20nUyAFCG9OPj4Lc18lViwZdVs0bVsIPHA1YRA2IBJXGQs6G10tOzZWNVUcQk1MFEBqMCoiRzEICj4zez0fNmcPTz1eBg5cclU7HgxfU2ZgD3MjeBZvAgRfRH1sR3JWRg%3D%3D; toUrl=https%3A%2F%2Fwww.zhipin.com%2F; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD%26city%3D101210100&s=3&g=&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1660382653; wt2=DV66z3ufgbmd4rxOmSv21WHLJ2ZcdZvtEs59lQBxpm11io7Lw-O3j6SonAqNi3kRtemP4oJzxNQ-UnAOKU7eCjQ~~; wbg=0; __c=1660382528; __a=64454490.1654601475.1659935320.1660382528.123.10.7.123; geek_zp_token=V1RNkhGeT72l1vVtRvyR0bISiy7TrfwSU~',
       'x-requested-with': 'XMLHttpRequest',
}


query=input("请输入关键字:")

for page in range(1,11):
       print(page)
       param = {
              "scene": 1,
              "query": query,
              "city": "101210100",
              "page": page,
              "pageSize": 30
       }
       resp1 = requests.get("https://www.zhipin.com/wapi/zpgeek/search/joblist.json", headers=head, params=param).json()
       # print(resp1)
       print(len(resp1['zpData']['jobList']))
       for i in range(len(resp1['zpData']['jobList'])):
              # 名字、地址、薪资、经验、学历、技能、hr、、公司名、公司相关信息、公司福利
              job_name = resp1['zpData']['jobList'][i]['jobName']
              address = resp1['zpData']['jobList'][i]['cityName'] + '/'+resp1['zpData']['jobList'][i]['areaDistrict'] + '/'+resp1['zpData']['jobList'][i]['businessDistrict']
              salary = resp1['zpData']['jobList'][i]['salaryDesc']
              experience = resp1['zpData']['jobList'][i]['jobExperience']
              degree = resp1['zpData']['jobList'][i]['jobDegree']
              skills = []
              for skill in range(len(resp1['zpData']['jobList'][i]['skills'])):
                     skills.append(resp1['zpData']['jobList'][i]['skills'][skill])
              skills2='/'.join(skills)
              hr = resp1['zpData']['jobList'][i]['bossName'] +'/'+ resp1['zpData']['jobList'][i]['bossTitle']
              brand_name = resp1['zpData']['jobList'][i]['brandName']
              brand_details = resp1['zpData']['jobList'][i]['brandIndustry'] + '/'+resp1['zpData']['jobList'][i][
                     'brandStageName'] +'/'+ resp1['zpData']['jobList'][i]['brandScaleName']
              welfares = []
              for welfare in range(len(resp1['zpData']['jobList'][i]['welfareList'])):
                     welfares.append(resp1['zpData']['jobList'][i]['welfareList'][welfare])
              welfares2='/'.join(welfares)
              url="https://www.zhipin.com/job_detail/fe2af1bb664595dc1XRz29m_EVtX.html?lid="+resp1['zpData']['jobList'][i]['lid']+'&securityId='+resp1['zpData']['jobList'][i]['securityId']
              print(url)

              path_file_name = f'./{query}_BossData.csv'
              if not os.path.exists(path_file_name):
                     print('新建并且写入')
                     with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(
                                   ['工作名称', '地址', '薪资', '经验要求', '学历要求', '技能要求', '联系人', '公司名', '公司相关信息', '公司福利','详情页url'])
                            writer.writerow([job_name,address,salary,experience,degree,skills2,hr,brand_name,brand_details,welfares2,url])
              else:
                     with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                            print('新建完成后写入')
                            writer = csv.writer(csvfile)
                            writer.writerow([job_name,address,salary,experience,degree,skills2,hr,brand_name,brand_details,welfares2,url])