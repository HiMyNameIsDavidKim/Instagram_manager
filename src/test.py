from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from random import randrange
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(1)

file = open(r"/Users/davidkim/security/insta_nir.txt", "r")
data = file.read()
id, pw = tuple(data.split('\n'))

click = browser.find_elements(By.TAG_NAME, 'input')
click[0].send_keys(id)
click[1].send_keys(pw)
click[1].send_keys(Keys.RETURN)
time.sleep(5)

btn_later1 = browser.find_element(By.CLASS_NAME, '_acan._acao._acas')
btn_later1.click()
time.sleep(3)

btn_later2 = browser.find_element(By.CLASS_NAME, '_a9--._a9_1')
btn_later2.click()
time.sleep(3)




# file = open(r"/Users/davidkim/security/insta_tags.txt", "r")
# data = file.read()
# args = list(data.split('\n'))
# browser.get("https://www.instagram.com/explore/tags/" + args[0])
# time.sleep(3)
#
# feed = browser.find_elements(By.CLASS_NAME, "_aagw")
# feed[0].click()
#
# likes = browser.find_element(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aada._aade')
# likes.click()
#
# count = 0
# for _ in range(100):
#     rand = randrange(100)
#     like_people = browser.find_elements(By.CLASS_NAME, '_acan._acap._acas._aj1-')[rand]
#     if like_people.text == '팔로우' and count < 5:
#         like_people.send_keys(Keys.ENTER)
#         count += 1
#         time.sleep(3)

# file = open(r"/Users/davidkim/security/insta_infl.txt", "r")
# data = file.read()
# args = list(data.split('\n'))
# browser.get("https://www.instagram.com/" + args[0])
# time.sleep(3)
#
# followers = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacu._aacy._aad6._aadb._aade')[1]
# followers.click()
#
# count = 0
# for _ in range(100):
#     like_people = browser.find_elements(By.CLASS_NAME, '_acan._acap._acas._aj1-')[-1]
#     if like_people.text == '팔로우' and count < 3:
#         like_people.send_keys(Keys.ENTER)
#         count += 1
#         time.sleep(3)





prof = browser.find_element(By.CLASS_NAME, '_aaav')
prof.click()
logout = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacu._aacx._aada')[-1]
logout.click()