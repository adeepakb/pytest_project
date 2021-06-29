from abc import ABC, abstractmethod


class RateSessionBase(ABC):

    @abstractmethod
    def tap_on_tab(self, text):
        raise NotImplemented()

    @abstractmethod
    def verify_feedback_and_checkbox_present(self, value, i):
        raise NotImplemented()

    @abstractmethod
    def tap_on_okay_button(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_star(self, rating):
        raise NotImplemented()

    @abstractmethod
    def text_match(self, expected_text):
        raise NotImplemented()

    @abstractmethod
    def verify_button(self, text):
        raise NotImplemented()

    @abstractmethod
    def tap_on_join_now(self):
        raise NotImplemented()

    @abstractmethod
    def verify_color_of_completed_status(self, rgb_color_code):
        raise NotImplemented()

    @abstractmethod
    def tap_rate_session_button(self):
        raise NotImplemented()

    @abstractmethod
    def verify_star_rating(self, locator, rating):
        raise NotImplemented()

    @abstractmethod
    def tap_on_first_session_card(self):
        raise NotImplemented()

    @abstractmethod
    def verify_rate_session_close_button(self):
        raise NotImplemented()

    @abstractmethod
    def tap_rate_session_close_button(self):
        raise NotImplemented()

    @abstractmethod
    def click_link(self, text):
        raise NotImplemented()

    @abstractmethod
    def back_navigation(self):
        raise NotImplemented()

    @abstractmethod
    def click_back(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_each_star_and_verify(self):
        raise NotImplemented()

    @abstractmethod
    def deselect_selected_stars_and_verify(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_submit_button(self):
        raise NotImplemented()

    @abstractmethod
    def verify_rating_on_session_details_screen(self, rating):
        raise NotImplemented()

    @abstractmethod
    def get_rated_session_card(self, index):
        raise NotImplemented()

    @abstractmethod
    def verify_rating_on_session_card(self, index, expected_rating):
        raise NotImplemented()

    @abstractmethod
    def verify_submit_button_enabled_or_not(self, text, expected_flag):
        raise NotImplemented()

    @abstractmethod
    def is_data_off_icon_displayed(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_each_star_and_verify_feedback(self):
        raise NotImplemented()

    @abstractmethod
    def verify_feedback_options(self, rating):
        raise NotImplemented()

    @abstractmethod
    def verify_select_deselect_feedback_options(self):
        raise NotImplemented()

    @abstractmethod
    def select_any_feedback(self):
        raise NotImplemented()

    @abstractmethod
    def find_completed_notrated_session(self):
        raise NotImplemented()

    @abstractmethod
    def verify_rate_session_link_is_present(self, text):
        raise NotImplemented()

    @abstractmethod
    def verify_rate_session_details(self, session_details_dict):
        raise NotImplemented()