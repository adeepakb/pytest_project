"""It contains all common elements and functionalities available to all pages."""
import datetime
import pytest
from PIL import Image, ImageChops
from math import sqrt
from subprocess import getoutput, Popen, PIPE, STDOUT
from datetime import datetime, timedelta
from time import sleep
from PIL import Image
from io import BytesIO
import cv2
import logging
import pytesseract
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException, \
    ElementNotSelectableException
from appium.webdriver.common.mobileby import MobileBy
from constants.load_json import get_data
from utilities.exceptions import DeviceUnavailableException, ConnectionTimeoutError, DateError
from utilities.return_type import ReturnType


class TutorCommonMethods:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def _by(locator_type):
        attr = getattr(MobileBy, locator_type.upper())
        return attr

    def webdriver_wait(self, timeout):
        wait = WebDriverWait(self.driver, timeout)
        return wait

    def wait_for_locator(self, locator_type, locator_value, timeout=5):
        try:
            wait = self.webdriver_wait(timeout)
            wait.until(ec.presence_of_element_located((self._by(locator_type), locator_value)))
        except TimeoutException:
            pass

    def wait_for_invisibility_of_element(self, locator_type, locator_value, timeout=20):
        wait = self.webdriver_wait(timeout)
        wait.until(ec.invisibility_of_element_located((self._by(locator_type), locator_value)))

    @staticmethod
    def wait_for_alert(driver, sec):
        wait = WebDriverWait(driver, sec)
        wait.until(ec.alert_is_present)
        alert = driver.switch_to().alert()
        return alert

    def wait_for_clickable(self, driver, locator_type, locator_value, sec=2):
        wait = WebDriverWait(driver, sec)
        wait.until(ec.element_to_be_clickable((self._by(locator_type), locator_value)))

    def fluent_wait(self, locator_type, locator_value):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(ec.presence_of_element_located((self._by(locator_type), locator_value)))

    @staticmethod
    def execute_command(command):
        sub = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT)
        return sub.communicate()

    def take_screen_shot(self, feature_filename):
        screen_shot = datetime.now()
        file_name = screen_shot.strftime("%d-%m-%y, %H-%M-%S")
        self.driver.get_screenshot_as_file("../../ScreenShots/" + feature_filename + " " + file_name + ".png")

    def get_element(self, locator_type, locator_value, wait=True):
        if locator_type.lower() != 'image' and wait:
            self.wait_for_locator(locator_type, locator_value)
        element = self.driver.find_element(self._by(locator_type), locator_value)
        return element

    def get_elements(self, locator_type, locator_value):
        elements = self.driver.find_elements(self._by(locator_type), locator_value)
        return elements

    # this method is use to click on the element
    def element_click(self, locator_type=None, locator_value=None, element=None):
        if element is None:
            element = self.get_element(locator_type, locator_value)
        try:
            element.click()
        except NoSuchElementException:
            logging.info("Cannot click on the element with locator: " + locator_value)

        # this method is use to click on the element

    @staticmethod
    def child_element_by_id(element, id_locator_value):
        return element.find_element_by_id(id_locator_value)

    @staticmethod
    def child_element_click_by_id(element, id_locator_value):
        element.find_element_by_id(id_locator_value).click()

    @staticmethod
    def child_element_text(element, id_locator_value):
        return element.find_element_by_id(id_locator_value).text

    @staticmethod
    def child_element_displayed(element, id_locator_value):
        return element.find_element_by_id(id_locator_value).is_displayed()

    def clear_app_data(self):
        self.execute_command('adb shell pm clear %s' % self.package_name)

    def clear_app_data_and_relaunch_the_app(self):
        try:
            self.clear_app_data()
            self.execute_command('adb shell monkey -p %s -c android.intent.category.LAUNCHER 1' % self.package_name)
            return ReturnType(True, "App data not cleared")
        except:
            return ReturnType(False,"App data not cleared")


    # this method first clear the data then enter the text in given element
    def enter_text(self, data, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.clear()
        element.send_keys(data)

    # this method is use to clear the data
    def clear_data(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.clear()

    def is_text_match(self, expected_text):
        locator_type = 'xpath'
        locator_value = "//android.widget.TextView"
        self.wait_for_locator(locator_type, locator_value, 15)
        list_of_elements = self.get_elements(locator_type, locator_value)
        for element in range(len(list_of_elements)):
            actual_text = list_of_elements[element].text
            if actual_text == expected_text:
                return True
        return False

    def is_button_displayed_with_text(self, expected_text):
        locator_type = 'xpath'
        locator_value = "//android.widget.Button"
        list_of_elements = self.get_elements(locator_type, locator_value)
        for element in range(len(list_of_elements)):
            actual_text = list_of_elements[element].text
            if expected_text == actual_text:
                return True
        return False

    def button_click(self, expected_text):
        locator_type = 'xpath'
        locator_value = "//android.widget.Button"
        list_of_elements = self.get_elements(locator_type, locator_value)
        try:
            for element in range(len(list_of_elements)):
                actual_text = list_of_elements[element].text
                if expected_text == actual_text:
                    list_of_elements[element].click()
                    break
        except NoSuchElementException:
            logging.info("Cannot click on the element with locator: " + locator_value)

    def is_button_enabled(self, expected_text):
        locator_type = 'xpath'
        locator_value = "//android.widget.Button"
        list_of_elements = self.get_elements(locator_type, locator_value)
        enabled_flag = False
        for element in range(len(list_of_elements)):
            actual_text = list_of_elements[element].text
            if expected_text == actual_text:
                print(list_of_elements[element].get_attribute("clickable"))
                enabled_flag = list_of_elements[element].is_enabled()
                break
        return enabled_flag

    # Find prominent color from cropped screenshot
    # provide rgb color code
    # provide index = 1 for text element, as background color will be the prominent color
    # provide index = 0 for color filled element which has no background color
    def verify_element_color(self, locator_type=None, locator_value=None, rgb_color_code=None, index=None,
                             element=None):
        if type(rgb_color_code) is str:
            target_color = tuple(map(int, rgb_color_code[1:-1].split(', ')))
        elif type(rgb_color_code) is list:
            target_color = tuple(rgb_color_code)
        elif type(rgb_color_code) is tuple:
            target_color = rgb_color_code
        else:
            raise TypeError(f"Argument 'rgb_color_code' cannot be {type(rgb_color_code).__name__} type.")
        if not element:
            element = self.get_element(locator_type, locator_value)
        location = element.location
        size = element.size
        png = self.driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        colors = im.getcolors(10000)
        colors.sort(key=lambda x: x[0], reverse=True)
        foreground_color = colors[index][1]
        print("Text color : %s" % (foreground_color,))
        match = self.root_mean_square_error(foreground_color, target_color)
        print(match)
        assert (match < 15), "Text color is not as expected"
        im.save('screenshot.png')

    @staticmethod
    def root_mean_square_error(rgb1, rgb2):
        sumof = (rgb1[0] - rgb2[0]) ** 2 + (rgb1[1] - rgb2[1]) ** 2 + (rgb1[2] - rgb2[2]) ** 2
        return sqrt(sumof / 3)

    def is_link_displayed(self, text):
        locator_type = 'xpath'
        locator_value = "//android.widget.TextView"
        self.wait_for_locator(locator_type, locator_value, timeout=30)
        list_of_elements = self.get_elements(locator_type, locator_value)
        for element in range(len(list_of_elements)):
            text2 = list_of_elements[element].text
            if text2 == text:
                list_of_elements[element].get_attribute("clickable")
                list_of_elements[element].is_enabled()
                return True
        return False

    def click_link(self, text):
        locator_type = 'xpath'
        locator_value = "//android.widget.TextView"
        list_of_elements = self.get_elements(locator_type, locator_value)
        for element in range(len(list_of_elements)):
            text2 = list_of_elements[element].text
            if text2 == text:
                attribute = list_of_elements[element].get_attribute("clickable")
                logging.info(attribute)
                list_of_elements[element].is_enabled()
                list_of_elements[element].click()
                break

    def scroll_to_element(self, text):
        try:
            loc_0 = "new UiScrollable(new UiSelector().scrollable(true))"
            loc_1 = ".scrollIntoView(new UiSelector().text(\"" + text + "\"))"
            element = self.driver.find_element_by_android_uiautomator(loc_0 + loc_1)
            return element
        except NoSuchElementException:
            logging.info("Given " + text + " isCorrect or not Present in the dropdown List")
            return False

    def is_scrolled_and_element_clicked(self, text):
        web_ele = self.scroll_to_element(text)
        if web_ele:
            try:
                self.element_click(element=web_ele)
                return True
            except NoSuchElementException:
                return False
        else:
            return web_ele

    # this method is use to check element is present or not if yes it will return True else False
    def is_element_present(self, locator_type, locator_value):
        try:
            self.wait_for_locator(locator_type, locator_value, 10)
            element = self.get_element(locator_type, locator_value)
            if element is not None:
                return True
            else:
                logging.info("Element not found")
                return False
        except (NoSuchElementException, TimeoutException):
            return False

    # this method is use to hide the visible keyboard from device
    def hide_keyboard(self):
        return self.driver.hide_keyboard()

    # this method is use to fetch the text from an element
    def get_element_text(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        if element is not None:
            element_txt = element.text
            return element_txt
        else:
            logging.error('Element text is Not Present')
            return str()

    def get_element_attr(self, data, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        if element is not None:
            element_txt = element.get_attribute(data)
            return element_txt
        else:
            logging.error('Element attribute is Not Present')
            return str()

    # this method is use to check text is present or not
    def is_text_displayed(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value).text
        if element is not None:
            return True
        else:
            logging.error('Element text is Not Present')
            return False

    # this method is use to check keyword is present or not
    def is_keyboard_shown(self):
        check = self.driver.is_keyboard_shown()
        if check:
            return True
        else:
            logging.error('Failed To show the Keyboard Screen')
            return False

    # this method is use to click on device back button
    def click_back(self):
        self.driver.back()

    def get_current_package(self):
        package = self.driver.current_package
        return package

    # this method is use to click on device home button
    def click_on_device_btn(self, text):
        if text == 'HomeButton':
            self.execute_command('adb shell input keyevent KEYCODE_HOME')
            return True
        else:
            return False

    def take_app_foreground(self, app_package):
        self.driver.activate_app(app_package)
        return True

    def query_app_state(self, text):
        check = self.driver.query_app_state(text)
        return check

    def toggle_wifi_connection(self, text):
        _status = getoutput('adb devices')
        wifi_state = "adb shell settings get global wifi_on"
        wifi_on = 2
        wifi_off = 0
        _t = timeout = 30
        mask = self.driver.mobile.network_connection.mask
        if "no devices" in _status:
            raise DeviceUnavailableException(_status)
        elif text == 'off' and (mask // 2) % 2 > 0:
            self.driver.mobile.set_network_connection(wifi_off)
            while int(getoutput(wifi_state)):
                if not _t:
                    raise ConnectionTimeoutError(timeout)
                sleep(1)
                _t -= 1
            else:
                while "Network is unreachable" not in getoutput("adb shell ping -c 1 8.8.8.8"):
                    if not _t:
                        raise ConnectionTimeoutError(timeout)
                    sleep(1)
                    _t -= 1
                else:
                    return True
        elif text == 'on' and (mask // 2) % 2 == 0:
            self.driver.mobile.set_network_connection(wifi_on)
            while not int(getoutput(wifi_state)):
                if not _t:
                    raise ConnectionTimeoutError(timeout)
                sleep(1)
                _t -= 1
            else:
                while "Network is unreachable" in getoutput("adb shell ping -c 1 8.8.8.8"):
                    if not _t:
                        raise ConnectionTimeoutError(timeout)
                    sleep(1)
                    _t -= 1
                else:
                    return True
        else:
            logging.info("WIFI-STATUS: %s" % text.upper())
            return False

    # capture partial screenshot of element
    def capture_screenshot(self, element, image_file_name):
        location = element.location
        size = element.size
        png = self.driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        im.save(image_file_name + '.png')

    # shape detection using opencv
    def detect_shapes(self, element):
        self.capture_screenshot(element, 'shapes')
        shapes_list = []
        # Load the image
        img = cv2.imread('shapes.png')
        # Convert to greyscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Convert to binary image by thresholding
        _, threshold = cv2.threshold(img_gray, 245, 255, cv2.THRESH_BINARY_INV)
        # Find the contours
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # For each contour approximate the curve and
        # detect the shapes.
        for contour in contours:
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5
            # approx is the number of edges that particular shape has
            if len(approx) == 3:
                shapes_list.append("triangle")
            elif len(approx) == 4:
                x1, y1, w, h = cv2.boundingRect(approx)
                aspect_ratio = float(w) / h
                if 0.95 <= aspect_ratio <= 1.05:
                    shapes_list.append("square")
                else:
                    shapes_list.append("rectangle")
            elif len(approx) == 5:
                shapes_list.append("pentagon")
            elif len(approx) == 10:
                shapes_list.append("star")
            else:
                shapes_list.append("circle")

        print(shapes_list)
        return shapes_list

    # get text from image file
    @staticmethod
    def get_text_from_image(imagefilename):
        img = cv2.imread(imagefilename + '.png')
        text = pytesseract.image_to_string(img)
        return text

    # This method takes cropped screenshot and return all the colors present w.r.t provided webelement
    def get_all_colors_present(self, locator_type=None, locator_value=None, element=None):
        if not element:
            element = self.get_element(locator_type, locator_value)
        location = element.location
        size = element.size
        png = self.driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        colors = im.getcolors(100000)
        colors.sort(key=lambda x: x[0], reverse=True)
        print(colors)
        im.save('screenshot.png')
        return colors

    def clear_app_from_recents(self):
        self.execute_command('adb shell input keyevent KEYCODE_APP_SWITCH')
        screen_size = self.driver.get_window_size()
        orientation = self.driver.orientation
        if orientation == "LANDSCAPE":
            x, y = screen_size['height'], screen_size['width']
        else:
            x, y = screen_size['width'], screen_size['height']
        start_x, start_y = x // 2, y // 2
        end_x, end_y = start_x, 5
        self.driver.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y, duration=3000)

    def get_device_type(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        dp = self.driver.get_display_density()
        diagonal = (sqrt(width ** 2 + height ** 2)) / dp
        if diagonal >= 10:
            return 'tab'
        else:
            return 'mobile'

    def wait_activity(self, activity_name, timeout=30):
        while timeout:
            c_a = self.driver.current_activity.split('.')[-1]
            if activity_name == c_a:
                return True
            else:
                sleep(1)
                timeout -= 1
        return False

    @staticmethod
    def is_holiday(day=datetime.today()):
        h_days = get_data('../../config/holidays.json', 'local')
        c_date = day.strftime("%m/%d/%Y")
        if c_date in h_days:
            return True
        return False

    def get_working_days(self, days):
        d_list = list()
        i = 0
        while len(d_list) < days:
            if not self.is_holiday(datetime.now() + timedelta(i)):
                day = datetime.now() + timedelta(i)
                d_list.append(day)
            i += 1
        return d_list

    @staticmethod
    def compare_images(image1, image2):
        im1 = Image.open(image1)
        im2 = Image.open(image2)
        diff = ImageChops.difference(im1, im2).getbbox()
        return diff

    def takeScreenShot(self, featureFileName):
        screenShot = datetime.datetime.now()
        fileName = screenShot.strftime("%d-%m-%y, %H-%M-%S")
        self.driver.get_screenshot_as_file('''../../ScreenShots/''' + featureFileName + " " + fileName + ".png")

    def noSuchEleExcept(self, featureFileName, methodName):
        logging.error("Failed Locator in Method" + methodName)
        self.takeScreenShot(featureFileName)
        pytest.fail("Failed Due to Locator in")

    def exception(self, featureFileName, methodName):
        logging.error('Failed due to Exception in Method ' + methodName)
        self.takeScreenShot(featureFileName)
        pytest.fail("Failed Due to Exception in")


class InValidLocatorError(Exception):
    pass
