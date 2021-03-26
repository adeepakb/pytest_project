import re
import time
import requests
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from constants.load_json import getdata
from pages.android.login_android import LoginAndroid
from pages.android.scroll_cards import ScrollCards
from utilities.common_methods import CommonMethods
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.masterclass import MasterClass

CommonMethods = CommonMethods()


class TrailClass():
    def __init__(self, driver):
        self.driver = driver
        self.login = LoginAndroid(driver)
        self.action = TouchAction(driver)
        self.scroll_cards = ScrollCards(driver)
        self.obj = TutorCommonMethods(driver)
        self.master = MasterClass(driver)
        package_name = self.driver.capabilities['appPackage'] + ':id'
        self.section_name = 'id', '%s/sectionName' % package_name
        self.card_list = 'id', '%s/sessions_list' % package_name
        self.card_root = 'id', '%s/card_root' % package_name
        self.rc_card_root = 'id', '%s/cvSessionCard' % package_name
        self.card_label_tv = 'id', '%s/tvWorkshop' % package_name
        self.upnext_subject_name = 'id', '%s/subject_name' % package_name
        self.subject_name = 'id', '%s/tvSubjectName' % package_name
        self.card_book_btn = 'id', '%s/btBookSession' % package_name
        self.see_more_tv = 'id', '%s/tvShowMoreText' % package_name
        self.card_schedule_tv = 'id', '%s/session_time' % package_name
        self.reg_card_topic = 'id', '%s/session_title' % package_name
        self.card_label_tv = 'id', '%s/tvWorkshop' % package_name
        self.card_icon_iv = 'id', '%s/cIvSessionImage' % package_name
        self.card_topic_tv = 'id', '%s/tvSessionTopicName' % package_name
        self.rc_card_schedule_tv = 'id', '%s/tvSessionTime' % package_name
        self.rounded_nav_button = 'id', '%s/roundedNavButton' % package_name

    def scroll_rc_in_view(self):
        # self.driver.implicitly_wait(30)
        session_list = self.obj.get_element(*self.card_list)
        self.scroll_cards.scroll_by_card(session_list, session_list)
        rc_text = 'recommended classes'
        rc_section = self.obj.get_elements(*self.section_name)[-1]
        if rc_section.text.lower() == 'recommended classes':
            session_list = self.obj.get_element(*self.card_list)
            self.scroll_cards.scroll_by_card(rc_section, session_list)
        elif rc_section.text.lower() == 'up next':
            self.obj.get_element(
                'android_uiautomator',
                'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                f'scrollTextIntoView("{rc_text.title()}")'
            )
            rc_section = self.obj.get_elements(*self.section_name)[-1]
            session_list = self.obj.get_element(*self.card_list)
            self.scroll_cards.scroll_by_card(rc_section, session_list)
        else:
            raise Exception("'Recommended Classes' section could not be located on the page.")

    def is_rc_session_card_displayed(self):
        self.scroll_rc_in_view()
        cards_root = self.obj.get_elements(*self.rc_card_root)
        for card in cards_root:
            if card.find_element_by_id(self.card_label_tv[-1]).text.lower() == 'workshop':
                return True
        return False

    def is_book_present_for_free_trail_classes(self):
        self.scroll_rc_in_view()
        i = 0
        cards_root = self.obj.get_elements(*self.rc_card_root)
        while True:
            for card in cards_root:
                try:
                    cards_root[i].find_element_by_id('com.byjus.thelearningapp.premium:id/tvWorkshop')
                except NoSuchElementException:
                    try:
                        subject = cards_root[i].find_element_by_id(
                            'com.byjus.thelearningapp.premium:id/tvSubjectName').text
                        if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS') and card.find_element_by_id(
                                'com.byjus.thelearningapp.premium:id/btBookSession').is_displayed():
                            return True
                    except NoSuchElementException:
                        return False
                i += 1
                if i == 3:
                    time.sleep(2)
                    prev_cards = cards_root
                    self.scroll_cards.scroll_by_card(cards_root[2], cards_root[0])
                    cards_root = self.obj.get_elements(*self.rc_card_root)
                    prev_card_subject = prev_cards[2].find_element_by_id('com.byjus.thelearningapp.premium:id/tvSessionTopicName').text
                    card_subject = cards_root[2].find_element_by_id('com.byjus.thelearningapp.premium:id/tvSessionTopicName').text
                    if prev_card_subject == card_subject:
                        return False
                    time.sleep(2)
                    i = 1

    def is_master_class_present(self):
        rc_section = self.obj.get_elements(*self.section_name)[-1]
        if 'Recommended Classes' not in rc_section.text:
            return False
        self.scroll_rc_in_view()
        cards_root = self.obj.get_elements(*self.rc_card_root)
        i = 0
        while True:
            for card in cards_root:
                try:
                    cards_root[i].find_element_by_id('com.byjus.thelearningapp.premium:id/tvSubjectName')
                except NoSuchElementException:
                    try:
                        subject = cards_root[i].find_element_by_id(
                            'com.byjus.thelearningapp.premium:id/tvWorkshop').text
                        if subject == 'WORKSHOP' and card.find_element_by_id(
                                'com.byjus.thelearningapp.premium:id/btBookSession').is_displayed():
                            return True
                    except NoSuchElementException:
                        return False
                i += 1
                if i == 3:
                    time.sleep(2)
                    prev_cards = cards_root
                    self.scroll_cards.scroll_by_card(cards_root[2], cards_root[0])
                    if prev_cards == cards_root:
                        return False
                    time.sleep(2)
                    i = 1
                    cards_root = self.obj.get_elements(*self.rc_card_root)

    def is_sessions_under_rc_displayed(self):
        self.scroll_rc_in_view()
        rc_sessions = False
        list_content = self.obj.get_elements('xpath', f'//*[@resource-id="{self.card_list[-1]}"]/*')
        self.login.implicit_wait_for(0)
        for element in list_content:
            try:
                session_section = element.find_element_by_id(self.section_name[-1])
                if session_section.text.lower() == 'recommended classes':
                    rc_sessions = True
                    continue
            except NoSuchElementException:
                if rc_sessions:
                    element.find_element_by_id(self.rc_card_root[-1])
                    self.login.implicit_wait_for(15)
                    return True
        self.login.implicit_wait_for(15)
        return False

    def verify_rc_session_card_details(self):
        rc_card_root = self.obj.get_element(*self.rc_card_root)
        logo_displayed = rc_card_root.find_element_by_id(self.card_icon_iv[-1]).is_displayed()
        label_displayed = rc_card_root.find_element_by_id(self.card_label_tv[-1]).is_displayed()
        topic_name_displayed = rc_card_root.find_element_by_id(self.card_topic_tv[-1]).is_displayed()
        schedule_details = rc_card_root.find_element_by_id(self.rc_card_schedule_tv[-1]).text
        schedule_match = re.findall(r'(?:\d{2}\D{0,3}\s\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec),\s'
                                    r'(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday))|Tomorrow'
                                    r'|Today, \d{1,2}:\d{2}\s(?i:AM|PM)',
                                    schedule_details)
        schedule_match_displayed = True if schedule_match else False
        book_btn = True if rc_card_root.find_element_by_id(self.card_book_btn[-1]).text.lower() == 'book' else False
        return all((logo_displayed, label_displayed, topic_name_displayed, schedule_match_displayed, book_btn))

    def is_all_rc_sessions_displayed(self):
        rc_sessions = self.obj.get_elements(*self.rc_card_root)
        c = 0
        for session in rc_sessions:
            label = session.find_element_by_id(self.card_label_tv[-1])
            if label.text.lower() == 'workshop':
                c += 1
        if c == len(rc_sessions) > 1:
            return True
        return False

    def is_see_all_link_displayed(self):
        see_more_less = self.obj.get_element(
            'android_uiautomator',
            'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
            f'scrollIntoView(resourceId("{self.see_more_tv[-1]}"))'
        )
        return see_more_less.is_displayed()

    def click_option_see_more(self, text: str = 'see all'):
        if self.is_see_all_link_displayed():
            see_more = self.obj.get_element(*self.see_more_tv)
            if see_more.text.lower() == text:
                see_more.click()
        return self

    def is_upnext_trial_class_completed(self):
        up_next_session = self.get_up_next_trial_class_session()
        up_next_title = up_next_session.find_element_by_id('com.byjus.thelearningapp.premium:id/session_title').text
        up_next_subject = up_next_session.find_element_by_id('com.byjus.thelearningapp.premium:id/subject_name').text
        self.tap_on_tab('Completed')
        self.driver.implicitly_wait(2)
        completed_cards = self.obj.get_elements('id', 'com.byjus.thelearningapp.premium:id/card')
        if len(completed_cards) == 0:
            return False
        completed_session_title = completed_cards[0].find_element_by_id(
            'com.byjus.thelearningapp.premium:id/session_title').text
        try:
            completed_subject = completed_cards[0].find_element_by_id(
                'com.byjus.thelearningapp.premium:id/tvWorkshop').text
        except NoSuchElementException:
            completed_subject = completed_cards[0].find_element_by_id(
                'com.byjus.thelearningapp.premium:id/subject_name').text
        if completed_subject == up_next_subject and completed_session_title == up_next_title:
            return True
        else:
            return False

    def tap_on_tab(self, text):
        self.obj.get_element('xpath',
                             '//android.widget.LinearLayout[@content-desc="' + text + '"]/android.widget.TextView').click()

    def get_up_next_trial_class_session(self):
        list_content = self.obj.get_elements('xpath', f'//*[@resource-id="{self.card_list[-1]}"]/*')
        section_name = list_content[0].find_element_by_id(self.section_name[-1]).text.lower()
        elements = self.obj.get_elements('id', 'com.byjus.thelearningapp.premium:id/card')
        while True:
            for element in elements:
                if section_name == 'up next':
                    try:
                        element.find_element_by_id('com.byjus.thelearningapp.premium:id/tvWorkshop')
                    except NoSuchElementException:
                        try:
                            subject = element.find_element_by_id('com.byjus.thelearningapp.premium:id/subject_name').text
                            if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS'):
                                return element
                        except NoSuchElementException:
                            return False
                elif section_name == 'recommended classes':
                    return False

    def is_trial_class_booked(self):
        up_next_session = self.get_up_next_trial_class_session()
        if up_next_session.is_displayed():
            return True

    # def book_master_class(self):
    #     self.master.book_master_class(validate=True)

    def book_master_class(self, db):
        flag = self.master.book_master_class(new_session=True, ff_tag=False, validate=True, error_validate=False, db=db)
        return flag

    def is_autobook_present(self):
        is_swap_button_present = self.obj.is_element_present('id', "com.byjus.thelearningapp.premium:id/swap_button")
        is_swap_button_enabled = self.obj.get_element('id',
                                                      "com.byjus.thelearningapp.premium:id/swap_button").is_enabled()
        if is_swap_button_present and is_swap_button_enabled:
            return True
        else:
            return False

    def verify_user_missed_session(self):
        autobook_message_present = self.obj.is_text_match(
            'We autobooked this class for you. Do you want to Swap with another?')
        rebook_message_present = self.obj.is_text_match("You missed a class.") and \
                                 self.obj.is_text_match("Would you like to rebook?")
        if autobook_message_present or rebook_message_present:
            return True
        else:
            return False

    def book_trial_class(self):
        self.master.scroll_rc_in_view()
        elements = self.obj.get_elements(*self.rc_card_root)
        i = 0
        while True:
            for element in elements:
                try:
                    elements[i].find_element_by_id('com.byjus.thelearningapp.premium:id/tvWorkshop')
                except NoSuchElementException:
                    subject = elements[i].find_element_by_id('com.byjus.thelearningapp.premium:id/tvSubjectName').text
                    if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS'):
                        elements[i].find_element_by_id('com.byjus.thelearningapp.premium:id/btBookSession').click()
                        self.obj.button_click("Confirm & Book")
                        self.obj.button_click("Okay")
                        return True
                i += 1
                if i == 3:
                    time.sleep(2)
                    self.scroll_cards.scroll_by_card(elements[2], elements[0])
                    time.sleep(2)
                    i = 1
                    elements = self.obj.get_elements(*self.rc_card_root)

    @staticmethod
    def delete_completed_sessions():
        url = "https://api.tllms.com/internal/staging/tutor_plus/internal_api/one_to_mega/v1/courses_subscriptions/bulk_delete"
        headers = {'Content-Type': 'application/json'}
        premium_id = str(getdata('../config/login_data.json', 'login_detail3', 'free_user_premium_id'))
        payload = {"premium_account_id": premium_id}
        r = requests.delete(url, json=payload, headers=headers)
        print(r.status_code)
        return r.status_code

    @staticmethod
    def expire_free_trail_subscriptions():
        url = "https://api.tllms.com/internal/staging/tutor_plus/internal_api/one_to_mega/v1/courses_subscriptions/bulk_expire"
        headers = {'Content-Type': 'application/json'}
        premium_id = str(getdata('../config/login_data.json', 'login_detail3', 'free_user_premium_id'))
        payload = {"premium_account_id": premium_id}
        r = requests.post(url, json=payload, headers=headers)
        print(r.status_code)
        return r.status_code

    def back_navigation(self):
        self.obj.get_element(*self.rounded_nav_button).click()

    def book_special_master_class(self):
        return self.master.book_special_master_class()

    def is_master_class_booked(self):
        return self.master.is_master_class_booked()
