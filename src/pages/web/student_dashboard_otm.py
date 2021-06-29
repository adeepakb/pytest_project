from pages.base.student_dashboard_otm import StudentDashboardBase


class StudentDashboardOneToMega(StudentDashboardBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver

    def verify_is_text_displayed(self):
        raise NotImplementedError()

    def is_back_nav_btn_displayed(self):
        raise NotImplementedError()

    def is_one_to_mega_screen_displayed(self):
        raise NotImplementedError()

    def ps_home_page_tab(self):
        raise NotImplementedError()

    def get_session(self):
        raise NotImplementedError()

    def completed_session(self):
        raise NotImplementedError()

    def click_on_card(self):
        raise NotImplementedError()

    def verify_rate_join_now(self):
        raise NotImplementedError()

    def is_button_displayed(self):
        raise NotImplementedError()

    def is_join_now_btn_displayed(self):
        raise NotImplementedError()

    def session_join_now(self):
        raise NotImplementedError()

    def is_bottom_sheet_displayed(self):
        raise NotImplementedError()

    def bottom_sheet_okay_btn(self):
        raise NotImplementedError()

    def network_btn_retry(self):
        raise NotImplementedError()

    def is_session_details_displayed(self):
        raise NotImplementedError()

    def click_on_button(self):
        raise NotImplementedError()

    def is_completed_sessions_displayed(self):
        raise NotImplementedError()

    def is_completed_check_displayed(self):
        raise NotImplementedError()

    def is_screen_displayed(self):
        raise NotImplementedError()

    def click_app_back_btn(self):
        raise NotImplementedError()

    def tap_on_req_grp(self):
        raise NotImplementedError()

    def is_completed_sessions_sorted(self):
        raise NotImplementedError()

    def click_back_button(self):
        raise NotImplementedError()

    def is_premium_school_homepage_displayed(self):
        raise NotImplementedError()

    def is_all_sessions_displayed(self):
        raise NotImplementedError()

    def is_up_next_displayed(self):
        raise NotImplementedError()

    def is_post_requisite_attached(self):
        raise NotImplementedError()

    def is_rate_now_card_displayed(self):
        raise NotImplementedError()

    def is_rated_count_displayed(self):
        raise NotImplementedError()

    def is_pr_details_displayed(self):
        raise NotImplementedError()

    def is_pre_post_requisite_displayed(self):
        raise NotImplementedError()

    def click_on_see_more(self):
        raise NotImplementedError()

    def get_req_sessions(self):
        raise NotImplementedError()

    def is_see_more_option_displayed(self):
        raise NotImplementedError()

    def scroll_up_next_top(self):
        raise NotImplementedError()

    def select_up_coming_card(self):
        raise NotImplementedError()

    def last_completed_session_up_next(self):
        raise NotImplementedError()

    def get_join_now_session(self):
        raise NotImplementedError()

    def get_completed_last_session(self):
        raise NotImplementedError()

    def join_session(self):
        raise NotImplementedError()

    def complete_last_session(self):
        raise NotImplementedError()

    def session_rating(self):
        raise NotImplementedError()

    def rate_session(self):
        raise NotImplementedError()

    def is_completed_first_card(self):
        raise NotImplementedError()

    def is_all_post_requisite_accessible(self):
        raise NotImplementedError()

    def is_live_chat_loaded(self):
        raise NotImplementedError()

    def complete_assessment(self):
        raise NotImplementedError()

    def verify_and_start_assessment(self):
        raise NotImplementedError()

    def refresh(self):
        raise NotImplementedError()
