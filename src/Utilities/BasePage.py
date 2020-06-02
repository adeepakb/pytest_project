import logging
import datetime
from Constants.constants import CONFIG_PATH
from Constants.load_json import *
from appium import webdriver


'''this class is used for starting appium and  launching App & getting the  Appium driver for all the test files '''

class BaseClass:
    
    '''this will start appium server automatically'''   
    
    def driverSetup(self):
        desired_caps = {}

        desiredCap = CONFIG_PATH
        desired_caps['platformName'] = getdata(desiredCap, 'desired_cap', 'platformName')
        try:
            desired_caps['udid'] = getdata(desiredCap, 'desired_cap', 'udid')
        except KeyError:
            pass
        desired_caps['deviceName'] = getdata(desiredCap, 'desired_cap', 'deviceName')
        desired_caps['appPackage'] = getdata(desiredCap, 'desired_cap', 'appPackage')
        desired_caps['appActivity'] = getdata(desiredCap, 'desired_cap', 'appActivity')
        desired_caps['eventTimings'] = getdata(desiredCap, 'desired_cap', 'eventTimings')
        desired_caps['noReset'] = getdata(desiredCap, 'desired_cap', 'noReset')
        driver = webdriver.Remote(getdata(desiredCap, 'desired_cap', 'url'), desired_caps)
        driver.implicitly_wait(getdata(desiredCap, 'desired_cap', 'implicitWait'))
        return driver

    def setupLogs(self,featureFileName):
        date_Time = datetime.datetime.now()
        dateTime = date_Time.strftime("%d-%m-%y, %H-%M-%S")
        logging.basicConfig(filename='App_logs/TestLogs/'+featureFileName+" "+dateTime+".log", filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
#         logging.basicConfig(filename='../../App_logs/TestLogs/'+featureFileName+" "+dateTime+".log", filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    
