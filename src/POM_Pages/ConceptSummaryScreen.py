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

featureFileName = "Concept Summary Screen"
CommonMethods = CommonMethods()

class ConceptSummaryScreen():

    player_frame=(By.ID,"com.byjus.thelearningapp:id/playerLayout")
    practice_frame=(By.ID,"com.byjus.thelearningapp:id/introView")
    chapter_name=(By.ID,"com.byjus.thelearningapp:id/pageTitle")
    play_pause_button=(By.ID,"com.byjus.thelearningapp:id/ivPlay")
    practice_decription = (By.ID, "com.byjus.thelearningapp:id/practiceDescription")
    highlighted_Journey_card = (By.ID, "com.byjus.thelearningapp:id/ivHighlight")
    practice_image = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp:id/introView']/descendant::android.widget.ImageView[@index=0]")
    # video_rew=(By.ID,"com.byjus.thelearningapp:id/exo_rew")
    # video_few=(By.ID,"	com.byjus.thelearningapp:id/exo_ffwd")
    # video_time=(By.ID,"com.byjus.thelearningapp:id/exo_position")
    # video_tap=(By.XPATH,"//android.view.View[@resource-id='com.byjus.thelearningapp:id/exo_subtitles' and @index=1]")


    def __init__(self, browser):
        self.browser = browser
        self.revisit = RevisitScreen(browser)

    def for_two_concepts(self,browser):
        try:
            total_concept=self.revisit.verify_concepts_summary_details_and_count(browser)
            logging.info("total concepts are "+str(total_concept))
            return total_concept

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(browser, featureFileName, 'verifyVideoCorousel')

    def swipe_for_concepts(self,browser):
        pass
    def verify_chapter_name(self,browser):
        try:
            check=CommonMethods.isElementPresent(browser,self.chapter_name)
            logging.info("chapter name is displayed in concept summary screen")
            ch_name=CommonMethods.getTextOfElement(browser,self.chapter_name)
            logging.info(ch_name)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(browser, featureFileName, 'verifyVideoCorousel')

    def verify_video_player(self,browser):
        try:
            check=CommonMethods.isElementPresent(browser,self.player_frame)
            logging.info("chapter video player is displayed in concept summary screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(browser, featureFileName, 'verifyVideoCorousel')
    def scroll_concept(self,browser):
        try:
            check=CommonMethods.isElementPresent(browser,self.practice_image)
            if check==True:
                logging.info("practice screen is displayed")
            else:
                while check==False:
                    CommonMethods.wait_for_locator(browser, self.play_pause_button, 15)
                    concept_video = CommonMethods.getElement(browser, self.play_pause_button)
                    n = concept_video.location_in_view
                    browser.swipe(n['x'], n['y'], n['x'] - 550, n['y'])
                    check = CommonMethods.isElementPresent(browser, self.practice_image)
                logging.info("practice screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(browser, featureFileName, 'verifyVideoCorousel')
    def click_on_video_card(self,browser):
        try:
            check=CommonMethods.isElementPresent(browser,self.play_pause_button)
            if check==True:
                CommonMethods.elementClick(browser,self.play_pause_button)
                start_time = CommonMethods.getTextOfElement(browser, self.video_time)
                logging.info(start_time)
                logging.info("clicked on play button")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(browser, featureFileName, 'verifyVideoCorousel')
        return start_time

    def check_video_played(self,browser):
        try:
            st_time=self.click_on_video_card(browser)
            sleep(30)
            play_btn=CommonMethods.isElementPresent(browser,self.play_pause_button)
            if play_btn==False:
                while play_btn==False:
                    CommonMethods.elementClick(browser, self.video_tap)
                    end_time = CommonMethods.getTextOfElement(browser, self.video_time)
                    play_btn = CommonMethods.isElementPresent(browser, self.play_pause_button)
                    logging.info(end_time)
                if st_time!=end_time:
                    logging.info("video is played")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(browser, featureFileName, 'verifyVideoCorousel')


