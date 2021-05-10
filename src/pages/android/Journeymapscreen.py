import sys
import os
from appium import webdriver
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import inspect
from selenium.webdriver.common.by import By
import logging
import pytest
from pyparsing import Char
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.interrupt import *
from utilities.common_methods import CommonMethods

featureFileName = "Journey map screen"
CommonMethods = CommonMethods()


class JourneyMapScreen():
    
    first_journey_card = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvChapterList']/android.widget.LinearLayout[@index=1]//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']/android.widget.RelativeLayout[@index=0]")
    btn_continue = (By.XPATH, "//android.widget.Button[@text='Continue']")
    btn_start = (By.XPATH, "//android.widget.Button[@text='Start']")
    btn_skip = (By.ID, "com.byjus.thelearningapp:id/btnSkip")
    node_frame = (By.ID, "com.byjus.thelearningapp:id/node_detail_layout")
    nodes_card = (By.XPATH, "//android.widget.LinearLayout/descendant::android.widget.LinearLayout/android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/node_title_text']")
    btn_next_in_videoscreen = (By.ID, "com.byjus.thelearningapp:id/btnBottomAction")
    resource_icon = (By.ID, "com.byjus.thelearningapp:id/llIcon")
    btn_setting_no_network_screen = (By.ID, "com.byjus.thelearningapp:id/errorPrimaryAction")
    btn_refresh_no_network_screen = (By.ID, "com.byjus.thelearningapp:id/errorSecondaryAction")
    txt_no_internet_networkscreen = (By.ID, "com.byjus.thelearningapp:id/tvErrorTitle")
    id_on_device_setting_screen = (By.ID, "com.android.settings:id/dashboard_container")
    no_internet_toast_message = (By.ID, "com.byjus.thelearningapp:id/snackbar_text")
    no_internet_screen_detail_card = (By.ID, "com.byjus.thelearningapp:id/tvErrorTitle")
    stickycard_id = (By.ID, "com.byjus.thelearningapp:id/journeyStickCard")
    journey_name_in_sticky_card = (By.ID, "com.byjus.thelearningapp:id/recentJourneyTitle")
    video_name_in_resource_screen = (By.ID, "com.byjus.thelearningapp:id/labelVideoName")
    lock_symbol_in_Journey_nodecard = (By.ID, "com.byjus.thelearningapp:id/ivLock")
    node_info_txt_In_nodecard = (By.ID, "com.byjus.thelearningapp:id/node_info_text")
    node_name_text = (By.XPATH, "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp:id/node_detail_layout']/descendant::android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/node_title_text']")
    resume_btn = (By.ID, "com.byjus.thelearningapp:id/resume_journey_button")
    resource_que_screen = (By.ID,"com.byjus.thelearningapp:id/llQuestionComponentParent")
    optional_node = (By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[@text='Optional']")
    skip_btn_in_optional_frame=(By.ID, "com.byjus.thelearningapp:id/btnSkip")
    resource_icons=(By.XPATH,"//android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/node_parent']")
    options_for_questions=(By.XPATH,"//android.view.View[@resource-id='root']/descendant::android.view.View[@text='b．']")
    submit_btn_in_question=(By.XPATH,"//android.view.View[@text='Submit']")
    next_btn_in_question=(By.XPATH,"//android.view.View[@text='Next']")
    badges_close_btn=(By.ID,"com.byjus.thelearningapp:id/ivCloseBtn")
    rich_text_screen=(By.ID,"com.byjus.thelearningapp:id/container")
    next_btn_in_richtext_screen=(By.ID,"com.byjus.thelearningapp:id/action_morph_btn")
    share_btn_in_richtext_screen=(By.ID,"com.byjus.thelearningapp:id/optionalNav")
    back_btn_in_richtext_screen=(By.ID,"com.byjus.thelearningapp:id/backNav")
    title_in_richtext_screen=(By.ID,"com.byjus.thelearningapp:id/title")

    trendingJourney_id = (By.ID, "com.byjus.thelearningapp:id/ivHighlight")
    concept_screen = (By.ID,"com.byjus.thelearningapp:id/rootView")
    exit_journey_secondary_opn = (By.ID,"com.byjus.thelearningapp:id/secondaryAction")
    leaving_so_soon_bottom_sheet_dialog = (By.ID,"com.byjus.thelearningapp:id/design_bottom_sheet")
    leaving_so_soon_quit = (By.ID,"com.byjus.thelearningapp:id/secondaryAction")
    
    
    
    icons=[]
    
    def __init__(self, driver):
        self.driver = driver
        
        
    def click_on_journey_card(self, driver):
        CommonMethods.elementClick(driver, self.first_journey_card)
        logging.info("journey screen is displayed")
        
    def verify_map_animation_and_node_arrangement(self, driver):
        try:
            sleep(10)
            CommonMethods.wait_for_element_visible( driver, self.btn_next_in_videoscreen, 5)
            check = CommonMethods.isElementPresent(driver, self.btn_next_in_videoscreen)
            if check == True:
                logging.info("Map Animation And Node Arrangement is done")
                CommonMethods.clickOnBackBtn(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_map_animation_and_node_arrangement')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_map_animation_and_node_arrangement')

    def verify_node_card(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.node_frame)
            if check == True:
                driver.swipe(300, 500, 300, 300)
                logging.info("Node card is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_node_card')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_node_card')

    def verify_node_name(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.node_frame)
            if check == True:
                logging.info("Node card is displayed")
 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_node_name')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_node_name')

    def get_text_of_node(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.node_frame)
            if check == True:
                driver.swipe(300, 500, 300, 300)
                textOfNode = CommonMethods.getTextOfElement(driver, self.node_name_text)
                logging.info("node text is: "+ textOfNode)
        except:
            CommonMethods.exception(driver, featureFileName, 'get_text_of_node')
        return textOfNode

    def verify_start_button(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.btn_start)
            if check == True:
                logging.info("start button is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_start_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_start_button')

    def loading_journey_first_time(self,driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.btn_start)
            if check == True:
                logging.info("user is loading journey first time")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'loading_journey_first_time')
        except:
            CommonMethods.exception(driver, featureFileName, 'loading_journey_first_time')

    def select_offline_mode(self, driver):
        try:
            set_connection_type(driver, 'offline')
            logging.info("enabled offline mode")
        except:
            CommonMethods.exception(driver, featureFileName, 'select_offline_mode')
        
    def verify_no_internet_access_screen(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.no_internet_screen_detail_card)
            if check == True:
                logging.info("No Internet access screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_no_internet_access_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_no_internet_access_screen')

    def click_on_settings_btn(self, driver):
        try:
            check = CommonMethods.elementClick(driver, self.btn_setting_no_network_screen)
            if(check == True):
                logging.info('Sucessfully Tapped On settings button ')

                pytest.fail("Failed Due to Locator in No Internet Access screen")
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_settings_btn')

    def verify_device_settings_screen(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.id_on_device_setting_screen)
            if check == True:
                logging.info("Device settings screen is displayed")

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_device_settings_screen')
        
    def verify_no_internet_toast_message(self, driver, txt):
        try:
            toastMsg = CommonMethods.getTextOfElement(driver, self.no_internet_toast_message)
#             logging.info(toastMsg)
            if toastMsg == txt:
                logging.info("No Internet Toast Message is displayed")

        except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_no_internet_toast_message')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_no_internet_toast_message')

    def click_on_refresh_btn(self, driver):
        try:
            check = CommonMethods.elementClick(driver, self.btn_refresh_no_network_screen)
            if(check == True):
                logging.info('Successfully Tapped On Refresh button ')

        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_refresh_btn')
            
    def click_on_continue_btn(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.btn_continue, 15)
            check = CommonMethods.elementClick(driver, self.btn_continue)
            if(check == True):
                logging.info('Successfully Tapped On Continue button ')

        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_continue_btn')
            
    def select_online_mode(self, driver, WIFI):
        try:
            set_connection_type(driver, WIFI)
            logging.info("enabled Online mode")
        except:
            CommonMethods.exception(driver, featureFileName, 'select_online_mode')
          
    def verify_resource_screen_map(self, driver):
        try:
            refreshBtn = CommonMethods.isElementPresent(driver, self.btn_refresh_no_network_screen)
            check = CommonMethods.isElementPresent(driver, self.btn_next_in_videoscreen)
            
            if refreshBtn == True:
                refreshBtn.click()
                logging.info("clicked on refresh button")
            elif check == True:
                logging.info("Resource screen is displayed")
            else :
                logging.info("Resource screen is not displayed")
                pytest.fail("Failed Due to Locator in Journey map screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyResourceScreen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyResourceScreen')
            
    def verify_no_internet_access_text(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.txt_no_internet_networkscreen)
            if check == True:
                logging.info("No Internet Access Text is displayed")
            else:
                logging.info("No Internet Access Text is not displayed")
                logging.info("Failed Locator in Method verifyNoInterNetAccessText")
                pytest.fail("Failed Due to Locator in No Internet Access screen")
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_no_internet_access_text')

    def verify_setting_and_refresh_btn(self, driver):
        try:
            check1 = CommonMethods.isElementPresent(driver, self.btn_setting_no_network_screen)
            check2 = CommonMethods.isElementPresent(driver, self.btn_refresh_no_network_screen)
            if check1 == True and check2 == True :
                logging.info("Settings and refresh buttons are displayed")
            else:
                logging.info("Settings and refresh buttons not displayed")
                logging.info("Failed Locator in Method verifySettingAndRefreshBtn")
                pytest.fail("Failed Due to Locator in No Internet Access screen")
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_setting_and_refresh_btn')

    def verify_node_frame_in_journey(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.node_frame)
            if check == True :
                logging.info("node frame is displayed")
            elif check == False:
                click_on_back_button(driver)
            else:
                logging.info("node frame is not displayed")
                logging.info("Failed Locator in Method verifyNodeFrameInJourney")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_node_frame_in_journey')
            
    def scroll_in_journeys(self, driver):
        CommonMethods.wait_for_element_visible(driver, self.node_frame, 2)
        nodeCrd = CommonMethods.getElement(driver, self.node_frame)
        n = nodeCrd.location_in_view
        driver.swipe(n['x'], n['y'], n['x'] , n['y'] + 200)
        return n

    def scroll_in_journeys_down(self, driver):
        nodeCrd = CommonMethods.getElement(driver, self.node_frame)
        n = nodeCrd.location_in_view
        driver.swipe(n['x'], n['y'], n['x'] , n['y'] - 200)
        return n

    def verify_resource_video_screen(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.video_name_in_resource_screen)
            if check == True:
                logging.info("Resource screen is displayed")
            else :
                logging.info("Resource screen is not displayed")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_resource_video_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_resource_video_screen')
            
#     def verifyAutoPlayVideoNotPresent(self, driver):
#         try:
#             check = CommonMethods.isElementPresent(driver, self.videoNameInResourceScreen)
#             
#             if check == False:
#                 logging.info("Resource screen is not displayed")
#             else :
#                 logging.info("Resource screen is displayed")
#                 pytest.fail("Failed Due to Locator in Journey map screen")
#                 
#         except NoSuchElementException:
#             CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyAutoPlayVideoNotPresent')
#         except:
#             CommonMethods.exception(driver, featureFileName, 'verifyAutoPlayVideoNotPresent')

    def get_text_of_sticky_card(self, driver):
        sticky_card_video_name = CommonMethods.getTextOfElement(driver, self.journey_name_in_sticky_card)
        logging.info(sticky_card_video_name)
        return sticky_card_video_name

    def verify_already_taken_journey(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.stickycard_id)
            self.get_text_of_sticky_card(driver)
            if check == True:
                logging.info("Journey already taken")
            else :
                logging.info("Journey is not taken previously")
                pytest.fail("Failed Due to Locator in personalised chapter list screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_already_taken_journey')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_already_taken_journey')
            
    def click_on_already_taken_journey(self, driver):
        try:
            check = CommonMethods.elementClick(driver, self.stickycard_id)
            if(check == True):
                logging.info('Successfully Tapped On already taken journey card')
            else:
                logging.info('Failed to Tap On Tapped On already taken journey card')
                logging.info("Failed Locator in Method clickOnAlreadyTakenJourney")
                pytest.fail("Failed Due to Locator in personalised chapter list screen")
        except:
            CommonMethods.exception(driver, featureFileName, 'clickOnAlreadyTakenJourney')
            
    def verify_journey_name_with_sticky_card_and_resource_screen(self, driver):
        try:
            sticky_card_video_name = self.get_text_of_sticky_card(driver)
            CommonMethods.wait_for_locator(driver, self.video_name_in_resource_screen, 15)
            resource_screen_video_name = CommonMethods.getTextOfElement(driver, self.video_name_in_resource_screen)
            resource_screen_video_name = list(resource_screen_video_name)
            logging.info(resource_screen_video_name)
            logging.info(sticky_card_video_name)
            if sticky_card_video_name in resource_screen_video_name:
                logging.info("Journey from sticky card is played")
            else :
                logging.info("Journey from sticky card is not played")
                pytest.fail("Failed Due to Locator in resource screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyJourneyNameWithStickyCardAndResourceScreen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyJourneyNameWithStickyCardAndResourceScreen')

    def scroll_for_locked_videos(self, driver):
        try: 
            CommonMethods.wait_for_locator(driver, self.btn_continue, 10)
#             lockedFrame = CommonMethods.isElementPresent(driver, self.lockSymbolInJourneyNodeCard)
            check = CommonMethods.isElementPresent(driver, self.btn_continue)
            lockedFrame = False
            if check == True :
                while lockedFrame == False:
                    currentNodeCords = self.scroll_in_journeys(driver)
                    driver.swipe(currentNodeCords['x'], currentNodeCords['y'], currentNodeCords['x'], currentNodeCords['y'] + 300)
                    check = CommonMethods.isElementPresent(driver, self.lock_symbol_in_Journey_nodecard)
                    break
                logging.info("locked video is displayed")
            else: 
                sleep(3)
                click_on_back_button(driver)    
                lockedFrame = CommonMethods.isElementPresent(driver, self.lock_symbol_in_Journey_nodecard)
                while lockedFrame == False:
                    currentNodeCords = self.scroll_in_journeys(driver)
                    driver.swipe(currentNodeCords['x'], currentNodeCords['y'], currentNodeCords['x'], currentNodeCords['y'] + 300)
                    check = CommonMethods.isElementPresent(driver, self.lock_symbol_in_Journey_nodecard)
                    break
            logging.info("locked video is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'scroll_for_locked_videos')
        except:
            CommonMethods.exception(driver, featureFileName, 'scroll_for_locked_videos')

    def verify_current_and_previous_node_txt(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.btn_continue)
            if check == False:
                logging.info("Node is changed")
            else :
                logging.info("Node is not Changed")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_current_and_previous_node_txt')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_current_and_previous_node_txt')

    def verify_node_name_and_locked_symbol(self, driver):
        try:
            check1 = CommonMethods.isElementPresent(driver, self.node_name_text)
            check2 = CommonMethods.isElementPresent(driver, self.lock_symbol_in_Journey_nodecard)
            if check1 == True and check2 == True :
                logging.info("Text and Locked symbol displayed")
            else :
                logging.info("Text and Locked symbol not displayed")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_node_name_and_locked_symbol')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_node_name_and_locked_symbol')
            
    def verify_msg_in_locked_node(self, driver, expMsg):
        try:
            actmsg = CommonMethods.getTextOfElement(driver, self.node_info_txt_In_nodecard)
            if expMsg == actmsg:
                logging.info(" message is present in node " + expMsg)
            else :
                logging.info(" message is not present in node" + expMsg)
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_msg_in_locked_node')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_msg_in_locked_node')

    def verify_resume_button(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.resume_btn)
            if check == True:
                logging.info("resume button displayed")
            else :
                logging.info("resume button not displayed")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_resume_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_resume_button')

    def click_on_resume_btn(self, driver):
        try:
            check = CommonMethods.elementClick(driver, self.resume_btn)
            if(check == True):
                logging.info('Successfully Tapped On Resume button ')
            else:
                logging.info('Failed to Tap On Resume button')
                logging.info("Failed Locator in Method clickOnResumeBtn")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_resume_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_resume_btn')
            
    def verify_nevigate_back_to_the_current_node(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.btn_continue)
            if check == True:
                logging.info("navigate back to the current node")
            else :
                logging.info("Failed to navigate to the current node")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_nevigate_back_to_the_current_node')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_nevigate_back_to_the_current_node')
    
    def scroll_for_resume(self, driver):
        try:
#             CommonMethods.wait_for_locator(driver, self.resume_btn, 15)
            check = CommonMethods.isElementPresent(driver, self.resume_btn)
            if check == False:
                while check == False:
                    currentNodeCords = self.scroll_in_journeys(driver)
                    driver.swipe(currentNodeCords['x'], currentNodeCords['y'], currentNodeCords['x'], currentNodeCords['y'] + 300)
                    check = CommonMethods.isElementPresent(driver, self.resume_btn)
            else:
                logging.info('Failed to find Resume button')
                logging.info("Failed Locator in Method scrollForResume")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'scroll_for_resume')
        except:
            CommonMethods.exception(driver, featureFileName, 'scroll_for_resume')

    def resource_q(self,driver):
        check2 = CommonMethods.isElementPresent(driver, self.resource_que_screen)
        if check2 == True:
            # CommonMethods.clickOnBackBtn(driver)
            resource_name = "Questions"
            logging.info(resource_name)
            logging.info("Questions resource screen displayed")
        else:
            logging.info("error")
    def after_any_resource(self, driver):
        try:
            sleep(3)
            resource_name = ""
            check1 = CommonMethods.isElementPresent(driver, self.video_name_in_resource_screen)
            check2 = CommonMethods.isElementPresent(driver, self.resource_que_screen)
            check3 = CommonMethods.isElementPresent(driver, self.concept_screen)
            if check1 == True :
                click_on_back_button(driver)  
                resource_name = "Video Screen"
                logging.info(resource_name)
                logging.info("video resource screen displayed")
            elif check2 == True :
                click_on_back_button(driver)  
                resource_name = "Questions"
                logging.info(resource_name)
                logging.info("Questions resource screen displayed")
            elif check3==True:
                click_on_back_button(driver)  
                resource_name = "concept screen"
                logging.info(resource_name)
                logging.info("concept screen displayed")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'after_any_resource')
        except:
            CommonMethods.exception(driver, featureFileName, 'after_any_resource')
        # return resource_name

#     def verify_resource_screen(self,driver):
#         try:
#             resource_name=""
#             check1 = CommonMethods.isElementPresent(driver, self.video_name_in_resource_screen)
#             check2 = CommonMethods.isElementPresent(driver, self.resource_que_screen)
#             if check1 == True :
#                 resource_name = "Video Screen"
#                 # logging.info(resource_name)
#                 logging.info("video resource screen displayed")
#             elif check2 == True:
#                 click_on_back_button(driver)
#                 resource_name = "Questions"
#                 # logging.info(resource_name)
#                 logging.info("Questions resource screen displayed")
#             else:
#                 logging.info('Failed to find Resource')
#                 logging.info("Failed Locator in Method afterAnyResource")
#                 pytest.fail("Failed Due to Locator in Journey map screen")
#         except NoSuchElementException:
#             CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_resource_screen')
#         except:
#             CommonMethods.exception(driver, featureFileName, 'verify_resource_screen')

    def find_optional_node(self, driver):
        try:
            self.after_any_resource(driver)
            op_node = CommonMethods.isElementPresent(driver, self.optional_node)
            if op_node == True:
                logging.info("optional node is present")   
            elif op_node == False:
                while op_node == False:
                    currentNodeCords = self.scroll_in_journeys_down(driver)
                    driver.swipe(currentNodeCords['x'], currentNodeCords['y'], currentNodeCords['x'], currentNodeCords['y'] - 200)
                    op_node = CommonMethods.isElementPresent(driver, self.optional_node)
                logging.info("optional node is present")
            else:
                logging.info('Failed to find optional node')
                logging.info("Failed Locator in Method findOptionalNode")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'find_optional_node')
        except:
            CommonMethods.exception(driver, featureFileName, 'find_optional_node')

    def journey_after_optional_node(self, driver):
        try:
            skipButton = CommonMethods.isElementPresent(driver, self.skip_btn_in_optional_frame)
            if skipButton == True:
                while skipButton == True:
                    currentNodeCords = self.scroll_in_journeys(driver)
                    driver.swipe(currentNodeCords['x'], currentNodeCords['y'], currentNodeCords['x'], currentNodeCords['y'] + 200)
                    skipButton = CommonMethods.isElementPresent(driver, self.skip_btn_in_optional_frame)
                    break
            else:
                logging.info("optional node is not present")
                logging.info("Failed Locator in Method journeyAfterOptionalNode")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'journey_after_optional_node')
        except:
            CommonMethods.exception(driver, featureFileName, 'journey_after_optional_node')
        
    def verify_optional_node(self, driver):
        try:
            op_node = CommonMethods.isElementPresent(driver, self.optional_node)
            if op_node==True:
                logging.info("optional node is present")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_optional_node')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_optional_node')

    def verify_optional_text(self, driver):
        try:
            op_node_text = CommonMethods.getTextOfElement(driver, self.optional_node)
            logging.info(op_node_text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_optional_text')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_optional_text')

    def verify_resource_icons_for_optional_node(self, driver):
        try:
            resources=CommonMethods.getElements( driver, self.resource_icons)
            logging.info(len(resources))
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_resource_icons_for_optional_node')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_resource_icons_for_optional_node')

    def verify_continue_and_skip_btn_on_optional_node(self, driver):
        try:
            continue_btn=CommonMethods.isElementPresent(driver, self.btn_continue)
            skip_btn=CommonMethods.isElementPresent(driver, self.skip_btn_in_optional_frame)
            if continue_btn==True and skip_btn==True:
                logging.info("continue and skip buttons are present")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_continue_and_skip_btn_on_optional_node')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_continue_and_skip_btn_on_optional_node')

    def click_on_skip_btn(self, driver):
        try:
            check = CommonMethods.elementClick(driver, self.skip_btn_in_optional_frame)
            if(check == True):
                logging.info('Successfully Tapped On Continue button ')
            else:
                logging.info('Failed to Tap On continue button')
                logging.info("Failed Locator in Method clickOnSkipBtn")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_skip_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_skip_btn')
    
    def find_resource_icons(self,driver):
        global icons
        icons=CommonMethods.getElements(driver, self.resource_icons)
        logging.info(icons)
        logging.info(len(icons))
        return icons

    def unique_resource_icons(self,driver):
        list_of_icons=self.find_resource_icons(driver)
        set_of_icons=set(list_of_icons)
        if len(list_of_icons)==len(set_of_icons):
            logging.info("all the icons are unique")
        else:
            logging.info("all the icons are not unique")

    def verify_video_resource(self, driver):
        try:
            logging.info("videoScreen is present")   
            CommonMethods.elementClick(driver, self.btn_next_in_videoscreen)
            badge_screen=CommonMethods.isElementPresent(driver, self.badges_close_btn)
            if badge_screen==True:
                CommonMethods.elementClick(driver, self.badges_close_btn)
            else:
                logging.info("Badge screen didn't display")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_resource')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_resource')
            
    def verify_question_resource(self, driver):
        try:
            logging.info("Question is present") 
            next_btn = CommonMethods.isElementPresent(driver, self.next_btn_in_question)
            if next_btn==True:
                logging.info("next button is present") 
            else:
                while next_btn==False:
                    currentNodeCords = self.scroll_in_journeys_down(driver)
                    driver.swipe(currentNodeCords['x'], currentNodeCords['y'], currentNodeCords['x'], currentNodeCords['y'] - 200)
                    next_btn = CommonMethods.isElementPresent(driver, self.next_btn_in_question)
                    break
            CommonMethods.elementClick(driver, self.next_btn) 
            badge_screen=CommonMethods.isElementPresent(driver, self.badges_close_btn)
            if badge_screen==True:
                CommonMethods.elementClick(driver, self.badges_close_btn)
            else:
                logging.info("Badge screen didn't display")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_question_resource')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_question_resource')
    
    def verify_rich_text_resource(self, driver):
        try:
            logging.info("Rich Text screen is present") 
            next_btn = CommonMethods.isElementPresent(driver, self.next_btn_in_richtext_screen)
            if next_btn==True:
                CommonMethods.elementClick(driver, self.next_btn)
            badge_screen=CommonMethods.isElementPresent(driver, self.badges_close_btn)
            if badge_screen==True:
                logging.info("Badge screen displayed")
                CommonMethods.elementClick(driver, self.badges_close_btn)
            else:
                logging.info("Badge screen didn't display")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_rich_text_resource')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_rich_text_resource')

    def match_resourceScreen_with_icons(self,driver):
        icons=self.find_resource_icons(driver)
        # logging.info(len(icons))
        if len(icons) >=1:
            for i in range(1,len(icons)):
                videoScreen = CommonMethods.isElementPresent(driver, self.video_name_in_resource_screen)
                if videoScreen==True:
                    self.verify_video_resource(driver)
                    i=i+1
                    break 
                question_screen = CommonMethods.isElementPresent(driver, self.resource_que_screen)
                if question_screen==True:
                    self.verify_question_resource(driver)
                    i=i+1
                    break
                rich_text_screen = CommonMethods.isElementPresent(driver, self.rich_text_screen)
                if rich_text_screen==True:
                    self.verify_rich_text_resource(driver)
                    i=i+1
                    break
    def click_on_start_button(self, driver):
        try:
            check = CommonMethods.elementClick(driver, self.btn_start)
            if(check == True):
                logging.info('Sucessfully Tapped On start button ')
            else:
                logging.info('Failed to Tap On start button')
                logging.info("Failed Locator in Method clickOn_start_button")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'clickOn_start_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'clickOn_start_button')

    def verify_already_taken_journey_in_journeymap(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.btn_continue)
            if check == True:
                logging.info("Journey already taken")
            else :
                logging.info("Journey is not taken previously")
                pytest.fail("Failed Due to Locator in Journey map screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_already_taken_journey_in_journeymap')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_already_taken_journey_in_journeymap')

    def scroll_till_first_node(self,driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.btn_continue)
            if check == True:
                logging.info("start button is changed in continue button ")
            first_node = CommonMethods.isElementPresent(driver, self.node_frame)
            if first_node == True:
                while first_node == False:
                    currentNodeCords = self.scroll_in_journeys_down(driver)
                    driver.swipe(currentNodeCords['x'], currentNodeCords['y'], currentNodeCords['x'],currentNodeCords['y'] - 200)
                    first_node = CommonMethods.isElementPresent(driver, self.node_frame)
                    break
                continue_btn = CommonMethods.isElementPresent(driver, self.btn_continue)
                logging.info("start button is changed in continue button ")
            else:
                logging.info("first node is not displayed")
                logging.info("Failed Locator in Method scroll_till_first_node")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'scroll_till_first_node')
        except:
            CommonMethods.exception(driver, featureFileName, 'scroll_till_first_node')

    def verify_countinue_btn(self,driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.btn_continue)
            if check == True:
                logging.info("already taken journey and continue button is displayed")
            else:
                logging.info("continue button is not displaying")
                logging.info("Failed Locator in Method verify_countinue_btn")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_countinue_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_countinue_btn')
            
    def click_on_trending_journey_card(self,driver):
        try:
            logging.info("trending journey")
            check = CommonMethods.isElementPresent(driver, self.trendingJourney_id)
            if check == True:
                CommonMethods.elementClick(driver, self.trendingJourney_id)
                logging.info("clicked on trending journey card")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_trending_journey_card')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_trending_journey_card')       
            
    def verify_resource_icons_in_node_card(self,driver):
        try:
            resources= CommonMethods.isElementPresent(driver, self.resource_icon)
            if resources == True:
                logging.info("resource icons are present")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_resource_icons_in_node_card')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_resource_icons_in_node_card')               