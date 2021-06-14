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
        self.result = result
        self.reason = reason


class KnowMoreTest(KnowMoreTestBase, TutorCommonMethods):
    def __init__(self, driver):
        self.driver = driver
        self.Hamburg = Hamburger(driver)
        self.ScrollCards = ScrollCards(driver)
        package_name = self.driver.desired_capabilities['appPackage'] + ':id'
        self.hamburger_icon = "id", "%s/roundedNavButton" % package_name
        self.byjus_classes = "id", "com.byjus.thelearningapp.premium:id/home_drawer_list_item_txtvw"
        self.know_more = "id", "%s/home_drawer_list_item_txtvw_new" % package_name
        self.confirm_and_book = "id", "%s/primaryAction" % package_name
        self.booking_page_dropdown = "id", "%s/ivChevron" % package_name
        self.bs_header_title = 'id', '%s/tvHeaderTittle' % package_name
        self.booking_times = 'id', '%s/toggleButtonsGroup' % package_name
        self.booked_screen_title = 'id', '%s/appTextView_title' % package_name
        self.booked_screen_time = 'id', '%s/appTextViewTime' % package_name
        self.booked_screen_ok = 'id', '%s/appButtonCtaOk' % package_name

    def click_on_hamburger(self):
        try:
            self.element_click(*self.hamburger_icon)
            return ReturnType(True, "clicked on Hamburger")
        except:
            return ReturnType(False, "Could not click on Hamburger")

    def verify_know_more_displayed(self):
        return_type = ReturnType(False, "")
        if self.is_element_present(*self.byjus_classes) and self.is_element_present(*self.know_more):
            return ReturnType(True, "Know more is being displayed in Hamburger")
        else:
            return ReturnType(False, "Know more is being displayed in Hamburger")

    def tap_on_byjus_classes_in_hamburger(self, button='Know More'):
        button_element = None
        if button == 'Know More':
            button_element = self.know_more
        else:
            button_element = self.byjus_classes

        try:
            if self.verify_know_more_displayed().result:
                self.element_click(*button_element)
            else:
                self.click_on_hamburger()
                self.element_click(*button_element)
            return ReturnType(True, "Clicked on Byjus classes homepage hamburger")
        except:
            return ReturnType(False, "Could not click on Byjus classes homepage hamburger")

    def validate_know_more(self):
        activityname = 'PremiumSchoolInfoActivity'
        if activityname in self.driver.current_activity:
            self.click_back()
            self.click_on_hamburger()
        try:
            self.tap_on_byjus_classes_in_hamburger()
            return ReturnType(True, "Byjus classes know more is responsive")
        except:
            return ReturnType(False, "Byjus classes know more is not responsive")

    def validate_webview_activity(self):
        activityname = 'PremiumSchoolInfoActivity'

        if activityname in self.driver.current_activity:
            return True
        else:
            return False

    def validate_know_more_webview(self):

        return_type = self.validate_webview_without_details()
        if self.is_desired_text_displayed("Why choose BYJU'S Classes?"):
            return_type.result = return_type.result and True
        else:
            return ReturnType(False, "Why choose BYJU'S Classes? is not being displayed")
        self.scroll_to_text("Interactive online classes by India's top teachers")
        if self.is_desired_text_displayed("Interactive online classes by India's top teachers"):
            return_type.result = return_type.result and True
        else:
            return ReturnType(False, "Interactive online classes by India's top teachers is not being displayed")
        self.scroll_to_text("Dedicated mentors to guide students")
        if self.is_desired_text_displayed("Dedicated mentors to guide students"):
            return_type.result = return_type.result and True
        else:
            return ReturnType(False, "Dedicated mentors to guide students is not being displayed")

        return return_type

    def validate_webview_without_details(self):
        return_type = ReturnType(False, "")
        if self.validate_webview_activity() is True:
            return_type.result = True
        else:
            return ReturnType(False, "Not in know more webview")

        if self.is_button_displayed_with_text("Book a Free Class") is True:
            return_type.result = True
            return_type.reason = "Book a free class button is shown"
        elif self.is_button_displayed_with_text("View class details") is True:
            return_type.result = True
            return_type.reason = "View class details button is shown"
        else:
            return ReturnType(False, "Book a free class button is not shown")
        return return_type

    def validate_book_a_free_class_card(self, text='Book a Free Class'):
        if self.is_button_displayed_with_text(text) is True:
            return ReturnType(True, "{} button is shown".format(text))
        else:
            return ReturnType(False, "{} button is not shown".format(text))

    def tap_on_book_card(self, text='Book a Free Class'):
        try:
            self.button_click(text)
            return ReturnType(True, "Found and clicked on {} Button".format(text))
        except:
            return ReturnType(False, "Not Found and not clicked on {} Button".format(text))

    def select_online_offline_mode(self, mode):
        try:
            set_connection_type(self.driver, mode)
            return ReturnType(True, "Network mode set to {}.".format(mode))
        except:
            return ReturnType(False, "Couldn't set network mode to {}.".format(mode))

    def verify_book_free_class_screen(self, expected_activity='PremiumSchoolCourseActivity'):
        time.sleep(3)
        if expected_activity in self.driver.current_activity:
            return ReturnType(True, " User is in Book a free class page {}".format(expected_activity))

        else:
            return ReturnType(False, " User is not in Book a free class page {}".format(expected_activity))

        return return_type

    def tap_on_book_button(self):
        try:
            self.is_scrolled_and_element_clicked("Book")

            if self.is_element_present(*self.booking_page_dropdown):
                ReturnType(True, "Book button found and booking page found")
            else:
                ReturnType(True, "Book button not found and booking page not found")
            return ReturnType(True, "Book button found")
        except:
            return ReturnType(False, "Book button not found")

        return return_type

    def book_a_session(self, **kwargs):
        db = kwargs['db']
        header_text = self.get_element(*self.bs_header_title).text
        selected_time = self.get_selected_time()
        if selected_time:
            db.selected_time = selected_time
        else:
            return ReturnType(False, " Time elements or booking screen not visible")
        try:
            self.element_click(*self.confirm_and_book)
            return ReturnType(True, "Clicked on confirm and book button on booking page")
        except:
            return ReturnType(False, "Couldn't click on confirm and book button on booking page")

    def get_selected_time(self):
        try:
            elements = self.get_elements(*self.booking_times)
            for element in elements:
                button_elements = element.find_elements_by_class_name("android.widget.TextView")
                for button_element in button_elements:
                    if button_element.is_selected():
                        return button_element.text
        except:
            return None

    def verify_and_close_booked_screen(self, **kwargs):
        db = kwargs['db']
        selected_time = db.selected_time
        check.equal(self.get_element(*self.booked_screen_title).text, "You Successfully Booked",
                    "Booked screen title is wrong")

        check.equal(selected_time in self.get_element(*self.booked_screen_time).text, True,
                    "Booked time is displayed correctly")
        try:
            self.get_element(*self.booked_screen_ok).click()
            return ReturnType(True, "Booked successfully and booking screen is verified")
        except:
            return ReturnType(False, "Couldn't book successfully and booking screen is not correct")

    def relaunch_app(self):
        try:
            self.driver.launch_app()
            return ReturnType(True, "Relaunch the application successful")
        except:
            return ReturnType(False, "Relaunch the application not successful")