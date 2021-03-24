import logging
import time
from selenium.common.exceptions import NoSuchElementException
from pages.base.student_session_base import StudentSessionBase


class StudentSessionWeb(StudentSessionBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
