import logging
import pickle
import time
from selenium.common.exceptions import NoSuchElementException
from constants.load_json import get_data
from constants.constants import Login_Credentials
from pages.base.login_base import LoginBase
from utilities.common_methods import CommonMethods
from selenium.webdriver.common.keys import Keys


class LoginWeb(LoginBase):
    def __init__(self, driver):
        self.driver = driver
