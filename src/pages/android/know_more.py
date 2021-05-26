import time

from appium.webdriver.common.touch_action import TouchAction

from pages.android.Hamburgermenu import Hamburger
from pages.android.scroll_cards import ScrollCards
from pages.base.know_more import KnowMoreTestBase
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

    def click_on_hamburger(self):
        try:
            self.get_element(*self.hamburger_icon).click()
            return True
        except:
            return False

    def verify_know_more_displayed(self):
        try:
            self.get_element(*self.byjus_classes).is_displayed()
            self.get_element(*self.know_more).is_displayed()
            return True
        except:
            return False

    def tap_on_byjus_classes_in_hamburger(self, button='Know More'):
        button_element = None
        if button == 'Know More':
            button_element = self.know_more
        else:
            button_element = self.byjus_classes

        try:
            if self.verify_know_more_displayed():
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
            return_type.reason= "Found and clicked on Book a Free Class Button"
        except:
            return_type.result = False
            return_type.reason = "Not Found and not clicked on Book a Free Class Button"
        return return_type



    # def scroll_webview(self, start_element, end_element, coincide='bottom', buffer=2):
    #     action = TouchAction(self.driver)
    #     start_element_width = self.element_location_and_size(start_element, dimension='width') // 2
    #     start_x = self.element_location_and_size(start_element, co_ordinates='x') + start_element_width
    #     start_element_height = self.element_location_and_size(start_element, dimension='height')
    #     start_y = self.element_location_and_size(start_element, co_ordinates='y') + start_element_height - buffer
    #     end_y = self.element_location_and_size(end_element, co_ordinates='y') + buffer
    #     action.press(x=start_x, y=start_y).wait(5000).move_to(x=start_x, y=end_y).release().perform()

    def scroll_by_element(self, start_element, end_element, direction='up', coincide='top'):
        action = TouchAction(self.driver)
        start_x = self.element_location_and_size(start_element, co_ordinates='x')
        if coincide == 'top':
            start_y = self.element_location_and_size(start_element, co_ordinates='y')
        elif coincide == 'bottom':
            start_y = self.element_location_and_size(start_element, co_ordinates='y') + \
                      self.element_location_and_size(start_element, dimension='height') - 10
        else:
            raise TypeError(f"can only coincide 'top' or 'bottom' not '{coincide}'.") from None
        end_x = self.element_location_and_size(start_element, co_ordinates='x')
        if direction == 'down':
            end_y = self.element_location_and_size(end_element, co_ordinates='y') + \
                    self.element_location_and_size(end_element, dimension='height') - 10
        else:
            end_y = self.element_location_and_size(end_element, co_ordinates='y')
        action.press(x=start_x, y=start_y).wait(5000).move_to(x=end_x, y=end_y).release().perform()
