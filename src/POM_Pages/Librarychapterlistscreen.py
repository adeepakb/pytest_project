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

from Utilities.common_methods import CommonMethods
from Constants.load_json import getdata

from POM_Pages.personalizedChapterList import PersonalizedChapterList
featureFileName = "Library chapter list screen"
CommonMethods = CommonMethods()


class LibraryChapterListsScreen():
    personalised_btn = (By.XPATH, "//android.widget.Button[@text='Personalised']")
    btn_library = (By.XPATH, "//android.widget.Button[@text='Library']")
    Btn_library_when_text_isnot_there = (By.XPATH, "(//android.widget.Button[@resource-id='com.byjus.thelearningapp.premium:id/roundedNavButton'])[2]")
    btn_back_arrow = (By.XPATH, "(//android.widget.Button[@resource-id='com.byjus.thelearningapp.premium:id/roundedNavButton'])[1]")
    txt_greeting_text = (By.ID, "com.byjus.thelearningapp.premium:id/header_greeting_text")
    btn_practice = (By.ID, "com.byjus.thelearningapp.premium:id/practice_mode_bottom_txtvw")
    txt_practice_in_practice_screen = (By.ID, "com.byjus.thelearningapp.premium:id/header_subtitle1_text")
    btn_test = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_list_item_test_txtvw")
    txt_test_in_test_screen = (By.ID, "com.byjus.thelearningapp.premium:id/header_subtitle1_text")
    video_cards = (By.XPATH, "//android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_list_video_color_imgvw']")
    video_id_in_video_screen = (By.ID, "com.byjus.thelearningapp.premium:id/exo_subtitles")
    chapter_names = (By.XPATH, "//android.widget.LinearLayout/descendant::android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_title_view']")
    video_title_in_video_screen = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_title_2")
    video_count = (By.XPATH, "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/video_count']")
#     chapterCountOfParticularChapterName=//android.widget.LinearLayout/descendant::android.widget.TextView[@text='Rational Numbers']/following-sibling::android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/video_count']
    total_chapters = (By.ID, "com.byjus.thelearningapp.premium:id/header_subtitle_text")
    video_thumbnail = (By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_video_name_txtvw']")
    video_progression_bar = (By.XPATH, "//android.widget.LinearLayout/descendant::android.widget.ProgressBar[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_progress_view']")
    txt_chapters = (By.ID, "com.byjus.thelearningapp.premium:id/chapterlistTitle")
    btn_optional_nav = (By.ID, "com.byjus.thelearningapp.premium:id/optionalNav")
    
    def __init__(self, driver):
        self.driver = driver
        self.personalised_screen = PersonalizedChapterList(driver)
        

    def click_on_personlised_button(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.personalised_btn, 3)
            check = CommonMethods.elementClick(driver, self.personalised_btn)
            if(check == True):
                logging.info('Successfully Tapped On Personalised button ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_personlised_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_personlised_button')
            
    def verify_personalised_screen(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.btn_library)
            if check == True:
                logging.info("Personalised chapter list screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_personalised_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_personalised_screen')
            
    def click_on_back_arrow(self, driver):
        try:
            check = CommonMethods.elementClick(driver, self.btn_back_arrow)
            if(check == True):
                logging.info('Successfully Tapped On back arrow button ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_back_arrow')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_back_arrow')

    def verify_home_screen(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.txt_greeting_text)
            if check == True:
                logging.info("Home screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_home_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_home_screen')
            
    def verify_library_screen(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.personalised_btn)
            if check == True:
                logging.info("library chapter list screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_library_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_library_screen')
    
    def click_on_practice_button(self, driver):
        try:
            check = CommonMethods.elementClick(driver, self.btn_practice)
            if(check == True):
                logging.info('Successfully Tapped On practice button ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_practice_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_practice_button')

    def verify_practice_screen(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.txt_practice_in_practice_screen)
            if check == True:
                logging.info("library chapter list screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_practice_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_practice_screen')
            
    def click_on_test_button(self, driver):
        try:
            check = CommonMethods.elementClick(driver, self.btn_test)
            if(check == True):
                logging.info('Successfully Tapped On Test button ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_test_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_test_button')
            
    def verify_test_screen(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.txt_test_in_test_screen)
            if check == True:
                logging.info("Test screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_test_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_test_screen')
      

    def click_on_video_card(self, driver):
        try:
            sleep(3)
            video_card1 = CommonMethods.getElements(driver, self.video_cards)
            global chapter_name
            chapter_name = video_card1[1].text
            logging.info(chapter_name)
            video_card1[1].click()
            logging.info('Successfully Tapped On video card ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_video_card')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_video_card')

    def verify_video_screen_of_perticular_chapter(self, driver):
        try:
            chapter_name_of_video = CommonMethods.getTextOfElement(driver, self.video_title_in_video_screen)
            logging.info(chapter_name_of_video)
            if chapter_name == chapter_name_of_video:
                logging.info("Video screen is displayed of particular chapter")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_screen_of_perticular_chapter')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_screen_of_perticular_chapter')
     
    def chapter_name_with_total_video_count(self, driver):
        dict_of_chapter_and_video_count = {}
        try:
            count = self.personalised_screen.chapter_count(driver)
#             count = self.chapter_count(driver)
            logging.info(count)
            for i in range(1, count):
                list_of_chapters = CommonMethods.getElements(driver, self.chapter_names)
                list_of_video_count = CommonMethods.getElements(driver, self.video_count)
                
                for j, k in zip(list_of_chapters, list_of_video_count):
                    list1 = CommonMethods.ConvertStringInToList(k.text)
                    totalvideos = int(list1[0])
                    dict_of_chapter_and_video_count.setdefault(j.text, totalvideos)
                driver.swipe(300, 500, 300, 100)
                sleep(1)
            logging.info(dict_of_chapter_and_video_count)


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'chapter_name_with_total_video_count')
        except:
            CommonMethods.exception(driver, featureFileName, 'chapter_name_with_total_video_count')
        return dict_of_chapter_and_video_count

    def verify_video_corousel(self, driver):
        try:
            dict_of_chapter_and_video_count = {}
            dict_of_chapter_and_video_count = self.chapter_name_with_total_video_count(driver)
            CommonMethods.elementClick(driver, self.btn_optional_nav)
            sleep(1)
            CommonMethods.elementClick(driver, self.btn_library)
            sleep(1)
            for i in dict_of_chapter_and_video_count:
                videoCouroselXpath = (By.XPATH, "//android.widget.TextView[@text='" + i + "']/parent::android.widget.RelativeLayout/following-sibling::androidx.recyclerview.widget.RecyclerView")
                check = CommonMethods.isElementPresent(driver, videoCouroselXpath)
                if check == True:
                    logging.info("video carousel is present for chapter " + i)
                    driver.swipe(300, 500, 300, 100)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyVideoCorousel')

    def chapter_names_without_video(self, driver):
        try:
            dict_of_chapters_without_video = {}
            dict_of_chapter_and_video_count = self.chapter_name_with_total_video_count(driver)
            for ele in dict_of_chapter_and_video_count:
                logging.info(ele)
                logging.info(dict_of_chapter_and_video_count[ele])
                if dict_of_chapter_and_video_count[ele] == 0:
                    dict_of_chapters_without_video.setdefault(ele, 0)
                    logging.info("videos are not available for this chapter " + ele)
                    pytest.fail("Failed in Library Chapter List")
                    logging.info("Failed in Method chapter_names_without_video")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'chapter_names_without_video')
        except:
            CommonMethods.exception(driver, featureFileName, 'chapter_names_without_video')
        return dict_of_chapters_without_video

    def for_scrolling_up(self, driver):
        CommonMethods.elementClick(driver, self.btn_optional_nav)
        sleep(1)
        CommonMethods.elementClick(driver, self.btn_library)
        sleep(1)    

#     def verify_test_and_practice_icons(self, driver):
#         try: 
#             exit_count = 0
#             self.for_scrolling_up(driver)
#             dict_of_chapter_and_video_count = {}
#             dict_of_chapter_and_video_count = self.chapter_name_with_total_video_count(driver)
#             sleep(2)
#             self.for_scrolling_up(driver)
#             for ele in dict_of_chapter_and_video_count:
#                 testxpath = (By.XPATH, "//android.widget.LinearLayout/descendant::android.widget.TextView[@text='" + ele + "']/parent::android.widget.RelativeLayout/following-sibling::android.widget.HorizontalScrollView/descendant::android.widget.Button[@text='Test']")
#                 practicexpath = (By.XPATH, "//android.widget.LinearLayout/descendant::android.widget.TextView[@text='" + ele + "']/parent::android.widget.RelativeLayout/following-sibling::android.widget.HorizontalScrollView/descendant::android.widget.Button[@text='Practice']")
#                 logging.info("videos are available for this chapter " + ele)
#                 check1 = CommonMethods.isElementPresent(driver, testxpath)
#                 check2 = CommonMethods.isElementPresent(driver, practicexpath)
#                 if check1 == True and check2 == True:
#                     logging.info("Test and Practice button are present for this chapter " + ele)
#                     driver.swipe(300, 500, 300, 100)
#                     exit_count = exit_count + 1
#                 elif exit_count == self.personalised_screen.chapter_count(driver):
# #                     logging.info("Test and Practice button not present for this chapter " + ele)
#                     break
#         except NoSuchElementException:
#             CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_test_and_practice_icons')
#         except:
#             CommonMethods.exception(driver, featureFileName, 'verify_test_and_practice_icons')
#             
    def verify_test_and_practice_btns(self,driver):
        try:
            check_test = CommonMethods.getElements(driver, self.btn_test)
            check_practice = CommonMethods.getElements(driver, self.btn_practice)
            if check_test !=None and check_practice !=None:
               logging.info("Test and Practice button not present") 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_test_and_practice_btns')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_test_and_practice_btns')
             
    
    def verify_test_and_practice_for_empty_chapter(self, driver):
        try:
            self.for_scrolling_up(driver)
            dict_of_chapter_and_video_count = {}
            dict_of_chapter_and_video_count = self.chapter_names_without_video(driver)
            self.for_scrolling_up(driver)
            for ele in dict_of_chapter_and_video_count:
                testxpath = (By.XPATH, "//android.widget.LinearLayout/descendant::android.widget.TextView[@text='" + ele + "']/parent::android.widget.RelativeLayout/following-sibling::android.widget.HorizontalScrollView/descendant::android.widget.Button[@text='Test']")
                practicexpath = (By.XPATH, "//android.widget.LinearLayout/descendant::android.widget.TextView[@text='" + ele + "']/parent::android.widget.RelativeLayout/following-sibling::android.widget.HorizontalScrollView/descendant::android.widget.Button[@text='Practice']")
                logging.info("videos are not available for this chapter " + ele)
                check1 = CommonMethods.isElementPresent(driver, testxpath)
                check2 = CommonMethods.isElementPresent(driver, practicexpath)
                if check1 == True and check2 == True:
                    logging.info("Test and Practice button are present for this chapter " + ele)
                    driver.swipe(300, 500, 300, 100)
                else:
                    logging.info("Test and Practice button not present for this chapter " + ele)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyTestAndPracticeForEmptyChapter')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyTestAndPracticeForEmptyChapter')

    def verify_video_thumbnail_progression_bar(self,driver):
        try:
            video_name = CommonMethods.getElements(driver, self.video_cards)
            progression_bar = CommonMethods.getElements(driver, self.video_progression_bar)
            if video_name != None and progression_bar != None:
                logging.info("Video card with video thumbnail and Video Progression below the video thumbnail is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_thumbnail_progression_bar')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_thumbnail_progression_bar')
     

    def verify_app_back_arrow(self, driver): 
        try:
            check = CommonMethods.isElementPresent(driver, self.btn_back_arrow)
            if check == True:
                logging.info("App back arrow is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_app_back_arrow')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_app_back_arrow')
            
    def verify_personalise_btn(self, driver, text): 
        try:
            check = CommonMethods.isElementPresent(driver, self.personalised_btn)
            if check == True:
                text_of_personalise_btn=CommonMethods.getTextOfElement(driver, self.personalised_btn)
                if text_of_personalise_btn==text:
                    logging.info("personalise button is displayed with text "+ text_of_personalise_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_personalise_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_personalise_btn')
            
    def verify_chapters_heading(self, driver): 
        try:
            check = CommonMethods.isElementPresent(driver, self.txt_chapters)
            if check == True:
                logging.info("Chapters heading is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_chapters_heading')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_chapters_heading')

    def verify_library_cha_screen(self,driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.personalised_btn, 3)
            text_personalise = CommonMethods.getTextOfElement(driver, self.personalised_btn)
            check = CommonMethods.isElementPresent(driver, self.btn_library)
            check1 = CommonMethods.isElementPresent(driver, self.Btn_library_when_text_isnot_there)
            if text_personalise == 'Personalised':
                logging.info("Library chapter list screen is displayed")
            elif check == True:
                CommonMethods.elementClick(driver, self.btn_library)
                logging.info("Library chapter list screen is displayed")
            elif check1 == True:
                CommonMethods.elementClick(driver, self.Btn_library_when_text_isnot_there)
                logging.info("Library chapter list screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_library_cha_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_library_cha_screen')       
    
          