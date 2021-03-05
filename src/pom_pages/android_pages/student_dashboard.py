import logging
import re
from datetime import datetime, timedelta
from time import strptime
import pytest
from Utilities.tutor_common_methods import TutorCommonMethods
from POM_Pages.Android_pages.session_popup import SessionAlert
from selenium.common.exceptions import NoSuchElementException
from POM_Pages.Android_pages.session_data import SessionData
from POM_Pages.Android_pages.scroll_cards import ScrollCards
from POM_Pages.Android_pages.login_android import Login


class StudentDashboard(TutorCommonMethods):
    def __init__(self, driver):
        self.joinnow = '//*[contains(@resource-id, "actionCardButton")]'
        self.driver = driver
        self.login = Login(driver)
        super().__init__(driver)
        self.session_data = SessionData(driver)
        self.scroll_card = ScrollCards(driver)
        self.session_pop = SessionAlert(driver)
        self.logo_image = '//*[contains(@resource-id, "LogoImage")]'
        self.cls_rom_text = '//*[contains(@resource-id, "headerLayout")]//android.widget.TextView'
        self.session_month_text = '//*[contains(@resource-id, "session_month_header")]'
        self.chapter_name = '//*[contains(@resource-id, "chapterName")]'
        self.avatar_classroom_image = '//*[contains(@resource-id, "AvatarImg")]'
        self.session_details_card = '//*[contains(@resource-id, "title")]//ancestor::android.widget.FrameLayout[contains(@resource-id, "container")]'
        self.dropdown_month_icon = '//*[contains(@resource-id, "spinnerMonth")]'
        self.dropdown_month_list = '//*[contains(@resource-id, "month_item_name_view")]'
        self.session_time_dtls = '//*[contains(@resource-id, "SessionScheduleTime")]'
        self.btn_retry = '//*[contains(@resource-id, "btnRetry")]'
        self.profile_back_button = '//*[contains(@resource-id, "roundedNavButton")]'

    def image_text_verification(self):
        try:
            image_displayed = self.get_element('xpath', self.logo_image).is_displayed()
            if image_displayed:
                return True
            return False
        except NoSuchElementException:
            return None

    def text_verify_classroom(self, expected_text):
        text_elements = self.get_elements('xpath', self.cls_rom_text)
        for element in text_elements:
            if expected_text == element.text:
                return True
        return False

    def text_verify_session_text(self, exp_text):
        session_text = self.get_element('xpath', self.session_month_text).text
        if session_text.text == exp_text:
            return True
        return False

    def is_up_next_card_selected(self):
        self.driver.implicitly_wait(10)
        end = self.get_element('xpath',
                               '//*[contains(@resource-id, "rvScheduleList")]')
        current_month_year = datetime.now().strftime('%B \'%y')
        self.get_element('xpath', self.dropdown_month_icon).click()
        for month_year in self.get_elements('xpath', self.dropdown_month_list):
            if current_month_year == month_year.text:
                month_year.click()
                break
        self.driver.implicitly_wait(0)
        while True:
            all_details = self.get_elements('xpath', self.session_time_dtls)
            try:
                next_label = self.get_element('xpath', '//*[contains(@resource-id, "tv_up_next_label")]')
                break
            except NoSuchElementException:
                print("ALLL card details................", all_details)
                self.scroll_card.scroll_by_card(all_details[-1], end)
        self.driver.implicitly_wait(10)
        previous_chapter_name = self.get_element('xpath', '//*[contains(@resource-id, "chapterName")]').text
        next_label.click()
        try:
            self.session_pop.cancel_join_session()
        except NoSuchElementException:
            pass
        current_chapter_name = self.get_element('xpath', '//*[contains(@resource-id, "chapterName")]').text
        if previous_chapter_name == current_chapter_name:
            return True
        return False

    def check_month_header_format(self, exp_text):
        month_header_text = self.get_element(
            'xpath', '//*[contains(@resource-id, "month_header")]').text
        match_res = re.match(r"Sessions\sin\s[A-Za-z]{3,9}\s'\d{2}", month_header_text)
        if match_res is not None:
            if month_header_text == match_res and exp_text in match_res:
                return True
        return False

    def verify_current_month(self):
        raw_data = datetime.now()
        expected_month = raw_data.strftime("%B \'%y")
        session_month = self.get_element('xpath', "//*[contains(@resource-id, 'month_item_name_view')]").text
        if expected_month == session_month:
            return True
        return False

    def is_profile_avatar_displayed(self):
        try:
            element_state = self.get_element('xpath', self.avatar_classroom_image).is_displayed()
            return element_state
        except NoSuchElementException:
            return False

    def is_attended_cards_displayed(self):
        self.driver.implicitly_wait(0)
        end = self.get_element('xpath',
                               '//*[contains(@resource-id, "rvScheduleList")]')
        while True:
            ac_cards = self.session_data.get_actual_cards_displayed()
            for card in ac_cards:
                response = self.session_data.get_session_status(card)
                if response != "Completed" or response == "UP NEXT":
                    previous_card = ac_cards[0]
                    previous_card_subj = self.session_data.get_session_topic_name(previous_card)
                    previous_card_time = self.session_data.get_session_time_detail(previous_card)
                    self.scroll_card.scroll_by_card(ac_cards[-1], end)
                    current_card = self.session_data.get_actual_cards_displayed()[0]
                    current_card_subj = self.session_data.get_session_topic_name(current_card)
                    current_card_time = self.session_data.get_session_time_detail(current_card)
                    if previous_card_subj == current_card_subj:
                        if previous_card_time == current_card_time:
                            self.driver.implicitly_wait(5)
                            return False
                    break
                elif response != "Not Completed":
                    self.driver.implicitly_wait(5)
                    return True

    def is_attended_cards_not_displayed(self):
        self.driver.implicitly_wait(0)
        end = self.get_element('xpath',
                               '//*[contains(@resource-id, "rvScheduleList")]')
        while True:
            ac_cards = self.session_data.get_actual_cards_displayed()
            for card in ac_cards:
                response = self.session_data.get_session_status(card)
                if response == "Completed" or response == "UP NEXT":
                    previous_card = ac_cards[0]
                    previous_card_subj = self.session_data.get_session_topic_name(previous_card)
                    previous_card_time = self.session_data.get_session_time_detail(previous_card)
                    self.scroll_card.scroll_by_card(ac_cards[-1], end)
                    current_card = self.session_data.get_actual_cards_displayed()[0]
                    current_card_subj = self.session_data.get_session_topic_name(current_card)
                    current_card_time = self.session_data.get_session_time_detail(current_card)
                    if previous_card_subj == current_card_subj:
                        if previous_card_time == current_card_time:
                            self.driver.implicitly_wait(5)
                            return False
                    break
                elif response == "Not Completed":
                    self.driver.implicitly_wait(5)
                    return True

    def is_session_details_card_displayed(self):
        try:
            details_card = self.get_element('xpath', self.session_details_card).is_displayed()
            return details_card
        except NoSuchElementException:
            return False

    def get_diff_of_cards_displayed(self, list_of_details):
        ac_dtls = len(list_of_details)
        ac_cards = len(self.session_data.get_actual_cards_displayed())
        return abs(ac_cards - ac_dtls)

    def is_cards_subjects_icon_displayed(self):
        subjects_icons = self.get_elements('xpath', '//*[contains(@resource-id, "SubjectLogo")]')
        diff = self.get_diff_of_cards_displayed(subjects_icons)
        if diff <= 1:
            return True
        return False

    def is_cards_subjects_name_displayed(self):
        subjects_name = self.get_elements('xpath', '//*[contains(@resource-id, "SubjectName")]')
        diff = self.get_diff_of_cards_displayed(subjects_name)
        if diff <= 1:
            return True
        return False

    def is_cards_topic_name_displayed(self):
        topics_name = self.get_elements('xpath', '//*[contains(@resource-id, "TopicName")]')
        diff = self.get_diff_of_cards_displayed(topics_name)
        if diff <= 1:
            return True
        return False

    def is_cards_schedule_details_displayed(self):
        scheduled_details = self.get_elements('xpath', '//*[contains(@resource-id, "ScheduleTime")]')
        for s_detail in scheduled_details:
            actual_text = re.findall(r'(?:\d{2}\D{0,3}\s\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec),'
                                     r'\s(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),'
                                     r'|Tomorrow|Today)\s\d:\d{2}\s(?:AM|PM)', s_detail.text)
            if actual_text:
                break
            else:
                return False
        return True

    def is_cards_rate_session_displayed(self):
        rate_sessions = self.get_elements('xpath', '//*[contains(@resource-id, "ScheduleTime")]')
        diff = self.get_diff_of_cards_displayed(rate_sessions)
        if diff <= 1:
            return True
        return False

    def verify_is_text_displayed(self, expected_text):
        response = self.get_element('xpath', "//*[contains(@text, '" + expected_text + "')]").is_displayed()
        return response

    def is_subject_name_displayed(self):
        subj_name = self.get_element('xpath', ' //*[contains(@resource-id, "subjectName")]').is_displayed()
        return subj_name

    def is_topic_name_displayed(self):
        tpc_name = self.get_element('xpath', ' //*[contains(@resource-id, "chapterName")]').is_displayed()
        return tpc_name

    def is_calendar_details_displayed(self):
        calndr_icon_displayed = self.get_element('xpath',
                                                 '//*[contains(@resource-id, "DateView")]/android.widget.ImageView').is_displayed()
        calndr_dtls = self.get_element('xpath', '//*[contains(@resource-id, "sessionDatetv")]').text
        details_match = re.findall(r'(?:\d{2}\D{0,3}\s\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec),'
                                   r'\s(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday))|Tomorrow|Today',
                                   calndr_dtls)
        if details_match and calndr_icon_displayed:
            return calndr_icon_displayed
        return False

    def is_time_details_displayed(self):
        time_icon_displayed = self.get_element('xpath',
                                               '//*[contains(@resource-id, "TimeView")]/android.widget.ImageView').is_displayed()
        time_details = self.get_element('xpath', '//*[contains(@resource-id, "sessionTimetv")]').text
        details_match = re.findall(r'\d:\d{2}\s[A-Z]{2}', time_details)
        if time_icon_displayed and details_match:
            return True
        return False

    def is_topic_desc_displayed(self):
        try:
            topic_desc = self.get_element('xpath',
                                          '//*[contains(@resource-id, "sessionDesctv")]').is_displayed()
        except NoSuchElementException:
            return False
        return topic_desc

    @staticmethod
    def get_date_time(days=0):
        current_date_time = (datetime.now() + timedelta(days=days)).strftime('%d %H:%M %m').split()
        return current_date_time

    def select_session_specific(self, ctype='post'):
        end = self.get_element('xpath',
                               '//*[contains(@resource-id, "rvScheduleList")]')
        abs_diff = None
        sessions_available = []
        while True:
            all_details = self.get_elements('xpath', self.session_time_dtls)
            for sch_dtls in all_details:
                date = sch_dtls.text
                if ',' in date:
                    filter_date = date.split(',')
                    date_month = filter_date[0].split()
                    ac_date = date_month[0]
                    ac_month = strptime(date_month[1], "%b").tm_mon
                    ac_date = filter_date[0].split()[0]
                    extracted_time = filter_date[-1].lstrip()
                else:
                    filter_date = date.split()
                    ac_date = filter_date[0].split()[0]
                    extracted_time = filter_date[-2] + " " + filter_date[-1]
                    ac_month = datetime.now().month
                current_time = float('.'.join(self.get_date_time()[1].split(':')))
                if ac_date == 'Today':
                    actual_date = int(self.get_date_time()[0])
                elif ac_date == 'Tomorrow':
                    actual_date = int(self.get_date_time(1)[0])
                current_date_time = datetime.now().strftime('%d %H:%M').split()
                current_time = float('.'.join(current_date_time[1].split(':')))
                if ac_date == 'Today':
                    actual_date = int(current_date_time[0])
                elif ac_date == 'Tomorrow':
                    actual_date = int(current_date_time[0]) + 1
                else:
                    actual_date = int(ac_date)
                formatting_date = datetime.strptime(extracted_time, "%I:%M %p")
                act_time = datetime.strftime(formatting_date, "%H:%M")
                actual_time = float('.'.join(act_time.split(':')))
                current_date = int(self.get_date_time()[0])
                current_month = datetime.now().month

                if ctype == 'post':
                    expected_date = int(self.get_date_time(4)[0])
                    expected_month = int(self.get_date_time(4)[2])
                    abs_diff = abs(actual_date - expected_date)
                    print("="*13+"POST"+"="*13)
                    print("Actual Month %s and Current Month %s and Expected Month %s" %
                          (ac_month, current_month, expected_month))
                    print("Actual Date %s and Expected Date %s" %
                          (actual_date, expected_date))
                    if ac_month == current_month == expected_month:
                        if actual_date > expected_date:
                            return sch_dtls
                    elif expected_month < ac_month:
                        pytest.fail("No session available")
                elif ctype == 'within':
                    expected_month = int(self.get_date_time(4)[2])
                    expected_date = int(self.get_date_time(4)[0])
                    abs_diff = abs(actual_date - expected_date)
                    print("=" * 13 + "WITHIN" + "=" * 13)
                    print("Actual Month %s and Current Month %s and Expected Month %s" %
                          (ac_month, current_month, expected_month))
                    print("Actual Date %s and Expected Date %s" %
                          (actual_date, expected_date))
                    if expected_month == ac_month:
                        if current_month >= ac_month:
                            if actual_date > current_date:
                                return sch_dtls
                elif ctype == 'on':
                    expected_date = int(self.get_date_time()[0])
                    expected_time = actual_time + 17
                    abs_diff = abs(actual_date - expected_date)
                    print("date.............................", actual_date, expected_date)
                    if ac_month == current_month:
                        if actual_date > expected_date and abs_diff == 1:
                            if actual_time <= current_time:
                                print("date.............................1", actual_date, expected_date)
                                sessions_available.append(sch_dtls)
                        elif actual_date == expected_date:
                            if expected_time >= current_time:
                                print("date.............................2", actual_date, expected_date)
                                sessions_available.append(sch_dtls)
                    elif ac_month > current_month:
                        print("False Statement......................")
                        logging.info('No session exists within 24hrs')
                        return sessions_available
            if sessions_available:
                return sessions_available
            print("Scrolling....................................")
            if abs_diff < 4:
                if abs_diff == 0:
                    self.scroll_card.scroll_by_card(all_details[abs_diff + 1], end)
                else:
                    self.scroll_card.scroll_by_card(all_details[abs_diff], end)
            else:
                self.scroll_card.scroll_by_card(all_details[-1], end)

    def is_choose_topic_displayed(self, ctype='post'):
        current_month_year = datetime.now().strftime('%B \'%y')
        self.get_element('xpath', self.dropdown_month_icon).click()
        for month_year in self.get_elements('xpath', self.dropdown_month_list):
            if current_month_year == month_year.text:
                month_year.click()
                break
        self.select_session_specific(ctype).click()
        try:
            state = self.get_element('xpath',
                                     '//*[contains(@resource-id, "actionCardButton")]').is_displayed()
            return state
        except NoSuchElementException:
            return False

    def is_sessions_starts_in_displayed(self, ctype='within'):
        current_month_year = datetime.now().strftime('%B \'%y')
        self.get_element('xpath', self.dropdown_month_icon).click()
        for month_year in self.get_elements('xpath', self.dropdown_month_list):
            if current_month_year == month_year.text:
                month_year.click()
                break
        self.select_session_specific(ctype).click()
        try:
            _text = self.get_element('xpath', '//*[contains(@resource-id, "cardTimertv")]').text
            return _text
        except NoSuchElementException:
            return False

    def is_session_start_timer_displayed(self, ctype='on'):
        current_month_year = datetime.now().strftime('%B \'%y')
        self.get_element('xpath', self.dropdown_month_icon).click()
        for month_year in self.get_elements('xpath', self.dropdown_month_list):
            if current_month_year == month_year.text:
                month_year.click()
                break
        self.select_session_specific(ctype)[0].click()
        self.session_pop.cancel_join_session()
        self.select_session_specific(ctype).click()
        try:
            _text = self.get_element('xpath', '//*[contains(@resource-id, "cardTimertv")]').text

            return _text
        except NoSuchElementException:
            return False

    def random_card(self):
        random_card = self.session_data.get_actual_cards_displayed()[2]
        return random_card

    def is_wifi_relevant_msg_displayed(self, text):
        if 'wrong' in text:
            try:
                msg_state = self.get_element('xpath',
                                             "//*[contains(@resource-id, 'home_reco_test_test_name')]").is_displayed()
                return msg_state
            except NoSuchElementException:
                return False
        try:
            msg_state = self.get_element('xpath', '//*[contains(@resource-id, "tvErrorDescription")]').is_displayed()

            return msg_state
        except NoSuchElementException:
            return False

    def tap_button_retry(self):
        self.driver.implicitly_wait(0)
        while True:
            try:
                self.get_element('xpath', self.btn_retry).click()
            except NoSuchElementException:
                break
        self.driver.implicitly_wait(10)

    def verify_session_details(self):
        previous_card = self.random_card().find_element_by_xpath(
            "//*[contains(@resource-id, 'TopicName')]").text

        displayed_card = self.get_element('xpath', self.chapter_name).text
        if previous_card == displayed_card:
            return True
        return False

    def is_one_to_many_screen_displayed(self):
        try:
            msg = self.get_element('xpath', '//*[contains(@resource-id, "llScheduleList")]').is_displayed()
            return msg
        except NoSuchElementException:
            return False

    def click_on_future_card(self):
        self.is_choose_topic_displayed()

    def is_session_details_text_displayed(self):
        try:
            _txt_b = self.get_element('xpath',
                                      '//*[contains(@resource-id, "titletv")]').text
            if _txt_b == 'SESSION DETAILS':
                return True
            return False
        except NoSuchElementException:
            return None

    def is_choose_topic_card_title_displayed(self):
        try:
            card_title = self.get_element(
                'xpath', '//*[contains(@resource-id, "cardTitletv")]').is_displayed()
            return card_title
        except NoSuchElementException:
            return False

    def is_subtext_of_choose_topic_displayed(self):
        try:
            sub_text = self.get_element(
                'xpath', '//*[contains(@resource-id, "cardSubTitletv")]').text
            if sub_text == 'Learn what you want':
                return True
            return False
        except NoSuchElementException:
            return None

    def is_message_of_session_details_displayed(self):
        try:
            sub_text = self.get_element(
                'xpath', '//*[contains(@resource-id, "messageTv")]').text
            if sub_text == 'You can choose a topic till 4 days prior to the session':
                return True
            return False
        except NoSuchElementException:
            return None

    def tap_on_choose_topic(self):
        self.get_element('xpath',
                         '//*[contains(@resource-id, "actionCardButton")]').click()

    def is_change_topic_section_displayed(self):
        try:
            status_displayed = self.get_element('xpath',
                                                "//*[contains(@resource-id, 'change_topic_title')]/"
                                                "ancestor::android.widget.LinearLayout[contains(@resource-id,"
                                                "'content')]").is_displayed()
            return status_displayed
        except NoSuchElementException:
            return False

    def is_topics_displayed_under_change_topic(self):
        try:
            section_displayed = self.get_element('xpath',
                                                 "//*[contains(@resource-id, 'change_topic_lv')]"
                                                 "//*[contains(@resource-id, 'ChangeTopicTitle')]").is_displayed()
            return section_displayed
        except NoSuchElementException:
            return False

    def is_done_button_displayed(self):
        try:
            button_displayed = self.get_element('xpath',
                                                '//*[contains(@resource-id, "change_topic_done_button")]').is_displayed()
            return button_displayed
        except NoSuchElementException:
            return False

    def is_close_button_displayed(self):
        try:
            button_displayed = self.get_element('xpath',
                                                '//*[contains(@resource-id, "change_topic_close_icon")]').is_displayed()
            return button_displayed
        except NoSuchElementException:
            return False

    def tap_on_any_change_topic(self):
        self.get_element('xpath',
                         "//*[contains(@resource-id, 'change_topic_lv')]"
                         "//*[contains(@resource-id, 'ChangeTopicTitle')]").click()

    def is_radio_button_selected(self):
        try:
            ele = self.get_element('xpath',
                                   "//*[contains(@resource-id, 'change_topic_lv')]")
            button_selected = ele.find_element_by_xpath('//*[contains(@resource-id, '
                                                        '"ivChangeTopicSelectButton")]').is_selected()
            return button_selected
        except NoSuchElementException:
            return False

    def tap_done_button(self):
        self.get_element('xpath',
                         '//*[contains(@resource-id, "change_topic_done_button")]').click()

    def tap_on_close_button(self):
        self.get_element('xpath',
                         '//*[contains(@resource-id, "change_topic_close_icon")]').click()

    def is_session_details_error_image_displayed(self):
        try:
            self.get_element('xpath',
                             '//*[contains(@resource-id, "networkErrorView")]'
                             '//*[contains(@resource-id, "imageView")]').is_displayed()
            return True
        except NoSuchElementException:
            return False

    def is_text_check_connection_displayed(self, text):
        _ele_text = self.get_element('xpath',
                                     '//*[contains(@resource-id, "networkErrorView")]//*[contains(@resource-id, '
                                     '"tvErrorDescription")]').text
        if _ele_text == text:
            return True
        return False

    def is_all_details_displayed_match(self):
        list_of_details = self.get_elements('xpath',
                                            '//*[contains(@resource-id, "container")]//android.widget.TextView')
        count = 0
        for details in list_of_details:
            if details.text == 'SESSION DETAILS':
                count += 1
            elif details.text == 'Choose a topic to learn':
                count += 1
            elif details.text.startswith('You can choose a topic'):
                count += 1
        if count == 3:
            return True
        return False

    def is_timer_displayed(self):
        available_sessions = self.select_session_specific('on')
        schedule_timer_list = []
        self.driver.implicitly_wait(5)
        for available_session in available_sessions:
            schedule_text = available_session.find_element_by_xpath(self.session_time_dtls).text
            schedule_timer_list.append(schedule_text)
            print("text...........", schedule_text)
        for session in schedule_timer_list:
            self.get_element('xpath', '//*[contains(@text, "' + session + '")]').click()
            self.session_pop.cancel_join_session()
            try:
                timer_text = self.get_element('xpath', '//*[contains(@resource-id, "cardTimerDescription")]').text
                if "hours" or "minutes" in timer_text:
                    return True
                return False
            except NoSuchElementException:
                pass
            finally:
                self.driver.implicitly_wait(15)
        self.select_session_specific('on').click()
        try:
            timer_text = self.get_element('xpath', '//*[contains(@resource-id, "cardTimerDescription")]').text
            if "hours" or "minutes" in timer_text:
                return True
            return False
        except NoSuchElementException:
            return None

    def is_date_count_displayed(self):
        self.select_session_specific('within').click()
        try:
            date_text = self.get_element('xpath', '//*[contains(@resource-id, "cardTimerDescription")]').text
            if "day" or "hours" in date_text:
                return True
            return False
        except NoSuchElementException:
            return None

    def is_respective_card_displayed(self):
        self.session_pop.cancel_download_asset()
        self.session_pop.cancel_join_session()
        selected_card = self.random_card()
        topic_name_text = selected_card.find_element_by_xpath('//*[contains(@resource-id, "TopicName")]').text
        date_text = selected_card.find_element_by_xpath('//*[contains(@resource-id, "SessionScheduleTime")]').text
        chapter_name = self.get_element('xpath', '//*[contains(@resource-id, "chapterName")]').text
        date_details = self.get_element('xpath', '//*[contains(@resource-id, "sessionDatetv")]').text
        if chapter_name == topic_name_text and date_details in date_text:
            return True
        return False

    def is_your_session_starts_text_displayed(self):
        self.select_session_specific('within').click()
        try:
            card_text = self.get_element('xpath', '//*[contains(@resource-id, "cardTimertv")]').text
        except NoSuchElementException:
            return None
        expected_text = 'Your session starts in'
        if card_text == expected_text:
            return True
        return False

    def is_you_can_choose_topic_text_not_displayed(self):
        try:
            self.get_element('xpath', '//*[contains(@resource-id, "messageTv")]').is_displayed()
            return False
        except NoSuchElementException:
            return True

    def is_join_now_button_displayed(self):
        self.select_session_specific('on')[0].click()
        self.session_pop.cancel_join_session()
        try:
            btn_disp = self.get_element('xpath', self.joinnow).is_displayed()
            return btn_disp
        except NoSuchElementException:
            return False

