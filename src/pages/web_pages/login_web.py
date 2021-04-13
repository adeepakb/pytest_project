import logging
import pickle
import time
from selenium.common.exceptions import NoSuchElementException
from constants.load_json import getdata
from constants.constants import Login_Credentials
from pages.base.login_base import LoginBase
from utilities.common_methods import CommonMethods
from selenium.webdriver.common.keys import Keys


class LoginWeb(LoginBase):
    def __init__(self, driver):
        self.driver = driver
        self.phone_number = "//*[contains(@resource-id, 'etPhoneNumber')]"
        self.password = "//*[contains(@resource-id, 'etPassword')]"
        self.next_btn = "//*[contains(@resource-id, 'btnNext')]"
        self.login_btn = "//*[contains(@resource-id, 'btnLogin')]"
        self.Profile_rb = "//input[@type='radio']"
        self.rcmd_section = "//div[text()='Recommended Classes']"


    def navigate_to_home_screen(self):
        self.skip_login()
        # self.driver.get('https://learn-staging.byjus.com')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//span[text() = 'LOGIN']").click()
        time.sleep(10)

    def enter_phone(self):
        self.driver.find_element_by_xpath("//input[@id='enterNumber']").send_keys(getdata(Login_Credentials, 'login_detail5', 'mobile_no'))

    def click_on_next(self):
        self.driver.find_element_by_xpath("// div[text() = 'NEXT']").click()

    def select_profile(self):
        time.sleep(2)
        elements = self.driver.find_elements_by_xpath("//input[@type='radio']")
        elements[1].click()
        self.click_on_next()

    def enter_otp(self):
        # self.select_profile()
        # CommonMethods.wait_for_element_visible(self.driver, self.Profile_rb, 10)
        self.driver.find_element_by_xpath("//input[@id='enterPassNumber']").send_keys(getdata(Login_Credentials, 'login_detail5', 'OTP'))
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

    # This step is not applicable in web. Hence skipping this for web
    def tap_on_prem_card(self):
        pass

    def click_on_hamburger(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='J-hamburger-64']").click()

    def click_on_premium_school(self):
        self.driver.find_element_by_xpath("//div[text()='BYJU’S Classes']").click()

    def enter_phone_expired_user(self):
        self.driver.find_element_by_xpath("//input[@id='enterNumber']").send_keys(getdata(Login_Credentials, 'login_detail4', 'mobile_no'))

    def select_profile_expired_user(self):

        #CommonMethods.wait_for_element_visible(self.driver, self.Profile_rb, 10)
        elements = self.driver.find_elements_by_xpath("//input[@type='radio']")
        elements[1].click()
        self.click_on_next()

    def enter_otp_expired_user(self):
        time.sleep(10)
        self.driver.find_element_by_xpath("//input[@id='enterPassNumber']").send_keys(getdata(Login_Credentials, 'login_detail4', 'OTP'))
        self.click_on_next()

    def login_as_free_user(self):
        self.driver.get('https://learn-staging.byjus.com')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//span[text() = 'LOGIN']").click()
        self.enter_phone_expired_user()
        self.click_on_next()
        self.select_profile_expired_user()
        self.enter_otp_expired_user()


    def gmail_login(self):
        input = self.driver.find_element_by_xpath("//input[@id='identifierId']")
        input.send_keys("prasanth.c")
        time.sleep(3)
        #input.send_keys(Keys.TAB)
        input.send_keys(Keys.ENTER)
        time.sleep(5)
        input1 = self.driver.find_element_by_xpath("//input[@name='password']")
        input1.send_keys("Tnl@12345")
        input1.send_keys(Keys.ENTER)



    def start_tutor_session(self):

        # open the first window
        self.driver.get('https://tutor-plus-staging.tllms.com/')
        self.driver.find_element_by_xpath("//span[text()='LOGIN']").click()
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys("prasanth.c@byjus.com")
        self.driver.find_element_by_xpath("//button[text()='Sign In']").click()
        self.gmail_login()
        time.sleep(10)
        self.driver.find_element_by_xpath("(//a[text()='Schedule Page'])[1]").click()
        time.sleep(2)
        channel_ID = self.driver.find_element_by_xpath("//input[@placeholder = 'Search by Channel ID']")
        channel_ID.send_keys("149511")
        channel_ID.send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath("//input[@placeholder='Enter Teacher Email']").send_keys("prasanth.c@byjus.com")
        self.driver.find_element_by_xpath("(//span[text()='Submit'])[2]").click()
        time.sleep(4)
        channel_ID.send_keys("149511")
        channel_ID.send_keys(Keys.ENTER)
        #clickonmeetingurl
        self.driver.find_element_by_xpath("//a[text()='url']").click()
        # get the window handle after the window has opened
        window_before = self.driver.window_handles[0]

    # window_before_title = self.driver.title
    # print(window_before_title)
        self.driver.execute_script("window.open('', 'new window')")

    # get the window handle after a new window has opened
        window_after = self.driver.window_handles[1]

    # switch on to new child window
        self.driver.switch_to.window(window_after)
        time.sleep(10)

    def click_on_end_session(self):

        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_before)
        self.driver.find_element_by_xpath("//div[text()='Ends in ']").click()
        time.sleep(5)
        self.driver.switch_to.window(window_after)

    def save_login(self):

        with open("../../config/login_web.pkl", "wb") as fp:
            pickle.dump(self.driver.get_cookies(), fp)

    def skip_login(self):
        self.driver.get('https://learn-staging.byjus.com')
        with open("../../config/login_web.pkl", "rb") as fp:
            session = pickle.load(fp)
        [self.driver.add_cookie(s) for s in session]
        self.driver.refresh()

    def text_match(self):
        pass

    def button_click(self, text):
        pass

