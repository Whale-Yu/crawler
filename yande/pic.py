
import requests
import os
import getpass
import pandas as pd


user_name=getpass.getuser()     # 获取计算机的用户名
dir_name = f'C:/Users/{user_name}/Desktop/img/'
data = pd.read_excel('pic_url.xlsx')
pic_url = data['url']
print(len(pic_url))
# pic_name = data['标题']
# for i in range(len(pic_url)):
#     url=pic_url[i]
#     print(url)
    # pic_resp = requests.get(url)
    # if not os.path.isdir(dir_name):
    #     os.makedirs(dir_name)
    #     with open(dir_name + str(pic_name[i]) + ".jpg", mode='wb') as f:
    #         f.write(pic_resp.content)
    #     f.close()
    # else:
    #     with open(dir_name + str(pic_name[i]) + ".jpg", mode='wb') as f:
    #         f.write(pic_resp.content)
    #     f.close()



