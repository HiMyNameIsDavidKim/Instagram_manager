import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from random import randrange
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import sys
from datetime import datetime

''' Because of IG's security program, use it line by line. '''

# Login
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(10)
file = open(r"/Users/davidkim/security/insta_lr.txt", "r", encoding='UTF8')
data = file.read()
idd, pw = tuple(data.split('\n'))
file.close()
click = driver.find_elements(By.TAG_NAME, 'input')
click[0].send_keys(idd)
click[1].send_keys(pw)
click[1].send_keys(Keys.RETURN)
driver.implicitly_wait(10)
time.sleep(5)
btn_later1 = driver.find_element(By.CLASS_NAME, '_acan._acao._acas')
btn_later1.click()
driver.implicitly_wait(10)
time.sleep(3)
btn_later2 = driver.find_element(By.CLASS_NAME, '_a9--._a9_1')
btn_later2.click()
driver.implicitly_wait(10)
time.sleep(3)

# UnflwChecker
file = open("/Users/davidkim/security/insta_flwer.txt", "r", encoding='UTF8')
data = file.read()
list_flwer = list(data.split('\n'))
file.close()
driver.get(f'https://www.instagram.com/{idd}')
time.sleep(3)
cnt_flwer = driver.find_elements(By.CLASS_NAME, '_ac2a')[1].text
cnt_flwing = driver.find_elements(By.CLASS_NAME, '_ac2a')[2].text
if len(list_flwer) < 10:
    driver.get(f'https://www.instagram.com/{idd}/followers/')
    time.sleep(3)
    while True:
        pop_up = driver.find_element(By.CLASS_NAME, "_aano")
        driver.execute_script("arguments[0].scrollBy(0, 1000)", pop_up)  # 반복
        time.sleep(1)
        names = driver.find_elements(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aad7._aade')
        if len(names) >= int(cnt_flwer):
            list_flwer = [name.text for name in names][1:]
            break
    file = open("/Users/davidkim/security/insta_flwer.txt", "w", encoding='UTF8')
    [file.write(f'{i}\n') for i in list_flwer]
    file.close()

# UnflwReady
driver.get(f'https://www.instagram.com/{idd}/following/')
driver.implicitly_wait(10)
time.sleep(3)
pop_up = driver.find_element(By.CLASS_NAME, "_aano")

# UnflwScroll
while True:
    driver.execute_script("arguments[0].scrollBy(0, 1000)", pop_up)
    time.sleep(2)
    names = driver.find_elements(By.CLASS_NAME, 'x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1'
                                                '.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf'
                                                '.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9'
                                                '.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r'
                                                '.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd'
                                                '.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt'
                                                '.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xh8yej3.x193iq5w'
                                                '.x1lliihq.x1dm5mii.x16mil14.xiojian.x1yutycm')
    if len(names) >= int(cnt_flwer):
        break


num = 100
# UnflwExcute
cnt = 0
for name in names:
    if name.text.split("\n")[0] not in list_flwer:
        btn = name.find_elements(By.CLASS_NAME, '_acan._acap._acat._aj1-')
        btn[0].click()
        time.sleep(1)
        btn2 = driver.find_elements(By.CLASS_NAME, '_a9--._a9-_')
        btn2[0].click()
        time.sleep(randrange(1, 3))
        cnt += 1
    names.remove(name)
    if cnt >= num:
        break

num = 100
# Story
driver.get('https://www.instagram.com/')
driver.implicitly_wait(10)
time.sleep(1)
story = driver.find_elements(By.CLASS_NAME, '_aarf.x1e56ztr')[1]
story.click()
time.sleep(1)
last_owner = ''
for _ in range(num):
    now_owner = driver.find_element(By.CLASS_NAME, '_ac0l').text[:5]
    if last_owner != now_owner:
        like = driver.find_element(By.CLASS_NAME, '_abm0._abl_')
        like.click()
        last_owner = now_owner
        time.sleep(1)
    next_story = driver.find_element(By.CLASS_NAME, '_9zm2')
    next_story.click()
    time.sleep(1)
    if _ >= num-1:
        body = driver.find_elements(By.TAG_NAME, 'body')
        body[0].send_keys(Keys.ESCAPE)
        time.sleep(3)

# Logout
driver.get(f'https://www.instagram.com/{idd}')
driver.implicitly_wait(10)
time.sleep(1)
settings = driver.find_element(By.CLASS_NAME, '_abm0')
settings.click()
time.sleep(1)
logout_btn = driver.find_elements(By.CLASS_NAME, '_a9--._a9_1')[-2]
logout_btn.click()
time.sleep(1)
