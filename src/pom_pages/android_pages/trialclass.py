import re
from datetime import datetime, timedelta
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from pom_pages.android_pages.login_android import LoginAndroid
from pom_pages.android_pages.scroll_cards import ScrollCards
from utilities.common_methods import CommonMethods
from utilities.tutor_common_methods import TutorCommonMethods

CommonMethods = CommonMethods()


class TrailClass():
    def __init__(self, driver):
        self.driver = driver
        self.login = LoginAndroid(driver)
        self.action = TouchAction(driver)
        self.scroll_cards = ScrollCards(driver)
        self.obj = TutorCommonMethods(driver)
        package_name = self.driver.capabilities['appPackage'] + ':id'
        self.section_name = 'id', '%s/sectionName' % package_name
        self.card_list = 'id', '%s/sessions_list' % package_name
        self.card_root = 'id', '%s/card_root' % package_name
        self.rc_card_root = 'id', '%s/cvSessionCard' % package_name
        self.card_label_tv = 'id', '%s/tvWorkshop' % package_name
        self.upnext_subject_name = 'id', '%s/subject_name' % package_name
        self.subject_name = 'id', '%s/tvSubjectName' % package_name
        self.see_more_tv = 'id', '%s/tvShowMoreText' % package_name
        self.card_schedule_tv = 'id', '%s/session_time' % package_name
        self.reg_card_topic = 'id', '%s/session_title' % package_name
        self.rc_card_root = 'id', '%s/cvSessionCard' % package_name
        self.card_strip_btn = 'id', '%s/card_strip_btn' % package_name
        self.card_label_tv = 'id', '%s/tvWorkshop' % package_name
        self.card_icon_iv = 'id', '%s/cIvSessionImage' % package_name
        self.card_topic_tv = 'id', '%s/tvSessionTopicName' % package_name
        self.rc_card_schedule_tv = 'id', '%s/tvSessionTime' % package_name
        self.card_slots_detail_tv = 'id', '%s/tvSlotsDetail' % package_name
        self.card_book_btn = 'id', '%s/btBookSession' % package_name
        self.card_filling_fast_label = 'id', '%s/tvFillingFast' % package_name
        self.pr_status_msg = 'id', '%s/post_requisite_status' % package_name
        self.book_primary_btn = 'id', '%s/primaryAction' % package_name
        self.book_secondary_btn = 'id', '%s/secondaryAction' % package_name
        self.bs_okay_btn = 'id', '%s/appButtonCtaOk' % package_name
        self.sd_topic_details = 'id', '%s/chapterNametv' % package_name
        self.sd_slot_header = 'id', '%s/tvSlotHeaderTittle' % package_name
        self.sd_time_slot_list = 'id', '%s/rvTimeSlotList' % package_name
        self.sd_scroll_view = 'id', '%s/sessionDetailScrollView' % package_name
        self.sd_book_btn = 'id', '%s/btnAction' % package_name
        self.sd_action_lyt_btn = 'id', '%s/btnAction' % package_name
        self.snack_bar = 'id', '%s/snackbar_text' % package_name
        self.dialog_message = 'id', '%s/dialog_message' % package_name
        self.session_card_reg = 'id', '%s/card' % package_name
        self.bs_header_title = 'id', '%s/tvHeaderTittle' % package_name
        self.bs_success_title = 'id', '%s/appTextView_title' % package_name
        self.bs_topic_name = 'id', '%s/appTextViewContent' % package_name
        self.bs_date_text = 'id', '%s/appTextViewDate' % package_name
        self.bs_time_text = 'id', '%s/appTextViewTime' % package_name
        self.bs_count_down_parent = 'id', '%s/constraintLayout2' % package_name
        self.bs_count_down_hour = 'id', '%s/appTextViewHour' % package_name
        self.pr_status_icon = 'id', '%s/post_requisite_status_icon' % package_name
        self.pr_date = 'id', '%s/post_requisite_date' % package_name
        self.pr_card_topic = 'id', '%s/topic_name' % package_name

    def scroll_rc_in_view(self):
        self.driver.implicitly_wait(30)
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
        prev_cards_root = None
        cards_root = self.obj.get_elements(*self.rc_card_root)
        # while True:
        for card in cards_root:
            try:
                card.find_element_by_id('com.byjus.thelearningapp.premium:id/tvWorkshop')
                continue
            except NoSuchElementException:
                subject = card.find_element_by_id('com.byjus.thelearningapp.premium:id/tvSubjectName').text
                try:
                    if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS') and card.find_element_by_id('com.byjus.thelearningapp.premium:id/btBookSession').is_displayed():
                        return True
                except NoSuchElementException:
                    return False
                # prev_cards_root = cards_root
                # self.scroll_cards.scroll_by_card(cards_root[2], cards_root[1])
                # cards_root = self.obj.get_elements(*self.rc_card_root)
                # if prev_cards_root[2].id == cards_root[3].id:
                #     return True

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

    def get_up_next_trial_class_session(self):
        list_content = self.obj.get_elements('xpath', f'//*[@resource-id="{self.card_list[-1]}"]/*')
        section_name = list_content[0].find_element_by_id(self.section_name[-1]).text.lower()
        elements = self.obj.get_elements('id', 'com.byjus.thelearningapp.premium:id/card')
        while True:
            for element in elements:
                if section_name == 'up next':
                    try:
                        subject = element.find_element_by_xpath('//*[contains(@resource-id, "subject_name")]')
                        if subject.text in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS'):
                            return element
                    except NoSuchElementException:
                        return False
                elif section_name == 'recommended classes':
                    return False

    def is_trail_class_booked(self):
        up_next_session = self.get_up_next_trial_class_session()
        if up_next_session.is_displayed():
            return True
