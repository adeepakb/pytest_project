import random
import time
from datetime import datetime
from time import sleep, strptime
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from pages.android.know_more import KnowMoreTest
from pages.android.login_android import LoginAndroid
from pages.android.scroll_cards import ScrollCards
from utilities.return_type import ReturnType
from utilities.staging_tllms import Stagingtllms
from pages.android.session_requisite import SessionRequisite
from pages.base.student_dashboard_otm import StudentDashboardBase
from utilities.tutor_common_methods import TutorCommonMethods
from utilities.exceptions import *
import pytest_check as check


class StudentDashboardOneToMega(StudentDashboardBase, TutorCommonMethods):
    def __init__(self, driver):
        """
        Args:
            driver:
        """
        self.driver = driver
        self.login = LoginAndroid(driver)
        self.action = TouchAction(driver)
        self.scroll_cards = ScrollCards(driver)
        self.session_requisite = SessionRequisite(self.driver)
        super().__init__(driver)
        self.device = self.get_device_type()
        self.device_type = self.get_device_type()
        self.staging = Stagingtllms(self.driver)
        self.__init_locators(self.device_type)

    def __init_locators(self, device_type=None):
        package_name = self.driver.desired_capabilities['appPackage'] + ':id'
        self.btn_premium = 'xpath', '//*[contains(@resource-id,"btnPremiumSchool")]'
        self.linear_layout = 'class name', 'android.widget.LinearLayout'
        self.nav_btn = 'id', '%s/backNav' % package_name
        self.chat_icon = 'id', '%s/optionalNav' % package_name
        self.card_list = 'id', '%s/sessions_list' % package_name
        self.see_more = 'id', '%s/see_more_tv' % package_name
        self.card_up_next = 'id', '%s/up_next_badge' % package_name
        self.card_subject_ico = 'id', '%s/subject_icon' % package_name
        self.card_subject_name = 'id', '%s/subject_name' % package_name
        self.card_topic_name = 'id', '%s/session_title' % package_name
        self.card_topic_name_pr = 'id', '%s/topic_name' % package_name
        self.card_time_desc = 'id', '%s/session_time' % package_name
        self.card_label_tv = 'id', '%s/tvWorkshop' % package_name
        self.card_content = 'id', '%s/content_card' % package_name
        self.card_content_header = 'id', '%s/session_header' % package_name
        self.see_more_tv = 'id', '%s/tvShowMoreText' % package_name
        self.requisite_card = 'id', '%s/llRequisiteContentLyt' % package_name
        self.pr_view = 'id', '%s/post_requisite_view' % package_name
        self.pre_req_time = 'id', '%s/pre_requisite_time' % package_name
        self.pr_heading = 'id', '%s/requisite_item_heading' % package_name
        self.pr_status_ico = 'id', '%s/post_requisite_status_icon' % package_name
        self.pr_status_msg = 'id', '%s/post_requisite_status' % package_name
        self.pr_status_date = 'id', '%s/post_requisite_date' % package_name
        self.pr_star_ico = 'id', '%s/post_requisite_star_icon' % package_name
        self.pr_star_rating = 'id', '%s/post_requisite_rating' % package_name
        self.sd_completed_img = 'id', '%s/sessionCompletedView' % package_name
        self.sd_subject_name = 'id', '%s/subjectNametv' % package_name
        self.sd_topic_name = 'id', '%s/chapterNametv' % package_name
        self.sd_calendar_ico = 'id', '%s/ivSessionCalendar' % package_name
        self.sd_date_desc = 'id', '%s/sessionDatetv' % package_name
        self.sd_clock_ico = 'id', '%s/ivTime' % package_name
        self.sd_time_desc = 'id', '%s/timeTv' % package_name
        self.sd_topic_desc = 'id', '%s/sessionDescriptionTv' % package_name
        self.sd_pre_req_list = 'id', '%s/rvPrepareSession' % package_name
        self.sd_post_req_list = 'id', '%s/rvReviseSession' % package_name
        self.sd_pre_req_header = 'id', '%s/prepareSessionTitleTextView' % package_name
        self.sd_post_req_header = 'id', '%s/reviseTitleTextView' % package_name
        self.sd_req_typ_title = 'id', '%s/tvTitle' % package_name
        self.sd_req_typ_desc = 'id', '%s/tvSubtitle' % package_name
        self.sd_req_typ_btn = 'id', '%s/tvWorksheetActionText' % package_name
        self.sd_req_assess = 'id', '%s/ivSessionType' % package_name
        self.sd_req_video_play = 'id', '%s/ivVideoPlay' % package_name
        self.sd_action_lyt_title = 'id', '%s/tvActionTitle' % package_name
        self.sd_action_lyt_desc = 'id', '%s/tvActionDescription' % package_name
        self.sd_action_lyt_btn = 'id', '%s/btnAction' % package_name
        self.sd_action_lyt_info_ico = 'id', '%s/infoImageLayout' % package_name
        self.sd_action_lyt_info_msg = 'id', '%s/tvActionInfo' % package_name
        self.sd_retry_btn = 'id', '%s/btnRetry' % package_name
        self.sd_content_details = 'id', '%s/sessionDetailScrollView' % package_name
        self.bottom_sheet_lyt = 'id', '%s/design_bottom_sheet' % package_name
        self.bottom_sheet_submit_btn = 'id', '%s/primaryAction' % package_name
        self.bottom_sheet_cancel_btn = 'id', '%s/secondaryAction' % package_name
        self.rating_bar = 'id', '%s/ratingBar' % package_name
        self.rating_btn_submit = 'id', '%s/btnSubmit' % package_name
        self.get_help_btn = 'id', '%s/roundedNavButton' % package_name
        self.assessment_retake = 'id', '%s/retake' % package_name
        self.assessment_start = 'id', '%s/test_start_button' % package_name
        self.assessment_submit_btn = 'id', '%s/rectangleNavButton' % package_name
        self.instruction_start_btn = 'id', '%s/btStartButton' % package_name
        self.toolbar_title_upnext = 'id', '%s/toolbar_title' % package_name
        if device_type != 'tab':
            self.toolbar_title = 'id', '%s/toolbar_title' % package_name
            self.home_page_tab = 'id', '%s/premium_school_home_tabs' % package_name
            self.card_root = 'id', '%s/card' % package_name
            self.card_root_sub = 'id', '%s/card_root' % package_name
            self.card_strip_title = 'id', '%s/strip_title' % package_name
            self.card_strip_desc = 'id', '%s/strip_message' % package_name
            self.card_strip_btn = 'id', '%s/card_strip_btn' % package_name
        else:
            self.toolbar_title = 'id', '%s/title' % package_name
            self.session_details = 'id', '%s/details_fragment' % package_name
            self.home_page_tab = 'id', '%s/tablet_home_tabs' % package_name
            self.card_root = 'id', '%s/card' % package_name
            self.card_strip_title = 'id', '%s/strip_title' % package_name
            self.card_strip_desc = 'id', '%s/strip_message' % package_name
            self.card_strip_btn = 'id', '%s/card_strip_btn' % package_name


    def verify_is_text_displayed(self, expected_text=None):
        while expected_text:
            try:
                response = self.get_element('xpath', "//*[contains(@text, '" + expected_text + "')]").is_displayed()
                return ReturnType(True, "{} is displayed".format(expected_text)) if response else ReturnType(False,
                                                                                                             "{} is not  displayed".format(
                                                                                                                 expected_text))
            except StaleElementReferenceException:
                pass
            except NoSuchElementException:
                return ReturnType(False, "{} is not  displayed".format(expected_text))

    def is_back_nav_btn_displayed(self):
        try:
            return self.get_element(*self.nav_btn).is_displayed()
        except NoSuchElementException:
            return False

    def is_one_to_mega_screen_displayed(self):
        activity_name = 'OneToMegaHomeActivity'
        screen_status = self.wait_activity(activity_name)
        return screen_status

    def ps_home_page_tab(self, tab_name="For you", check=False):
        try:
            if self.get_element(*self.toolbar_title_upnext).text.lower() == 'up next':
                self.click_back()
        except:
            pass
        action_bar_tab = self.get_element(*self.home_page_tab)
        tabs_view = action_bar_tab.find_elements_by_class_name('android.widget.TextView')
        for tab_view in tabs_view:
            if tab_view.text.lower() == tab_name.lower():
                if not check and not tab_view.is_selected():
                    tab_view.click()
                    return tab_view.is_selected()
                elif check:
                    return tab_view.is_selected()
        return False

    def get_session(self, session_type='up_next'):
        retry = 1
        self.ps_home_page_tab()
        self.session_requisite.is_cards_loaded()
        self.login.implicit_wait_for(0)
        # self.scroll_up_next_top()
        while retry:
            try:
                see_more_less = self.get_element(*self.see_more_tv)
                if see_more_less.text.lower() != 'see less':
                    see_more_less.click()
                    try:
                        if self.is_button_displayed('retry'):
                            self.click_back()
                    except:
                        pass
            except NoSuchElementException:
                pass
            session_list = self.get_element(*self.card_list)
            session_cards = session_list.find_elements_by_class_name('android.view.ViewGroup')
            for session in session_cards:
                try:
                    if session_type == 'up_next':
                        try:
                            session.find_element_by_id(self.pr_status_ico[-1])
                            self.login.implicit_wait_for(0)
                            continue
                        except NoSuchElementException:
                            #self.click_back()
                            return session
                    elif session_type == 'future':
                        try:
                            session.find_element_by_id(self.pr_status_ico[-1])
                            self.login.implicit_wait_for(0)
                            break
                        except NoSuchElementException:
                            return random.choice(session_cards)
                    elif session_type == 'tomorrow':
                        time_now = time.strftime('%d %m')
                        current_day, current_month = list(map(int, time_now.split()))
                        current_day += 1
                        try:
                            actual_time_raw = session.find_element_by_id(self.pre_req_time[-1]).text
                        except NoSuchElementException:
                            try:
                                actual_time_raw = session.find_element_by_id(self.card_time_desc[-1]).text
                            except NoSuchElementException:
                                actual_time_raw = session.find_element_by_id(self.pr_status_date[-1]).text
                        if 'today' in actual_time_raw.lower():
                            actual_date, actual_month = list(map(int, time.strftime("%d %m").split()))
                        else:
                            dt_mn = actual_time_raw.split(",")[0]
                            struct_time = time.strptime(dt_mn, "%d %b")
                            actual_month, actual_date = struct_time.tm_mon, struct_time.tm_mday
                        if actual_month == current_month:
                            if actual_date == current_day:
                                return session
                    else:
                        NotImplementedError()
                except (IndexError, NoSuchElementException):
                    pass
            self.scroll_cards.scroll_by_card(session_cards[-1], session_list)
            retry -= 1
        raise SessionNotFoundError('no up coming sessions available')

    def completed_session(self):
        p_e = self.get_element(*self.card_root)
        if p_e.find_element_by_id(self.pr_view[-1]).is_displayed():
            return p_e

    def click_on_card(self, session_type=None):
        session_card = None
        session_type = "_".join(session_type.split())
        if session_type == 'future' or session_type == 'tomorrow' or session_type == 'up_next':
            session_card = self.get_session(session_type)
        elif session_type == 'completed':
            session_card = self.completed_session()
        session_list = self.get_element(*self.card_list)
        outer_limit = self.driver.get_window_rect()['height'] * (95 / 100)
        if session_card.location['y'] > outer_limit:
            self.scroll_cards.scroll_by_card(start_element=session_card, end_element=session_list)
        x = session_card.location['x'] + session_card.size['width'] // 2
        y = session_card.location['y'] + 0.3 * session_card.size['height'] // 2
        self.action.tap(x=x, y=y).perform()

    def verify_rate_join_now(self, expected=None):
        btn_text = self.get_element(*self.card_strip_btn).text
        if btn_text.lower() == expected:
            return True
        return False

    def is_button_displayed(self, btn_type=None):
        btn_status = None
        retry = 2
        while retry:
            try:
                if btn_type == 'get help':
                    btn_status = self.get_element(*self.chat_icon).is_displayed()
                elif btn_type == 'app back':
                    btn_status = self.get_element(*self.nav_btn).is_displayed()
                elif btn_type.lower() == 'retry':
                    btn_status = self.network_btn_retry(verify=True)
                elif btn_type.lower() == 'rate now' or btn_type.lower() == 'join now':
                    btn_status = self.verify_rate_join_now(expected=btn_type.lower())
                return btn_status
            except StaleElementReferenceException:
                retry -= 1
                sleep(1)

    def is_join_now_btn_displayed(self):
        retry = 1
        while retry:
            try:
                ele = self.get_element(
                    'android_uiautomator',
                    'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                    f'scrollIntoView(resourceId("{self.card_strip_btn[-1]}"))'
                )
                if ele.text == 'Join Now':
                    return ReturnType(True, "Join now button is displayed")
                else:
                    self.ps_home_page_tab(tab_name='completed')
                    try:
                        topic_name = self.get_element(*self.card_topic_name_pr).text
                    except NoSuchElementException:
                        topic_name = self.get_element(*self.card_topic_name).text
                    self.staging.reset_session_one_to_mega(topic_name=topic_name)
                    self.refresh()
            except NoSuchElementException:
                return ReturnType(False, "Join now button is not being displayed")
            retry -= 1

    def session_join_now(self):
        root_element = self.get_element(*self.card_root)
        in_session = root_element.find_element_by_id(self.card_time_desc[-1]).text
        if 'Today' in in_session:
            try:
                join_now = root_element.find_element_by_id(self.card_strip_btn[-1])
            except NoSuchElementException:
                join_now = self.driver.find_element_by_id(self.card_strip_btn[-1])
            if join_now.text == 'Join Now':
                join_now.click()

    def is_bottom_sheet_displayed(self):
        self.login.implicit_wait_for(2)
        try:
            self.get_element(*self.bottom_sheet_lyt, wait=False)
            return ReturnType(True, "Bottom  sheet is displayed")
        except NoSuchElementException:
            return ReturnType(False, "Bottom  sheet is not displayed")
        finally:
            self.login.implicit_wait_for(15)

    def bottom_sheet_okay_btn(self, verify=False):
        timeout = 2
        okay_btn = self.get_element(*self.bottom_sheet_submit_btn)
        if not verify:
            okay_btn.click()
            while timeout:
                if self.is_bottom_sheet_displayed().result:
                    timeout -= 1
                    sleep(1)
                else:
                    return
        else:
            return ReturnType(True,
                              "Bottom sheet okay button is  displayed") if okay_btn.is_displayed() else ReturnType(
                False,
                "Bottom sheet okay button is  displayed")

    def network_btn_retry(self, verify=False):
        retry = 2
        rty_btn = self.get_element(*self.sd_retry_btn)
        if not verify:
            while retry:
                try:
                    rty_btn = self.get_element(*self.sd_retry_btn)
                    rty_btn.click()
                except (NoSuchElementException, StaleElementReferenceException):
                    retry -= 1
                    sleep(1)
        else:
            return rty_btn.is_displayed()

    def is_session_details_displayed(self):
        try:
            self.get_element(*self.sd_content_details)
            return ReturnType(True, "Session Details are being displayed")
        except NoSuchElementException:
            return ReturnType(False, "Session Details are not being displayed")

    def click_on_button(self, button=None):
        if button.lower() == 'okay':
            self.bottom_sheet_okay_btn()
        elif button.lower() == 'join':
            self.session_join_now()
        elif button.lower() == 'retry':
            self.network_btn_retry()

    def is_completed_sessions_displayed(self):
        self.login.implicit_wait_for(20)
        try:
            displayed = self.get_element(*self.pr_view).is_displayed()
            return ReturnType(True, "Session is completed ") if displayed else ReturnType(False,
                                                                                          "Session is not completed ")
        except NoSuchElementException:
            return ReturnType(False, "Session is not completed ")

    def is_completed_check_displayed(self):
        try:
            return ReturnType(True, "completed check is displayed") if self.get_element(
                *self.pr_status_ico).is_displayed() else ReturnType(False, "completed check is displayed")
        except NoSuchElementException:
            return ReturnType(False, "completed check is displayed")

    def is_screen_displayed(self, title=None):
        timeout = 2
        self.login.implicit_wait_for(0)
        while timeout:
            toolbar_titles = self.get_elements(*self.toolbar_title)
            for toolbar_title in toolbar_titles:
                try:
                    if toolbar_title.text == title and self.device_type != 'tab':
                        return ReturnType(True, "{} screen is displayed".format(title))
                    elif self.device_type != 'mobile':
                        self.get_element(*self.session_details, wait=False)
                        return ReturnType(True, "{} screen is displayed".format(title))
                except (NoSuchElementException, StaleElementReferenceException):
                    timeout -= 1
                    sleep(1)
            else:
                timeout -= 1
                sleep(1)
        return ReturnType(False, "{} screen is not displayed".format(title))

    def click_app_back_btn(self):
        self.get_element(*self.nav_btn).click()

    def tap_on_req_grp(self, req_typ=None):
        self.login.implicit_wait_for(30)
        req_parent = self.get_element(*self.sd_pre_req_list)
        if req_parent is None:
            raise AttachmentError('no requisites available in the current screen')
        if req_typ == 'assessment':
            req_parent.find_element(By.ID, self.sd_req_assess[-1]).click()
        elif req_typ == 'video':
            req_parent.find_element(By.ID, self.sd_req_video_play[-1]).click()

    def is_completed_sessions_sorted(self):
        cards = self.get_elements(*self.card_root)
        recent = self.get_element(*self.pr_status_date).text
        end = self.get_element(*self.card_list)
        start = cards[-1]
        self.scroll_cards.scroll_by_card(start, end)
        old = self.get_element(*self.pr_status_date).text
        ld, lm = recent.split()
        pd, pm = old.split()
        lm, pm = strptime(lm, '%b').tm_mon, strptime(pm, '%b').tm_mon
        if lm == pm:
            if ld > pd:
                return ReturnType(True, "Completed session is sorted")
        elif lm > pm:
            return ReturnType(True, "Completed session is sorted")
        return ReturnType(False, "Completed session is not sorted")

    def click_back_button(self):
        random.choice((self.click_back(), self.click_app_back_btn()))

    def is_premium_school_homepage_displayed(self):
        user_home_activity = 'UserHomeActivity'
        home_activity = 'HomeActivity'
        current_activity = self.driver.current_activity
        self.wait_activity(home_activity, 15)
        if user_home_activity in current_activity:
            self.click_app_back_btn()
        return ReturnType(True,
                          "Premium scholl homepage is displayed") if home_activity in self.driver.current_activity else ReturnType(
            False, "Premium scholl homepage is not displayed")

    def is_all_sessions_displayed(self):
        session_list = self.get_element(*self.card_list)
        sessions = session_list.find_elements_by_class_name('android.view.ViewGroup')
        days = [_.strftime("%d %b") for _ in self.get_working_days(7)]
        self.login.implicit_wait_for(0)
        swipe_to = 5
        scroll_down = True
        while swipe_to:
            end = self.get_element(*self.card_list)
            session = None
            for session in sessions:
                try:
                    _d = session.find_element_by_id(self.card_time_desc[-1]).text
                    if days[-1] in _d:
                        return ReturnType(True, "All sessions are displayed")
                except NoSuchElementException:
                    pass
            if scroll_down:
                self.scroll_cards.scroll_by_card(session, end)
            try:
                see_more_less = self.get_element(*self.see_more_tv)
                if see_more_less.text.lower() != 'see less':
                    see_more_less.click()
                    scroll_down = False
            except NoSuchElementException:
                self.scroll_cards.scroll_by_card(session, end)
            sessions = self.get_elements(*self.card_root)
            swipe_to -= 1
        return ReturnType(False, "All sessions are not displayed")

    def is_up_next_displayed(self):
        swipe = 3
        while swipe:
            try:
                session = self.get_element(*self.card_root)
                session_list = self.get_element(*self.card_list)
                self.scroll_to_element("Up next")
                if session.find_element('id', self.pr_status_msg[-1]).text.lower() == "completed":
                    self.scroll_cards.scroll_by_card(session, session_list)
                    swipe -= 1
            except NoSuchElementException:
                return ReturnType(True, "Up next is being displayed")
        else:
            return ReturnType(False, "Up next is not being displayed")

    def is_post_requisite_attached(self):
        s = self.get_element(*self.pr_status_msg).text
        if s.lower() == 'completed':
            try:
                h = self.get_element(*self.pr_heading).text
                if h.lower() == 'revision material':
                    return ReturnType(True, "Post Requisite is attacthed checked revision material")
                return ReturnType(False,
                                  "Either Post Requisite is not attacthed checked or revision material not shown")
            except NoSuchElementException:
                return ReturnType(False, "Post requisite not found")

    def is_rate_now_card_displayed(self):
        try:
            t = self.get_element(*self.card_strip_btn).text
            if t.lower() == 'rate now':
                return ReturnType(True, "Rate card is displayed")
            return ReturnType(False, "Rate card is not displayed")
        except NoSuchElementException:
            raise SessionNotCompletedError("'Rate Now' button is not displayed")

    def is_rated_count_displayed(self):
        try:
            return ReturnType(self.get_element(*self.pr_star_rating).is_displayed(), "Rated count is displayed")
        except NoSuchElementException:
            return ReturnType(False, "Rated count is not  displayed")

    def is_pr_details_displayed(self):
        try:
            self.get_element(*self.pr_status_msg)
            self.get_element(*self.pr_status_date)
            self.get_element(*self.card_subject_name)
            return ReturnType(True, "Pr details are shown")
        except NoSuchElementException:
            return ReturnType(False, "Pr details are shown")

    def is_pre_post_requisite_displayed(self, pre=False, post=False, session='completed'):
        r = self.get_element(*self.card_root)
        if session == 'completed':
            r.find_element_by_id(self.pr_status_ico[-1]).click()
        elif session == 'upcoming':
            self.select_up_coming_card()
        revision_text = 'Revision Material'
        post_title_text = 'Prepare for the Session'
        self.login.implicit_wait_for(0)
        try:
            a, b = pre, post
            if pre:
                a = self.get_element(
                    'android_uiautomator',
                    'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                    f'scrollTextIntoView("{post_title_text}")'
                ).is_displayed()
            if post:
                b = self.get_element(
                    'android_uiautomator',
                    'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                    f'scrollTextIntoView("{revision_text}")'
                ).is_displayed()
            elif pre is False and post is False:
                raise TypeError(
                    "is_pre_post_requisite_displayed() expected at least one argument to be 'True': 'pre' or 'post'"
                ) from None
            flag = a is pre and b is post
            return ReturnType(True, "Pre/post requisite is displayed") if flag else ReturnType(False,
                                                                                               "Pre/post requisite is not displayed")
        except NoSuchElementException:
            return ReturnType(False, "Pre/post requisite is not displayed")

    def click_on_see_more(self):
        self.get_element(*self.see_more).click()

    def get_req_sessions(self):
        self.login.implicit_wait_for(2.5)
        try:
            req = self.get_element(*self.sd_pre_req_list, wait=False).find_elements(*self.linear_layout)
        except NoSuchElementException:
            req = self.get_element(*self.sd_post_req_list, wait=False).find_elements(*self.linear_layout)
        self.login.implicit_wait_for(15)
        return req

    def is_see_more_option_displayed(self):
        req = self.get_elements(*self.requisite_card)
        see_more = self.get_element(*self.see_more)
        if see_more.is_displayed() and len(req) == 2:
            see_more.click()
            req = self.get_req_sessions()
            self.scroll_cards.scroll_by_card(req[-1], req[0])
            req = self.get_req_sessions()
            if len(req) > 2:
                self.click_app_back_btn()
                return ReturnType(True," see more option is displayed")
        return ReturnType(False,"see more option is not being displayed")

    def scroll_up_next_top(self):
        start = self.get_element(*self.card_up_next)
        end = self.get_element(*self.card_list)
        self.scroll_cards.scroll_by_card(start, end)

    def select_up_coming_card(self):
        self.login.implicit_wait_for(0)
        swipe = 3
        while swipe:
            session_cards = self.get_elements(*self.card_content)
            session_list = self.get_element(*self.card_list)
            for session in session_cards:
                try:
                    try:
                        session.find_element_by_id(self.pr_status_date[-1])
                    except NoSuchElementException:
                        session.find_element_by_id(self.pre_req_time[-1])
                except NoSuchElementException:
                    try:
                        session.find_element_by_id(self.card_time_desc[-1])
                    except NoSuchElementException:
                        continue
                try:
                    card = session.find_element_by_id(self.card_content_header[-1])
                except NoSuchElementException:
                    card = session
                try:
                    card.find_element_by_id(self.pr_status_msg[-1])
                except NoSuchElementException:
                    card.click()
                    return
            self.scroll_cards.scroll_by_card(session_cards[-1], session_list)
            swipe -= 1
        else:
            raise SessionNotFoundError("'UP NEXT' session might not be displayed.")

    def last_completed_session_up_next(self, completed=None):
        self.click_back()
        self.staging.otm_home_screen()
        check = 1
        self.wait_for_locator(*self.card_list)
        session_list = self.get_element(*self.card_list)
        session = None
        if completed == 'today':
            lst_cmp_ssn_dt = time.strftime("%d %b")
        else:
            try:
                self.get_element(*self.pr_status_msg)
                lst_cmp_ssn_dt = self.get_element(*self.pr_status_date).text
            except NoSuchElementException:
                self.ps_home_page_tab(tab_name='Completed')
                self.wait_for_locator(*self.pr_status_msg)
                self.get_element(*self.pr_status_msg)
                lst_cmp_ssn_dt = self.get_element(*self.pr_status_date).text
                self.ps_home_page_tab(tab_name='For you')
        while check:
            session_cards = session_list.find_elements_by_class_name('android.view.ViewGroup')
            for session in session_cards:
                try:
                    session.find_element_by_id(self.pr_status_ico[-1])
                    self.login.implicit_wait_for(0)
                    continue
                except NoSuchElementException:
                    pass
                try:
                    up_nxt_ssn_dt = session.find_element_by_id(self.pre_req_time[-1]).text
                    return lst_cmp_ssn_dt, up_nxt_ssn_dt
                except NoSuchElementException:
                    try:
                        up_nxt_ssn_dt = session.find_element_by_id(self.card_time_desc[-1]).text
                        return lst_cmp_ssn_dt, up_nxt_ssn_dt
                    except NoSuchElementException:
                        pass
            self.scroll_cards.scroll_by_card(start_element=session, end_element=session_list)
            check -= 1
        raise SessionNotCompletedError('no completed sessions available in the current screen')

    def get_join_now_session(self):
        up_next_sessions = list()
        session_list = self.get_element(*self.card_list)
        session_cards = session_list.find_elements_by_class_name('android.view.ViewGroup')
        self.login.implicit_wait_for(0)
        for session in session_cards:
            try:
                if session.find_element_by_id(self.card_strip_btn[-1]).text.lower() == 'join now':
                    up_next_sessions.append(session)
            except NoSuchElementException:
                pass
        if not up_next_sessions:
            raise NoSuchElementException("'Join Now' button could not be located on the page using given search "
                                         "parameters.")
        self.login.implicit_wait_for(15)
        return up_next_sessions

    def get_completed_last_session(self):
        self.ps_home_page_tab('completed')
        last_session_element = self.get_element(*self.card_root)
        session_completed_date = last_session_element.find_element_by_id(self.pr_status_date[-1]).text
        today = datetime.now().strftime("%d %b")
        try:
            time.strptime(session_completed_date, "%d %b")
        except ValueError:
            raise DateError("completed session date format has been changed.") from None
        if session_completed_date == today:
            return last_session_element
        else:
            raise DateError("completed session date is not today's date")

    # todo: change implementation
    def join_session(self, rate_action='skip', session_type='regular'):
        retry = 2
        session_reset_status = False
        self.login.implicit_wait_for(15)
        _session = None
        while retry:
            try:
                sessions = self.get_join_now_session()
                self.login.implicit_wait_for(0)
                card_topic_name = None
                for session in sessions:
                    try:
                        session_label = session.find_element_by_id(self.card_label_tv[-1]).text.lower()
                    except NoSuchElementException:
                        session_label = None
                    if session_label == 'workshop' and session_type == 'regular':
                        self.staging.end_ongoing_session(
                            topic_name=session.find_element_by_id(self.card_topic_name[-1]).text, rate_action='rate')
                    elif session_label == 'workshop' and session_type == 'masterclass':
                        try:
                            _session = session.find_element_by_id(self.card_strip_btn[-1])
                            card_topic_name = session.find_element_by_id(self.card_topic_name[-1]).text
                        except NoSuchElementException:
                            pass
                    else:
                        try:
                            _session = session.find_element_by_id(self.card_strip_btn[-1])
                            card_topic_name = session.find_element_by_id(self.card_topic_name[-1]).text
                        except NoSuchElementException:
                            pass
                _session.click()
                return card_topic_name
            except NoSuchElementException:
                if not session_reset_status:
                    completed_session = self.get_completed_last_session()
                    try:
                        session_topic_name = completed_session.find_element_by_id(
                            self.card_topic_name[-1]).text
                    except NoSuchElementException:
                        session_topic_name = completed_session.find_element_by_id(
                            self.card_topic_name_pr[-1]).text
                    if rate_action == 'skip':
                        self.staging.reset_session_one_to_mega(completed='today', topic_name=session_topic_name)
                        session_reset_status = True
                    elif rate_action == 'rate':
                        self.staging.reset_session_one_to_mega(
                            completed='today', user_profile='user_2', topic_name=session_topic_name)
                        session_reset_status = True
                retry -= 1

    def complete_last_session(self, rate_action="skip", rate_activity_check=False, db=None, profile='login_details_3',
                              sub_profile='profile_1', user_profile='user_1', relaunch=False):
        # if rate_action == 'rate':
        #     user_profile = 'user_2'
        # else:
        #     user_profile = 'user_1'
        self.login.set_user_profile(user_profile=user_profile)  # .verify_home_screen() TODO
        self.staging.session_relaunch()
        self.staging.attach_session_video(grade="8", profile=profile, user_profile=user_profile,
                                          sub_profile=sub_profile)
        self.login.click_on_premium_school(relaunch=relaunch)
        if not self.rate_session():
            join_session_topic_name = self.join_session(rate_action=rate_action)
            db.topic_name = join_session_topic_name
            session = 'today',
            self.staging.end_ongoing_session(rate_action=rate_action, user_profile=user_profile,
                                             sub_profile=sub_profile, topic_name=join_session_topic_name)
            self.login.implicit_wait_for(0)
            self.get_element(*self.bottom_sheet_submit_btn).click()
            if rate_activity_check:
                check.equal(self.wait_activity('RatingActivity'), True, "Not in rate activity")
        self.session_rating(action=rate_action)
        return True

    def session_rating(self, action="skip"):
        rating_activity = "RatingActivity"
        if action == "skip":
            if self.wait_activity(rating_activity, 5):
                self.click_app_back_btn()
                try:
                    if self.get_element(*self.toolbar_title).text.lower() == 'session details':
                        self.click_app_back_btn()
                except NoSuchElementException:
                    pass
        elif action == 'rate':
            try:
                rate_or_join = self.get_element(*self.card_strip_btn)
                if rate_or_join.text == 'Rate Now':
                    rate_or_join.click()
                else:
                    raise Exception()
            except NoSuchElementException:
                pass
            if self.wait_activity(rating_activity, 15):
                rating_bar = self.get_element("id","com.byjus.thelearningapp.premium:id/ratingBarInitial")
                bar_location = rating_bar.location
                bar_size = rating_bar.size
                start_x, start_y = bar_location['x'], bar_location['y'] + bar_size['height'] // 2
                end_x, end_y = start_x + bar_size['width'], start_y
                self.action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).wait(2500).release().perform()
                self.get_element(*self.rating_btn_submit).click()

    def rate_session(self, session='today'):
        self.login.implicit_wait_for(5)
        cst = None
        last_completed = time.strftime("%d %b")
        self.wait_for_locator(*self.card_list)
        session_list = self.get_element(*self.card_list)
        session_cards = session_list.find_elements_by_class_name('android.view.ViewGroup')
        self.login.implicit_wait_for(0)
        for session in session_cards:
            try:
                cst = session.find_element_by_id(self.pr_status_date[-1]).text
                break
            except NoSuchElementException:
                try:
                    cst = session.find_element_by_id(self.card_time_desc[-1]).text
                    break
                except NoSuchElementException:
                    return False
        if cst == last_completed:
            try:
                if session.find_element_by_id(self.card_strip_btn[-1]).text == "Rate Now":
                    return True
            except NoSuchElementException:
                return False

    def is_completed_first_card(self):
        session_card = self.get_elements(*self.card_root)[0]
        status_msg = session_card.find_element_by_id(self.pr_status_msg[-1]).text
        if status_msg.lower() == 'completed':
            return ReturnType(True, "First card is sompleted")
        return ReturnType(False, "First card is not completed")

    def is_all_post_requisite_accessible(self, session_status='completed'):
        count = 0
        if session_status.lower() == 'completed':
            session_card = self.get_elements(*self.card_root)[0]
            status_msg = session_card.find_element_by_id(self.pr_status_msg[-1]).text
            if status_msg.lower() == 'completed':
                x = session_card.location['x'] + session_card.size['width'] // 2
                y = session_card.location['y'] + 0.25 * session_card.size['height'] // 2
                self.action.tap(x=x, y=y).perform()
                self.session_requisite.get_requisites_attached()
                all_requisites = self.session_requisite.get_requisites_attached()
                all_titles = [
                    requisite.find_element(By.XPATH, '//*[@resource-id="%s"]' % self.sd_req_typ_title[-1])
                    for requisite in all_requisites
                ]
                for index, _ in enumerate(all_titles):
                    try:
                        ttv = all_titles[index].text
                    except StaleElementReferenceException:
                        all_requisites = self.session_requisite.get_requisites_attached()
                        all_titles = [
                            requisite.find_element(By.XPATH, '//*[@resource-id="%s"]' % self.sd_req_typ_title[-1])
                            for requisite in all_requisites
                        ]
                        ttv = all_titles[index].text
                    all_titles[index].click()
                    if "video" in ttv.lower():
                        if "k3" in ttv.lower():
                            self.wait_activity('DrmVideoActivity')
                        else:
                            self.wait_activity('VideoDialogActivity')
                        self.get_element(*self.session_requisite.video_close_iv).click()
                    elif "journey" in ttv.lower():
                        self.wait_activity('LearnJourneyActivity')
                        self.click_app_back_btn()
                    elif "assessment" in ttv.lower():
                        self.wait_activity('WorksheetTestInstructionActivity')
                        self.click_back()
                    if not self.wait_activity('OneToMegaHomeActivity', timeout=5):
                        self.click_back()
                    count += 1
                if count == len(all_titles):
                    return True
                return False
        else:
            NotImplementedError()

    def is_live_chat_loaded(self):
        live_chat_activity = 'LiveChatActivity'
        self.get_elements(*self.get_help_btn)[-1].click()
        if self.wait_activity(live_chat_activity):
            return ReturnType(True, " Live chat is loaded")
        return ReturnType(False, " Live chat is  not loaded")

    def complete_assessment(self):
        retry = 3
        self.verify_and_start_assessment()
        if self.wait_activity('WorksheetTestInstructionActivity', 10):
            self.get_element(*self.instruction_start_btn).click()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.get_element(By.CSS_SELECTOR, '#begin-assessment').click()
            self.get_element(By.CSS_SELECTOR, '#exit-assessment').click()
            self.driver.switch_to.alert.accept()
        elif self.wait_activity('HighlightsActivity'):
            self.get_element(*self.assessment_retake).click()
        check.equal(self.wait_activity('TestStartActivity'), True, "test start page not displayed")
        self.get_element(*self.assessment_start).click()
        self.get_element(*self.assessment_submit_btn).click()
        check.equal(self.get_element(*self.bottom_sheet_lyt).is_displayed(), True,
                    "Bottom Sheet is not being displayed")
        self.get_element(*self.bottom_sheet_submit_btn).click()
        check.equal(self.wait_activity('HighlightsActivity'), True, "Highlight page not shown")
        while retry:
            if not self.wait_activity('OneToMegaHomeActivity', timeout=5):
                self.click_back()
            retry -= 1
        return ReturnType(True, "Session completed successfully")

    def verify_and_start_assessment(self):
        self.get_element(
            'android_uiautomator',
            'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
            f'scrollIntoView(resourceId("{self.sd_pre_req_header[-1]}"))'
        )
        self.session_requisite.get_requisites_attached()
        all_requisites = self.session_requisite.get_requisites_attached()
        all_titles = [
            requisite.find_element(By.XPATH, '//*[@resource-id="%s"]' % self.sd_req_typ_title[-1]).text
            for requisite in all_requisites
        ]
        for ttv in all_titles:
            if "assessment" in ttv.lower():
                self.get_element('id', 'com.byjus.thelearningapp.premium:id/tvTitle').click()
                return ReturnType(True, "Assessment verified and started")
        return ReturnType(False, "Assessment verified and started")

    def refresh(self):
        user_home_activity = "UserHomeActivity"
        otm_home_activity = "OneToMegaHomeActivity"
        home_activity = "HomeActivity"
        timeout = 3
        for _ in range(4):
            self.click_back()
            if self.wait_activity(user_home_activity, timeout):
                self.get_element(*self.btn_premium).click()
                break
            elif self.wait_activity(otm_home_activity, timeout):
                timeout = 2
            elif self.wait_activity(home_activity, timeout):
                element = self.get_element(
                    'android_uiautomator',
                    'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                    'scrollIntoView(resourceId("com.byjus.thelearningapp.premium:id/marketing_classes_dynamic_image"))')
                element.click()
                break
            else:
                self.driver.launch_app()
                element = self.get_element(
                    'android_uiautomator',
                    'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                    'scrollIntoView(resourceId("com.byjus.thelearningapp.premium:id/marketing_classes_dynamic_image"))')
                element.click()
                if self.wait_activity(user_home_activity, timeout):
                    self.get_element(*self.btn_premium).click()
                break

    def is_completed_session_displayed(self):
        card_root = self.get_element(*self.card_root)
        try:
            card_root.find_element_by_id(self.pr_status_msg[-1])
            return ReturnType(True, "Completed session is displayed")
        except NoSuchElementException:
            return ReturnType(False, "Completed session is displayed")
