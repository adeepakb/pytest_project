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
# from nose.config import flag
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Utilities.common_methods import CommonMethods
from POM_Pages.Journeymapscreen import JourneyMapScreen
from builtins import int
from ctypes.wintypes import INT

featureFileName = "Personalized chapter list screen"
CommonMethods = CommonMethods()


class PersonalizedChapterList():
    
    stickycard_id = (By.ID, "com.byjus.thelearningapp:id/journeyStickCard")
    Btn_library_xpath = (By.XPATH, "//android.widget.Button[@text='Library']")
    Btn_library_when_text_isnot_there = (By.XPATH, "(//android.widget.Button[@resource-id='com.byjus.thelearningapp:id/roundedNavButton'])[2]")
    Btn_personalised_xpath = (By.XPATH, "//android.widget.Button[@text='Personalised']")
    Btn_BackArrow_xpath = (By.XPATH, "(//android.widget.Button[@resource-id='com.byjus.thelearningapp:id/roundedNavButton'])[1]")
    txt_greetingText_id = (By.ID, "com.byjus.thelearningapp:id/header_greeting_text")
    trendingJourney_id = (By.ID, "com.byjus.thelearningapp:id/ivHighlight")
    subjectName_id = (By.ID, "com.byjus.thelearningapp:id/header_title_text")
    subtitleText_id = (By.ID, "com.byjus.thelearningapp:id/header_subtitle_text")
    recommendedLearning_id = (By.ID, "com.byjus.thelearningapp:id/resumeTitle")
    forwardArrowOfStickyCard_id = (By.ID, "com.byjus.thelearningapp:id/journeyResumeIcon")
    practiceInChapters_xpath = (By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[@text='Practice']")
    chapters_xpath=(By.XPATH,"//android.widget.RelativeLayout[@resource-id='com.byjus.thelearningapp:id/parent_layout']/descendant::android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/tvChapterName']")
    subTopics_xpath = (By.XPATH, "//android.widget.RelativeLayout/android.widget.TextView[@text='Rational Numbers']/following-sibling::androidx.recyclerview.widget.RecyclerView/descendant::android.widget.TextView")
    journeyNameInStickyCard = (By.ID, "com.byjus.thelearningapp:id/recentJourneyTitle")
    journeyCardIcon = (By.XPATH, "//android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/ivSubtopicIcon']")
    journeyCardName = (By.XPATH, "//android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/tvSubtopicName']")
    btn_mathematics_xpath = (By.XPATH, "//android.widget.TextView[@text='Mathematics']")
    first_row_of_chapters=(By.XPATH,"//android.widget.RelativeLayout[@resource-id='com.byjus.thelearningapp:id/parent_layout' and @index=0]")
    second_row_of_chapters=(By.XPATH,"//android.widget.RelativeLayout[@resource-id='com.byjus.thelearningapp:id/parent_layout' and @index=1]")
#     journey_name_in_loading_screen=(By.ID,"com.byjus.thelearningapp:id/journey_name")
#     journey_name_in_loading_screen=(By.ID,"com.byjus.thelearningapp:id/animation_view")
    name_of_journey_with_respect_to_chapter_name=(By.XPATH,"//android.widget.RelativeLayout[@resource-id='com.byjus.thelearningapp:id/parent_layout']/descendant::android.widget.TextView[@text='Rational Numbers']/following-sibling::androidx.recyclerview.widget.RecyclerView/descendant::android.widget.TextView")
    chapter_names=(By.XPATH,"//android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/tvChapterName']")
    practice_card=(By.XPATH,"(//android.widget.RelativeLayout/descendant::android.widget.TextView[@text='Practice'])[1]")
    test_card=(By.XPATH,"(//android.widget.RelativeLayout/descendant::android.widget.TextView[@text='Tests'])[1]")
    first_subtopic_of_first_chapter=(By.XPATH,"(//android.widget.RelativeLayout/descendant::androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']/descendant::android.widget.RelativeLayout)[1]")
    practice_screen=(By.ID,"com.byjus.thelearningapp:id/header_subtitle1_text")
    test_screen=(By.ID,"com.byjus.thelearningapp:id/header_layout")
    toast_msg=(By.ID,"com.byjus.thelearningapp:id/snackbar_text")
    
    search_btn = (By.ID,"com.byjus.thelearningapp:id/optionalNav")
    search_bar_in_search_screen = (By.ID,"com.byjus.thelearningapp:id/searchBar")
    tool_bar = (By.ID,"com.byjus.thelearningapp:id/toolbarView")
    sticky_card_minimize = (By.ID,"com.byjus.thelearningapp:id/collapsedHeader")
    sticky_card_min_text = (By.ID,"com.byjus.thelearningapp:id/collapsedHeaderTitle")
    sticky_card_min_forward_arrow = (By.ID,"com.byjus.thelearningapp:id/collapsedHeaderForwardArrow")
    subject_centre_alligned = (By.ID,"com.byjus.thelearningapp:id/title")
    
    primaryActionBtn=(By.ID,"com.byjus.thelearningapp:id/primaryAction")
    start_practice= (By.ID,"com.byjus.thelearningapp:id/tvStartPractice")
    secondaryActionBtn =(By.ID,"com.byjus.thelearningapp:id/secondaryAction")
    chapter_list = (By.ID,"com.byjus.thelearningapp:id/rvChapterList")
    resume_practice_title = (By.ID,"com.byjus.thelearningapp:id/resumeTitle")
    
    def __init__(self, browser):
        self.browser = browser
        self.journey_map=JourneyMapScreen(browser)
        
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
                
    def scroll_from_bottom_to_top(self,browser):
        try:
            display_sub = CommonMethods.isElementPresent(browser,self.subjectName_id)
            if display_sub == False:
               while display_sub == False:
                    browser.swipe(300, 100, 300,500 )
                    display_sub = CommonMethods.isElementPresent(browser, self.subjectName_id)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'scroll_from_bottom_to_top')
        except:
            CommonMethods.exception(browser, featureFileName, 'scroll_from_bottom_to_top')
              
    def verify_trending_journey_card_highlighted(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.trendingJourney_id)
            
            if check == True:
                logging.info('Trending Journey Card is highlighted')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_trending_journey_card_highlighted')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_trending_journey_card_highlighted')
            
    def click_on_library_button(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.Btn_library_xpath, 3)
            check = CommonMethods.isElementPresent(browser, self.Btn_library_xpath)
            check1 = CommonMethods.isElementPresent(browser, self.Btn_library_when_text_isnot_there)
            if check == True:
                CommonMethods.elementClick(browser, self.Btn_library_xpath)
                logging.info('Sucessfully Tapped On library button ')
            elif check1 == True:
                CommonMethods.elementClick(browser, self.Btn_library_when_text_isnot_there)
                logging.info('Sucessfully Tapped On library button ')
            else:
                pass
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_library_button')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_library_button')

    def verify_library_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.Btn_personalised_xpath) 
            if check == True:
                logging.info("library chapter list screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_library_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_library_screen')
            
    def click_on_back_arrow(self, browser):
        try:
            check = CommonMethods.elementClick(browser, self.Btn_BackArrow_xpath)
            if(check == True):
                logging.info('Successfully Tapped On back arrow button ')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_back_arrow')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_back_arrow')
        
    def verify_home_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.txt_greetingText_id)
            
            if check == True:
                logging.info("Home screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_home_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_home_screen')

    def varify_trending_journey_in_first_and_second_row(self, browser):
        try:
            first_row=CommonMethods.isElementPresent(browser,self.first_row_of_chapters)
            second_row=CommonMethods.isElementPresent(browser,self.second_row_of_chapters)
            check = CommonMethods.isElementPresent(browser, self.trendingJourney_id)
            if first_row==True and second_row and check ==True:
                logging.info("Trending journey is displaying in first or second row ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'varify_trending_journey_in_first_and_second_row')
        except:
            CommonMethods.exception(browser, featureFileName, 'varify_trending_journey_in_first_and_second_row')

    def varify_trending_journey_in_third_or_below_row(self,browser):
        try:
            check1 = CommonMethods.isElementPresent(browser, self.sticky_card_minimize)
            check2 = CommonMethods.isElementPresent(browser, self.trendingJourney_id)
            if check1 and check2 == True:
                logging.info("trending journey is highlighted in third or below row") 
            else:
                logging.info("trending journey is highlighted in first or second row")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_search_button')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_search_button') 
    
    def varify_back_arrow_button(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.Btn_BackArrow_xpath)
            
            if check == True:
                logging.info('when Trending Journey Card is highlighted in first or second row, back arrow botton is present')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'varifyBackArrowButton')
        except:
            CommonMethods.exception(browser, featureFileName, 'varifyBackArrowButton')
            
    def verify_library_button_and_text(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.Btn_library_xpath)
            text = CommonMethods.getTextOfElement(browser, self.Btn_library_xpath)
            if check == True:
                logging.info('Library button along with the text ' + text + ' at the top right side of the screen id displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifyLibraryButtonAndText')
        except:
            CommonMethods.exception(browser, featureFileName, 'verifyLibraryButtonAndText')
            
    def verify_subject_name_with_chapters_and_journeys(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.subjectName_id)
            subjectName = CommonMethods.getTextOfElement(browser, self.subjectName_id)
            chaptersAndJourneys = CommonMethods.getTextOfElement(browser, self.subtitleText_id)
            if check == True:
                logging.info(subjectName + 'is present with total no. of ' + chaptersAndJourneys)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_subject_name_with_chapters_and_journeys')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_subject_name_with_chapters_and_journeys')
            
    def verify_resume_card_with_forward_icon(self, browser):
        try:
            check1 = CommonMethods.isElementPresent(browser, self.stickycard_id)
            check2 = CommonMethods.isElementPresent(browser, self.forwardArrowOfStickyCard_id)
            if (check1 == True) and (check2 == True):
                logging.info('resume Card is displayed with forward Arrow')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_resume_card_with_forward_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_resume_card_with_forward_icon')
    
    def chapter_count(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.subtitleText_id, 3)
            chaptersCount = CommonMethods.getTextOfElement(browser, self.subtitleText_id)
#             logging.info(chaptersCount)
            list1 = CommonMethods.ConvertStringInToList(chaptersCount)
            totalchapterscount = int(list1[0])
            logging.info(totalchapterscount)
            return totalchapterscount
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'chapter_count')
        except:
            CommonMethods.exception(browser, featureFileName, 'chapter_count')
            
    def for_scrolling_up(self, browser):
        CommonMethods.elementClick(browser, self.Btn_BackArrow_xpath)
        sleep(1)
        CommonMethods.elementClick(browser, self.btn_mathematics_xpath)
        sleep(1) 
    
    def get_allchapter_names(self, browser):
        try:
            dictOfChapters = {}
            count = self.chapter_count(browser)
#             count=int((count/2)+2)
            for i in range(1, int(count)):
                listOfChapters = CommonMethods.getElements(browser, self.chapters_xpath)
                for k in listOfChapters:
                    dictOfChapters.setdefault(k.text)
                browser.swipe(300, 500, 300, 50)
                sleep(1)
            logging.info(dictOfChapters)
            return dictOfChapters
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'get_allchapter_names')
        except:
            CommonMethods.exception(browser, featureFileName, 'get_allchapter_names')

    def verify_journey_card_icon_and_name(self, browser):
        try:
            check1 = CommonMethods.isElementPresent(browser, self.journeyCardIcon)
            check2 = CommonMethods.isElementPresent(browser, self.journeyCardName)
            if (check1 == True) and (check2 == True):
                logging.info('In journey card journey Icon and Journey Name are present')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_journey_card_icon_and_name')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_journey_card_icon_and_name')

# -----------------------------

    def click_on_sticky_card(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.stickycard_id, 5)
            journey_name = CommonMethods.getTextOfElement(browser, self.journeyNameInStickyCard)
            check = CommonMethods.isElementPresent(browser, self.stickycard_id)
            if(check == True):
                CommonMethods.elementClick(browser, self.stickycard_id)
                logging.info('Successfully clicked On resume card')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_sticky_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_sticky_card')
        return journey_name

    def verify_journey_name_with_respect_to_sticky_card(self,browser):
        try:
            journey_name=self.click_on_sticky_card(browser)
            loading=CommonMethods.isElementPresent(browser,self.journey_name_in_loading_screen)
            if loading==True:
                journey_title=CommonMethods.getTextOfElement(browser,self.journey_name_in_loading_screen)
                if journey_title==journey_name:
                    logging.info("navigate to particular journey")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_journey_name_with_respect_to_sticky_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_journey_name_with_respect_to_sticky_card')
            
    def scroll_left_to_right(self,browser, chaptername):
        try:
            journey_xpath=(By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.TextView[@text='"+ chaptername +"']/following-sibling::androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']")
            test_xpath=(By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.TextView[@text='"+ chaptername +"']/following-sibling::androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']/descendant::android.widget.TextView[@text='Tests']")
            practice_xpath=(By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.TextView[@text='"+ chaptername +"']/following-sibling::androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']/descendant::android.widget.TextView[@text='Practice']")
            journey_ele=CommonMethods.getElement(browser, journey_xpath)
            checkForTest = CommonMethods.isElementPresent(browser, test_xpath)
            checkForPractice = CommonMethods.isElementPresent(browser, practice_xpath)
            check = CommonMethods.isElementPresent(browser, journey_xpath)
            if check==True:
                if checkForTest==True and checkForPractice==True:
                    logging.info("test and practice are present")
                else:
                    while checkForTest==True and checkForPractice==True:
                        chord=journey_ele.location_in_view
                        browser.swipe(chord['x'], chord['y'], chord['x']+200, chord['y'])
                        checkForTest = CommonMethods.isElementPresent(browser, test_xpath)
                        checkForPractice = CommonMethods.isElementPresent(browser, practice_xpath)
                    logging.info("test and practice are present")
                return True
        except:     
            return False
        
                
    def  verify_test_practice_and_journey_cards(self,browser):
        try:
            self.get_allchapter_names(browser)
            logging.info("journey cards, test and practice cards are present")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_test_and_practice')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_test_and_practice')
    
    def  verify_test_and_practice(self,browser):
        try:
            chapters=self.get_allchapter_names(browser)
            logging.info(len(chapters.keys()))
            self.scroll_from_bottom_to_top(browser)
            for chapter in list(chapters.keys()):
     
                logging.info(chapter)
                chapter_xpath=(By.XPATH,"//android.widget.RelativeLayout[@resource-id='com.byjus.thelearningapp:id/parent_layout']/descendant::android.widget.TextView[@text='"+ chapter +"']")
                check=CommonMethods.isElementPresent(browser, chapter_xpath)
                if check != None: 
                    practice_icon = browser.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().resourceId(\"com.byjus.thelearningapp:id/rvSubtopic\")).setAsHorizontalList().scrollIntoView("
                                    + "new UiSelector().textContains(\"Practice\"))")
                    if practice_icon !=None:
                        logging.info("practice is present")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_test_and_practice')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_test_and_practice')
            
#     def click_on_practice_card(self, browser):
#         try:
#             check = CommonMethods.isElementPresent(browser, self.practice_card)
#             if(check == False):
#                 while check==False:
#                     first_card=CommonMethods.getElement(browser, self.first_subtopic_of_first_chapter)
#                     chord=first_card.location_in_view
#                     browser.swipe(chord['x'], chord['y'], chord['x']+200, chord['y'])
#                     check = CommonMethods.isElementPresent(browser, self.practice_card)
#             CommonMethods.elementClick(browser, self.practice_card)
#             logging.info('Successfully clicked On practice card')
# 
#         except NoSuchElementException:
#             CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_practice_card')
#         except:
#             CommonMethods.exception(browser, featureFileName, 'click_on_practice_card')
    
    def click_on_practice_card(self, browser):
        try:
            browser.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().resourceId(\"com.byjus.thelearningapp:id/rvSubtopic\")).setAsHorizontalList().scrollIntoView("
            + "new UiSelector().textContains(\"Practice\"))").click()
            logging.info('Successfully clicked On practice card')
            
            if CommonMethods.isElementPresent(browser,self.start_practice):
                CommonMethods.elementClick(browser,self.start_practice)
            if CommonMethods.isElementPresent(browser, self.primaryActionBtn):
                CommonMethods.elementClick(browser,self.primaryActionBtn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_practice_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_practice_card')        
    
    def quit_inbtween(self,browser):
        try:
            CommonMethods.click_on_device_back_btn(browser)
#             CommonMethods.wait_for_locator(browser, self.secondaryActionBtn, 5)
            check = CommonMethods.isElementPresent(browser, self.secondaryActionBtn)
            if check == True:
                CommonMethods.elementClick(browser, self.secondaryActionBtn)
            else:
                CommonMethods.click_on_device_back_btn(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'quit_inbtween')
        
        except:
            CommonMethods.exception(browser,featureFileName,'quit_inbtween')
            
    def click_on_test_card(self, browser):
        try:
            browser.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().resourceId(\"com.byjus.thelearningapp:id/rvSubtopic\")).setAsHorizontalList().scrollIntoView("
            + "new UiSelector().textContains(\"Tests\"))").click()
            logging.info('Successfully clicked On test card')
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_test_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_test_card')
            
    def verify_practice_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.practice_screen)
            if check == True :
                logging.info('practice screen is displayed')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_practice_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_practice_screen')
            
    def verify_test_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.test_screen)
            if check == True :
                logging.info('test screen is displayed')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_test_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_test_screen')
            
    def journey_cards_in_each_chapters(self,browser):
        try:
            sub_topics_dict={}
#             list_of_subtopics_names=[]
            chapters=self.get_allchapter_names(browser)
#             logging.info(len(chapters.keys()))
            self.scroll_from_bottom_to_top(browser)
            for chapter in list(chapters.keys()):
                list_of_subtopics_names=[]
                chapter_xpath=(By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.TextView[@text='"+ chapter +"']/following-sibling::androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']/parent::android.widget.RelativeLayout")
                check= CommonMethods.isElementPresent( browser, chapter_xpath)
                
                if check==False:
                    while check==False:
                        browser.swipe(300, 500, 300, 200)
                        check= CommonMethods.isElementPresent( browser, chapter_xpath)

                logging.info("chapter name is : "+ chapter)
                journey_card_xpath=(By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.TextView[@text='"+ chapter +"']/following-sibling::androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']/descendant::android.widget.TextView[not (@text='Practice') and not (@text='Tests')]")
                sub_topic_list=CommonMethods.getElements(browser, journey_card_xpath)
                for subtopic in sub_topic_list:
                    sub_topic_name=subtopic.text
                    list_of_subtopics_names.append(sub_topic_name)
                sub_topics_dict[chapter]=list_of_subtopics_names
                logging.info(sub_topics_dict)
                logging.info("total subtopics are "+str(len(list_of_subtopics_names)))
#                 del list_of_subtopics_names[:len(list_of_subtopics_names)]
                sub_topics_dict.popitem()
#                 del list_of_subtopics_names[:]
#                 if check==False:
#                     while check==False:
#                         browser.swipe(300, 500, 300, 100)
#                         check= CommonMethods.isElementPresent( browser, chapter_xpath)
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'journey_cards_in_each_chapters')
        except:
            CommonMethods.exception(browser, featureFileName, 'journey_cards_in_each_chapters')
            
    def verify_journey_map_screen(self,browser):
        try:
            self.journey_map.verify_node_card(browser)
            logging.info("journey map screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_journey_map_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_journey_map_screen')
            
    def verify_toast_message(self,browser,text):
        try:
#             check=CommonMethods.isElementPresent(browser, self.toast_msg)
            message=CommonMethods.getTextOfElement(browser, self.toast_msg)
            if message==text:
                logging.info("toast message is displayed "+message)
            else:
               logging.info("failed to identify toast message") 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_toast_message')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_toast_message')
            
    def verify_personalised_chapter_list_screen(self, browser):
        try:
            per_btn = CommonMethods.isElementPresent(browser, self.Btn_personalised_xpath)
            if per_btn == True:
                CommonMethods.elementClick(browser, self.Btn_personalised_xpath)
                CommonMethods.wait_for_element_visible(browser, self.Btn_library_xpath, 3)
                logging.info("Personalised chapter list screen is displayed")
                
            else:
                logging.info("Personalised chapter list screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_personalised_chapter_list_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_personalised_chapter_list_screen')
    
    def go_up_with_respect_to_highlight_journey(self,browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.trendingJourney_id, 3)
            highlight_journey_check=CommonMethods.isElementPresent(browser,self.trendingJourney_id)
            display_sub=CommonMethods.isElementPresent(browser,self.subjectName_id)
            if highlight_journey_check and display_sub == False:
                CommonMethods.elementClick(browser, self.Btn_library_when_text_isnot_there)
                CommonMethods.wait_for_element_visible(browser, self.Btn_personalised_xpath, 3)
                CommonMethods.elementClick(browser, self.Btn_personalised_xpath)
            else:
                logging.info("highlight journey is in first 3 lines")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'go_up_with_respect_to_highlight_journey')
        except:
            CommonMethods.exception(browser, featureFileName, 'go_up_with_respect_to_highlight_journey')
    
    def verify_search_button(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.search_btn)  
            if check == True:
                logging.info("search button is displayed")     
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_search_button')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_search_button')     
            
    
    def click_on_search_button(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.search_btn)
            if check == True:
                logging.info('search button is present')
                CommonMethods.elementClick(browser, self.search_btn)
                logging.info('successfully clicked on search button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_search_button')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_search_button')       
            
    def verify_search_screen(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.search_bar_in_search_screen)
            if check == True:
                logging.info('search screen is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_search_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_search_screen')       
                    
    def verify_subject_name_centre_allign(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.subject_centre_alligned)  
            if check == True:
                logging.info("subject name is displayed and it is centre allign")     
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_subject_name_centre_allign')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_subject_name_centre_allign')     
    
    def verify_min_sticky_card_with_forward_arrow(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.sticky_card_minimize) 
            forward_arrow =CommonMethods.isElementPresent(browser, self.sticky_card_min_forward_arrow) 
            if check and forward_arrow  == True:
                logging.info("sticky card is displayed with forward arrow")   
                test_of_card = CommonMethods.getTextOfElement(browser, self.sticky_card_min_text)  
                logging.info("text on sticky card is : "+test_of_card)
            else :
                logging.info("sticky card is not displayed because trending journey is in first or second row")  
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_search_button')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_search_button')     
    
    def verify_resume_practice_card(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.resume_practice_title)  
            if check == True:
                logging.info("resume practice card is present")     
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_resume_practice_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_resume_practice_card')     
                           
    def verify_minimise_top_label(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.subjectName_id)  
            if check == True:
                while check == True:
                    browser.swipe(300, 500, 300, 50)
                    check = CommonMethods.isElementPresent(browser, self.subjectName_id) 
            else:
                check = CommonMethods.isElementPresent(browser, self.subject_centre_alligned) 
                logging.info("while scrolling upward top label is minimised")     
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_minimise_top_label')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_minimise_top_label')     
                        
              