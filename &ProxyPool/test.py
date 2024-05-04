import requests

# 没有使用代理
# resp = requests.get("http://httpbin.org/get")
response = requests.get("http://httpbin.org/get")
print(response.text)

# 使用代理
# proxy = {
#     'http': 'http://127.0.0.1:10809',
#     "https": "http://127.0.0.1:10809"
# }

# clash
proxy = {
    'http': 'http://127.0.0.1:7890',
    "https": "http://127.0.0.1:7890"
}

response = requests.get("http://httpbin.org/get", proxies=proxy)
print(response.text)
