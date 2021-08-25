import re
import time
from datetime import datetime, timedelta
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from constants.constants import REQUISITE_DETAILS
from pages.android.scroll_cards import ScrollCards
from pages.android.session_popup import SessionAlert
from constants.load_json import get_data
from utilities.staging_tlms import Stagingtlms
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.login_android import LoginAndroid
from utilities.common_methods import CommonMethods
from pages.base.ps_home_screen_base import PSHomeScreenBase
from appium.webdriver.common.mobileby import MobileBy

CommonMethods = CommonMethods()


class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class PS_Homescreen_Android(PSHomeScreenBase):
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.login = LoginAndroid(driver)
        self.scroll_cards = ScrollCards(driver)
        self.driver = driver
        self.action = TouchAction(driver)
        package_name = self.driver.capabilities['appPackage'] + ':id'
        self.for_you_tab = '//androidx.appcompat.app.ActionBar.Tab[@content-desc="For you"]/android.widget.TextView'
        self.get_help = 'com.byjus.thelearningapp.premium:id/optionalNav'
        self.back_navigation = 'com.byjus.thelearningapp.premium:id/backNav'
        self.bottom_sheet = 'com.byjus.thelearningapp.premium:id/bottomSheet'
        self.close_chat = 'com.byjus.thelearningapp.premium:id/closeChatBtn'
        self.arrow_button = 'com.byjus.thelearningapp.premium:id/arrow_btn'
        self.requisite_items = 'com.byjus.thelearningapp.premium:id/llRequisiteContentLyt'
        self.home_tabs = 'com.byjus.thelearningapp.premium:id/premium_school_home_tabs'
        self.home_page_title = 'com.byjus.thelearningapp.premium:id/toolbar_title'
        self.design_bottom_sheet = 'com.byjus.thelearningapp.premium:id/design_bottom_sheet'
        self.bottom_sheet_book = 'com.byjus.thelearningapp.premium:id/bt_primaryAction'
        self.bottom_sheet_dismiss ='com.byjus.thelearningapp.premium:id/tv_secondaryAction'
        self.byjus_classes_banner= 'com.byjus.thelearningapp.premium:id/ivMarketingBannerTop'
        self.home_screen_user_name =  "com.byjus.thelearningapp.premium:id/header_title_text"
        self.rc_card_root = 'id', '%s/cvSessionCard' % package_name
        self.session_time = '%s/session_time' % package_name
        self.see_all = '%s/tvShowMoreText' % package_name
        self.see_all_icon = '%s/ivShowMore' % package_name
        self.card = 'id', '%s/card_root' % package_name
        self.title = f'{package_name}/tvTitle'
        self.post_req_session = f'{package_name}/cvSession'
        self.session = 'com.byjus.thelearningapp.premium:id/dlSessionLyt'
        self.session_list = 'com.byjus.thelearningapp.premium:id/sessions_list'
        self.post_requisite_date = 'com.byjus.thelearningapp.premium:id/post_requisite_date'
        self.subject_name = 'com.byjus.thelearningapp.premium:id/subject_name'
        self.topic_name = 'com.byjus.thelearningapp.premium:id/topic_name'
        self.workshop_tag = 'com.byjus.thelearningapp.premium:id/tvWorkshop'
        self.session_title = 'com.byjus.thelearningapp.premium:id/session_title'
        self.pre_requisite_time = 'com.byjus.thelearningapp.premium:id/pre_requisite_time'
        self.post_requisite_status = 'com.byjus.thelearningapp.premium:id/post_requisite_status'


    def verify_ps_tabs(self, expected_text):
        text_elements = self.obj.get_elements('class_name', 'android.widget.LinearLayout')
        for element in text_elements:
            if expected_text == element.get_attribute('content-desc'):
                return ReturnType(True, '%s Tab is present'%expected_text)
        return ReturnType(False, '%s Tab is not present'%expected_text)

    def tap_on_tab(self, text):
        self.obj.get_element('xpath',
                             '//android.widget.LinearLayout[@content-desc="' + text + '"]/android.widget.TextView').click()

    def verify_home_screen(self):
        check = self.obj.is_element_present('id',self.home_screen_user_name)
        if check:
            return ReturnType(True, 'User is in home screen')
        else:
            return ReturnType(False, 'User is not in home screen')

    def verify_arrow_present_for_each_requisite(self):
        if len(self.obj.get_elements('id', self.requisite_items)) == len(self.obj.get_elements('id', self.arrow_button)):
            return ReturnType(True, 'Forward arrow is displayed for requisite')
        else:
            return ReturnType(False, 'Forward arrow is not displayed for requisite')

    def is_tab_selected(self, text):
        try:
            displayed = self.obj.get_element('xpath',
                                             '//android.widget.LinearLayout[@content-desc="' + text + '"]/android.widget.TextView').is_selected()
            if displayed:
                return ReturnType(True, '%s Tab is selected'%text)
            return ReturnType(False, '%s Tab is not selected'%text)
        except NoSuchElementException:
            return ReturnType(False, '%s Tab is not displayed'%text)

    def click_back(self):
        self.obj.click_back()

    def tap_on_get_help(self):
        self.obj.get_element('id', self.get_help).click()
        time.sleep(8)
        self.obj.click_back()

    def is_get_help_present(self):
        if self.obj.is_element_present('id', self.get_help):
            return ReturnType(True, 'Get help option is present')
        else:
            return ReturnType(False, 'Get help option is not present')

    def is_back_nav_present(self):
        if self.obj.is_element_present('id', self.back_navigation):
            return ReturnType(True, 'back navigation icon is present')
        else:
            return ReturnType(False, 'back navigation icon is not present')

    def is_bottom_sheet_present(self):
        if self.obj.is_element_present('id', self.bottom_sheet):
            return ReturnType(True,'quick help bottom sheet did show up')
        else:
            return ReturnType(False, 'quick help bottom sheet did not show up')

    def close_get_help(self):
        self.obj.get_element('id', self.close_chat).click()

    def verify_get_help_close(self):
        if self.obj.is_element_present('id', self.close_chat):
            return ReturnType(True, 'Cancel icon is present on chat box')
        else:
            return ReturnType(False, 'Cancel icon is not present on chat box')

    def verify_card_details(self):
        subject_name = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "subject_name")]').text
        topic_name = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "session_title")]').text
        session_time = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "session_time")]').text

        assert all(v is not None for v in [subject_name, topic_name]), "Session card details not loaded"
        m = re.match(
            "[0-3][0-9] (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec), (Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)|(Today), [01]?[0-9]:[0-5][0-9] (AM|PM)",
            session_time)
        assert m is not None, "Session time is in DD MMM,DAY, HH:MM am/pm format"

    def verify_session_details_card_loaded(self):
        subject_name = self.obj.get_element('xpath', '//*[contains(@resource-id, "subjectNametv")]').text
        topic_name = self.obj.get_element('xpath', '//*[contains(@resource-id, "chapterNametv")]').text
        session_date = self.obj.get_element('xpath', '//*[contains(@resource-id, "sessionDatetv")]').text
        session_time = self.obj.get_element('xpath', '//*[contains(@resource-id, "timeTv")]').text
        session_desc = self.obj.get_element('xpath', '//*[contains(@resource-id, "sessionDescriptionTv")]').text
        details_dict = {
            "Subject": subject_name,
            "Topic": topic_name,
            "Schedule Date": session_date,
            "Schedule Time": session_time,
            "Session Desc": session_desc
        }
        assert all(v is not None for v in [subject_name, topic_name, session_time, session_date,
                                           session_desc]), "Session card details not loaded"
        return details_dict

    def verify_button(self, text):
        self.obj.is_button_displayed(text)
        if self.obj.is_button_enabled(text):
            return ReturnType(True, '%s button is displayed' %text)
        else:
            return ReturnType(False,  '%s button is not displayed' %text)

    def attach_post_requisite(self, driver, requisite_name):
        requisite_id = get_data(REQUISITE_DETAILS,requisite_name)
        Stagingtlms(driver).attach_requisite(requisite_id)

    def detach_post_requisite(self,driver):
        Stagingtlms(driver).detach_requisite()

    def verify_completed_card_details(self):
        subject_name = self.obj.get_element('id', self.subject_name).text
        if self.obj.is_element_present('id', self.session_title):
            topic_name = self.obj.get_element('id', self.session_title).text
        else:
            topic_name = self.obj.get_element('id', self.topic_name).text
        session_status = self.obj.get_element('id', self.post_requisite_status).text
        session_date = self.obj.get_element('id', self.post_requisite_date).text
        details_dict = {
            "Subject": subject_name,
            "Topic": topic_name,
            "Schedule Date": session_date,
            "Session status": session_status
        }
        return details_dict

    def tap_outside_dialog_layout(self):
        self.action.tap(None, x=100, y=100).release().perform()

    def is_user_in_ps_page(self):
        self.obj.wait_for_locator('id', self.home_page_title)
        if (self.obj.get_element('id', self.home_page_title).text == 'Classes' and
                self.obj.get_element('id', self.home_tabs).is_displayed()):
            return ReturnType(True, 'User is in the PS screen')
        else:
            return ReturnType(False, 'User is not in the PS screen')

    def verify_bottom_sheet(self):
        if (self.obj.get_element('id','com.byjus.thelearningapp.premium:id/tv_title').text == "BYJU's Classes" and
                self.obj.get_element('id', self.bottom_sheet_book).text == 'Book a Free Trial' and
                self.obj.get_element('id', self.bottom_sheet_dismiss).text == 'Dismiss' and
                self.obj.get_element('id', self.design_bottom_sheet).is_displayed()):
            return ReturnType(True, "User is in BYJU's Classes pop up screen")
        else:
            return ReturnType(False,"User is not in BYJU's Classes pop up screen")

    def verify_banner(self):
        if self.obj.get_element('id',self.byjus_classes_banner):
            return ReturnType(True, 'Byjus classes banner is present')
        else:
            return ReturnType(False, 'Byjus classes banner is not present')

    def verify_booking_page(self):
        if self.obj.is_text_match('Book a free class'):
            return ReturnType(True, 'User is in Book a free class page')
        else:
            return ReturnType(False, 'User is not in Book a free class page')

    def verify_two_upcoming_sessions_present(self):
        self.obj.scroll_to_element("See all")
        cards = self.obj.get_elements(*self.card)
        if len(cards) == 0:
            return ReturnType(False, 'No cards present in classes dashboard')
        count = 0
        for i in range(len(cards)):
            session_time = self.obj.get_element('id', self.session_time).text
            if (datetime.today() + timedelta(days=1)).strftime("%d %b, %A") in session_time or \
                    (datetime.today() + timedelta(days=2)).strftime("%d %b, %A") in session_time:
                count += 1
            if count == 2:
                return ReturnType(True, 'Upcoming session is present in dashboard')

    def verify_see_all_present(self):
        self.obj.scroll_to_element("See all")
        if self.obj.is_element_present('id', self.see_all) and self.obj.is_element_present('id', self.see_all_icon):
            return ReturnType(True, 'See all option and icon present in the dashboard')
        else:
            return ReturnType(False, 'See all option and icon present not present in  the dashboard')

    def tap_on_see_all(self):
        self.obj.element_click('id', self.see_all)

    def verify_up_next_screen(self):
        cards_root = self.obj.get_elements(*self.card)
        if self.obj.is_text_match('Up next') and len(cards_root) > 0:
            return ReturnType(True, 'User landed on up next screen')
        else:
            return ReturnType(False, 'User is not on up next screen')

    def verify_elements_and_up_next_pagination(self):
        if not self.obj.is_text_match('Up next'):
            return ReturnType(False, 'Up next header not present on up next screen')
        cards_root = self.obj.get_elements(*self.card)
        if len(cards_root) == 0:
            return ReturnType(False, 'No sessions listed in up next screen')
        count = 0
        while True:
            for card in cards_root:
                if self.obj.is_child_element_present(card, 'id', self.post_requisite_date):
                    session_date = self.obj.child_element_text(card, self.post_requisite_date)
                    card_subject = self.obj.child_element_text(card, self.subject_name)
                    card_title = self.obj.child_element_text(card, self.topic_name)
                    print(session_date)
                    if all(v is None for v in [session_date, card_subject, card_title]):
                        return ReturnType(False, 'All session details are not present in the Up next screen')
                    count += 1
                elif self.obj.is_child_element_present(card, 'id', self.pre_requisite_time):
                    session_date = self.obj.child_element_text(card, self.pre_requisite_time)
                    card_subject = self.obj.child_element_text(card, self.subject_name)
                    card_title = self.obj.child_element_text(card, self.topic_name)
                    print(session_date)
                    if all(v is None for v in [session_date, card_subject, card_title]):
                        return ReturnType(False, 'All session details not present in the Up next screen')
                    count += 1
                elif self.obj.is_child_element_present(card, 'id', self.session_time):
                    session_date = self.obj.child_element_text(card, self.session_time)
                    try:
                        card_subject = self.obj.child_element_text(card, self.subject_name)
                    except:
                        card_subject = self.obj.child_element_text(card, self.workshop_tag)
                    card_title = self.obj.child_element_text(card, self.session_title)
                    print(session_date)
                    if all(v is None for v in [session_date, card_subject, card_title]):
                        return ReturnType(False, 'All session details are not present in the Up next screen')
                    count += 1
            session_list = self.obj.get_element('id', self.session_list)
            self.scroll_cards.scroll_by_element(cards_root[len(cards_root) - 1], session_list)
            time.sleep(0.5)
            print(count)
            cards_root = self.obj.get_elements(*self.card)
            if count >= 20:
                return ReturnType(True, 'All the elements in the Up next screen. 20 sessions present in up next screen')

    def verify_elements_and_completed_pagination(self):
        cards_root = self.obj.get_elements(*self.card)
        count = 0
        if len(cards_root) == 0:
            return ReturnType(False, 'No sessions listed in completed screen')
        while True:
            session_list = self.obj.get_element('id', self.session_list)
            for card in cards_root:
                try:
                    session_date = self.obj.child_element_text(card, self.post_requisite_date)
                except NoSuchElementException:
                    self.scroll_cards.scroll_by_element(cards_root[len(cards_root) - 1], session_list)
                    continue
                card_subject = self.obj.child_element_text(card, self.subject_name)
                try:
                    card_title = self.obj.child_element_text(card, self.topic_name)
                except:
                    card_title = self.obj.child_element_text(card, self.session_title)
                if all(v is None for v in [session_date, card_subject, card_title]):
                    return ReturnType(False, 'All session details are not present in completed screen')
                count += 1
            self.scroll_cards.scroll_by_element(cards_root[len(cards_root) - 1], session_list)
            time.sleep(0.5)
            print(count)
            cards_root = self.obj.get_elements(*self.card)
            if count >= 20:
                return ReturnType(True,
                                  'All the elements in the completed screen. 20 sessions present in completed screen')

    def all_tagged_resource_types(self):
        try:
            sessions = self.obj.get_elements('id', self.post_req_session)
            titles = self.obj.get_elements('id', self.title)
            if len(sessions) == 0 or len(titles) == 0:
                raise Exception("Under Completed tab, post requisite card is not present")
            items = ["ClassNote", "K12 video", "Journey"]
            for title in titles:
                print(title.text)
            count = 0
            for i in range(0, 3):
                title = titles[i].text
                if (title == items[i]) and sessions[i].is_enabled():
                    count += 1
            if count == 3:
                return ReturnType(True, 'All 3 tagged resources are present in app')
            else:
                return ReturnType(False, "3 resources are tagged in cms, but only %d resources are present" % count)
        except NoSuchElementException:
            return ReturnType(False, 'post requisite sessions are not present')

    def verify_user_in_session(self):
        self.obj.wait_for_locator('id', self.session, 10)
        if self.obj.is_element_present('id', self.session):
            return ReturnType(True, "User is on tutor session screen")
        else:
            return ReturnType(False, "User is not on tutor session screen")

    def get_for_you_or_next_screen_elements(self):
        list = []
        cards_root = self.obj.get_elements(*self.card)
        self.action.move_to(cards_root[0], 20, 20)
        details_dict = SessionAlert(self.driver).content_card_loaded()
        list.append(details_dict)
        for i in range(2):
            self.scroll_cards.scroll_by_element(cards_root[1], cards_root[0])
            cards_root = self.obj.get_elements(*self.card)
            details_dict = SessionAlert(self.driver).content_card_loaded()
            list.append(details_dict)
        print(list)
        return list

    def verify_for_you_and_next_screen(self):
        for_you_list = self.get_for_you_or_next_screen_elements()
        self.obj.element_click('id', self.see_all)
        up_next_list = self.get_for_you_or_next_screen_elements()
        if for_you_list == up_next_list:
            return ReturnType(True, "Session cards with details is identical in both for you and up next screens")
        else:
            return ReturnType(False, "Session cards with details is not identical in both for you and up next screens")
