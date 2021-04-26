
from selenium.common.exceptions import NoSuchElementException
import logging
import time
from pages.base.ps_home_screen_base import PSHomeScreenBase


class PSHomescreenWeb(PSHomeScreenBase):
    def __init__(self, driver):
        self.driver = driver