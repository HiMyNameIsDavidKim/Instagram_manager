from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from random import randrange
from bs4 import BeautifulSoup


class InstaManager(object):
    def __init__(self, TAGS=False, INFL=False):
        global browser, url_login, url_tags, url_infl, file_idpw, file_tags, file_infl
        browser = webdriver.Chrome()
        url_login = 'https://www.instagram.com/accounts/login/'
        url_tags = "https://www.instagram.com/explore/tags/"
        url_infl = "https://www.instagram.com/"
        file_idpw = r"/Users/davidkim/security/insta_nir.txt"
        file_tags = r"/Users/davidkim/security/insta_tags.txt"
        file_infl = r"/Users/davidkim/security/insta_infl.txt"
        self.TAGS = TAGS
        self.INFL = INFL

    def process(self):
        self.login()
        self.laters()
        if self.TAGS:
            self.follow_by_tags()
        if self.INFL:
            self.follow_by_infl()
        self.logout()
        browser.quit()

    def id_n_pw(self):
        file = open(file_idpw, "r")
        data = file.read()
        id, pw = tuple(data.split('\n'))
        print('### id and pw is uploaded. ###')
        return id, pw

    def login(self):
        browser.get(url_login)
        browser.implicitly_wait(10)

        id, pw = self.id_n_pw()
        click = browser.find_elements(By.TAG_NAME, 'input')
        click[0].send_keys(id)
        click[1].send_keys(pw)
        click[1].send_keys(Keys.RETURN)
        print('### Login is completed. ###')
        time.sleep(5)

    def logout(self):
        prof = browser.find_element(By.CLASS_NAME, '_aaav')
        prof.click()
        logout = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacu._aacx._aada')[-1]
        logout.click()
        print('### Logout is completed. ###')

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
        for _ in range(100):
            like_people = browser.find_elements(By.CLASS_NAME, '_acan._acap._acas._aj1-')[-1]
            if like_people.text == '팔로우' and count < num:
                like_people.send_keys(Keys.ENTER)
                count += 1
                time.sleep(3)
        print('### Follow loop is completed. ###')

    def follow_by_tags(self):
        print('### Now start to follow by tags. ###')
        file = open(file_tags, "r")
        data = file.read()
        tags = list(data.split('\n'))
        for tag in tags:
            browser.get(url_tags + tag)
            time.sleep(3)

            self.follow_feed_liker(5)

    def follow_feed_liker(self, num):
        feed = browser.find_elements(By.CLASS_NAME, "_aagw")
        feed[0].click()
        time.sleep(3)

        likes = browser.find_element(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aada._aade')
        likes.click()
        time.sleep(3)

        self.follow_loop(num)

    def follow_by_infl(self):
        print('### Now start to follow by influencers. ###')
        file = open(file_infl, "r")
        data = file.read()
        infls = list(data.split('\n'))
        for infl in infls:
            browser.get(url_infl + infl)
            time.sleep(3)

            self.follow_followers(5)

    def follow_followers(self, num):
        followers = browser.find_elements(By.CLASS_NAME, '_aacl._aaco._aacu._aacy._aad6._aadb._aade')[1]
        followers.click()
        time.sleep(3)

        self.follow_loop(num)


if __name__ == '__main__':
    insta = InstaManager()
    insta.process()