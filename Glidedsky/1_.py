# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/22 11:06
# @Author :yujunyu
# @Site :
# @File :1_.py
# @software: PyCharm


import requests
from bs4 import BeautifulSoup

#头文件
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    #注意带上Cookie，不然会被拦截，参考图1，大家参考自己填上
    "Cookie": "footprints=eyJpdiI6InRXTzBtWlZTQzl4b3FvTklYdG1sclE9PSIsInZhbHVlIjoiVmJKYWRWY2E5SmNOdmpnQWhzV0VrWUpmUnFWWDZ1QnhkUGlCbnltUVM4Z0Q3UUJ0V2ZjMmp3eTlsMTlyXC9SN3EiLCJtYWMiOiJiOWZkMGYwZTAzMDA4OTQ5YzM3ZWEwZWMyMzk1MWE1NWYxYjAzMWNjYmViZTFiOGMzYzRkZGU1MDU5NTMwODczIn0%3D; __gads=ID=7f1cdb8891f51649-22192bab9dd40035:T=1655653983:RT=1655653983:S=ALNI_Mb0M7YWCr9RmmXTFF3JpVE8yoMgpg; _ga=GA1.2.1826316154.1655653985; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6Im11OG15T1BjbDF1K1V3TTVDWlVyQ1E9PSIsInZhbHVlIjoiMHNHT2NEWm9wZHV4ZitGZFoyNDI5d3FEYzM1RnV6XC9lNUJ0UkYzNG1UdHArVXFzVStZZ1JIdHM5Z2RJZk5SM3Q1bjNGc0h5c3c4djF2eU9UUndBVDAwXC9VbFZQWG42dUJOWVArMnRlZTd3aUMyNkZETTIzKzA5azk2YmpCSzhEQklReldGdDB0ZU9VcVA4SCtrNG12OG94dWhKVStMckVBMzZwSlpKUUx0cVE9IiwibWFjIjoiNmI5Y2Q5NjViZmQwNDViYjcxOTA5Yzc5MTE3NWYwZDNiOGRjZGZkMThlMTFkOTc3MjZkZGFmNjBhYmQ0YmY2NCJ9; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1655950506,1658369737,1658459082; _gid=GA1.2.1690510403.1658459083; __gpi=UID=000006c9e621ad0d:T=1655653983:RT=1658459082:S=ALNI_MaK5Bya9O0XUlC8zrvGTwz7219rWQ; XSRF-TOKEN=eyJpdiI6IkNCcHUxblR3TUtid0dGYWtsNFwvZWV3PT0iLCJ2YWx1ZSI6IlZJSVNzY3pDRGROVENuaWE5WjJ5NzZkSlQ5UjJMQUJIeERoU0VRcGFLTVZXMGNxK2cyeUMwMzR5T0JJY21vTDkiLCJtYWMiOiIzNWE4N2QwZTUzYTk1ZjIxNjdlZGRhMmE4NWU1ZTQzOTQ5NGI0NzU0YjJlOTlkZGY0YzI5MzZiNmY0MjhiNjI3In0%3D; glidedsky_session=eyJpdiI6IjhPak1ST2FPN01qNEFRV1E3WTUwclE9PSIsInZhbHVlIjoiQ1Q1bGx1dWJrbEhXbjdSRXBkc2UzMlN1N0pEUG1OQ3ZvTXJVMWdGYUtrajJjWldGdnczdWdLTURYXC9zTDZ2SEUiLCJtYWMiOiJmNzA4ZWQ0NmI2OTA5ODlhZWU5MTMzZDE2MzZhMTQ4OTI4OWUzZGI3M2Q1NjY2OGY3Nzk5MzdhZjUyZmYyOGE1In0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1658459611"
}
#最后的总数
sum = 0
#请求地址
url = "http://glidedsky.com/level/web/crawler-basic-1"
response = requests.get(url=url,headers=headers)

#使用 BeautifulSoup 解析
data = BeautifulSoup(response.text,"lxml")

#参考图2，获取全部数字，遍历
div_list = data.find_all(class_="col-md-1")
for div in div_list:
    d = BeautifulSoup(str(div),"lxml")
    sum += int(d.text.strip())

print(sum)


