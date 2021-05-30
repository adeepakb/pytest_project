from abc import ABC, abstractmethod
import requests


class TrialClassBase(ABC):

    @abstractmethod
    def scroll_rc_in_view(self):
        raise NotImplemented()

    @abstractmethod
    def is_book_present_for_free_trail_classes(self):
        raise NotImplemented()

    @abstractmethod
    def is_master_class_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_sessions_under_rc_displayed(self):
        raise NotImplemented()

    @abstractmethod
    def is_see_all_link_displayed(self):
        raise NotImplemented()

    @abstractmethod
    def click_option_see_more(self, text):
        raise NotImplemented()

    @abstractmethod
    def is_upnext_trial_class_completed(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_tab(self, text):
        raise NotImplemented()

    @abstractmethod
    def get_up_next_trial_class_session(self):
        raise NotImplemented()

    @abstractmethod
    def is_trial_class_booked(self):
        raise NotImplemented()

    @abstractmethod
    def book_master_class(self, db):
        raise NotImplemented()

    @abstractmethod
    def is_autobook_present(self):
        raise NotImplemented()

    @abstractmethod
    def verify_user_missed_session(self):
        raise NotImplemented()

    @abstractmethod
    def book_trial_class(self):
        raise NotImplemented()

    @abstractmethod
    def back_navigation(self):
        raise NotImplemented()

    @abstractmethod
    def book_special_master_class(self):
        raise NotImplemented()

    @abstractmethod
    def is_master_class_booked(self):
        raise NotImplemented()

    @abstractmethod
    def verify_completed_trial_cards(self):
        raise NotImplemented()

    @staticmethod
    def delete_completed_sessions_api(premium_id):
        url = "https://api.tllms.com/internal/staging/" \
              "tutor_plus/internal_api/one_to_mega/v1/courses_subscriptions/bulk_delete"
        headers = {'Content-Type': 'application/json'}
        payload = {"premium_account_id": premium_id}
        r = requests.delete(url, json=payload, headers=headers)
        print(r.status_code)
        return r.status_code

    @abstractmethod
    def delete_completed_sessions(self):
        raise NotImplemented()

    @staticmethod
    def expire_free_trail_subscriptions_api(premium_id):
        url = "https://api.tllms.com/internal/staging/tutor_plus/" \
              "internal_api/one_to_mega/v1/courses_subscriptions/bulk_expire"
        headers = {'Content-Type': 'application/json'}
        payload = {"premium_account_id": premium_id}
        r = requests.post(url, json=payload, headers=headers)
        print(r.status_code)
        return r.status_code

    @abstractmethod
    def expire_free_trail_subscriptions(self):
        raise NotImplemented()

    @abstractmethod
    def verify_rcmnded_section_ispresent(self):
        raise NotImplemented()

    @abstractmethod
    def verify_free_trial_message(self):
        raise NotImplemented()