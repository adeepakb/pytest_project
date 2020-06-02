import pytest
from pytest_bdd import scenarios, given, when, then, parsers, scenario

import os
import sys
import subprocess
import logging
from time import sleep

from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from POM_Pages.homepage import HomePage
from Utilities.BasePage import BaseClass
from POM_Pages.homescreen import HomeScreen
from POM_Pages.profileScreen import ProfileScreen
from Utilities.interrupt import *

browser = fixture = 'browser'
baseClass = BaseClass()
home = HomePage(browser)
home_screen = HomeScreen(browser)
profile = ProfileScreen(browser)

"""storing the feature file name"""
featureFileName = "Profile Screen"
"""configuring the Logging Files"""
baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')

# scenario 10
@given('Launch the app online')
def launch_app(browser):
    home.navigate_to_home_screen(browser)
#     home.handle_covid19_popup(browser)
    
    
@given('User is Logged In user with some data.')
def loged_in(browser):
    pass


@given('User taps on profile card on hamburger menu')
def hamburger_menu(browser):
    home_screen.click_on_hamburger_menu(browser)
    profile.click_on_home_drawr_forward_icon(browser)
    
    
@when('User is in profile screen')
def profile_screen(browser):
    profile.verify_profile_screen(browser)
    
    
@then('Verify that back arrow on the top left corner')
def back_arrow(browser):
    profile.verify_back_arrow(browser)
    
    
@then('Profile Image beside Profile name (Default Avatar) with Edit option')
def avtar(browser):
    profile.verify_avtar_and_edit_opn(browser)
    
    
@then('Profile Name below the profile image.')
def profile_name(browser):
    profile.verify_profile_name(browser)
    
    
@then('My badges below that profile name with badges name.')
def badges(browser):
    profile.verify_badges_and_badges_list(browser)
    
    
@then('Course Selection drop down below the profile name')
def course_selection(browser):
    profile.verify_course_selection(browser)
    
    
@then('Profile Completeness Progression in Percentage')
def profile_completeness(browser):
    profile.verify_profile_completion_and_percentage(browser)
    
    
# scenario 79
@then('verify Phone Number field with icon in Account details')
def acc_phn(browser):
    profile.verify_phn_no_and_icon(browser)
    
    
@then('An Edit icon should be shown next to this field click on edit icon')
def phn_edit(browser):
    profile.click_phn_no_edit(browser)
      
    
@then('Phone number field should accept only numeric values.')
def phn_numeric(browser):
    profile.verify_phn_no_and_text(browser)
    
# scenario 80
@then('verify Profile Name with icon and should be Pre Filled')
def profile_name_icon(browser):
    profile.scroll_down(browser)
    profile.verify_profile_name_icon(browser)
    
    
@then('verify Email with icon and should be Pre Filled')
def email_icon(browser):
    profile.verify_email_icon_and_value(browser)
      
@then('verify Location with icon and should be Pre Filled')
def loc_icon(browser):
    profile.verify_phn_no_and_text(browser)

    
@then(parsers.parse('verify gender with icon with "{text}" text'))
def gender_txt(browser,text):
    profile.verify_gender_icon_text(browser, text)
    
@then(parsers.parse('verify birthday with icon with "{birthday_text}" text'))
def bday_txt(browser,birthday_text):
    profile.verify_bday_icon_text(browser, birthday_text)
      
@then('Sign out button with icon')
def sign_out(browser):
    profile.verify_sign_out_and_image(browser)    


# scenario 3
@given('Launch app on offline')
def launch_offline(browser):
    home.navigate_to_home_screen(browser)
#     home.handle_covid19_popup(browser)
    home_screen.click_on_hamburger_menu(browser)
    profile.click_on_home_drawr_forward_icon(browser)
    profile.select_offline_mode(browser)

@given('User is in profile screen')
def profile_screen_offline(browser):
    profile.verify_profile_screen(browser)

@when('User taps on profile image')
def tap_profile(browser):
    profile.click_on_profile_image(browser)
    
# scenario 5
@given('Launch the app')
def launch_with_profile(browser):
    home.navigate_to_home_screen(browser)
#     home.handle_covid19_popup(browser)
    home_screen.click_on_hamburger_menu(browser)
    profile.click_on_home_drawr_forward_icon(browser)
    
    

@then('Verify that User should be displayed popup with list of avatars')
def avtar_popup(browser):
    profile.verify_avtar_pop_up(browser)

# scenario 6
@when('User is in Avatar popup')
def verify_avtar_popup(browser):
    profile.click_on_profile_image(browser)
    profile.verify_avtar_pop_up(browser)


@then('Verify that avatar label and list avatar should be displayed')
def list_avtar(browser):
    profile.verify_avtar_label_and_list_of_avtars(browser)

# scenario 7
@given('User is in Avatar popup')
def avtar_pop_up(browser):
    profile.click_on_profile_image(browser)
    profile.verify_avtar_pop_up(browser)
    

@when('User selects the profile image')
def profile_image(browser):
    profile.select_pro_image_from_avtars(browser)

@then('Verify that user navigate back to profile screen and profile image should be changed')
def changed_pro_image(browser):
    profile.verify_profile_image_if_selected(browser)

# scenario 8
@when('User taps on device back button')
def device_bck_btn(browser):
    click_on_back_button(browser)

@then('Verify that popup should be dismissed')
def avtar_popup_dismissed(browser):
    profile.verify_avtar_pop_up(browser)

# scenario 9
@when('User comes out of popup without selecting an avatar')
def without_selecting_pro_image(browser):
    click_on_back_button(browser)

@then('Verify that Old image should be retained in profile screen')
def old_image_retained(browser):
    profile.verify_profile_image_if_not_selected(browser)
