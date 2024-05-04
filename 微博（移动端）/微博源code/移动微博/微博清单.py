# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/22 16:49
# @Author :yujunyu
# @Site :
# @File :微博清单.py
# @software: PyCharm
# 程序功能: 按关键字爬取微博清单
# 程序作者: 马哥python说
import os
import re  # 正则表达式提取文本
from jsonpath import jsonpath  # 解析json数据
import requests  # 发送请求
import pandas as pd  # 存取csv文件
import datetime  # 转换时间用


def trans_time(v_str):
	"""转换GMT时间为标准格式"""
	GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
	timeArray = datetime.datetime.strptime(v_str, GMT_FORMAT)
	ret_time = timeArray.strftime("%Y-%m-%d %H:%M:%S")
	return ret_time


def get_weibo_list(v_keyword, v_max_page):
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding": "gzip, deflate, br",
	}
	for page in range(1, v_max_page + 1):
		print('===开始爬取第{}页微博==='.format(page))
		url = 'https://m.weibo.cn/api/container/getIndex'
		params = {
			"containerid": "100103type=1&q={}".format(v_keyword),
			"page_type": "searchall",
			"page": page
		}
		r = requests.get(url, headers=headers, params=params)
		print(r.status_code)
		# pprint(r.json())
		cards = r.json()["data"]["cards"]
		text_list = jsonpath(cards, '$..mblog.text')
		dr = re.compile(r'<[^>]+>', re.S)
		text2_list = []
		print('text_list is:')
		print(text_list)
		if not text_list:  # 如果未获取到微博内容，进入下一轮循环
			continue
		if type(text_list) == list and len(text_list) > 0:
			for text in text_list:
				text2 = dr.sub('', text)  # 正则表达式提取微博内容
				print(text2)
				text2_list.append(text2)
		time_list = jsonpath(cards, '$..mblog.created_at')
		time_list = [trans_time(v_str=i) for i in time_list]
		author_list = jsonpath(cards, '$..mblog.user.screen_name')
		id_list = jsonpath(cards, '$..mblog.id')
		bid_list = jsonpath(cards, '$..mblog.bid')
		reposts_count_list = jsonpath(cards, '$..mblog.reposts_count')
		comments_count_list = jsonpath(cards, '$..mblog.comments_count')
		attitudes_count_list = jsonpath(cards, '$..mblog.attitudes_count')
		df = pd.DataFrame(
			{
				'页码': [page] * len(id_list),
				'微博id': id_list,
				'微博bid': bid_list,
				'微博作者': author_list,
				'发布时间': time_list,
				'微博内容': text2_list,
				'转发数': reposts_count_list,
				'评论数': comments_count_list,
				'点赞数': attitudes_count_list,
			}
		)
		if os.path.exists(v_weibo_file):
			header = None
		else:
			header = ['页码', '微博id', '微博bid', '微博作者', '发布时间', '微博内容', '转发数', '评论数', '点赞数']  # csv文件头
		df.to_csv(v_weibo_file, mode='a+', index=False, header=header, encoding='utf_8_sig')
		print('csv保存成功:{}'.format(v_weibo_file))

if __name__ == '__main__':
	max_search_page = 80
	search_keyword = '裸眼3D'
	v_weibo_file = '微博清单_{}_前{}页.csv'.format(search_keyword, max_search_page)
	if os.path.exists(v_weibo_file):
		os.remove(v_weibo_file)
		print('微博清单存在，已删除: {}'.format(v_weibo_file))
	get_weibo_list(v_keyword=search_keyword, v_max_page=max_search_page)
	df = pd.read_csv(v_weibo_file)
	df.drop_duplicates(subset=['微博bid'], inplace=True, keep='first')
	df.to_csv(v_weibo_file, index=False, encoding='utf_8_sig')
	print('数据清洗完成')
