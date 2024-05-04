import random

# 随机获取一个user_agent
def get_user_agent():
    android_user_agents = [
        'Mozilla/5.0 (Linux; Android 7.0; MI 5s Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 wxwork/2.4.16 MicroMessenger/6.3.22 NetType/WIFI Language/zh',
        'Mozilla/5.0 (Linux; Android 9; PCNM00 Build/PKQ1.190630.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045129 Mobile Safari/537.36 MMWEBID/1926 MicroMessenger/7.0.12.1620(0x27000C37) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
        'Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/9034 MicroMessenger/7.0.12.1620(0x27000C36) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
        'Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Pro Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1171 MMWEBSDK/200201 Mobile Safari/537.36 MMWEBID/229 MicroMessenger/7.0.12.1620(0x27000C37) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
        'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1171 MMWEBSDK/191201 Mobile Safari/537.36 MMWEBID/4454 MicroMessenger/7.0.10.1580(0x27100AFF) Process/toolsmp NetType/WIFI Language/zh_CN ABI/arm32',
        'Mozilla/5.0 (Linux; Android 9; BKL-AL20 Build/HUAWEIBKL-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/7838 MicroMessenger/7.0.11.1600(0x27000B34) Process/tools NetType/4G Language/zh_CN ABI/arm64',
        'Mozilla/5.0 (Linux; Android 10; VOG-AL00 Build/HUAWEIVOG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/2687 MicroMessenger/7.0.10.1580(0x27000AFE) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
    ]
    return random.choice(android_user_agents)