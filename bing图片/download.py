import pandas as pd
import requests
import os
import getpass

user_name = getpass.getuser()  # 获取计算机的用户名
dir_name = f'C:/Users/{user_name}/Desktop/img/'
data = pd.read_csv('./CG动画人脸_src.csv')
pic_url = data['src']
for i in range(len(pic_url)):
    url = pic_url[i]
    print(url)
    while True:
        try:
            pic_resp = requests.get(url)
            break
        except:
            print('重试1！！')
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
        with open(dir_name + str(i) + ".jpg", mode='wb') as f:
            f.write(pic_resp.content)
        f.close()
    else:
        with open(dir_name + str(i) + ".jpg", mode='wb') as f:
            f.write(pic_resp.content)
        f.close()
