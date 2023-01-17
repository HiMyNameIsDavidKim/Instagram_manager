from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


class InstaManager(object):
    def __init__(self):
        global browser, url_login
        browser = webdriver.Chrome()
        url_login = r'https://www.instagram.com/accounts/login/'
        self.id = ''
        self.pw = ''

    def process(self):
        self.login()
        self.laters()
        browser.quit()

    def id_n_pw(self):
        file = open(r"/Users/davidkim/security/insta_nir.txt", "r")
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


if __name__ == '__main__':
    insta = InstaManager()
    insta.process()