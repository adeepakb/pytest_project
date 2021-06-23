from pages.base.session_requisite import SessionRequisiteBase


class SessionRequisite(SessionRequisiteBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver

    def is_element_displayed(self):
        raise NotImplementedError()

    def verify_requisite_details(self):
        raise NotImplementedError()

    def click_app_back_btn(self):
        raise NotImplementedError()

    def get_req_sessions(self):
        raise NotImplementedError()

    def verify_subject_details(self):
        raise NotImplementedError()

    def verify_topic_details(self):
        raise NotImplementedError()

    @staticmethod
    def verify_calendar_details(*args):
        raise NotImplementedError()

    @staticmethod
    def verify_time_details(*args):
        raise NotImplementedError()

    def is_subject_icon_displayed(self):
        raise NotImplementedError()

    def is_cards_loaded(self):
        raise NotImplementedError()

    def verify_content_description(self):
        raise NotImplementedError()

    def get_requisites_attached(self):
        raise NotImplementedError()

    def is_see_more_option_displayed(self):
        raise NotImplementedError()

    def is_all_requisites_attached(self):
        raise NotImplementedError()

    def ps_home_page_tab(self):
        raise NotImplementedError()

    def scroll_up_next_top(self):
        raise NotImplementedError()

    def get_session(self):
        raise NotImplementedError()

    def verify_video_playing(self):
        raise NotImplementedError()

    def is_video_not_buffering(self):
        raise NotImplementedError()

    def static_exo_player(self):
        raise NotImplementedError()

    def complete_video(self):
        raise NotImplementedError()

    def change_orientation(self):
        raise NotImplementedError()

    def is_video_landscape_playable(self):
        raise NotImplementedError()

    def verify_video_player_elements(self):
        raise NotImplementedError()

    def verify_session_card_details(self):
        raise NotImplementedError()

    def future_card(self):
        raise NotImplementedError()

    def verify_pre_requisite_details(self):
        raise NotImplementedError()

    def verify_app_home_screen(self):
        raise NotImplementedError()
