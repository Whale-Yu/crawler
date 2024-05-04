import os
import requests
from urllib.parse import quote
import json
import csv
import pandas as pd
import xlwt,xlrd
from mysql_conn import create_table,insert_table
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent

class Save(object):
    csvflag = False
    excelflag = False
    mysqlflag = False
    def __init__(self,str,filename):
        self.str = str
        self.filename = filename
    def save_way(self):
        if "1" in self.str:
            self.csvflag = True
            create_csv(self.filename + '.csv')
        if "2" in self.str:
            self.excelflag = True
            workbook = create_excel(self.filename + '.xlsx')
        if "3" in self.str:
            self.mysqlflag = True
            create_mysql_table(self.filename)


    def save(self,*args):
        if self.csvflag:
            insert_csv(self.filename + '.csv',args)
        # if self.excelflag:
        #
        if self.mysqlflag:
            insert_table(self.filename,args)

#创建csv文件
def create_csv(filename):
    if not os.path.exists(filename):
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(["题名", "作者", "来源", "发表时间", "数据库", "被引", "下载"])
#插入数据
def insert_csv(filename, args):
    with open(filename, mode='a', encoding='utf-8', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow([args[i] for i in range(len(args))])

def create_excel(filename):
    if not os.path.exists(filename):
        workbook = xlwt.Workbook(filename)
    else:
        workbook = xlrd.open_workbook(filename)
    return workbook

#创建数据库表
def create_mysql_table(table_name):
    try:
        create_table(f"{table_name}", "title", "author", "source", "date", "data", "quote", "download")
    except Exception as e:
        print(e)
        pass

def post_pageNum(pageNum:int,kw,data_saver=None):
    headers = {
        "Cookie": "cangjieStatus_NZKPTKNS72=true; cangjieConfig_NZKPTKNS72=%7B%22status%22%3Atrue%2C%22startTime%22%3A%222023-01-05%22%2C%22endTime%22%3A%222024-01-05%22%2C%22type%22%3A%22mix%22%2C%22poolSize%22%3A10%2C%22intervalTime%22%3A10000%2C%22persist%22%3Afalse%7D; Ecp_ClientId=d221118081600302565; Ecp_ClientIp=60.191.251.189; cnkiUserKey=b7df25ac-340e-85d3-9407-5dbe240ed0ca; Ecp_loginuserbk=SH0205; knsLeftGroupSelectItem=1%3B2%3B; Ecp_showrealname=1; SID_kns_new=kns25128007; language=chs; ASP.NET_SessionId=zkqugknt5qsjywy2dtljus3c; SID_kns8=015123151; Ecp_IpLoginFail=23030736.19.58.146; CurrSortField=%e7%9b%b8%e5%85%b3%e5%ba%a6%2frelevant%2c(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27time%27)+desc; CurrSortFieldType=desc; dblang=all; _pk_ref=%5B%22%22%2C%22%22%2C1678151519%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses=*; _pk_id=49cf36e6-e19f-4746-a750-e8d14bdcfea9.1678102106.2.1678151524.1678151519.",
        "Host": "kns.cnki.net",
        "Referer": f"https://kns.cnki.net/kns/search?dbcode=SCDB&kw={quote(kw)}&korder=SU&crossdbcodes=CJFQ,CDFD,CMFD,CPFD,IPFD,CCND,CISD,SNAD,BDZK,CCJD,CJRF,CJFN",
        "User-Agent": FakeUserAgent().random,
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://kns.cnki.net"
    }
    queryjson = {
        "Platform": "", "Resource": "CROSSDB", "DBCode": "SCDB",
        "KuaKuCode": "CJZK,CDFD,CMFD,CPFD,IPFD,CCND,BDZK,CPVD",
        "QNode": {"QGroup":
                      [{"Key": "Subject", "Title": "", "Logic": 0,
                        "Items": [{"Field": "SU", "Value": f"{kw}", "Operator": "TOPRANK", "Logic": 0}],
                        "ChildItems": []}]}, "ExScope": 1, "SearchType": "0",
    }
    queryjson = json.dumps(queryjson)
    data = {
        "QueryJson": queryjson,
        "DbCode": "SCDB",
        "pageNum": f"{pageNum}",
        "pageSize": "20",
        "sortField": "PT",
        "sortType": "desc",
        "boolSearch": "false",
        "boolSortSearch": "false",
        "version": "kns7",
        "CurDisplayMode": "listmode",
        "productStr": "CJZK, CDFD, CMFD, CPFD, IPFD, CCND, BDZK",
        "sentenceSearch": "false",
        "aside": "主题:机器视觉",
    }
    get_page(url='https://kns.cnki.net/kns/brief/grid',headers=headers,data=data,data_saver=data_saver)
    print(f"第{pageNum}页已爬取完毕")

def get_page(url,headers,data,data_saver):
    resp = requests.post(url=url, headers=headers, data=data)
    parse_info(resp.text,data_saver=data_saver)

def parse_info(content,data_saver):
    soup = BeautifulSoup(content,'html.parser')
    name_list = soup.find_all('td',class_="name")
    author_list = soup.find_all('td',class_="author")
    source_list = soup.find_all('td',class_="source")
    date_list = soup.find_all('td',class_="date")
    data_list = soup.find_all('td',class_="data")
    quote_list = soup.find_all('td',class_="quote")
    download_list = soup.find_all('td',class_="download")

    for i in range(len(name_list)):
        name = name_list[i].text.replace('\n','') #题名
        author = ''.join(author_list[i].text.split('\n')[1:-1]) #作者
        source = source_list[i].text.replace('\n','') #来源
        date = date_list[i].text.replace('\n','')#发表时间
        data = data_list[i].text.replace('\n','') #数据库
        quote = quote_list[i].text.replace('\n','') #被引
        if quote == '':
            quote = '0'
        download = download_list[i].text.replace('\n','') #下载
        if download == '':
            download = '0'
        data_saver.save(name,author,source,date,data,quote,download)
if __name__ == '__main__':
    kw = input("请输入要搜索的关键词:")
    s = Save(input("请选择保存方式\n1为csv\n2为excel\n3为Mysqldatabase(可多选):"),input("\n请输入要保存的文件名:"))
    s.save_way()
    num = 1
    while True:
        post_pageNum(num,kw,s)
        num += 1
        break