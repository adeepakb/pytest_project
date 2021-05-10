import datetime
import random
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from utilities.tutor_common_methods import TutorCommonMethods


class DropDownSelect(TutorCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.action = TouchAction(driver)
        self.dropdown_icon = '//*[contains(@resource-id, "spinnerMonth")]'
        self.dropdown_list = '//*[contains(@resource-id,"month_item_view_group")]'
        self.dropdown_list_text = self.dropdown_list + '/android.widget.TextView'

    def select_dropdown(self):
        month_dropdown = self.get_element('xpath', self.dropdown_icon)
        month_dropdown.click()

    def select_month(self, index):
        months_list = self.get_elements('xpath', self.dropdown_list)
        months_list[index].click()

    def is_dropdown_icon_displayed(self):
        try:
            icon_val = self.get_element('xpath', self.dropdown_icon).is_displayed()
            return icon_val
        except NoSuchElementException:
            return False

    def is_dropdown_list_displayed(self):
        try:
            icon_val = self.get_element('xpath', self.dropdown_list).is_displayed()
            return icon_val
        except NoSuchElementException:
            return False

    @staticmethod
    def generate_month_year_list(start, duration):
        exp_list = list()
        d = datetime.datetime.strptime(start, "%B '%y")
        start_values = d.strftime('%m %y').split()
        start_month, start_year = int(start_values[0]), int(start_values[1])
        for i in range(duration):
            if start_month == 13:
                start_year += 1
                start_month = 1
            dd = datetime.datetime.strptime(str(start_month) + " " + str(start_year), '%m %y')
            exp_list.append(dd.strftime("%B '%y"))
            start_month += 1
        return exp_list

    def is_month_list_sorted(self):
        months_list = self.get_elements('xpath', self.dropdown_list_text)
        expected_list = self.generate_month_year_list(months_list[0].text, len(months_list))
        actual_list = [_.text for _ in months_list]
        if expected_list == actual_list:
            return True
        return False

    def is_current_month_highlighted(self):
        displayed_month_year = self.get_element('xpath', '//*[contains(@resource-id,"month_item_name_view")]').text
        current_month_year = datetime.datetime.now().strftime("%B '%y")
        if displayed_month_year == current_month_year:
            return True
        return False

    def is_respective_details_displayed(self):
        self.select_month(random.randint(0, 12))
        session_month_header = self.get_element('xpath', '//*[contains(@resource-id, "month_header")]').text
        displayed_month_year = self.get_element('xpath', '//*[contains(@resource-id,"month_item_name_view")]').text
        time_details = self.get_elements('xpath', '//*[contains(@resource-id, "SessionScheduleTime")]')
        d = datetime.datetime.strptime(displayed_month_year, "%B '%y")
        details_month_short = d.strftime("%b")
        all_details = list(details_month_short in _.text for _ in time_details)
        if displayed_month_year in session_month_header and all(all_details) and len(time_details) == len(all_details):
            return True
        return False

    def is_drop_down_displayed(self):
        timeout = 10
        self.select_dropdown()
        list_displayed = self.get_element('xpath', '//android.widget.ListView').is_displayed()
        if list_displayed:
            self.action.tap(x=random.randint(100, 750), y=random.randint(25, 500)).perform()
        while timeout:
            timeout -= 2
            try:
                self.get_element('xpath', '//android.widget.ListView')
                return True
            except NoSuchElementException:
                return False
