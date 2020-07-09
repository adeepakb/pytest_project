import sys
import os
import time

# from io import BytesIO
# from PIL import Image
# import math
# import numpy as np 
# from skimage.measure import compare_ssim
# import cv2
# from timeit import timeit


from appium import webdriver
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
# import inspect
from selenium.webdriver.common.by import By
import logging
import pytest
# from pyparsing import Char
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.common_methods import CommonMethods
# from Constants.load_json import getdata
from Utilities.interrupt import *
featureFileName = "Home Screen"
CommonMethods = CommonMethods()


class HomeScreen():
    
    home_screen_user_name=(By.ID,"com.byjus.thelearningapp.premium:id/header_title_text")
    greeting_text=(By.ID,"com.byjus.thelearningapp.premium:id/header_greeting_text")
    analytics_icon=(By.ID,"com.byjus.thelearningapp.premium:id/home_analytics")
    back_btn=(By.ID,"com.byjus.thelearningapp.premium:id/roundedNavButton")
    analytics_screen=(By.XPATH,"//android.widget.TextView[@text='Learning Analysis']")
    mathematics_card_xpath = (By.XPATH, "//android.widget.TextView[@text='Mathematics']")
    trendingJourney_id = (By.ID, "com.byjus.thelearningapp.premium:id/ivHighlight")
    Btn_library = (By.XPATH, "//android.widget.Button[@text='Library']")
    back_to_top_arrow=(By.ID,"com.byjus.thelearningapp.premium:id/backToTopClick")
    back_arrow = (By.ID,"com.byjus.thelearningapp.premium:id/backNav")
    
    badge_icon=(By.ID,"com.byjus.thelearningapp.premium:id/cvUserLevel")
    badge_screen=(By.XPATH,"//android.widget.TextView[@text='My Badges' and @resource-id='com.byjus.thelearningapp.premium:id/header_title_text']")
    badge_level=(By.ID,"com.byjus.thelearningapp.premium:id/tvLevelNumber")
    badge_name=(By.ID,"com.byjus.thelearningapp.premium:id/tvLevelName")
    
    subject_grid_view=(By.ID,"com.byjus.thelearningapp.premium:id/home_subject_gridLayout")
    subject_names=(By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/home_subject_view_layout']/descendant::android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/home_subject_name_txtvw']")
    
    
    recently_learned_card_header=(By.ID,"com.byjus.thelearningapp.premium:id/home_card_section_title")
    recently_learned_card_text=(By.ID,"com.byjus.thelearningapp.premium:id/home_card_title_text")
    forward_arrow_in_recent_learned_card=(By.ID,"com.byjus.thelearningapp.premium:id/home_card_section_right_arrow_button")
    recent_learned_screen=(By.XPATH,"//android.widget.TextView[@text='Recently Learned']")
    recently_learned_card=(By.ID,"com.byjus.thelearningapp.premium:id/home_card_Linear_layout")
    recently_learned_card_image=(By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/home_card_Linear_layout']/android.widget.LinearLayout[@index=0]")
    
    resume_journey_text=(By.XPATH,"//android.widget.TextView[@text='Resume Journey']")
    resume_journey_card=(By.XPATH,"//android.widget.TextView[@text='Resume Journey']/following-sibling::android.widget.FrameLayout/descendant::android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/home_card_Linear_layout']")
    
    
    top_one_recomeandation=(By.ID,"com.byjus.thelearningapp.premium:id/tvTopRecommendationTitle")
    top_pics_text=(By.ID,"com.byjus.thelearningapp.premium:id/tvRecommendationTitle")
    top_pics_card=(By.ID,"com.byjus.thelearningapp.premium:id/llTopRecommendation")
    top_pics_recomandation_bar=(By.ID,"com.byjus.thelearningapp.premium:id/rvRecommendation")
    cards_inside_recomandation_bar=(By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/rvRecommendation']/descendant::android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/tvName']")
    ele_for_scroll=(By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/rvRecommendation']/descendant::android.widget.LinearLayout[3]") 

    quizzo_text=(By.XPATH,"//android.widget.LinearLayout/descendant::android.widget.TextView[@text='Quizzo']")
    quizzo_card=(By.XPATH,"//android.widget.LinearLayout/descendant::android.widget.TextView[@text='Quizzo']/following-sibling::android.widget.FrameLayout")
    quizzo_hero_image=(By.XPATH,"//android.widget.TextView[@text='Quizzo']/following-sibling::android.widget.FrameLayout/descendant::android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/home_card_Linear_layout']/descendant::android.widget.LinearLayout[@index=0][1]")
    quizzo_card_header_text=(By.XPATH,"//android.widget.TextView[@text='Play Quizzo challenge!']")
    quizzo_card_sub_title=(By.XPATH,"//android.widget.TextView[@text='Match your wits with other students? Play Quizzo now!']")
    quizzo_forward_arrow=(By.XPATH,"//android.widget.TextView[@text='Quizzo']/following-sibling::android.widget.FrameLayout/descendant::android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/home_card_section_right_arrow_button']")
    quizzo_screen=(By.ID,"com.byjus.thelearningapp.premium:id/btnQuizzoChallenge")
    
    byjus_corner_text=(By.ID,"com.byjus.thelearningapp.premium:id/home_discover_txtvw_title")
    byjus_corner_card_text=(By.XPATH,"//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/home_discover_nametxtv'][1]")
    byjus_corner_forward_arrow=(By.ID,"com.byjus.thelearningapp.premium:id/button_show_all")
    byjus_corner_see_all_text=(By.XPATH,"//android.widget.TextView[@text='See All']")
    byjus_corner_cards_bar=(By.ID,"com.byjus.thelearningapp.premium:id/home_discover_lstvw")
    byjus_corner_screen_title=(By.ID,"com.byjus.thelearningapp.premium:id/home_discover_lstvw")
    byjus_corner_screen_description=(By.ID,"com.byjus.thelearningapp.premium:id/discover_detail_webview")
    byjus_corner_screen_other_content=(By.ID,"com.byjus.thelearningapp.premium:id/discover_detail_more_from_channel_txtvw")
    byjus_corner_bar_first_ele=(By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/home_discover_lstvw']/descendant::android.widget.FrameLayout[2]")
    byjus_corner_first_article=(By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/home_discover_lstvw']/descendant::android.widget.FrameLayout[1]")
    byjus_corner_screen=(By.ID,"com.byjus.thelearningapp.premium:id/toolbar_title")
    byjus_corner_text_video_icon=(By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/home_discover_icon_imgvw']")
    
    share_the_app_text=(By.ID,"com.byjus.thelearningapp.premium:id/home_card_section_title")
    share_the_app_card=(By.XPATH,"//android.widget.TextView[@text='Share the app']/following-sibling::android.widget.FrameLayout/descendant::android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/home_card_Linear_layout']")
    share_the_app_hero_image=(By.XPATH,"//android.widget.TextView[@text='Share the app']/following-sibling::android.widget.FrameLayout/descendant::android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/home_card_Linear_layout']/descendant::android.widget.LinearLayout[@index=0][1]")
    share_with_friends_txt=(By.ID,"com.byjus.thelearningapp.premium:id/home_card_title_text")
    share_the_app_subtitle_txt=(By.XPATH,"//android.widget.TextView[@text='Share the app']/following-sibling::android.widget.FrameLayout/descendant::android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/home_card_sub_title_text']")
    share_the_app_forward_arrow=(By.XPATH,"//android.widget.TextView[@text='Share the app']/following-sibling::android.widget.FrameLayout/descendant::android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/home_card_section_right_arrow_button']")
    share_pop_up_txt=(By.ID,"com.byjus.thelearningapp.premium:id/shareTitle")
    share_pop_up_share_list=(By.ID,"com.byjus.thelearningapp.premium:id/share_list")
    share_pop_up_list_item=(By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/share_list']/descendant::android.widget.LinearLayout[1]")
    share_pop_up_gmail_app_icon=(By.XPATH,"//androidx.recyclerview.widget.RecyclerView/descendant::android.widget.TextView[@text='Gmail']")
    gmail_compose_mail_with_share_link=(By.ID,"com.google.android.gm:id/action_bar_root")
    gmail_compose_mail_send_icon=(By.ID,"com.google.android.gm:id/send")
    
    hamburger_menu_button=(By.ID,"com.byjus.thelearningapp.premium:id/backNav")
    user_image_in_home_drawer=(By.ID,"com.byjus.thelearningapp.premium:id/home_drawer_imgvw_profile")
    home_drawer=(By.ID,"com.byjus.thelearningapp.premium:id/home_drawer_header_view")
    home_drawer_profile_name=(By.ID,"com.byjus.thelearningapp.premium:id/home_drawer_txtvw_profile_name")
    home_drawer_grade=(By.ID,"com.byjus.thelearningapp.premium:id/home_drawer_txtvw_course")
    home_drawer_forwar_arrow=(By.ID,"com.byjus.thelearningapp.premium:id/home_drawer_imgvw_arrow_right")
    grade_selection_drop_dwn=(By.ID,"com.byjus.thelearningapp.premium:id/tvGrade")
    total_subjects=(By.XPATH,"//android.widget.GridLayout/descendant::android.widget.TextView")
    
    goggle_icon=(By.ID,"com.byjus.thelearningapp.premium:id/homeCameraX")
    camera_permission_agree_btn=(By.ID,"com.byjus.thelearningapp.premium:id/primaryAction")
    camera_permission_no_thanks_btn=(By.ID,"com.byjus.thelearningapp.premium:id/secondaryAction")
    camera_allow_popup=(By.ID,"com.android.packageinstaller:id/permission_allow_button")
    camera_btn_in_camer_screen= (By.ID,"com.android.packageinstaller:id/permission_allow_button")
    camera_permission_pop_up=(By.ID,"com.byjus.thelearningapp.premium:id/dialog_layout")
    
    request_home_dmo_btn=(By.ID,"com.byjus.thelearningapp.premium:id/home_drawer_txtvw_home_demo")
    live_classes = (By.XPATH,"//android.widget.TextView[@text='Live Classes']")
    
    def __init__(self, browser):
        self.browser = browser
        
    def verify_home_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.home_screen_user_name)
            if check == True:
                logging.info("Home screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_home_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_home_screen')
    
    def verify_greeting_msg(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.greeting_text)
            if check == True:
                grtn_txt=CommonMethods.getTextOfElement(browser, self.greeting_text)
                logging.info("greeting text is displayed "+grtn_txt)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_greeting_msg')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_greeting_msg')
            
    def click_on_badges_level_icon(self, browser):
        try:
            CommonMethods.elementClick(browser, self.badge_icon)
            logging.info('Successfully Tapped On badges level icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_badges_level_icon')
            
    def click_on_analytics_icon(self, browser):
        try:
            CommonMethods.elementClick(browser, self.analytics_icon)
            logging.info('Successfully Tapped On analytics icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_analytics_icon')
    
    def verify_analytics_icon(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.analytics_icon)
            if check == True:
                logging.info("Analytics icon is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_analytics_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_analytics_icon')
    
    def verify_badges_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.badge_screen)
            if check == True:
                logging.info("Badges screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_badges_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_badges_screen')
            
    def verify_analytics_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.analytics_screen)
            if check == True:
                logging.info("analytics screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_analytics_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_analytics_screen')
    def click_on_back_arrow(self, browser):
        try:
            CommonMethods.elementClick(browser, self.back_btn)
            logging.info('Successfully clicked on back arrow button')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_back_arrow')
          
    def click_on_subject_maths(self, browser):
        try:
            CommonMethods.elementClick(browser, self.mathematics_card_xpath)
            logging.info('Successfully Tapped on subject card Mathamatics')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_subject_maths')
            
    def verify_chapter_list_screen(self, browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.Btn_library)
            if check == True:
                logging.info("chapter list screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_chapter_list_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_chapter_list_screen')
    
    def verify_recently_learned_text(self,text,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.recently_learned_card_header)
            if check == True:
                header_text=CommonMethods.getTextOfElement(browser, self.recently_learned_card_header)
                if header_text == text:
                    logging.info("The recently learned card header text is same :"+header_text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_recently_learned_text')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_recently_learned_text')
    def verify_recently_learned_card_text(self,text,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.recently_learned_card_text)
            if check == True:
                card_text=CommonMethods.getTextOfElement(browser, self.recently_learned_card_text)
                if card_text == text:
                    logging.info("The recently learned card text is same :"+card_text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_recently_learned_card_text')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_recently_learned_card_text')   
    
    def verify_forward_icon_in_recently_learned(self, browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.forward_arrow_in_recent_learned_card)
            if check == True:
                logging.info("forward icon is present in recently learned card")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_forward_icon_in_recently_learned')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_forward_icon_in_recently_learned')
    
    def verify_recently_learned_screen(self, browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.recent_learned_screen)
            if check == True:
                logging.info("recently learned screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_recently_learned_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_recently_learned_screen')
    
    def verify_image_of_recently_learned_card(self, browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.recently_learned_card_image)
            if check == True:
                logging.info("hero image is present in recently learned card")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_image_of_recently_learned_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_image_of_recently_learned_card')
    
    def click_on_recently_learned_card(self, browser):
        try:
            CommonMethods.elementClick(browser, self.recently_learned_card)
            logging.info('Successfully clicked on recently learned card')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_recently_learned_card')

    def create_recently_learned_card(self,browser):
        try:
            CommonMethods.elementClick(browser, self.mathematics_card_xpath)
            CommonMethods.wait_for_locator(browser, self.trendingJourney_id, 5)
            CommonMethods.elementClick(browser, self.trendingJourney_id)
            check=CommonMethods.isElementPresent(browser, self.greeting_text)
            if check==False:
                while check == False:
                    click_on_back_button(browser)
                    check=CommonMethods.isElementPresent(browser, self.greeting_text)
#             CommonMethods.elementClick(browser, self.back_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'create_recently_learned_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'create_recently_learned_card')
    
    def verify_recently_learned_card(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.recently_learned_card)
            if check == True:
                logging.info("recently learned card is present")
            else:
#                 self.create_recently_learned_card(browser)             
                browser.swipe(300, 400, 300,100 )
            logging.info("recently learned card is present")   
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_recently_learned_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_recently_learned_card')
    
    def verify_recomandation_bar(self,browser):
        try:
            check= CommonMethods.isElementPresent(browser, self.top_pics_recomandation_bar)
            if check== True:
                logging.info('Recommendation bar is displayed in Top Pics')
            else:
                while check== False:
                    browser.swipe(300, 600, 300,10 )
                    check= CommonMethods.isElementPresent(browser, self.top_pics_recomandation_bar)
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_recently_learned_card')
    
    def verify_seven_cards_of_top_pics(self,browser):
        try:
            dict_of_cards={}
            length_of_dict=len(dict_of_cards.keys())
            first_key=CommonMethods.getTextOfElement(browser, self.top_one_recomeandation)
            dict_of_cards.setdefault(first_key,None)
            for count in range(0,5):  
                for i in CommonMethods.getElements(browser, self.cards_inside_recomandation_bar):
#                     logging.info(i.text)
                    dict_of_cards.setdefault(i.text,None)
                    recomandation_bar=CommonMethods.getElement( browser, self.ele_for_scroll)
                    chord=recomandation_bar.location_in_view
                    browser.swipe(chord['x'], chord['y'], chord['x']-100, chord['y']) 
            if len(dict_of_cards.keys())==7:
                logging.info("all seven cards of Top Pics are")
            for j in dict_of_cards.keys():
                logging.info(j)   
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_seven_cards_of_top_pics')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_seven_cards_of_top_pics')
    
    def click_on_first_top_picks_card(self, browser):
        try:
            name_of_card=CommonMethods.getTextOfElement(browser, self.top_one_recomeandation)
            CommonMethods.elementClick(browser, self.top_one_recomeandation)
#             set_connection_type(browser, "DATA_ONLY")
            logging.info('Successfully clicked on Top Picks card :'+name_of_card)
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_first_top_picks_card')
        return name_of_card
    
    def verify_quizzo_card(self, browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.quizzo_card)
            if check == False:
                while check==False:
                    browser.swipe(300, 600, 300, 100 )
                    check = CommonMethods.isElementPresent(browser, self.quizzo_card)
            logging.info("quizzo card is present")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_quizzo_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_quizzo_card')
         
    def verify_quizzo_text(self, browser,text):
        try:
            text_quizzo=CommonMethods.getTextOfElement(browser, self.quizzo_text)
            if text==text_quizzo:
                logging.info('Quizzo text is present')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_quizzo_text')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_quizzo_text')

    def verify_quizzo_hero_image(self, browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.quizzo_hero_image)
            if check==True:
                logging.info('Quizzo hero image is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_quizzo_hero_image')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_quizzo_hero_image')

    def verify_quizzo_play_text(self, browser,text):
        try:
            text_quizzo=CommonMethods.getTextOfElement(browser, self.quizzo_card_header_text)
            if text==text_quizzo:
                logging.info('Quizzo card header text is present '+text_quizzo)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_quizzo_play_text')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_quizzo_play_text')

    def verify_quizzo_forward_icon(self, browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.quizzo_forward_arrow)
            if check==True:
                logging.info('Quizzo forward icon is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_quizzo_forward_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_quizzo_forward_icon')
    
    def verify_user_name(self, browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.home_screen_user_name)
            if check==True:
                logging.info('user name is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_user_name')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_user_name')
            
    
    def click_on_quizzo_card(self, browser):
        try:
            CommonMethods.elementClick(browser, self.quizzo_card)
            logging.info('Successfully clicked on quizzo card')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_quizzo_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_quizzo_card')

    def verify_quizzo_screen(self, browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.quizzo_screen)
            if check == True:
                logging.info("quizzo screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_quizzo_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_quizzo_screen')
            
    def verify_byjus_corner_card(self, browser): 
        try:
            check_byjus_corner_card = browser.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().resourceId(\"com.byjus.thelearningapp.premium:id/home_scroll_view\")).setAsVerticalList().scrollIntoView("
            + "new UiSelector().textContains(\"BYJU'S Corner\"))")
            logging.info("byjus corner card is present")
            if check_byjus_corner_card !=None:
                logging.info("byjus corner card is present")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_byjus_corner_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_byjus_corner_card')
    

    def verify_byjus_corner_text(self, browser,text):
        try:
            text_byjus=CommonMethods.getTextOfElement(browser, self.byjus_corner_text)
            if text==text_byjus:
                logging.info('byjus corner text is present '+ text_byjus)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_byjus_corner_text')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_byjus_corner_text')
            
    def verify_byjus_corner_card_bottom_text(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.byjus_corner_card_text)
            if check == True:
                logging.info("byjus corner card text is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_byjus_corner_card_bottom_text')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_byjus_corner_card_bottom_text')
    
    def verify_byjus_corner_seeall_forward_icon(self,browser):
        try:
            check_seeall = browser.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().resourceId(\"com.byjus.thelearningapp.premium:id/home_discover_lstvw\")).setAsHorizontalList().scrollIntoView("
                            +"new UiSelector().textContains(\"See All\"))")
            if check_seeall != None:
               logging.info("See All and forward icon is displayed")     
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_byjus_corner_seeall_forward_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_byjus_corner_seeall_forward_icon')
    
    def click_an_article_byjus_corner(self, browser):
        try:
            CommonMethods.elementClick(browser, self.byjus_corner_first_article)
            logging.info('Successfully clicked on byjus corner article')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_an_article_byjus_corner')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_an_article_byjus_corner')
    
    def verify_byjus_corner_article_title(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.byjus_corner_screen_title)
            if check == True:
                logging.info("inside byjus corner article title is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_byjus_corner_article_title')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_byjus_corner_article_title')
           
    def verify_byjus_corner_article_description(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.byjus_corner_screen_description)
            if check == True:
                logging.info("inside byjus corner article description is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_byjus_corner_article_description')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_byjus_corner_article_description')
    
    def verify_byjus_corner_article_other_content(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.byjus_corner_screen_other_content)
            if check==True:
                logging.info("inside byjus corner article other content is displayed")
            elif check == False:
                while check==False:
                    browser.swipe(300, 700, 300, 10 )
                    check = CommonMethods.isElementPresent(browser, self.byjus_corner_screen_other_content)
                logging.info("inside byjus corner article other content is displayed")
            else:
                logging.info("inside byjus corner article other content is not displayed")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_byjus_corner_article_other_content')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_byjus_corner_article_other_content')
     
    def click_on_see_all_icon(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.byjus_corner_see_all_text)
            if check==True:
                CommonMethods.elementClick(browser, self.byjus_corner_see_all_text)
                logging.info('Successfully clicked on byjus corner see all icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_see_all_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_see_all_icon')
    
    def verify_byjus_corner_screen(self, browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.byjus_corner_screen)
            if check == True:
                logging.info("bujus corner screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_byjus_corner_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_byjus_corner_screen')
    
    def verify_share_the_app_card(self, browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.share_the_app_card)
            if check == False:
                while check==False:
                    browser.swipe(300, 700, 300, 200 )
                    check = CommonMethods.isElementPresent(browser, self.share_the_app_card)
            logging.info("byjus share the app card is present")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_share_the_app_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_share_the_app_card')
   
    def verify_share_the_app_txt(self, browser,text):
        try:
            text_byjus=CommonMethods.getTextOfElement(browser, self.share_the_app_text)
            if text==text_byjus:
                logging.info('share the app text is present '+ text_byjus)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_share_the_app')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_share_the_app')
    
    def verify_share_the_app_hero_image(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.share_the_app_hero_image)
            if check == True:
                logging.info("share the app hero image is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_share_the_app_hero_image')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_share_the_app_hero_image')
                     
    def verify_seven_cards_of_top_pics_varient_c(self,browser):
        try:
            dict_of_cards={}
            length_of_dict=len(dict_of_cards.keys())
            first_key=CommonMethods.getTextOfElement(browser, self.top_one_recomeandation)
            dict_of_cards.setdefault(first_key,None)
            for count in range(0,5):  
                for i in CommonMethods.getElements(browser, self.cards_inside_recomandation_bar):
#                     logging.info(i.text)
                    dict_of_cards.setdefault(i.text,None)
                    recomandation_bar=CommonMethods.getElement( browser, self.ele_for_scroll)
                    chord=recomandation_bar.location_in_view
                    browser.swipe(chord['x'], chord['y'], chord['x']-200, chord['y']) 
            if len(dict_of_cards.keys())==7:
                for j in dict_of_cards.keys():
                    if j == 'Practice':
                        logging.info("prtice card is present")
                    elif j == 'Quizzo':
                        logging.info("Quizzo card is present")
                    elif j == 'Test':
                        logging.info("Test card is present")
                    else:
                        logging.info("Journey or discovery card name is :"+j)    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_seven_cards_of_top_pics_varient_c')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_seven_cards_of_top_pics_varient_c')
                    
    def verify_share_the_app_subtitle_txt(self, browser,text):
        try:
            text_byjus=CommonMethods.getTextOfElement(browser, self.share_the_app_subtitle_txt)
            if text==text_byjus:
                logging.info('share the app subtitle text is present '+ text_byjus)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_share_the_app_subtitle_txt')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_share_the_app_subtitle_txt')
    
    def verify_share_the_app_forward_icon(self, browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.share_the_app_forward_arrow)
            if check==True:
                logging.info('share the app forward icon is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_share_the_app_forward_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_share_the_app_forward_icon')
    
    def click_on_share_the_app_card(self, browser):
        try:
            CommonMethods.elementClick(browser, self.share_the_app_card)
            logging.info('Successfully clicked on byjus share the app card')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_share_the_app_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_share_the_app_card')
    
    def verify_share_the_app_pop_up(self, browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.share_the_app_text)
            if check==True:
                logging.info('share the app pop up is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_share_the_app_pop_up')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_share_the_app_pop_up')
    def click_on_gmail_app_icon(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.share_pop_up_gmail_app_icon, 5)
            check = CommonMethods.isElementPresent(browser, self.share_pop_up_gmail_app_icon)
            if check == True:
                CommonMethods.elementClick(browser, self.share_pop_up_gmail_app_icon)
                logging.info('Successfully clicked on Gmail app icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_gmail_app_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_gmail_app_icon')
    def verify_compose_mail_send_button(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.gmail_compose_mail_send_icon, 5)
            check=CommonMethods.isElementPresent(browser, self.gmail_compose_mail_send_icon)
            if check==True:
                logging.info('compose_mail is generated and send button is displayed so user can share the link through Gmail')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_compose_mail_send_button')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_compose_mail_send_button')
    def verify_app_quit(self, browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.home_screen_user_name)
            if check==False:
                logging.info('App is closed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_app_quit')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_app_quit')
    
    def verify_badge_icon_level_name(self, browser):
        try:
            check_badge_icon=CommonMethods.isElementPresent(browser, self.badge_icon)
            check_badge_level=CommonMethods.isElementPresent(browser, self.badge_level)
            check_badge_name=CommonMethods.isElementPresent(browser, self.badge_name)
            if check_badge_icon and check_badge_level and check_badge_name == True:
                logging.info('Badge Icon, badge level and badge name are displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_badge_icon_level_name')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_badge_icon_level_name')
                   
    def verify_subject_grid_view(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.subject_grid_view)
            if check == True:
                logging.info("subject grid view is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_subject_grid_view')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_subject_grid_view')
            
    def verify_resume_journey_card(self,browser):
        try:
            check= CommonMethods.isElementPresent(browser, self.resume_journey_card)
            if check== True:
                logging.info('Resume journey card is displayed in Top Pics')
            else:
                while check== False:
                    browser.swipe(300, 600, 300,10 )
                    check= CommonMethods.isElementPresent(browser, self.resume_journey_card)
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_resume_journey_card')
    
    def click_on_hamburger_menu(self, browser):
        try:
            CommonMethods.elementClick(browser, self.hamburger_menu_button)
            logging.info('Successfully clicked on hamburger menu')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_hamburger_menu')
          
    
    def verify_home_drawer(self, browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.home_drawer)
            if check==True:
                logging.info('Home drawer is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_home_drawer')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_home_drawer')
            
    def verify_user_name_profile_image(self, browser):
        try:
            check_user_name=CommonMethods.isElementPresent(browser, self.home_screen_user_name)
            check_profile_image=CommonMethods.isElementPresent(browser, self.user_image_in_home_drawer)
            
            if check_user_name and check_profile_image == True:
                logging.info('In home drawer user name and profile image are displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_user_name_profile_image')        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_user_name_profile_image')

    def verify_grade_in_home_drawer(self, browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.home_drawer_grade)
            if check==True:
                logging.info('grade is displayed in Home drawer ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_grade_in_home_drawer')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_grade_in_home_drawer')
            
    def verify_forward_arrow_in_home_drawer(self, browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.home_drawer_forwar_arrow)
            if check==True:
                logging.info('forward arrow is displayed in Home drawer ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_forward_arrow_in_home_drawer')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_forward_arrow_in_home_drawer')
                    
    def verify_icons_image_and_separate_line(self, browser,text):
        try:
            exit_count = 0
            icon_text=(By.XPATH,"//android.widget.TextView[@text='"+text+"']")
            icon_image=(By.XPATH,"//android.widget.TextView[@text='"+text+"']/preceding-sibling::android.widget.ImageView")
            icon_seperate_thin_line=(By.XPATH,"//android.widget.TextView[@text='"+text+"']/following-sibling::android.view.View")
            check_icon_text=CommonMethods.isElementPresent(browser,icon_text)
            if check_icon_text==True:
                check_icon_image=CommonMethods.isElementPresent(browser, icon_image)
                check_icon_separate_line=CommonMethods.isElementPresent(browser, icon_seperate_thin_line)
                if check_icon_image and check_icon_separate_line== True:
                    logging.info("In home drawer "+text+" , "+text+" image and separate line are displayed")
                    exit_count = exit_count+1
            elif check_icon_text==False:
                while check_icon_text==False:
                    browser.swipe(300, 600, 300,10 )
                    check_icon_text=CommonMethods.isElementPresent(browser,icon_text)
                    exit_count = exit_count+1
                    if exit_count==20:
                        break
                check_icon_image=CommonMethods.isElementPresent(browser, icon_image)
                check_icon_separate_line=CommonMethods.isElementPresent(browser, icon_seperate_thin_line)
                if check_icon_image and check_icon_separate_line== True:
                    logging.info("In home drawer "+text+" , "+text+" image and separate line are displayed")
                    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_icons_image_and_separate_line')        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_icons_image_and_separate_line')
            
    def verify_request_home_demo_btn(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.request_home_dmo_btn)
            if check == True:
                logging.info("request home demo button is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_request_home_demo_btn')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_request_home_demo_btn')
    
    def get_subject_count(self,browser):
        try:
            CommonMethods.wait_for_locator(browser, self.total_subjects, 15)
            subjects=CommonMethods.getElements(browser, self.total_subjects)
#             logging.info(len(subjects))  
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'get_subject_count')
        except:
            CommonMethods.exception(browser, featureFileName, 'get_subject_count')
        return len(subjects)
                   
    def switch_grade(self,browser,text):
        try:
#             grade_xpath=(By.XPATH,"//android.widget.TextView[@text='6th grade']")
            grade_xpath=(By.XPATH,"//android.widget.TextView[@text='"+text+"']")
            self.click_on_hamburger_menu(browser)
            CommonMethods.wait_for_locator(browser, self.home_drawer_grade, 5)
            CommonMethods.elementClick(browser, self.home_drawer_grade)
            CommonMethods.wait_for_locator(browser, self.grade_selection_drop_dwn, 5)
            CommonMethods.elementClick(browser, self.grade_selection_drop_dwn)
            sleep(2)
            CommonMethods.elementClick(browser, grade_xpath)
#             click_on_back_button(browser)
            CommonMethods.wait_for_locator(browser, self.back_arrow, 5)
            logging.info(text)
            CommonMethods.elementClick(browser, self.back_arrow)
#             CommonMethods.click_on_device_back_btn(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'switch_grade')
        except:
            CommonMethods.exception(browser, featureFileName, 'switch_grade')
    
    def odd_sub_left_alligned(self,browser):
        self.switch_grade(browser, '6th grade')
        sub_in_6th_grade=self.get_subject_count(browser)
        logging.info("subjects in 6th grade :"+str(sub_in_6th_grade))
        self.switch_grade(browser, "8th Grade")
        sub_in_8th_grade=self.get_subject_count(browser)
        logging.info("subjects in 8th grade :"+str(sub_in_8th_grade))
        if (sub_in_6th_grade) % 2 !=0:
            last_subject=(By.XPATH,"//android.widget.GridLayout[@resource-id='com.byjus.thelearningapp.premium:id/home_subject_gridLayout']/descendant::android.widget.RelativeLayout[@index=sub_in_6th_grade]")   
            CommonMethods.isElementPresent(browser, last_subject)  
            logging.info("subject in 6th grade are odd in numbers and it is alligned left")
    
    def click_on_goggles_icon(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.goggle_icon)
            if check==True:
                CommonMethods.elementClick(browser, self.goggle_icon)
                logging.info('Successfully clicked on goggles icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_goggles_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_goggles_icon')
    
    def verify_camera_screen(self, browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.camera_btn_in_camer_screen)
            if check == True:
                logging.info("camera screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_camera_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_camera_screen')
    
    def verify_camera_permission_popup(self, browser): 
        try:
            check = CommonMethods.isElementPresent(browser, self.camera_permission_pop_up)
            if check == True:
                CommonMethods.elementClick(browser, self.camera_permission_no_thanks_btn)
                logging.info("camera permission pop up is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_camera_permission_popup')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_camera_permission_popup')
    
    def check_live_classes_option(self,browser):
        check = CommonMethods.isElementPresent(browser, self.live_classes)
        if check == True:
            logging.info("live classes option is present")
            pytest.fail("failed because some new temporary options are added in Hemburger menu ")