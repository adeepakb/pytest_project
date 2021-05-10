# Module Owner - Reshma R Nair
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from constants.load_json import getdata
from pages.android.login_android import LoginAndroid
from pages.android.scroll_cards import ScrollCards
from pages.base.trialclass_base import TrialClassBase
from utilities.common_methods import CommonMethods
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.masterclass import MasterClass

CommonMethods = CommonMethods()


class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class TrailClassAndroid(TrialClassBase):
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
        self.see_more_tv = 'id', '%s/tvShowMoreText' % package_name
        self.card_schedule_tv = 'id', '%s/session_time' % package_name
        self.card_icon_iv = 'id', '%s/cIvSessionImage' % package_name
        self.rounded_nav_button = 'id', '%s/roundedNavButton' % package_name
        self.card_topic_tv = '%s/tvSessionTopicName' % package_name
        self.card_book_btn = '%s/btBookSession' % package_name  # com.byjus.thelearningapp:id/tvSessionTopicName
        self.workshop_label = '%s/tvWorkshop' % package_name
        self.subject_name = '%s/tvSubjectName' % package_name
        self.upnext_subject_name = '%s/subject_name' % package_name
        self.card_topic = '%s/session_title' % package_name
        self.card = '%s/card' % package_name

    def scroll_rc_in_view(self):
        try:
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
        except NoSuchElementException:
            pass  # skip if not found. reusing same method for book a free class trial classes

    def is_book_present_for_free_trail_classes(self):
        self.scroll_rc_in_view()
        i = 0
        cards_root = self.obj.get_elements(*self.rc_card_root)
        if len(cards_root) == 0:
            return ReturnType(False, 'No cards present recommended classes')
        while True:
            for card in cards_root:
                try:
                    self.obj.child_element_by_id(cards_root[i], self.workshop_label)
                except NoSuchElementException:
                    try:
                        subject = self.obj.child_element_text(cards_root[i], self.subject_name)
                        if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS') \
                                and self.obj.child_element_displayed(card, self.card_book_btn):
                            return ReturnType(True, 'Trial class session card with book is present')
                    except NoSuchElementException:
                        return ReturnType(False, 'Trial class session card with book is not present')
                except IndexError:
                    return ReturnType(False, 'Unable to find Trial class session')
                i += 1
                if i == 3:
                    prev_cards = cards_root
                    self.scroll_cards.scroll_by_card(cards_root[2], cards_root[0])
                    time.sleep(1)  # waiting until scroll is completed and page loaded
                    cards_root = self.obj.get_elements(*self.rc_card_root)
                    prev_card_subject = self.obj.child_element_text(prev_cards[2], self.card_topic_tv)
                    card_subject = self.obj.child_element_text(cards_root[2], self.card_topic_tv)
                    if prev_card_subject == card_subject:
                        return ReturnType(False, 'Reached end of page and trial session card with book is not present')
                    i = 1

    def is_master_class_present(self):
        try:
            rc_section = self.obj.get_elements(*self.section_name)[-1]
            if 'Recommended Classes' not in rc_section.text:
                return ReturnType(False, 'Recommended Classes section is not present')
            self.scroll_rc_in_view()
            cards_root = self.obj.get_elements(*self.rc_card_root)
            if len(cards_root) == 0:
                return ReturnType(False, 'No cards present recommended classes')
            i = 0
            while True:
                for card in cards_root:
                    try:
                        self.obj.child_element_by_id(cards_root[i], self.subject_name)
                    except NoSuchElementException:
                        try:
                            subject = self.obj.child_element_text(cards_root[i], self.workshop_label)
                            if subject == 'WORKSHOP' and self.obj.child_element_displayed(card, self.card_book_btn):
                                return ReturnType(True, 'Masterclass is present')
                        except NoSuchElementException:
                            return ReturnType(False, 'Masterclass is not present')
                    i += 1
                    if i == 3:
                        prev_cards = cards_root
                        self.scroll_cards.scroll_by_card(cards_root[2], cards_root[0])
                        time.sleep(1)  # waiting until scroll is completed and page loaded
                        if prev_cards == cards_root:
                            return ReturnType(False, 'Scrolled till the end and Masterclass not found')
                        i = 1
                        cards_root = self.obj.get_elements(*self.rc_card_root)
        except Exception:
            return ReturnType(False, 'Test failed due to exception')

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
        up_next_title = self.obj.child_element_text(up_next_session, self.card_topic)
        up_next_subject = self.obj.child_element_text(up_next_session, self.upnext_subject_name)
        self.tap_on_tab('Completed')
        self.driver.implicitly_wait(2)
        completed_cards = self.obj.get_elements('id', 'com.byjus.thelearningapp.premium:id/card')
        if len(completed_cards) == 0:
            return ReturnType(False, 'No cards present under Completed tab')
        completed_session_title = self.obj.child_element_text(completed_cards[0], self.card_topic)
        try:
            completed_subject = self.obj.child_element_text(completed_cards[0], self.workshop_label)
        except NoSuchElementException:
            completed_subject = self.obj.child_element_text(completed_cards[0], self.upnext_subject_name)
        if completed_subject == up_next_subject and completed_session_title == up_next_title:
            return ReturnType(True, 'Up next free session is displayed in completed tab')
        else:
            return ReturnType(True, 'Up next free session is not displayed in completed tab')

    def tap_on_tab(self, text):
        self.obj.get_element('xpath',
                             '//android.widget.LinearLayout[@content-desc="' + text + '"]/android.widget.TextView').click()

    def get_up_next_trial_class_session(self):
        try:
            list_content = self.obj.get_elements('xpath', f'//*[@resource-id="{self.card_list[-1]}"]/*')
            if len(list_content) == 0:
                raise Exception("No trial cards present in booking page For you tab")
            section_name = self.obj.child_element_text(list_content[0], self.section_name[-1])
            elements = self.obj.get_elements('id', 'com.byjus.thelearningapp.premium:id/card')
            if len(elements) == 0:
                raise Exception('No cards present in booking page For you tab')
            while True:
                for element in elements:
                    if section_name == 'Up Next':
                        try:
                            self.obj.child_element_by_id(element, self.workshop_label)
                        except NoSuchElementException:
                            try:
                                subject = self.obj.child_element_text(element, self.upnext_subject_name)
                                if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS'):
                                    return element
                            except NoSuchElementException:
                                return False
        except:
            return False

    def is_trial_class_booked(self):
        up_next_session = self.get_up_next_trial_class_session()
        try:
            if up_next_session.is_displayed():
                return ReturnType(True, 'Booked trial class is present under up next section')
        except:
            return ReturnType(False, 'Booked trial class is not present under up next section')

    def verify_upnext_free_class_details(self, tllms_topic_details):
        up_next_session = self.get_up_next_trial_class_session()
        app_trial_subject = self.obj.child_element_text(up_next_session, self.upnext_subject_name)
        app_topic_name = self.obj.child_element_text(up_next_session, self.card_topic)
        if app_trial_subject.lower().capitalize() in tllms_topic_details and app_topic_name in tllms_topic_details:
            return ReturnType(True, 'Free class details in app is same as shown in staging')
        else:
            return ReturnType(False, "Free class details in app subject "+app_trial_subject+" topic "+app_topic_name+"is not same as shown in staging" +tllms_topic_details)

    def book_master_class(self, db):
        flag = self.master.book_master_class(new_session=True, ff_tag=False, validate=True, error_validate=False, db=db)
        if flag is True:
            return ReturnType(True, 'Successfully booked master class')
        else:
            return ReturnType(False, 'Booking master class failed')

    def is_autobook_present(self):
        is_swap_button_present = self.obj.is_element_present('id', "com.byjus.thelearningapp.premium:id/swap_button")
        is_swap_button_enabled = self.obj.get_element('id',
                                                      "com.byjus.thelearningapp.premium:id/swap_button").is_enabled()
        if is_swap_button_present and is_swap_button_enabled:
            return ReturnType(True, 'autobook option is present')
        else:
            return ReturnType(False, 'autobook option is not present')

    def verify_user_missed_session(self):
        autobook_message_present = self.obj.is_text_match(
            'We autobooked this class for you. Do you want to Swap with another?')
        rebook_message_present = self.obj.is_text_match("You missed a class.") and \
                                 self.obj.is_text_match("Would you like to rebook?")
        if autobook_message_present or rebook_message_present:
            return ReturnType(True, 'User missed booked session message is  present')
        else:
            return ReturnType(False, 'User missed booked session message is not present')

    def book_trial_class(self):
        self.scroll_rc_in_view()
        elements = self.obj.get_elements(*self.rc_card_root)
        if len(elements) == 0:
            raise Exception('No cards present under recommended classes')
        i = 0
        while True:
            for element in elements:
                try:
                    self.obj.child_element_by_id(elements[i], self.workshop_label)
                except NoSuchElementException:
                    subject = self.obj.child_element_text(elements[i], self.subject_name)
                    if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS'):
                        self.obj.child_element_click_by_id(elements[i], self.card_book_btn)
                        self.obj.button_click("Confirm & Book")
                        self.obj.button_click("Okay")
                i += 1
                if i == 3:
                    self.scroll_cards.scroll_by_card(elements[2], elements[0])
                    time.sleep(1)  # waiting until scroll is completed and page loaded
                    i = 1
                    elements = self.obj.get_elements(*self.rc_card_root)

    def delete_completed_sessions(self):
        premium_id = str(getdata('../config/login_data.json', 'login_detail3', 'free_user_premium_id'))
        status_code = self.delete_completed_sessions_api(premium_id)
        if status_code == 200:
            return ReturnType(True, 'free trial sessions reset api is successful')
        else:
            return ReturnType(False, 'free trial sessions reset api failed')

    def expire_free_trail_subscriptions(self):
        premium_id = str(getdata('../config/login_data.json', 'login_detail3', 'free_user_premium_id'))
        status_code = self.expire_free_trail_subscriptions_api(premium_id)
        if status_code == 200:
            return ReturnType(True, 'free trial subscription expire api is successful')
        else:
            return ReturnType(False, 'free trial subscription expire api failed')

    def back_navigation(self):
        self.obj.get_element(*self.rounded_nav_button).click()

    def book_special_master_class(self):
        self.master.book_special_master_class()

    def verify_completed_trial_cards(self):
        if self.login.text_match("Completed your free trial class?") and \
                self.login.text_match("Explore our free workshops!"):
            return ReturnType(True, 'Completed trial card message is displayed')
        else:
            return ReturnType(False, 'Completed trial card message is not displayed')

    def verify_rcmnded_section_ispresent(self):
        if CommonMethods.scrollToElement(self.driver, 'Recommended Classes'):
            return ReturnType(True, '"Recommended Classes" section is present')
        else:
            return ReturnType(False, '"Recommended Classes" section is present')

    def verify_free_trial_message(self):
        if self.login.text_match('Hope you enjoyed your trial class!') and \
                self.login.text_match('Our academic counsellor will reach out to you shortly to provide more information on BYJU’S Classes.'):
            return ReturnType(True, 'Expected message is shown once user reaches maximum free trail class limit')
        else:
            return ReturnType(False, 'Expected message is not shown once user reaches maximum free trail class limit')
