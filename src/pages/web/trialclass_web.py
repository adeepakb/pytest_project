# Module Owner - Prasanth C
import logging
import time
from selenium.common.exceptions import NoSuchElementException
from constants.load_json import get_data
from pages.base.trialclass_base import TrialClassBase


class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class TrialClassWeb(TrialClassBase):
    def __init__(self, driver):
        self.driver = driver
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
        self.recommended_classes= "//div[text()='Recommended Classes']/parent::div/parent::div/div//div[@class='cardSession']"

    def is_book_present_for_free_trail_classes(self):
        cards = self.driver.find_elements_by_xpath(self.recommended_classes)
        for card in cards:
            if "MASTERCLASS" in card.text:
                   continue
            elif "MASTERCLASS" not in card.text and card.find_element_by_xpath("//span[text()='BOOK']").is_displayed():
                topic_name = card.find_element_by_xpath('.//div[@class="topicText"]').text
                print("topic name: ", topic_name)
                return ReturnType(True, 'Trial class session card with book is present')
            else:
                return ReturnType(False, 'Trial class session card with book is not present')
        return ReturnType(False, 'Reached end of sessions and trial session card with book is not present')



    def is_trial_class_booked(self):
        try:
            if self.book_trial_class():
                return True
            else:
                logging.info("Element not found")
                return False
        except NoSuchElementException:
            return False

    def verify_button(self):
        pass

    def is_autobook_present(self):
        pass

    def verify_user_missed_session(self):
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

    def is_upnext_trial_class_completed(self):
        time.sleep(10)
        comptab = self.driver.find_element("xpath", self.comp_class_tab)
        comptab.click()
        subjects = self.driver.find_elements('xpath', self.sub_label_txt)
        for subject in subjects:
            subject = subject.text
            try:
                if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS') and subject.is_displayed():
                    return False
                else:
                    return True
            except NoSuchElementException:
                return True

    def book_trial_class(self):
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 2000)")
        cards = self.driver.find_elements_by_xpath("//div[@class='cardSession']")
        for card in cards:

            if card.find_element_by_xpath(
                    ".//div[@class='subjectNameText']").text.lower() != "masterclass" and \
                    card.find_element_by_xpath(".//span[text()='BOOK']").is_displayed():
                topic_name = card.find_element_by_xpath('.//div[@class="topicText"]').text
                print("topic name: ", topic_name)
                card.find_element_by_xpath('.//div[@class="btnCard"]').click()
                ele = self.driver.find_element_by_xpath("//span[text()='CONFIRM & BOOK NOW']")
                ele.click()
                time.sleep(3)
                skip = self.driver.find_element('xpath', self.skip_btn)
                skip.click()

    def verify_completed_trial_cards(self):
        try:
            time.sleep(4)
            element = self.driver.find_element_by_xpath("//div[@class='Component-message-4997']").is_displayed()
            if element is not None:
                return True
            else:
                logging.info("Element not found")
                return False
        except NoSuchElementException:
            return False

    def delete_completed_sessions(self):
        premium_id = str(get_data('../config/login_data.json', 'login_detail6', 'free_user_premium_id'))
        return self.delete_completed_sessions_api(premium_id)

    def expire_free_trail_subscriptions(self):
        premium_id = str(get_data('../config/login_data.json', 'login_detail5', 'free_user_premium_id'))
        return self.expire_free_trail_subscriptions_api(premium_id)

    def book_master_class(self, db):
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0, 2000)")
        cards = self.driver.find_elements_by_xpath("//div[@class='cardSession']")
        for card in cards:
            if card.find_element_by_xpath(
                    ".//div[@class='subjectNameText']").text.lower() == "masterclass" and \
                    card.find_element_by_xpath(".//span[text()='BOOK']").is_displayed():
                topic_name = card.find_element_by_xpath('.//div[@class="topicText"]').text
                print("topic name: ", topic_name)
                card.find_element_by_xpath('.//div[@class="btnCard"]').click()
                return True


    def back_navigation(self):
        pass

    def is_master_class_present(self):
        self.driver.execute_script("window.scrollTo(0, 2000)")
        cards = self.driver.find_elements_by_xpath("//div[@class='cardSession']")
        for card in cards:
            try:
                if card.find_element_by_xpath(".//div[@class='subjectNameText']").text.lower() == "masterclass":
                    return True
                else:
                    return False
            except NoSuchElementException:
                return False

    def book_special_master_class(self):
        pass

    def scroll_rc_in_view(self):
        pass

    def is_sessions_under_rc_displayed(self):
        pass

    def is_see_all_link_displayed(self):
        pass

    def click_option_see_more(self, text):
        pass

    def is_master_class_booked(self):
        pass

    def get_up_next_trial_class_session(self):
        pass

    def tap_on_tab(self, text):
        pass

    def verify_rcmnded_section_ispresent(self):
        try:
            time.sleep(4)
            element = self.driver.find_element('xpath', self.rcmd_section).is_displayed()
            if element is not None:
                return True
            else:
                logging.info("Element not found")
                return False
        except NoSuchElementException:
            return False

    def verify_free_trial_message(self):
        try:
            time.sleep(4)
            element = self.driver.find_element('xpath', self.hope_you_enjoy_msg).is_displayed()
            if element is not None:
                return True
            else:
                logging.info("Element not found")
                return False
        except NoSuchElementException:
            return False
