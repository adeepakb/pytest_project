from selenium.common.exceptions import NoSuchElementException
from Utilities.tutor_common_methods import TutorCommonMethods


class SessionData:
    def __init__(self, driver):
        self.driver = driver
        common = TutorCommonMethods(self.driver)
        self.get_elements = common.get_elements
        self.get_element = common.get_element

    def get_cards_list(self):
        elements = self.get_elements('xpath', '//*[contains(@resource-id, "ScheduleCard")]')
        return elements

    def get_session_header_month(self):
        self.driver.implicitly_wait(0)
        condition = 0
        elements = self.get_elements('xpath', '//*[contains(@resource-id, "rvScheduleList")]/*')
        present_at = 0
        for element in elements:
            try:
                month_header = element.find_element_by_xpath(
                    '//*[contains(@resource-id, "month_header")]').text
                if condition == 0 and present_at != 0:
                    try:
                        elements[0].find_element_by_xpath(
                            '//*[contains(@resource-id, "SessionTakenDone")]')
                        condition = 1
                    except NoSuchElementException:
                        try:
                            elements[0].find_element_by_xpath(
                                '//*[contains(@resource-id, "SubjectName")]').text
                        except NoSuchElementException:
                            present_at -= 1
                            condition = 1
                return month_header, present_at
            except NoSuchElementException:
                pass
            present_at += 1
        return None, None

    @staticmethod
    def get_sessions_ratings(card):
        try:
            rate_status = card.find_element_by_xpath(
                '//*[contains(@resource-id, "session_rate_bar")]').text
        except NoSuchElementException:
            rate_status = None
        return rate_status

    @staticmethod
    def is_rate_session_link_present(card):
        try:
            card.find_element_by_xpath(
                '//*[contains(@resource-id, "tvRateSessionLink")]')
            return "Not rated"
        except NoSuchElementException:
            return None

    @staticmethod
    def check_for_up_next(card):
        try:
            up_next = card.find_element_by_xpath(
                '//*[contains(@resource-id, "up_next_label")]').text
            return up_next
        except NoSuchElementException:
            return False

    def get_session_status(self, card):
        try:
            session_done = card.find_element_by_xpath(
                '//*[contains(@resource-id, "SessionTakenDone")]'
            ).is_displayed()
            if session_done:
                return 'Completed'
        except NoSuchElementException:
            up_next_status = self.check_for_up_next(card)
            if up_next_status:
                return up_next_status
            return 'Not Completed'

    def get_card_with_index(self, index):
        cards = self.get_cards_list()
        card = cards[index]
        return card

    @staticmethod
    def get_session_subject_name(card):
        sub_name = card.find_element_by_xpath(
            '//*[contains(@resource-id,"SubjectName")]').text
        return sub_name

    @staticmethod
    def get_session_topic_name(card):
        topic_name = card.find_element_by_xpath(
            '//*[contains(@resource-id,"TopicName")]').text
        return topic_name

    def get_actual_cards_displayed(self):
        session_cards_time_dtls = self.get_elements('xpath',
                                                    '//*[contains(@resource-id, "SessionScheduleTime")]'
                                                    '//ancestor::android.widget.FrameLayout'
                                                    '[contains(@resource-id,"ScheduleCard")]'
                                                    )
        session_cards_subj_dtls = self.get_elements('xpath',
                                                    '//*[contains(@resource-id, "SubjectName")]'
                                                    '//ancestor::android.widget.FrameLayout'
                                                    '[contains(@resource-id, "ScheduleCard")]'
                                                    )
        if len(session_cards_time_dtls) == len(session_cards_subj_dtls):
            return session_cards_time_dtls
        elif len(session_cards_time_dtls) > len(session_cards_subj_dtls):
            return session_cards_subj_dtls
        return session_cards_time_dtls

    @staticmethod
    def get_session_time_detail(card):
        time_detail_current = card.find_element_by_xpath(
            '//*[contains(@resource-id, "SessionScheduleTime")]').text
        return time_detail_current

    def get_session_card_details(self):
        """get number of cards displayed completely"""
        cards_displayed_complete = self.get_actual_cards_displayed()
        details_list = list()
        for card in cards_displayed_complete:
            '''Session Subject Name'''
            session_sub = self.get_session_subject_name(card)
            '''Session Subject Topic Name'''
            session_topic = self.get_session_topic_name(card)
            '''Session Time Details'''
            session_time = self.get_session_time_detail(card)
            '''Session Completed Status'''
            session_status = self.get_session_status(card)
            '''Session Ratings'''
            session_rating = self.get_sessions_ratings(card)
            '''update to dict'''
            details_list.append(
                {
                    "Subject":  session_sub,
                    "Topic":    session_topic,
                    "Schedule": session_time,
                    "Status":   session_status,
                    "Ratings":  session_rating
                }
            )
        return details_list
