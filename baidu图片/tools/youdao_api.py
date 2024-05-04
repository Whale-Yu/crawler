from urllib import request, parse
import json
from faker import Faker


class trans(object):
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    def tran(self, text):
        index = text.find("http")
        text = text[:index]
        text = text.replace('\n', '').replace('#', '').replace('RT ', '').replace(':', '')
        ua = Faker().user_agent()
        headers = {
            'User-Agent': ua,
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',

        }
        # 表单数据
        from_data = {
            'i': text,
            'from': 'UTO',
            'to': 'UTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        from_data = parse.urlencode(from_data).encode('utf-8')
        req = request.Request(self.url, from_data, headers)
        res = request.urlopen(req).read().decode("utf-8")
        target = json.loads(res)
        try:
            result = target['translateResult'][0][0]['tgt']
        except:
            result = "Translate failed"
        return result


if __name__ == '__main__':
    eng=trans().tran('apple')
    print(eng.replace(' ', ''))
