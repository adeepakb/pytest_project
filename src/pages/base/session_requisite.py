from abc import ABC, abstractmethod


class SessionRequisiteBase(ABC):
    @abstractmethod
    def is_element_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_requisite_details(self):
        raise NotImplementedError()

    @abstractmethod
    def click_app_back_btn(self):
        raise NotImplementedError()

    @abstractmethod
    def get_req_sessions(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_subject_details(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_topic_details(self):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def verify_calendar_details(*args):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def verify_time_details(*args):
        raise NotImplementedError()

    @abstractmethod
    def is_subject_icon_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_cards_loaded(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_content_description(self):
        raise NotImplementedError()

    @abstractmethod
    def get_requisites_attached(self):
        raise NotImplementedError()

    @abstractmethod
    def is_see_more_option_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_all_requisites_attached(self):
        raise NotImplementedError()

    @abstractmethod
    def ps_home_page_tab(self):
        raise NotImplementedError()

    @abstractmethod
    def scroll_up_next_top(self):
        raise NotImplementedError()

    @abstractmethod
    def get_session(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_video_playing(self):
        raise NotImplementedError()

    @abstractmethod
    def is_video_not_buffering(self):
        raise NotImplementedError()

    @abstractmethod
    def static_exo_player(self):
        raise NotImplementedError()

    @abstractmethod
    def complete_video(self):
        raise NotImplementedError()

    @abstractmethod
    def change_orientation(self):
        raise NotImplementedError()

    @abstractmethod
    def is_video_landscape_playable(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_video_player_elements(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_session_card_details(self):
        raise NotImplementedError()

    @abstractmethod
    def future_card(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_pre_requisite_details(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_app_home_screen(self):
        raise NotImplementedError()
