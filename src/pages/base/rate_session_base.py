from abc import ABC, abstractmethod


class LoginBase(ABC):

    @abstractmethod
    def launch_and_navigate_to_login_page(self):
        raise NotImplemented('subclasses must override launch_and_navigate_to_login_page()!')


    @abstractmethod
    def click_on_premium_school(self):
        raise NotImplemented('subclasses must override click_on_premium_school()!')

    @abstractmethod
    def enter_phone(self):
        raise NotImplemented('subclasses must override enter_phone()!')

    @abstractmethod
    def enter_otp(self):
        raise NotImplemented('subclasses must override enter_otp()!')

    @abstractmethod
    def verify_home_page_loaded(self):
        raise NotImplemented('subclasses must override verify_home_page_loaded()!')
