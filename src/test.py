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

story = browser.find_element(By.CLASS_NAME, '_aarf.x1e56ztr.x1gslohp')
story.click()
time.sleep(1)

story_owner = browser.find_element(By.CLASS_NAME, '_ac0l').text
like = browser.find_element(By.CLASS_NAME, '_aame')
color = like.find_element(By.CLASS_NAME, '_ab6-').value_of_css_property('color')
if color == 'rgba(255, 255, 255, 1)':
    like.click()
time.sleep(1)

next_story = browser.find_element(By.CLASS_NAME, '_9zm2')
next_story.click()
time.sleep(1)

quit_story = browser.find_elements(By.CLASS_NAME, '_abl-')[-1]
quit_story.click()
time.sleep(3)




prof = browser.find_element(By.CLASS_NAME, '_aaav')
prof.click()
logout = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacu._aacx._aada')[-1]
logout.click()