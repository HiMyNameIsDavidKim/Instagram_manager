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
file = open(r"/Users/davidkim/security/blog_thatGul.txt", "r")
cmt_thatGul = file.read()
file = open(r"/Users/davidkim/security/blog_theThatGul.txt", "r")
cmt_theThatGul = file.read()

input_box = driver.find_element(By.CSS_SELECTOR, '#id')
input_box.send_keys(idd)
time.sleep(1)
input_box = driver.find_element(By.CSS_SELECTOR, '#pw')
input_box.send_keys(pw)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.btn_login').click()
time.sleep(5)

# soyChu_straw
straws = []
for page in range(10):
    driver.get(f"https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage={page}&groupId=0")
    time.sleep(1)
    spans = driver.find_elements(By.CLASS_NAME, 'reply')
    if len(straws) > 4:
        break
    for span in spans:
        if int(span.find_element(By.TAG_NAME, 'em').text) > 30:
            span.click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            straws.append(f'{driver.current_url}+?copen=1')
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])

# soyChu_soy
for straw in straws:
    driver.get(straw)
    driver.switch_to.window(driver.window_handles[-1])
    driver.switch_to.frame('mainFrame')
    time.sleep(2)
    btn = driver.find_element(By.CLASS_NAME, 'u_cbox_page')
    btn.click()
    time.sleep(2)
    soys = driver.find_elements(By.CLASS_NAME, 'u_cbox_name')
    for soy in soys:
        soy.send_keys(Keys.CONTROL +'\n')
        time.sleep(1)
    driver.close()
    cnt_soy = 1  # You can run again from here.
    soy_windows = driver.window_handles
    for soy_window in soy_windows:
        driver.switch_to.window(soy_window)
        time.sleep(0.5)
        driver.switch_to.frame('mainFrame')
        btn = driver.find_element(By.CLASS_NAME, 'btn_area')
        if btn.text == '이웃추가':
            btn.click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(2)
            each = driver.find_elements(By.TAG_NAME, 'label')[-1]  #
            each.click()
            nex = driver.find_element(By.CLASS_NAME, 'button_next._buddyAddNext')
            nex.click()
            time.sleep(2)
            text_box = driver.find_element(By.TAG_NAME, 'textarea')
            text_box.send_keys(cmt_soyChu)
            nex = driver.find_element(By.CLASS_NAME, 'button_next._addBothBuddy')
            nex.click()
            driver.close()
        driver.switch_to.window(soy_window)
        if cnt_soy != len(soy_windows):
            driver.close()
        cnt_soy += 1

# thatGul
for groupId in [6, 1, 5]:
    for page in range(1, 100):
        driver.get(f"https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage={page}&groupId={groupId}")
        time.sleep(1)
        gul_time = driver.find_element(By.CLASS_NAME, 'time')
        if gul_time.text[-1] != '전':
            break
        gongs = driver.find_elements(By.CLASS_NAME, 'u_likeit_list_btn._button.off')
        for gong in gongs:
            gong.click()
            time.sleep(0.5)
        spans = driver.find_elements(By.CLASS_NAME, 'reply')
        for span in spans:
            span.click()
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[-1])
            driver.switch_to.frame('mainFrame')
            nicks = driver.find_elements(By.CLASS_NAME, 'u_cbox_nick')
            if 'lightroong' in [i.text for i in nicks]:
                pass
            else:
                text_box = driver.find_element(By.CLASS_NAME, 'u_cbox_text.u_cbox_text_mention')
                text_box.send_keys(cmt_thatGul)
                btn = driver.find_element(By.CLASS_NAME, 'u_cbox_txt_upload')
                btn.click()
                time.sleep(2)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])

# theThatGul
driver.switch_to.window(driver.window_handles[-1])
driver.switch_to.frame('mainFrame')
pages = driver.find_elements(By.CLASS_NAME, 'u_cbox_page')
for i in range(0, 300):
    daps = driver.find_elements(By.CLASS_NAME, 'u_cbox_btn_reply')
    daps[2 * i].click()
    time.sleep(1)
    text_box = driver.find_element(By.CLASS_NAME, 'u_cbox_text.u_cbox_text_mention')
    text_box.send_keys(cmt_theThatGul)
    secret = driver.find_element(By.CLASS_NAME, 'u_cbox_secret_check')
    secret.click()
    btn = driver.find_element(By.CLASS_NAME, 'u_cbox_txt_upload')
    btn.click()
    time.sleep(2)

# window comeback
driver.switch_to.window(driver.window_handles[-1])