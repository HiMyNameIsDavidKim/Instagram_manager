import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from random import randrange
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# nick = 'lr'
nick = 'mat'
# Login
driver = webdriver.Chrome(f'C:\\Users\\light\\PycharmProjects\\pythonProject\\chromedriver-win64\\chromedriver.exe')
# ChromeDriverManager().install()
driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(10)
time.sleep(3)
file = open(r"C:\Users\light\Documents\security\insta_"+nick+".txt", "r", encoding='UTF8')
data = file.read()
idd, pw = tuple(data.split('\n'))
file.close()
click = driver.find_elements(By.TAG_NAME, 'input')
click[0].send_keys(idd)
click[1].send_keys(pw)
click[1].send_keys(Keys.RETURN)
''' Because of IG's security program, use it line by line. '''

# Story
def story():
    num = 100
    driver.get('https://www.instagram.com/')
    driver.implicitly_wait(10)
    time.sleep(1)
    story = driver.find_elements(By.CLASS_NAME, '_aarf.x1e56ztr')[1]
    story.click()
    time.sleep(1)
    last_owner = ''
    cnt = 0
    for _ in range(num):
        body = driver.find_element(By.TAG_NAME, 'body')
        now_owner = driver.find_element(By.CLASS_NAME, '_ac0l').text[:30]
        likes = driver.find_elements(By.CLASS_NAME, '_abx4')
        if len(likes) != 0 and last_owner != now_owner and '광고' not in now_owner:
            likes[0].click()
            last_owner = now_owner
            time.sleep(1)
        elif len(likes) == 0 and last_owner != now_owner and '광고' not in now_owner:
            likes_2 = driver.find_elements(By.CLASS_NAME, '_ac13')
            likes_2[0].click()
            last_owner = now_owner
            time.sleep(1)
        body.send_keys(Keys.RIGHT)
        time.sleep(1)
        cnt += 1
        if cnt >= num:
            driver.get('https://www.instagram.com/')
            time.sleep(3)
    return print('story completed.')

# Feed
def feed():
    num = 50
    driver.get('https://www.instagram.com/?variant=following')
    driver.implicitly_wait(10)
    time.sleep(1)
    body = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(num//3):
        body.send_keys(Keys.END)
        time.sleep(5)
        like_btns = driver.find_elements(By.CLASS_NAME, '_aamw')
        like_btns.reverse()
        cnt = 0
        for like_btn in like_btns:
            color = like_btn.find_element(By.TAG_NAME, 'svg')
            color = color.value_of_css_property('color')
            if color == 'rgba(38, 38, 38, 1)':
                like_btn = like_btn.find_element(By.TAG_NAME, 'div')
                driver.execute_script("arguments[0].click();", like_btn)
                [body.send_keys(Keys.UP) for ___ in range(15)]
                time.sleep(randrange(10, 15))
                cnt += 1
            if cnt > 2:
                body.send_keys(Keys.HOME)
                break
    return print('feed completed.')

# flwerList
def flwerList():
    file = open(r"C:\Users\light\Documents\security\insta_flwer_"+nick+".txt", "r", encoding='UTF8')
    data = file.read()
    list_flwer = list(data.split('\n'))
    file.close()
    driver.get(f'https://www.instagram.com/{idd}')
    time.sleep(3)
    cnt_flwer = driver.find_elements(By.CLASS_NAME, '_ac2a')[1].text
    cnt_flwing = driver.find_elements(By.CLASS_NAME, '_ac2a')[2].text
    if len(list_flwer) != cnt_flwer:
        driver.get(f'https://www.instagram.com/{idd}/followers/')
        time.sleep(3)
        last_names = None
        while True:
            pop_up = driver.find_element(By.CLASS_NAME, "_aano")
            driver.execute_script("arguments[0].scrollBy(0, 1000)", pop_up)  # 반복
            time.sleep(3)
            names = driver.find_elements(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aad7._aade')
            if len(names) >= int(cnt_flwer) or names == last_names:
                list_flwer = [name.text for name in names][1:]
                break
            last_names = names
        file = open(r"C:\Users\light\Documents\security\insta_flwer_"+nick+".txt", "w", encoding='UTF8')
        [file.write(f'{i}\n') for i in list_flwer]
        file.close()

# UnflwReady
def unflwReady():
    scroll_cnt = 75
    driver.get(f'https://www.instagram.com/{idd}/following/')
    driver.implicitly_wait(10)
    time.sleep(3)
    pop_up = driver.find_element(By.CLASS_NAME, "_aano")
    for _ in range(scroll_cnt):
        driver.execute_script("arguments[0].scrollBy(0, 1000)", pop_up)
        time.sleep(2)
        if _ == scroll_cnt-1:
            names = driver.find_elements(By.CLASS_NAME, 'x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')
    print(f'##### Ready to unfollow. #####')
    return names

# UnflwExcute
def unflwExcute(names):
    num = 30
    cnt = 0
    file = open(r"C:\Users\light\Documents\security\insta_flwer_"+nick+".txt", "r", encoding='UTF8')
    data = file.read()
    list_flwer = list(data.split('\n'))
    file.close()
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
    print(f'##### Complete to unfollow. #####')

if __name__ == '__main__':
    cnt = 0
    hour = 2
    for i in range(1000):
        for _ in range(1000):
            try:
                print('##### Loop start #####')
                story()
                feed()
                print('##### Loop end #####')
                time.sleep(60 * 60 * hour)
                cnt = 0
            except:
                if cnt >= 2:
                    driver.get('https://www.instagram.com/')
                    print('@@@@@ Error came out @@@@@')
                    time.sleep(60 * 60 * hour)
                    cnt = 0
                    break
                else:
                    print('@@@@@ RESET @@@@@')
                    cnt += 1
                    break

if __name__ == '__main__':
    # flwerList()
    names = unflwReady()
    unflwExcute(names)
    unflwExcute(names)
    names = unflwReady()
    unflwExcute(names)
    unflwExcute(names)
    driver.get(f'https://www.instagram.com/{idd}')

# End