import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

import config
from decorators import social_login_required


class SocialNetworkScraper:

    BASE_URL = f"http://{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_PORT}"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    BLOG_URL = f"{BASE_URL}/user/blog"

    def __init__(self, driver=None):
        self.driver = driver or self.create_driver()
        self.is_logged_in = False

    def create_driver(self):
        """
        Create chrome driver instance
        """
        try:
            options = Options()
            options.add_argument("--start-maximized")

            self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, options=options)
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_login(self):
        """
        Log in to social-network
        """

        # create driver & navigate to login page
        self.driver.get(self.LOGIN_URL)

        # set username
        username_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        # set password
        password_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)

        # log-in by pressing Enter
        password_elem.send_keys(keys.Keys.ENTER)
        self.is_logged_in = True

    @social_login_required
    def social_network_add_post(self, title, content):
        """
        Create automated post on social-network
        """
        # navigate to user blog posts page
        self.driver.get(self.BLOG_URL)
        time.sleep(1)

        # set title
        title_elem = self.driver.find_element(By.ID, "title")
        title_elem.send_keys(title)
        time.sleep(1)

        # set content
        content_elem = self.driver.find_element(By.ID, "content")
        content_elem.send_keys(content)
        time.sleep(1)

        # click Create post button
        create_post_elem = self.driver.find_element(By.XPATH, "//form/button[@type='submit']")
        create_post_elem.click()
        time.sleep(1)

        return self.driver
