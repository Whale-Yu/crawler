import time
from selenium import webdriver
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")










####淘宝购物Python全自动实现####

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
time.sleep(3)
browser.find_element_by_link_text("亲，请登录").click()
print(f"请尽快扫码登录")
time.sleep(10)
browser.get("https://cart.taobao.com/cart.htm")
time.sleep(4)
#购物车 商品全选
while True:
    if browser.find_element_by_id("J_SelectAll1"):
        browser.find_element_by_id("J_SelectAll1").click()
        break
time.sleep(4)
#Python全自化结算
while True:
    try:
        browser.find_element_by_link_text("结 算").click()
        print(f"主人,结算提交成功,我已帮全买到商品啦,请及时支付订单")
        speaker.Speak(f"主人,结算提交成功,我已帮买到商品啦,请及时支付订单")
        time.sleep(1)
        break
    except:
        pass
# 点击提交订单按钮
while True:
    try:
        if browser.find_element_by_link_text('提交订单').click():
            print(f"抢购成功，请尽快付款")
    except:
        print(f"主人,我已帮你抢到商品啦,您来支付吧")
        break
time.sleep(0.01)


