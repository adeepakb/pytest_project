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


    def __init__(self, driver):
        self.driver = driver
        self.revisit = RevisitScreen(driver)

    def for_two_concepts(self,driver):
        try:
            total_concept=self.revisit.verify_concepts_summary_details_and_count(driver)
            logging.info("total concepts are "+str(total_concept))
            return total_concept

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyVideoCorousel')

    def swipe_for_concepts(self,driver):
        pass
    def verify_chapter_name(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver,self.chapter_name)
            logging.info("chapter name is displayed in concept summary screen")
            ch_name=CommonMethods.getTextOfElement(driver,self.chapter_name)
            logging.info(ch_name)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyVideoCorousel')

    def verify_video_player(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver,self.player_frame)
            logging.info("chapter video player is displayed in concept summary screen")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyVideoCorousel')
    def scroll_concept(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver,self.practice_image)
            if check==True:
                logging.info("practice screen is displayed")
            else:
                while check==False:
                    CommonMethods.wait_for_locator(driver, self.play_pause_button, 15)
                    concept_video = CommonMethods.getElement(driver, self.play_pause_button)
                    n = concept_video.location_in_view
                    driver.swipe(n['x'], n['y'], n['x'] - 550, n['y'])
                    check = CommonMethods.isElementPresent(driver, self.practice_image)
                logging.info("practice screen is displayed")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyVideoCorousel')
    def click_on_video_card(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver,self.play_pause_button)
            if check==True:
                CommonMethods.elementClick(driver,self.play_pause_button)
                start_time = CommonMethods.getTextOfElement(driver, self.video_time)
                logging.info(start_time)
                logging.info("clicked on play button")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyVideoCorousel')
        return start_time

    def check_video_played(self,driver):
        try:
            st_time=self.click_on_video_card(driver)
            sleep(30)
            play_btn=CommonMethods.isElementPresent(driver,self.play_pause_button)
            if play_btn==False:
                while play_btn==False:
                    CommonMethods.elementClick(driver, self.video_tap)
                    end_time = CommonMethods.getTextOfElement(driver, self.video_time)
                    play_btn = CommonMethods.isElementPresent(driver, self.play_pause_button)
                    logging.info(end_time)
                if st_time!=end_time:
                    logging.info("video is played")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyVideoCorousel')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyVideoCorousel')


