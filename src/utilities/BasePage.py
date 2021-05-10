import logging
import datetime
from cryptography.fernet import Fernet
from constants.load_json import *
from appium import webdriver as AppiumDriver
from selenium import webdriver as ChromeDriver
from selenium.webdriver.chrome.options import Options

'''this class is used for starting appium and  launching App & getting the  Appium driver for all the test files '''


class BaseClass:
    '''this will start appium server automatically'''

    def setup_android(self):
        key = os.getenv('SECRET')
        f = Fernet(key)
        encrypted_data = getdata('../config/config.json', 'encrypted_data', 'token')
        decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))

        desired_caps = {}
        desired_caps['platformName'] = decrypted_data['desired_cap']['platformName']
        try:
            desired_caps['udid'] = decrypted_data['desired_cap']['udid']
        except KeyError:
            pass
        desired_caps['deviceName'] = decrypted_data['desired_cap']['deviceName']
        desired_caps['appPackage'] = decrypted_data['desired_cap']['appPackage']
        desired_caps['appActivity'] = decrypted_data['desired_cap']['appActivity']
        desired_caps['eventTimings'] = decrypted_data['desired_cap']['eventTimings']
        desired_caps['autoAcceptAlerts'] = decrypted_data['desired_cap']['autoAcceptAlerts']
        desired_caps['newCommandTimeout'] = decrypted_data['desired_cap']['newCommandTimeout']
        desired_caps['noReset'] = decrypted_data['desired_cap']['noReset']
        driver = AppiumDriver.Remote(decrypted_data['desired_cap']['url'], desired_caps)
        driver.implicitly_wait(decrypted_data['desired_cap']['implicitWait'])
        return driver

    def setup_browser(self):
        chrome_options = Options()
        driver = ChromeDriver.Chrome(options=chrome_options)
        return driver

    def setupLogs(self, featureFileName):
        date_Time = datetime.datetime.now()
        dateTime = date_Time.strftime("%d-%m-%y, %H-%M-%S")
        # logging.basicConfig(filename='App_logs/TestLogs/'+featureFileName+" "+dateTime+".log", filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.basicConfig(filename='../../App_logs/TestLogs/' + featureFileName + " " + dateTime + ".log",
                            filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
