
from selenium.common.exceptions import NoSuchElementException
import logging
import time
from pages.base.ps_home_screen_base import PSHomeScreenBase


class PSHomescreenWeb(PSHomeScreenBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
        self.rcmd_section = "//div[text()='Recommended Classes']"
        self.book_btn = "//span[text()='BOOK']"
        self.subjectname = "//div[@class='subjectNameText']"
        self.book_buttn = ".//div[@class='btnCard']"
        self.comp_class_tab = "//span[text()='COMPLETED CLASSES']"
        self.sub_label_txt = "//div[@class='textCell']"
        self.hope_you_enjoy_msg = "//div[text()='Hope you enjoyed your trial class!']"
        self.rebook_msg = "//div[@class='rebookSlotMsg']"
        self.skip_btn = "//div[@class='skipbtn']"
        self.rebook_cls_sec = "//div[text()='Rebook Classes']"
        self.join_btn = "//span[text()='JOIN']"

    def is_user_in_ps_page(self):
        try:
            time.sleep(4)
            element = self.driver.find_element_by_xpath("// div[text() = 'Classes']")
            if element is not None:
                return True
            else:
                logging.info("Element not found")
                return False
        except (NoSuchElementException):
            return False

    def verify_user_booked_the_trial_session(self):
        try:
            if self.book_a_free_trial_class():
                return True
            else:
                logging.info("Element not found")
                return False
        except NoSuchElementException:
            return False

    def click_on_completed_classes_tab(self):
        time.sleep(10)
        comptab = self.driver.find_element("xpath", self.comp_class_tab)
        comptab.click()

    def verify_user_missed_booked_session(self):
        try:
            time.sleep(4)
            you_missed_session_msg = self.driver.find_element('xpath', self.rebook_msg)
           # rebook_classes_sec = self.driver.find_element('xpath', self.rebook_cls_sec)
            if you_missed_session_msg.is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def verify_multiple_master_classes_booked(self):
        try:
            self.book_master_class_session()
            skip = self.driver.find_element('xpath', self.skip_btn)
            skip.click()
            self.book_master_class_session()
            return True
        except NoSuchElementException:
            return False

    def verify_button(self):
        pass

    def is_autobook_present(self):
        pass

    def verify_ps_tabs(self, expected_text):
        pass

    def tap_on_tab(self, text):
        pass

    def verify_arrow_present_for_each_requisite(self):
        pass

    def is_tab_selected(self, text):
        pass

    def click_back(self):
        pass

    def tap_on_get_help(self):
        pass

    def is_get_help_present(self):
        pass

    def is_back_nav_present(self):
        pass

    def is_bottom_sheet_present(self):
        pass

    def close_get_help(self):
        pass

    def verify_get_help_close(self):
        pass

    def verify_card_details(self):
        pass

    def verify_session_details_card_loaded(self):
        pass

    def attach_post_requisite_with_assessement(self, driver, assessment_name):
        pass

    def verify_completed_card_details(self):
        pass

    def tap_outside_dialog_layout(self):
        pass


    def click_on_join_now_btn(self):
        ele = self.driver.find_element("xpath", self.join_btn)
        if ele.is_enabled():
            ele.click
            return True
        else:
            return False



