import re
import subprocess
from time import sleep
from cryptography.fernet import Fernet
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
        key = os.getenv('SECRET')
        f = Fernet(key)
        encrypted_data = get_data(desired_cap, 'encrypted_data', 'token')
        decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))
        data = decrypted_data['desired_cap']
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
    def get_current_app_version():
        stdout, stderr = subprocess.Popen(
            'adb shell dumpsys package com.byjus.thelearningapp.premium | grep versionCode',
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        output = stdout.decode("ascii")
        app_version = re.search(r'^.*?\bversionCode=(\d+)', output).group(1)
        return app_version

    @staticmethod
    def setup_browser():
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--use-fake-device-for-media-stream")
        driver = Chrome(options=chrome_options)
        return driver
