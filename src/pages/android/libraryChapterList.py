import sys
import os
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import inspect
from selenium.webdriver.common.by import By
import logging
import pytest
from pyparsing import Char
from selenium.webdriver.support.wait import WebDriverWait
# from appium.webdriver.webelement import MobileBy
from utilities.common_methods import CommonMethods
from constants.load_json import get_data

featureFileName = "Personalized chapter list screen"

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

sys.path.append(PATH("../constants/"))

# import load_json
# from load_json import getdata

# CommonMethods = CommonMethods()


class LibraryChapterList(CommonMethods):
    
    def __init__(self, driver):
        self.driver = driver
        self.frame_trendingjourneycard_xpath = "//android.widget.LinearLayout[@instance='6']"
        
