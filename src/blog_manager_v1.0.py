from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from random import randrange
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import sys

# Because of Naver's security program, use it line by line.

# Login
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

# soyChu
browser.get("https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0")
time.sleep(1)

straws = []
spans = browser.find_elements(By.CLASS_NAME, 'reply')
for span in spans:
    if int(span.find_element(By.TAG_NAME, 'em').text) > 30:
        straws.append(span)

for straw in straws:
    straw.click()

iframe = browser.find_element(By.TAG_NAME, 'iframe')
browser.switch_to.frame(iframe)


# html = browser.find_element(By.TAG_NAME, 'html')
# body = browser.find_element(By.TAG_NAME, 'body')
# browser.switch_to.parent_frame()
#
# soys = browser.find_element(By.CLASS_NAME, 'u_cbox_name')
# for soy in soys:
#     soy.get_attribute('href')
#     print(soy)