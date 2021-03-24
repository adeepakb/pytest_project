from abc import ABC, abstractmethod


class InstructionDialogBase(ABC):

    @abstractmethod
    def is_close_instruction_displayed(self):
        raise NotImplemented()

    @abstractmethod
    def is_requisite_list(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_close_instruction(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_begin_assessment(self):
        raise NotImplemented()

    @abstractmethod
    def is_assessment_popup_present(self):
        raise NotImplemented()

    @abstractmethod
    def click_back(self):
        raise NotImplemented()

    @abstractmethod
    def is_user_in_ps_page(self):
        raise NotImplemented()

    @abstractmethod
    def end_test(self):
        raise NotImplemented()

    @abstractmethod
    def verify_score_present(self):
        raise NotImplemented()

    @abstractmethod
    def set_future_assessment_start_date(self):
        raise NotImplemented()

    @abstractmethod
    def set_assessment_start_date_today(self):
        raise NotImplemented()

    @abstractmethod
    def attach_post_requisite_with_assessement(self, assessment_name):
        raise NotImplemented()

    @abstractmethod
    def get_assessment_available_until_date(self):
        raise NotImplemented()

    @abstractmethod
    def set_expired_assessment_end_date(self):
        raise NotImplemented()

    @abstractmethod
    def reset_future_end_date(self):
        raise NotImplemented()

    @abstractmethod
    def capture_screenshot_of_assessment(self, image_name):
        raise NotImplemented()

    @abstractmethod
    def image_diff(self, img1, img2):
        raise NotImplemented()