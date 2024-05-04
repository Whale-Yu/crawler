# 获取@优酷轮播台@的真实流媒体地址。
# 优酷轮播台是优酷直播live.youku.com下的一个子栏目，轮播一些经典电影电视剧，个人感觉要比其他直播平台影视区的画质要好，
# 而且没有平台水印和主播自己贴的乱七八糟的字幕遮挡。
# liveId 是如下形式直播间链接:
# “https://vku.youku.com/live/ilproom?spm=a2hcb.20025885.m_16249_c_59932.d_11&id=8019610&scm=20140670.rcmd.16249.live_8019610”中的8019610字段。

import requests
import time
import hashlib
import json


class YouKu:

    def __init__(self, rid):
        """
        获取优酷轮播台的流媒体地址
        Args:
            rid: 直播间url中id=8019610，其中id即为房间号
        """
        self.rid = rid
        self.s = requests.Session()

    def get_real_url(self):
        try:
            tt = str(int(time.time() * 1000))
            data = json.dumps({'liveId': self.rid, 'app': 'Pc'}, separators=(',', ':'))
            url = 'https://acs.youku.com/h5/mtop.youku.live.com.livefullinfo/1.0/?appKey=24679788'
            cookies = self.s.get(url).cookies
            token = cookies.get_dict().get('_m_h5_tk')[0:32]
            sign = hashlib.md5(f'{token}&{tt}&24679788&{data}'.encode('utf-8')).hexdigest()
            params = {
                't': tt,
                'sign': sign,
                'data': data
            }
            response = self.s.get(url, params=params).json()
            streamname = response.get('data').get('data').get('stream')[0].get('streamName')
            real_url = f'https://lvo-live.youku.com/vod2live/{streamname}_mp4hd2v3.m3u8?&expire=21600&psid=1&ups_ts=' \
                       f'{int(time.time())}&vkey= '
        except Exception:
            raise Exception('请求错误')
        return real_url


def get_real_url(rid):
    try:
        yk = YouKu(rid)
        return yk.get_real_url()
    except Exception as e:
        print('Exception：', e)
        return False


if __name__ == '__main__':
    r = input('请输入优酷轮播台房间号：\n')
    print(get_real_url(r))
