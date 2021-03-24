import random
from time import sleep, strftime, strptime
from typing import List
import re
from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from _pytest.main import NoMatch
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

from pages.base.session_requisite import SessionRequisiteBase
from utilities.exceptions import SessionNotFoundError
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.login_android import LoginAndroid
from pages.android.scroll_cards import ScrollCards


class SessionRequisite(SessionRequisiteBase, TutorCommonMethods):
    def __init__(self, driver):
        self.driver = driver
        self.login = LoginAndroid(driver)
        self.scroll_cards = ScrollCards(driver)
        self.device_type = self.get_device_type()
        self.action = TouchAction(driver)
        self.action_1 = TouchAction(driver)
        self.multi_action = MultiAction(self.driver)
        super().__init__(driver)
        self.__init_locators(self.device_type)

    def __init_locators(self, device_type=None):
        package_name = self.driver.desired_capabilities['appPackage'] + ':id'
        self.card_list = 'id', '%s/sessions_list' % package_name
        self.card_up_next = 'id', '%s/up_next_badge' % package_name
        self.card_subject_ico = 'id', '%s/subject_icon' % package_name
        self.card_subject_name = 'id', '%s/subject_name' % package_name
        self.card_topic_name = 'id', '%s/session_title' % package_name
        self.card_topic_name_pr = 'id', '%s/topic_name' % package_name
        self.card_time_desc = 'id', '%s/session_time' % package_name
        self.arrow_btn = 'id', '%s/arrow_btn' % package_name
        self.requisite_title = 'id', '%s/tvRequisiteTitle' % package_name
        self.pr_view = 'id', '%s/post_requisite_view' % package_name
        self.pre_req_time = 'id', '%s/pre_requisite_time' % package_name
        self.pr_heading = 'id', '%s/requisite_item_heading' % package_name
        self.pr_status_ico = 'id', '%s/post_requisite_status_icon' % package_name
        self.pr_status_msg = 'id', '%s/post_requisite_status' % package_name
        self.pr_status_date = 'id', '%s/post_requisite_date' % package_name
        self.pr_star_ico = 'id', '%s/post_requisite_star_icon' % package_name
        self.pr_star_rating = 'id', '%s/post_requisite_rating' % package_name

        self.see_more_tv = 'id', '%s/see_more_tv' % package_name
        self.requisite_card = 'id', '%s/llRequisiteContentLyt' % package_name
        self.linear_layout = 'class name', 'android.widget.LinearLayout'
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
        self.sd_req_next_arrow = 'id', '%s/ivNext' % package_name
        self.sd_req_video_thumbnail = 'id', '%s/ivVideoThumbnail' % package_name
        self.sd_req_video_play = 'id', '%s/ivVideoPlay' % package_name
        self.sd_action_lyt_title = 'id', '%s/tvActionTitle' % package_name
        self.sd_action_lyt_desc = 'id', '%s/tvActionDescription' % package_name
        self.sd_action_lyt_btn = 'id', '%s/btnAction' % package_name
        self.sd_action_lyt_info_ico = 'id', '%s/infoImageLayout' % package_name
        self.sd_action_lyt_info_msg = 'id', '%s/tvActionInfo' % package_name
        self.sd_retry_btn = 'id', '%s/btnRetry' % package_name
        self.sd_content_details = 'id', '%s/sessionDetailScrollView' % package_name
        self.nav_btn = 'id', '%s/roundedNavButton' % package_name
        self.video_play_ib = 'id', '%s/exo_play' % package_name
        self.video_pause_ib = 'id', '%s/exo_pause' % package_name
        self.video_rewind_iv = 'id', '%s/exo_rew' % package_name
        self.video_forward_iv = 'id', '%s/exo_ffwd' % package_name
        self.video_start_time_tv = 'id', '%s/exo_position' % package_name
        self.video_end_time_tv = 'id', '%s/exo_duration' % package_name
        self.video_seek_bar = 'id', '%s/exo_progress' % package_name
        self.video_buffer = 'id', '%s/exo_buffering' % package_name
        self.video_quality_ib = 'id', '%s/video_quality_selection' % package_name
        self.video_play_speed_tv = 'id', '%s/playback_speed' % package_name
        self.audio_track_ib = 'id', '%s/audio_tracks' % package_name
        self.video_close_iv = 'id', '%s/imgCloseVideo' % package_name
        self.video_orientation_ib = 'id', '%s/orientation_toggle' % package_name
        self.video_frame_lyt = 'id', '%s/exo_content_frame' % package_name
        if device_type != 'tab':
            self.toolbar_title = 'id', '%s/toolbar_title' % package_name
            self.home_page_tab = 'id', '%s/premium_school_home_tabs' % package_name
            self.card_root = 'id', '%s/card' % package_name
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
            self.card_strip_btn = 'id', '%s/btnAction' % package_name

    def is_element_displayed(self, desc=None):
        d = '_'.join(desc.split())
        if d == 'forward_icon':
            try:
                return self.get_element(*self.arrow_btn).is_displayed()
            except NoSuchElementException:
                return False

    def verify_requisite_details(self, dtls=None):
        if dtls == 'forward_icons':
            icons = self.get_elements(*self.arrow_btn)
            if len(icons) == 2:
                return True
            else:
                return False
        else:
            requisites_title = self.get_elements(*self.requisite_title)
            for req_title in requisites_title:
                if dtls in req_title.text.lower():
                    return True

    def click_app_back_btn(self):
        self.get_element(*self.nav_btn).click()

    def get_req_sessions(self) -> List[WebElement]:
        self.login.implicit_wait_for(2.5)
        try:
            req = self.get_element(*self.sd_post_req_list, wait=False).find_elements(
                By.XPATH, '*/' + self.linear_layout[-1])
        except NoSuchElementException:
            req = self.get_element(*self.sd_pre_req_list, wait=False).find_elements(
                By.XPATH, '*/' + self.linear_layout[-1])
        self.login.implicit_wait_for(15)
        return req

    def verify_subject_details(self):
        try:
            subj = self.get_element(*self.sd_subject_name, wait=False).is_displayed()
        except NoSuchElementException:
            subj = self.get_element(*self.card_subject_name, wait=False).is_displayed()
        return subj

    def verify_topic_details(self, details=False):
        try:
            topic = self.get_element(*self.sd_topic_name, wait=False).is_displayed()
        except NoSuchElementException:
            try:
                topic = self.get_element(*self.card_topic_name, wait=False).is_displayed()
            except NoSuchElementException:
                topic = self.get_element(*self.card_topic_name_pr, wait=False).is_displayed()
        if details:
            ele = self.get_element(
                'android_uiautomator',
                'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                f'scrollIntoView(resourceId("{self.sd_topic_desc[-1]}"))'
            )
            desc = ele.is_displayed()
            return desc
        return topic

    @staticmethod
    def verify_calendar_details(dtls, date_month=False):
        if not date_month:
            details_match = re.findall(r'(?:\d{2}\D{0,3}\s\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec),\s'
                                       r'(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday))|Tomorrow'
                                       r'|Today, \d{1,2}:\d{2}\s(?i:AM|PM)',
                                       dtls)
        else:
            details_match = re.findall(r'(?:\d{2}\D{0,3}\s\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))', dtls)
        if details_match:
            return True
        return False

    @staticmethod
    def verify_time_details(dtls):
        details_match = re.findall(r'\d{1,2}:\d{2}\s(?i:AM|PM)', dtls)
        if details_match:
            return True
        return False

    def is_subject_icon_displayed(self):
        self.login.implicit_wait_for(0)
        try:
            subj_ico = self.get_element(*self.card_subject_ico, wait=False)
            return subj_ico.is_displayed()
        except NoSuchElementException:
            try:
                if self.get_element(*self.pre_req_time, wait=False).is_displayed():
                    return True
                else:
                    return False
            except NoSuchElementException:
                try:
                    if self.get_element(*self.pr_view, wait=False).is_displayed():
                        return True
                    else:
                        return False
                except Exception as exec_content:
                    raise exec_content from None

    def is_cards_loaded(self):
        nxt = 4
        self.login.implicit_wait_for(2.5)
        while nxt:
            try:
                self.get_element(*self.card_root, wait=False)
                return True
            except NoSuchElementException:
                nxt -= 1
        if not nxt:
            raise Exception('no future sessions available')

    def verify_content_description(self, section=None, e_type=None):
        self.is_cards_loaded()
        self.login.implicit_wait_for(0)
        section = section.lower()
        if e_type is not None:
            e_type = e_type.lower()
        if section == 'subject':
            if e_type == 'name':
                return self.verify_subject_details()
            elif e_type == 'icon':
                subj_ico = self.is_subject_icon_displayed()
                return subj_ico
        elif section == 'topic':
            if e_type == 'name':
                return self.verify_topic_details()
            elif e_type == 'description':
                return self.verify_topic_details(True)
        elif section == 'calendar':
            date = self.get_element(*self.sd_date_desc, wait=False).text
            ico = self.get_element(*self.sd_calendar_ico, wait=False).is_displayed()
            return ico and self.verify_calendar_details(date)
        elif section == 'clock':
            time_dtls = self.get_element(*self.sd_time_desc, wait=False).text
            ico = self.get_element(*self.sd_clock_ico, wait=False).is_displayed()
            return ico and self.verify_time_details(time_dtls)
        elif section == 'time':
            try:
                time_dtls = self.get_element(*self.sd_time_desc, wait=False).text
            except NoSuchElementException:
                time_dtls = self.get_element(*self.card_time_desc, wait=False).text
            return self.verify_time_details(time_dtls)
        elif section == 'date':
            try:
                dtls = self.get_element(*self.pr_status_date, wait=False).text
                return self.verify_calendar_details(dtls, True)
            except NoSuchElementException:
                try:
                    dtls = self.get_element(*self.pre_req_time, wait=False).text
                    return self.verify_calendar_details(dtls)
                except NoSuchElementException:
                    dtls = self.get_element(*self.card_time_desc, wait=False).text
                    return self.verify_calendar_details(dtls)

    def get_requisites_attached(self):
        req = self.get_req_sessions()
        if not len(req) < 2:
            self.scroll_cards.scroll_by_card(req[1], req[0])
        req = self.get_req_sessions()
        return req

    def is_see_more_option_displayed(self):
        self.login.implicit_wait_for(15)
        req = self.get_elements(*self.requisite_card)
        try:
            see_more = self.get_element(*self.see_more_tv, wait=False)
        except NoSuchElementException:
            return False
        if see_more.is_displayed() and len(req) >= 2:
            see_more.click()
            return self.is_all_requisites_attached()
        return False

    def is_all_requisites_attached(self):
        self.get_requisites_attached()
        req = self.get_requisites_attached()
        if len(req) > 2:
            self.click_app_back_btn()
            return True

    def ps_home_page_tab(self, tab_name="For you", check=False):
        action_bar_tab = self.get_element(*self.home_page_tab)
        tabs_view = action_bar_tab.find_elements_by_class_name('android.widget.TextView')
        for tab_view in tabs_view:
            if tab_view.text == tab_name:
                if not check and not tab_view.is_selected():
                    tab_view.click()
                    return tab_view.is_selected()
                elif check:
                    return tab_view.is_selected()
        return False

    def scroll_up_next_top(self):
        start = self.get_element(*self.card_up_next)
        end = self.get_element(*self.card_list)
        self.scroll_cards.scroll_by_card(start, end)

    def get_session(self, session_type='up_next'):
        retry = 3
        self.ps_home_page_tab()
        self.is_cards_loaded()
        self.login.implicit_wait_for(0)
        # self.scroll_up_next_top()
        while retry:
            session_list = self.get_element(*self.card_list)
            session_cards = session_list.find_elements_by_class_name('android.view.ViewGroup')
            for session in session_cards:
                try:
                    if session_type == 'up_next':
                        self.scroll_cards.scroll_by_card(session, session_list)
                        return session
                    elif session_type == 'future':
                        self.scroll_cards.scroll_by_card(session, session_list)
                        return random.choice(session_cards)
                    elif session_type == 'tomorrow':
                        time_now = strftime('%d %m')
                        current_day, current_month = list(map(int, time_now.split()))
                        try:
                            actual_time_raw = session.find_element_by_id(self.pre_req_time[-1]).text
                        except NoSuchElementException:
                            try:
                                actual_time_raw = session.find_element_by_id(self.card_time_desc[-1]).text
                            except NoSuchElementException:
                                actual_time_raw = session.find_element_by_id(self.pr_status_date[-1]).text
                        dt_mn = actual_time_raw.split(",")[0]
                        struct_time = strptime(dt_mn, "%d %b")
                        actual_month, actual_date = struct_time.tm_mon, struct_time.tm_mday
                        if actual_month == current_month:
                            if actual_date == current_day:
                                return session
                        self.scroll_cards.scroll_by_card(session, session_list)
                except NoSuchElementException:
                    pass
                except IndexError:
                    retry -= 1
                    break
        raise SessionNotFoundError('no up coming sessions available')

    def verify_video_playing(self):
        t = 20
        self.login.implicit_wait_for(60)
        self.static_exo_player()
        pm, ps = list(map(int, self.get_element(*self.video_start_time_tv).text.split(":")))
        self.login.implicit_wait_for(4.5)
        retry = False
        while t:
            try:
                sleep(0.5)
                if retry is True:
                    self.static_exo_player()
                cm, cs = list(map(int, self.get_element(*self.video_start_time_tv).text.split(":")))
                if cm > pm or (cm == pm and cs > ps) or cs != 0:
                    return True
                else:
                    self.get_element(*self.video_forward_iv).click()
                    t -= 1
                    sleep(1)
            except (NoSuchElementException, StaleElementReferenceException):
                retry = True
                t -= 1
                sleep(1)

    def is_video_not_buffering(self, t=30):
        self.login.implicit_wait_for(0)
        while t:
            try:
                self.get_element(*self.video_buffer, wait=False).is_displayed()
                t -= 1
                sleep(1)
            except NoSuchElementException:
                return True
        return bool(t)

    def static_exo_player(self):
        self.login.implicit_wait_for(15)
        frame_layout = self.get_element(*self.video_frame_lyt, wait=False)
        lyt_x, lyt_y = frame_layout.location['x'] + 5, int(frame_layout.size['height'] * 0.6)
        self.login.implicit_wait_for(0)
        try:
            self.get_element(*self.video_play_ib, wait=False)
            return
        except NoSuchElementException:
            retry = 15
        while retry:
            try:
                self.action_1.tap(x=lyt_x, y=lyt_y).release().perform()
                self.get_element(*self.video_pause_ib, wait=False).click()
                retry -= retry
            except (NoSuchElementException, StaleElementReferenceException):
                retry -= 1

    def complete_video(self):
        self.driver.implicitly_wait(0)
        t = 30
        if self.is_video_not_buffering():
            while t:
                try:
                    self.static_exo_player()
                    self.get_element(*self.video_seek_bar, wait=False)
                    seek_bar_loc = self.get_element(*self.video_seek_bar, wait=False).location
                    seek_bar_size = self.get_element(*self.video_seek_bar, wait=False).size
                    start_x, start_y = seek_bar_loc['x'], seek_bar_loc['y'] + seek_bar_size['height'] // 2
                    end_x, end_y = start_x + seek_bar_size['width'], start_y
                    sweep_act = self.action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).wait(1000).release()
                    action_2 = TouchAction(self.driver)
                    tap_act = action_2.tap(element=self.get_element(*self.video_play_ib))
                    self.multi_action.add(sweep_act, tap_act)
                    self.multi_action.perform()
                    return True
                except (NoSuchElementException, StaleElementReferenceException):
                    t -= 1
            raise NoSuchElementException
        raise NoMatch

    def change_orientation(self):
        self.static_exo_player()
        self.get_element(*self.video_orientation_ib).click()
        self.get_element(*self.video_play_ib).click()
        return self.verify_video_playing()

    def is_video_landscape_playable(self):
        if self.change_orientation():
            self.click_back()
            return True
        return False

    def verify_video_player_elements(self):
        self.static_exo_player()
        video_elements = [
            self.video_start_time_tv, self.video_end_time_tv, self.video_seek_bar, self.video_quality_ib,
            self.video_play_speed_tv, self.audio_track_ib, self.video_close_iv, self.video_orientation_ib,
            self.video_frame_lyt
        ]
        self.get_element(*self.video_play_ib).click()
        self.static_exo_player()
        self.get_element(*self.video_forward_iv).click()
        self.get_element(*self.video_rewind_iv).click()
        try:
            self.get_element(*self.video_buffer)
        except NoSuchElementException:
            pass
        for vel in video_elements:
            self.get_element(*vel)
        return True

    def verify_session_card_details(self, session=None):
        details = [
            ("subject", "name"),
            ("topic", "name"),
            ("date", None)
        ]
        for dt in details:
            assert self.verify_content_description(*dt)
        if session is None:
            assert self.verify_requisite_details("forward_icons")
            assert self.is_see_more_option_displayed()
        return True

    def future_card(self):
        session = self.get_session('future')
        end = self.get_element(*self.card_list)
        self.scroll_cards.scroll_by_card(start_element=session, end_element=end)

    def verify_pre_requisite_details(self):
        self.get_requisites_attached()
        attachments = self.get_requisites_attached()
        for attachment in attachments:
            if "video" in attachment.find_element(*self.sd_req_typ_title).text.lower():
                assert attachment.find_element(*self.sd_req_video_thumbnail)
            else:
                assert attachment.find_element(*self.sd_req_assess)
            assert attachment.find_element(*self.sd_req_typ_desc)
            assert attachment.find_element(*self.sd_req_next_arrow)
        if attachments:
            return True

    def verify_app_home_screen(self):
        home_activity = "HomeActivity"
        user_home_activity = "UserHomeActivity"
        if self.wait_activity(user_home_activity):
            self.click_back()
        return self.wait_activity(home_activity)
