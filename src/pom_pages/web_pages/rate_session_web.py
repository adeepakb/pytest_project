import logging
import time
from selenium.common.exceptions import NoSuchElementException



class RateSessionWeb():
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
