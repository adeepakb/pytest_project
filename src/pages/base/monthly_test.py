from abc import ABC, abstractmethod


class MonthlyTestBase(ABC):
    @abstractmethod
    def verify_session_details(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def is_test_card_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def start_test(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def take_test(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_test_instruction_screen(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def click_on_test_card(self):
        raise NotImplementedError()

    @abstractmethod
    def is_session_details_page_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_last_question(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def start_assessment_web(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def is_end_finish_button_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_resume_button_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def select_random_question(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def verify_web_assessment_screen(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def saved_session(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def login_learn_staging(self, context):
        raise NotImplementedError()

    @abstractmethod
    def resume_assessment_on_web(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def get_up_test_topic_name(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def assessment_confirmation_pop_up(self):
        raise NotImplementedError()

    @abstractmethod
    def offline_assessment(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def submit_assessment_offline(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def is_error_msg_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def book_master_class(self, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def complete_assessment_session(self, **kwargs):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def is_session_end_time_reached():
        raise NotImplementedError()

    @abstractmethod
    def is_result_button_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_assessment_displayed_in_completed_tab(self):
        raise NotImplementedError()

    @abstractmethod
    def is_start_test_btn_displayed_at_start_time(self):
        raise NotImplementedError()
