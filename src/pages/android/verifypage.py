'''to verify the registered user or enterning the otp'''
import sys
import os

from appium import webdriver

from constants.load_json import *
from utilities.common_methods import CommonMethods


class VerifyPage():

    def __init__(self, driver):
        
        self.verify_pag = "com.byjus.thelearningapp:id/touch_outside"
        self.txt_otp = "com.byjus.thelearningapp:id/etOTP"
        self.verifyText_xpath = "//android.widget.TextView[@text='Verify']"
        self.otp1 = get_data(PATH('../test_data/login_data.json'), "login_details", "OTP")
        
    def clickOnVerifyPage(self, driver):
        driver.find_element_by_id(self.verify_pag).click()
        
#     def enterOtp(self,driver):
#         sleep(15)
#         run("adb shell input text "+otp+"")
# #         otpcode=driver.find_element_by_id(self.txt_otp)
# #         otpcode.send_keys(getdata(PATH('../test_data/login_data.json'),"login_details","OTP"))
# 
#     def demo(self):
#         Pass

