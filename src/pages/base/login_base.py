from abc import ABC, abstractmethod


class LoginBase(ABC):

    @abstractmethod
    def click_on_premium_school(self):
        raise NotImplemented('subclasses must override click_on_premium_school()!')

    @abstractmethod
    def click_on_hamburger(self):
        raise NotImplemented

    @abstractmethod
    def enter_phone(self,mobile_num):
        raise NotImplemented('subclasses must override enter_phone()!')

    @abstractmethod
    def enter_otp(self,cc,mobile_num,otp):
        raise NotImplemented('subclasses must override enter_otp()!')

    @abstractmethod
    def verify_home_page_loaded(self):
        raise NotImplemented('subclasses must override verify_home_page_loaded()!')

    @abstractmethod
    def navigate_to_home_screen(self, login_profile, user_profile, sub_profile):
        raise NotImplemented()

    @abstractmethod
    def navigate_to_one_to_many_and_mega_user(self):
        raise NotImplemented()

    @abstractmethod
    def login_as_free_user(self):
        raise NotImplemented()
