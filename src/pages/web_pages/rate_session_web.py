import logging
import time
from selenium.common.exceptions import NoSuchElementException



class RateSessionWeb():
    def __init__(self, driver):
        self.driver = driver