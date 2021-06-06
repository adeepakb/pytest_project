from abc import ABC, abstractmethod


class StudentSessionBase(ABC):

    @abstractmethod
    def verify_button(self, text):
        raise NotImplemented()

    @abstractmethod
    def is_dots_icon_displayed(self):
        raise NotImplemented('subclasses must override click_on_premium_school()!')

    @abstractmethod
    def is_tutor_icon_displayed(self):
        raise NotImplemented('subclasses must override enter_phone()!')

    @abstractmethod
    def verify_subject_name(self, subject_value):
        raise NotImplemented('subclasses must override enter_otp()!')

    @abstractmethod
    def verify_chapter_name(self, topic_title):
        raise NotImplemented()

    @abstractmethod
    def is_student_chat_enabled(self):
        raise NotImplemented()
    @abstractmethod
    def tap_on_disabled_chat(self):
        raise NotImplemented()

    @abstractmethod
    def is_chat_icon_displayed(self):
        raise NotImplemented()

    @abstractmethod
    def is_live_chat_displayed(self):
        raise NotImplemented()

    @abstractmethod
    def is_chat_close_icon_displayed(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_chat_icon(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_join_now(self):
        raise NotImplemented()

    @abstractmethod
    def close_chat(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_chat_textbox(self):
        raise NotImplemented()

    @abstractmethod
    def tap_outside_dialog_layout(self):
        raise NotImplemented()

    @abstractmethod
    def video_elements_present(self):
        raise NotImplemented()

    @abstractmethod
    def verify_student_chat_dialog(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_chat_dialog(self):
        raise NotImplemented()

    @abstractmethod
    def is_emoji_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_cursor_present(self):
        raise NotImplemented()

    @abstractmethod
    def click_back(self):
        raise NotImplemented()

    @abstractmethod
    def is_keyboard_shown(self):
        raise NotImplemented()

    @abstractmethod
    def enter_text_in_chat(self, message):
        raise NotImplemented()

    @abstractmethod
    def verify_entered_chat(self, message):
        raise NotImplemented()

    @abstractmethod
    def tap_on_chat_send(self):
        raise NotImplemented()

    @abstractmethod
    def verify_message_at_student_side(self, message):
        raise NotImplemented()

    @abstractmethod
    def speed_test(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_cancel(self):
        raise NotImplemented()

    @abstractmethod
    def verify_offline_dialog_disappeared(self):
        raise NotImplemented()

    @abstractmethod
    def scroll_chat_container(self):
        raise NotImplemented()

    @abstractmethod
    def is_video_play_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_video_pause_progress_bar_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_video_progress_bar_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_video_play_pause_progress_bar_present(self):
        raise NotImplemented()
