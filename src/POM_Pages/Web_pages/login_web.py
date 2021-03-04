import logging
import time
from selenium.common.exceptions import NoSuchElementException
from Constants.load_json import getdata
from POM_Pages.Base_Pages.LoginBase import LoginBase
from Constants.constants import Login_Credentials


class LoginWeb(LoginBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
        self.phone_number = "//*[contains(@resource-id, 'etPhoneNumber')]"
        self.password = "//*[contains(@resource-id, 'etPassword')]"
        self.next_btn = "//*[contains(@resource-id, 'btnNext')]"
        self.login_btn = "//*[contains(@resource-id, 'btnLogin')]"

    def implicit_wait_for(self, pool):
        self.driver.implicitly_wait(pool)

    def click_on_premium_school(self):
        self.driver.find_element_by_xpath("//div[@class='P-hamburger-64']").click()
        self.driver.find_element_by_xpath("//div[text()='BYJU’S Classes']").click()

    def launch_and_navigate_to_login_page(self):
        self.driver.get('https://learn-staging.byjus.com')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//span[text() = 'LOGIN']").click()

    def enter_phone(self):
        self.driver.find_element_by_xpath("//input[@id='enterNumber']").send_keys(getdata(Login_Credentials, 'login_detail3', 'mobile_no'))

    def click_on_next(self):
        self.driver.find_element_by_xpath("// div[text() = 'NEXT']").click()

    def select_profile(self):
        elements = self.driver.find_elements_by_xpath("//input[@type='radio']")
        elements[1].click()
        self.click_on_next()

    def enter_otp(self):
        self.select_profile()
        time.sleep(10)
        self.driver.find_element_by_xpath("//input[@class='inputEleOTP']").send_keys(getdata(Login_Credentials, 'login_detail3', 'OTP'))
        self.click_on_next()

    def verify_home_page_loaded(self):
        try:
            time.sleep(4)
            element = self.driver.find_element_by_xpath("//div[text()='Byju’s Classes']")
            if element is not None:
                return True
            else:
                logging.info("Element not found")
                return False
        except (NoSuchElementException):
            return False