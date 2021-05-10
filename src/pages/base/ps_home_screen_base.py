from abc import ABC, abstractmethod


class PSHomeScreenBase(ABC):

    @abstractmethod
    def verify_ps_tabs(self, expected_text):
        raise NotImplemented()

    @abstractmethod
    def tap_on_tab(self, text):
        raise NotImplemented()

    @abstractmethod
    def verify_arrow_present_for_each_requisite(self):
        raise NotImplemented()

    @abstractmethod
    def is_tab_selected(self, text):
        raise NotImplemented()

    @abstractmethod
    def click_back(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_get_help(self):
        raise NotImplemented()

    @abstractmethod
    def is_get_help_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_back_nav_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_bottom_sheet_present(self):
        raise NotImplemented()

    @abstractmethod
    def close_get_help(self):
        raise NotImplemented()

    @abstractmethod
    def verify_get_help_close(self):
        raise NotImplemented()

    @abstractmethod
    def verify_card_details(self):
        raise NotImplemented()

    @abstractmethod
    def verify_session_details_card_loaded(self):
        raise NotImplemented()

    @abstractmethod
    def verify_button(self, text):
        raise NotImplemented()

    @abstractmethod
    def attach_post_requisite(self, driver, requisite_name):
        raise NotImplemented()

    @abstractmethod
    def verify_completed_card_details(self):
        raise NotImplemented()

    @abstractmethod
    def tap_outside_dialog_layout(self):
        raise NotImplemented()

    @abstractmethod
    def is_user_in_ps_page(self):
        raise NotImplemented()
