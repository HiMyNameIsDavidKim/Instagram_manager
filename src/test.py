from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from random import randrange
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import sys

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
time.sleep(1)

file = open(r"/Users/davidkim/security/blog_lr.txt", "r")
data = file.read()
idd, pw = tuple(data.split('\n'))

input_box = browser.find_element(By.CSS_SELECTOR, '#id')
input_box.send_keys(idd)
time.sleep(1)
input_box = browser.find_element(By.CSS_SELECTOR, '#pw')
input_box.send_keys(pw)
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '.btn_login').click()
time.sleep(5)

btn_later1 = browser.find_element(By.CLASS_NAME, '_acan._acao._acas')
btn_later1.click()
time.sleep(3)
btn_later2 = browser.find_element(By.CLASS_NAME, '_a9--._a9_1')
btn_later2.click()
time.sleep(3)

########################

story = browser.find_elements(By.CLASS_NAME, '_aarf.x1e56ztr.x1gslohp')[1]
story.click()

########################

browser.get(f'https://www.instagram.com/{idd}')
browser.implicitly_wait(10)
time.sleep(1)
settings = browser.find_element(By.CLASS_NAME, '_abm0')
settings.click()
time.sleep(1)
logout_btn = browser.find_elements(By.CLASS_NAME, '_a9--._a9_1')[-2]
logout_btn.click()
time.sleep(1)