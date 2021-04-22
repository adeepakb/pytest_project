import json
import os
import re
from random import randint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.load_json import getdata
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
import time
from utilities.tutor_common_methods import TutorCommonMethods


class Stagingtlms:

    def __init__(self, driver):
        self.driver = driver
        self.obj = TutorCommonMethods(driver)
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)

    def login_to_staging(self):
        email = str(getdata('../config/config.json', 'staging_access', 'email'))
        password = str(getdata('../config/config.json', 'staging_access', 'password'))

        self.chrome_driver.get('https://staging.tllms.com/admin')
        self.chrome_driver.maximize_window()
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

    def get_tutor_url(self, course='primary', premium_id='primary'):
        email = str(getdata('../config/config.json', 'staging_access', 'email'))
        today = datetime.today().strftime('%Y-%m-%d')
        if course == 'primary':
            session_course_id = str(getdata('../config/login_data.json', 'login_detail3', 'course_id_primary'))
            premium_id = str(getdata('../config/config.json', 'account_details', 'premium_id'))
        elif course == 'secondary':
            session_course_id = str(getdata('../config/login_data.json', 'login_detail3', 'course_id_secondary'))
            premium_id = str(getdata('../config/config.json', 'account_details', 'premium_id'))
        elif course == 'ternary':
            session_course_id = str(getdata('../config/login_data.json', 'login_detail3', 'course_id_ternary'))
            premium_id = str(getdata('../config/login_data.json', 'login_detail3', 'free_user_premium_id'))

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
                elif 'FREE' in status:
                    self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        email_col) + "]/li[@id='teacher_email_input']/input[@id='teacher_email']").clear()
                    self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        email_col) + "]/li[@id='teacher_email_input']/input[@id='teacher_email']").send_keys(email)
                    tutor_url = self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        meeting_col) + "]/li[@id='meeting_url_input']/input[@id='meeting_url']").get_attribute('value')
            except NoSuchElementException:
                continue

        self.chrome_driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
        self.chrome_driver.close()
        return tutor_url

    def reset_session(self, course='primary'):
        premium_id = str(getdata('../config/config.json', 'account_details', 'premium_id'))
        today = datetime.today().strftime('%Y-%m-%d')
        if course == 'primary':
            session_course_id = str(getdata('../config/login_data.json', 'login_detail3', 'course_id_primary'))
            premium_id = str(getdata('../config/config.json', 'account_details', 'premium_id'))
        elif course == 'secondary':
            session_course_id = str(getdata('../config/login_data.json', 'login_detail3', 'course_id_secondary'))
            premium_id = str(getdata('../config/config.json', 'account_details', 'premium_id'))
        elif course == 'ternary':
            session_course_id = str(getdata('../config/login_data.json', 'login_detail1', 'course_id'))
            premium_id = str(getdata('../config/login_data.json', 'login_detail1', 'premium_id'))

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

    @staticmethod
    def get_mobile_and_ccode():
        mobile = str(getdata('../config/config.json', 'account_details', 'mobile'))
        return mobile

    def get_otp(self, account_type='many'):
        if account_type == 'many':
            complete_mobile = self.get_mobile_and_ccode()
        elif account_type == 'asset_not_tagged_account_details':
            complete_mobile = str(getdata('../config/config.json', 'asset_not_tagged_account_details', 'mobile'))
        self.login_to_staging()
        self.wait_for_locator_webdriver("//li[@id='otp']")
        self.chrome_driver.find_element_by_xpath("//li[@id='otp']").click()
        self.wait_for_locator_webdriver("//li[@id='mobile_otps']")
        self.chrome_driver.find_element_by_xpath("//li[@id='mobile_otps']").click()
        self.chrome_driver.find_element_by_css_selector("#q_mobile_no").send_keys(complete_mobile)
        self.obj.wait_for_locator('xpath', "//*[@name='commit']", 3)
        self.chrome_driver.find_element_by_xpath("//*[@name='commit']").click()
        otp = self.chrome_driver.find_element_by_css_selector("td.col-otp").text
        self.chrome_driver.close()
        return otp

    def wait_for_locator_webdriver(self, locator_value):
        try:
            WebDriverWait(self.chrome_driver, 15, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.presence_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_clickable_element_webdriver(self, locator_value):
        try:
            WebDriverWait(self.chrome_driver, 15).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_element_not_present_webdriver(self, locator_value):
        try:
            WebDriverWait(self.chrome_driver, 15).until(EC.invisibility_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def select_course(self, course_id):
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

    def select_topic_and_update_teaching_material(self, topic_id):
        teaching_material = str(getdata('../config/config.json', 'update_pdf_in_cms_details', 'teaching_material'))

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
        email = str(getdata('../config/config.json', 'staging_access', 'email'))
        password = str(getdata('../config/config.json', 'staging_access', 'password'))
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
        self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(Keys.ENTER)
        self.wait_for_clickable_element_webdriver("//input[@type='password']")
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(Keys.ENTER)

    def update_teaching_material(self, course_details):
        print(course_details)
        course_id = re.search(r'^.*?\bCourse id : (\d+)', course_details).group(1)
        topic_id = re.search(r'Topic id ?: (\d+)', course_details).group(1)
        self.login_to_cms_staging()
        self.select_course(course_id)
        self.select_topic_and_update_teaching_material(topic_id)
        self.chrome_driver.close()

    def is_session_present_today(self):
        premium_id = str(getdata('../config/config.json', 'account_details', 'premium_id'))
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
        premium_id = str(getdata('../config/config.json', 'asset_not_tagged_account_details', 'premium_id'))
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
        email = str(getdata('../config/config.json', 'staging_access', 'email'))
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
        premium_id = str(getdata('../config/config.json', 'account_details', 'premium_id'))
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
                    self.chrome_driver.switch_to_window(self.chrome_driver.window_handles[1])
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
                        WebDriverWait(self.chrome_driver, 5).until(EC.alert_is_present(),
                                                                   'Timed out waiting for confirmation popup to appear.')
                        alert = self.chrome_driver.switch_to.alert
                        alert.accept()
                        print("alert accepted")
                        time.sleep(2)
                    except TimeoutException:
                        print("no alert")
                    self.chrome_driver.close()
                    self.chrome_driver.switch_to_window(self.chrome_driver.window_handles[0])
            except NoSuchElementException:
                continue
        self.chrome_driver.close()

    def detach_requisite(self):
        premium_id = str(getdata('../config/config.json', 'account_details', 'premium_id'))
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
                    self.chrome_driver.switch_to_window(self.chrome_driver.window_handles[1])
                    self.wait_for_locator_webdriver("//a[text()='Detach Requisite Group']")
                    self.chrome_driver.find_element_by_xpath("//a[text()='Detach Requisite Group']").click()
                    try:
                        WebDriverWait(self.chrome_driver, 5).until(EC.alert_is_present(),
                                                                   'Timed out waiting for confirmation popup to appear.')
                        alert = self.chrome_driver.switch_to.alert
                        alert.accept()
                        print("alert accepted")
                        time.sleep(2)
                    except TimeoutException:
                        print("no alert")
                    self.chrome_driver.close()
                    self.chrome_driver.switch_to_window(self.chrome_driver.window_handles[0])
            except NoSuchElementException:
                continue
        self.chrome_driver.close()

    def upload_class_note(self, filename):
        tnl_cohort_id = str(getdata('../config/login_data.json', 'login_detail3', 'tnl_cohort_id'))
        self.wait_for_clickable_element_webdriver("//div[text()='Class Notes']")
        self.chrome_driver.find_element_by_xpath("//div[text()='Class Notes']").click()
        self.wait_for_clickable_element_webdriver("//div[text()='Upload']")
        self.chrome_driver.find_element_by_xpath("//div[text()='Upload']").click()

        note_name = 'Class_note_' + str(randint(1, 100000))
        self.chrome_driver.find_element_by_xpath("//input[@id='name']").send_keys(note_name)
        input_element = self.chrome_driver.find_element_by_xpath("//input[@type='file']")
        current_location = os.path.dirname(os.path.abspath(__file__))
        location = os.path.normpath(os.path.join(current_location, "../../files/" + filename + ""))
        input_element.send_keys(location)

        self.chrome_driver.find_element_by_xpath("//*[contains(@class,'MuiInputBase-formControl MuiInput-formControl')]").click()
        time.sleep(2)
        self.chrome_driver.find_element_by_xpath("//*[@role='option' and text()='" + tnl_cohort_id + "']").click()
        self.chrome_driver.find_element_by_xpath("//span[text()='Submit']").click()
        return note_name

    def verify_classnote_upload_error(self):
        self.wait_for_locator_webdriver("//span[@id='message-id']")
        if self.chrome_driver.find_element_by_xpath("//span[@id='message-id']").text == 'file size should not be more than 15MB':
            return True

    def incorrect_note_format_error(self):
        self.wait_for_locator_webdriver("//span[@id='message-id']")
        if self.chrome_driver.find_element_by_xpath("//span[@id='message-id']").text == 'File type is invalid':
            return True

    def update_post_requisite_class_note(self, requisite_name, class_note_id):
        self.login_to_cms_staging()
        self.wait_for_locator_webdriver("//div[text()='Requisite Groups']")
        self.chrome_driver.find_element_by_xpath("//div[text()='Requisite Groups']").click()
        self.wait_for_locator_webdriver("//span[text()='Un Publish']")
        self.chrome_driver.find_element_by_xpath("//span[text()='Un Publish']").click()

        id_col = requisite_name_col = None
        rows = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root table')]/tbody/tr"))
        cols = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root table')]/thead/tr/th"))
        for i in range(1, cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'MuiTable-root table')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'ID':
                id_col = i
            elif header == 'Requisite':
                requisite_name_col = i
        for r in range(1, rows + 1):
            name = self.chrome_driver.find_element_by_xpath(
                "//tr[" + str(r) + "]/td[" + str(requisite_name_col) + "]").text
            if name == requisite_name:
                self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(id_col) + "]/div/span").click()
                break

        self.wait_for_locator_webdriver("//input[@id='class_note_id']")
        self.chrome_driver.find_element_by_xpath("//input[@id='class_note_id']").clear()
        self.chrome_driver.find_element_by_xpath("//input[@id='class_note_id']").send_keys(class_note_id)
        self.chrome_driver.find_element_by_xpath("//span[text()='Update']").click()
        self.wait_for_clickable_element_webdriver("//span[text()='Publish']")
        self.chrome_driver.find_element_by_xpath("//span[text()='Publish']").click()
        self.chrome_driver.close()

    @staticmethod
    def booking_time(hours, minutes, day=None):
        time_now = datetime.now()
        if day is not None and day.lower() == 'tomorrow':
            n_day = (time_now + timedelta(days=1)).strftime("%A")
            return n_day, "8:00", "23:00"
        if minutes is None:
            mins = 32
        else:
            mins = 30 + int(minutes)
        if int(time_now.strftime("%S")) >= 45:
            time_now = datetime.now()
            mins = 33 if minutes is None else 30 + int(minutes) + 1
        start_time = (time_now + timedelta(hours=0, minutes=mins))
        if hours is not None:
            end_hour = int(hours) if int(hours) > 0 else 1
        else:
            end_hour = 23 - int(start_time.strftime("%H"))
        end_time = (start_time + timedelta(hours=end_hour, minutes=0)).strftime("%H:%M")
        c_day, ac_time = start_time.strftime('%A %H:%M').split()
        return c_day, ac_time, end_time

    # todo: change implementation
    def _add_slot(self, booking_time=None, course_id=None):
        def group_name(d, t):
            return "auto_" + str(time.strptime(d, "%A").tm_wday + 1) + ''.join(t.split(":"))

        # self.session_relaunch(cms=True)
        self.chrome_driver.get(f"https://tutor-plus-cms-staging.tllms.com/courses/%s/slot_groups/new" % course_id)
        number_of_slots = self.chrome_driver.find_elements('css selector', 'div.slotCardContainer')
        if len(number_of_slots) == 1:
            b_day, start_time, end_time = booking_time
            weeks = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Saturday", "Sunday")
            for i, day in enumerate(weeks):
                if day.lower() == b_day.lower():
                    index = i
                    break
            else:
                raise Exception("DayFormatException: bad day format '%s'" % b_day)
            grp_name = group_name(b_day, start_time)
            self.chrome_driver.find_element_by_css_selector("input.slotNameInput").send_keys(grp_name)
            self.chrome_driver.find_element("css selector", "div.MuiInput-input").click()
            self.chrome_driver.find_elements("css selector", "div#menu- .MuiListItem-button")[index].click()
            self.chrome_driver.find_element("css selector",
                                            "div.slotContent > div:nth-child(2) input.slotInput").send_keys(start_time)
            self.chrome_driver.find_element("css selector",
                                            "div.slotContent > div:nth-child(3) input.slotInput").send_keys(end_time)
            self.chrome_driver.find_element("css selector", "button[type=button]").click()
            new_slot_grp_url = self.chrome_driver.current_url
            try:
                self.chrome_driver.implicitly_wait(30)
                self.chrome_driver.find_element("xpath", "//span[text()=\"Add New Slot Group\"]")
            except NoSuchElementException:
                pass
            timeout = 30
            while timeout:
                if self.chrome_driver.current_url != new_slot_grp_url:
                    self.chrome_driver.quit()
                    break
                else:
                    timeout -= 1
                    time.sleep(1)
            else:
                self.chrome_driver.quit()
                raise Exception("Cannot update slot in 'https://tutor-plus-cms-staging.tllms.com/'")
            return {
                grp_name: {
                    "slot_0": {
                        "day": b_day,
                        "start_time": start_time,
                        "end_time": end_time
                    }
                }
            }
        else:
            NotImplementedError("Booking for more than one slot is not yet implemented.")

    def verify_and_add_slot(self, hours=None, minutes=None, day=None):
        with open('../../config/course.json') as io_read:
            course = json.load(io_read)['cbse_4']
        course_id = course['id']
        b_day, start_time, *_ = b_time = self.booking_time(hours, minutes, day)
        # available_slots = self.get_available_slots(b_day, start_time)
        # if all(available_slots) is False:
        slot = self._add_slot(b_time, course_id)
        with open('../../config/course.json', 'r+') as io_write:
            course = json.load(io_write)
            io_write.seek(0)
            course['cbse_4']['slots'].update(slot)
            json.dump(course, io_write, indent=2)
        # else:
        #     return available_slots
