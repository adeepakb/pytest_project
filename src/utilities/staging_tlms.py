import json
import os
import random
import re
import string
from cryptography.fernet import Fernet
from random import randint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.load_json import get_data
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
import time
from utilities.exceptions import SlotUpdateError, AttachmentError, InvalidModeSelection
from utilities.tutor_common_methods import TutorCommonMethods


class Stagingtlms:

    def __init__(self, driver):
        self.driver = driver
        self.obj = TutorCommonMethods(driver)
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
        key = os.getenv('SECRET')
        f = Fernet(key)
        encrypted_data = get_data('../config/config.json', 'encrypted_data', 'token')
        self.decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))

    def login_to_staging(self):
        email = self.decrypted_data['staging_access']['email']
        password = self.decrypted_data['staging_access']['password']
        self.chrome_driver.get('https://staging.tllms.com/admin')
        self.chrome_driver.maximize_window()
        self.wait_for_locator_webdriver("//input[@id='email']")
        self.chrome_driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        self.wait_for_locator_webdriver("//button[@type='submit']")
        self.chrome_driver.find_element_by_xpath("//button[@type='submit']").click()
        self.wait_for_locator_webdriver("//input[@type='email']")
        self.chrome_driver.save_screenshot('image1.png')
        self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
        self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(Keys.ENTER)
        self.chrome_driver.save_screenshot('image2.png')
        self.wait_for_clickable_element_webdriver("//input[@type='password']")
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(Keys.ENTER)
        self.chrome_driver.save_screenshot('image3.png')

    def navigate_to_student_sessions(self, premium_id, date='today'):
        # today = datetime.today().strftime('%Y-%m-%d')
        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//*[text()='Mentoring']")
        self.chrome_driver.find_element_by_xpath("//*[text()='Mentoring']").click()
        self.wait_for_clickable_element_webdriver("//*[text()='1:M - Schedule Student Sessions']")
        self.chrome_driver.find_element_by_xpath("//*[text()='1:M - Schedule Student Sessions']").click()
        self.wait_for_locator_webdriver("//a[text()='Scheduling Sessions(User Wise)']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Scheduling Sessions(User Wise)']").click()
        self.wait_for_locator_webdriver("//input[@id ='target_date']")
        if date == 'today':
            date = datetime.today().strftime('%Y-%m-%d')
            self.chrome_driver.find_element_by_xpath("//input[@id ='target_date']").send_keys(date)
        elif date == 'tomorrow':
            self.chrome_driver.find_element_by_xpath("//input[@id ='target_date']").click()
            next_calender_sibling = "//td/a[contains(@class,'ui-state-highlight ui-state-active')]/parent::td/following-sibling::td[1]/a"
            self.wait_for_clickable_element_webdriver(next_calender_sibling)
            self.chrome_driver.find_element_by_xpath(next_calender_sibling).click()
        self.wait_for_locator_webdriver("//input[@id ='premium_account_id']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='premium_account_id']").send_keys(premium_id)
        self.wait_for_locator_webdriver("//input[@value ='Start Scheduling']")
        self.chrome_driver.find_elements_by_xpath("//input[@value ='Start Scheduling']")[1].click()


    def get_tutor_url(self, course='primary', login_data="neo_login_detail1", user='student1', date='today'):
        email = self.decrypted_data['staging_access']['email']
        session_course_id = premium_id = None
        if course == 'primary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_primary'))
            premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'premium_id'))
        elif course == 'secondary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_secondary'))
            premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'premium_id'))
        elif course == 'ternary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_ternary'))
            premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'free_user_premium_id'))
        elif course == 'neo':
            neo_details = get_data('../config/login_data.json', login_data, user)
            premium_id = neo_details['premium_id']
        self.navigate_to_student_sessions(premium_id, date)
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
                tagged_col_status = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(tagged_col) + "]").text
                if 'neo' in tagged_col_status:
                    self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        status_col) + "]/li[@id='teacher_email_input']/input[@id='teacher_email']").clear()
                    self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        status_col) + "]/li[@id='teacher_email_input']/input[@id='teacher_email']").send_keys(email)
                    tutor_url = self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        status_col) + "]/li[@id='meeting_url_input']/input[@id='meeting_url']").get_attribute('value')
                    break
                status = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(status_col) + "]").text
                # incase of multiple sessions in same day
                course_details = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(tagged_col) + "]/div[@class='course_details']").text
                course_id = re.search(r'^.*?\bCourse id : (\d+)', course_details).group(1)
                if 'one_to_mega' in status and course_id == session_course_id or 'FREE' in status:
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
        self.chrome_driver.close()
        return tutor_url

    def reset_session(self, course='primary'):
        premium_id = None
        today = datetime.today().strftime('%Y-%m-%d')
        if course == 'primary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_primary'))
            premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'premium_id'))
        elif course == 'secondary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_secondary'))
            premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'premium_id'))
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

    def get_mobile_and_ccode(self):
        mobile = self.decrypted_data['account_details']['mobile']
        return mobile

    def get_otp(self, cc, mobile_num):
        self.login_to_staging()
        self.wait_for_locator_webdriver("//li[@id='otp']")
        self.chrome_driver.save_screenshot('image5.png')
        self.chrome_driver.find_element_by_xpath("//li[@id='otp']").click()
        self.wait_for_clickable_element_webdriver("//li[@id='mobile_otps']")
        self.chrome_driver.find_element_by_xpath("//li[@id='mobile_otps']").click()
        self.chrome_driver.find_element_by_css_selector("#q_mobile_no").send_keys(cc + "" + mobile_num)
        self.obj.wait_for_locator('xpath', "//*[@name='commit']", 5)
        self.chrome_driver.find_element_by_xpath("//*[@name='commit']").click()
        self.wait_for_locator_webdriver("//*[contains(@id,mobile_otp)]")
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
        teaching_material = self.decrypted_data['update_pdf_in_cms_details']['teaching_material']
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
        email = self.decrypted_data['staging_access']['email']
        password = self.decrypted_data['staging_access']['password']

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
        self.wait_for_locator_webdriver("//img[@alt='titleLogo']")

    def update_teaching_material(self, course_details):
        print(course_details)
        course_id = re.search(r'^.*?\bCourse id : (\d+)', course_details).group(1)
        topic_id = re.search(r'Topic id ?: (\d+)', course_details).group(1)
        self.login_to_cms_staging()
        self.select_course(course_id)
        self.select_topic_and_update_teaching_material(topic_id)
        self.chrome_driver.close()

    def is_session_present_today(self):
        premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'premium_id'))
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
        email = self.decrypted_data['staging_access']['email']
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

    def attach_requisite(self, requisite_id):
        premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'premium_id'))
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
        status_col = tagged_col = None
        for i in range(1, cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'index_table')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'Status':
                status_col = i
            elif header == 'Teaching Material/Video Tagged':
                tagged_col = i

        topic_id = None
        for r in range(1, rows + 1):
            try:
                status = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(status_col) + "]").text
                if 'one_to_mega' in status:
                    course_topic_details = self.chrome_driver.find_element_by_xpath(
                        "//tr[" + str(r) + "]/td[" + str(tagged_col) + "]/div[@class='course_details']").text
                    topic_id = re.search(r'Topic id : (\d+)', course_topic_details).group(1)
            except NoSuchElementException:
                continue

        tmb_id = get_data("../config/attachments.json", "one_to_mega", '8')["tmb_id"]
        uri = "tmbs/%s" % tmb_id
        tmb_name = get_data("../config/attachments.json", "one_to_mega", '8')["tmb_name"]
        self.chrome_driver.get('https://tutor-plus-cms-staging.tllms.com/' + uri)
        self.chrome_driver.find_element_by_xpath('//span[text()="LOGIN"]').click()
        self.wait_for_locator_webdriver("//button[label=Requisites]")
        self.chrome_driver.find_element("css selector", "button[label=Requisites]").click()
        self.chrome_driver.find_element("xpath",
                                        "//div[contains(text(), '14-8th Grade Marketing-Standard VIII-CBSE')]/../..//a[contains(text(), \"RG\")]").click()
        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[-1])
        input_box = self.chrome_driver.find_element(By.CSS_SELECTOR, ".input-box")
        input_box.clear()
        input_box.send_keys(requisite_id)
        time.sleep(1)
        self.chrome_driver.find_element(By.CSS_SELECTOR, "button[label=Save]").click()
        attached_id = self.chrome_driver.find_element("xpath",
                                                      "//div[contains(text(), '14-8th Grade Marketing-Standard VIII-CBSE')]/../..//span[@class=\"requisite_group_id\"]").text
        if requisite_id != attached_id:
            raise AttachmentError("'Requisite Group' attachment might not be successful.")
        self._attachment_write(tmb_id, tmb_name, topic_id)
        self.chrome_driver.close()

    def _attachment_write(self, tmb_id, tmb_name=None, topic_id=None):
        if tmb_id is None:
            raise TypeError("'tmb_id' must be str, not None")
        topics_uri = 'raw_topics/%s'
        topic_id = int(topic_id)
        self.chrome_driver.get('https://tutor-plus-cms-staging.tllms.com/' + (topics_uri % topic_id))
        try:
            self.chrome_driver.find_element_by_xpath('//span[text()="LOGIN"]').click()
        except NoSuchElementException:
            pass
        self.wait_for_locator_webdriver("//div[text()='Edit']")
        self.chrome_driver.find_element("css selector", "button[label=Edit]").click()
        drp_box_input = self.chrome_driver.find_element(
            "xpath", "//div[contains(text(), \"TMB\")]/following-sibling::div//input")
        drp_box_input.clear()
        drp_box_input.click()
        drp_box_input.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        drp_box_input.send_keys(tmb_name)
        retry = 3
        while retry:
            list_options = self.chrome_driver.find_elements("css selector", ".tmbTagOption .tagOptionIdText")
            if len(list_options) != 0:
                try:
                    for option in list_options:
                        if option.text == tmb_id:
                            option.click()
                            break
                    else:
                        if retry < 1:
                            raise Exception(f"ID Error: \"{tmb_id}\" is not displayed in the list")
                    break
                except StaleElementReferenceException:
                    pass
            retry -= 1
            time.sleep(0.5)
        else:
            raise Exception("<Empty List>: contents might have taken too long to load")
        chapter_input = self.chrome_driver.find_element("css selector", "input[placeholder=\"Enter Chapter\"]")
        chapter_input.clear()
        chapter_input.send_keys("null")
        self.chrome_driver.find_element("css selector", "button[label=Save]").click()
        try:
            missing_param = self.chrome_driver.find_element("id", "message-id").text
            print("missing param........................", missing_param)
            raise AttachmentError(missing_param)
        except NoSuchElementException:
            pass

    def detach_requisite(self):
        premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'premium_id'))
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
        tnl_cohort_id = str(get_data('../config/login_data.json', 'login_detail3', 'tnl_cohort_id'))
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

        self.chrome_driver.find_element_by_xpath(
            "//*[contains(@class,'MuiInputBase-formControl MuiInput-formControl')]").click()
        time.sleep(2)
        self.chrome_driver.find_element_by_xpath("//*[@role='option' and text()='" + tnl_cohort_id + "']").click()
        self.chrome_driver.find_element_by_xpath("//span[text()='Submit']").click()
        return note_name

    def verify_classnote_upload_error(self):
        self.wait_for_locator_webdriver("//span[@id='message-id']")
        if self.chrome_driver.find_element_by_xpath(
                "//span[@id='message-id']").text == 'file size should not be more than 15MB':
            return True

    def incorrect_note_format_error(self):
        self.wait_for_locator_webdriver("//span[@id='message-id']")
        if self.chrome_driver.find_element_by_xpath("//span[@id='message-id']").text == 'File type is invalid':
            return True

    def update_post_requisite_class_note(self, requisite_name, class_note_id):
        self.login_to_cms_staging()
        self.wait_for_locator_webdriver("//div[text()='Requisite Groups']")
        self.chrome_driver.find_element_by_xpath("//div[text()='Requisite Groups']").click()

        self.chrome_driver.execute_script("document.body.style.zoom='88%'")
        id_col = requisite_name_col = action_col = None
        page_num = 1
        rows = len(
            self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root table')]/tbody/tr"))
        cols = len(
            self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root table')]/thead/tr/th"))
        for i in range(1, cols + 1):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'MuiTable-root table')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'ID':
                id_col = i
            elif header == 'Requisite':
                requisite_name_col = i
            elif header == 'Action':
                action_col = i
        for r in range(1, rows + 1):
            req_name_element = self.chrome_driver.find_element_by_xpath(
                "//tr[" + str(r) + "]/td[" + str(requisite_name_col) + "]/div[contains(@class,'tableBodyTextStyle')]")
            name = req_name_element.text
            if name == requisite_name:
                self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(action_col) + "]/div/button/span[text()='Un Publish']").click()
                self.wait_for_element_not_present_webdriver(
                    "//tr[" + str(r) + "]/td[" + str(action_col) + "]/div/button/span[text()='Un Publish']")
                req_id_element = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(id_col) + "]/div/span")
                self.chrome_driver.execute_script("arguments[0].click();", req_id_element)
                self.wait_for_locator_webdriver("//input[@id='class_note_id']")
                self.chrome_driver.find_element_by_xpath("//input[@id='class_note_id']").clear()
                self.chrome_driver.find_element_by_xpath("//input[@id='class_note_id']").send_keys(class_note_id)
                self.chrome_driver.find_element_by_xpath("//span[text()='Update']").click()
                self.wait_for_clickable_element_webdriver(
                    "//tr[" + str(r) + "]/td[" + str(action_col) + "]/div/button/span[text()='Publish']")
                self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(action_col) + "]/div/button/span[text()='Publish']").click()
                self.chrome_driver.close()
                break
            if r == rows:
                # svg_icons = self.chrome_driver.find_elements_by_xpath("//*[@type='button']")
                # length = len(svg_icons)
                # svg_icons[length - 1].click()  # click on next for pagination
                # page_num += 1
                # xpath = "//*[@class='MuiButton-label' and text()='"+str(page_num)+"']"
                # icon = self.chrome_driver.find_element_by_xpath(xpath)
                # icon.click()
                page_num += 1
                uri = "requisite_groups?page=%s" % page_num
                self.chrome_driver.get('https://tutor-plus-cms-staging.tllms.com/' + uri)
                self.chrome_driver.execute_script("document.body.style.zoom='88%'")
                r = 1

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

    def _add_slot(self, booking_time=None, new_course_id=None):
        def group_name(d, t):
            return "auto_" + str(time.strptime(d, "%A").tm_wday + 1) + ''.join(t.split(":"))

        # self.session_relaunch(cms=True)
        self.chrome_driver.get(
            f"https://tutor-plus-cms-staging.tllms.com/neo_courses/%s/slot_groups/new" % new_course_id)
        ms_count = 1
        self.wait_for_locator_webdriver("//div[@class='subheader--title']")
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
        items = list(range(1, len(dropdowns) * 2, 2))
        for i, dropdown in enumerate(dropdowns):
            dropdown.click()
            index = index if index + i < 8 else 0
            self.chrome_driver.find_elements("css selector", "div#menu- .MuiListItem-button")[index + i].click()
            self.chrome_driver.find_element("xpath",
                                            "(//input[@class=\"slotInput\"])[%s]" % items[i]
                                            ).send_keys(start_time)
            self.chrome_driver.find_element("xpath",
                                            "(//input[@class=\"slotInput\"])[%s]" % (items[i] + 1)).send_keys(
                end_time)
            self.chrome_driver.find_element("xpath", "//div[text()=\"Select Session Type\"][1]").click()
            self.chrome_driver.find_element("xpath", "//li[text()=\"Mandatory\"]").click()
        self.chrome_driver.find_element("css selector", "button.submitButton[type=button]").click()
        new_slot_grp_url = self.chrome_driver.current_url
        try:
            self.wait_for_locator_webdriver("//div[text()='Create New Slot Group']")
            self.chrome_driver.find_element("xpath", "//div[text()='Create New Slot Group']")
        except NoSuchElementException:
            pass
        timeout = 30
        while timeout:
            if self.chrome_driver.current_url != new_slot_grp_url:
                ths = self.chrome_driver.find_elements("css selector", ".tableHeaderTextStyle")
                id_index = [ths.index(i) for i in ths if i.text.lower() == "id"][-1]
                tds = self.chrome_driver.find_elements("css selector", ".tableBodyTextStyle span")
                sl_id, sl_name = tds[id_index].text, tds[id_index + 1].text
                return sl_id, sl_name
            else:
                timeout -= 1
                time.sleep(1)
        else:
            self.chrome_driver.quit()
            raise SlotUpdateError(
                f"Cannot update slot in "
                f"'https://tutor-plus-cms-staging.tllms.com/neo_courses/{new_course_id}/slot_groups'")

    def _add_batch(self, new_course_id, *slot_details):
        uri = "neo_courses/%s" % new_course_id
        url = 'https://tutor-plus-cms-staging.tllms.com/' + uri
        new_batch_url = url + "/batches/new"
        self.chrome_driver.get(url)
        self.wait_for_locator_webdriver('//div[text()="Create New Batch"]')
        self.chrome_driver.find_element("css selector", ".batches-container .btn").click()
        batch_input, slot_drp_dwn, topic_drp_dwn = self.chrome_driver.find_elements("css selector", "input[type=text]")
        date_fields = self.chrome_driver.find_elements("css selector", "input[type=date]")
        topic_count = self.chrome_driver.find_element("css selector", "input[type=number]")
        today, tomorrow = datetime.today().strftime('%m%d%Y'), (datetime.today() + timedelta(days=1)).strftime('%m%d%Y')
        batch_name = "test_batch_" + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
        batch_input.send_keys(batch_name)
        slot_drp_dwn.click()
        slot_id, slot_grp_name = slot_details
        for char in slot_grp_name:
            slot_drp_dwn.send_keys(char)
            time.sleep(0.15)
        drp_dwn_ids = self.chrome_driver.find_elements("css selector", ".slotGroup-id")
        for drp_dwn_id in drp_dwn_ids:
            if drp_dwn_id.text.lower() == "id:" + slot_id:
                drp_dwn_id.click()
                break
        else:
            raise Exception(f"NAME: \"{slot_grp_name}\", ID: \"{slot_id}\" is not found in the \"Slot Group\" list")
        date_fields[0].send_keys(today)
        date_fields[1].send_keys(tomorrow)
        self.chrome_driver.find_element(
            "xpath", "//*[text()=\"Holiday Preference*\"]/following-sibling::div//input/..").click()
        self.chrome_driver.find_elements("css selector", "#menu- li")[1].click()
        topic_drp_dwn.click()
        self.chrome_driver.find_element("css selector", "ul[role=listbox] > li").click()
        topic_count.send_keys("5")
        self.chrome_driver.find_element("css selector", "button[type=button][label=Next]").click()
        timeout = 30
        while timeout:
            if self.chrome_driver.current_url != new_batch_url:
                break
            else:
                timeout -= 1
                time.sleep(1)
        else:
            raise Exception("took too long to add new batch")
        self.chrome_driver.quit()

    def verify_and_add_slot(self, hours=None, minutes=None, day=None):
        with open('../config/course.json') as io_read:
            course = json.load(io_read)['cbse_4']
        course_id = course['id']
        b_day, start_time, *_ = b_time = self.booking_time(hours, minutes, day)
        # available_slots = self.get_available_slots(b_day, start_time)
        # if all(available_slots) is False:
        slot = self._add_slot(b_time, course_id)
        with open('../config/course.json', 'r+') as io_write:
            course = json.load(io_write)
            io_write.seek(0)
            course['cbse_4']['slots'].update(slot)
            json.dump(course, io_write, indent=2)
        # else:
        #     return available_slots

    def get_free_course_details(self):
        premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'free_user_premium_id'))
        self.navigate_to_student_sessions(premium_id)
        rows = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/tbody/tr"))
        cols = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/thead/tr/th"))
        session_detail_col = status_col = topic_details = None
        for i in range(1, cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'index_table')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'Status':
                status_col = i
            elif header == 'Session Detail':
                session_detail_col = i

        for r in range(1, rows + 1):
            try:
                status = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(status_col) + "]").text
                if 'FREE' in status:
                    topic_details = self.chrome_driver.find_element_by_xpath(
                        "//tr[" + str(r) + "]/td[" + str(session_detail_col) + "]").text
                    print(topic_details)
            except NoSuchElementException:
                continue
        self.chrome_driver.close()
        return topic_details

    # operation : Activate/ Deactivate
    def deactivate_or_activate_all_slot_groups(self, operation, course_id):
        self.login_to_cms_staging()
        self.wait_for_locator_webdriver("//div[text()='Courses']")
        self.chrome_driver.find_element_by_xpath("//div[text()='Courses']").click()
        self.wait_for_locator_webdriver("//input[@type='text']")
        self.chrome_driver.find_element_by_xpath("//input[@type='text']").send_keys(course_id)
        self.wait_for_locator_webdriver("//a[text()='" + course_id + "']")
        self.chrome_driver.find_element_by_xpath("//a[text()='" + course_id + "']").click()
        self.wait_for_locator_webdriver("//span[text()='Slot Groups']")
        self.chrome_driver.find_element_by_xpath("//span[text()='Slot Groups']").click()
        action_col = 4
        while True:
            rows = len(
                self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root table')]/tbody/tr"))
            for r in range(1, rows + 1):
                self.wait_for_locator_webdriver("//tr[" + str(r) + "]/td[" + str(action_col) + "]")
                name = self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(action_col) + "]").text
                if name == operation:
                    self.chrome_driver.find_element_by_xpath(
                        "//tr[" + str(r) + "]/td[" + str(action_col) + "]/div/span").click()
                    self.wait_for_clickable_element_webdriver('//span[text()="Confirm"]')
                    self.chrome_driver.find_element_by_xpath('//span[text()="Confirm"]').click()
            svg_icons = self.chrome_driver.find_elements_by_css_selector('.MuiButton-root')
            length = len(svg_icons)
            if svg_icons[length - 1].get_attribute('disabled') is not None:
                break
            svg_icons[length - 1].click()

    def login_and_add_slot(self, hours=None, minutes=None, day=None, course_id=None):
        self.login_to_cms_staging()
        b_day, start_time, *_ = b_time = self.booking_time(hours, minutes, day)
        slot_details = self._add_slot(b_time, course_id)
        self._add_batch(course_id, *slot_details)
        d = datetime.strptime(start_time, "%H:%M")
        return d.strftime("%-I:%M %p")

    def get_session_url_tutorplustllms(self):
        uri = "https://tutor-plus-staging.tllms.com/schedules"
        self.chrome_driver.get(uri)
        email = self.decrypted_data['staging_access']['email']
        tutor_url = None
        premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'premium_id'))
        rows = len(self.chrome_driver.find_elements_by_xpath("//div[contains(@class,'rdt_Table')]/div[@role='row']"))
        cols = len(self.chrome_driver.find_elements_by_xpath("//div[contains(@class,'rdt_Table')]/div[@role='button']"))

        status_col = email_col = scheduled_time_col = None
        for i in range(1, cols):
            header = \
            self.chrome_driver.find_elements_by_xpath("//div[contains(@class,'rdt_Table')]/div[@role='button']")[i].text
            if header == 'COURSE TYPE':
                status_col = i
            elif header == 'SCHEDULED AT':
                scheduled_time_col = i
            elif email_col == 'TUTOR EMAIL':
                email_col = i

        for r in range(0, rows):
            try:
                status = \
                self.chrome_driver.find_elements_by_xpath("//div[contains(@class,'rdt_Table')]/div[@role='cell']")[
                    r * status_col].text
                scheduled_time = \
                self.chrome_driver.find_elements_by_xpath("//div[contains(@class,'rdt_Table')]/div[@role='cell']")[
                    r * scheduled_time_col].text
                if 'one_to_mega' in status and '00:00-23:00' in scheduled_time:
                    self.chrome_driver.find_elements_by_xpath("//div[@role='cell']//a[@class='channel']")[r].click()
                    self.chrome_driver.switch_to_window(self.chrome_driver.window_handles[1])
                    premium_ids_elts = self.chrome_driver.find_elements_by_xpath("//td[contains(@class,'premiumId')]")
                    for element in premium_ids_elts:
                        actual_premium_id = element.text
                        if premium_id == actual_premium_id:
                            print("premium id found")
                            self.chrome_driver.close()
                            self.chrome_driver.switch_to_window(self.chrome_driver.window_handles[0])
                            self.chrome_driver.find_elements_by_xpath(
                                "//div[@role='cell']//input[@name='tutor_email']")[r].clear()
                            self.chrome_driver.find_elements_by_xpath(
                                "//div[@role='cell']//input[@name='tutor_email']")[r].send_keys(email)
                            tutor_url = self.chrome_driver.find_elements_by_xpath(
                                "//div[@role='cell']//div[@class='tutorInputField']/input[@type='text']")[
                                r].get_attribute('value')
                            break
                        else:
                            self.chrome_driver.close()
                            self.chrome_driver.switch_to_window(self.chrome_driver.window_handles[0])
                            continue
            except NoSuchElementException:
                continue
        # TODO - pagination
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'Submit')]").click()
        self.chrome_driver.close()
        print(tutor_url)
        return tutor_url
