import time

import requests
import random

proxypool_url = 'http://127.0.0.1:5555/random'
target_url = 'http://httpbin.org/get'


def get_random_proxy():
    """
    get random proxy from proxypool
    :return: proxy
    """
    try:
        proxy = requests.get(proxypool_url).text.strip()
        return proxy

    except requests.exceptions.ConnectionError as e:
        print('Error1', e.args)


def crawl(url, proxy):
    """
    use proxy to crawl page
    :param url: page url
    :param proxy: proxy, such as 8.8.8.8:8888
    :return: html
    """
    # proxies = {'http': 'http://' + proxy}
    proxies = {
        'http': f'http://{proxy}',
        "https": f"http://{proxy}"
    }
    return requests.get(url, proxies=proxies).text


def main():
    """
    main method, entry point
    :return: none
    """
    proxy = get_random_proxy()
    print('get random proxy: ', proxy)

    try:
        html = crawl(target_url, proxy)
        print(html)
        # if len(html.split(','))==10:
        #     f = open('ip_pool.txt', 'a', encoding='utf-8')
        #     f.write(f'{proxy}\n')
        #     print("\033[34m可用并写入\033[0m")
    except:
        print('Error2')


if __name__ == '__main__':
    main()
