from abc import ABC, abstractmethod


class LoginBase(ABC):
    @abstractmethod
    def implicit_wait_for(self):
        raise NotImplementedError()

    @abstractmethod
    def set_user_profile(self):
        raise NotImplementedError()

    @abstractmethod
    def grant_permissions(self):
        raise NotImplementedError()

    @abstractmethod
    def switch_profile(self):
        raise NotImplementedError()

    @abstractmethod
    def switch_grade(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_user_profile(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_home_screen(self):
        raise NotImplementedError()

    @abstractmethod
    def on_boarding_activity(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_premium_school(self):
        raise NotImplementedError()

    @abstractmethod
    def enter_phone(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_next(self):
        raise NotImplementedError()

    @abstractmethod
    def enter_password(self):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def switch_back_to_app():
        raise NotImplementedError()

    @abstractmethod
    def is_app_icon_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_alert_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def allow_deny_permission(self,permissions: list):
        raise NotImplementedError()

    @abstractmethod
    def is_login_form_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def text_match(self):
        raise NotImplementedError()

    @abstractmethod
    def dropdown_select(self):
        raise NotImplementedError()

    @abstractmethod
    def is_dropdown_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def mobile_number_input(self):
        raise NotImplementedError()

    @abstractmethod
    def find_buttons(self):
        raise NotImplementedError()

    @abstractmethod
    def find_input_boxes(self):
        raise NotImplementedError()

    @abstractmethod
    def is_toast_message_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def clear_input_field(self):
        raise NotImplementedError()

    @abstractmethod
    def validate_error_msg(self):
        raise NotImplementedError()

    @abstractmethod
    def is_app_minimized(self):
        raise NotImplementedError()

    @abstractmethod
    def is_all_permission_visible(self):
        raise NotImplementedError()

    @abstractmethod
    def is_password_field_visible(self):
        raise NotImplementedError()

    @abstractmethod
    def field_visibility_text(self):
        raise NotImplementedError()

    @abstractmethod
    def is_homescreen_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_session_card(self):
        raise NotImplementedError()

    @abstractmethod
    def is_offline_validation_layout_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_offline_validation_layout(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_link(self):
        raise NotImplementedError()

    @abstractmethod
    def wait_for_dialog_to_be_invisible(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_country_code_dropdown(self):
        raise NotImplementedError()

    @abstractmethod
    def enter_reg_mobile_number(self):
        raise NotImplementedError()

    @abstractmethod
    def enter_cc_and_phone_number(self):
        raise NotImplementedError()

    @abstractmethod
    def select_country_code(self):
        raise NotImplementedError()

    @abstractmethod
    def wait_for_element_not_to_be_present(self):
        raise NotImplementedError()

    @abstractmethod
    def is_otp_screen_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_snack_bar_message(self):
        raise NotImplementedError()

    @abstractmethod
    def is_auto_otp_dialog_box_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def enter_otp(self):
        raise NotImplementedError()

    @abstractmethod
    def get_otp(self):
        raise NotImplementedError()

    @abstractmethod
    def is_timer_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def is_text_box_editable(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_edit_icon(self):
        raise NotImplementedError()

    @abstractmethod
    def is_one_to_many_dashboard_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def tap_bck_btn(self):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_from_config(key):
        raise NotImplementedError()

    @abstractmethod
    def click_on_one_to_many(self):
        raise NotImplementedError()

    @abstractmethod
    def select_country_code_other(self):
        raise NotImplementedError()

    @abstractmethod
    def enter_passwd(self):
        raise NotImplementedError()

    @abstractmethod
    def login_with_otp(self):
        raise NotImplementedError()

    @abstractmethod
    def reset_and_login_with_otp(self):
        raise NotImplementedError()

    @abstractmethod
    def cancel_session_join(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_student_profile(self):
        raise NotImplementedError()

    @abstractmethod
    def is_up_next_and_unattended_cards_displayed(self):
        raise NotImplementedError()

    @abstractmethod
    def tap_on(self):
        raise NotImplementedError()
