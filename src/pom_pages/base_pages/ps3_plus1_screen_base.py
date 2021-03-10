from abc import ABC, abstractmethod


class PS_3Plus1ScreenBase(ABC):

    @abstractmethod
    def is_calendar_with_date_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_timestamp_with_time_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_back_button_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_forward_button_present(self):
        raise NotImplemented()

    @abstractmethod
    def verify_optional_mandatory_class_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_date_time_present(self):
        raise NotImplemented()

    @abstractmethod
    def verify_change_topic_not_present_mandatory_session(self):
        raise NotImplemented()

    @abstractmethod
    def find_latest_mandatory_topic(self):
        raise NotImplemented()

    @abstractmethod
    def verify_date_time_format(self):
        raise NotImplemented()

    @abstractmethod
    def card_arrow_button_click(self):
        raise NotImplemented()

    @abstractmethod
    def verify_choose_topic_screen(self):
        raise NotImplemented()

    @abstractmethod
    def verify_topic_select_button(self):
        raise NotImplemented()

    @abstractmethod
    def tap_back_icon(self):
        raise NotImplemented()

    @abstractmethod
    def verify_choose_topic_title(self, latest_topic_title):
        raise NotImplemented()

    @abstractmethod
    def select_first_topic(self):
        raise NotImplemented()

    @abstractmethod
    def verify_extra_session_booked(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_booked_extra_session(self):
        raise NotImplemented()

    @abstractmethod
    def is_session_desc_present(self):
        raise NotImplemented()

    @abstractmethod
    def change_topic_and_verify(self):
        raise NotImplemented()

    @abstractmethod
    def verify_ps_tabs(self, expected_text):
        raise NotImplemented()

    @abstractmethod
    def tap_on_tab(self, text):
        raise NotImplemented()