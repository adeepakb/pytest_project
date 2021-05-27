import time

from appium.webdriver.common.touch_action import TouchAction

from pages.android.Hamburgermenu import Hamburger
from pages.android.scroll_cards import ScrollCards
from pages.base.know_more import KnowMoreTestBase
from utilities.interrupt import set_connection_type
from utilities.tutor_common_methods import TutorCommonMethods
import pytest_check as check


class ReturnType:
    def __init__(self, result, reason):
        self.result = False
        self.reason = ""


class KnowMoreTest(KnowMoreTestBase, TutorCommonMethods):
    def __init__(self, driver):
        self.driver = driver
        self.Hamburg = Hamburger(driver)
        self.ScrollCards = ScrollCards(driver)
        package_name = self.driver.desired_capabilities['appPackage'] + ':id'
        self.hamburger_icon = "id", "%s/roundedNavButton" % package_name
        self.byjus_classes = "id", "com.byjus.thelearningapp.premium:id/home_drawer_list_item_txtvw"
        self.know_more = "id", "com.byjus.thelearningapp.premium:id/home_drawer_list_item_txtvw_new"
        self.confirm_and_book = "id", "%s/primaryAction" % package_name

    def click_on_hamburger(self):
        try:
            self.get_element(*self.hamburger_icon).click()
            return True
        except:
            return False

    def verify_know_more_displayed(self):
        return_type = ReturnType(False, "")
        try:
            self.get_element(*self.byjus_classes).is_displayed()
            self.get_element(*self.know_more).is_displayed()
            return_type.result = True
            return_type.reason = "Know more is being displayed in Hamburger"
        except:
            return_type.result = False
            return_type.reason = "Know more is not being displayed in Hamburger"
        return return_type

    def tap_on_byjus_classes_in_hamburger(self, button='Know More'):
        button_element = None
        if button == 'Know More':
            button_element = self.know_more
        else:
            button_element = self.byjus_classes

        try:
            if self.verify_know_more_displayed().result:
                button_element = self.get_element(*button_element)
                button_element.click()
            else:
                self.click_on_hamburger()
                button_element = self.get_element(*button_element)
                button_element.click()
            return True
        except:
            return False

    def validate_know_more(self):
        activityname = 'PremiumSchoolInfoActivity'
        if activityname in self.driver.current_activity:
            self.click_back()
            self.click_on_hamburger()
        try:
            self.tap_on_byjus_classes_in_hamburger()
            return True
        except:
            return False

    def validate_webview_activity(self):
        activityname = 'PremiumSchoolInfoActivity'

        if activityname in self.driver.current_activity:
            return True
        else:
            return False

    def validate_know_more_webview(self):

        return_type = ReturnType(False, "")
        if self.validate_webview_activity() is True:
            return_type.result = True
        else:
            return_type.result = False
            return_type.reason = "Not in know more webview"
            return return_type

        if self.is_button_displayed_with_text("Book a Free Class") is True:
            return_type.result = True
            return_type.reason = "Book a free class button is shown"
        else:
            return_type.result = False
            return_type.reason = "Book a free class button is not shown"
            return return_type
        return return_type

    def validate_book_a_free_class_card(self):
        return_type = ReturnType(False, "")
        if self.is_button_displayed_with_text("Book a Free Class") is True:
            return_type.result = True
            return_type.reason = "Book a free class button is shown"
        else:
            return_type.result = False
            return_type.reason = "Book a free class button is not shown"
            return return_type
        return return_type

    def tap_on_book_card(self):
        return_type = ReturnType(False, "")
        try:
            self.button_click("Book a Free Class")
            return_type.result = True
            return_type.reason = "Found and clicked on Book a Free Class Button"
        except:
            return_type.result = False
            return_type.reason = "Not Found and not clicked on Book a Free Class Button"
        return return_type

    def select_online_offline_mode(self, mode):
        return_type = ReturnType(False, "")
        try:
            set_connection_type(self.driver, mode)
            return_type.result = True
            return_type.reason = "Network mode set to {}.".format(mode)
        except:
            return_type.result = False
            return_type.reason = "Couldn't set network mode to {}.".format(mode)
        return return_type

    def verify_book_free_class_screen(self, expected_activity='PremiumSchoolCourseActivity'):
        return_type = ReturnType(False, "")

        if expected_activity in self.driver.current_activity:
            return_type.result = True
            return_type.reason = " User is in Book a free class page {}".format(expected_activity)

        else:
            return_type.result = False
            return_type.reason = " User is in student dashboard {}".format(expected_activity)

        return return_type

    def tap_on_book_button(self):
        return_type = ReturnType('False', "")
        try:
            self.button_click("Book")
            return_type.result = True
            return_type.reason = "Book button found"
        except:
            return_type.result = False
            return_type.reason = "Book button not found on book class screen"
        return return_type

    def book_a_session(self):
        return_type = ReturnType(False, "")
        try:
            self.element_click(*self.confirm_and_book)
            return_type.result = True
            return_type.reason(" Clicked on confirm and book button on boking page")
        except:
            return_type.result = False
            return_type.reason(" Couldn't click on confirm and book button on boking page")
        return return_type