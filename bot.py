from selenium import webdriver
from util_methods.util_methods import *
import os
import time

class InstaBot:

    def __init__(self, username=None, pwd=None):
        """
        Initialize Instabot object and calls login method 

        Args:
            username:str: instagram account's username 
            pwd:str: instagram account's password

        Attributes:
            login_url:str: url for login page
            user_url:str: url for instagram user 
            tag_url:str:url for hashtag
            driver:Selenium.webdriver.Chrome: Chromedriver that automates brower actions
        """

        self.username = config['AUTH']['username']
        self.pwd = config['AUTH']['password']

        self.login_url = config['URLS']['login']
        self.user_url = config['URLS']['nav_user_url']
        self.tag_url = config['URLS']['hash_tag_url']

        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")

        self.login()

    def login(self):
        """Logs user in using username and password"""

        self.driver.get(self.login_url)

        time.sleep(1)

        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.pwd)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button").click()

        time.sleep(3)

    def save_info(self):
        """
        If the option to save username and pwd pops up when logging in, the 'Not Now' option is pressed
        """
        not_now_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")[0]

        not_now_button.click()

    def notifs(self):
        """
        If the option to turn on notification pops up when logging in, the 'Not Now' option in pressed
        """
        not_now_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")[0]

        not_now_button.click()

    def nav_user(self, user):
        """
        Navigates to user instagram profile

        Args:
            user:str: username to search
        """
        self.driver.get(self.user_url.format(user))

    def follow(self, user):
        """
        Follows instagram user

        Args:
            user:str: username to follow
        """
        self.nav_user(user)

        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]

        follow_button.click()

    def unfollow(self, user):
        """
        Unfollows instagram user

        Args:
            user:str: username to unfollow
        """
        self.nav_user(user)

        following_button = self.driver.find_element_by_class_name("glyphsSpriteFriend_Follow")
        following_button.click()

        unfollow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")[0]
        unfollow_button.click()

    def scroll(self):
        timeout = time.time() + 10
        page_start = 0

        while time.time() < timeout: 
            self.driver.execute_script("window.scrollTo({}, {})".format(str(page_start), str(page_start+4)))
            page_start+=4
        

if __name__ == "__main__":
    config_file_path = './config.ini'
    config = init_config(config_file_path)
    ig_bot = InstaBot()
    ig_bot.save_info()
    ig_bot.notifs()
    ig_bot.scroll()
    ig_bot.follow("harrystyles")
    ig_bot.unfollow("harrystyles")
