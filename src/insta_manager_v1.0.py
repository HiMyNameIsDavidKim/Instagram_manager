from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


class InstaManager(object):
    def __init__(self):
        global url_chr, browser, url_login
        url_chr = r'../lib/chromedriver.exe'
        browser = webdriver.Chrome(url_chr)
        url_login = r'https://www.instagram.com/accounts/login/'
        self.id = ''
        self.pw = ''

    def process(self):
        self.login()
        self.laters()

    def id_n_pw(self):
        self.id = input('please input ID : ')
        self.pw = input('please input PW : ')
        return self.id, self.pw

    def login(self):
        browser.get(url_login)
        time.sleep(1)

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