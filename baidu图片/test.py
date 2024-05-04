# # # import requests  # 导入请求库
# # # import re
# # # import os
# # #
# # # url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11513145951136847483&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%8F%A3%E7%BD%A9&queryWord=%E5%8F%A3%E7%BD%A9&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=90&rn=30&gsm=5a&1683422786613='
# # # # 添加请求头，模拟浏览器，有些网站可以不加这个，不过最好是加上，油多不坏菜这个道理
# # # headers = {
# # #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
# # # res = requests.get(url, headers=headers)  # 发送请求，返回数据
# # # html = res.text  # 把返回的内容解析
# # # # 使用正则表达式匹配图片url
# # # img_url_list = re.findall('"thumbURL":"(.*?)"', html)
# # # # print(img_url_list)
# # # for i in range(len(img_url_list)):
# # #     print(img_url_list[i])
# # #     res_img = requests.get(img_url_list[i], headers=headers)
# # #     img = res_img.content  # 这个里是图片，我们需要返回二进制数据
# # #     # 把图片保存起来
# # #     dir = 'baiduImg'
# # #     try:  # 如果没有文件夹就创建
# # #         os.mkdir(dir)
# # #     except:
# # #         pass
# # #     with open(os.path.join(dir, str(i) + '_img.jpg'), 'wb') as f:
# # #         f.write(img)
# # #
# # #     print("爬取{}张图片成功".format(i))
# #
#
# import requests
# import re
# import os, glob
#
# keyword = '戴口罩的人'
# num = 200
#
# dir = 'baiduImg'
# try:
#     os.mkdir(dir)
# except:
#     pass
#
# count = 0
# p = 0
# while 1:
#     print(f'pn:{p}')
#     url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11513145951136847483&ipn=rj&ct=201326592&is=&fp=result&fr=&word={keyword}&queryWord={keyword}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={p}&rn=30&gsm=5a&1683422786613='
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
#     }
#     res = requests.get(url, headers=headers).json()
#     sum = 0
#     for i in range(len(res['data'])):
#         try:
#             print(res['data'][i]['thumbURL'])
#             sum += 1
#             res_img = requests.get(res['data'][i]['thumbURL'], headers=headers)
#             img = res_img.content
#
#             # with open(os.path.join(dir, keyword + '_' + str(count) + '.jpg'), 'wb') as f:
#             #     f.write(img)
#
#             # 使用glob模块匹配所有符合条件的文件（这里假设只有jpg和png格式的图片）
#             image_files = glob.glob(os.path.join(dir, '*.jpg'))
#             if len(image_files) >= num:
#                 print(f'共爬取{len(image_files)}')
#                 break
#
#             count += 1
#             print(f"爬取{i}张图片成功")
#         except:
#             pass
#
#     print(sum)
#
#     p += 30
#
#     image_files = glob.glob(os.path.join(dir, '*.jpg'))
#     if len(image_files) >= num:
#         print(f'共爬取{len(image_files)}')
#         break


import os
import requests
from faker import Faker


def download_images(keyword, num):
    """
    爬取百度图片搜索结果中指定关键词keyword的前 num 张图片，并下载到本地文件夹。
    :param keyword: 搜索关键词
    :param num: 需要下载的图片数量
    """
    # 创建保存图片的文件夹
    dir_name = f'downloads/{keyword}'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    count = 0
    page_num = 0

    # 持续爬取图片，直到达到指定数量
    while True:
        print(f'正在爬取第{page_num + 1}页...')

        # 待请求URL
        url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11513145951136847483&ipn=rj&ct=201326592&is=&fp=result&fr=&word={keyword}&queryWord={keyword}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={page_num * 30}&rn=30&gsm=5a&1683422786613='

        # 模拟请求头
        headers = {
            'User-Agent': Faker().user_agent()
        }

        # 发送 HTTP 请求，获取响应结果并解析 JSON 数据
        response = requests.get(url, headers=headers).json()

        # 遍历所有图片信息
        for image_info in response['data']:
            try:
                # 打印当前正在下载的图片的 URL
                print(f'正在下载第 {count} 张图片')
                print(image_info['thumbURL'])

                # 下载图片并保存到本地文件夹
                image_data = requests.get(image_info['thumbURL'], headers=headers)
                with open(os.path.join(dir_name, f'{keyword}_{count}.jpg'), 'wb') as f:
                    f.write(image_data.content)

                count += 1

                # 如果已经下载了足够数量的图片，则退出爬虫程序
                if count >= num:
                    print(f'一共下载了 {num} 张图片！！！！！！')
                    print(f'图片已保存至:{dir_name}')
                    return

            except:
                pass
        # 增加页数，以爬取下一页的图片
        page_num += 1


if __name__ == '__main__':
    download_images('戴口罩的人', num=200)
