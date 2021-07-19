import random
import re
from datetime import datetime, timedelta
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from pages.android.application_login import Login
from pages.android.scroll_cards import ScrollCards
from pages.android.session_requisite import SessionRequisite
from utilities.return_type import ReturnType
from utilities.staging_tllms import Stagingtllms
from pages.android.student_dashboard_otm import StudentDashboardOneToMega
from pages.base.masterclass import MasterClassBase
from utilities.tutor_common_methods import TutorCommonMethods
from utilities.exceptions import *
import pytest_check as check


class MasterClass(MasterClassBase, TutorCommonMethods):
    def __init__(self, driver):
        self.driver = driver
        self.login = Login(driver)
        self.action = TouchAction(driver)
        self.scroll_cards = ScrollCards(driver)
        self.session_requisite = SessionRequisite(self.driver)
        super().__init__(driver)
        self.device_type = self.get_device_type()
        self.staging = Stagingtllms(self.driver)
        self.dashboard = StudentDashboardOneToMega(self.driver)
        self.__init_locators(self.device_type)
        self.ERROR_MESSAGE = 'Please connect to network and try again!'
        self.join_topic_name = None

    def __init_locators(self, device_type=None):
        package_name = self.driver.capabilities['appPackage'] + ':id'
        self.section_name = 'id', '%s/sectionName' % package_name
        self.card_list = 'id', '%s/sessions_list' % package_name
        self.card_root = 'id', '%s/card_root' % package_name
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
        self.see_more_tv = 'id', '%s/tvShowMoreText' % package_name
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
        rc_section = self.get_elements(*self.section_name)[-1]
        if rc_section.text.lower() == 'recommended classes':
            session_list = self.get_element(*self.card_list)
            self.scroll_cards.scroll_by_card(rc_section, session_list)
        elif rc_section.text.lower() == 'up next':
            self.get_element(
                'android_uiautomator',
                'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                f'scrollTextIntoView("{rc_text.title()}")'
            )
            rc_section = self.get_elements(*self.section_name)[-1]
            session_list = self.get_element(*self.card_list)
            self.scroll_cards.scroll_by_card(rc_section, session_list)
        else:
            raise Exception("'Recommended Classes' section could not be located on the page.")

    def is_rc_session_card_displayed(self):
        self.scroll_rc_in_view()
        cards_root = self.get_elements(*self.rc_card_root)
        for card in cards_root:
            if card.find_element_by_id(self.card_label_tv[-1]).text.lower() == 'workshop':
                return ReturnType(True, "RC card is displayed")
        return ReturnType(False, "RC card is not displayed")

    def is_sessions_under_rc_displayed(self):
        self.scroll_rc_in_view()
        rc_sessions = False
        list_content = self.get_elements('xpath', f'//*[@resource-id="{self.card_list[-1]}"]/*')
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
                    return ReturnType(True, "rc session is displayed")
        self.login.implicit_wait_for(15)
        return ReturnType(False, "rc session is displayed")

    def verify_rc_session_card_details(self):
        rc_card_root = self.get_element(*self.rc_card_root)
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
        return ReturnType(True, "rc session card details are shown") if all(
            (
                logo_displayed, label_displayed, topic_name_displayed, schedule_match_displayed,
                book_btn)) else ReturnType(
            False, "rc session card details are not  shown")

    def is_all_rc_sessions_displayed(self):
        rc_sessions = self.get_elements(*self.rc_card_root)
        c = 0
        for session in rc_sessions:
            label = session.find_element_by_id(self.card_label_tv[-1])
            if label.text.lower() == 'workshop':
                c += 1
        if c == len(rc_sessions) > 1:
            return ReturnType(True, "All Rc sessions are displayed")
        return ReturnType(False, "All Rc sessions are not being displayed")

    def is_see_all_link_displayed(self):
        see_more_less = self.get_element(
            'android_uiautomator',
            'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
            f'scrollIntoView(resourceId("{self.see_more_tv[-1]}"))'
        )
        return ReturnType(True, "All links displayed") if see_more_less.is_displayed() else ReturnType(False,
                                                                                                       "All links are not displayed")

    def click_option_see_more(self, text: str = 'see all'):
        if self.is_see_all_link_displayed().result:
            see_more = self.get_element(*self.see_more_tv)
            if see_more.text.lower() == text:
                see_more.click()
        return self

    def reset_view(self):
        try:
            self.get_element(
                'android_uiautomator',
                'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                f'scrollTextIntoView("Up Next")'
            )
            return ReturnType(True, "Reset is being viewed")
        except:
            return ReturnType(False, "Reset is not  being viewed")

    def get_up_next_master_class_session(self, hp_tab=True):
        self.dashboard.ps_home_page_tab()
        self.click_option_see_more().reset_view()
        check, view_changed = 3, False
        list_view = self.get_element(*self.card_list)
        list_content = self.get_elements('xpath', f'//*[@resource-id="{self.card_list[-1]}"]/*')
        section_name = list_content[0].find_element_by_id(self.section_name[-1]).text.lower()
        self.login.implicit_wait_for(0)
        while check:
            list_content = self.get_elements('xpath', f'//*[@resource-id="{self.card_list[-1]}"]/*')
            for element in list_content:
                if view_changed:
                    try:
                        section_name = element.find_element_by_id(self.section_name[-1]).text.lower()
                    except NoSuchElementException:
                        pass
                if section_name == 'up next':
                    try:
                        if element.find_element_by_id(self.card_label_tv[-1]).is_displayed():
                            try:
                                if element.find_element_by_id(self.pr_status_msg[-1]).text.lower() == 'completed':
                                    return False
                                else:
                                    return element
                            except NoSuchElementException:
                                return element
                    except NoSuchElementException:
                        pass
                elif section_name == 'recommended classes' and view_changed:
                    return False
            self.scroll_cards.scroll_by_card(list_content[-2], list_view)
            view_changed = True
            check -= 1

    def get_completed_master_class_session(self):
        self.dashboard.ps_home_page_tab(tab_name='Completed')
        sessions = self.get_elements(*self.card_root)
        today = datetime.now().strftime("%d %b")
        self.login.implicit_wait_for(0)
        for session in sessions:
            try:
                if session.find_element_by_id(self.card_label_tv[-1]).is_displayed() and \
                        session.find_element_by_id(self.pr_date[-1]).text == today:
                    return session
            except NoSuchElementException:
                pass

    def is_master_class_booked(self):
        completed_session = self.get_completed_master_class_session()
        mc_completed_session = completed_session.is_displayed() if completed_session is not None else False
        up_next_session = self.get_up_next_master_class_session()
        mc_up_next_session = up_next_session.is_displayed() if not isinstance(up_next_session, bool) \
            else up_next_session
        return ReturnType(True, "Master class is booked") if any(
            (mc_up_next_session, mc_completed_session)) else ReturnType(False, "Master class is not booked")

    def is_regular_session_displayed(self):
        list_view = self.get_element(*self.card_list)
        check = 2
        while check:
            list_content = self.get_elements('xpath', f'//*[@resource-id="{self.card_list[-1]}"]/*')
            for element in list_content:
                try:
                    element.find_element_by_id(self.card_label_tv[-1])
                except NoSuchElementException:
                    return ReturnType(True, "Regular sessions are displayed")
            self.click_option_see_more()
            self.scroll_cards.scroll_by_card(list_content[-1], list_view)
            check -= 1
        return ReturnType(False, "Regular sessions are not  being displayed")

    def verify_booking_screen(self, booking_success_activity=""):
        self.login.implicit_wait_for(0)
        element = None
        if not booking_success_activity:
            try:
                header_text = self.get_element(*self.bs_header_title).text
                check.equal(header_text.lower(), 'select date & time', "Header title is not correct in booking screen")
                try:
                    element = self.book_primary_btn[-1]
                    confirm_book = self.get_element(*self.book_primary_btn).text
                    element = self.book_secondary_btn[-1]
                    cancel_text = self.get_element(*self.book_secondary_btn).text
                except NoSuchElementException:
                    return ReturnType(False, "Booking Screen details are wrong")
                check.equal(confirm_book.lower(), 'confirm & book', "confirm and book is wrong")
                check.equal(cancel_text.lower(), 'cancel', 'cancel display is wrong')
                return ReturnType(True, "Booking screen details are correct")
            except NoSuchElementException:
                return ReturnType(False, "Booking Screen details are wrong")
        else:
            assert self.wait_activity(booking_success_activity)
            elements = [
                self.bs_success_title, self.bs_topic_name, self.bs_date_text,
                self.bs_time_text, self.bs_count_down_parent, self.bs_count_down_hour, self.bs_okay_btn]
            displayed_status = list()
            for element in elements:
                displayed_status.append(self.get_element(*element).is_displayed())
            check.equal(all(displayed_status), True, "Booking screen details are wrong")
            return ReturnType(True, "Session screen details are correct") if all(displayed_status) else ReturnType(
                False, "Booking Screen details are wrong")

    def book_special_master_class(self):
        self.login.implicit_wait_for(2)
        sessions = self.get_elements(*self.rc_card_root)
        for session in sessions:
            try:
                session.find_element_by_id(self.card_book_btn[-1]).click()
                sessions.clear()
                self.get_element(*self.book_primary_btn).click()
                self.get_element(*self.bs_okay_btn).click()
                return ReturnType(True, "Booked master class")
            except NoSuchElementException:
                return ReturnType(False, "Couldnt book master class")

    def book_master_class(self, new_session=False, validate=False, ff_tag=True, error_validate=True, **kwargs):
        if not self.is_master_class_booked().result or new_session:
            db = kwargs['db']
            self.scroll_rc_in_view()
            booking_success_activity = 'BookingSuccessActivity'
            otm_home_activity = 'OneToMegaHomeActivity'
            sessions = self.get_elements(*self.rc_card_root)
            self.login.implicit_wait_for(1)
            for session in sessions:
                try:
                    if ff_tag:
                        assert session.find_element_by_id(self.card_filling_fast_label[-1]).is_displayed()
                    db.booked_date_time = session.find_element_by_id(self.rc_card_schedule_tv[-1]).text
                    session.find_element_by_id(self.card_book_btn[-1]).click()
                    sessions.clear()
                except NoSuchElementException:
                    pass
            self.login.implicit_wait_for(15)
            if validate:
                self.verify_booking_screen()
            try:
                self.get_element(*self.book_primary_btn).click()
            except NoSuchElementException:
                pass
            if error_validate:
                error_message = None
                try:
                    error_message = self.get_element(*self.dialog_message).text
                except NoSuchElementException:
                    try:
                        error_message = self.get_element(*self.snack_bar).text
                    except NoSuchElementException:
                        pass
                finally:
                    if error_message is not None and self.wait_activity(otm_home_activity):
                        return error_message
            if self.wait_activity(booking_success_activity):
                if validate:
                    self.verify_booking_screen(booking_success_activity)
                self.get_element(*self.bs_okay_btn).click()
                assert self.wait_activity(otm_home_activity)
            return True

    def is_all_workshop_tag_displayed(self):
        rc_sessions = self.get_elements(*self.rc_card_root)
        count = 0
        for rc_session in rc_sessions:
            rc_session.find_element_by_id(self.card_label_tv[-1])
            count += 1
        if count == len(rc_sessions):
            return ReturnType(True, "All workshop tags are being displayed")
        return ReturnType(False, "All workshop tags are not  being displayed")

    def verify_session_details(self, element_name: str = None):
        if element_name.lower() == 'topic_name':
            return self.get_element(*self.sd_topic_details).is_displayed()
        elif element_name.lower() == 'slots':
            e1 = self.get_element(*self.sd_slot_header).is_displayed()
            e2 = self.get_element(*self.sd_scroll_view).get_attribute('scrollable')
            e3 = self.get_element(*self.sd_time_slot_list).is_displayed()
            if e1 and e3 and e2 == 'true':
                return True
            return False
        elif element_name.lower() == 'book_button':
            return self.get_element(*self.sd_book_btn).is_displayed()
        else:
            raise NotImplementedError(f'verification for the element "{element_name}" is not yet implemented. ')

    def tap_on_master_card(self):
        self.get_element(*self.rc_card_root).click()
        self.login.implicit_wait_for(15)
        try:
            self.get_element(*self.sd_topic_details)
        except NoSuchElementException:
            pass

    def book_offline(self, **kwargs):
        self.get_element(*self.card_book_btn).click()
        self.login.implicit_wait_for(2.5)
        try:
            error_message = self.get_element(*self.snack_bar).text
        except NoSuchElementException:
            self.get_element(*self.book_primary_btn).click()
            error_message = self.get_element(*self.snack_bar).text
        if error_message == self.ERROR_MESSAGE:
            return True
        return False

    def is_upcoming_regular_cards_displayed(self, view='expanded'):
        self.reset_view()

        if view == 'expanded':
            card_list = self.get_elements(*self.session_card_reg)
            self.scroll_cards.scroll_by_card(card_list[1], self.get_element(*self.card_list))
            len_cards = len(self.get_elements(*self.session_card_reg))
        else:
            len_cards = len(self.get_elements(*self.session_card_reg))
        if len_cards > 3 and view == 'expanded':
            return ReturnType(True, "upcoming regular class are displayed in expanded")
        elif len_cards <= 3 and view == 'collapse':
            return ReturnType(True, "upcoming regular class are displayed in collapse")
        return ReturnType(True, "upcoming regular class are not displayed in collapse and expanded")

    def is_regular_classes_scrollable(self):
        if self.is_see_all_link_displayed().result:
            return ReturnType(True, "Regular class is scrollable") if self.get_element(
                *self.session_card_reg).is_displayed() else ReturnType(False, "Regular class is scrollable")

    def verify_filling_fast_label(self, section='masterclass'):
        if section.lower() == 'masterclass':
            sessions = self.get_elements(*self.rc_card_root)
        elif section == 'regular':
            sessions = self.get_elements(*self.card_root)
        else:
            raise NotImplementedError(f'{section} section validation is not yet implemented')
        self.login.implicit_wait_for(0)
        for session in sessions:
            try:
                return ReturnType(True, "Filling fast label is displayed") if session.find_element_by_id(
                    self.card_filling_fast_label[-1]).is_displayed() else ReturnType(False,
                                                                                     "Filling fast label is not displayed")
            except NoSuchElementException:
                pass
        return ReturnType(False,
                          "Filling fast label is not displayed")

    def is_master_class_available(self, day="today", max_rec=None):
        try:
            session = self.get_up_next_master_class_session()
            if session and day == "today":
                try:
                    session.find_element_by_id(self.pr_status_msg[-1])
                    return ReturnType(False, "Master class is not available for {} ".format(day))
                except NoSuchElementException:
                    return ReturnType(True, "Master class is  available for {}".format(day))
            else:
                raise SessionNotFoundError("no 'Up Next' masterclass session is available, try resetting if already "
                                           "ended.")
        except SessionNotFoundError:
            self.dashboard.ps_home_page_tab('completed')
            try:
                topic_name = self.get_element(*self.reg_card_topic).text
            except NoSuchElementException:
                topic_name = self.get_element(*self.pr_card_topic).text
            self.staging.reset_session_one_to_mega(
                profile='login_details_3', user_profile='user_2', sub_profile='profile_3', topic_name=topic_name)
            if not max_rec:
                return self.is_master_class_available(max_rec=True)
            else:
                raise SessionNotFoundError("no 'Up Next' masterclass session is available, try resetting if already "
                                           "ended.") from None

    def get_master_class_join_now_button(self):
        session = self.get_up_next_master_class_session()
        if session:
            try:
                join_now_btn = session.find_element_by_id(self.card_strip_btn[-1])
                if join_now_btn:
                    if join_now_btn.text.lower() == 'join now':
                        return session
                return None
            except NoSuchElementException:
                return None

    def tap_up_next_mc_session(self):
        session = self.get_up_next_master_class_session()
        session.click()

    def join_master_class_session(self, screen='dashboard'):
        self.staging.attach_session_video(grade="4", profile='login_details_3', user_profile='user_2',
                                          sub_profile='profile_3')
        self.dashboard.refresh()
        btn = self.get_master_class_join_now_button()
        if btn is None:
            session = self.get_up_next_master_class_session()
            if session is False:
                session = self.get_completed_master_class_session()
                try:
                    topic_name = session.find_element_by_id(self.reg_card_topic[-1]).text
                except NoSuchElementException:
                    topic_name = session.find_element_by_id(self.pr_card_topic[-1]).text
            else:
                try:
                    topic_name = session.find_element_by_id(self.card_topic_tv[-1]).text
                except NoSuchElementException:
                    topic_name = session.find_element_by_id(self.pr_card_topic[-1]).text
            self.staging.reset_session_one_to_mega(
                profile='login_details_3', user_profile='user_2', sub_profile='profile_3', topic_name=topic_name)
            btn = self.get_master_class_join_now_button()
        if screen == 'details_screen':
            self.tap_up_next_mc_session()
            btn = self.get_element(*self.sd_action_lyt_btn)
            if not btn.text.lower() == "join now":
                raise SessionEndedError('current master class session might be already ended.')
            self.join_topic_name = self.get_element(*self.sd_topic_details).text
            btn.find_element_by_id(self.sd_action_lyt_btn[-1]).click()
        else:
            self.join_topic_name = self.get_element(*self.reg_card_topic).text
            btn.find_element_by_id(self.card_strip_btn[-1]).click()
        assert self.wait_activity('PremiumSchoolSessionActivity')

    def skip_the_session_booking_time(self):
        sessions = self.get_elements(*self.rc_card_root)
        self.login.implicit_wait_for(0)
        for session in sessions:
            if session.find_element_by_id(self.card_filling_fast_label[-1]).is_displayed():
                session_time_12, midday = session.find_element_by_id(
                    self.rc_card_schedule_tv[-1]).text.split(',')[-1].strip().split()
                if midday == 'PM' and (int(session_time_12.split(":")[0])) != 12:
                    ah, am = ((int(session_time_12.split(":")[0]) + 12), int(session_time_12.split(":")[-1]))
                else:
                    ah, am = tuple(map(int, session_time_12.split(":")))
                ch, cm = tuple(map(int, (datetime.now() + timedelta(minutes=30)).strftime("%H %M").split()))
                diff = (am - cm)
                if ah == ch:
                    if diff < 0:
                        return ReturnType(True, "Session booking time skipped succeesfully")
                    elif diff <= 2 or diff == 0:
                        diff = (diff + 1) * 60
                        while diff:
                            if diff % 5 == 0:
                                self.get_element(*self.card_label_tv)
                            sleep(1)
                            diff -= 1
                        return ReturnType(True, "Session booking time skipped succeesfully")
                    else:
                        raise Exception("too long to wait")
                return ReturnType(False, "Session booking time has not been  skipped succeesfully")

    def end_master_class_session(self):
        self.join_master_class_session()
        self.staging.end_ongoing_session(user_profile='user_2', sub_profile='profile_3',
                                         topic_name=self.join_topic_name)
        self.login.implicit_wait_for(15)
        self.get_element(*self.dashboard.bottom_sheet_submit_btn).click()
        self.dashboard.session_rating(action="skip")

    def is_completed_mc_session_displayed(self, tab_name='for you'):
        self.dashboard.ps_home_page_tab(tab_name)
        self.dashboard.ps_home_page_tab(tab_name, check=True)
        mc_session_elements = [self.card_label_tv, self.pr_status_icon, self.pr_status_msg, self.pr_date]
        session = self.get_element(*self.card_root)
        for i, element_loc in enumerate(mc_session_elements):
            element = session.find_element_by_id(element_loc[-1])
            if i == 2:
                assert element.text == 'Completed'
            elif i == 3:
                assert element.text == (datetime.now().strftime("%d %b"))
            assert element.is_displayed()

    def attach_requisite(self, req_type='all', asset_type=''):
        session = self.get_completed_master_class_session()
        try:
            topic_name = session.find_element_by_id(self.reg_card_topic[-1]).text
        except NoSuchElementException:
            topic_name = session.find_element_by_id(self.pr_card_topic[-1]).text
        if req_type == 'all':
            self.staging.attach_requisite_group(user_profile='user_2',
                                                sub_profile='profile_3', grade="4",
                                                days='today', req_type='pre_post_ak3_29', asset_type=asset_type.lower(),
                                                profile='login_details_3')
        else:
            raise NotImplementedError()

    @staticmethod
    def format_date_time(raw_date_time):
        raw_date_time = raw_date_time.split(', ')
        r_date, r_time = raw_date_time[0], raw_date_time[-1]
        t = datetime.strptime(r_time, "%I:%M %p")
        time_24 = t.strftime("%H:%M")
        if r_date.lower() == 'today':
            date_month = datetime.now().strftime("%d %m")
        elif r_date.lower() == 'tomorrow':
            date_month = (datetime.now() + timedelta(days=1)).strftime("%d %m")
        else:
            d = datetime.strptime(r_date, "%d %b")
            date_month = d.strftime("%d %m")
        return date_month, time_24

    def is_master_class_sorted(self, db=None):
        self.reset_view()
        rc_sessions = self.get_elements(*self.card_root)
        session_date_time = None
        self.login.implicit_wait_for(0)
        for rc_session in rc_sessions:
            try:
                rc_session.find_element_by_id(self.card_label_tv[-1])
            except NoSuchElementException:
                continue
            try:
                session_time = rc_session.find_element_by_id(self.card_schedule_tv[-1]).text
            except NoSuchElementException:
                session_time = rc_session.find_element_by_id(self.pr_date[-1]).text
            if db.booked_date_time == session_time:
                next_session = rc_sessions.index(rc_session) + 1
                next_reg_session_date_time = rc_sessions[next_session] if next_session < len(rc_sessions) else None
                if next_reg_session_date_time is None:
                    raise SessionNotFoundError("end of regular session list!")
                else:
                    try:
                        session_date_time = next_reg_session_date_time.find_element_by_id(
                            self.card_schedule_tv[-1]).text
                    except NoSuchElementException:
                        session_date_time = next_reg_session_date_time.find_element_by_id(
                            self.pr_date[-1]
                        ).text
        if session_date_time is None:
            raise SessionNotFoundError("no booked masterclass session match in the session list")
        mc_date_month, mc_time = self.format_date_time(db.booked_date_time)
        r_date_month, r_time = self.format_date_time(session_date_time)
        mc_date, mc_month = mc_date_month.split()
        mc_hour, mc_minutes = mc_time.split(":")
        r_hour, r_minutes = r_time.split(":")
        r_date, r_month = r_date_month.split()
        if r_month > mc_month:
            return ReturnType(True, "Master class is sorted")
        elif r_month == mc_month:
            if r_date > mc_date:
                return ReturnType(True, "Master class is sorted")
            elif r_date == mc_date:
                if r_hour > mc_hour:
                    return ReturnType(True, "Master class is sorted")
                elif r_hour == mc_hour and r_minutes > mc_minutes:
                    return ReturnType(True, "Master class is sorted")
        return ReturnType(False, "Master class is  notsorted")

    def select_random_masterclass_date(self, action="cancel"):
        self.get_element(*self.card_slots_detail_tv)
        sessions = self.get_elements(*self.rc_card_root)
        self.login.implicit_wait_for(1)
        for session in sessions:
            try:
                session.find_element_by_id(self.card_book_btn[-1]).click()
                sessions.clear()
            except NoSuchElementException:
                pass
        self.login.implicit_wait_for(15)
        try:
            time_slot_view = self.get_element(*self.sd_time_slot_list)
            time_slots = time_slot_view.find_elements_by_class_name("android.widget.RelativeLayout")
            random.choice(time_slots).click()
            if action == "book":
                self.get_element(*self.book_primary_btn).click()
            elif action == "cancel":
                self.get_element(*self.book_secondary_btn).click()
        except NoSuchElementException:
            pass


class MasterClassFuturePaid(TutorCommonMethods):
    def __init__(self, driver):
        self.driver = driver
        self.login = Login(driver)
        self.action = TouchAction(driver)
        self.scroll_cards = ScrollCards(driver)
        self.session_requisite = SessionRequisite(self.driver)
        super().__init__(driver)
        self.device_type = self.get_device_type()
        self.staging = Stagingtllms(self.driver)
        self.dashboard = StudentDashboardOneToMega(self.driver)
        self.__init_locators(self.device_type)
        self.ERROR_MESSAGE = 'Please connect to network and try again!'
        self.join_topic_name = None

    def __init_locators(self, device_type=None):
        package_name = self.driver.capabilities['appPackage'] + ':id'
        self.section_name = 'id', '%s/sectionName' % package_name
        self.card_list_root = "id", "%s/root_view" % package_name
        self.card_list = 'id', '%s/rvCourseList' % package_name
        self.card_root = "id", "%s/cvSessionCard" % package_name
        self.card_root_reg = "id", "%s/card_root" % package_name
        self.card_label_tv = 'id', '%s/tvWorkshop' % package_name
        self.card_book_btn = 'id', '%s/btBookSession' % package_name
        self.session_header = "id", "%s/tvTitle" % package_name
        self.toolbar = "id", "%s/toolbarView" % package_name
        self.card_filling_fast_label = 'id', '%s/tvFillingFast' % package_name
        self.sc_card_schedule_tv = 'id', '%s/tvSessionTime' % package_name
        self.book_primary_btn = 'id', '%s/primaryAction' % package_name
        self.bs_okay_btn = 'id', '%s/appButtonCtaOk' % package_name
        self.snack_bar = 'id', '%s/snackbar_text' % package_name
        self.dialog_message = 'id', '%s/dialog_message' % package_name
        self.pr_date = 'id', '%s/post_requisite_date' % package_name
        self.pr_status_msg = 'id', '%s/post_requisite_status' % package_name

    def scroll_sc_in_view(self):
        try:
            self.get_element(
                'android_uiautomator',
                'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                f'scrollTextIntoView("Special Classes")'
            )
        except NoSuchElementException:
            return self.get_element(
                'android_uiautomator',
                'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                f'scrollTextIntoView("Recommended Classes")'
            ).is_displayed()
        toolbar = self.get_element(*self.toolbar)
        session_headers = self.get_elements(*self.session_header)
        for session_header in session_headers:
            if session_header.text.lower() == "special classes":
                start_location = session_header.location
                end_location = toolbar.location
                start_element_size = session_header.size
                start_x = start_location['x'] + start_element_size["width"] // 2
                start_y = start_location['y'] + start_element_size["height"] - 10
                end_y = end_location['y'] + toolbar.size["height"] + 10
                self.action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).wait(3000).release().perform()
                return

    def is_master_class_available(self):
        self.scroll_sc_in_view()
        card = self.get_element(*self.card_root)
        mc_label_text = card.find_element_by_id(self.card_label_tv[-1]).text.lower()
        if mc_label_text == "workshop" and card.find_element_by_id(self.card_book_btn[-1]).is_displayed():
            return ReturnType(True, "Master class is available")
        return ReturnType(False, "Master class is not available")

    def book_master_class(self, ff_tag=True, error_validate=True, **kwargs):
        db = kwargs['db']
        self.scroll_sc_in_view()
        booking_success_activity = 'BookingSuccessActivity'
        otm_home_activity = 'OneToMegaHomeActivity'
        sessions = self.get_elements(*self.card_root)
        self.login.implicit_wait_for(1)
        for session in sessions:
            try:
                if ff_tag:
                    assert session.find_element_by_id(self.card_filling_fast_label[-1]).is_displayed()
                db.booked_date_time = session.find_element_by_id(self.sc_card_schedule_tv[-1]).text
                session.find_element_by_id(self.card_book_btn[-1]).click()
                sessions.clear()
            except NoSuchElementException:
                pass
        self.login.implicit_wait_for(15)
        try:
            self.get_element(*self.book_primary_btn).click()
        except NoSuchElementException:
            pass
        if error_validate:
            error_message = None
            try:
                error_message = self.get_element(*self.dialog_message).text
            except NoSuchElementException:
                try:
                    error_message = self.get_element(*self.snack_bar).text
                except NoSuchElementException:
                    pass
            finally:
                if error_message is not None and self.wait_activity(otm_home_activity):
                    return error_message
        if self.wait_activity(booking_success_activity):
            self.get_element(*self.bs_okay_btn).click()
            assert self.wait_activity(otm_home_activity)
        return True

    def get_completed_master_class_session(self):
        self.dashboard.ps_home_page_tab(tab_name='Completed')
        sessions = self.get_elements(*self.card_root)
        if not sessions:
            sessions = self.get_elements(*self.card_root_reg)
        today = datetime.now().strftime("%d %b")
        self.login.implicit_wait_for(0)
        for session in sessions:
            try:
                if session.find_element_by_id(self.card_label_tv[-1]).is_displayed() and \
                        session.find_element_by_id(self.pr_date[-1]).text == today:
                    return session
            except NoSuchElementException:
                pass

    def get_up_next_master_class_session(self):
        package_name = self.driver.capabilities['appPackage'] + ':id'
        card_list = 'id', '%s/sessions_list' % package_name
        self.dashboard.ps_home_page_tab()
        check, view_changed = 3, False
        list_view = self.get_element(*card_list)
        list_content = self.get_elements('xpath', f'//*[@resource-id="{card_list[-1]}"]/*')
        section_name = list_content[0].find_element_by_id(self.section_name[-1]).text.lower()
        self.login.implicit_wait_for(0)
        while check:
            list_content = self.get_elements('xpath', f'//*[@resource-id="{card_list[-1]}"]/*')
            for element in list_content:
                if view_changed:
                    try:
                        section_name = element.find_element_by_id(self.section_name[-1]).text.lower()
                    except NoSuchElementException:
                        pass
                if section_name == 'up next':
                    try:
                        if element.find_element_by_id(self.card_label_tv[-1]).is_displayed():
                            try:
                                if element.find_element_by_id(self.pr_status_msg[-1]).text.lower() == 'completed':
                                    return False
                                else:
                                    return element
                            except NoSuchElementException:
                                return element
                    except NoSuchElementException:
                        pass
                elif section_name == 'recommended classes' and view_changed:
                    return False
            self.scroll_cards.scroll_by_card(list_content[-2], list_view)
            view_changed = True

    def is_master_class_booked(self):
        completed_session = self.get_completed_master_class_session()
        mc_completed_session = completed_session.is_displayed() if completed_session is not None else False
        up_next_session = self.get_up_next_master_class_session()
        mc_up_next_session = up_next_session.is_displayed() if not isinstance(up_next_session, bool) \
            else up_next_session
        return ReturnType(True, "Master class is booked") if any(
            (mc_up_next_session, mc_completed_session)) else ReturnType(False, "Master class is not booked")
