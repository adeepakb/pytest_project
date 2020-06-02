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

featureFileName = "Revisit Screen"
CommonMethods = CommonMethods()


class RevisitScreen():
    revisit_node_journey_card=(By.XPATH, "//android.widget.RelativeLayout/descendant::android.widget.TextView[@text='Negatives and Reciprocals']")
    btn_exit_journey =(By.ID,"com.byjus.thelearningapp:id/secondaryAction")
    node_revisit=(By.XPATH,"//android.widget.TextView[@text='Concept Refresher']")
    progression_bar=(By.ID,"com.byjus.thelearningapp:id/challengeProgressIndicator")
    close_icon=(By.ID,"com.byjus.thelearningapp:id/roundedNavButton")
    revisit_label=(By.XPATH, "(//android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/title'])[1]")
    concept_summary_and_name=(By.XPATH, "//androidx.recyclerview.widget.RecyclerView/descendant::android.widget.LinearLayout/descendant::android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/title']")
    txt_description=(By.ID,"com.byjus.thelearningapp:id/description")
    swipe_to_start=(By.ID, "com.byjus.thelearningapp:id/swipeStart")
    concept_summary_screen=(By.ID,"com.byjus.thelearningapp:id/layout_header")
    concept_summary_screen_video_player = (By.ID, "com.byjus.thelearningapp:id/playerLayout")
    node_frame = (By.ID, "com.byjus.thelearningapp:id/node_detail_layout")
    txt_practice_in_practice_screen=(By.XPATH, "//android.widget.LinearLayout/descendant::android.widget.TextView[@text='Practice']")
    highlighted_Journey_card = (By.ID, "com.byjus.thelearningapp:id/ivHighlight")
    practice_image=(By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp:id/introView']/descendant::android.widget.ImageView[@index=0]")

    def __init__(self, browser):
        self.browser = browser

    def verify_revisit_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.revisit_label)
            if check == True:
                logging.info("Revisit screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_revisit_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_revisit_screen')

    def click_on_revisit_journey_card(self,browser):
        try:
            check=CommonMethods.isElementPresent(browser,self.revisit_node_journey_card)
            if check==True:
                logging.info("revisit node journey card is visible")
            else:
                while check==False:
                    nodeCrd = CommonMethods.getElement(browser, self.highlighted_Journey_card)
                    n = nodeCrd.location_in_view
                    browser.swipe(n['x'], n['y'], n['x'], n['y'] - 200)
                    check = CommonMethods.is_element_visible(browser, self.revisit_node_journey_card)
            CommonMethods.elementClick(browser,self.revisit_node_journey_card)
            logging.info("clicked on revisit journey card")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_revisit_journey_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_revisit_journey_card')
    def verify_progression_bar(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.progression_bar)
            if check == True:
                logging.info("progression bar is displayed in revisit screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_progression_bar')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_progression_bar')

    def verify_close_icon(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.close_icon)
            if check == True:
                logging.info("close icon is displayed in revisit screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_close_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_close_icon')

    def verify_lets_revisit_label(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.revisit_label)
            if check == True:
                logging.info("let's Revisit label is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_lets_revisit_label')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_lets_revisit_label')

    def verify_concepts_summary_details_and_count(self, browser):
        try:
            # concepts=browser.find_elements_by_xpath("//androidx.recyclerview.widget.RecyclerView / descendant::android.widget.LinearLayout / descendant::android.widget.TextView[ @ resource - id = 'com.byjus.thelearningapp:id/title']")
            concepts=CommonMethods.getElements(browser, self.concept_summary_and_name)
            if len(concepts) >= 0:
                logging.info("concept summary and their name is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_concepts_summary_details_and_count')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_concepts_summary_details_and_count')
        return len(concepts)

    def verify_text_description(self, browser, expected_text):
        try:
            actual_text=CommonMethods.getTextOfElement(browser,self.txt_description)
            if expected_text == actual_text:
                logging.info("concept text description is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_text_description')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_text_description')
    def verify_text_swipe_to_start(self, browser, expected_text):
        try:
            actual_text=CommonMethods.getTextOfElement(browser, self.swipe_to_start)
            if expected_text == actual_text:
                logging.info("swipe to start text is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_text_swipe_to_start')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_text_swipe_to_start')
    def swipe_for_swipe_to_start(self,browser):
        try:
            CommonMethods.wait_for_locator(browser, self.swipe_to_start, 20)
            start = CommonMethods.getElement(browser, self.swipe_to_start)
            n = start.location_in_view
            browser.swipe(n['x'], n['y'], n['x']-300, n['y'])
            logging.info("swiped successfully")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'swipe_for_swipe_to_start')
        except:
            CommonMethods.exception(browser, featureFileName, 'swipe_for_swipe_to_start')
        return  n

    def verify_concept_summary_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.concept_summary_screen)
            if check == True:
                logging.info("concept summary screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_concept_summary_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_concept_summary_screen')

    def verify_journey_map_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.node_frame)
            if check == True:
                logging.info("journey map screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_journey_map_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_journey_map_screen')

    def click_on_close_icon(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.close_icon, 20)
            check = CommonMethods.elementClick(browser, self.close_icon)
            if check == True:
                logging.info("clicked on close icon in revisit screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_close_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_close_icon')

    def click_on_device_back_btn(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.close_icon, 20)
            click_on_back_button(browser)
            logging.info("clicked on device back button from revisit screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_device_back_btn')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_device_back_btn')

    def verify_practice_screen(self, browser):
        try:
            check=CommonMethods.isElementPresent(browser,self.practice_image)
            if check == True:
                logging.info("practice screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_practice_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_practice_screen')

    def swipe_till_practice_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.txt_practice_in_practice_screen)
            if check==False:
                cords=self.swipe_for_swipe_to_start(browser)
                while check==False:
                    browser.swipe(cords['x'], cords['y'], cords['x'] - 300, cords['y'])
                    check = CommonMethods.isElementPresent(browser, self.txt_practice_in_practice_screen)
            else:
                logging.info("practice screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'swipe_till_practice_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'swipe_till_practice_screen')