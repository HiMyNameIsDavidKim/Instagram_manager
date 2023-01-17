from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


class InstaManager(object):
    def __init__(self):
        global browser, url_login, url_tags, file_idpw, file_tags
        browser = webdriver.Chrome()
        url_login = r'https://www.instagram.com/accounts/login/'
        url_tags = "https://www.instagram.com/explore/tags/"
        file_idpw = r"/Users/davidkim/security/insta_nir.txt"
        file_tags = r"/Users/davidkim/security/insta_tags.txt"
        self.id = ''
        self.pw = ''

    def process(self):
        self.login()
        self.laters()
        self.follow_by_tags()
        browser.quit()

    def id_n_pw(self):
        file = open(file_idpw, "r")
        data = file.read()
        self.id, self.pw = tuple(data.split('\n'))
        return self.id, self.pw

    def login(self):
        browser.get(url_login)
        browser.implicitly_wait(10)

        id, pw = self.id_n_pw()
        click = browser.find_elements(By.TAG_NAME, 'input')
        click[0].send_keys(id)
        click[1].send_keys(pw)
        click[1].send_keys(Keys.RETURN)
        time.sleep(5)

    def laters(self):
        btn_later1 = browser.find_element(By.CLASS_NAME, '_acan._acao._acas')
        btn_later1.click()
        time.sleep(5)
        btn_later2 = browser.find_element(By.CLASS_NAME, '_a9--._a9_1')
        btn_later2.click()
        time.sleep(5)

    def follow_by_tags(self):
        file = open(file_tags, "r")
        data = file.read()
        tags = list(data.split('\n'))
        for tag in tags:
            browser.get(url_tags + tag)
            time.sleep(5)

            self.follow_feed_liker()

    def follow_feed_liker(self):
        feed = browser.find_elements(By.CLASS_NAME, "_aagw")
        feed[0].click()
        time.sleep(3)

        likes = browser.find_element(By.CLASS_NAME, '_aacl._aaco._aacw._aacx._aada._aade')
        likes.click()
        time.sleep(3)

        count = 0
        for _ in range(100):
            like_people = browser.find_element(By.CLASS_NAME, '_acan._acap._acas._aj1-')
            if like_people.text == '팔로우' and count < 5:
                like_people.send_keys(Keys.ENTER)
                count += 1
                time.sleep(3)


if __name__ == '__main__':
    insta = InstaManager()
    insta.process()