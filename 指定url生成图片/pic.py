import pandas as pd
import requests
import os
import getpass

user_name = getpass.getuser()  # 获取计算机的用户名
dir_name = f'C:/Users/{user_name}/Desktop/img/'
data = pd.read_excel(r"C:\Users\yujunyu\Desktop\2023-2-11-15-3-13-329687896191400-桌上型电脑电源  全汉企业-采集的数据-后羿采集器.xlsx")
pic_url = data['缩略图']
pic_name = data['标题']
for i in range(len(pic_url)):
    url = pic_url[i]
    print(url)
    pic_resp = requests.get(url)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
        with open(dir_name + str(pic_name[i]) + ".jpg", mode='wb') as f:
            f.write(pic_resp.content)
        f.close()
    else:
        with open(dir_name + str(pic_name[i]) + ".jpg", mode='wb') as f:
            f.write(pic_resp.content)
        f.close()
