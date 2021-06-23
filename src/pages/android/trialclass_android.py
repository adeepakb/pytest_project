# Module Owner - Reshma R Nair
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from constants.load_json import get_data
from pages.android.login_android import LoginAndroid
from pages.android.scroll_cards import ScrollCards
from pages.base.trialclass_base import TrialClassBase
from utilities.common_methods import CommonMethods
from utilities.return_type import ReturnType
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.masterclass import MasterClass

CommonMethods = CommonMethods()


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
        self.rc_card_schedule_tv = 'id', '%s/tvSessionTime' % package_name
        self.rounded_nav_button = 'id', '%s/roundedNavButton' % package_name
        self.card_topic_tv = '%s/tvSessionTopicName' % package_name
        self.card_book_btn = '%s/btBookSession' % package_name  # com.byjus.thelearningapp:id/tvSessionTopicName
        self.workshop_label = '%s/tvWorkshop' % package_name
        self.subject_name = '%s/tvSubjectName' % package_name
        self.upnext_subject_name = '%s/subject_name' % package_name
        self.card_topic = '%s/session_title' % package_name
        self.card = '%s/card' % package_name
        self.course_list = '%s/rvCourseList' % package_name
        self.expired_title = "id", "%s/tvSessionExpiryTitle" % package_name
        self.title = '%s/tvTitle' % package_name
        self.filling_fast = '%s/tvFillingFast' % package_name
        self.rc_card_schedule_tv = '%s/tvSessionTime' % package_name
        self.other_slots_detail = '%s/tvSlotsDetail' % package_name
        self.bs_okay_btn = '%s/appButtonCtaOk' % package_name
        self.confirm_book_popup_date = '%s/tvTittle' % package_name
        self.toggle_buttons = '%s/toggleButtonsGroup' % package_name
        self.bs_success_title = 'id', '%s/appTextView_title' % package_name
        self.bs_topic_name = 'id', '%s/appTextViewContent' % package_name
        self.bs_date_text = 'id', '%s/appTextViewDate' % package_name
        self.bs_time_text = 'id', '%s/appTextViewTime' % package_name
        self.bs_count_down_layout = 'id', '%s/constraintLayout2' % package_name
        self.bs_count_down_hour = 'id', '%s/appTextViewHour' % package_name
        self.bs_count_down_hour_text = 'id', '%s/appTextView2' % package_name
        self.bs_count_down_minutes = 'id', '%s/appTextViewMin' % package_name
        self.bs_count_down_minutes_text = 'id', '%s/appTextView3' % package_name
        self.bs_count_down_seconds = 'id', '%s/appTextViewSec' % package_name
        self.bs_count_down_seconds_text = 'id', '%s/appTextView4' % package_name
        self.bottom_sheet = '%s/design_bottom_sheet' % package_name

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
                    time.sleep(2)
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
                        time.sleep(2)
                        prev_cards = cards_root
                        self.scroll_cards.scroll_by_card(cards_root[2], cards_root[0])
                        if prev_cards == cards_root:
                            return ReturnType(False, 'Scrolled till the end and Masterclass not found')
                        time.sleep(2)
                        i = 1
                        cards_root = self.obj.get_elements(*self.rc_card_root)
        except Exception:
            return ReturnType(False, 'Test failed due to exception')

    def is_sessions_under_rc_displayed(self):
        self.scroll_rc_in_view()
        rc_sessions = False
        list_content = self.obj.get_elements('xpath', f'//*[@resource-id="{self.card_list[-1]}"]/*')
        self.login.implicit_wait_for(0)
        for element in list_content:
            try:
                session_section = self.obj.child_element_by_id(element, self.section_name[-1])
                if session_section.text.lower() == 'recommended classes':
                    rc_sessions = True
                    continue
            except NoSuchElementException:
                if rc_sessions:
                    self.obj.child_element_by_id(element, self.rc_card_root[-1])
                    self.login.implicit_wait_for(15)
                    return True
        self.login.implicit_wait_for(15)
        return False

    def is_see_all_link_displayed(self):
        see_more_less = self.obj.get_element(
            'android_uiautomator',
            'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
            f'scrollIntoView(resourceId("{self.see_more_tv[-1]}"))'
        )
        return ReturnType(True, "All links displayed") if see_more_less.is_displayed() else ReturnType(False,
                                                                                                       "All links are not displayed")

    def click_option_see_more(self, text: str = 'see all'):
        if self.is_see_all_link_displayed().result:
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
            return ReturnType(False, 'No completed session present under Completed tab')
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
        list_content = self.obj.get_elements('xpath', f'//*[@resource-id="{self.card_list[-1]}"]/*')
        section_name = self.obj.child_element_text(list_content[0], self.section_name[-1])
        elements = self.obj.get_elements('id', 'com.byjus.thelearningapp.premium:id/card')
        while True:
            for element in elements:
                if section_name.lower() == 'up next':
                    try:
                        self.obj.child_element_by_id(element, self.workshop_label)
                    except NoSuchElementException:
                        try:
                            subject = self.obj.child_element_text(element, self.upnext_subject_name)
                            if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS'):
                                return element
                        except NoSuchElementException:
                            return False

    def is_trial_class_booked(self):
        up_next_session = self.get_up_next_trial_class_session()
        if up_next_session.is_displayed():
            return ReturnType(True, "Trial class is booked")
        else:
            return ReturnType(False, "Trial class is not booked, could not see upnext session")

    def book_master_class(self, db):
        flag = self.master.book_master_class(new_session=True, ff_tag=False, validate=True, error_validate=False, db=db)
        return flag

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
        self.master.scroll_rc_in_view()
        elements = self.obj.get_elements(*self.rc_card_root)
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
                    time.sleep(2)
                    self.scroll_cards.scroll_by_card(elements[2], elements[0])
                    time.sleep(2)
                    i = 1
                    elements = self.obj.get_elements(*self.rc_card_root)

    def delete_completed_sessions(self):
        premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'free_user_premium_id'))
        status_code = self.delete_completed_sessions_api(premium_id)
        if status_code == 200:
            return ReturnType(True, 'free trial sessions reset api is successful')
        else:
            return ReturnType(False, 'free trial sessions reset api failed')

    def expire_free_trail_subscriptions(self):
        premium_id = str(get_data('../config/login_data.json', 'login_detail3', 'free_user_premium_id'))
        status_code = self.expire_free_trail_subscriptions_api(premium_id)
        if status_code == 200:
            return ReturnType(True, 'free trial subscription expire api is successful')
        else:
            return ReturnType(False, 'free trial subscription expire api failed')

    def back_navigation(self):
        self.obj.get_element(*self.rounded_nav_button).click()

    def book_special_master_class(self):
        return self.master.book_special_master_class()

    def is_master_class_booked(self):
        return self.master.is_master_class_booked()

    def verify_completed_trial_cards(self):
        return ReturnType(True, "Completed card verified") if (
                self.login.text_match("Completed your free trial class?") and \
                self.login.text_match("Explore our free workshops!")) else ReturnType(False,
                                                                                      "Completed card not verified, Completed your free trial class? or Explore our free workshops! not displayed ")

    def verify_rcmnded_section_ispresent(self):
        return CommonMethods.scrollToElement(self.driver, 'Recommended Classes')

    def verify_free_trial_message(self):

        if not self.login.text_match('Hope you enjoyed your trial class!'):
            return ReturnType(False, "hope you enjoyed your trial class! is not beind displayed")
        elif not self.login.text_match('Our academic counsellor will reach out to you shortly to provide more '
                                       'information on BYJU’S Classes.'):
            return ReturnType(False, "Our academic counsellor will reach out to you shortly is not being displayed")
        else:
            return ReturnType(True, " free trial messages are displayed correctly")

    def is_free_trail_expired(self):
        try:
            status = self.obj.get_element(*self.expired_title).is_displayed()
            return status
        except NoSuchElementException:
            return False


class TrailClassFuturePaid(TutorCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.scroll_cards = ScrollCards(driver)
        self.action = TouchAction(driver)
        self.device_type = self.get_device_type()
        self.__init_locators(self.device_type)

    def __init_locators(self, device_type=None):
        package_name = self.driver.capabilities['appPackage'] + ':id'
        self.section_name = 'id', '%s/sectionName' % package_name
        self.card_list_root = "id", "%s/root_view" % package_name
        self.card_list = 'id', '%s/rvCourseList' % package_name
        self.card_root = "id", "%s/cvSessionCard" % package_name
        self.card_label_tv = 'id', '%s/tvWorkshop' % package_name
        self.card_book_btn = 'id', '%s/btBookSession' % package_name
        self.session_header = "id", "%s/tvTitle" % package_name
        self.card_subject_tv = "id", "%s/tvSubjectName" % package_name
        self.toolbar = "id", "%s/toolbarView" % package_name
        self.book_primary_btn = 'id', '%s/primaryAction' % package_name
        self.bs_okay_btn = 'id', '%s/appButtonCtaOk' % package_name
        self.expired_title = "id", "%s/tvSessionExpiryTitle" % package_name

    def scroll_rgc_in_view(self):
        try:
            self.get_element(
                'android_uiautomator',
                'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                f'scrollTextIntoView("Regular Classes")'
            )
        except NoSuchElementException:
            return self.get_element(
                'android_uiautomator',
                'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                f'scrollTextIntoView("Up Next")'
            ).is_displayed()
        toolbar = self.get_element(*self.toolbar)
        session_headers = self.get_elements(*self.session_header)
        for session_header in session_headers:
            if session_header.text.lower() == "regular classes":
                start_location = session_header.location
                start_element_size = session_header.size
                start_x = start_location['x'] + start_element_size["width"] // 2
                start_y = start_location['y'] + start_element_size["height"] - 10
                end_location = toolbar.location
                end_y = end_location['y'] + toolbar.size["height"] + 10
                self.action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).wait(3000).release().perform()
                return False

    def is_trial_class_available(self):
        if self.scroll_rgc_in_view():
            return True
        cards = self.get_elements(*self.card_root)
        self.driver.implicitly_wait(0)
        for card in cards:
            try:
                label_text = card.find_element_by_id(self.card_label_tv[-1]).text.lower()
            except NoSuchElementException:
                try:
                    label_text = card.find_element_by_id(self.card_subject_tv[-1]).text.lower()
                except NoSuchElementException:
                    label_text = None
            if label_text != "workshop" and label_text is not None \
                    and card.find_element_by_id(self.card_book_btn[-1]).is_displayed():
                return True
        return False

    def book_trial_class(self):
        if self.scroll_rgc_in_view():
            return True
        elements = self.get_elements(*self.card_root)
        self.driver.implicitly_wait(0)
        for element in elements:
            try:
                element.find_element_by_id(self.card_label_tv[-1])
            except NoSuchElementException:
                try:
                    subject = element.find_element_by_id(self.card_subject_tv[-1]).text
                except NoSuchElementException:
                    continue
                if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS'):
                    element.find_element_by_id(self.card_book_btn[-1]).click()
                    self.get_element(*self.book_primary_btn).click()
                    self.get_element(*self.bs_okay_btn).click()
                    return True
