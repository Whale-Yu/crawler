# -*- codeing = utf-8 -*-
# @Time :2023/3/20 10:09
# @Author :yujunyu
# @Site :
# @File :wahis.py
# @software: PyCharm

# # index:https://wahis.woah.org/#/event-management

import requests
from faker import Faker
import json
import os
import csv
from get_lng_lat import get_lng_lat


path_file_name = 'data.csv'

url1 = 'https://wahis.woah.org/api/v1/pi/event/filtered-list?language=en'

headers = {
    'content-type': 'application/json',
    'user-agent': Faker().user_agent()
}

playload = {"eventIds": [], "reportIds": [], "countries": [], "firstDiseases": [], "secondDiseases": [], "typeStatuses": [], "reasons": [],
            "eventStatuses": [], "reportTypes": [], "reportStatuses": [], "eventStartDate": None, "submissionDate": None, "animalTypes": [],
            "sortColumn": None, "sortOrder": None, "pageSize": 100, "pageNumber": 0}

# 获取total_size
resp1 = requests.post(url=url1, headers=headers, data=json.dumps(playload)).json()  # 注意playload中是request playload，需要以json格式传入。不同于一般的data
total_size = resp1['totalSize']
print(f'总共:{total_size}条')

# 按total_size来遍历页
for i in range(total_size // 100 + 1):
    playload = {"eventIds": [], "reportIds": [], "countries": [], "firstDiseases": [], "secondDiseases": [], "typeStatuses": [],
                "reasons": [],
                "eventStatuses": [], "reportTypes": [], "reportStatuses": [], "eventStartDate": None, "submissionDate": None,
                "animalTypes": [],
                "sortColumn": None, "sortOrder": None, "pageSize": 100, "pageNumber": i}

    resp2 = requests.post(url=url1, headers=headers, data=json.dumps(playload)).json()

    list = resp2['list']
    print('\033[31m开始爬取第{}页共:{}条\033[0m'.format(i + 1, len(list)))

    for i in range(len(list)):
        # Country
        country = list[i]['country']
        # Report number
        reportType = list[i]['reportType']
        reportNumber = list[i]['reportNumber']
        if reportNumber == 0:
            reportNumber = reportType
        else:
            reportNumber = reportType + '_' + str(reportNumber)
        # Disease
        disease = list[i]['disease']
        # Genotype/ Serotype/ Subtype
        subType = list[i]['subType']
        # Reason
        reason = list[i]['reason']
        # Start date
        eventStartDate = list[i]['eventStartDate']
        eventStartDate = eventStartDate.split('T')
        eventStartDate = eventStartDate[0].replace('-', '/')
        # Report date
        submissionDate = list[i]['submissionDate']
        submissionDate = submissionDate.split('T')
        submissionDate = submissionDate[0].replace('-', '/')

        # reportId
        reportId = list[i]['reportId']
        # reportStatus
        reportStatus = list[i]['reportStatus']
        # eventId
        eventId = list[i]['eventId']
        # eventStatus
        eventStatus = list[i]['eventStatus']

        # animalType
        animalType = list[i]['animalType']
        print(reportId, country)

        # 获取经纬度
        lng, lat, country_ch = get_lng_lat(country)

        # 保存数据
        if not os.path.exists(path_file_name):
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    [
                        'Longitude',
                        'Latitude',
                        'Country-CH',
                        'Country',
                        'Report number',
                        'Disease',
                        'Genotype/ Serotype/ Subtype',
                        'Reason',
                        'Start date',
                        'Report date',
                        'reportId',
                        'reportStatus',
                        'eventId',
                        'eventStatus',
                        'animalType'
                    ]
                )
                writer.writerow(
                    [
                        lng,
                        lat,
                        country_ch,
                        country,
                        reportNumber,
                        disease,
                        subType,
                        reason,
                        eventStartDate,
                        submissionDate,
                        reportId,
                        reportStatus,
                        eventId,
                        eventStatus,
                        animalType
                    ]
                )
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    [
                        lng,
                        lat,
                        country_ch,
                        country,
                        reportNumber,
                        disease,
                        subType,
                        reason,
                        eventStartDate,
                        submissionDate,
                        reportId,
                        reportStatus,
                        eventId,
                        eventStatus,
                        animalType
                    ]
                )
