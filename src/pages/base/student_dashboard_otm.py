from abc import ABC, abstractmethod


class StudentDashboardBase(ABC):
    @abstractmethod
    def verify_is_text_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_back_nav_btn_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_one_to_mega_screen_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def ps_home_page_tab(self):
        raise NotImplementedError()

    @abstractmethod
    def get_session(self):
        raise NotImplementedError()

    @abstractmethod
    def completed_session(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_card(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_rate_join_now(self):
        raise NotImplementedError()

    @abstractmethod
    def is_button_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_join_now_btn_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def session_join_now(self):
        raise NotImplementedError()

    @abstractmethod
    def is_bottom_sheet_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def bottom_sheet_okay_btn(self):
        raise NotImplementedError()

    @abstractmethod
    def network_btn_retry(self):
        raise NotImplementedError()

    @abstractmethod
    def is_session_details_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_button(self):
        raise NotImplementedError()

    @abstractmethod
    def is_completed_sessions_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_completed_check_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_screen_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def click_app_back_btn(self):
        raise NotImplementedError()

    @abstractmethod
    def tap_on_req_grp(self):
        raise NotImplementedError()

    @abstractmethod
    def is_completed_sessions_sorted(self):
        raise NotImplementedError()

    @abstractmethod
    def click_back_button(self):
        raise NotImplementedError()

    @abstractmethod
    def is_premium_school_homepage_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_all_sessions_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_up_next_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_post_requisite_attached(self):
        raise NotImplementedError()

    @abstractmethod
    def is_rate_now_card_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_rated_count_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_pr_details_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_pre_post_requisite_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_see_more(self):
        raise NotImplementedError()

    @abstractmethod
    def get_req_sessions(self):
        raise NotImplementedError()

    @abstractmethod
    def is_see_more_option_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def scroll_up_next_top(self):
        raise NotImplementedError()

    @abstractmethod
    def select_up_coming_card(self):
        raise NotImplementedError()

    @abstractmethod
    def last_completed_session_up_next(self):
        raise NotImplementedError()

    @abstractmethod
    def get_join_now_session(self):
        raise NotImplementedError()

    @abstractmethod
    def get_completed_last_session(self):
        raise NotImplementedError()

    @abstractmethod
    def join_session(self):
        raise NotImplementedError()

    @abstractmethod
    def complete_last_session(self):
        raise NotImplementedError()

    @abstractmethod
    def session_rating(self):
        raise NotImplementedError()

    @abstractmethod
    def rate_session(self):
        raise NotImplementedError()

    @abstractmethod
    def is_completed_first_card(self):
        raise NotImplementedError()

    @abstractmethod
    def is_all_post_requisite_accessible(self):
        raise NotImplementedError()

    @abstractmethod
    def is_live_chat_loaded(self):
        raise NotImplementedError()

    @abstractmethod
    def complete_assessment(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_and_start_assessment(self):
        raise NotImplementedError()

    @abstractmethod
    def refresh(self):
        raise NotImplementedError()
