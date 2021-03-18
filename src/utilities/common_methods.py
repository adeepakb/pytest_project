"""It contains all common elements and functionalities available to all pom_pages."""
import pytest
import os
import sys
from time import sleep
import datetime
import logging
import subprocess
from appium import webdriver
from selenium.webdriver import android
from math import sqrt
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class CommonMethods():
    #     def __init__(self, driver):
    #         self.driver = driver

    # this method is use to capture the screen shot

    def accept_notification(self, driver, locator):
        try:
            self.wait_for_locator(driver, locator, 5)
            self.elementClick(driver, locator)
        except:
            pass

    def wait_for_element_visible(self, driver, locator, sec):
        try:
            driver.implicitly_wait(0)
            wait = WebDriverWait(driver, sec)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_device_type(self, driver):
        list = []
        size = driver.get_window_size()
        width = size['width']
        height = size['height']
        dp = driver.get_display_density()
        diagonal = (sqrt(width ** 2 + height ** 2)) / dp
        print(diagonal)
        if diagonal > 7:
            return 'tab'
        else:
            return 'mobile'

    def click_on_Coordinate(self, x, y):
        self.run('adb shell input tap ' + x + ' ' + y)

    def click_none_of_the_above(self, driver, locator):
        try:
            self.wait_for_element_visible(driver, locator, 3)
            self.elementClick(driver, locator)
        except:
            pass

    def ConvertStringInToList(self, string):
        li = list(string.split(" "))
        return li

    def noSuchEleExcept(self, driver, featureFileName, methodName):
        logging.error("Failed Locator in Method" + methodName)
        self.takeScreenShot(driver, featureFileName)
        pytest.fail("Failed Due to Locator in")

    def exception(self, driver, featureFileName, methodName):
        logging.error('Failed due to Exception in Method ' + methodName)
        self.takeScreenShot(driver, featureFileName)
        pytest.fail("Failed Due to Exception in")

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

    def wait_for_locator(self, driver, locator, sec):
        #         locatorType = locator[0]
        #         locatorValue = locator[1]
        wait = WebDriverWait(driver, sec)
        #         wait.until(EC.presence_of_element_located((self.getByType(locatorType), locatorValue)))
        wait.until(EC.presence_of_element_located(locator), "Locator Not Found")

    def wait_for_alert(self, driver, sec):
        wait = WebDriverWait(driver, sec)
        wait.until(EC.alert_is_present)
        alert = driver.switch_to().alert()
        alert.cancel()

    def wait_for_clickable(self, driver, locator, sec):
        try:
            locatorType = locator[0]
            locator = locator[1]
            wait = WebDriverWait(driver, sec)
            wait.until(EC.element_to_be_clickable((self.getByType(locatorType), locator)))
            return True
        except:
            return False

    def run(self, command):
        sub = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return sub.communicate(5)

    def element_click_using_x_y(self, x, y):
        self.run('adb shell input tap {} {}'.format(x, y))

    def takeScreenShot(self, driver, featureFileName):
        screenShot = datetime.datetime.now()
        fileName = screenShot.strftime("%d-%m-%y, %H-%M-%S")
        driver.get_screenshot_as_file('''../../ScreenShots/''' + featureFileName + " " + fileName + ".png")

    # this methos is use to get the address of the element
    def getElement(self, driver, locator):
        locatorType = locator[0]
        locatorValue = locator[1]
        element = None
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        element = driver.find_element(byType, locatorValue)
        return element

    # this methos is use to get the address of the elements
    def getElements(self, driver, locator):
        elements = []
        locatorType = locator[0]
        locatorValue = locator[1]
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        #             elements = driver.find_elements(byType, locator)
        elements.extend(driver.find_elements(byType, locatorValue))

        #         except:
        #             logging.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return elements

    # this method is use to click on the element
    def elementClick(self, driver, locator):
        try:
            element = self.getElement(driver, locator)
            if element is not None:
                element.click()
                return True
            else:
                logging.info(locator + 'Not clicked')
                return False
        except:
            return False
            logging.info("Cannot click on the element with locator: " + locator)

    # this method first clear the data then enter the text in given element
    def enterText(self, driver, data, locator):
        try:
            element = self.getElement(driver, locator)
            element.clear()
            sleep(3)
            element.send_keys(data)
            return True

        except:
            logging.info("Cannot send data on the element with locator: ")
            return False

    # this method is use to clear the data
    def clearData(self, driver, locator):
        try:
            element = self.getElement(self, driver, locator)
            sleep(2)
            element.clear()
        except:
            logging.info("Cannot clear on the element with locator: ")

    #             logging.info("Cannot clear on the element with locator: " + locator)

    # this method is use to compare two texts
    def verifyTextMatch(self, actualText, expectedText):
        try:
            if actualText == expectedText:
                logging.info("### VERIFICATION MATCHED !!!")
                return True
            else:
                logging.info("### VERIFICATION DOES NOT MATCHED !!!")
                return False
        except NoSuchElementException:
            logging.info("No element")

    def findText(self, driver, text):
        check = False
        locator = (By.XPATH, "//android.widget.TextView")
        allTexts = self.getElements(driver, locator)
        #         allTexts = driver.find_elements_by_xpath("//android.widget.TextView[@text=\'"+text+"\']")
        for i in range(len(allTexts)):
            text2 = allTexts[i].text
            if text2 == text:
                check = True
        return check

    def find_radio_btn(self, driver, text):
        check = False
        locator = (By.XPATH, "//android.widget.RadioButton")
        allTexts = self.getElements(driver, locator)
        #         allTexts = driver.find_elements_by_xpath("//android.widget.TextView[@text=\'"+text+"\']")
        for i in range(len(allTexts)):
            text2 = allTexts[i].text
            if text2 == text:
                check = True
        return check

    def find_element_of_radio_btn(self, driver, text):
        ele = None
        locator = (By.XPATH, "//android.widget.RadioButton")
        allTexts = self.getElements(driver, locator)
        #         allTexts = driver.find_elements_by_xpath("//android.widget.TextView[@text=\'"+text+"\']")
        for i in range(len(allTexts)):
            text2 = allTexts[i].text
            if text2 == text:
                ele = allTexts[i]
                break
        return ele

    def find_element_of_text(self, driver, text):
        ele = None
        locator = (By.XPATH, "//android.widget.TextView")
        allTexts = self.getElements(driver, locator)
        #         allTexts = driver.find_elements_by_xpath("//android.widget.TextView[@text=\'"+text+"\']")
        for i in range(len(allTexts)):
            text2 = allTexts[i].text
            if text2 == text:
                ele = allTexts[i]
                break
        return ele

    def findButton(self, driver, text):
        locator = (By.XPATH, "//android.widget.Button")
        allTexts = self.getElements(driver, locator)
        #         allTexts = driver.find_elements_by_xpath("//android.widget.TextView[@text=\'"+text+"\']")
        for i in range(len(allTexts)):
            text2 = allTexts[i].text
            if text2 == text:
                return True
                break
        return False

    def findLink(self, driver, text):
        locator = (By.XPATH, "//android.widget.TextView")
        allTexts = self.getElements(driver, locator)
        #         allTexts = driver.find_elements_by_xpath("//android.widget.TextView[@text=\'"+text+"\']")
        for i in range(len(allTexts)):
            text2 = allTexts[i].text
            if text2 == text:
                attribute = allTexts[i].get_attribute("clickable")
                allTexts[i].is_enabled()
                return True
                break
        return False

    def clickLink(self, driver, text):
        locator = (By.XPATH, "//android.widget.TextView")
        allTexts = self.getElements(driver, locator)
        #         allTexts = driver.find_elements_by_xpath("//android.widget.TextView[@text=\'"+text+"\']")
        for i in range(len(allTexts)):
            text2 = allTexts[i].text
            if text2 == text:
                attribute = allTexts[i].get_attribute("clickable")
                logging.info(attribute)
                allTexts[i].is_enabled()
                allTexts[i].click()
                return True
                break
        return False

    def scrollToElement(self, driver, text):
        try:
            scrollable = "new UiScrollable(new UiSelector().scrollable(true))"
            textElement = ".scrollIntoView(new UiSelector().text(\"" + text + "\"))"
            driver.find_element_by_android_uiautomator(scrollable + textElement)
            return True
        except NoSuchElementException:
            logging.info("Given " + text + " isCorrect or not Present in the dropdown List")
            return False
            pytest.fail()

    def scrollToElementAndClick(self, driver, text):
        try:
            scrollable = "new UiScrollable(new UiSelector().scrollable(true))"
            textElement = ".scrollIntoView(new UiSelector().text(\"" + text + "\"))"
            driver.find_element_by_android_uiautomator(scrollable + textElement).click()
            return True
        except:
            return False

    def verifyTwoText(self, actual, expected):
        if actual == expected:
            logging.info("The " + actual + " and " + expected + "  are Matching")
            return True
        else:
            logging.info("The " + actual + " and " + expected + "  are not Matching")
            return False

    # this method is use to check element is present or not if yes it will return True else False
    def isElementPresent(self, driver, locator):
        try:
            element = None
            self.wait_for_locator(driver, locator, 5)
            element = self.getElement(driver, locator)
            if element is not None:
                return True
            else:
                logging.info("Element not found")
                return False
        except:
            return False

        # this method is use to hide the visible keyboard from device

    def hideKeyboard(self, driver):
        if driver.hide_keyboard():
            return True
        else:
            return False

    # this method is use to fetch the text from an element
    def getTextOfElement(self, driver, locator):
        try:
            element = self.getElement(driver, locator)
            if element is not None:
                elementTxt = element.text
                return elementTxt
            else:
                logging.error('Element text is Not Present')
        except:
            return None

    '''this method is use to fetch the value of 
    attribute from the locator , 
    in this we need to pass attribute name'''

    def getAttributeOfElement(self, driver, data, locator):
        element = self.getElement(driver, locator)
        if element is not None:
            elementTxt = element.get_attribute(data)
            return elementTxt
        else:
            logging.error('Element attribute is Not Present')

    # this method is use to check text is present or not
    def verifyTextisPresent(self, driver, locator):
        element = self.getElement(driver, locator)
        if element is not None:
            elementTxt = element.text
            return True
        else:
            logging.error('Element text is Not Present')
            return False

    # this method is use to check keyword is present or not
    def isKeyBoardShown(self, driver):
        check = driver.is_keyboard_shown()
        if check == True:
            return True
        else:
            logging.error('Failed To show the Keyboard Screen')
            return False

    # this method is use to click on device back button
    def click_on_device_back_btn(self, driver):
        driver.back()

    def getCurrentPackage(self, driver):
        package = driver.current_package()
        logging.info(package)
        return package

    # this method is use to click on device home button
    def click_on_device_home_btn(self):
        try:
            sleep(2)
            self.run("adb shell input keyevent KEYCODE_HOME")
            return True
        except:
            return False
            logging.info('Error in clicking the device back btn')

    def viewAppForeground(self, driver, appPackage):
        text = appPackage
        if text == 'HomeButton':
            self.run('adb shell input keyevent KEYCODE_HOME')
            return True

        else:
            return False

    def isAppActive(self, driver, text):
        try:
            check = driver.query_app_state(text)
            return check

        except:
            return check

    def acceptNotification(self, driver):
        try:
            allowPopUp = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            """Agreeing Allow Notification"""
            if allowPopUp.is_displayed():
                allowPopUp.click()
                sleep(2)
                allowPopUp.click()
        #             print('Clicked On Accept Element')
        except:
            pass

    def is_element_visible(self, driver, locator):
        element = self.getElement(driver, locator)
        if element is not None:
            check = element.getAttribute("Visible")
            if check == True:
                logging.info("element is visible")
                return True
            else:
                logging.error('element is not visible')
                return False

    # -------------------------------janardhan---------------------------

    def take_app_foreground(self, driver, appPackage):
        try:
            driver.activate_app(appPackage)
            logging.info('irfan Success')
            return True

        except:
            return False

    def get_screen_orientation(self, driver):
        screen = driver.orientation
        return screen

    def get_element_location(self, driver, locator):
        element = self.getElement(driver, locator)
        location = element.location
        return location

    def get_size_of_element(self, driver, locator):
        element = self.getElement(driver, locator)
        location = element.rect
        return location

    def get_swipe_count(self, driver, locator):
        text = self.getTextOfElement(driver, locator)
        res = [int(i) for i in text.split() if i.isdigit()]
        return res

    def select_topic(self, driver, sub_chapter_xpath, topic_xpath, swipe_count):
        logging.info(topic_xpath)
        loc = self.get_element_location(driver, sub_chapter_xpath)
        x2 = loc["x"] + 100
        y2 = loc["y"] + 100
        x1 = x2 + 700
        y1 = y2
        for i in range(swipe_count):
            if self.isElementPresent(driver, topic_xpath):
                self.elementClick(driver, topic_xpath)
                break
            else:
                self.run('adb shell input swipe {} {} {} {}'.format(x1, y1, x2, y2))

    def set_screen_orientation(self, driver, screen):
        driver.orientation = "LANDSCAPE"
