import json
import os

from cryptography.fernet import Fernet
from selenium.webdriver import ActionChains

from constants.load_json import get_data
from utilities.neo_tute_mentoring import NeoTute
from selenium.webdriver.chrome.options import  Options
from selenium import webdriver

from utilities.staging_tlms import Stagingtlms


class NeoTutot(NeoTute):
    def __init__(self, driver):
        self.driver = driver
        # self.tlms = Stagingtlms(driver)
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--no-sandbox')
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
        self.chrome_driver1 = webdriver.Chrome(options=self.chrome_options)
        self.tlms = Stagingtlms(self.chrome_driver1)
        self.chrome_driver_tlms = self.tlms.chrome_driver
        key = os.getenv('SECRET')
        f = Fernet(key)
        encrypted_data = get_data('../config/config.json', 'encrypted_data', 'token')
        self.decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))
        self.chrome_driver = webdriver.Chrome(chrome_options=self.chrome_options)
        super().__init__(self.chrome_driver)
        self.action = ActionChains(self.chrome_driver)
