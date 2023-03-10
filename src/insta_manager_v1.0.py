from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from random import randrange
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
import sys


class InstaManager(object):
    def __init__(self, TAGS=False, STORY=False, FEED=False, INFL=False, UNFLW=False, REPEAT=1):
        global browser, url_login, url_tags, url_main, \
            file_idpw, file_tags, file_infl, file_unfl
        browser = webdriver.Chrome()
        url_login = 'https://www.instagram.com/accounts/login/'
        url_tags = "https://www.instagram.com/explore/tags/"
        url_main = 'https://www.instagram.com/'
        file_idpw = r"/Users/davidkim/security/insta_nir.txt"
        file_tags = r"/Users/davidkim/security/insta_tags.txt"
        file_infl = r"/Users/davidkim/security/insta_infl.txt"
        file_unfl = r"/Users/davidkim/security/insta_unfl.txt"
        self.TAGS = TAGS
        self.STORY = STORY
        self.FEED = FEED
        self.INFL = INFL
        self.UNFLW = UNFLW
        self.REPEAT = REPEAT
        self.idd = None
        self.cnt_flwer = 0
        self.cnt_flwing = 0
        self.list_unflw = []
        self.check = 0

    def process(self):
        self.login()
        self.laters()
        for _ in range(self.REPEAT):
            if self.TAGS:
                self.follow_by_tags(5)
            if self.STORY:
                self.like_stories(30)
            if self.FEED:
                self.like_feeds(30)
            if self.INFL:
                self.follow_by_infl(5)
            if self.UNFLW:
                self.manage_flw(10)
        self.logout()

    def id_n_pw(self):
        file = open(file_idpw, "r")
        data = file.read()
        idd, pw = tuple(data.split('\n'))
        file.close()
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
        browser.implicitly_wait(10)
        time.sleep(5)

    def logout(self):
        browser.get(f'{url_main}{self.idd}')
        browser.implicitly_wait(10)
        time.sleep(1)

        settings = browser.find_element(By.CLASS_NAME, '_abm0')
        settings.click()
        time.sleep(1)

        logout_btn = browser.find_elements(By.CLASS_NAME, '_a9--._a9_1')[-2]
        logout_btn.click()
        time.sleep(1)

        print('### Logout is completed. ###')
        browser.quit()

    def laters(self):
        btn_later1 = browser.find_element(By.CLASS_NAME, '_acan._acao._acas')
        btn_later1.click()
        browser.implicitly_wait(10)
        time.sleep(3)
        btn_later2 = browser.find_element(By.CLASS_NAME, '_a9--._a9_1')
        btn_later2.click()
        browser.implicitly_wait(10)
        time.sleep(3)
        print('### Later processes is completed. ###')

    def check_reqs_over(self, minute, index):
        divs = browser.find_elements(By.TAG_NAME, 'div')
        if '????????? ?????? ???????????????' in divs[-index].text:
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            ok = browser.find_element(By.CLASS_NAME, '_a9--._a9_1')
            ok.click()
            for i in range(minute):
                print(f'### System cool down : {minute-i} min left ###')
                time.sleep(60)
            self.check += 1

    def warn_reqs_over(self, index):
        divs = browser.find_elements(By.TAG_NAME, 'div')
        if '????????? ?????? ???????????????' in divs[-index].text:
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            print('### Warning : Too much request ###')
            print('### Shut Down ###')
            self.check += 1

    def follow_loop(self, num):
        while True:
            like_peoples = browser.find_elements(By.CLASS_NAME, '_acan._acap')
            target = []
            [target.append(i) if i.text == '?????????' else None for i in like_peoples]
            if len(target) > num+3:
                break
            pop_up = browser.find_elements(By.CLASS_NAME, "_acan._acap")[-1]
            pop_up.send_keys(Keys.TAB)
            time.sleep(1)
        like_peoples = target[1:]

        count = 0
        for like_people in like_peoples:
            like_people.click()
            count += 1
            time.sleep(3)
            browser.implicitly_wait(1)
            if count >= num:
                break

            if self.check in range(10):
                self.check_reqs_over(10, 50)
            elif self.check == 10:
                self.warn_reqs_over(50)
                break

        print(f'### Follow loop is completed.({count}ea) ###')

    def follow_by_tags(self, num):
        print('### Now start to follow by tags. ###')
        file = open(file_tags, "r")
        data = file.read()
        tags = list(data.split('\n'))
        file.close()
        for tag in tags:
            print(f'### tag : {tag} ###')
            browser.get(url_tags + tag)
            browser.implicitly_wait(10)
            time.sleep(3)

            self.follow_feed_liker(num)

    def follow_feed_liker(self, num):
        feed = browser.find_elements(By.CLASS_NAME, "_aagw")[randrange(0, 5)]
        feed.click()
        browser.implicitly_wait(10)
        time.sleep(3)

        likes = browser.find_element(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aada._aade')
        likes.click()
        browser.implicitly_wait(10)
        time.sleep(3)

        self.follow_loop(num)

    def follow_by_infl(self, num):
        print('### Now start to follow by influencers. ###')
        file = open(file_infl, "r")
        data = file.read()
        infls = list(data.split('\n'))
        file.close()
        for infl in infls:
            print(f'### influencer : {infl} ###')
            browser.get(url_main + infl + '/followers/')
            browser.implicitly_wait(10)
            time.sleep(3)

            while True:
                pop_up = browser.find_element(By.CLASS_NAME, "_aano")
                browser.execute_script("arguments[0].scrollBy(0, 1000)", pop_up)  # ??????
                time.sleep(1)

                like_peoples = browser.find_elements(By.CLASS_NAME, '_acan._acap._acas._aj1-')
                if len(like_peoples) != 0:
                    break

            self.follow_loop(num)

    def like_stories(self, num):
        print('### Now start to like stories. ###')
        browser.get(url_main)
        browser.implicitly_wait(10)
        time.sleep(3)

        story = browser.find_elements(By.CLASS_NAME, '_aarf.x1e56ztr')[1]
        story.click()
        time.sleep(3)

        last_owner = ''
        for _ in range(num):
            now_owner = browser.find_element(By.CLASS_NAME, '_ac0l').text[:5]

            if last_owner != now_owner:
                like = browser.find_element(By.CLASS_NAME, '_abm0._abl_')
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

            if limit > 3:
                print(f'### There is no more feeds. Break loop. ###')
                break

            browser.get(url_main)
            time.sleep(3)
            print(f'like_feeds count : {_ + 1}')

        print('### Like stories is completed. ###')

    def manage_flw(self, num):
        print('### Now start to Manage followers. ###')
        self.get_list_unfl(num)
        list_unflw = self.list_unflw

        cnt = 0
        for _ in range(1, num+1):
            unflw = list_unflw[-2]
            browser.get(f'{url_main}{unflw}')
            time.sleep(1)

            buttons = browser.find_element(By.CLASS_NAME, '_acan._acap')
            if buttons.text == '?????????':
                buttons.click()
                time.sleep(1)

                button = browser.find_elements(By.CLASS_NAME, '_abm4')[-1]
                button.click()
                time.sleep(1)

                cnt += 1
                print(f'unfollow count : {cnt}')

            list_unflw.remove(unflw)

            if self.check in range(10):
                self.check_reqs_over(10, 30)
            elif self.check == 10:
                self.warn_reqs_over(30)
                break

        file = open(file_unfl, "w")
        [file.write(f'{i}\n') if i != '?????????' and i != '' else None for i in self.list_unflw]
        file.close()

        print('### Manage followers is completed. ###')

    def get_list_unfl(self, num):
        file = open(file_unfl, "r")
        data = file.read()
        self.list_unflw = list(data.split('\n'))
        file.close()

        if len(self.list_unflw) < num:
            self.my_cnt_flws()
            list_flwer = self.get_list_flwer()
            list_flwing = self.get_list_flwing()
            self.list_unflw = [i for i in list_flwing if i not in list_flwer]
            self.list_unflw = [i if i != '?????????' and i != '' else None for i in self.list_unflw]
            file = open(file_unfl, "w")
            [file.write(f'{i}\n') for i in self.list_unflw]
            file.close()
        else:
            pass

    def my_cnt_flws(self):
        browser.get(f'{url_main}{self.idd}')
        time.sleep(3)
        self.cnt_flwer = browser.find_elements(By.CLASS_NAME, '_ac2a')[1].text
        self.cnt_flwing = browser.find_elements(By.CLASS_NAME, '_ac2a')[2].text

    def get_list_flwer(self):
        browser.get(f'{url_main}{self.idd}/followers/')
        time.sleep(3)
        while True:
            pop_up = browser.find_element(By.CLASS_NAME, "_aano")
            browser.execute_script("arguments[0].scrollBy(0, 1000)", pop_up)  # ??????
            time.sleep(1)
            names = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aad7._aade')
            if len(names) >= int(self.cnt_flwer):
                list_flwer = [name.text for name in names][1:]
                break
        print(f'### followers : {len(list_flwer)} ###')
        return list_flwer

    def get_list_flwing(self):
        browser.get(f'{url_main}{self.idd}/following/')
        time.sleep(3)
        while True:
            pop_up = browser.find_element(By.CLASS_NAME, "_aano")
            browser.execute_script("arguments[0].scrollBy(0, 1000)", pop_up)  # ??????
            time.sleep(1)
            names = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aad7._aade')
            if len(names) > int(self.cnt_flwer)+100:
                list_flwing = [name.text for name in names][1:]
                break
        print(f'### followings sample : {len(list_flwing)} ###')
        return list_flwing


if __name__ == '__main__':
    insta = InstaManager(TAGS=True,
                         STORY=True,
                         FEED=True,
                         INFL=True,
                         UNFLW=False,
                         REPEAT=1)
    insta.process()