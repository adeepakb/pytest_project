from abc import ABC, abstractmethod


class MasterClassBase(ABC):
    @abstractmethod
    def scroll_rc_in_view(self):
        raise NotImplementedError()

    @abstractmethod
    def is_rc_session_card_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_sessions_under_rc_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_rc_session_card_details(self):
        raise NotImplementedError()

    @abstractmethod
    def is_all_rc_sessions_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_see_all_link_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def click_option_see_more(self):
        raise NotImplementedError()

    @abstractmethod
    def reset_view(self):
        raise NotImplementedError()

    @abstractmethod
    def get_up_next_master_class_session(self):
        raise NotImplementedError()

    @abstractmethod
    def get_completed_master_class_session(self):
        raise NotImplementedError()

    @abstractmethod
    def is_regular_session_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_booking_screen(self):
        raise NotImplementedError()

    @abstractmethod
    def book_master_class(self):
        raise NotImplementedError()

    @abstractmethod
    def is_all_workshop_tag_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_session_details(self):
        raise NotImplementedError()

    @abstractmethod
    def tap_on_master_card(self):
        raise NotImplementedError()

    @abstractmethod
    def book_offline(self):
        raise NotImplementedError()

    @abstractmethod
    def is_upcoming_regular_cards_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_regular_classes_scrollable(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_filling_fast_label(self):
        raise NotImplementedError()

    @abstractmethod
    def is_master_class_available(self):
        raise NotImplementedError()

    @abstractmethod
    def get_master_class_join_now_button(self):
        raise NotImplementedError()

    @abstractmethod
    def tap_up_next_mc_session(self):
        raise NotImplementedError()

    @abstractmethod
    def join_master_class_session(self):
        raise NotImplementedError()

    @abstractmethod
    def skip_the_session_booking_time(self):
        raise NotImplementedError()

    @abstractmethod
    def end_master_class_session(self):
        raise NotImplementedError()

    @abstractmethod
    def is_completed_mc_session_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def attach_requisite(self):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def format_date_time(*args):
        raise NotImplementedError()

    @abstractmethod
    def is_master_class_sorted(self):
        raise NotImplementedError()
