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
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
time.sleep(1)

file = open(r"/Users/davidkim/security/blog_lr.txt", "r")
data = file.read()
idd, pw = tuple(data.split('\n'))
file = open(r"/Users/davidkim/security/blog_soyChu.txt", "r")
cmt_soyChu = file.read()

input_box = driver.find_element(By.CSS_SELECTOR, '#id')
input_box.send_keys(idd)
time.sleep(1)
input_box = driver.find_element(By.CSS_SELECTOR, '#pw')
input_box.send_keys(pw)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.btn_login').click()
time.sleep(5)

# soyChu
# for page in range(10):
driver.get(f"https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage={page}&groupId=0")
time.sleep(1)

straws = []
spans = driver.find_elements(By.CLASS_NAME, 'reply')
for span in spans:
    if int(span.find_element(By.TAG_NAME, 'em').text) > 30:
        straws.append(span)

for straw in straws:
    straw.click()

main_windows = driver.window_handles
driver.switch_to.window(main_windows[-1])
driver.switch_to.frame('mainFrame')

btn = driver.find_element(By.CLASS_NAME, 'u_cbox_page')
btn.click()

soys = driver.find_elements(By.CLASS_NAME, 'u_cbox_name')
for soy in soys:
    soy.send_keys(Keys.CONTROL +'\n')
driver.close()

soy_windows = list(set(driver.window_handles) - set(main_windows))
for soy_window in soy_windows:
    driver.switch_to.window(soy_window)
    time.sleep(0.5)
    driver.switch_to.frame('mainFrame')
    btn = driver.find_element(By.CLASS_NAME, 'btn_area')
    if btn.text == '이웃추가':
        btn.click()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        each = driver.find_elements(By.TAG_NAME, 'label')[-1]
        each.click()
        nex = driver.find_element(By.CLASS_NAME, 'button_next._buddyAddNext')
        nex.click()
        time.sleep(0.5)
        text_box = driver.find_element(By.TAG_NAME, 'textarea')
        text_box.send_keys(cmt_soyChu)
        nex = driver.find_element(By.CLASS_NAME, 'button_next._addBothBuddy')
        nex.click()
        driver.close()
    driver.switch_to.window(soy_window)
    driver.close()
    time.sleep(0.5)


### 리스트 레인지 오버 에러 뜸 뭔지 모르겠음