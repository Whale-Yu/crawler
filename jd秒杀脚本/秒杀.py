# !/usr/bin/env python
# 20200515
# 京东秒杀脚本，扫码登录版
from selenium import webdriver
import time,datetime
driver = webdriver.Chrome()
# 时间格式："2020-05-15 10:30:00.000000"
def jdAutoBuy(ordertime):
    print('.........................START..........................')
    driver.get("https://passport.jd.com/new/login.aspx")
    driver.implicitly_wait(5)
    #10秒内扫码登录，过时会跳过
    time.sleep(10)
    driver.get("https://cart.jd.com/cart.action")
    #如果没有全选，点击全选
    if not driver.find_element_by_class_name('jdcheckbox').is_selected():
        driver.find_element_by_class_name('jdcheckbox').click()
    #driver.save_screenshot('order.png')
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now>ordertime:
            driver.find_element_by_class_name('submit-btn').click()
            #js = "document.getElementsByClassName('submit-btn')[0].click()"
            #driver.execute_script(js)
            driver.find_element_by_id('order-submit').click()
            driver.quit()
            break
    print('.........................END..........................')

##调用秒杀函数
jdAutoBuy('2023-05-16 09:13:00.000000')


