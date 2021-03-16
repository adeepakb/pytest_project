import pytest
from appium.webdriver.common.touch_action import TouchAction

from pages.android.scroll_cards import ScrollCards
from utilities.common_methods import CommonMethods
from pages.android.login_android import Login
from pages.android.session_data import SessionData
from utilities.tutor_common_methods import TutorCommonMethods

CommonMethods = CommonMethods()


class StartSession:
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.action = TouchAction(driver)
        self.login = Login(driver)
        self.driver = driver
        self.action = TouchAction(driver)
        self.root = None
        self.sessiondata = SessionData(driver)
        self.scrollcards = ScrollCards(driver)
        self.back_navigation = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/roundedNavButton"]'
        self.card = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/cvScheduleCard"]'

    def find_up_next_session(self):
        flag = False
        while True:
            i = 0
            session_cards_list = self.obj.get_elements('xpath', self.card)
            while i < 5:
                status = self.sessiondata.check_for_up_next(session_cards_list[i])
                if status == 'UP NEXT':
                    session_cards_list[i].click()
                    flag = True
                    break
                i += 1
                if i == 5:
                    self.scrollcards.scroll_by_card(session_cards_list[1], session_cards_list[3])
                    i = 0
                    session_cards_list = self.obj.get_elements('xpath', self.card)
            if flag:
                break
            if flag is False:
                pytest.skip("No 'UP NEXT' session present")
        return i

    def is_back_arrow_button_displayed(self):
        assert self.obj.is_element_present('xpath', self.back_navigation), "back arrow button not present"

    def click_back_arrow_button(self):
        self.obj.element_click('xpath', self.back_navigation)

    def click_device_back(self):
        self.obj.click_back()
