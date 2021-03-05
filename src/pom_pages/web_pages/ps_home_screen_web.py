import logging
import time
from selenium.common.exceptions import NoSuchElementException
from Constants.load_json import getdata
from POM_Pages.Base_Pages.LoginBase import LoginBase
from Constants.constants import Login_Credentials


class PSHomescreenWeb(LoginBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
