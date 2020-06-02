import sys
import os
import time

from io import BytesIO
from PIL import Image
import math
import numpy as np 
from skimage.measure import compare_ssim
import cv2
from timeit import timeit


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


class ProfileScreen():
    
    back_arrow = (By.ID,"com.byjus.thelearningapp:id/backNav")
    avtar_with_edit = (By.ID,"com.byjus.thelearningapp:id/edit_relyt_avatar")
    profile_name=(By.ID,"com.byjus.thelearningapp:id/tvUserName")
    my_badged_text=(By.ID,"com.byjus.thelearningapp:id/tvBadgeTitle")
    badges_list=(By.ID,"com.byjus.thelearningapp:id/rvBadgeList")
    
    profile_completion_text=(By.ID,"com.byjus.thelearningapp:id/profile_completeness_text")
    profile_completion_progress=(By.ID,"com.byjus.thelearningapp:id/progress_profile")
    profile_completion_percentage=(By.ID,"com.byjus.thelearningapp:id/profile_completeness_percent")
    account_details_title=(By.ID,"com.byjus.thelearningapp:id/account_details_title")
    acc_phone_image=(By.ID,"com.byjus.thelearningapp:id/phone_image")
    acc_mobile_number=(By.ID,"com.byjus.thelearningapp:id/mobile_number")
    acc_phn_no_edit=(By.ID,"com.byjus.thelearningapp:id/phone_number_cta")
    change_no_phn_text_box=(By.ID,"com.byjus.thelearningapp:id/etPhoneNumber")
    sign_out_image=(By.ID,"com.byjus.thelearningapp:id/signout_image")
    sign_out_text=(By.ID,"com.byjus.thelearningapp:id/signout")
    bday_image=(By.ID,"com.byjus.thelearningapp:id/birthday_image")
    add_bday_text=(By.ID,"com.byjus.thelearningapp:id/birthday")
    location_image=(By.ID,"com.byjus.thelearningapp:id/location_image")
    location_text=(By.ID,"com.byjus.thelearningapp:id/location")
    gender_image=(By.ID,"com.byjus.thelearningapp:id/gender_image")
    gender_text=(By.ID,"com.byjus.thelearningapp:id/gender")
    mail_image=(By.ID,"com.byjus.thelearningapp:id/mail_image")
    mail_text=(By.ID,"com.byjus.thelearningapp:id/mail")
    name_image=(By.ID,"com.byjus.thelearningapp:id/name_image")
    name_text=(By.ID,"com.byjus.thelearningapp:id/name")
    profile_details=(By.ID,"com.byjus.thelearningapp:id/profile_details")
    home_drawer_forward_arrow=(By.ID,"com.byjus.thelearningapp:id/home_drawer_imgvw_arrow_right")
    
    avtar_label = (By.ID,"com.byjus.thelearningapp:id/account_details_title")
    avtar_list = (By.ID,"com.byjus.thelearningapp:id/avatar_list_view")
    avtar_images =(By.XPATH,"//androidx.recyclerview.widget.RecyclerView/descendant::android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/avatar_image']")
    
    grade_selection=(By.ID,"com.byjus.thelearningapp:id/tvGrade")
    course_bottom_sht_dialog = (By.ID,"com.byjus.thelearningapp:id/design_bottom_sheet")
    change_ur_grade_label= (By.ID,"com.byjus.thelearningapp:id/account_details_title")
    all_courses_text = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView/descendant::android.widget.TextView")
    grade_change_toast_msg = (By.ID,"com.byjus.thelearningapp:id/snackbar_text")
    enrolled_courses = (By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/course_enrolled_view']")
    radio_btn = (By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.RadioButton")
    
    def __init__(self, browser):
        self.browser = browser
        
    def verify_profile_screen(self,browser):
        try:
            CommonMethods.wait_for_locator(browser, self.avtar_with_edit, 3)
            pro_screen = CommonMethods.isElementPresent(browser, self.avtar_with_edit)
            if pro_screen == True:
                logging.info('profile screen is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_profile_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_profile_screen')

    def verify_back_arrow(self,browser):
        try:
            back_arrow = CommonMethods.isElementPresent(browser, self.back_arrow)
            if back_arrow == True:
                logging.info('back arrow is displayed on top left corner')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_back_arrow')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_back_arrow')
    
    def verify_avtar_and_edit_opn(self,browser):
        try:
            avtar_edit_opn = CommonMethods.isElementPresent(browser, self.avtar_with_edit)
            if avtar_edit_opn == True:
                logging.info('profile image avtar and edit option are displayd')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_avtar_and_edit_opn')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_avtar_and_edit_opn')
    
    def verify_profile_name(self,browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.profile_name)
            if check == True:
                pro_name = CommonMethods.getTextOfElement(browser, self.profile_name)
            logging.info("profile name : "+ pro_name + " is displayed" )
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_profile_name')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_profile_name')
            
    def verify_badges_and_badges_list(self,browser):
        try:
            badges = CommonMethods.isElementPresent(browser, self.my_badged_text)
            badges_list = CommonMethods.isElementPresent(browser, self.badges_list)
            if badges and badges_list == True:
                logging.info('profile image avtar and edit option are displayd')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_avtar_and_edit_opn')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_avtar_and_edit_opn')
    
    def verify_course_selection(self,browser):
        try:
            grade_selection = CommonMethods.isElementPresent(browser, self.grade_selection)
            if grade_selection == True:
                logging.info("Course Selection drop down is displayed" )
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_course_selection')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_course_selection')
            
    def verify_profile_completion_and_percentage(self,browser):
        try:
            profile_completion_title = CommonMethods.isElementPresent(browser, self.profile_completion_text)
            profile_completion_progressio_bar = CommonMethods.isElementPresent(browser, self.profile_completion_progress)
            profile_completion_percentage = CommonMethods.isElementPresent(browser, self.profile_completion_percentage)
            if profile_completion_title and profile_completion_progressio_bar and profile_completion_percentage == True:
                percentages=CommonMethods.getTextOfElement(browser, self.profile_completion_percentage)
                logging.info("profile completion title with progression bar and percentages : "+ str(percentages) + " are displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_profile_completion_and_percentage')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_profile_completion_and_percentage')
    
    def verify_sign_out_and_image(self,browser):
        try:
            sign_out = CommonMethods.isElementPresent(browser, self.sign_out_text)
            sign_out_image = CommonMethods.isElementPresent(browser, self.sign_out_image)
            if sign_out and sign_out_image == True:
                logging.info('sign out title and image are displayd')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_sign_out_and_image')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_sign_out_and_image')
    
    def click_on_home_drawr_forward_icon(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.home_drawer_forward_arrow, 3)
            CommonMethods.elementClick(browser, self.home_drawer_forward_arrow)
            logging.info('Successfully Tapped On home drawer forward arrow')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_home_drawr_forward_icon')
            
    def verify_phn_no_and_icon(self,browser):
        try:
            phn_no = CommonMethods.isElementPresent(browser, self.acc_mobile_number)
            phnno_icon = CommonMethods.isElementPresent(browser, self.acc_phone_image)
            if phn_no and phnno_icon == True:
                logging.info('phone number and phone icon are displayd')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_phn_no_and_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_phn_no_and_icon')
    
    def click_phn_no_edit(self, browser):
        try:
            phn_edit= CommonMethods.isElementPresent(browser, self.acc_phn_no_edit)
            if phn_edit == True:
                logging.info('Phone no edit icon is displayed')
                CommonMethods.elementClick(browser, self.acc_phn_no_edit)
                logging.info('Successfully Tapped phone edit icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_phn_no_edit')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_phn_no_edit')
            
    def verify_phn_no_and_text(self,browser):
        try:
            phn_no_box = CommonMethods.isElementPresent(browser, self.change_no_phn_text_box)
            if phn_no_box == True:
                phn_no_text = CommonMethods.getTextOfElement(browser, self.change_no_phn_text_box)
                check=phn_no_text.isdigit()
                if check==True:
                    logging.info('phone number field is accepting numeric only')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_phn_no_and_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_phn_no_and_icon')
    
    def verify_profile_name_icon(self,browser):
        try:
            profile_name = CommonMethods.isElementPresent(browser, self.profile_name)
            profile_icon = CommonMethods.isElementPresent(browser, self.name_image)
            if profile_name and profile_icon == True:
                logging.info('profile name and image are displayed')
                profile_name_text = CommonMethods.getTextOfElement(browser, self.profile_name)
                logging.info("profile name pre filled value is : "+profile_name_text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_phn_no_and_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_phn_no_and_icon')
    
    def verify_email_icon_and_value(self,browser):
        try:
            email = CommonMethods.isElementPresent(browser, self.mail_text)
            email_icon = CommonMethods.isElementPresent(browser, self.mail_image)
            if email and email_icon == True:
                logging.info('mail and mail icon are displayed')
                email_value = CommonMethods.getTextOfElement(browser, self.mail_text)
                logging.info("email pre filled value is : "+ email_value)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_email_icon_and_value')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_email_icon_and_value')
            
    def verify_loc_icon_and_value(self,browser):
        try:
            loc = CommonMethods.isElementPresent(browser, self.location_text)
            loc_icon = CommonMethods.isElementPresent(browser, self.location_image)
            if loc and loc_icon == True:
                logging.info('location and location icon are displayed')
                loc_value = CommonMethods.getTextOfElement(browser, self.location_text)
                logging.info("location pre filled value is : "+ loc_value)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_loc_icon_and_value')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_loc_icon_and_value')
               
    def verify_gender_icon_text(self,browser, text):
        try:
            gender = CommonMethods.isElementPresent(browser, self.gender_text)
            gender_icon = CommonMethods.isElementPresent(browser, self.gender_image)
            if gender and gender_icon == True:
                logging.info('gender field and gender icon are displayed')
                gender_txt = CommonMethods.getTextOfElement(browser, self.gender_text)
                if text == gender_txt:
                    logging.info("text in gender field is : "+ gender_txt)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_gender_icon_text')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_gender_icon_text')
             
    def verify_bday_icon_text(self,browser, text):
        try:
            bday = CommonMethods.isElementPresent(browser, self.add_bday_text)
            bday_icon = CommonMethods.isElementPresent(browser, self.bday_image)
            if bday and bday_icon == True:
                logging.info('birthday field and birthday icon are displayed')
                birthdy_txt = CommonMethods.getTextOfElement(browser, self.add_bday_text)
                if text == birthdy_txt:
                    logging.info("text in birthday field is : "+ birthdy_txt)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_bday_icon_text')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_bday_icon_text')
             
    def scroll_down(self,browser):
        browser.swipe(300, 600, 300,100 )
        
#     def select_offline_mode(self, browser):
#         try:
#             set_connection_type(browser, 'offline')
#             logging.info("enabled offline mode")
#         except:
#             CommonMethods.exception(browser, featureFileName, 'select_offline_mode')
#         
    def click_on_profile_image(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.avtar_with_edit, 2)
            CommonMethods.elementClick(browser, self.avtar_with_edit)
            logging.info('Successfully Tapped On profile image')
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_profile_image')
    
    def verify_avtar_pop_up(self,browser):
        try:
            avtar_pop_up = CommonMethods.isElementPresent(browser, self.avtar_label)
            if avtar_pop_up  == True:
                logging.info('avtar pop up is displayed')
            elif avtar_pop_up  == False:
                logging.info('avtar pop up is not displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_avtar_pop_up')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_avtar_pop_up')
           
    def verify_avtar_label_and_list_of_avtars(self,browser):
        try:
            avtar_label = CommonMethods.isElementPresent(browser, self.avtar_label)
            avtars = CommonMethods.isElementPresent(browser, self.avtar_list)
            if avtar_label and avtars  == True:
                logging.info('avtars label is displayed')
                logging.info('list of avtars is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_avtar_label_and_list_of_avtars')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_avtar_label_and_list_of_avtars')
           
    def select_pro_image_from_avtars(self,browser):
        try:
            avtars = CommonMethods.isElementPresent(browser, self.avtar_list)
            if avtars == True:
                images = CommonMethods.getElements(browser, self.avtar_images)
                images[1].click()
                logging.info('selected 2nd image from avtars list')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'select_pro_image_from_avtars')
        except:
            CommonMethods.exception(browser, featureFileName, 'select_pro_image_from_avtars')
    
    def verify_profile_image_if_selected(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.avtar_with_edit)
            if check == True:
                logging.info('avtar image is changed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_profile_image_if_selected')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_profile_image_if_selected')
    
    def verify_profile_image_if_not_selected(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.avtar_with_edit)
            if check == True:
                logging.info('avtar image is not changed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_profile_image_if_not_selected')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_profile_image_if_not_selected')
                  