from datetime import datetime,timedelta
import re
from appium.webdriver.common.touch_action import TouchAction
from utilities.staging_tlms import Stagingtlms
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.login_android import LoginAndroid
from utilities.common_methods import CommonMethods
from pages.base.instruction_dialog_base import InstructionDialogBase
CommonMethods = CommonMethods()


class InstructionDialogAndroid(InstructionDialogBase):
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.action = TouchAction(driver)
        self.login = LoginAndroid(driver)
        self.driver = driver
        self.tlms = Stagingtlms(driver)
        self.close_instruction = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/ivCloseInstruction"]'
        self.assessment_popup = '//*[@resource-id = "assessment"]'
        self.home_tabs = 'com.byjus.thelearningapp.premium:id/premium_school_home_tabs'
        self.home_page_title = 'com.byjus.thelearningapp.premium:id/toolbar_title'
        self.assessment_ok_button = 'android:id/button1'
        self.exit_assessment = 'android:id/button1'
        self.requisite_list = 'com.byjus.thelearningapp.premium:id/requisite_item_list'
        self.begin_assessment = '//*[@resource-id = "begin-assessment"]'
        self.exit_assessment_button = '//android.view.View[@content-desc="Exit Assessment"]/android.widget.TextView'

    def is_close_instruction_displayed(self):
        return self.obj.is_element_present('xpath', self.close_instruction)

    def is_requisite_list(self):
        is_present = self.obj.is_element_present('id', self.requisite_list)
        return is_present

    def tap_on_close_instruction(self):
        self.obj.get_element('xpath', self.close_instruction).click()

    def tap_on_begin_assessment(self):
        self.obj.wait_for_locator('xpath', self.begin_assessment,10)
        self.obj.get_element('xpath', self.begin_assessment).click()
        self.obj.wait_for_locator('xpath', '//*[@resource-id = "main-wrapper"]',5)

    def is_assessment_popup_present(self):
        return self.obj.is_element_present('xpath', self.assessment_popup)

    def click_back(self):
        self.obj.click_back()

    def is_user_in_ps_page(self):
        return (self.obj.get_element('id', self.home_page_title).text == 'Classes' and
                self.obj.get_element('id', self.home_tabs).is_displayed())

    def end_test(self):
        self.obj.get_element('xpath',self.exit_assessment_button).click()
        self.obj.get_element('id', self.assessment_ok_button).click()

    def verify_score_present(self):
        score_found = False
        locator_type = 'xpath'
        locator_value = "//	android.view.View"
        self.obj.wait_for_locator(locator_type, locator_value, 15)
        list_of_elements = self.obj.get_elements(locator_type, locator_value)
        for element in range(len(list_of_elements)):
            actual_text = list_of_elements[element].text
            m = re.match("\d+.0 \/ \d+.0 = \d+%", actual_text)
            if m is not None:
                score_found = True
        return score_found

    def set_future_assessment_start_date(self):
        future_date = (datetime.today() + timedelta(days=1)).strftime('%d-%m-%Y %H:%M')
        date = self.tlms.set_assessment_start_date(future_date, 68881)
        return datetime.strptime(date, '%d-%m-%Y %H:%M').strftime('%I:%M %p, %B %d,%Y')

    def set_assessment_start_date_today(self):
        self.tlms.set_assessment_start_date(datetime.today().strftime('%d-%m-%Y %H:%M'),68881)

    def attach_post_requisite_with_assessement(self,assessment_name):
        self.tlms.attach_requisite(assessment_name)

    def get_assessment_available_until_date(self):
        date = self.tlms.get_assessment_available_until_date(68881)
        return datetime.strptime(date, '%d-%m-%Y %H:%M').strftime('%B %d,%Y %I:%M %p')

    def set_expired_assessment_end_date(self):
        expired_datetime = (datetime.today() - timedelta(minutes=2)).strftime('%d-%m-%Y %H:%M')
        date = self.tlms.set_assessment_end_date(expired_datetime, 68881)
        return date

    def reset_future_end_date(self):
        future_datetime = (datetime.today() + timedelta(days=150)).strftime('%d-%m-%Y %H:%M')
        date = Stagingtlms(self.driver).set_assessment_end_date(future_datetime,68881)
        return date

    def capture_screenshot_of_assessment(self,image_name):
        element = self.obj.get_element('xpath', '//*[@resource-id = "main-wrapper"]')
        self.obj.capture_screenshot(element, image_name)

    def image_diff(self,img1,img2):
        return self.obj.compare_images(img1+".png", img2+".png")