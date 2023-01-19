from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from random import randrange
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
import sys


class InstaManager(object):
    def __init__(self, TAGS=False, STORY=False, INFL=False, FEED=False, UNFLW=False, xN=1):
        global browser, url_login, url_tags, url_main, \
            file_idpw, file_tags, file_infl
        browser = webdriver.Chrome()
        url_login = 'https://www.instagram.com/accounts/login/'
        url_tags = "https://www.instagram.com/explore/tags/"
        url_main = 'https://www.instagram.com/'
        file_idpw = r"/Users/davidkim/security/insta_nir.txt"
        file_tags = r"/Users/davidkim/security/insta_tags.txt"
        file_infl = r"/Users/davidkim/security/insta_infl.txt"
        self.TAGS = TAGS
        self.STORY = STORY
        self.INFL = INFL
        self.FEED = FEED
        self.UNFLW = UNFLW
        self.xN = xN
        self.idd = None
        self.cnt_flwer = 0
        self.cnt_flwing = 0

    def process(self):
        self.login()
        self.laters()
        for _ in range(self.xN):
            if self.TAGS:
                self.follow_by_tags(2)
            if self.STORY:
                self.like_stories(30)
            if self.INFL:
                self.follow_by_infl(2)
            if self.FEED:
                self.like_feeds(30)
            if self.UNFLW:
                self.manage_flw(15)
        self.logout()

    def id_n_pw(self):
        file = open(file_idpw, "r")
        data = file.read()
        idd, pw = tuple(data.split('\n'))
        self.idd = idd
        print('### id and pw is uploaded. ###')
        return idd, pw

    def login(self):
        browser.get(url_login)
        browser.implicitly_wait(10)

        idd, pw = self.id_n_pw()
        click = browser.find_elements(By.TAG_NAME, 'input')
        click[0].send_keys(idd)
        click[1].send_keys(pw)
        click[1].send_keys(Keys.RETURN)
        print('### Login is completed. ###')
        time.sleep(5)

    def logout(self):
        browser.get(url_main)
        browser.implicitly_wait(10)

        prof = browser.find_element(By.CLASS_NAME, '_aaav')
        prof.click()
        logout = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacu._aacx._aada')[-1]
        logout.click()
        print('### Logout is completed. ###')
        browser.quit()

    def laters(self):
        btn_later1 = browser.find_element(By.CLASS_NAME, '_acan._acao._acas')
        btn_later1.click()
        time.sleep(3)
        btn_later2 = browser.find_element(By.CLASS_NAME, '_a9--._a9_1')
        btn_later2.click()
        time.sleep(3)
        print('### Later processes is completed. ###')

    def follow_loop(self, num):
        count = 0
        like_peoples = browser.find_elements(By.CLASS_NAME, '_acan._acap._acas._aj1-')
        for like_people in like_peoples:
            like_people.click()
            count += 1
            time.sleep(5)
            browser.implicitly_wait(1)
            if count >= num:
                break
        print('### Follow loop is completed. ###')

    def warn_reqs_over(self):
        divs = browser.find_elements(By.TAG_NAME, 'div')
        if '나중에 다시 시도하세요' in divs[-30].text:
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            self.logout()
            sys.exit()

    def follow_by_tags(self, num):
        print('### Now start to follow by tags. ###')
        file = open(file_tags, "r")
        data = file.read()
        tags = list(data.split('\n'))
        for tag in tags:
            browser.get(url_tags + tag)
            browser.implicitly_wait(10)

            print(f'### tag : {tag} ###')
            self.follow_feed_liker(num)

    def follow_feed_liker(self, num):
        feed = browser.find_elements(By.CLASS_NAME, "_aagw")
        feed[randrange(0, 10)].click()
        browser.implicitly_wait(10)

        likes = browser.find_element(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aada._aade')
        likes.click()
        browser.implicitly_wait(10)

        self.follow_loop(num)

    def follow_by_infl(self, num):
        print('### Now start to follow by influencers. ###')
        file = open(file_infl, "r")
        data = file.read()
        infls = list(data.split('\n'))
        for infl in infls:
            browser.get(url_main + infl + '/followers/')
            browser.implicitly_wait(10)

            print(f'### influencer : {infl} ###')
            self.follow_loop(num)

    def like_stories(self, num):
        print('### Now start to like stories. ###')
        browser.get(url_main)
        time.sleep(3)

        story = browser.find_elements(By.CLASS_NAME, '_aarf.x1e56ztr.x1gslohp')[3]
        story.click()
        time.sleep(1)

        last_owner = ''
        for _ in range(num):
            now_owner = browser.find_element(By.CLASS_NAME, '_ac0l').text[:5]

            if last_owner != now_owner:
                like = browser.find_element(By.CLASS_NAME, '_abm0._abl_')
                # color = like.find_element(By.CLASS_NAME, '_ab6-').value_of_css_property('color')
                # if color == 'rgba(255, 255, 255, 1)':
                like.click()
                last_owner = now_owner
                time.sleep(1)

            next_story = browser.find_element(By.CLASS_NAME, '_9zm2')
            next_story.click()
            time.sleep(1)
            print(f'like_stories count : {_ + 1}')

        quit_story = browser.find_elements(By.CLASS_NAME, '_abl-')[-1]
        quit_story.click()
        time.sleep(3)
        print('### Like stories is completed. ###')

    def like_feeds(self, num):
        print('### Now start to like feeds. ###')
        browser.get(url_main)
        time.sleep(3)

        limit = 0
        for _ in range(num):
            one_btn = browser.find_elements(By.CLASS_NAME, '_aamw')[0]

            color = one_btn.find_element(By.CLASS_NAME, '_abm0')
            color = color.find_element(By.CLASS_NAME, '_ab6-')
            color = color.value_of_css_property('color')

            if color == 'rgba(142, 142, 142, 1)':
                like_btn = one_btn.find_element(By.CLASS_NAME, '_abm0._abl_')
                like_btn.click()
            else: limit += 1

            if limit > 10:
                print(f'### There is no more feeds. Break loop. ###')
                break

            browser.get(url_main)
            time.sleep(3)
            print(f'like_feeds count : {_ + 1}')

        print('### Like stories is completed. ###')

    def manage_flw(self, num):
        print('### Now start to Manage followers. ###')
        self.my_cnt_flws()
        list_flwer = self.get_list_flwer()
        print(f'### followers : {len(list_flwer)} ###')
        list_flwing = self.get_list_flwing()
        print(f'### followings sample : {len(list_flwing)} ###')
        list_unflw = [i for i in list_flwing if i not in list_flwer]
        for _ in range(1, num+1):
            unflw = list_unflw[-_]
            browser.get(f'https://www.instagram.com/{unflw}')
            time.sleep(1)

            buttons = browser.find_element(By.CLASS_NAME, '_acan._acap._acat._aj1-')
            buttons.click()
            time.sleep(1)

            button = browser.find_elements(By.CLASS_NAME, '_abm4')[-1]
            button.click()
            time.sleep(1)
            print(f'unfollow count : {_}')

            self.warn_reqs_over()

        print('### Manage followers is completed. ###')

    def my_cnt_flws(self):
        browser.get(f'https://www.instagram.com/{self.idd}')
        time.sleep(3)
        self.cnt_flwer = browser.find_elements(By.CLASS_NAME, '_ac2a')[1].text
        self.cnt_flwing = browser.find_elements(By.CLASS_NAME, '_ac2a')[2].text

    def get_list_flwer(self):
        browser.get(f'https://www.instagram.com/{self.idd}/followers/')
        time.sleep(3)
        while True:
            pop_up = browser.find_element(By.CLASS_NAME, "_aano")
            browser.execute_script("arguments[0].scrollBy(0, 1000)", pop_up)  # 반복
            time.sleep(0.5)
            names = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aad7._aade')
            if len(names) >= int(self.cnt_flwer):
                list_flwer = [name.text for name in names][1:]
                break
        return list_flwer

    def get_list_flwing(self):
        browser.get(f'https://www.instagram.com/{self.idd}/following/')
        time.sleep(3)
        while True:
            pop_up = browser.find_element(By.CLASS_NAME, "_aano")
            browser.execute_script("arguments[0].scrollBy(0, 1000)", pop_up)  # 반복
            time.sleep(0.5)
            names = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aad7._aade')
            if len(names) > int(self.cnt_flwer)+200:
                list_flwing = [name.text for name in names][1:]
                break
        return list_flwing


if __name__ == '__main__':
    insta = InstaManager(TAGS=False,
                         STORY=False,
                         INFL=False,
                         FEED=False,
                         UNFLW=True,
                         xN=2)
    insta.process()