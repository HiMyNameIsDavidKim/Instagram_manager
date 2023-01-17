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

all_btn = browser.find_elements(By.CLASS_NAME, '_aamw')
one_btn = all_btn[2]

color = one_btn.find_element(By.CLASS_NAME, '_abm0')
color = color.find_element(By.CLASS_NAME, '_ab6-')
color = color.value_of_css_property('color')
print(color)
if color == 'rgba(142, 142, 142, 1)':
    like_btn = one_btn.find_element(By.CLASS_NAME, '_abm0._abl_')
    like_btn.click()
    time.sleep(5)

for _ in range(100):
    all_btn = browser.find_elements(By.CLASS_NAME, '_aamw')
    one_btn = all_btn[0]
    color = one_btn.find_element(By.CLASS_NAME, '_abm0')
    color = color.find_element(By.CLASS_NAME, '_ab6-')
    color = color.value_of_css_property('color')
    if color == 'rgba(142, 142, 142, 1)':
        like_btn = one_btn.find_element(By.CLASS_NAME, '_abm0._abl_')
        like_btn.click()
    browser.get(url_feed)
    time.sleep(3)


prof = browser.find_element(By.CLASS_NAME, '_aaav')
prof.click()
logout = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacu._aacx._aada')[-1]
logout.click()