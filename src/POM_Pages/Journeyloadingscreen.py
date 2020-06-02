import sys
import os
from appium import webdriver
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
import pytest
from pyparsing import Char
from selenium.webdriver.support.wait import WebDriverWait
# from nose.config import flag
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from appium.webdriver.webelement import MobileBy
from Utilities.interrupt import *
from Utilities.common_methods import CommonMethods
# from Constants.load_json import getdata
featureFileName = "Journey loading screen"
CommonMethods = CommonMethods()


class JourneyLoadingScreen():
    first_Journey_Card = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvChapterList']/android.widget.LinearLayout[@index=1]//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']/android.widget.RelativeLayout[@index=0]")
    back_arrow = (By.ID, "com.byjus.thelearningapp:id/roundedNavButton")
    journey_name = (By.ID, "com.byjus.thelearningapp:id/journey_name")
    animationView = (By.ID, "com.byjus.thelearningapp:id/animation_view")
    greetingText = (By.ID, "com.byjus.thelearningapp:id/greeting")
    personal_message = (By.ID, "com.byjus.thelearningapp:id/personal_message")
    btn_library_xpath = (By.XPATH, "//android.widget.Button[@text='Library']")
    node_Frame = (By.ID, "com.byjus.thelearningapp:id/node_detail_layout")
    btn_start = (By.XPATH, "//android.widget.Button[@text='Start']")
    btn_continue = (By.XPATH, "//android.widget.Button[@text='Continue']")
    node_with_node_text=(By.XPATH,"//android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/node_title_text']/parent::android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp:id/node_parent']")
    node_Name_Text = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp:id/node_detail_layout']/descendant::android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/node_title_text']")
    journey_loading_screen=(By.ID,"com.byjus.thelearningapp:id/viewKonfetti")
    already_taken_journey_with_threedot=(By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/ivLayoverIcon']")
    journey_list=(By.XPATH,"//androidx.recyclerview.widget.RecyclerView [@resource-id='com.byjus.thelearningapp:id/rvSubtopic']//android.widget.RelativeLayout")
    video_name_in_resource_screen = (By.ID, "com.byjus.thelearningapp:id/labelVideoName")
    resource_que_screen = (By.ID, "com.byjus.thelearningapp:id/llQuestionComponentParent")
    trendingJourney_id = (By.ID, "com.byjus.thelearningapp:id/ivHighlight")
    subjectName_id = (By.ID, "com.byjus.thelearningapp:id/header_title_text")
#     taken_journey=(By.XPATH,"//android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/ivLayoverIcon']")
    exit_journey_button=(By.ID,"com.byjus.thelearningapp:id/secondaryAction")
    btn_library = (By.XPATH, "//android.widget.Button[@text='Library']")
    Btn_library_when_text_isnot_there = (By.XPATH, "(//android.widget.Button[@resource-id='com.byjus.thelearningapp:id/roundedNavButton'])[2]")
    personalised_btn = (By.XPATH, "//android.widget.Button[@text='Personalised']")
    def __init__(self, browser):
        self.browser = browser
        
        
    def scroll_up_with_highlight_journey(self,browser):
        check=CommonMethods.isElementPresent(browser,self.trendingJourney_id)
        display_sub=CommonMethods.isElementPresent(browser,self.subjectName_id)
        if check==True:
           while display_sub==False:
                nodeCrd = CommonMethods.getElement(browser, self.trendingJourney_id)
                n = nodeCrd.location_in_view
                browser.swipe(n['x'], n['y'], n['x'], n['y'] + 100)
#                 print(n['x'],n['y'])
                display_sub = CommonMethods.isElementPresent(browser, self.subjectName_id)
                
    def switch_to_twoG(self,browser):
        try:
            set_connection_type(browser, "DATA_ONLY")
            logging.info("enabled data connection mode")
        except:
            CommonMethods.exception(browser, featureFileName, 'switch_to_twoG')

    def switch_to_wifi(self,browser):
        try:
            set_connection_type(browser, "WIFI_ONLY")
            logging.info("enabled wifi connectio mode")
        except:
            CommonMethods.exception(browser, featureFileName, 'switch_to_wifi')

    def scroll_in_journeys(self, browser):
        nodeCrd = CommonMethods.getElement(browser, self.node_Frame)
        n = nodeCrd.location_in_view
        browser.swipe(n['x'], n['y'], n['x'] , n['y'] + 200)
        return n

    def click_on_journey_card(self, browser):
        CommonMethods.elementClick(browser, self.first_Journey_Card)
        logging.info("journey screen is displayed")

    def verify_back_arrow(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.back_arrow)
            if check == True:
                logging.info("back arrow is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_back_arrow')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_back_arrow')

    def verify_chapter_name(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.journey_name, 2)
            check = CommonMethods.isElementPresent(browser, self.journey_name)
            if check == True:
                chapter_nam=CommonMethods.getTextOfElement(browser, self.journey_name)
                # logging.info(chapter_nam)
                logging.info("chapter name is "+chapter_nam)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_chapter_name')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_chapter_name')

    def verify_msg(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.personal_message)
            if check == True:
                msg = CommonMethods.getTextOfElement(browser, self.personal_message)
                logging.info("personal msg is displayed "+msg)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_msg')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_msg')

    def click_on_device_back_Btn(self, browser):
        try:
            click_on_back_button(browser)
            logging.info('Successfully Tapped On device back button')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_device_back_Btn')

#     def verify_personlised_screen(self, browser):
#         try:
#             check = CommonMethods.isElementPresent(browser, self.btn_library_xpath)
#             if check == True:
#                 logging.info("personalised screen is displayed")
#         except NoSuchElementException:
#             CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_personlised_screen')
#         except:
#             CommonMethods.exception(browser, featureFileName, 'verify_personlised_screen')

    def verify_journey_first(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.btn_start)
            if check == True:
                logging.info("journey is loading first time")
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_journey_first')

    def verify_journey_map_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.node_Frame)
            if check == True :
                logging.info("journey map screen is displayed")
            elif check == False:
                click_on_back_button(browser)
                logging.info("journey map screen is displayed")
            else:
                logging.info("journey map screen is not displayed")
                logging.info("Failed Locator in Method verify_journey_map_screen")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except :
            logging.info("Failed Locator in Method verify_journey_map_screen")
            CommonMethods.takeScreenShot(browser, featureFileName)
            pytest.fail("Failed Due to Locator in Journey map screen")

    def get_all_node_names(self,browser):
        try:
            node_names=[]
            check = CommonMethods.isElementPresent(browser, self.node_Frame)
            node= CommonMethods.isElementPresent(browser,self.node_with_node_text)

            if check == True:
                while node == True:
                    currentNodeCords = self.scroll_in_journeys(browser)
                    browser.swipe(currentNodeCords['x'], currentNodeCords['y'], currentNodeCords['x'],
                                  currentNodeCords['y'] + 200)
                    # check = CommonMethods.isElementPresent(browser, self.node_Frame)
                    node= CommonMethods.isElementPresent(browser,self.node_with_node_text)
                    text=CommonMethods.getTextOfElement(browser,self.node_Name_Text)
                    if text not in node_names:
                        node_names.append(text)
                logging.info("node with node name displayed")
            else:
                click_on_back_button(browser)
                check = CommonMethods.isElementPresent(browser, self.node_Frame)
                node = CommonMethods.isElementPresent(browser, self.node_with_node_text)
                if check == True:
                    while node == True:
                        currentNodeCords = self.scroll_in_journeys(browser)
                        browser.swipe(currentNodeCords['x'], currentNodeCords['y'], currentNodeCords['x'],
                                      currentNodeCords['y'] + 200)
                        node = CommonMethods.isElementPresent(browser, self.node_with_node_text)
                        text = CommonMethods.getTextOfElement(browser, self.node_Name_Text)
                        if text not in node_names:
                            node_names.append(text)
                logging.info("node with node name displayed")
        except:
            CommonMethods.exception(browser, featureFileName, 'get_all_node_names')
        return node_names

    def nodes(self,browser):
        nodes=self.get_all_node_names(browser)
        logging.info(nodes)

    def verify_journey_loading_screen(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.journey_loading_screen)
            if check == True:
                logging.info("journey screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_journey_loading_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_journey_loading_screen')

    def verify_already_download_journey(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.btn_continue)
            if check == True:
                logging.info("user opened already downloaded journey")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_already_download_journey')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_already_download_journey')

    def verify_node_frame_and_get_text_node(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.node_Frame)
            if check == True:
                text = CommonMethods.getTextOfElement(browser, self.node_Name_Text)
                logging.info("user will continue journey with this node"+text)
            else :
                click_on_back_button(browser)
                text = CommonMethods.getTextOfElement(browser, self.node_Name_Text)
                logging.info("user will continue journey with this node" + text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_node_frame_and_get_text_node')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_node_frame_and_get_text_node')

    def click_on_new_journey_without_three_do(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.already_taken_journey_with_threedot)
            if check == False:
                logging.info('This journey is loading first time')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_new_journey_without_three_do')

    def verify_resource_screen(self, browser):
        try:
            resource_name = ""
            check1 = CommonMethods.isElementPresent(browser, self.video_name_in_resource_screen)
            check2 = CommonMethods.isElementPresent(browser, self.resource_que_screen)
            if check1 == True:
                resource_name = "Video Screen"
                logging.info("video resource screen displayed")
            elif check2 == True:
                click_on_back_button(browser)
                resource_name = "Questions"
                logging.info("Questions resource screen displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_resource_screen')

    def verify_resource(self, browser):
        try:
            check1 = CommonMethods.isElementPresent(browser, self.video_name_in_resource_screen)
            check2 = CommonMethods.isElementPresent(browser, self.resource_que_screen)
            if check1 == True:
                logging.info("video resource screen displayed")
            elif check2 == True:
                logging.info("Questions resource screen displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_resource')

    def click_on_new_journey_card(self, browser):
        try:
            browser.swipe(300, 500, 300, 100)
            journey_card_without_test_practice=(By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.TextView/following-sibling::androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']/descendant::android.widget.TextView[not (@text='Practice') and not (@text='Tests')]")
            all_journeys=CommonMethods.getElements(browser, journey_card_without_test_practice)
            logging.info(len(all_journeys))
            taken_journey_with_dot_symbol=(By.XPATH,"//*[contains(@resource-id,'com.byjus.thelearningapp:id/ivLayoverIcon')]/parent::android.widget.RelativeLayout/descendant::android.widget.TextView")     
            taken_jorney_cards=CommonMethods.getElements(browser, taken_journey_with_dot_symbol)
            logging.info(len(taken_jorney_cards))
            text_of_taken_journey=[]
            for i in taken_jorney_cards:
                logging.info(i.text)
                text_of_taken_journey.append(i.text)
            for j in all_journeys:
                if j.text not in text_of_taken_journey:
                    j.click()
                    break      
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_new_journey_card')     
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_new_journey_card')
    
    
    
    def click_on_already_taken_journey_card(self, browser):
        try:
            sleep(2)
            journey_card_without_test_practice = (By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.TextView/following-sibling::androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']/descendant::android.widget.TextView[not (@text='Practice') and not (@text='Tests')]")
            all_journeys=CommonMethods.getElements(browser, journey_card_without_test_practice)
            logging.info(len(all_journeys))
            taken_journey_with_dot_symbol=(By.XPATH,"//*[contains(@resource-id,'com.byjus.thelearningapp:id/ivLayoverIcon')]/parent::android.widget.RelativeLayout/descendant::android.widget.TextView")     
            taken_jorney_cards=CommonMethods.getElements(browser, taken_journey_with_dot_symbol)
            logging.info(len(taken_jorney_cards))
            text_of_taken_journey=[]
            for i in taken_jorney_cards:
#                 logging.info(i.text)
                text_of_taken_journey.append(i.text)
#             logging.info(text_of_taken_journey)
#             logging.info(all_journeys)
            for j in all_journeys:
                if j.text in text_of_taken_journey:
#                     logging.info(j.text)
                    j.click()
                    break
                else:
                    logging.info('already taken journey is not present')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_already_taken_journey_card')             
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_already_taken_journey_card')
    
    def handle_exit_journey_pop_up(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.exit_journey_button)
            if check==True:
                CommonMethods.elementClick(browser, self.exit_journey_button)
                logging.info("Exit journey pop up displayed and closed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'handle_exit_journey_pop_up')             
        except:
            CommonMethods.exception(browser, featureFileName, 'handle_exit_journey_pop_up')
      
    def verify_personaised_screen(self,browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.btn_library)
            check1 = CommonMethods.isElementPresent(browser, self.Btn_library_when_text_isnot_there)
            personaised_button = CommonMethods.isElementPresent(browser, self.personalised_btn)
            if check == True:
                logging.info("personalised chapter list screen is displayed")
            elif check1 == True:
                logging.info("personalised chapter list screen is displayed")
            elif personaised_button == True:
                text_personalise = CommonMethods.getTextOfElement(browser, self.personalised_btn)
                if text_personalise =='Personalised':
                    CommonMethods.elementClick(browser, self.personalised_btn)
                    logging.info("personalised chapter list screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_personaised_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_personaised_screen')   
