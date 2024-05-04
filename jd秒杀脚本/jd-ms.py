# !/usr/bin/env python
# 20200515
# 京东秒杀脚本，扫码登录版
from selenium import webdriver
import time, datetime

from selenium.webdriver.common.by import By
import pyttsx3

def say(text=''):
    # 初始化
    pt = pyttsx3.init()
    # 说什么
    pt.say(text)
    # 开始说吧
    pt.runAndWait()

# 时间格式："2020-05-15 10:30:00.000000"
def jdAutoBuy(ordertime):
    driver = webdriver.Chrome()

    print('.........................START..........................')
    say('请在10秒内完成登录，届时无效！！！！')
    print('请在10秒内完成登录，届时无效！！！！')
    driver.get("https://passport.jd.com/new/login.aspx")
    driver.implicitly_wait(5)
    # 10秒内扫码登录，过时会跳过
    time.sleep(10)

    print('跳转至购物车...')
    driver.get("https://cart.jd.com/cart.action")
    say('已跳转至购物车...')

    # 如果没有全选，点击全选
    if not driver.find_element(By.XPATH, r'//*[@id="cart-body"]/div[2]/div[3]/div[1]/div/input').is_selected():
        print('自动全选中商品...')
        driver.find_element(By.XPATH, r'//*[@id="cart-body"]/div[2]/div[3]/div[1]/div/input').click()  # 点击事件
        say('已自动全选中商品...')

    # driver.save_screenshot('order.png')
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(f'当前时间:{now}')
        if now > ordertime:
            print('开始点击结算...')
            driver.find_element(By.XPATH, r'//*[@id="cart-body"]/div[2]/div[5]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a').click()  # 点击事件
            say('已结算...')

            # js = "document.getElementsByClassName('submit-btn')[0].click()"
            # driver.execute_script(js)

            print('开始点击提交...')
            driver.find_element(By.XPATH, r'//*[@id="order-submit"]').click()  # 点击事件
            say('已提交')
            driver.quit()
            break
    print('商品秒杀成功，及时付款即可！！！！')
    say('主人,商品秒杀成功，及时付款即可！！！！')
    print('.........................END..........................')


if __name__=='__main__':

    jdAutoBuy('2023-03-16 19:17:00.000000')




