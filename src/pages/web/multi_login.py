import logging
import pickle
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from constants.load_json import get_data
from pages.base.login_base import LoginBase
from constants.constants import Login_Credentials
from utilities.common_methods_web import CommonMethodsWeb
from selenium.webdriver.chrome.options import Options
from utilities.staging_tllms import Stagingtllms
from utilities.staging_tlms import Stagingtlms


class MultiLogin:

    def __init__(self, driver):
        self.driver = driver
        self.obj = CommonMethodsWeb(driver)
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--no-sandbox')
        # self.chrome_options.add_argument('--headless')
        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
        # key = os.getenv('SECRET')
        # f = Fernet(key)
        # encrypted_data = get_data('../config/config.json', 'encrypted_data', 'token')
        # self.decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))


    def login_and_navigate_to_home_screen(self, cc, phone_num, otp):
        self.driver.get('https://learn-staging.byjus.com')
        self.driver.maximize_window()
        self.obj.element_click(self.login_butn)
        self.enter_phone(phone_num)
        # self.obj.enter_text(mobile_num, self.phone_number)
        # self.click_on_next()
        # self.enter_otp(cc, phone_num, otp)