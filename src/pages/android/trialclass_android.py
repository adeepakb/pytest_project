# Module Owner - Reshma R Nair
import re
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
        self.course_list = '%s/rvCourseList' % package_name
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
                self.login.text_match(
                    'Our academic counsellor will reach out to you shortly to provide more information on BYJU’S Classes.'):
            return ReturnType(True, 'Expected message is shown once user reaches maximum free trail class limit')
        else:
            return ReturnType(False, 'Expected message is not shown once user reaches maximum free trail class limit')

    def scroll_to_regular_classes(self):
        CommonMethods.scrollToElement(self.driver, 'Regular Classes')
        rc_section = self.obj.get_element('id', self.title)
        if rc_section.text.lower() == 'regular classes':
            session_list = self.obj.get_element('id', self.course_list)
            self.scroll_cards.scroll_by_card(rc_section, session_list)

    def is_free_trial_class_present_under_reg_class(self):
        self.scroll_to_regular_classes()
        try:
            cards_root = self.obj.get_elements(*self.rc_card_root)
            if len(cards_root) == 0:
                return ReturnType(False, 'No trial cards present under regular classes')
            while True:
                for card in cards_root:
                    try:
                        subject = self.obj.child_element_text(card, self.subject_name)
                        if subject in (
                                'PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS') and self.obj.child_element_displayed(
                            card,
                            self.card_book_btn):
                            return ReturnType(True, 'Trial class session card is present')
                    except NoSuchElementException:
                        return ReturnType(False, 'Trial class session card with book is not present')
        except NoSuchElementException:
            return ReturnType(False, 'No cards present in booking page')

    def is_master_class_present_under_master_class_section(self):
        try:
            cards_root = self.obj.get_elements(*self.rc_card_root)
            if len(cards_root) == 0:
                return ReturnType(False, 'No master classes present in book a free class screen')
            while True:
                for card in cards_root:
                    try:
                        subject = self.obj.child_element_text(card, self.workshop_label)
                        if subject == 'WORKSHOP' and self.obj.child_element_displayed(card, self.card_book_btn):
                            return ReturnType(True, 'Masterclass is present')
                    except NoSuchElementException:
                        return ReturnType(False, 'Masterclass is not present')
        except NoSuchElementException:
            return ReturnType(False, 'No cards present in booking page')

    def is_free_trial_class_details_present_under_reg_class(self):
        self.scroll_to_regular_classes()
        try:
            cards_root = self.obj.get_elements(*self.rc_card_root)
            if len(cards_root) == 0:
                return ReturnType(False, 'No trial classes present under regular classes')
            while True:
                for card in cards_root:
                    try:
                        subject = self.obj.child_element_text(card, self.subject_name)
                        if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS') \
                                and self.obj.get_element_text('id', self.card_topic_tv) is not None \
                                and self.obj.get_element_text('id', self.rc_card_schedule_tv) is not None \
                                and self.obj.get_element_text('id', self.other_slots_detail) is not None:
                            return ReturnType(True, 'Trial class session details are present')
                    except NoSuchElementException:
                        return ReturnType(False, 'Trial class session details are not  present')
        except NoSuchElementException:
            return ReturnType(False, 'No cards present in booking page')

    def is_master_class_details_present_under_master_class(self):
        try:
            cards_root = self.obj.get_elements(*self.rc_card_root)
            if len(cards_root) == 0:
                return ReturnType(False, 'No master classes present in book a free class screen')
            while True:
                for card in cards_root:
                    try:
                        subject = self.obj.child_element_text(card, self.workshop_label)
                        if subject == 'WORKSHOP' and self.obj.get_element_text('id', self.card_topic_tv) is not None \
                                and self.obj.get_element_text('id', self.rc_card_schedule_tv) is not None \
                                and self.obj.get_element_text('id', self.other_slots_detail) is not None:
                            return ReturnType(True, 'Master class session details are present')
                    except NoSuchElementException:
                        return ReturnType(False, 'Master class session details are not present')
        except NoSuchElementException:
            return ReturnType(False, 'No cards present in booking page')

    def click_on_book_btn_reg_class(self):
        self.scroll_to_regular_classes()
        cards_root = self.obj.get_elements(*self.rc_card_root)
        if len(cards_root) == 0:
            raise Exception("No trial classes present under regular classes")
        for card in cards_root:
            subject = self.obj.child_element_text(card, self.subject_name)
            if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS'):
                self.obj.child_element_click_by_id(card, self.card_book_btn)
                break

    def is_date_and_time_popup_present(self):
        self.obj.is_text_match('Select date & time')
        if self.obj.is_element_present('id', self.toggle_buttons):
            try:
                if self.obj.get_element_text('id', self.confirm_book_popup_date) is not None:
                    return ReturnType(True, 'Toggle buttons and Date present in Select date & time popup')
                else:
                    return ReturnType(False, 'Date is empty in Select date & time popup')
            except NoSuchElementException:
                return ReturnType(False, 'Date element is not present in Select date & time popup')
        else:
            return ReturnType(False, 'Toggle buttons not present in Select date & time popup')

    def verify_select_date_time_buttons(self):
        if self.obj.is_button_displayed('Confirm & Book'):
            if self.obj.is_text_match('Cancel'):
                return ReturnType(True, 'Confirm & Book and Cancel buttons are present in Select date & time popup')
            else:
                return ReturnType(False, 'Cancel button is not present in Select date & time popup')
        else:
            return ReturnType(False, 'Confirm & Book button is not present in Select date & time popup')

    def click_on_confirm_n_book_btn(self):
        self.obj.button_click("Confirm & Book")
        self.obj.element_click('id', self.bs_okay_btn)

    def close_application(self):
        self.driver.close_app()

    def dismiss_trail_popup(self):
        if self.obj.is_element_present('id', self.bottom_sheet):
            self.obj.click_link('Dismiss')

    def verify_trial_class_confirmation_msg(self):
        self.obj.wait_for_locator('id', 'com.byjus.thelearningapp.premium:id/appTextView_title')
        if self.login.text_match("You Successfully Booked"):
            return ReturnType(True, 'Successfully trial class booked message is displayed')
        else:
            return ReturnType(False, 'Successfully trial class booked message is not displayed')

    def verify_booking_screen(self):
        elements = [self.bs_success_title, self.bs_topic_name, self.bs_date_text, self.bs_time_text]
        displayed_status = []
        for element in elements:
            displayed_status.append(self.obj.get_element(*element).is_displayed())
            if all(displayed_status):
                continue
            else:
                return ReturnType(False, '%s is not displayed in booking confirmation page' % element[1])
        return ReturnType(True, 'Session title , date , day , time are displayed in booking confirmation page')

    def verify_timer(self):
        elements = [self.bs_count_down_layout, self.bs_count_down_hour, self.bs_count_down_minutes,
                    self.bs_count_down_seconds]
        displayed_status = []
        for element in elements:
            displayed_status.append(self.obj.get_element(*element).is_displayed())
            if all(displayed_status):
                continue
            else:
                return ReturnType(False, '%s is not displayed in booking confirmation page' % element[1])
        return ReturnType(True, 'Session starts in time is not displayed in booking confirmation page')

    def verify_okay_button_present(self):
        if self.obj.is_button_displayed("Okay"):
            return ReturnType(True, 'Okay button is displayed in trial class booking confirmation page')
        else:
            return ReturnType(False, 'Okay button is not displayed in trial class booking confirmation page')

    def verify_timer_format(self):
        elements = [self.bs_count_down_hour, self.bs_count_down_hour_text,
                    self.bs_count_down_minutes, self.bs_count_down_minutes_text,
                    self.bs_count_down_seconds, self.bs_count_down_seconds_text]
        element_text_parts = []
        for element in elements:
            element_text_parts.append(self.obj.get_element(*element).text)
        element_text = (" ".join(element_text_parts))
        m = re.match("[0-9][0-9] HOURS? [0-5][0-9] MINS? [0-5][0-9] SECS?", element_text)
        if m is not None:
            return ReturnType(True, 'Timer is displayed in HH.MM.SS format in booking confirmation page')
        else:
            return ReturnType(True, 'Timer is not displayed in HH.MM.SS format in booking confirmation page')

    def is_filling_fast_present(self):
        if self.obj.is_element_present('id', self.filling_fast):
            return ReturnType(True, 'slot avaliblity indicator(Filling Fast) is present in regular class booking page')
        else:
            return ReturnType(False,
                              'slot avaliblity indicator(Filling Fast)  is present in regular class booking page')

    def is_trial_card_unique_in_booking_page(self):
        self.scroll_to_regular_classes()
        trial_class_topics = []
        i = 0
        while True:
            cards_root = self.obj.get_elements(*self.rc_card_root)
            if len(cards_root) == 0:
                return ReturnType(False, 'No trial cards present under regular classes')
            for card in cards_root:
                subject = self.obj.child_element_text(cards_root[i], self.subject_name)
                if subject in ('PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'MATHEMATICS'):
                    trial_class_topics.append(self.obj.child_element_text(cards_root[i], self.card_topic_tv))
                i += 1
                if i == 4:
                    break
            if i == 4:
                prev_cards = cards_root
                self.scroll_cards.scroll_by_card(cards_root[3], cards_root[0])
                cards_root = self.obj.get_elements(*self.rc_card_root)
                prev_card_subject = self.obj.child_element_text(prev_cards[3], self.card_topic_tv)
                card_subject = self.obj.child_element_text(cards_root[3], self.card_topic_tv)
                if prev_card_subject == card_subject:
                    for i in range(len(trial_class_topics) - 1):
                        if trial_class_topics[i] == trial_class_topics[i + 1]:
                            return ReturnType(False, 'duplicate session cards  present with same session name %s' %
                                              trial_class_topics[i])
                        else:
                            print('No duplicate session cards  present with same session name %s' % trial_class_topics)
                            return ReturnType(True, 'No duplicate session cards present with same session name')
                i = 1

    def is_free_trial_card_not_present(self,backend_scheduled_start_time):
        self.scroll_to_regular_classes()
        cards = self.obj.get_elements(*self.rc_card_root)
        if len(cards) == 0:
            return ReturnType(False, 'No trial card present under regular classes')
        for card in cards:
            if "Today %s"%backend_scheduled_start_time in self.obj.child_element_text(card,self.rc_card_schedule_tv) :
                return ReturnType(False, 'Trial session which starts at %s(within 30 mins) is present under regular classes' % backend_scheduled_start_time)
            else:
                continue
        return ReturnType(True,'Trial session which starts at %s(within 30 mins) is not present under regular classes' % backend_scheduled_start_time)