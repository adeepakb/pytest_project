import sys
import os
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from utilities.interrupt import *
from utilities.common_methods import CommonMethods

featureFileName = "Question screen"
CommonMethods = CommonMethods()


class RevisitScreen():


    def __init__(self, driver):
        self.driver = driver