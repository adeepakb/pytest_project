import logging
import random
from datetime import datetime, timedelta
from time import strptime

import pytest
from selenium.common.exceptions import NoSuchElementException

from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.session_popup import SessionAlert
from pages.android.session_data import SessionData
from pages.android.scroll_cards import ScrollCards
from pages.android.login_android import LoginAndroid


class ChooseTopic(TutorCommonMethods):
    def __init__(self, driver):
        self.driver = driver
        self.login = LoginAndroid(driver)
        self.session_data = SessionData(driver)
        self.session_pop = SessionAlert(driver)
        self.scroll_card = ScrollCards(driver)
        self.profile_back_button = '//*[contains(@resource-id, "roundedNavButton")]'
        self.dropdown_month_icon = '//*[contains(@resource-id, "spinnerMonth")]'
        self.dropdown_month_list = '//*[contains(@resource-id, "month_item_name_view")]'
        self.session_time_dtls = '//*[contains(@resource-id, "SessionScheduleTime")]'
        super().__init__(driver)

    def is_up_next_displayed(self):
        self.driver.implicitly_wait(0)
        end = self.get_element('xpath',
                               '//*[contains(@resource-id, "rvScheduleList")]')
        while True:
            ac_cards = self.session_data.get_actual_cards_displayed()
            previous_card = ac_cards[0]
            previous_card_subj = self.session_data.get_session_topic_name(previous_card)
            previous_card_time = self.session_data.get_session_time_detail(previous_card)
            for card in ac_cards:
                response = self.session_data.get_session_status(card)
                if response == "UP NEXT":
                    self.scroll_card.scroll_by_card(card, end)
                    self.driver.implicitly_wait(5)
                    return card
            self.scroll_card.scroll_by_card(ac_cards[-1], end)
            current_card = self.session_data.get_actual_cards_displayed()[0]
            current_card_subj = self.session_data.get_session_topic_name(current_card)
            current_card_time = self.session_data.get_session_time_detail(current_card)
            if previous_card_subj == current_card_subj:
                if previous_card_time == current_card_time:
                    self.driver.implicitly_wait(5)
                    return False

    def is_up_next_card_selected(self):
        c_sub_name, c_topic_name, c_sch_time = None, None, None
        s_sub_name = self.get_element(
            'xpath',
            '//*[contains(@resource-id, "subjectNametv")]'
        ).text
        s_topic_name = self.get_element(
            'xpath',
            '//*[contains(@resource-id, "chapterNametv")]'
        ).text
        s_sch_time = self.get_element(
            'xpath',
            '//*[contains(@resource-id, "sessionDatetv")]'
        ).text

        details_match = self.is_up_next_displayed()
        if details_match is not False:
            c_sub_name = details_match.find_element_by_xpath(
                '//*[contains(@resource-id, "tvSubjectName")]'
            ).text

            c_topic_name = details_match.find_element_by_xpath(
                '//*[contains(@resource-id, "tvTopicName")]'
            ).text
            c_sch_time = details_match.find_element_by_xpath(
                '//*[contains(@resource-id, "tvSessionScheduleTime")]'
            ).text
        if s_sub_name == c_sub_name and s_topic_name == c_topic_name and s_sch_time in c_sch_time:
            return True
        return False

    def is_up_next_badge_displayed(self):
        _text = self.get_element(
            'xpath',
            '//*[contains(@resource-id, "tv_up_next_label")]'
        ).text
        if _text.lower() == "up next":
            return True
        return False

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
                    print("=" * 13 + "POST" + "=" * 13)
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

    def click_on_card_day(self, ctype='post'):
        current_month_year = datetime.now().strftime('%B \'%y')
        self.get_element('xpath', self.dropdown_month_icon).click()
        for month_year in self.get_elements('xpath', self.dropdown_month_list):
            if current_month_year == month_year.text:
                month_year.click()
                break
        self.login.implicit_wait_for(0)
        self.select_session_specific(ctype).click()
        self.login.implicit_wait_for(10)

    def is_choose_topic_card_displayed(self):
        try:
            topic_card = self.get_element(
                'xpath',
                '//*[contains(@resource-id, "detailSessionCardLay")]'
            )
            topic_card_text = topic_card.find_element_by_xpath('//*[contains(@resource-id, "actionCardButton")]').text
            if topic_card_text.lower() == "choose topic":
                return True
            return False
        except NoSuchElementException:
            return None

    def click_on_choose_topic(self):
        self.get_element(
            'xpath',
            '//*[contains(@resource-id, "actionCardButton")]'
        ).click()

    def is_radio_buttons_displayed(self):
        radio_button_list = self.get_elements(
            'xpath',
            "//*[contains(@resource-id, 'ivChangeTopicSelectButton')]"
        )
        if len(radio_button_list) > 1:
            return True
        return False

    def is_change_topic_list_displayed(self):
        try:
            topic_list = self.get_element(
                'xpath',
                '//*[contains(@resource-id, "change_topic_lv")]'
            ).is_displayed()
            return topic_list
        except NoSuchElementException:
            return False

    def is_radio_buttons_and_topic_list_displayed(self):
        if self.is_change_topic_list_displayed() and self.is_radio_buttons_displayed():
            return True
        return False

    def is_list_scrollable(self):
        list_box = self.get_element(
            'xpath',
            '//*[contains(@resource-id, "change_topic_lv")]'
        )
        last_topic_name = list_box.find_elements_by_xpath(
            '//*[contains(@resource-id, "tvChangeTopicTitle")]'
        )
        last_topic_name_text = last_topic_name[-2].text
        self.scroll_card.scroll_by_element(last_topic_name[-2], list_box)
        first_topic_name = list_box.find_elements_by_xpath(
            '//*[contains(@resource-id, "tvChangeTopicTitle")]'
        )
        first_topic_name_text = first_topic_name[0].text
        self.scroll_card.scroll_by_element(first_topic_name[0], list_box, direction='down')
        changed_topic_name_text = list_box.find_elements_by_xpath(
            '//*[contains(@resource-id, "tvChangeTopicTitle")]'
        )[-2].text
        if last_topic_name_text == first_topic_name_text == changed_topic_name_text:
            return True
        return False

    def get_radio_button_selected(self):
        radio_button_list = self.get_elements(
            'xpath',
            "//*[contains(@resource-id, 'ivChangeTopicSelectButton')]"
        )
        list_of_radio_buttons_selected = list()
        for radio_button in radio_button_list:
            if radio_button.is_selected():
                list_of_radio_buttons_selected.append(radio_button)
        return list_of_radio_buttons_selected

    def get_particular_topic_element(self, topic_name):
        list_of_topics = self.get_elements(
            'xpath',
            '//*[contains(@resource-id, "tvChangeTopicTitle")]/../..')
        for parent_element in list_of_topics:
            element = parent_element.find_element_by_xpath('//*[contains(@resource-id, "tvChangeTopicTitle")]')
            if element.text == topic_name:
                return parent_element

    def is_particular_topic_selected(self, actual_topic_name):
        topic_name_element = self.get_particular_topic_element(actual_topic_name)
        try:
            selected_topic = topic_name_element.find_element_by_xpath(
                "//*[contains(@resource-id, 'ivChangeTopicSelectButton')]").is_displayed()
            return selected_topic
        except NoSuchElementException:
            return False

    def click_on_random_topic_radio_button(self):
        self.driver.implicitly_wait(0)
        list_of_topics = self.get_elements(
            'xpath',
            '//*[contains(@resource-id, "tvChangeTopicTitle")]/..'
        )
        for topic in list_of_topics:
            try:
                topic.find_element_by_xpath('//*[contains(@resource-id, "tvChangeTopicDescription")]')
                list_of_topics.remove(topic)
                break
            except NoSuchElementException:
                pass
        topic = list_of_topics[random.randint(0, len(list_of_topics) - 1)]
        topic_text = topic.find_element_by_xpath('//*[contains(@resource-id, "tvChangeTopicTitle")]').text
        topic.find_element_by_xpath("//*[contains(@resource-id, 'ivChangeTopicSelectButton')]").click()
        return topic_text

    def click_on_done_button(self):
        self.get_element(
            'xpath',
            '//*[contains(@resource-id, "change_topic_done_button")]'
        ).click()

    def is_topic_changed(self, change_topic_name):
        self.driver.implicitly_wait(5)
        current_topic = self.get_element(
            'xpath',
            '//*[contains(@resource-id, "chapterNametv")]'
        ).text
        current_schedule_date = self.get_element(
            'xpath',
            '//*[contains(@resource-id, "sessionDatetv")]'
        ).text
        current_schedule_time = self.get_element(
            'xpath',
            '//*[contains(@resource-id, "sessionTimetv")]'
        ).text
        scheduled_cards = self.session_data.get_cards_list()
        for card in scheduled_cards:
            date_time = card.find_element_by_xpath('//*[contains(@resource-id, "tvSessionScheduleTime")]').text
            chapter_name = card.find_element_by_xpath('//*[contains(@resource-id, "tvTopicName")]').text
            if (current_schedule_date and current_schedule_time) in date_time:
                if chapter_name == current_topic == change_topic_name:
                    return True
        return False

    def is_only_one_topic_selected(self):
        radio_button_list = self.get_radio_button_selected()
        if len(radio_button_list) == 1:
            return True
        return False

    def is_change_topic_card_displayed(self):
        try:
            change_topic_text = self.get_element(
                'xpath',
                "//*[contains(@resource-id, 'change_topic_title')]"
            ).text
            if change_topic_text.lower() == 'change topic':
                return True
            return False
        except NoSuchElementException:
            return None

    def is_subtopics_displayed(self, current_topic_name):
        topic_name_element = self.get_particular_topic_element(current_topic_name)
        try:
            sub_topic = topic_name_element.find_element_by_xpath(
                '//*[contains(@resource-id, "tvChangeTopicDescription")]').is_displayed()
            return sub_topic
        except NoSuchElementException:
            return False

    def verify_color_two(self):

        from time import sleep
        sleep(2)
        self.login.implicit_wait_for(0)
        post_element = self.select_session_specific()
        self.login.implicit_wait_for(10)
        logos = self.get_elements('xpath', '//*[contains(@resource-id, "ivSubjectLogo")]//..')
        subject_card = None
        for logo in logos:
            current_detail = logo.find_element_by_xpath(self.session_time_dtls).text
            expected_detail = post_element.find_element_by_xpath(self.session_time_dtls).text
            if current_detail == expected_detail:
                subject_card = logo
        subject_logo = subject_card.find_element_by_xpath(
            '//*[contains(@resource-id, "ivSubjectLogo")]')
        subject_card = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id,"detailSessionCardBg")]')
        for card in (subject_logo, subject_card):
            list_of_colors = self.get_all_colors_present(None, None, element=card)[1][1]
            self.verify_element_color(None, None, rgb_color_code=list_of_colors, index=1, element=card)
