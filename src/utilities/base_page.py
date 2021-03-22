from time import sleep
from urllib3.exceptions import MaxRetryError
from constants.constants import CONFIG_PATH
from constants.load_json import *
from selenium.webdriver.chrome.options import Options
from appium.webdriver import Remote
from selenium.webdriver import Chrome


class BaseClass:

    @staticmethod
    def setup_android():
        desired_caps = dict()
        retry, error = 3, None
        desired_cap = CONFIG_PATH
        data = getdata(desired_cap, 'desired_cap')
        imp_wait, command_executor = data.pop("implicitWait"), data.pop("url")
        desired_caps.update(data)
        while retry:
            try:
                driver = Remote(command_executor, desired_caps)
                driver.implicitly_wait(imp_wait)
                return driver
            except MaxRetryError as e:
                error = e
                retry -= 1
                sleep(1)
        if not retry:
            raise error

    @staticmethod
    def setup_browser():
        chrome_options = Options()
        driver = Chrome(options=chrome_options)
        return driver
