from pages.base.masterclass import MasterClassBase


class MasterClass(MasterClassBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver

    def scroll_rc_in_view(self):
        raise NotImplementedError()

    def is_rc_session_card_displayed(self):
        raise NotImplementedError()

    def is_sessions_under_rc_displayed(self):
        raise NotImplementedError()

    def verify_rc_session_card_details(self):
        raise NotImplementedError()

    def is_all_rc_sessions_displayed(self):
        raise NotImplementedError()

    def is_see_all_link_displayed(self):
        raise NotImplementedError()

    def click_option_see_more(self):
        raise NotImplementedError()

    def reset_view(self):
        raise NotImplementedError()

    def get_up_next_master_class_session(self):
        raise NotImplementedError()

    def get_completed_master_class_session(self):
        raise NotImplementedError()

    def is_regular_session_displayed(self):
        raise NotImplementedError()

    def verify_booking_screen(self):
        raise NotImplementedError()

    def book_master_class(self):
        raise NotImplementedError()

    def is_all_workshop_tag_displayed(self):
        raise NotImplementedError()

    def verify_session_details(self):
        raise NotImplementedError()

    def tap_on_master_card(self):
        raise NotImplementedError()

    def book_offline(self):
        raise NotImplementedError()

    def is_upcoming_regular_cards_displayed(self):
        raise NotImplementedError()

    def is_regular_classes_scrollable(self):
        raise NotImplementedError()

    def verify_filling_fast_label(self):
        raise NotImplementedError()

    def is_master_class_available(self):
        raise NotImplementedError()

    def get_master_class_join_now_button(self):
        raise NotImplementedError()

    def tap_up_next_mc_session(self):
        raise NotImplementedError()

    def join_master_class_session(self):
        raise NotImplementedError()

    def skip_the_session_booking_time(self):
        raise NotImplementedError()

    def end_master_class_session(self):
        raise NotImplementedError()

    def is_completed_mc_session_displayed(self):
        raise NotImplementedError()

    def attach_requisite(self):
        raise NotImplementedError()

    @staticmethod
    def format_date_time(*args):
        raise NotImplementedError()

    def is_master_class_sorted(self):
        raise NotImplementedError()
