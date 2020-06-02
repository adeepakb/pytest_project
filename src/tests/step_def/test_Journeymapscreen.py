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
from POM_Pages.Journeymapscreen import JourneyMapScreen
from Utilities.interrupt import *
from POM_Pages.Journeyloadingscreen import JourneyLoadingScreen
from POM_Pages.personalizedChapterList import PersonalizedChapterList

browser = fixture = 'browser'
baseClass = BaseClass()
home = HomePage(browser)
journey_map = JourneyMapScreen(browser)
journey_loading_screen = JourneyLoadingScreen(browser)
personalise_list = PersonalizedChapterList(browser)
"""storing the feature file name"""
featureFileName = "Journey map screen"

"""configuring the Logging Files"""
baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')

# resource_name = ""


# scenario 1
@given('Launch the app')
def launch_app(browser):
#     journey.select_online_mode(browser, 'WIFI_ONLY')
#     home.navigate_to_login_page(browser, '8th Grade')
    home.navigate_to_home_screen_for_varientC(browser)
    

@given('user is in journey map screen')
def personalized_chapter(browser):
    home.select_subject_mathematics(browser)
    personalise_list.verify_personalised_chapter_list_screen(browser)

    
@when('Journey map animation is shown to the user and node arrangement is done')
# @when('Journey path animation is completed and Node card is shown to the user')
def map_animation(browser):
    journey_map.click_on_trending_journey_card(browser)
    journey_map.verify_map_animation_and_node_arrangement(browser)


@then('Verify that journey path animation should be shown with (^) from the bottom of the screen')
def verify_journey_path(browser):
    pass


@then('Verify Node card should be shown to the user')
def nodeCard(browser):
    journey_map.verify_node_card(browser)

     
# scenario 2
@given('User opens the journey for the first time')
def first_journey(browser):
    home.select_subject_mathematics(browser)
    personalise_list.verify_personalised_chapter_list_screen(browser)
    journey_loading_screen.click_on_new_journey_card(browser)
 
@given('User is in journey map screen.')
def first_journey_map(browser):
    journey_loading_screen.verify_journey_map_screen(browser)
 
 
@then('Verify <Node name> text')
def node_name(browser):
    journey_map.get_text_of_node(browser)
 
 
@then('Verify <Resource> icons')
def resource_icons(browser):
    journey_map.verify_resource_icons_in_node_card(browser)
 
 
@then('Verify "start" button')
def start_button(browser):
    journey_map.verify_start_button(browser)
 
#  scenario 3
@when('Node card is shown to the user')
def node_card_shown(browser):
    journey_map.verify_node_card(browser)
 
 
@then('Verify that "Start" button should be highlighted with subject theme color')
def start_btn_color(browser):
    pass


# scenario 4
@when('Journey path animation is completed and node card is shown to the user')
def animation_completed(browser):
    journey_map.verify_node_name(browser)
 
 
@then('Verify that first node should auto play and user should be redirected to the <ResourceScreen>( Video or Question or Rich text)')
def node_auto_play(browser):
    journey_map.match_resourceScreen_with_icons(browser)
 
# scenario 5
@when('User taps on "Start" button on Node card')
def tap_on_start_btn(browser):
    journey_map.click_on_start_button(browser)
 
 
@then('Verify that user should be redirected to <ResourceScreen>')
def redirect(browser):
    journey_map.match_resourceScreen_with_icons(browser)
 
 
# scenario 6
@given('Launch the app online')
def launch_app_online(browser):
#     journey.select_online_mode(browser, 'WIFI_ONLY')
#     home.navigate_to_login_page(browser, '8th Grade')
    home.navigate_to_home_screen(browser)
    personalise_list.verify_personalised_chapter_list_screen(browser)


@given('user has already taken the first node')
def already_taken(browser):
    journey_loading_screen.click_on_already_taken_journey_card(browser)
 
 
@when('User navigate back to first node')
def navigate_to_first_node(browser):
    browser.swipe(300, 500, 300, 300)
    
    
@then('Verify that "Start" button should be changed to "Continue" button.')
def verify_btn(browser):
    journey_map.scroll_till_first_node(browser)
    

# scenario 8
@when('user has completed the previous node')
def click_on_continue(browser):
    personalise_list.scroll_up_with_highlight_journey(browser)
    journey_loading_screen.click_on_already_taken_journey_card(browser)
    sleep(2)
    
     
@then('Verify that journey path animation should continue')
def verify_animation(browser):
    journey_map.verify_countinue_btn(browser)
    journey_map.scroll_in_journeys(browser)


@then('Verify next nodes node card should be shown to the user')
def next_node_card(browser):
    journey_map.verify_node_card(browser)
    
    
# scenario 9
@given('user has completed the previous node')
def click_continue(browser):
    personalise_list.scroll_up_with_highlight_journey(browser)
    journey_loading_screen.click_on_already_taken_journey_card(browser)
    sleep(2)
 
@then('Verify <NodeName> text')
def verify_node_name(browser):
    journey_map.get_text_of_node(browser)
 
@then('Verify <Resource> icons')
def verify_resource_icons(browser):
    journey_map.verify_resource_icons_for_optional_node(browser)
 
@then('Verify "Continue" button')
def verify_continue(browser):
    journey_map.verify_countinue_btn(browser)
 

# scenario 11
@then('Verify that current node should auto play and redirected to <ResourceScreen>')
def auto_resource_screen(browser):
    journey_map.verify_resource_screen(browser)


# scenario 12
@given('node card is shown to the user.')
def node_card1(browser):
    personalise_list.scroll_up_with_highlight_journey(browser)
    journey_loading_screen.click_on_already_taken_journey_card(browser)
    journey_map.verify_node_card(browser)
 
 
@when('user taps on "Continue" button on node card')
def tap_on_continue(browser):
    journey_map.click_on_continue_btn(browser)
 
 
@then('Verify that user should be redirected to <ResourceScreen>')
def resource_screen(browser):
    # journey.verifyResourceVideoScreen(browser)
    journey_map.verify_resource_screen(browser)
    

# scenario 13
@given('node is about to auto play')
def video_auto_play(browser):
    journey_map.click_on_trending_journey_card(browser)
    
 
@when('User interact with journey map screen by scrolling the screen')
def scroll(browser):
    journey_map.scroll_in_journeys(browser)
 
 
@then('Verify that auto playing animation should stop')
def verify_scrolled(browser):
    journey_map.verify_node_name(browser)
 
 
@then('journey node should not auto play')
def journey_node_not_play(browser):
    journey_loading_screen.verify_journey_map_screen(browser)
 
 
# scenario 14
@given('user is in Personalised chapter list screen')
def personalised_screen(browser):
    home.select_subject_mathematics(browser)
 
 
@given('user has already taken the journey')
def journey_already_taken(browser):
    journey_map.get_text_of_sticky_card(browser)
    journey_map.verify_already_taken_journey(browser)
 
 
@when('User taps on journey card')
def taps_journey_card(browser):
    journey_map.click_on_already_taken_journey(browser)
    
 
@then('Verify that journey node which user need to continue to proceed the journey should auto play')
def auto_play_journey(browser):
    journey_loading_screen.verify_chapter_name(browser)

# scenario 15
@when('User scroll the screen upwards')
def scroll_upward(browser):
    journey_loading_screen.click_on_already_taken_journey_card(browser)
    journey_map.scroll_for_locked_videos(browser)
 
 
@when('point to any node other than current node')
def point_new_node(browser):
    journey_map.verify_current_and_previous_node_txt(browser)
 
 
@then('Verify that node card should appear with <NodeName> and locked symbol')
def verify_node_with_locked_symbol(browser):
    journey_map.verify_node_name_and_locked_symbol(browser)
 
 
@then(parsers.parse('Verify "{text}" message'))
def verify_nodemsg(browser, text):
    journey_map.verify_msg_in_locked_node(browser, text)
 
 
@then('Verify "Resume" button on journey map screen')
def resume_btn(browser):
    journey_map.verify_resume_button(browser)
 
 
# # # scenario 16
# # @then('Verify that "Resume" button should be in subject theme color')
# # def verifyColor(browser):
# #     journey_map.getColorCodeOfResumeButton(browser)
# 
# 
# scenario 17
@given('user is in journey map screen and the screen is scrolled')
def journey_map_scrolled_screen(browser):
    home.select_subject_mathematics(browser)
    journey_loading_screen.click_on_already_taken_journey_card(browser)
#     sleep(2)
    journey_map.scroll_for_locked_videos(browser)
 
 
@when('User taps on "Resume" button')
def tap_on_resume_btn(browser):
    # journey.scrollForResume(browser)
    journey_map.click_on_resume_btn(browser)
 
 
@then('Verify that user should navigate back to the current node')
def navigate_back(browser):
    journey_map.verify_nevigate_back_to_the_current_node(browser)
 
 
@then('verify node should auto play and user should be in <ResourceScreen>')
def auto_play_resource_screen(browser):
    journey_map.after_any_resource(browser)
 
 
# scenario 18
@given('user has taken few questions or watched a video or gone through a rich text')
def watch_video(browser):
    home.select_subject_mathematics(browser)
    journey_loading_screen.click_on_already_taken_journey_card(browser)
    journey_map.click_on_continue_btn(browser)
 
@given('User is in Journey map screen')
def journey_map_screen(browser):
    journey_map.after_any_resource(browser)
    sleep(3)
    journey_map.scroll_for_resume(browser)
 
 
@then('Verify that user should be redirected to <ResourceScreen>')
def verify_resource(browser):
    journey_map.after_any_resource(browser)
 
 
@then('node should start from the first resource')
def first_resource(browser):
    pass
 
 
# # scenario 19
# @given('user is in journey map screen')
# def personalized_chapter_screen2(browser):
#     home.select_subject_mathematics(browser)
#     journey_map.click_on_journey_card(browser)
#     sleep(2)
# 
# 
# @given('the journey has optional node')
# def optional_node(browser):
#     journey_map.find_optional_node(browser)
# 
# 
# @when('User completes the mandatory node just before the optional node')
# def journey_befor_optional(browser):
#     journey_map.journey_after_optional_node(browser)
# 
# 
# @then('Verify that path should be drawn through optional node to next mandatory node')
# def from_optional(browser):
#     journey_map.click_on_continue_btn(browser)
#  
# # scenario 20  
# @given('User completes the mandatory node just before the optional node')
# def mandatory_node(browser):
#     pass 
# @when('Node card is shown to the user')
# def optional_node_crd(browser):
#     journey_map.verify_optional_node(browser)
#     
# @then('Verify that optional node card should have <NodeName>')
# def optional_node_name(browser):
#     journey_map.verify_optional_text(browser)
# @then('Verify <Resource> icons')
# 
# def optional_node_resource_icon(browser):
#     journey_map.verify_resource_icons_for_optional_node(browser)
# @then('Verify "Continue" and "skip" buttons')
# 
# def verify_continue_and_skip(browser):
#     journey_map.verify_continue_and_skip_btn_on_optional_node(browser)
# 
#     
# # scenario 22
# @then('verify that user should be redirected to <ResourceScreen>')
# def verify_Resource(browser):
#     journey_map.verify_resource_screen(browser)
# # scenario 23
# @when('User taps on "Skip" button')
# def tap_on_skip(browser):
#     journey_map.click_on_skip_btn(browser)
#     
# @then('Verify that same optional node frame should display if already click on skip button')
# def do_nothing(browser):
#     journey_map.verify_optional_node(browser)
#  
#  scenario 24
@when('node card is shown to the user')
def verify_node_card(browser):
    journey_map.verify_node_card(browser)
# 
# @when('journey node has video-question-rich text inside the node')
# def verify_resource_icon(browser):
#     journey_map.find_resource_icons(browser)
#     
# @then('Verify that based on what elements are present inside the node those <Resource> icons should appear on node card')
# def verify_resources_sequence(browser):
#     journey_map.match_resourceScreen_with_icons(browser)
# # scenario 25
# @given('journey node has multiple questions inside the node(For ex: There can be multiple questions inside a node but the icon only one question icon should be shown on the node card)')
# def multiple_icons(browser):
#     pass
# 
# @then('Verify that icons should appear only once on the node card')
# def verify_icons(browser):
#     journey_map.unique_resource_icons(browser)
# 
# # scenario 26
# @when('journey node has resources Video followed by question')
# def video_followedby_question(browser):
#     journey_map.unique_resource_icons(browser)
# 
# @then('Verify that icon should appear in the order these Video, question, rich text appear for the first time inside the node')
# def verify_resourc_icon(browser):
#     pass
# 
# # Scenario 35
# @given('User is in Offline')
# def offline(browser):
#     home.select_subject_mathematics(browser)
#     journey_map.click_on_journey_card(browser)
#     sleep(3)
#     journey_map.select_offline_mode(browser)
# 
# 
# @given('user is in "No internet access" screen')
# def no_internet(browser):
#     journey_map.verify_no_internet_access_screen(browser)
# 
# 
# @when('User taps on "SETTINGS" button')
# def click_on_setting(browser):
#     journey_map.click_on_settings_btn(browser)
#     
#     
# @then('Verify that tapping on "SETTINGS" button should navigate the user to <PhoneSettingsScreen>')
# def phone_setting(browser):
#     journey_map.verify_device_settings_screen(browser)
# 
# 
# # scenario 33
# @given('user is in Offline')
# def offline1(browser):
#     sleep(3)
#     journey_map.select_offline_mode(browser)
# 
#     
# @when('user has journey node card')
# def journey_card(browser):
#     journey_map.verify_node_frame_in_journey(browser)
# 
# 
# @when('user taps on "Continue" button on node card')
# def tap_On_Continue(browser):
#     journey_map.click_on_continue_btn(browser)
# 
# @then('user is in "No internet access" screen')    
# def no_internet1(browser):
#     journey_map.verify_no_internet_access_screen(browser)
# 
# # scenario 34
# @then('Verify  hero image')
# def hero_image(browser):
#     pass
# 
# @then('Verify "No Internet Access" label')
# def verify_access_label(browser):
#     journey_map.verify_no_internet_access_text(browser)
# 
# 
# @then('Verify "There is a problem in your internet connection" text')
# def verify_txt(browser):
#     pass
# 
# 
# @then('Verify "SETTINGS" and "REFRESH" button')
# def setting_a_snd_refresh(browser):
#     journey_map.verify_setting_and_refresh_btn(browser)
# 
# # Scenario 36
# @when('User taps on "REFRESH" button')
# def click_on_refresh(browser):
#     journey_map.click_on_refresh_btn(browser)
# 
# 
# @then('Verify that toast message "Please connect to network and try again later" should be shown')
# def toast_message(browser):
#     journey_map.verify_no_internet_toast_message(browser, "Please connect to network and try again later.")
# 
# 
# # scenario 37
# @given('User is back to online')
# def online(browser):
#     journey_map.select_online_mode(browser, "wifi")
#     sleep(1)
# 
# 
# @then('Verify that tapping on "REFRESH" option should redirect the user to journey <ResourceScreen>')
# def verify_any_resource(browser):
#     journey_map.click_on_refresh_btn(browser)
#     sleep(5)
#     journey_map.verify_resource(browser)

