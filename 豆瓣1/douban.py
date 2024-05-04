import requests
from lxml import etree
import os
import csv

head1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
    'Referer': 'https://movie.douban.com/explore',
    'Cookie': 'bid=yjYbw02SRKk; ll="118172"; gr_user_id=112d1f0c-cd0a-4017-b422-56595447672f; _vwo_uuid_v2=D711FFC491786D65C73C827CFFA8682DC|b1b93be7a2257853fbd610d85ca5e63b; __gads=ID=7d52698c738b1afa-2283da1b27cf0084:T=1643435911:RT=1643435911:S=ALNI_MYvpZxFVkKYnqIhoDkTvNY3nvQkzQ; __yadk_uid=h0RVkfw3pJHrLCV0fsuz3254ERHP75rJ; douban-fav-remind=1; viewed="4055198"; __gpi=UID=000006a4592350b5:T=1655267409:RT=1659833625:S=ALNI_MY30YRaYfBUWSZtU6leRrR7DYCQfw; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1659835994; dbcl2="260574641:XLAJOSeAOAs"; push_noty_num=0; push_doumail_num=0; ck=PTyl; ap_v=0,6.0; __utma=30149280.301316717.1651235739.1659848485.1659861171.14; __utmc=30149280; __utmz=30149280.1659861171.14.12.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmv=30149280.26057; __utmb=30149280.6.10.1659861171; __utma=223695111.989429162.1655267407.1659848616.1659861189.13; __utmb=223695111.0.10.1659861189; __utmc=223695111; __utmz=223695111.1659861189.13.11.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1659861189%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=f1b7af25a8247134.1655267407.13.1659861200.1659849437.',
    'X-Requested-With': 'XMLHttpRequest'
}
tag_list = ['热门', '最新', '经典', '可播放', '豆瓣高分', '冷门佳片', '华语', '欧美', '韩国', '日本', '动作', '喜剧', '爱情', '科幻', '悬疑', '恐怖', '治愈']
print(len(tag_list))
page = int(input("请输入页数:"))
# for t in range(len(tag_list)):
#     print(tag_list[t])
tag=tag_list[1]     # 改变类别
page_limit = 0 + 20 * (page - 1)
for page in range(0, page_limit + 1, 20):
    # print(page)
    params1 = {
        'type': 'movie',
        'tag': tag,  # 可变
        'sort': 'recommend',
        'page_limit': 20,
        'page_start': page,  # 可变 /+20
    }
    url1 = "https://movie.douban.com/j/search_subjects"
    resp1 = requests.get(url=url1, params=params1, headers=head1, timeout=20).json()
    # print(resp1)
    print(len(resp1['subjects']))
    for i in range(len(resp1['subjects'])):
        movie_url = resp1['subjects'][i]['url']
        print(movie_url)
        resp2 = requests.get(movie_url, headers=head1, timeout=20)
        html = etree.HTML(resp2.text)
        # 电影名、上映时间、标签、导演、编剧、演员、评分、简介、海报url
        try:
            title = html.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
        except:
            title = ''
        try:
            time = html.xpath('//*[@id="content"]/h1/span[2]/text()')[0].strip('()')
        except:
            time = ''
        try:  # 取了3个标签
            label = (html.xpath('//*[@id="info"]/span[5]/text()')[0] + '/' +
                     html.xpath('//*[@id="info"]/span[6]/text()')[0] + '/' +
                     html.xpath('//*[@id="info"]/span[7]/text()')[0]).strip('制片国家/地区:').strip('制片国家/地区:/语言').strip(
                '/官方网站')
        except:
            label = ''
        try:
            dir = html.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]
        except:
            dir = ''
        try:
            writes = html.xpath('//*[@id="info"]/span[2]/span[2]/a/text()')
            writes = '/'.join(writes)
        except:
            writes = ''
        try:
            actors = html.xpath('//*[@id="info"]/span[3]/span[2]//*')
            all_actor = []
            for actor in actors:
                all_actor.append(actor.xpath('./text()')[0])
            all_actor = '/'.join(all_actor)
        except:
            all_actor = ''
        try:
            rate = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]
        except:
            rate = ''
        try:
            intro = html.xpath('//*[@id="link-report"]/span/text()')[0].strip()
        except:
            intro = ''
        try:
            img_url = html.xpath('//*[@id="mainpic"]/a/img/@src')[0]
        except:
            img_url = ''

        print(label)
        path_file_name = './doubanMovie.csv'
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['类别', '电影详情页url', '电影名', '年份', '标签', '导演', '编剧', '演员', '评分', '简介', '海报url'])
                writer.writerow(
                    [tag, movie_url, title, time, label, dir, writes, all_actor, rate, intro, img_url])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow(
                    [tag, movie_url, title, time, label, dir, writes, all_actor, rate, intro, img_url])
