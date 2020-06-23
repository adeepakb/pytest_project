from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.tutor_common_methods import TutorCommonMethods
from src.Constants.load_json import getdata
from selenium.webdriver.chrome.options import Options
from datetime import datetime


class Stagingtlms:

    def __init__(self, driver):
        self.driver = driver
        self.obj = TutorCommonMethods(driver)
        self.chrome_options = Options()
        self.chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.chrome_driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.__init()

    def __init(self):
        self.url_session_user_wise = 'https://staging.tllms.com/admin/student_sessions/#scheduling-sessions-user-wise'
        self.premium_id = str(getdata('../../config/config.json', 'account_details', 'premium_id'))
        self.today = datetime.today().strftime('%Y-%m-%d')

    def login_to_staging(self, cms_login=None):
        email = str(getdata('../../config/config.json', 'staging_access', 'email'))
        password = str(getdata('../../config/config.json', 'staging_access', 'password'))
        self.chrome_driver.maximize_window()
        if cms_login:
            self.chrome_driver.get('https://tutor-plus-cms-staging.tllms.com')
            self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
            self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
        else:
            self.chrome_driver.get('https://staging.tllms.com/admin')
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

    def get_tutor_url(self):
        email = str(getdata('../../config/config.json', 'staging_access', 'email'))
        premium_id = str(getdata('../../config/config.json', 'account_details', 'premium_id'))
        today = datetime.today().strftime('%Y-%m-%d')

        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//li[@id='mentoring']")
        self.chrome_driver.find_element_by_xpath("//li[@id='mentoring']").click()
        self.wait_for_clickable_element_webdriver("//li[@id='student_sessions']")
        self.chrome_driver.find_element_by_xpath("//li[@id='student_sessions']").click()

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
        for r in range(1, rows + 1):
            try:
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

    def reset_session(self):
        premium_id = str(getdata('../../config/config.json', 'account_details', 'premium_id'))
        today = datetime.today().strftime('%Y-%m-%d')

        self.login_to_staging()
        self.wait_for_locator_webdriver("//li[@id='mentoring']")
        self.chrome_driver.find_element_by_xpath("//li[@id='mentoring']").click()
        self.wait_for_locator_webdriver("//li[@id='student_sessions']")
        self.chrome_driver.find_element_by_xpath("//li[@id='student_sessions']").click()

        self.wait_for_locator_webdriver("//a[text()='Scheduling Sessions(User Wise)']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Scheduling Sessions(User Wise)']").click()
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver("//input[@id ='target_date']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='target_date']").send_keys(today)
        self.wait_for_locator_webdriver("//input[@id ='premium_account_id']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='premium_account_id']").send_keys(premium_id)
        self.wait_for_locator_webdriver("//input[@value ='Start Scheduling']")
        self.chrome_driver.find_elements_by_xpath("//input[@value ='Start Scheduling']")[1].click()
        self.chrome_driver.find_element_by_xpath("//a[text()= 'Reset']").click()
        self.chrome_driver.close()

    @staticmethod
    def get_mobile_and_ccode():
        mobile = str(getdata('../../config/config.json', 'account_details', 'mobile'))
        return mobile

    def get_otp(self):
        complete_mobile = self.get_mobile_and_ccode()
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
            WebDriverWait(self.chrome_driver, 15).until(EC.presence_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_clickable_element_webdriver(self, locator_value):
        try:
            WebDriverWait(self.chrome_driver, 15).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def select_topic(self):
        course_id = str(getdata('../../config/config.json', 'update_pdf_in_cms_details', 'course_id'))
        if not course_id:
            self.login_to_staging()
            self.chrome_driver.get(self.url_session_user_wise)
            self.wait_for_locator_webdriver("//input[@id ='target_date']")
            self.chrome_driver.find_element_by_css_selector("#target_date").send_keys(self.today)
            self.wait_for_locator_webdriver("//input[@id ='premium_account_id']")
            self.chrome_driver.find_element_by_css_selector("#premium_account_id").send_keys(self.premium_id)
            self.wait_for_locator_webdriver("//input[@value ='Start Scheduling']")
            self.chrome_driver.find_element_by_css_selector("#scheduling-sessions-user-wise #_submit_action").click()
        # Tutor is in cms course page
        self.wait_for_locator_webdriver("//table[contains(@class,'MuiTable-root')]")
        course_table_rows = len(
            self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root')]/tbody/tr"))
        course_table_cols = len(
            self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'MuiTable-root')]/thead/tr/th"))
        course_id_col = None
        topics_col = 10
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

    def update_teaching_material(self):
        topic_id = str(getdata('../../config/config.json', 'update_pdf_in_cms_details', 'topic_id'))
        teaching_material = str(getdata('../../config/config.json', 'update_pdf_in_cms_details', 'teaching_material'))

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
            self.wait_for_locator_webdriver("//tr[" + str(row) + "]/td[" + str(topics_id_col) + "]")
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
                break
            row += 1
            if topic_found is False and row == topic_table_rows:
                svg_icons = self.chrome_driver.find_elements_by_css_selector('.MuiSvgIcon-root')
                length = len(svg_icons)
                svg_icons[length - 1].click()  # click on next for pagination
                row = 1

    def update_topic_in_cms(self):
        self.login_to_staging(cms_login=True)
        self.select_topic()
        self.update_teaching_material()
        self.chrome_driver.close()
