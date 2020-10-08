import sys
import os
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.interrupt import *
from Utilities.common_methods import CommonMethods
from POM_Pages.revisitScreen import RevisitScreen
from POM_Pages.ConceptSummaryScreen import ConceptSummaryScreen

from POM_Pages.revisitScreen import RevisitScreen
featureFileName = "Start Practice screen"
CommonMethods = CommonMethods()

class StartPracticeScreen():
    practice_image = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp:id/introView']/descendant::android.widget.ImageView[@index=0]")
    practice_label=(By.XPATH,"//android.widget.LinearLayout/descendant::android.widget.TextView[@text='Practice']")
    practice_frame = (By.ID, "com.byjus.thelearningapp:id/introView")
    practice_decription = (By.ID, "com.byjus.thelearningapp:id/practiceDescription")
    btn_practice = (By.ID, "com.byjus.thelearningapp:id/startPractice")
    # que_screen_frame=(By.ID,"com.byjus.thelearningapp:id/questionView")
    que_label=(By.XPATH,"//android.widget.TextView[@text='Question']")

    def __init__(self, driver):
        self.driver = driver
        self.revisit = RevisitScreen(driver)
        self.concpt =ConceptSummaryScreen(driver)

    def verify_practice_label(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver,self.practice_label)
            if check==True:
                logging.info("practice label is displayed in practice screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_practice_label')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_practice_label')

    def verify_practice_description_text(self,driver,exp_text):
        try:
            actual_text=CommonMethods.getTextOfElement(driver,self.practice_decription)
            if actual_text==exp_text:
                logging.info("practice desctiption is present--> "+ actual_text +" in practice screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_practice_description_text')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_practice_description_text')
    def verify_practice_button(self,driver):
        try:
            CommonMethods.wait_for_locator(driver, self.btn_practice, 15)
            check=CommonMethods.isElementPresent(driver,self.btn_practice)
            if check==True:
                logging.info("practice button is displayed in practice screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_practice_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_practice_button')

    def click_on_practice_button(self,driver):
        try:
            check=CommonMethods.elementClick(driver,self.btn_practice)
            if check==True:
                logging.info("successfully clicked on practice button in practice screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_practice_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_practice_button')

    def verify_question_screen(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver,self.que_label)
            if check==True:
                logging.info("question screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_question_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_question_screen')
