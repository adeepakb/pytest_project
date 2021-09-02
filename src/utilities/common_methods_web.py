import pytest
from io import BytesIO
import cv2
import pytesseract
import logging
from PIL import Image
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException, \
    ElementNotSelectableException

class CommonMethodsWeb():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            logging.info("Locator type " + locatorType + " not correct/supported")
        return False

    # this methos is use to get the address of the element
    def get_element(self, locator):
        locatorType = locator[0]
        locatorValue = locator[1]
        element = None
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        element = self.driver.find_element(byType, locatorValue)
        return element

    # this method is use to click on the element
    def elementClick(self, locator):
        try:
            element = self.get_element(locator)
            if element is not None:
                element.click()
                return True
            else:
                logging.info(locator + 'Not clicked')
                return False
        except:
            logging.info("Cannot click on the element with locator: " + locator)
            return False

    # this method first clear the data then enter the text in given element
    def enterText(self, data, locator):
        try:
            element = self.get_element(locator)
            element.clear()
            element.send_keys(data)
            return True
        except:
            logging.info("Cannot send data on the element with locator: ")
            return False

    def button_click(self, text):

        ele = self.driver.find_element("xpath", "//*[text()='+text']")
        ele.click()

    def wait(self, sec):

        self.driver.implicitly_wait(sec)

    def get_elements(self, locator):
        elements = []
        locatorType = locator[0]
        locatorValue = locator[1]
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        elements.extend(self.driver.find_elements(byType, locatorValue))
        return elements

    # this method is use to check element is present or not if yes it will return True else False
    def is_element_present(self, locator):
        try:
            element = self.get_element(locator)
            if element is not None:
                return True
            else:
                logging.info("Element not found")
                return False
        except (NoSuchElementException):
            return False

    def get_web_elements(self, locator_type, locator_value):
        elements = self.driver.find_elements(self._by(locator_type), locator_value)
        return elements

    @staticmethod
    def _by(locator_type):
        attr = getattr(By, locator_type)
        return attr

    def webdriver_wait(self, timeout):
        wait = WebDriverWait(self.driver, timeout)
        return wait

    def wait_for_locator(self, locator, timeout=5):
        try:
            wait = self.webdriver_wait(timeout)
            wait.until(ec.presence_of_element_located((self._by(locator))))
        except TimeoutException:
            pass

    def child_element_text(self, element, locator):
        return element.find_element_by_xpath(locator).text

    def get_child_element(self,element,locator_type, locator_value):
        return element.find_element(locator_type,locator_value)

    def get_child_elements(self, element, locator_type, locator_value):
        return element.find_elements(locator_type, locator_value)

    def wait_for_element_visible(self, driver, locator, timeout=30):
        try:
            wait = WebDriverWait(driver, timeout)
            wait.until(ec.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_for_locator_webdriver(self, locator_value, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_clickable_element_webdriver(self, locator_value, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def get_elment(self, locator_type, locator_value, wait=False):
        self.wait_for_locator(locator_type, locator_value)
        element = self.driver.find_element(self._by(locator_type), locator_value)
        return element

# this method is use to check element is present or not if yes it will return True else False
    def is_element_displayed(self, locator_type, locator_value):
        try:
            element = self.get_elment(locator_type, locator_value)
            if element is not None:
                return True
            else:
                logging.info("Element not found")
                return False
        except (NoSuchElementException, TimeoutException):
            return False

 # this method is use to click on the element
    def click_element(self, locator_type=None, locator_value=None, element=None):
        if element is None:
            element = self.get_elment(locator_type, locator_value)
        try:
            element.click()
        except NoSuchElementException:
            logging.info("Cannot click on the element with locator: " + locator_value)

    # get text from image file
    @staticmethod
    def get_text_from_image(imagefilename):
        img = cv2.imread(imagefilename + '.png')
        text = pytesseract.image_to_string(img, lang='eng')
        return text

    # shape detection using opencv
    @staticmethod
    def detect_shapes(element):
        png = element.screenshot_as_png
        im = Image.open(BytesIO(png))
        im.save('shapes.png')
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

    def move_focus_to_element(driver, element_to_hover_over):
        try:
            hover = ActionChains(driver).move_to_element(element_to_hover_over)
            hover.perform()
        except NoSuchElementException:
            logging.info("Hover operation failed.")