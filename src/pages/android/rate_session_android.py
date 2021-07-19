import time
import pytest
from appium.webdriver.common.touch_action import TouchAction
from pages.base.rate_session_base import RateSessionBase
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.session_completed import SessionComplete
from pages.android.session_data import SessionData
from pages.android.login_android import LoginAndroid
from pages.android.scroll_cards import ScrollCards
from utilities.common_methods import CommonMethods
import re
import pytest_check as check

CommonMethods = CommonMethods()


class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class Dashboard(RateSessionBase):
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.sessioncomplete = SessionComplete(driver)
        self.sessiondata = SessionData(driver)
        self.action = TouchAction(driver)
        self.login = LoginAndroid(driver)
        self.scrollcards = ScrollCards(driver)
        self.driver = driver
        self.card = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/card"]'
        self.rate_session_link = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/tvRateSessionLink"]'
        self.completed_badge = '//*[contains(@resource-id,"sessionCompleted")]'
        self.rate_session_button = '//*[contains(@resource-id,"actionCardButton")]'
        self.rate_session_mobile = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/ivActionMobile"]'
        self.rate_session_close_button = '//*[contains(@resource-id,"feedback_session_close_icon")]'
        self.feedback_rating_bar = '//*[@class= "android.widget.RatingBar"]'
        self.submitted_rating_bar = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/ratingTv"]'
        self.data_off_icon = '//*[@resource-id="com.byjus.thelearningapp.premium:id/imageView"]'
        self.back_nav = '//*[@resource-id="com.byjus.thelearningapp.premium:id/roundedNavButton"]'
        self.feedback_options = '//*[@resource-id="com.byjus.thelearningapp.premium:id/tvFeedback"]'
        self.feedback_options_checkbox = '//*[@resource-id="com.byjus.thelearningapp.premium:id/ivCheckBox"]'
        self.submit_rate_session = '//*[@resource-id="com.byjus.thelearningapp.premium:id/btnSubmit"]'
        self.session_end_okay_button = 'com.byjus.thelearningapp.premium:id/primaryAction'
        self.join_now = 'com.byjus.thelearningapp.premium:id/btnAction'
        self.session_subject = 'com.byjus.thelearningapp.premium:id/subject_name'

    def tap_on_tab(self, text):
        self.obj.get_element('xpath',
                             '//android.widget.LinearLayout[@content-desc="' + text + '"]/android.widget.TextView').click()

    def verify_feedback_and_checkbox_present(self, value, i):
        index = int(i) - 1
        self.obj.wait_for_locator('xpath', self.feedback_options)
        feedback_option = self.obj.get_elements('xpath', self.feedback_options)
        assert (feedback_option[index].text == value), "verify feedback option is present failed"

        self.obj.wait_for_locator('xpath', self.feedback_options_checkbox)
        feedback_options_checkbox_item = self.obj.get_elements('xpath', self.feedback_options_checkbox)
        print(feedback_options_checkbox_item[index].is_enabled())
        assert (feedback_options_checkbox_item[
                    index].is_enabled() is True), "verify feedback option checkox is present failed"

    def tap_on_okay_button(self):
        self.obj.wait_for_locator('id', self.session_end_okay_button)
        self.obj.get_element('id', self.session_end_okay_button).click()

    def tap_on_star(self, rating):
        bar = self.driver.find_element_by_xpath(self.feedback_rating_bar)
        start_x = bar.location['x']
        end_x = bar.size['width']
        height = bar.size['height']
        y_axis = bar.location['y'] + (height * 0.1)
        tapAt = start_x + (end_x * 0.1) * (rating*2-1)
        self.action.press(x=tapAt, y= y_axis).release().perform()

    def text_match(self, expected_text):
        text_matches = self.obj.is_text_match(expected_text)
        if text_matches is True:
            return ReturnType(True, '%s text is displayed' % expected_text)
        return ReturnType(False, '%s text is not displayed' % expected_text)

    def verify_button(self, text):
        if self.obj.is_button_displayed(text):
            return ReturnType(True, '%s button is displayed' % text)
        else:
            return ReturnType(False, '%s button is not displayed' % text)

    def tap_on_join_now(self):
        self.obj.wait_for_locator('id', self.join_now)
        self.obj.get_element('id', self.join_now).click()

    def verify_color_of_completed_status(self, rgb_color_code):
        self.obj.verify_element_color('xpath', self.completed_badge, rgb_color_code, 1)

    def tap_rate_session_button(self):
        device = CommonMethods.get_device_type(self.driver)
        if device == 'tab':
            self.obj.element_click('xpath', self.rate_session_button)
        elif device == 'mobile':
            self.obj.element_click('xpath', self.rate_session_mobile)

    def verify_star_rating(self, locator, rating):
        self.obj.wait_for_locator('xpath', locator)
        feedback_rating_bar = self.driver.find_element_by_xpath(locator).text
        assert (feedback_rating_bar == rating), "Verify %s selected stars in rate session card failed" % rating

    def tap_on_first_session_card(self):
        session_cards_list = self.obj.get_elements('id', self.session_subject)
        card = session_cards_list[0]
        card.click()

    def verify_rate_session_close_button(self):
        if self.obj.is_element_present("xpath", self.rate_session_close_button):
            return ReturnType(True, 'Cancel button is present')
        else:
            return ReturnType(False, 'Cancel button is not present')

    def tap_rate_session_close_button(self):
        self.obj.element_click("xpath", self.rate_session_close_button)

    def click_link(self, text):
        self.obj.click_link(text)

    def back_navigation(self):
        self.obj.element_click("xpath", self.back_nav)

    def click_back(self):
        self.obj.click_back()

    def tap_on_each_star_and_verify(self):
        for i in range(1, 5):
            self.tap_on_star(i)
            self.verify_star_rating(self.feedback_rating_bar, str(i) + '.0')

    def deselect_selected_stars_and_verify(self):
        for i in range(5, 1):
            self.tap_on_star(i)
            self.verify_star_rating(self.feedback_rating_bar, str(i) + '.0')

    def tap_on_submit_button(self):
        self.obj.element_click("xpath", self.submit_rate_session)

    def verify_rating_on_session_details_screen(self, rating):
        CommonMethods.scrollToElement(self.driver, "Your Rating")
        self.verify_star_rating(self.submitted_rating_bar, rating)

    def get_rated_session_card(self, index):
        session_cards_list = self.obj.get_elements('xpath', self.card)
        rated_card = session_cards_list[index]
        rating = self.sessiondata.get_sessions_ratings(rated_card)
        return rating

    def verify_rating_on_session_card(self, index, expected_rating):
        rating = self.get_rated_session_card(index)
        assert (rating == expected_rating), "Verify %s selected stars in rate session card failed" % rating

    def verify_submit_button_enabled_or_not(self, text, expected_flag):
        if expected_flag is True:
            assert self.obj.is_button_enabled(text) is True, "Submit button is disabled"
        else:
            assert self.obj.is_button_enabled(text) is False, "Submit button is not disabled"

    def is_data_off_icon_displayed(self):
        data_off_icon_displayed = self.obj.get_element('xpath', self.data_off_icon).is_displayed()
        is_enabled = self.obj.get_element('xpath', self.data_off_icon).is_enabled()
        if data_off_icon_displayed and is_enabled:
            return ReturnType(True, 'Data off icon is present')
        return ReturnType(False, 'Data off icon is not present')

    def tap_on_each_star_and_verify_feedback(self):
        for i in range(1, 5):
            self.tap_on_star(i)
            self.verify_feedback_options(str(i) + '.0')
            feedback_options_checkbox_item = self.obj.get_elements('xpath', self.feedback_options_checkbox)
            feedback_options_checkbox_item[i].click()
            time.sleep(2)
            assert (feedback_options_checkbox_item[i].get_attribute(
                "checked") == 'true'), "verify able to select the feedback options failed"
            feedback_options_checkbox_item[i].click()
            time.sleep(2)
            assert (feedback_options_checkbox_item[i].get_attribute(
                "checked") == 'false'), "verify able to deselect the feedback options failed"

    def verify_feedback_options(self, rating):
        self.obj.wait_for_locator('xpath', self.feedback_options)
        assert self.obj.get_element('xpath',
                                    self.feedback_options).is_displayed(), "Verify for %s selected stars feedback options not displayed" % rating
        items = ["Teaching Technique", "Solution Provided", "Tutor's Behaviour", "Call Quality", "Video Quality"]
        feedback_options_checkbox_items = self.obj.get_elements('xpath', self.feedback_options_checkbox)
        for i in range(0, 5):
            feedback_options_checkbox_item_text = feedback_options_checkbox_items[i].text
            assert (feedback_options_checkbox_item_text == items[
                i]), "Verify all feedback options not displayed for %s selected stars" % rating

    def verify_select_deselect_feedback_options(self):
        self.obj.wait_for_locator('xpath', self.feedback_options_checkbox)
        feedback_options_checkbox_item = self.obj.get_elements('xpath', self.feedback_options_checkbox)
        for i in range(0, 5):
            feedback_options_checkbox_item[i].click()
            time.sleep(3)
            assert (feedback_options_checkbox_item[i].get_attribute(
                "checked") == 'true'), "verify able to select the feedback options failed"
        for i in range(0, 5):
            feedback_options_checkbox_item[i].click()
            time.sleep(3)
            assert (feedback_options_checkbox_item[i].get_attribute(
                "checked") == 'false'), "verify able to deselect the feedback options failed "

    def select_any_feedback(self):
        self.obj.wait_for_locator('xpath', self.feedback_options_checkbox)
        feedback_options_checkbox_items = self.obj.get_elements('xpath', self.feedback_options_checkbox)
        feedback_options_checkbox_items[0].click()

    def find_completed_notrated_session(self):
        flag = False
        while True:
            i = 0
            session_cards_list = self.obj.get_elements('xpath', self.card)
            while i < 5:
                rating = self.sessiondata.is_rate_session_link_present(session_cards_list[i])
                if rating == 'Not rated':
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
                pytest.skip("No unrated sessions present")
        return i

    def verify_rate_session_link_is_present(self, text):
        assert self.obj.is_link_displayed(text) is True, "Rate Session link is not present"

    def verify_rate_session_details(self, session_details_dict):
        subject_name = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "subjectName")]').text
        topic_name = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "chapterName")]').text
        session_date = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "sessionDatetv")]').text
        session_time = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "sessionTimetv")]').text

        self.obj.is_text_match("Let us know how your experience was!")
        self.verify_star_rating(self.feedback_rating_bar, '0.0')
        # m = re.match("[0-3][0-9] ([A-Z]{1}[a-z]{2}), ([A-Z]{1}([a-z]{8}|[a-z]{7}|[a-z]{6}|[a-z]{5}))|[A-Z]{1}[a-z]{4}", session_date)
        m = re.match("[0-3][0-9] (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec), (Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)|(Today)",
            session_date)
        check.equal(m is not None, True, "Session date is not in DD MMM,DAY format")

        self.obj.is_text_match("Not attended")
        self.obj.is_button_displayed("Submit")

        rating_card_details_dict = {"Subject": subject_name.strip(),
                                    "Topic": topic_name.strip(),
                                    "Schedule Date": session_date.strip(),
                                    "Schedule Time": session_time.strip()}

        item_found_count= None
        for key, value in rating_card_details_dict.items():
            expected_value = session_details_dict[key]
            if expected_value in value:
                item_found_count = +1
        if item_found_count == 4:
            return ReturnType(True, "Values in rate session card is matching with session card details")
        else:
            return ReturnType(False, "Values in rate session card is not matching with session card details")
