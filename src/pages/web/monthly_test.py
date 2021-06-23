from pages.base.monthly_test import MonthlyTestBase


class MonthlyTest(MonthlyTestBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver

    def verify_session_details(self, **kwargs):
        raise NotImplementedError()

    def is_test_card_displayed(self):
        raise NotImplementedError()

    def start_test(self, **kwargs):
        raise NotImplementedError()

    def take_test(self):
        raise NotImplementedError()

    def verify_test_instruction_screen(self, **kwargs):
        raise NotImplementedError()

    def click_on_test_card(self):
        raise NotImplementedError()

    def is_session_details_page_displayed(self):
        raise NotImplementedError()

    def verify_last_question(self, **kwargs):
        raise NotImplementedError()

    def start_assessment_web(self, **kwargs):
        raise NotImplementedError()

    def is_end_finish_button_displayed(self):
        raise NotImplementedError()

    def is_resume_button_displayed(self):
        raise NotImplementedError()

    def select_random_question(self, **kwargs):
        raise NotImplementedError()

    def verify_web_assessment_screen(self, **kwargs):
        raise NotImplementedError()

    def saved_session(self, **kwargs):
        raise NotImplementedError()

    def login_learn_staging(self, context):
        raise NotImplementedError()

    def resume_assessment_on_web(self, **kwargs):
        raise NotImplementedError()

    def get_up_test_topic_name(self, **kwargs):
        raise NotImplementedError()

    def assessment_confirmation_pop_up(self):
        raise NotImplementedError()

    def offline_assessment(self, **kwargs):
        raise NotImplementedError()

    def submit_assessment_offline(self, **kwargs):
        raise NotImplementedError()

    def is_error_msg_displayed(self):
        raise NotImplementedError()

    def book_master_class(self, **kwargs):
        raise NotImplementedError()

    def complete_assessment_session(self, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def is_session_end_time_reached():
        raise NotImplementedError()

    def is_result_button_displayed(self):
        raise NotImplementedError()

    def is_assessment_displayed_in_completed_tab(self):
        raise NotImplementedError()

    def is_start_test_btn_displayed_at_start_time(self):
        raise NotImplementedError()
