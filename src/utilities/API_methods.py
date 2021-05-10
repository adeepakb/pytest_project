import requests
import json
from constants.load_json import *
from constants.constants import CONFIG_PATH, Login_Credentials
import threading
import random
from utilities.common_methods import CommonMethods
from selenium.webdriver.common.by import By
import logging
import subprocess
import sys

CommonMethods = CommonMethods()

data_file = CONFIG_PATH

url = getdata(data_file, "API_credentials", "url")
params = {'key': getdata(data_file, "API_credentials", "key") , 'secret': getdata(data_file, "API_credentials", "secret")}


skipBtn_id = (By.ID, "com.byjus.thelearningapp:id/buttonSkip")
allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
mobile_num_field = (By.ID,"com.byjus.thelearningapp:id/etPhoneNumber")
country_code_field = (By.ID,"com.byjus.thelearningapp:id/drop_down_text_view")

def allow_notifications(browser):
        if CommonMethods.wait_for_element_visible(browser, allow_btn_id, 5):
            CommonMethods.accept_notification(browser, allow_btn_id)
            CommonMethods.accept_notification(browser, allow_btn_id)


def delete_deviceid(mobile_num):
#     mobile_num = str(mobile_num)
    query = """
            mutation{
            destroyDeviceId(mobileNo:\""""+mobile_num+"""\")
            {
            mobileDevices{
            deviceId
            }
        }
    }
    """
    resp = requests.post(url, json={'query': query}, params=params)
    print(resp.status_code)
    print(resp.json())
    
    
# def delete_all_registered_mobile_num(browser):
#     CommonMethods.run('adb shell pm clear com.byjus.thelearningapp')
#     CommonMethods.run('adb shell am start -n com.byjus.thelearningapp/com.byjus.app.onboarding.activity.SplashActivity')
#     allow_notifications(browser)
#     if CommonMethods.wait_for_element_visible(browser, skipBtn_id, 5):
#         logging.info("all the registered mobile is deleted")
#         CommonMethods.run('adb shell pm clear com.byjus.thelearningapp')
#         CommonMethods.run('adb shell am start -n com.byjus.thelearningapp/com.byjus.app.onboarding.activity.SplashActivity')
#     elif CommonMethods.wait_for_element_visible(browser, mobile_num_field, 5):
#         country_code = CommonMethods.getTextOfElement(browser, country_code_field)
#         mobile_number = CommonMethods.getTextOfElement(browser, mobile_num_field)
#         mobile_num = country_code+"-"+mobile_number
#         delete_deviceid(mobile_num)
#         delete_all_registered_mobile_num(browser)



mobile = '+91-2583697415'
mobile_number = "\""+mobile+"\""
delete_deviceid(mobile_number)        
        
def delete_single_registered_mobile_num(browser,mobile_num):
    delete_deviceid(mobile_num)
    CommonMethods.run('adb shell pm clear com.byjus.thelearningapp')
    CommonMethods.run('adb shell am start -n com.byjus.thelearningapp/com.byjus.app.onboarding.activity.SplashActivity')
    allow_notifications(browser)
    

