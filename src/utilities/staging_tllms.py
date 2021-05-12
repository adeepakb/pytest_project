import os
import sys
from random import randint
from selenium.webdriver import ActionChains
import json
import pickle
import random
import re
import time
import warnings
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSessionIdException, \
    StaleElementReferenceException, ElementNotInteractableException, SessionNotCreatedException, \
    NoAlertPresentException, UnableToSetCookieException, InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from utilities.tutor_common_methods import TutorCommonMethods
from constants.load_json import get_data
from selenium.webdriver.chrome.options import Options
from utilities.exceptions import *
from datetime import datetime , timedelta



class Stagingtllms(TutorCommonMethods):

    def __init__(self, driver):
        self.driver = driver
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument(f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                         f'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36')
        # self.chrome_options.add_argument("--window-size=1600,900")
        try:
            with open("../../config/chrome_session.json", "r") as fp:
                chrome_session = json.load(fp)
        except FileNotFoundError:
            chrome_session = None
        if not chrome_session:
            self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
            _d = {'session_url': self.chrome_driver.service.service_url, 'session_id': self.chrome_driver.session_id}
            with open("../../config/chrome_session.json", "w") as fp:
                json.dump(_d, fp)
        else:
            self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
            self.chrome_driver.quit()
            self.chrome_driver.command_executor._url = chrome_session["session_url"]
            self.chrome_driver.session_id = chrome_session["session_id"]
        super().__init__(driver)
        self.__init()

    def __const(self, sub_profile_type='primary'):
        self.TUTOR_PLUS_CMS_URL = 'https://tutor-plus-cms-staging.tllms.com/'
        self.STAGING_TLLMS_URL = 'https://staging.tllms.com/admin/'
        self.ATTACHMENT_DETAILS = '../../config/attachments.json'
        self.LOGIN_DETAILS = '../../config/login_data.json'
        self.REQUISITE_DETAILS = '../../config/ps_requisite.json'
        self.EMAIL = str(get_data('../../config/config.json', 'staging_access', 'email'))
        self.PASSWORD = str(get_data('../../config/config.json', 'staging_access', 'password'))
        self.IN_REQ = 'in_req'
        self.POST_REQ = 'post_req'
        self.PRE_REQ = 'pre_req'
        self.ALL_PRE_POST_REQ = 'all_pre_post'
        self.PROFILE = 'login_details_3'
        self.MOBILE = 'mobile_number'
        self.USER = 'profile_name'
        self.PREMIUM_ID = 'premium_id'
        self.OTP = 'OTP'

    def __init(self):
        self.__const()
        self.wait = WebDriverWait(self.chrome_driver, timeout=30)
        self.url_session_user_wise = self.STAGING_TLLMS_URL + 'student_sessions/#scheduling-sessions-user-wise'
        try:
            self.premium_id = str(get_data('../../config/config.json', 'profile_credentials', 'premium_id'))
        except KeyError:
            pass
        self.today = datetime.today().strftime('%Y-%m-%d')

    def save_session(self):
        self.chrome_driver.find_element(By.CSS_SELECTOR, 'img[src]')
        self.chrome_driver.get_screenshot_as_file("view.png")
        with open('../../config/login.pkl', 'wb') as io_write:
            pickle.dump(self.chrome_driver.get_cookies(), io_write)

    def login_to_staging(self, cms_login=None):
        self.chrome_driver.implicitly_wait(30)
        email = self.EMAIL
        password = self.PASSWORD
        retry = 3
        current_url = None
        try:
            if cms_login:
                self.chrome_driver.get(self.TUTOR_PLUS_CMS_URL)
                self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
                self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
            else:
                self.chrome_driver.get(self.STAGING_TLLMS_URL)
            self.wait_for_locator_webdriver("//input[@id='email']")
            self.chrome_driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
            self.wait_for_locator_webdriver("//button[@type='submit']")
            self.chrome_driver.find_element_by_xpath("//button[@type='submit']").click()
            self.wait_for_locator_webdriver("//input[@type='email']")
            self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
            self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(Keys.ENTER)
            self.wait_for_clickable_element_webdriver("//input[@type='password']")
            self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
            self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(Keys.ENTER)
        except NoSuchElementException:
            self.chrome_driver.get_screenshot_as_file("failed.png")
            raise
        while retry:
            current_url = self.chrome_driver.current_url
            if "tllms.com" in current_url:
                return self
            retry -= 1
            sleep(0.5)
        try:
            os.mkdir("screenshots")
        except FileExistsError:
            pass
        date_month = datetime.now().strftime("%H%M%S_%d%m%Y")
        file_name = "../../test_data/screenshots/failed_%s.png" % date_month
        self.chrome_driver.get_screenshot_as_file(file_name)
        raise InvalidSessionURL(f"unusual redirect to '{current_url}'.")

    def get_tutor_url(self, course='primary', premium_id='primary'):
        email = str(get_data('../config/config.json', 'staging_access', 'email'))
        today = datetime.today().strftime('%Y-%m-%d')
        if course == 'primary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_primary'))
            premium_id = str(get_data('../config/config.json', 'account_details', 'premium_id'))
        elif course == 'secondary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_secondary'))
            premium_id = str(get_data('../config/config.json', 'account_details', 'premium_id'))
        elif course == 'ternary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail1', 'course_id'))
            premium_id = str(get_data('../config/login_data.json', 'login_detail1', 'premium_id'))

        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//*[text()='Mentoring']")
        self.chrome_driver.find_element_by_xpath("//*[text()='Mentoring']").click()
        self.wait_for_clickable_element_webdriver("//*[text()='1:M - Schedule Student Sessions']")
        self.chrome_driver.find_element_by_xpath("//*[text()='1:M - Schedule Student Sessions']").click()

        self.wait_for_locator_webdriver("//a[text()='Scheduling Sessions(User Wise)']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Scheduling Sessions(User Wise)']").click()
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver("//input[@id ='target_date']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='target_date']").send_keys(today)
        self.wait_for_locator_webdriver("//input[@id ='premium_account_id']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='premium_account_id']").send_keys(premium_id)
        self.wait_for_locator_webdriver("//input[@value ='Start Scheduling']")
        self.chrome_driver.find_elements_by_xpath("//input[@value ='Start Scheduling']")[1].click()

        tutor_url = None
        rows = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/tbody/tr"))
        cols = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/thead/tr/th"))

        email_col = meeting_col = 8
        tagged_col = status_col = None
        for i in range(1, cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'index_table')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'Teaching Material/Video Tagged':
                tagged_col = i
            elif header == 'Status':
                status_col = i

        for r in range(1, rows + 1):
            try:
                status = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(status_col) + "]").text
                # incase of multiple sessions in same day
                course_details = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(tagged_col) + "]/div[@class='course_details']").text
                course_id = re.search(r'^.*?\bCourse id : (\d+)', course_details).group(1)
                if 'one_to_mega' in status and course_id == session_course_id:
                    self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        email_col) + "]/li[@id='teacher_email_input']/input[@id='teacher_email']").clear()
                    self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        email_col) + "]/li[@id='teacher_email_input']/input[@id='teacher_email']").send_keys(email)
                    tutor_url = self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        meeting_col) + "]/li[@id='meeting_url_input']/input[@id='meeting_url']").get_attribute('value')
                    break

            except NoSuchElementException:
                continue

        self.chrome_driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
        self.chrome_driver.save_screenshot("image1.png")
        self.chrome_driver.close()
        return tutor_url

    def reset_session(self, course='primary'):
        premium_id = str(get_data('../config/config.json', 'account_details', 'premium_id'))
        today = datetime.today().strftime('%Y-%m-%d')
        if course == 'primary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_primary'))
            premium_id = str(get_data('../config/config.json', 'account_details', 'premium_id'))
        elif course == 'secondary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_secondary'))
            premium_id = str(get_data('../config/config.json', 'account_details', 'premium_id'))
        elif course == 'ternary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail1', 'course_id'))
            premium_id = str(get_data('../config/login_data.json', 'login_detail1', 'premium_id'))

        self.login_to_staging()
        self.chrome_driver.save_screenshot("image.png")
        self.wait_for_clickable_element_webdriver("//*[text()='Mentoring']")
        self.chrome_driver.find_element_by_xpath("//*[text()='Mentoring']").click()
        self.chrome_driver.save_screenshot("image1.png")
        self.wait_for_clickable_element_webdriver("//*[text()='1:M - Schedule Student Sessions']")
        self.chrome_driver.find_element_by_xpath("//*[text()='1:M - Schedule Student Sessions']").click()
        self.chrome_driver.save_screenshot("image2.png")

        self.wait_for_locator_webdriver("//a[text()='Scheduling Sessions(User Wise)']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Scheduling Sessions(User Wise)']").click()
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver("//input[@id ='target_date']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='target_date']").send_keys(today)
        self.wait_for_locator_webdriver("//input[@id ='premium_account_id']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='premium_account_id']").send_keys(premium_id)
        self.wait_for_locator_webdriver("//input[@value ='Start Scheduling']")
        self.chrome_driver.find_elements_by_xpath("//input[@value ='Start Scheduling']")[1].click()

        rows = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/tbody/tr"))
        cols = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/thead/tr/th"))
        reset_col = 10
        tagged_col = status_col = None
        for i in range(1, cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'index_table')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'Teaching Material/Video Tagged':
                tagged_col = i
            elif header == 'Status':
                status_col = i

        for r in range(1, rows + 1):
            try:
                status = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(status_col) + "]").text
                # incase of multiple sessions in same day
                course_details = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(tagged_col) + "]/div[@class='course_details']").text
                course_id = re.search(r'^.*?\bCourse id : (\d+)', course_details).group(1)
                if 'one_to_mega' in status and course_id == session_course_id:
                    self.chrome_driver.find_element_by_xpath(
                        "//tr[" + str(r) + "]/td[" + str(reset_col) + "]/a[text()= 'Reset']").click()
                    break
            except NoSuchElementException:
                continue
        self.chrome_driver.close()

    def get_mobile_and_ccode(self, profile='login_details_3', user_profile='user_1', sub_profile='profile_1'):
        from pages.android.application_login import Login
        login = Login(self.driver)
        mobile = login.set_user_profile(profile, user_profile, sub_profile).user_mobile
        return mobile

    def get_otp(self, cc_mobile=None, account_type=None):
        # complete_mobile = self.get_mobile_and_ccode()
        if account_type == 'asset_not_tagged_account_details':
            cc_mobile = str(get_data('../config/config.json', 'asset_not_tagged_account_details', 'mobile'))
        self.session_relaunch()
        self.wait_for_locator_webdriver("//li[@id='otp']")
        self.chrome_driver.find_element_by_xpath("//li[@id='otp']").click()
        self.wait_for_locator_webdriver("//li[@id='mobile_otps']")
        self.chrome_driver.find_element_by_xpath("//li[@id='mobile_otps']").click()
        self.chrome_driver.find_element_by_css_selector("#q_mobile_no").send_keys(cc_mobile)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='commit']"))).click()
        otp = self.chrome_driver.find_element_by_css_selector("td.col-otp").text
        self.chrome_driver.close()
        return otp

    def wait_for_locator_webdriver(self, locator_value=None):
        try:
            WebDriverWait(self.chrome_driver, 15, ignored_exceptions=[StaleElementReferenceException]).until(
                ec.presence_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_clickable_element_webdriver(self, locator_value=None):
        try:
            WebDriverWait(self.chrome_driver, 15).until(ec.element_to_be_clickable((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_element_not_present_webdriver(self, locator_value=None):
        try:
            WebDriverWait(self.chrome_driver, 15).until(ec.invisibility_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def select_course(self, course_id=None):
        # Tutor is in cms course page
        self.wait_for_locator_webdriver("//table[contains(@class,'MuiTable-root')]")
        course_table_rows = len(
            self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root')]/tbody/tr"))
        course_table_cols = len(
            self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root')]/thead/tr/th"))
        course_id_col = None
        topics_col = 11
        for i in range(1, course_table_cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'MuiTable-root')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'ID':
                course_id_col = i
                break
        r = 1
        while True:
            course_found = False
            self.wait_for_locator_webdriver("//tr[" + str(r) + "]/td[" + str(course_id_col) + "]")
            value = self.chrome_driver.find_element_by_xpath(
                "//tr[" + str(r) + "]/td[" + str(course_id_col) + "]").text
            if course_id == value:
                course_found = True
                self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(topics_col) + "]/a").click()
                break
            r += 1
            if course_found is False and r == course_table_rows:
                svg_icons = self.chrome_driver.find_elements_by_css_selector('.MuiSvgIcon-root')
                length = len(svg_icons)
                svg_icons[length - 1].click()  # click on next for pagination
                r = 1

    def select_topic_and_update_teaching_material(self, topic_id=None):
        teaching_material = str(get_data('../config/config.json', 'update_pdf_in_cms_details', 'teaching_material'))

        # Tutor is in cms topics page
        self.wait_for_locator_webdriver("//table[contains(@class,'MuiTable-root')]")
        topic_table_rows = len(
            self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root')]/tbody/tr"))
        topic_table_cols = len(
            self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root')]/thead/tr/th"))
        topics_id_col = None
        for i in range(1, topic_table_cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'MuiTable-root')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'ID':
                topics_id_col = i
                break
        row = 1
        while True:
            topic_found = False
            time.sleep(1.0)
            result = self.chrome_driver.find_element_by_xpath(
                "//tr[" + str(row) + "]/td[" + str(topics_id_col) + "]").text
            if topic_id == result:
                topic_found = True
                teaching_material_input_fields = self.chrome_driver.find_elements_by_css_selector(
                    '.MuiAutocomplete-inputRoot .MuiAutocomplete-input')
                teaching_material_input_fields[row - 1].click()
                teaching_material_input_fields[row - 1].send_keys((Keys.COMMAND, "a"))
                teaching_material_input_fields[row - 1].send_keys(teaching_material, Keys.ARROW_DOWN)
                input_id = teaching_material_input_fields[row - 1].get_attribute("id")
                activedescendant = input_id + "-option-0"
                activedescendant_expected = activedescendant.replace("Mui", "mui")
                self.chrome_driver.find_element_by_css_selector(
                    "li#" + activedescendant_expected + ".MuiAutocomplete-option").click()
                self.wait_for_locator_webdriver("//span[contains(text(),'Save')]")
                self.chrome_driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
                time.sleep(0.5)
                break
            row += 1
            if topic_found is False and row == topic_table_rows:
                svg_icons = self.chrome_driver.find_elements_by_css_selector('.MuiSvgIcon-root')
                length = len(svg_icons)
                svg_icons[length - 1].click()  # click on next for pagination
                row = 1

    def login_to_cms_staging(self):
        email = str(get_data('../config/config.json', 'staging_access', 'email'))
        password = str(get_data('../config/config.json', 'staging_access', 'password'))
        # Login to CMS
        self.chrome_driver.get('https://tutor-plus-cms-staging.tllms.com/?page=1')
        self.chrome_driver.maximize_window()
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
        self.wait_for_locator_webdriver("//input[@id='email']")
        self.chrome_driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        self.wait_for_locator_webdriver("//button[@type='submit']")
        self.chrome_driver.find_element_by_xpath("//button[@type='submit']").click()
        self.wait_for_locator_webdriver("//input[@type='email']")
        self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
        self.wait_for_locator_webdriver("//span[contains(text(),'Next')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()
        self.wait_for_clickable_element_webdriver("//input[@type='password']")
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.wait_for_locator_webdriver("//span[contains(text(),'Next')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()

    def update_teaching_material(self, course_details):
        print(course_details)
        course_id = re.search(r'^.*?\bCourse id : (\d+)', course_details).group(1)
        topic_id = re.search(r'Topic id ?: (\d+)', course_details).group(1)
        self.login_to_cms_staging()
        self.select_course(course_id)
        self.select_topic_and_update_teaching_material(topic_id)
        self.chrome_driver.close()

    def is_session_present_today(self):
        premium_id = str(get_data('../config/config.json', 'account_details', 'premium_id'))
        today = datetime.today().strftime('%Y-%m-%d')

        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//li[@id='mentoring']")
        self.chrome_driver.find_element_by_xpath("//li[@id='mentoring']").click()
        self.wait_for_clickable_element_webdriver("//*[text()='1:M - Schedule Student Sessions']")
        self.chrome_driver.find_element_by_xpath("//*[text()='1:M - Schedule Student Sessions']").click()
        self.wait_for_locator_webdriver("//a[text()='Scheduling Sessions(User Wise)']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Scheduling Sessions(User Wise)']").click()
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver("//input[@id ='target_date']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='target_date']").send_keys(today)
        self.wait_for_locator_webdriver("//input[@id ='premium_account_id']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='premium_account_id']").send_keys(premium_id)
        self.wait_for_locator_webdriver("//input[@value ='Start Scheduling']")
        self.chrome_driver.find_elements_by_xpath("//input[@value ='Start Scheduling']")[1].click()
        flag = False
        rows = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/tbody/tr"))
        if rows >= 1:
            flag = True
        self.chrome_driver.close()
        return flag

    def is_teaching_material_tagged(self):
        premium_id = str(get_data('../config/config.json', 'asset_not_tagged_account_details', 'premium_id'))
        today = datetime.today().strftime('%Y-%m-%d')

        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//li[@id='mentoring']")
        self.chrome_driver.find_element_by_xpath("//li[@id='mentoring']").click()
        self.wait_for_clickable_element_webdriver("//*[text()='1:M - Schedule Student Sessions']")
        self.chrome_driver.find_element_by_xpath("//*[text()='1:M - Schedule Student Sessions']").click()

        self.wait_for_locator_webdriver("//a[text()='Scheduling Sessions(User Wise)']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Scheduling Sessions(User Wise)']").click()
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver("//input[@id ='target_date']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='target_date']").send_keys(today)
        self.wait_for_locator_webdriver("//input[@id ='premium_account_id']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='premium_account_id']").send_keys(premium_id)
        self.wait_for_locator_webdriver("//input[@value ='Start Scheduling']")
        self.chrome_driver.find_elements_by_xpath("//input[@value ='Start Scheduling']")[1].click()

        rows = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/tbody/tr"))
        cols = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/thead/tr/th"))
        course_info = dict()
        tagged_flag = tagged_col = None
        for i in range(1, cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'index_table')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'Teaching Material Tagged':
                tagged_col = i
                break

        for r in range(1, rows + 1):
            try:
                tagged_flag = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(tagged_col) + "]/div[contains(@class,'status_tag')]").text
                course_details = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(tagged_col) + "]/div[@class='course_details']").text
                course_info = {
                    "tagged": tagged_flag,
                    "course_details": course_details
                }
            except NoSuchElementException:
                continue

        self.chrome_driver.close()
        return course_info

    def click_on_teaching_material_link(self):
        self.wait_for_clickable_element_webdriver("//a[text()='Teaching Material ']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Teaching Material ']").click()

    def verify_teaching_material_page(self):
        self.wait_for_locator_webdriver("//th[text()='ID']")
        self.chrome_driver.find_element_by_xpath("//th[text()='ID']").is_displayed()
        self.chrome_driver.find_element_by_xpath("//th[text()='MATERIAL NAME']").is_displayed()

    def click_on_add_material_button(self):
        self.wait_for_clickable_element_webdriver("//span[text()='Add Material']")
        self.chrome_driver.find_element_by_xpath("//span[text()='Add Material']").click()

    def verify_teaching_material_popup(self):
        self.wait_for_locator_webdriver("//*[@role='dialog']")
        self.wait_for_locator_webdriver("//div[@id='max-width-dialog-title']")
        header_text = self.chrome_driver.find_element_by_xpath("//div[@id='max-width-dialog-title']").text
        assert header_text == 'Upload Teaching Material', "Upload Teaching Material header is not present"
        self.chrome_driver.find_element_by_xpath("//label[text()='Material Name:']").is_displayed()
        self.chrome_driver.find_element_by_xpath("//input[@id='name']").is_displayed()
        self.chrome_driver.find_element_by_xpath("//label[text()='Upload:']").is_displayed()
        self.chrome_driver.find_element_by_xpath("//input[@id='pdfContainer']").is_displayed()
        self.chrome_driver.find_element_by_xpath("//span[text()='Submit']").is_displayed()
        self.chrome_driver.find_element_by_xpath("//span[text()='Close']").is_displayed()

    def click_outside_upload_teaching_material_popup(self):
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(
            self.chrome_driver.find_element_by_xpath("//*[@class='MuiIconButton-label']"), 10, 10).perform()

    def verify_teaching_material_popup_is_closed(self):
        self.wait_for_element_not_present_webdriver("//*[@role='dialog']")
        try:
            self.chrome_driver.find_element_by_xpath("//*[@role='dialog']").is_displayed()
        except NoSuchElementException:
            return False
        return True

    def close_driver(self):
        self.chrome_driver.close()

    def close_upload_teaching_material_dialog(self):
        self.chrome_driver.find_element_by_xpath("//span[text()='Close']").click()

    def verify_teaching_material_page_pagination(self):
        i = 1
        length = len(self.chrome_driver.find_elements_by_css_selector('.MuiButton-label'))
        while i < length:
            pagination_icon = self.chrome_driver.find_element_by_xpath("//span[text()=" + str(i) + "]")
            self.chrome_driver.execute_script("arguments[0].click();", pagination_icon)  # click on next for pagination
            self.chrome_driver.implicitly_wait(0.5)
            pagination_icon = self.chrome_driver.find_element_by_xpath(
                "//span[text()=" + str(i) + "]")  # page reloaded,hence fetching element again
            assert pagination_icon.is_enabled() == True, "Page " + i + "is not selected"
            i += 1

    def set_material_name(self):
        global material_name
        random = randint(1, 100000)
        material_name = 'Material_' + str(random)
        self.chrome_driver.find_element_by_xpath("//input[@id='name']").send_keys(material_name)
        return material_name

    def choose_pdf_file(self):
        input_element = self.chrome_driver.find_element_by_xpath("//input[@type='file']")
        current_location = os.path.dirname(os.path.abspath(__file__))
        location = os.path.normpath(os.path.join(current_location, '../../files/Simple_Equations_Sample.pdf'))
        input_element.send_keys(location)
        ActionChains(self.chrome_driver).send_keys(Keys.ESCAPE).perform()

    def verify_file_other_than_pdf_cannot_be_selected(self):
        self.chrome_driver.execute_script("arguments[0].click();",
                                          self.chrome_driver.find_element_by_xpath("//input[@type='file']"))
        accept_value = self.chrome_driver.find_element_by_xpath("//input[@type='file']").get_attribute('accept')
        assert accept_value == ".pdf", "Able to select files other than .pdf file"

    def click_on_submit_teaching_material_page(self):
        self.chrome_driver.find_element_by_xpath("//span[text()='Submit']").click()

    def is_uploaded_file_present(self):
        self.wait_for_locator_webdriver("//*[text()='" + material_name + "']")
        material_name_found = material_id_found = False
        table_items = self.chrome_driver.find_elements_by_css_selector('.MuiTableRow-root')
        for item in table_items:
            item_value = item.text
            items = item_value.split()
            if material_name == items[1]:
                material_name_found = True
            if items[0] is not None:
                material_id_found = True
        assert material_name_found is True and material_id_found is True, "Material is not added"

    def verify_page_num_is_highlighted(self, page_num):
        pagination_icon = self.chrome_driver.find_element_by_xpath(
            "//span[text()=" + page_num + "]")  # page reloaded,hence fetching element again
        assert pagination_icon.is_enabled() == True, "Page " + page_num + "is not selected"

    def add_role_to_user(self, role):
        email = str(get_data('../config/config.json', 'staging_access', 'email'))
        self.wait_for_clickable_element_webdriver("//a[text()='Users']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Users']").click()
        self.wait_for_clickable_element_webdriver("//input[@id='q_email']")
        self.chrome_driver.find_element_by_xpath("//input[@id='q_email']").send_keys(email)
        self.chrome_driver.find_element_by_xpath("//input[@name='commit']").click()

        self.wait_for_clickable_element_webdriver("//a[@title='View']")
        self.chrome_driver.find_element_by_xpath("//a[@title='View']").click()

        self.wait_for_clickable_element_webdriver("//a[text()='Roles']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Roles']").click()
        select = Select(self.chrome_driver.find_element_by_xpath("//*[@id='resource_role']"))
        select.select_by_visible_text(role)
        add_buttons = self.chrome_driver.find_elements_by_xpath("//*[@name='commit']")
        add_buttons[0].click()

    def is_role_added(self, role):
        self.login_to_cms_staging()
        self.wait_for_clickable_element_webdriver("//*[@class='MuiAvatar-img']")
        self.chrome_driver.find_element_by_xpath("//*[@class='MuiAvatar-img']").click()
        role_found = False
        menu_items = self.chrome_driver.find_elements_by_css_selector('.MuiMenuItem-root')
        for item in menu_items:
            print(item.text)
            if role == item.text:
                role_found = True
        self.chrome_driver.close()
        return role_found

    def set_assessment_start_date(self, date, assessment_id):
        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//li[@id='assessments']")
        self.chrome_driver.find_element_by_xpath("//li[@id='assessments']").click()
        self.chrome_driver.find_element_by_css_selector("#q_id").send_keys(assessment_id)
        self.wait_for_clickable_element_webdriver("//*[@name='commit']")
        self.chrome_driver.find_element_by_xpath("//*[@name='commit']").click()

        self.wait_for_clickable_element_webdriver("//a[text()='Edit']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Edit']").click()
        self.wait_for_clickable_element_webdriver("//input[@id='assessment_available_starting']")
        self.chrome_driver.find_element_by_xpath("//input[@id='assessment_available_starting']").clear()
        self.chrome_driver.find_element_by_xpath("//input[@id='assessment_available_starting']").send_keys(date)
        self.chrome_driver.find_element_by_xpath("//*[@name='commit']").click()
        self.chrome_driver.close()
        return date

    def set_assessment_end_date(self, date, assessment_id):
        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//li[@id='assessments']")
        self.chrome_driver.find_element_by_xpath("//li[@id='assessments']").click()
        self.chrome_driver.find_element_by_css_selector("#q_id").send_keys(assessment_id)
        self.wait_for_clickable_element_webdriver("//*[@name='commit']")
        self.chrome_driver.find_element_by_xpath("//*[@name='commit']").click()

        self.wait_for_clickable_element_webdriver("//a[text()='Edit']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Edit']").click()
        self.wait_for_clickable_element_webdriver("//input[@id='assessment_available_until']")
        self.chrome_driver.find_element_by_xpath("//input[@id='assessment_available_until']").clear()
        date = self.chrome_driver.find_element_by_xpath("//input[@id='assessment_available_until']").send_keys(date)
        self.chrome_driver.find_element_by_xpath("//*[@name='commit']").click()
        self.chrome_driver.close()
        return date

    def get_assessment_available_until_date(self, assessment_id):
        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//li[@id='assessments']")
        self.chrome_driver.find_element_by_xpath("//li[@id='assessments']").click()
        self.chrome_driver.find_element_by_css_selector("#q_id").send_keys(assessment_id)
        self.wait_for_clickable_element_webdriver("//*[@name='commit']")
        self.chrome_driver.find_element_by_xpath("//*[@name='commit']").click()

        self.wait_for_clickable_element_webdriver("//a[text()='Edit']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Edit']").click()
        self.wait_for_clickable_element_webdriver("//input[@id='assessment_available_until']")
        date = self.chrome_driver.find_element_by_xpath("//input[@id='assessment_available_until']").get_attribute(
            'value')
        self.chrome_driver.close()
        return date

    def attach_requisite(self, requisite_name):
        premium_id = str(get_data('../config/config.json', 'account_details', 'premium_id'))
        today = datetime.today().strftime('%Y-%m-%d')

        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//li[@id='mentoring']")
        self.chrome_driver.find_element_by_xpath("//li[@id='mentoring']").click()
        self.wait_for_clickable_element_webdriver("//*[text()='1:M - Schedule Student Sessions']")
        self.chrome_driver.find_element_by_xpath("//*[text()='1:M - Schedule Student Sessions']").click()

        self.wait_for_locator_webdriver("//a[text()='Scheduling Sessions(User Wise)']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Scheduling Sessions(User Wise)']").click()
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver("//input[@id ='target_date']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='target_date']").send_keys(today)
        self.wait_for_locator_webdriver("//input[@id ='premium_account_id']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='premium_account_id']").send_keys(premium_id)
        self.wait_for_locator_webdriver("//input[@value ='Start Scheduling']")
        self.chrome_driver.find_elements_by_xpath("//input[@value ='Start Scheduling']")[1].click()

        rows = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/tbody/tr"))
        cols = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/thead/tr/th"))
        channel_col = status_col = None
        for i in range(1, cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'index_table')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'Channel':
                channel_col = i
            elif header == 'Status':
                status_col = i

        for r in range(1, rows + 1):
            try:
                status = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(status_col) + "]").text
                if 'one_to_mega' in status:
                    self.chrome_driver.find_element_by_xpath(
                        "//tr[" + str(r) + "]/td[" + str(channel_col) + "]/a[@target='_blank']").click()
                    # switch to newly opened tab to attach requisite
                    self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[1])
                    self.wait_for_locator_webdriver("//a[text()='Attach Requisite Group']")
                    self.chrome_driver.find_element_by_xpath("//a[text()='Attach Requisite Group']").click()
                    self.wait_for_locator_webdriver("//span[@role='presentation']")
                    self.chrome_driver.find_element_by_xpath("//span[@role='presentation']").click()
                    # self.wait_for_locator_webdriver("//li[text()='"+requisite_name+"']")
                    # self.chrome_driver.find_element_by_xpath("//li[text()='"+requisite_name+"']").click()
                    self.chrome_driver.find_element_by_xpath("//input[@class='select2-search__field']").send_keys(
                        requisite_name)
                    time.sleep(2)
                    self.chrome_driver.find_element_by_xpath(
                        "//li[@class='select2-results__option select2-results__option--highlighted']").click()
                    self.wait_for_locator_webdriver("//button[@type='submit']")
                    self.chrome_driver.find_element_by_xpath("//button[@type='submit']").click()
                    try:
                        WebDriverWait(self.chrome_driver, 5).until(ec.alert_is_present(),
                                                                   'Timed out waiting for confirmation popup to appear.')
                        alert = self.chrome_driver.switch_to.alert
                        alert.accept()
                        print("alert accepted")
                        time.sleep(2)
                    except TimeoutException:
                        print("no alert")
                    self.chrome_driver.close()
                    self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[0])
            except NoSuchElementException:
                continue
        self.chrome_driver.close()

    def detach_requisite(self):
        premium_id = str(get_data('../config/config.json', 'account_details', 'premium_id'))
        today = datetime.today().strftime('%Y-%m-%d')

        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//li[@id='mentoring']")
        self.chrome_driver.find_element_by_xpath("//li[@id='mentoring']").click()
        self.wait_for_clickable_element_webdriver("//*[text()='1:M - Schedule Student Sessions']")
        self.chrome_driver.find_element_by_xpath("//*[text()='1:M - Schedule Student Sessions']").click()

        self.wait_for_locator_webdriver("//a[text()='Scheduling Sessions(User Wise)']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Scheduling Sessions(User Wise)']").click()
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver("//input[@id ='target_date']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='target_date']").send_keys(today)
        self.wait_for_locator_webdriver("//input[@id ='premium_account_id']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='premium_account_id']").send_keys(premium_id)
        self.wait_for_locator_webdriver("//input[@value ='Start Scheduling']")
        self.chrome_driver.find_elements_by_xpath("//input[@value ='Start Scheduling']")[1].click()

        rows = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/tbody/tr"))
        cols = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/thead/tr/th"))
        channel_col = status_col = None
        for i in range(1, cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'index_table')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'Channel':
                channel_col = i
            elif header == 'Status':
                status_col = i

        for r in range(1, rows + 1):
            try:
                status = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(status_col) + "]").text
                if 'one_to_mega' in status:
                    self.chrome_driver.find_element_by_xpath(
                        "//tr[" + str(r) + "]/td[" + str(channel_col) + "]/a[@target='_blank']").click()
                    # switch to newly opened tab to attach requisite
                    self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[1])
                    self.wait_for_locator_webdriver("//a[text()='Detach Requisite Group']")
                    self.chrome_driver.find_element_by_xpath("//a[text()='Detach Requisite Group']").click()
                    try:
                        WebDriverWait(self.chrome_driver, 5).until(ec.alert_is_present(),
                                                                   'Timed out waiting for confirmation popup to appear.')
                        alert = self.chrome_driver.switch_to.alert
                        alert.accept()
                        print("alert accepted")
                        time.sleep(2)
                    except TimeoutException:
                        print("no alert")
                    self.chrome_driver.close()
                    self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[0])
            except NoSuchElementException:
                continue
        self.chrome_driver.close()

    def saved_session(self):
        try:
            with open('../../config/login.pkl', 'rb') as io_read:
                c = pickle.load(io_read)
                if not bool(c):
                    raise EOFError from None
                else:
                    return c
        except (EOFError, FileNotFoundError):
            self.login_to_staging().save_session()
            return list()

    def session_relaunch(self, cms=False):
        retry = 3
        url = self.STAGING_TLLMS_URL if cms is False else self.TUTOR_PLUS_CMS_URL
        while retry:
            session = self.saved_session()
            self.chrome_driver.quit()
            self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
            self.__init()
            if bool(session):
                self.chrome_driver.get(url)
                try:
                    [self.chrome_driver.add_cookie(s) for s in session]
                except UnableToSetCookieException:
                    self.chrome_driver.get_screenshot_as_file("../../test_data/view.png")
                    raise
                self.chrome_driver.get(url)
                if '/users/sign_in' in self.chrome_driver.current_url:
                    self.login_to_staging().save_session()
                    break
                elif cms:
                    self.chrome_driver.find_element("xpath", "//span[text()='LOGIN']").click()
                    self.wait_for_element_not_present_webdriver("//span[text()='LOGIN']")
                    try:
                        self.chrome_driver.implicitly_wait(30)
                        self.chrome_driver.find_element("css selector", "img[src]")
                    except NoSuchElementException:
                        pass
                    if self.TUTOR_PLUS_CMS_URL in self.chrome_driver.current_url:
                        self.save_session()
                        break
                    else:
                        retry -= 1
                elif url in self.chrome_driver.current_url:
                    break
                else:
                    retry -= 1
        else:
            raise SessionNotCreatedException("New session could not be created") from None

    def get_premium_id(self, profile='login_details_3', user_profile=None, sub_profile=None):
        from pages.android.application_login import Login
        login = Login(self.driver)
        login.set_user_profile(profile, user_profile, sub_profile)
        login_data = self.LOGIN_DETAILS
        m, i, u = login.user_mobile, login.premium_id, login.profile_name
        if i is None:
            with open(login_data, "r+") as io_write:
                data = json.load(io_write)
                io_write.seek(0)
                user = data[profile][user_profile][sub_profile]
                user.update({self.PREMIUM_ID: self._pid(u, m)})
                json.dump(data, io_write, indent=4)
            return user[self.PREMIUM_ID], True
        return i, False

    def _pid(self, user_profile=None, mobile=None):
        self.session_relaunch()
        self.chrome_driver.implicitly_wait(30)
        self.chrome_driver.find_element(By.ID, 'users').click()
        self.chrome_driver.find_element(By.ID, 'q_mobile').send_keys(mobile)
        self.chrome_driver.find_element(By.CSS_SELECTOR, '.buttons > input').click()

        users_col = self.chrome_driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
        try:
            f_name, l_name = user_profile.split(maxsplit=1)
        except ValueError:
            f_name, l_name = user_profile, ""
        for user in users_col:
            first_name = user.find_element(By.CSS_SELECTOR, ".col.col-first_name").text
            last_name = user.find_element(By.CSS_SELECTOR, ".col.col-last_name").text
            if first_name == user_profile:
                user.find_element(By.CSS_SELECTOR, ".col.col-id>a").click()
                break
            elif first_name == f_name and last_name == l_name:
                user.find_element(By.CSS_SELECTOR, ".col.col-id>a").click()
                break
        else:
            raise UnknownUserProfile("none matched against given user")
        _id = self.chrome_driver.find_element(By.CSS_SELECTOR, ".row.row-premium_account > td > a").text
        return _id

    def working_day(self, days=None):
        for d in range(1, 6):
            if not self.is_holiday(datetime.now() + timedelta(days)):
                date = datetime.now() + timedelta(days)
                break
            days += d
        else:
            raise DateError("no working day available")
        return date

    def otm_home_screen(self):
        from pages.android.student_dashboard_otm import StudentDashboardOneToMega
        __o = StudentDashboardOneToMega(self.driver)
        otm_home_activity = 'OneToMegaHomeActivity'
        user_home_activity = 'UserHomeActivity'
        home_activity = 'HomeActivity'
        if otm_home_activity in self.driver.current_activity:
            pass
        elif user_home_activity in self.driver.current_activity:
            self.get_element('xpath', __o.login.btn_premium).click()
        elif home_activity in self.driver.current_activity:
            __o.login.click_on_premium_school()
        else:
            self.driver.close_app()
            self.driver.launch_app()
            __o.login.click_on_premium_school()
        return __o

    def get_session_completed_up_next_date(self, completed=None):
        __o = self.otm_home_screen()
        last_date, up_nxt_date = __o.last_completed_session_up_next(completed)
        __o.click_app_back_btn()
        if __o.login.wait_activity("UserHomeActivity", 5):
            __o.click_app_back_btn()
        return last_date, up_nxt_date.split(',')[0]

    def date_check(self, session=None, completed=None):
        name = type(session).__name__
        if isinstance(session, str):
            if session == 'yesterday':
                days = -1
            elif session == 'today':
                days = 0
            elif session == 'tomorrow':
                days = 1
            elif session == 'completed' or session == 'up next':
                session_desc = self.get_session_completed_up_next_date(completed=completed)
                if session == 'completed':
                    ssn = session_desc[0]
                else:
                    ssn = session_desc[-1]
                details = ssn.split()
                if details[0].lower() != 'today':
                    date, month = details
                    current_month = time.strftime('%b')
                    if month == current_month:
                        days = int(date) - int(time.strftime('%d'))
                        working_day = datetime.now() + timedelta(days)
                        return working_day
                    else:
                        raise DateError(
                            "session completed month ('%s') is not in the current month ('%s')" % (month, current_month)
                        )
                elif details[0].lower() == 'today':
                    days = 0
                else:
                    raise NotImplementedError(f"'{ssn}' session is not yet implemented.")
            else:
                raise DateError("not implemented, provide day in ('int' or 'float') instead")
        elif isinstance(session, int):
            days = session
        else:
            raise TypeError(f"expected 'str' or 'int', got '{name}' type instead")
        return self.working_day(days)

    def _req_grp_name(self, r=None, a=None):
        t = r.lower()
        c = a.lower()
        r_d = self.REQUISITE_DETAILS
        if t == 'in':
            o = get_data(r_d, self.IN_REQ)
            if c == 'assessment':
                n = o[c]
                return n
            else:
                raise AssetTypeError(r, a)
        elif t == 'pre':
            o = get_data(r_d, self.PRE_REQ)
            if c == 'all' or c == 'assessment' or c == 'journey' or c == 'k12 video' or c == 'practice' or c == 'video':
                if c == 'video':
                    c = 'k12 video'
                c = "_".join(c.split())
                n = o[c]
            else:
                raise AssetTypeError(r, a)
        elif t == 'post':
            o = get_data(r_d, self.POST_REQ)
            if c == 'all' or c == 'assessment' or c == 'journey' or c == 'k3 video' or c == 'k12 video' or c == 'video':
                if c == 'video':
                    c = random.choice(('k3 video', 'k12 video'))
                c = "_".join(c.split())
                n = o[c]
            elif c == 'two':
                n = o[c]
            else:
                raise AssetTypeError(r, a)
        elif t == 'all_pre_post':
            o = get_data(r_d, self.ALL_PRE_POST_REQ)
            n = o
        elif t == 'pre_post_ak3_29':
            o = get_data(r_d, "pre_post_ak3_29")
            n = o
        else:
            raise RequisiteTypeError(r)
        return n

    def _requisite_group(self, rt=None, at=None, mode='attach'):
        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[-1])
        if mode.lower() == 'attach':
            grp_name = self._req_grp_name(rt, at)
            self.chrome_driver.find_element(By.XPATH, '//a[text()="Attach Requisite Group"]').click()
            # select = Select(self.chrome_driver.find_element_by_id('requisite_group_id'))
            # field_text = select.first_selected_option.text
            # uncomment if reverted back to old changes
            retry = 5
            field = self.chrome_driver.find_element(By.CSS_SELECTOR, '.select2-selection__arrow')
            try:
                field_text = field.find_element(By.XPATH, '../../span[@id="select2-requisite_group_id-container"]').text
            except NoSuchElementException:
                field_text = str()
            field.click()
            self.chrome_driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(grp_name)
            while retry:
                try:
                    self.chrome_driver.find_element(By.XPATH, '//li[text()="%s"]' % grp_name).click()
                    retry = 0
                except (NoSuchElementException, StaleElementReferenceException):
                    retry -= 1
                    sleep(1)
            # if field_text != grp_name:
            #     select.select_by_visible_text(grp_name)
            self.chrome_driver.find_element(By.CSS_SELECTOR, "#_submit_action>button").click()
            # if field_text:
            try:
                self.chrome_driver.switch_to.alert.accept()
            except NoAlertPresentException:
                pass
            notice = self.chrome_driver.find_element(By.CSS_SELECTOR, ".flashes .flash").text
            if "attached" not in notice.lower():
                raise AttachmentError("'Requisite Group' attachment might not be successful.")
        elif mode.lower() == 'detach':
            self.chrome_driver.find_element(By.XPATH, '//a[text()="Detach Requisite Group"]').click()
            self.chrome_driver.switch_to.alert.accept()
            notice = self.chrome_driver.find_element(By.CSS_SELECTOR, ".flashes .flash").text
            if "detached" not in notice.lower():
                raise AttachmentError("'Requisite Group' detachment might not be successful.")
        else:
            raise InvalidModeSelection(f"'{mode}' is not a valid mode.")
        return self

    def _session_user_wise(self, session=None, user_profile=None,
                           sub_profile=None, profile='login_details_3', completed=None):
        time_details = self.date_check(session, completed=completed)
        p_id, status = self.get_premium_id(profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        date = str(time_details).split(maxsplit=1)[0]
        student_session_url = 'https://staging.tllms.com/admin/student_sessions'
        try:
            if not status:
                self.session_relaunch()
            self.chrome_driver.execute_script(f"window.open('{student_session_url}');")
        except InvalidSessionIdException:
            self.session_relaunch()
            self.chrome_driver.execute_script(f"window.open('{student_session_url}');")
        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[-1])
        self.chrome_driver.find_element(By.ID, 'ui-id-2').click()
        self.chrome_driver.find_element(By.ID, "premium_account_id").send_keys(p_id)
        self.chrome_driver.execute_script('document.getElementById("target_date").removeAttribute("readonly")')
        self.chrome_driver.find_element(By.ID, 'target_date').clear()
        self.chrome_driver.find_element(By.ID, 'target_date').send_keys(date + '\n')
        self.chrome_driver.find_element(
            By.XPATH, '//div[@id="scheduling-sessions-user-wise"]//li[@id="_submit_action"]/input').click()
        if self.chrome_driver.current_url == student_session_url:
            raise ClassRoomNotFoundError(f"no classrooms found for the specified user on {date}.")

    def attach_requisite_group(self, req_type=None, asset_type=None, days=None,
                               profile=None, user_profile=None, sub_profile=None, session_topic_nm=None):
        self._session_user_wise(days, profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        sessions = self.chrome_driver.find_elements(
            By.XPATH, "(//tr/td[contains(text(),'one_to_mega')])")
        for session in sessions:
            raw_topic_name = session.find_element_by_xpath('./preceding-sibling::td[4]').text
            if session_topic_nm is not None and session_topic_nm in raw_topic_name:
                session.find_element_by_xpath('./preceding-sibling::td/a').click()
                break
            elif session_topic_nm is None:
                session.find_element_by_xpath('./preceding-sibling::td/a').click()
                break
        self._requisite_group(req_type, asset_type).destroy_tabs()

    def destroy_tabs(self):
        windows = self.chrome_driver.window_handles
        for window in windows:
            self.chrome_driver.switch_to.window(window)
            self.chrome_driver.close()

    def _session_url(self, topic_name=None):
        if topic_name is None:
            url = self.chrome_driver.find_element(
                By.XPATH,
                "(//tr/td[contains(text(),'one_to_mega')])[1]/following-sibling::td/li[@id='meeting_url_input']/input"
            ).get_attribute('value')
            email = self.chrome_driver.find_element(
                By.XPATH,
                "//tr/td[contains(text(),'one_to_mega')]/following-sibling::td/li[@id='teacher_email_input']/input"
            )
            return url, email
        else:
            sessions = self.chrome_driver.find_elements(
                By.XPATH, "(//tr/td[contains(text(),'one_to_mega')])")
            for session in sessions:
                raw_topic_name = session.find_element_by_xpath('./preceding-sibling::td[4]').text
                if topic_name in raw_topic_name:
                    m_url = session.find_element_by_xpath(
                        "./following-sibling::td/li[@id='meeting_url_input']/input").get_attribute('value')
                    e_mail = session.find_element_by_xpath(
                        "./following-sibling::td/li[@id='teacher_email_input']/input")
                    return m_url, e_mail
            else:
                raise SessionNotFoundError(f"the session with the topic name '{topic_name}' is not found on the page.")

    def end_ongoing_session(self, rate_action='skip', topic_name=None, user_profile=None, sub_profile=None):
        timeout = 240
        # todo: log: get sub_profile_type
        if rate_action == 'skip':
            if user_profile is None and sub_profile is None:
                self._session_user_wise(session='today', user_profile='user_1', sub_profile='profile_1')
            else:
                self._session_user_wise(session='today', user_profile=user_profile, sub_profile=sub_profile)
        elif rate_action == 'rate':
            if user_profile is None and sub_profile is None:
                self._session_user_wise(session='today', user_profile='user_2', sub_profile='profile_1')
            else:
                self._session_user_wise(session='today', user_profile=user_profile, sub_profile=sub_profile)
        m_url, email_input = self._session_url(topic_name)
        self.chrome_driver.execute_script(f"arguments[0].setAttribute('value', '{self.EMAIL}')", email_input)
        self.chrome_driver.find_element(By.CSS_SELECTOR, '#_submit_action').click()
        self.chrome_driver.get(m_url)
        self.wait_for_clickable_element_webdriver('//span[text()="LOGIN"]')
        self.chrome_driver.find_element(By.XPATH, '//span[text()="LOGIN"]').click()
        self.chrome_driver.implicitly_wait(0)
        try:
            count = 20
            while timeout:
                try:
                    self.chrome_driver.find_element(By.CSS_SELECTOR, '.endPopupContainer .subText')
                    timeout -= 1
                    sleep(1)
                    count = 0
                except NoSuchElementException:
                    if not count:
                        timeout -= timeout
                    else:
                        count -= 1
                        sleep(0.5)
            self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.session-button.timer'))).click()
            self.chrome_driver.find_element(By.XPATH, "//div[text()='End Session Now']").click()
            self.chrome_driver.find_element(By.CSS_SELECTOR, ".endBtn").click()
            info = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "label.Mui-error"))).text
            if 'ended now' in info.lower():
                return True
            else:
                warnings.warn("tutor session might not be ended properly")
        except TimeoutException:
            err_msg = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "label.Mui-error"))).text
            if 'session is ended' in err_msg.lower():
                return True
            elif 'not authorized' in err_msg.lower():
                raise UnknownUserProfile(
                    f"'{self.EMAIL}' is not a valid tutor email or not updated in 'Schedule Page'.") from None
            else:
                raise SessionNotEndedError('session might not be ended or could not validate the message') from None

    def detach_requisite_attachment(self, profile='login_details_3', user_profile='user_1', sub_profile='profile_1'):
        self.session_relaunch()
        self._session_user_wise(
            session='completed', profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        self.chrome_driver.find_element(
            By.XPATH, "//tr/td[contains(text(),'one_to_mega')]/preceding-sibling::td/a").click()
        self._requisite_group(None, None, mode='detach').destroy_tabs()

    def is_otm_session_activity(self):
        __o = self.otm_home_screen()
        return __o.is_join_now_btn_displayed()

    def get_otm_first_session_detail(
            self, profile='login_details_3', user_profile='user_1', sub_profile='profile_1', completed=None):
        self.session_relaunch()
        self._session_user_wise(
            session='completed', profile=profile, user_profile=user_profile, sub_profile=sub_profile,
            completed=completed)
        session_detail = self.chrome_driver.find_element(
            By.XPATH,
            "(//tr/td[contains(text(),'one_to_mega')])[1]/preceding-sibling::td[4]").text.lower()
        return session_detail

    def reset_session_one_to_mega(
            self, profile='login_details_3', user_profile='user_1',
            sub_profile='profile_1', completed=None, topic_name=None):
        self.session_relaunch()
        self._session_user_wise(
            session='completed', profile=profile, user_profile=user_profile, sub_profile=sub_profile,
            completed=completed)
        mega_sessions = self.chrome_driver.find_elements_by_xpath("//tr/td[contains(text(),'one_to_mega')]")
        mega_session = mega_sessions[0]
        for mega_session in mega_sessions:
            mega_topic_name = mega_session.find_element_by_xpath("./preceding-sibling::td[4]").text
            if topic_name.lower() in mega_topic_name.lower():
                break
        t = mega_session.find_element(By.XPATH, "./preceding-sibling::td/b/..").text
        date_time = t.split('\n')
        session_date, session_time = date_time[0], date_time[-1]
        struct_time = time.strptime(session_date, '%d-%b-%Y')
        cd, cm, cy = list(map(int, time.strftime("%d %m %Y").split()))
        sd, sm, sy = struct_time.tm_mday, struct_time.tm_mon, struct_time.tm_year
        ch = int(time.strftime("%H"))
        ah = int(session_time.split("-")[-1].strip().split(":")[0])
        if sy == cy:
            if sm == cm:
                if sd == cd:
                    if ah > ch:
                        mega_session.find_element(By.XPATH, "./following-sibling::td/a[text()='Reset']").click()
                        self.otm_home_screen()
                elif sd > cd:
                    self.otm_home_screen()
                    # SessionResetException("Reset-Error: 'session yet to be started.'")
                else:
                    SessionResetException("Reset-Error: 'session reached the end time.'")
            else:
                SessionResetException("Reset-Error: 'session is not in the current month.'")
        else:
            raise SessionResetException("Reset-Error: 'session is not in the current year.'")

    def topic_id_row(self, tid=None):
        for cl in range(1, 11):
            col = self.chrome_driver.find_element(By.XPATH, "((//tbody/tr)[%s]/td/div)[1]" % cl)
            if int(col.text) == tid:
                return self.chrome_driver.find_elements(By.XPATH, "((//tbody/tr)[%s]/td/div)" % cl)

    def _license_key(self, this=None, label=None, attachment=None, tag=None):
        try:
            if "hls" in label:
                video_hls = attachment['hls']
                input_box = this.find_element(By.XPATH, tag)
                if input_box.get_attribute('value') == "":
                    input_box.clear()
                    input_box.send_keys(video_hls['license_key'])
                else:
                    input_box.clear()
                    input_box.send_keys(video_hls['license_key'])
            elif "dash" in label:
                video_hls = attachment['dash']
                input_box = this.find_element(By.XPATH, tag)
                if input_box.get_attribute('value') == "":
                    input_box.clear()
                    input_box.send_keys(video_hls['license_key'])
                else:
                    input_box.clear()
                    input_box.send_keys(video_hls['license_key'])
            else:
                raise NotImplementedError(f"'{label}' is not yet implemented")
        except (ElementNotInteractableException, InvalidElementStateException):
            """input fields are disabled"""
            pass

    def _video_url(self, this=None, label=None, attachment=None, tag=None):
        try:
            if "hls" in label:
                video_hls = attachment['hls']
                input_box = this.find_element(By.XPATH, tag)
                if input_box.get_attribute('value') == "":
                    input_box.clear()
                    input_box.send_keys(video_hls['video_url'])
                else:
                    input_box.clear()
                    input_box.send_keys(video_hls['video_url'])
            elif "dash" in label:
                video_dash = attachment['dash']
                input_box = this.find_element(By.XPATH, tag)
                if input_box.get_attribute('value') == "":
                    input_box.clear()
                    input_box.send_keys(video_dash['video_url'])
                else:
                    input_box.clear()
                    input_box.send_keys(video_dash['video_url'])
            else:
                raise NotImplementedError(f"'{label}' is not yet implemented")
        except (ElementNotInteractableException, InvalidElementStateException):
            """input fields are disabled"""
            pass

    def _write_key_license(self, topic_id_col_elements=None, tag_label=None, tag_input=None, video_n='video_0'):
        video_attachment = get_data(self.ATTACHMENT_DETAILS, 'one_to_mega', video_n)
        for col in topic_id_col_elements:
            self.chrome_driver.implicitly_wait(0)
            try:
                element_label = col.find_element(By.XPATH, tag_label).text.lower()
            except NoSuchElementException:
                continue
            if "key" in element_label:
                self._license_key(this=col, label=element_label, attachment=video_attachment, tag=tag_input)
            elif "url" in element_label:
                self._video_url(this=col, label=element_label, attachment=video_attachment, tag=tag_input)

    def _attachment_write(self, course_id=None, topic_id=None):
        self.chrome_driver.implicitly_wait(30)
        topics_uri = 'courses/%s/topics?page=%s'
        items_per_page = 10
        topic_id = int(topic_id)
        self.chrome_driver.get("https://tutor-plus-cms-staging.tllms.com/%s" % topics_uri % (course_id, 1))
        try:
            self.chrome_driver.find_element_by_xpath('//span[text()="LOGIN"]').click()
        except NoSuchElementException:
            pass
        new_topic_id = int(self.chrome_driver.find_element(By.XPATH, "((//tbody/tr)[1]/td)[1]").text)
        to_page = (abs(new_topic_id - topic_id) // items_per_page) + 1
        to_url = (self.TUTOR_PLUS_CMS_URL + topics_uri) % (course_id, to_page)
        self.chrome_driver.get(to_url)
        topic_id_col_elements = self.topic_id_row(topic_id)
        tag_label = "./div/label"
        tag_input = "./div/div/input"
        self._write_key_license(topic_id_col_elements=topic_id_col_elements, tag_label=tag_label, tag_input=tag_input)

    def attach_session_video(self, profile=None, user_profile=None, sub_profile=None, session='today'):
        self.chrome_driver.implicitly_wait(30)
        self.get_premium_id(profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        self._session_user_wise(session=session, profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        video_tagged_session = self.chrome_driver.find_elements_by_xpath(
            "//tr/td[contains(text(),'one_to_mega')]/preceding-sibling::td/div[contains(@class, 'status')]"
        )
        vt_details = list()
        for index, video_tagged in enumerate(video_tagged_session, 1):
            if video_tagged.text.lower() != 'yes':
                vt_details.append(self.chrome_driver.find_element(
                    By.XPATH,
                    "(//tr/td[contains(text(),'one_to_mega')]/preceding-sibling::"
                    f"td/div[contains(text(),'Course id')])[{index}]"
                ).text)
        for vt_detail in vt_details:
            details = list(re.findall(r"(?i:(course\sid.*:\s\d*)(?:[^\b]*)(topic\sid\s:\s\d*))", vt_detail)[-1])
            course_id, topic_id = details[0].split(':')[-1].strip(), details[-1].split(':')[-1].strip()
            self._attachment_write(course_id=course_id, topic_id=topic_id)
            button_save = self.chrome_driver.find_element(By.XPATH, '//button/span[text()="Save"]')
            button_save.click()

    def requisite_assessment(self):
        post_asset_id = '61414'
        self.session_relaunch()
        self.chrome_driver.get('https://staging.tllms.com/admin/assessments')
        self.chrome_driver.find_element_by_id('q_id').send_keys(post_asset_id)
        self.chrome_driver.find_element_by_name('commit').click()
        self.chrome_driver.find_element_by_xpath('//a[text()="Edit"]').click()

    @staticmethod
    def booking_time(hours, minutes, end_hour=None, end_minutes=0, day=None):
        time_now = datetime.now()
        if day is not None and day.lower() == 'tomorrow':
            n_day = (time_now+timedelta(days=1)).strftime("%A")
            return n_day, "8:00", "23:00"
        if minutes is None:
            mins = 32
        else:
            mins = 30 + int(minutes)
        if int(time_now.strftime("%S")) >= 45:
            time_now = datetime.now()
            mins = 33 if minutes is None else 30 + int(minutes) + 1
        start_time = (time_now + timedelta(hours=0, minutes=mins))
        if end_hour is None:
            if hours is not None:
                end_hour = int(hours) if int(hours) > 0 else 1
            else:
                end_hour = 23 - int(start_time.strftime("%H"))
        end_time = (start_time + timedelta(hours=end_hour, minutes=end_minutes)).strftime("%H:%M")
        c_day, ac_time = start_time.strftime('%A %H:%M').split()
        return c_day, ac_time, end_time

    @staticmethod
    def get_available_slots(b_day: str, b_time: str):
        with open('../../config/course.json') as io_read:
            course = json.load(io_read)['cbse_4']
        main_slots = course['slots']
        i = 0
        for main_slot in main_slots:
            if len(main_slots[main_slot]) == 3:
                slots = ['slot_0', 'slot_1', 'slot_2']
            elif len(main_slots[main_slot]) == 2:
                slots = ['slot_0', 'slot_1']
            elif len(main_slots[main_slot]) == 1:
                slots = ['slot_0']
            elif len(main_slots[main_slot]) == 0:
                slots = list()
            else:
                raise NotImplementedError('slot booking more than three is not yet implemented.')
            for s in slots:
                slot = main_slots[main_slot][s]
                ah, am = tuple(map(int, slot['start_time'].split(":")))
                ch, cm = tuple(map(int, b_time.split(":")))
                if b_day == slot['day']:
                    if ch == ah:
                        if am == cm:
                            return main_slot, slots[i]
                        elif abs((am - cm)) < 2:
                            return main_slot, slots[i]
                i += 1
            i = 0
        return None, None

    def _add_slot(self, booking_time=None, course_id=None):
        def group_name(d, t):
            return "auto_" + str(time.strptime(d, "%A").tm_wday + 1) + ''.join(t.split(":"))
        self.session_relaunch(cms=True)
        self.chrome_driver.get(f"https://tutor-plus-cms-staging.tllms.com/courses/%s" % course_id)
        ms_count = int(self.chrome_driver.find_element_by_xpath(
            '//*[text()="Mandatory Sessions Count"]/following-sibling::*').text)
        self.chrome_driver.get(f"https://tutor-plus-cms-staging.tllms.com/courses/%s/slot_groups/new" % course_id)
        freq = int(self.chrome_driver.find_element("css selector", ".elipseMinus + input").get_attribute("value"))
        slot_count = abs(ms_count - freq)
        if ms_count < freq:
            for _ in range(slot_count):
                self.chrome_driver.find_element("xpath", "//div[@class=\"elipseMinus\"][text()=\"-\"]").click()
        elif ms_count > freq:
            for _ in range(slot_count):
                self.chrome_driver.find_element("xpath", "//div[@class=\"elipseMinus\"][text()=\"+\"]").click()
        number_of_slots = int(len(self.chrome_driver.find_elements('css selector', 'div.slotCardContainer')))
        if ms_count != number_of_slots:
            raise SlotUpdateError("'Mandatory Sessions Count' and 'Number Of Slots' should be same")
        b_day, start_time, end_time = booking_time
        weeks = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Saturday", "Sunday")
        for i, day in enumerate(weeks, 1):
            if day.lower() == b_day.lower():
                index = i
                break
        else:
            raise Exception("DayFormatException: bad day format '%s'" % b_day)
        grp_name = group_name(b_day, start_time)
        self.chrome_driver.find_element_by_css_selector("input.slotNameInput").send_keys(grp_name)
        dropdowns = self.chrome_driver.find_elements(
            By.XPATH, "(//label[text()=\"Day*\"]/../following-sibling::div)//div[text()=\"Select the day\"]")
        items = list(range(1, len(dropdowns)*2, 2))
        for i, dropdown in enumerate(dropdowns):
            dropdown.click()
            self.chrome_driver.find_elements("css selector", "div#menu- .MuiListItem-button")[index+i].click()
            self.chrome_driver.find_element("xpath",
                                            "(//input[@class=\"slotDateInput\"])[%s]" % items[i]
                                            ).send_keys(start_time)
            self.chrome_driver.find_element("xpath",
                                            "(//input[@class=\"slotDateInput\"])[%s]" % (items[i]+1)).send_keys(end_time)
            self.chrome_driver.find_element("xpath", "//div[text()=\"Select Session Type\"][1]").click()
            self.chrome_driver.find_element("xpath", "//li[text()=\"Mandatory\"]").click()
        self.chrome_driver.find_element("css selector", "button.submitButton[type=button]").click()
        new_slot_grp_url = self.chrome_driver.current_url
        try:
            self.chrome_driver.implicitly_wait(30)
            self.chrome_driver.find_element("xpath", "//span[text()=\"Create New Slot Group\"]")
        except NoSuchElementException:
            pass
        timeout = 30
        while timeout:
            if self.chrome_driver.current_url != new_slot_grp_url:
                self.chrome_driver.quit()
                break
            else:
                timeout -= 1
                sleep(1)
        else:
            self.chrome_driver.quit()
            raise SlotUpdateError("Cannot update slot in 'https://tutor-plus-cms-staging.tllms.com/'")

    def verify_and_add_slot(self, cohort, course_tag, hours=None, minutes=None, end_hour=None, end_minutes=0, day=None):
        """
        Example:
        cohort - 14 (for 8th CBSE)
        course_tag - free trial or masterclass
        """
        with open('../../config/course.json') as io_read:
            course = json.load(io_read)["cbse"][cohort][course_tag]
        course_id = course['id']
        b_day, start_time, *_ = b_time = self.booking_time(
            hours=hours, minutes=minutes, day=day, end_hour=end_hour, end_minutes=end_minutes)
        # available_slots = self.get_available_slots(b_day, start_time)
        # if all(available_slots) is False:
        slot = self._add_slot(b_time, course_id)
        # with open('../../config/slots.json', 'r+') as io_write:
        #     course = json.load(io_write)
        #     io_write.seek(0)
        #     course['cbse_4']['slots'].update(slot)
        #     json.dump(course, io_write, indent=2)
        # else:
        #     return available_slots

    def student_session_details(self, days, profile, user_profile, sub_profile):
        # self.attach_session_video(profile, user_profile, sub_profile, session=days)
        self._session_user_wise(session=days, profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        headers = self.chrome_driver.find_elements("css selector", "thead > tr > th")
        content_rows = self.chrome_driver.find_elements("css selector", "tbody > tr")
        session_details = dict()
        session_list = list()
        for j, row in enumerate(content_rows, 1):
            if j % 2 != 0:
                contents_row = row.find_elements("css selector", "td")
                for i, header in enumerate(headers):
                    if header.text.strip() != "":
                        session_details.update({header.text.strip().lower(): contents_row[i].text.strip()})
                session_list.append(session_details.copy())
        return session_list

    def modify_test_requisite_assessment(self, channel_id, field, day, status):
        """
        """
        if channel_id is None:
            self.session_relaunch()
            with open("../../test_data/classroom_details.json") as fd:
                channel_id = json.load(fd)["channel"]
        self.chrome_driver.get("https://tutor-plus-staging.tllms.com/studentSessions/%s" % channel_id)
        self.chrome_driver.find_element(By.XPATH, '//span[text()="LOGIN"]').click()
        self.chrome_driver.implicitly_wait(15)
        asset_id = self.chrome_driver.find_element("xpath",
                                                   "//*[text()=\"OneToMany::TestRequisite\"]/../..//*[text("
                                                   ")=\"ASSESSMENT_ID\"]/following-sibling::td").text
        self.chrome_driver.get("https://staging.tllms.com/admin/assessments/%s/edit" % asset_id)
        if status == "expire":
            if day == "yesterday":
                date_time = (datetime.now() + timedelta(days=-1)).strftime("%d-%m-%Y %H:%M")
            elif day == "today":
                date_time = (datetime.now() + timedelta(minutes=-2)).strftime("%d-%m-%Y %H:%M")
            else:
                raise NotImplementedError()
            date_time_list = date_time.split(":")
            minutes = date_time_list.pop()
            # date_time_list.append("00" if int(minutes) <= 5 else "10")
            # date_time = ":".join(date_time_list)
            if field.lower() == "start_time":
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_starting").click()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_starting").send_keys(date_time)
            elif field.lower() == "end_time":
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_until").click()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_until").send_keys(date_time)
            elif field.lower() == "result_time":
                self.chrome_driver.find_element(
                    "css selector", "#assessment_send_results_at").clear()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_send_results_at").send_keys(date_time)
            else:
                raise NotImplementedError()
            self.chrome_driver.find_element("css selector", "input[name=commit]").click()
        else:
            raise NotImplementedError()

    def modify_test_requisite_assessment(self, channel_id, field, day, status,time=None):
        """
        """
        if channel_id is None:
            self.session_relaunch()
            with open("../../test_data/classroom_details.json") as fd:
                channel_id = json.load(fd)["channel"]
        if not self.chrome_driver.find_element(*self.assessment_text).text.lower() == "assessment session":
            self.chrome_driver.get("https://tutor-plus-staging.tllms.com/studentSessions/%s" % channel_id)
            self.chrome_driver.find_element(By.XPATH, '//span[text()="LOGIN"]').click()
        self.chrome_driver.implicitly_wait(15)
        asset_id = self.chrome_driver.find_element("xpath",
                                                   "//*[text()=\"OneToMany::TestRequisite\"]/../..//*[text("
                                                   ")=\"ASSESSMENT_ID\"]/following-sibling::td").text
        self.chrome_driver.get("https://staging.tllms.com/admin/assessments/%s/edit" % asset_id)
        if status == "expire":
            if day == "yesterday":
                date_time = (datetime.now() + timedelta(days=-1)).strftime("%d-%m-%Y %H:%M")
            elif day == "today":
                date_time = (datetime.now() + timedelta(minutes=-2)).strftime("%d-%m-%Y %H:%M")
            else:
                raise NotImplementedError()
            date_time_list = date_time.split(":")
            minutes = date_time_list.pop()

            date_time_list.append("00" if int(minutes) <= 5 else "10")
            date_time = ":".join(date_time_list)
            if time is not None:
                date_time = time.strftime("%d-%m-%Y %H:%M")
            if field.lower() == "start_time":
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_starting").click()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_starting").send_keys(date_time)
            elif field.lower() == "end_time":
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_until").click()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_until").clear()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_until").send_keys(date_time)
            elif field.lower() == "result_time":
                self.chrome_driver.find_element(
                    "css selector", "#assessment_send_results_at").clear()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_send_results_at").send_keys(date_time)
            else:
                raise NotImplementedError()
            self.chrome_driver.find_element("css selector", "input[name=commit]").click()
        else:
            raise NotImplementedError()


    def change_assessment_time(self,db,minutes_to_add=0,current=True):
        sd = db.sd
        if current:
            time_required = datetime.strptime(datetime.now().strftime('%d-%b-%Y %H:%M'), '%d-%b-%Y %H:%M')
            two_minute = timedelta(minutes_to_add=2)
            time_required_new = time_required + two_minute
        else:
            # time_of_interest = sd[0]['time']
            # time_of_interest = time_of_interest.split("\n")[1].split("-")[1]
            time_list = sd[0]['time'].replace("\n", " ").split(" - ")
            date = time_list[0].split(" ")[0]
            new_timelist = []
            new_timelist.append(date)
            new_timelist.append(" " + time_list[1])
            new_time = "".join(new_timelist)
            time_required = datetime.strptime(new_time, '%d-%b-%Y %H:%M')
            two_minute = timedelta(minutes=2)
            time_required_new = time_required + two_minute

        self.modify_test_requisite_assessment(sd[0]['channel'], field="end_time", day='today', status='expire',
                                          time=time_required_new)