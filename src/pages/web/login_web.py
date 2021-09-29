import logging
import pickle
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from constants.load_json import get_data
from pages.base.login_base import LoginBase
from constants.constants import Login_Credentials
from utilities.common_methods_web import CommonMethodsWeb
from utilities.staging_tllms import Stagingtllms
from utilities.staging_tlms import Stagingtlms


class LoginWeb(LoginBase):
    def __init__(self, driver):
        if driver is None:
            chrome_options = Options()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--use-fake-ui-for-media-stream")
            self.driver = webdriver.Chrome(options=chrome_options)
        else :
            self.driver = driver
        self.obj = CommonMethodsWeb(self.driver)
        self.LOGIN_DETAILS = '../../config/login_data.json'
        self.login_butn = (By.XPATH, "//span[text() = 'LOGIN']")
        self.phone_number = (By.XPATH, "//input[@id='enterNumber']")
        self.password = (By.XPATH, "//input[@id='enterPassNumber']")
        self.next_btn = "//*[contains(@resource-id, 'btnNext')]"
        self.login_btn = "//*[contains(@resource-id, 'btnLogin')]"
        self.Profile_rb = "//input[@type='radio']"
        self.rcmd_section = (By.XPATH, "//div[text()='Recommended Classes']")
        self.nxt_btn = (By.XPATH, "//div[text()='NEXT']")
        self.byjus_classes = (By.XPATH, "//div[text()='BYJU’S Classes']")
        self.hamburger = (By.XPATH, "//div[contains(@class,'ee-hamburger-')]")
        self.multiple_accnt = (By.XPATH, "//div[text()='Multiple Accounts']")
        self.profile = '//*[@value="VAL"]'
        self.profile_form = (By.XPATH, '//*[@id="form"]')
        self.PREMIUM_ID = 'premium_id'
        self.profiles = (By.XPATH,"//input[@class='profile-radio-button']")

    # This step is not applicable in web. Hence skipping this for web
    def click_on_premium_school(self):
        pass

    def launch_and_navigate_to_login_page(self):
        self.skip_login()
        # self.driver.get('https://learn-staging.byjus.com')
        self.driver.maximize_window()
        self.obj.element_click(self.login_butn)

    def enter_phone(self, mobile_num):
        self.obj.enter_text(mobile_num, self.phone_number)

    def click_on_next(self):
        self.obj.wait_for_element_visible(self.nxt_btn, 15)
        self.obj.element_click(self.nxt_btn)

    def select_profile(self, login_profile, user_profile, sub_profile):
        self.login_data = get_data(Login_Credentials, login_profile)
        self.profile_name = self.login_data[user_profile][sub_profile]["profile_value"]
        self.profile = self.profile.replace("VAL", self.profile_name)
        self.obj.wait_for_locator_webdriver('//*[@value="{}"]'.format(self.profile))
        element = self.obj.get_element((By.XPATH, self.profile))
        self.obj.wait_for_clickable_element_webdriver(element, 10)
        self.obj.get_element((By.XPATH, self.profile)).click()
        self.obj.element_click(self.nxt_btn)

    def select_third_profile(self):
        self.obj.wait_for_element_visible(self.nxt_btn, 15)
        elements = self.obj.get_elements(self.profiles)
        elements[2].click()
        print(elements)
        self.click_on_next()

    def enter_otp(self, cc, mobile_num, otp):
        if otp is None:
            otp = Stagingtlms(self.driver).get_otp(cc, mobile_num)
        self.obj.wait_for_element_visible(self.password, 10)
        self.obj.enter_text(otp, self.password)
        self.click_on_next()

    def verify_home_page_loaded(self):
        try:
            self.obj.wait_for_element_visible(self.byjus_classes, 5)
            element = self.obj.get_element(self.byjus_classes)
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
        self.obj.element_click(self.hamburger)

    def click_on_byjus_classes(self):
        self.obj.element_click(self.byjus_classes)

    def enter_phone_expired_user(self):
        self.driver.find_element_by_xpath("//input[@id='enterNumber']").send_keys(
            get_data(Login_Credentials, 'login_detail4', 'mobile_no'))

    def select_profile_expired_user(self):
        elements = self.driver.find_elements_by_xpath("//input[@type='radio']")
        elements[1].click()
        self.click_on_next()

    def enter_otp_expired_user(self):
        self.obj.wait_for_element_visible(self.password, 50)
        self.driver.find_element_by_xpath("//input[@id='enterPassNumber']").send_keys(
            get_data(Login_Credentials, 'login_detail4', 'OTP'))
        self.click_on_next()

    def login_as_free_user(self):
        self.driver.get('https://learn-staging.byjus.com')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//span[text() = 'LOGIN']").click()
        self.enter_phone_expired_user()
        self.click_on_next()
        self.select_profile_expired_user()
        self.enter_otp_expired_user()

    def verify_rcmnded_section_ispresent(self):
        try:
            self.obj.wait_for_element_visible(self.rcmd_section)
            self.driver.execute_script("window.scrollTo(0, 300)")
            element = self.obj.is_element_present(self.rcmd_section)
            if element is not None:
                return True
            else:
                logging.info("Element not found")
                return False
        except NoSuchElementException:
            return False

    def click_on_end_session(self):
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_before)
        self.driver.find_element_by_xpath("//div[text()='Ends in ']").click()
        self.obj.wait(5)
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

    def button_click(self):
        pass

    def navigate_to_home_screen(self, login_profile, user_profile, sub_profile):
        self.driver.get('https://learn-staging.byjus.com')
        self.driver.maximize_window()
        self.obj.element_click(self.login_butn)
        phone_num = get_data(Login_Credentials, 'login_detail5', 'mobile_no')
        self.enter_phone(phone_num)
        self.click_on_next()
        self.select_profile(login_profile, user_profile, sub_profile)
        self.enter_otp('+91-', phone_num, '1089')

    def navigate_to_one_to_many_and_mega_user(self):
        pass

    def set_user_profile(self, login_profile='login_detail5', user_profile='user_1', sub_profile='profile_1'):
        self.login_data = get_data(Login_Credentials, login_profile)
        self.user_mobile = self.login_data[user_profile]["mobile_number"]
        self.profile_name = self.login_data[user_profile][sub_profile]["profile_name"]
        self.otp = self.login_data[user_profile]["OTP"]
        self.premium_id = self.login_data[user_profile][sub_profile]["premium_id"]
        return self

    def get_premium_id(self, profile='login_detail5', user_profile=None, ):
        self.set_user_profile(profile, user_profile)
        login_data = self.LOGIN_DETAILS
        m, i = self.user_mobile, self.premium_id
        if i is None:
            with open(login_data, "r+") as io_write:
                data = json.load(io_write)
                io_write.seek(0)
                user = data[profile][user_profile]
                user.update({self.PREMIUM_ID: Stagingtllms._pid(m)})
                json.dump(data, io_write, indent=4)
            return user[self.PREMIUM_ID], True
        return i, False

    def login_and_navigate_to_home_screen(self, cc, phone_num, otp):
        self.driver.get('https://learn-staging.byjus.com')
        self.driver.maximize_window()
        self.obj.wait_for_element_visible(self.login_butn)
        self.obj.element_click(self.login_butn)
        self.enter_phone(phone_num)
        self.click_on_next()
        self.enter_otp(cc, phone_num, otp)

    def get_profile_details(self):
        profile_details = {}
        profile_items = self.obj.get_elements(('xpath', "//*[contains(@class,'Connect(t)-label')]"))
        mid = int(len(profile_items) / 2)
        for i in range(mid):
            profile_details.update({profile_items[i], profile_items[i + 1]})
        return profile_details


    def login_for_neo_class_mweb(self, cc, phone_num, otp):
        self.driver.get('https://learn-staging.byjus.com')
        self.driver.set_window_size(1280, 800)
        size = self.driver.get_window_size()
        print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
        self.obj.element_click(self.login_butn)
        self.enter_phone(phone_num)
        self.click_on_next()
        self.enter_otp(cc, phone_num, otp)

