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
from POM_Pages.Journeyloadingscreen import JourneyLoadingScreen

browser = fixture = 'browser'
baseClass = BaseClass()
home = HomePage(browser)
hm_screen = HomeScreen(browser)
journey_loading=JourneyLoadingScreen(browser)
"""storing the feature file name"""
featureFileName = "Home Screen"
"""configuring the Logging Files"""
baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')

# scenario 10
@given('Launch the app online')
def launch_app(browser):
#     home.navigate_to_login_page(browser, '8th Grade')
    home.navigate_to_home_screen(browser)


@when('User is in home screen')
def hm_scn(browser):
    hm_screen.verify_home_screen(browser)


@then('Verify greeting message <Good Morning,Good Afternoon,Good Evening> text should be shown based on user timings.')
def grt_txt(browser):
    hm_screen.verify_greeting_msg(browser)


# scenario 7
@given('Fields are enabled on backend')
def fields_enabled(browser):
    pass

    
@when('User taps on Hamburger menu')
def hamburger_menu(browser):
    hm_screen.click_on_hamburger_menu(browser)

@then('Verify that tapping on Hamburger menu in Home Screen, Hamburger menu/Side Navigation drawer should be opened')
def taping_hamburger(browser):
    hm_screen.verify_home_drawer(browser)
    hm_screen.check_live_classes_option(browser)

@then('Name of the user with Profile Image should present')
def name_and_image(browser):
    hm_screen.verify_user_name_profile_image(browser)

@then('Enrolled Grade should present')
def grade(browser):
    hm_screen.verify_grade_in_home_drawer(browser)

@then('Forward Arrow button should present')
def forwrd_arrow(browser):
    hm_screen.verify_forward_arrow_in_home_drawer(browser)

@then(parsers.parse('"{bookmark_text}" with icon should present'))
def bookmark_and_separate_line(browser,bookmark_text):
    hm_screen.verify_icons_image_and_separate_line(browser, bookmark_text)

@then(parsers.parse('"{notifications_text}" with icon should present'))
def notifications_and_separate_line(browser,notifications_text):
    hm_screen.verify_icons_image_and_separate_line(browser, notifications_text)

@then(parsers.parse('"{badges_text}" with icon should present'))
def badges_and_separate_line(browser,badges_text):
    hm_screen.verify_icons_image_and_separate_line(browser, badges_text)

@then(parsers.parse('"{parent_text}" with icon should present'))
def parent_connect_and_separate_line(browser,parent_text):
    hm_screen.verify_icons_image_and_separate_line(browser, parent_text)

@then(parsers.parse('"{quizzo_text}" with icon should present'))
def quizzo_and_separate_line(browser,quizzo_text):
    hm_screen.verify_icons_image_and_separate_line(browser, quizzo_text)

@then(parsers.parse('"{share_app_text}" with icon should present'))
def share_app_and_separate_line(browser,share_app_text):
    hm_screen.verify_icons_image_and_separate_line(browser, share_app_text)

@then(parsers.parse('"{contact_us_text}" with icon should present'))
def contact_us_and_separate_line(browser,contact_us_text):
    hm_screen.verify_icons_image_and_separate_line(browser, contact_us_text)

@then(parsers.parse('"{redeem_voucher_text}" with icon should present'))
def redeem_voucher_and_separate_line(browser,redeem_voucher_text):
    hm_screen.verify_icons_image_and_separate_line(browser, redeem_voucher_text)

@then(parsers.parse('"{school_super_league_text}" with icon should present'))
def school_super_league_and_separate_line(browser,school_super_league_text):
    hm_screen.verify_icons_image_and_separate_line(browser, school_super_league_text)

@then(parsers.parse('"{subscribe_now_text}" with icon should present'))
def subscribe_now_and_separate_line(browser,subscribe_now_text):
    hm_screen.verify_icons_image_and_separate_line(browser, subscribe_now_text)

@then(parsers.parse('"{terms_conditions_text}" with icon should present'))
def terms_conditions_and_separate_line(browser,terms_conditions_text):
    hm_screen.verify_icons_image_and_separate_line(browser, terms_conditions_text)

@then(parsers.parse('"{colgate_scholarship_text}" with icon should present'))
def colgate_scholarship_and_separate_line(browser,colgate_scholarship_text):
    hm_screen.verify_icons_image_and_separate_line(browser, colgate_scholarship_text)

@then('Request a Home Demo purple color button with icon should be present at the bottom of the screen')
def request_home_demo_and_separate_line(browser):
    hm_screen.verify_request_home_demo_btn(browser)

@then('Ensure that all the above mentioned options should be separated by a thin line')
def separate_thin_line(browser):
    pass


# scenario 11
@given('User is in home screen')
def hme_scrn(browser):
    hm_screen.verify_home_screen(browser)


@when('User taps on badges icon')  
def tap_badge(browser):
    hm_screen.click_on_badges_level_icon(browser)


@then('Verify that user should be taken to <BadgesScreen>')
def badge_screen(browser):
    hm_screen.verify_badges_screen(browser)  
    hm_screen.click_on_back_arrow(browser)


# scenario 12
@when('User taps on analytics icon')
def tap_analytic(browser):
    hm_screen.click_on_analytics_icon(browser)


@then('Verify that user should be taken to <AnalyticsScreen>')
def analytics_screen(browser):
    hm_screen.verify_analytics_screen(browser)
    hm_screen.click_on_back_arrow(browser)


# scenario 14
@then('Verify that grade consists of odd number of subjects then odd subjects should be left aligned')
def grade_subjects(browser):
    hm_screen.odd_sub_left_alligned(browser)
    
# scenario 15
@when('User taps on any subject card')
def tap_subject(browser):
    hm_screen.click_on_subject_maths(browser)


@then('Verify that user should be navigates to respective subject <ChapterlistScreen> in personalized mode')
def chapter_list(browser):
    hm_screen.verify_chapter_list_screen(browser)


# scenario 16  
@then(parsers.parse('Verify Recently learned card should be displaced with Header "{text}" text'))
def recently_learn_txt(browser,text):
    hm_screen.create_recently_learned_card(browser)
    hm_screen.verify_recently_learned_card(browser)
    hm_screen.verify_recently_learned_text(text, browser)


@then('verify hero image')
def hero_img(browser):
    hm_screen.verify_image_of_recently_learned_card(browser)


@then(parsers.parse('verify "{txt}" text'))
def recently_learn_card_text(browser,txt):
    hm_screen.verify_recently_learned_card_text(txt, browser)


@then('verify "Forward" button')
def recently_lear_forward(browser):
    hm_screen.verify_forward_icon_in_recently_learned(browser)

    
# scenario 17
@when('User taps on recently learned card')
def tap_recently_learn(browser):
    hm_screen.verify_recently_learned_card(browser)
    hm_screen.click_on_recently_learned_card(browser)


@then('Verify that user should be taken to <RecentlyLearnedScreen>')
def recently_learn_screen(browser):
    hm_screen.verify_recently_learned_screen(browser)
    hm_screen.click_on_back_arrow(browser)


# scenario 18
@then('Verify that user should be able to see 7 cards on top picks section with the revision card at the top of the top picks section')
def seven_cards(browser):
    hm_screen.verify_recomandation_bar(browser)
    hm_screen.verify_seven_cards_of_top_pics(browser)
    
    
# scenario 19
@given('Device is white listed for Variant A and B experiment')
def white_listed_A_B(browser):
    home.navigate_to_home_screen(browser)


@given('launch the app online')
def launch_app_c(browser):
    hm_screen.verify_recomandation_bar(browser)
    
@then('Verify that all 7 cards under top picks should be journey cards')
def top_pics_A_B(browser):
    hm_screen.verify_seven_cards_of_top_pics(browser)

   
# scenario 20
@given('Device is white listed for variant c experiment')
def white_listed_c(browser):
    home.navigate_to_home_screen_for_varientC(browser)
    home.handle_covid19_popup_secondary_ok_opn(browser)
    

@then('Verify that user should be able to see 3 journey, 1 practice,1 test, 1 quizzo, 1 discovery video')
def top_pics_c(browser):
    hm_screen.verify_seven_cards_of_top_pics_varient_c(browser)


# scenario 21
@when('User taps on any top picks card')
def tap_on_top_picks(browser):
    hm_screen.verify_recomandation_bar(browser)
    hm_screen.click_on_first_top_picks_card(browser)


@then('Verify that user should be taken to <RespectiveScreen>')
def journey_top_picks(browser):
    journey_loading.verify_chapter_name(browser)
#     hm_screen.verify_clicked_topick_chapter_name(browser)


# scenario 22
@given('user is in journey map screen')
def journey_map(browser):
    hm_screen.verify_recomandation_bar(browser)
    hm_screen.click_on_first_top_picks_card(browser)


@when('User taps on back button')
def click_on_back(browser):
    journey_loading.verify_journey_map_screen(browser)
    journey_loading.click_on_device_back_Btn(browser)
    journey_loading.handle_exit_journey_pop_up(browser)
    

@then('Verify that user should be navigate back to <HomeScreen>')
def  back_to_home(browser):
    hm_screen.verify_home_screen(browser)
    

# scenario 23   
@given('Quizzo is enabled on back end')
def enable_quizzo(browser):
    pass


@then(parsers.parse('Verify that Quizzo card in the Home screen should A header "{text}"'))
def header_quizzo(browser,text):
    hm_screen.verify_quizzo_card(browser)
    hm_screen.verify_quizzo_text(browser, text)


@then('A hero image')
def quizzo_hero_image(browser):
    hm_screen.verify_quizzo_hero_image(browser)


@then(parsers.parse('A text "{text}"'))
def quizzo_challenge_text(browser,text):
    hm_screen.verify_quizzo_play_text(browser, text)


@then('Forward button next to the text')
def quizzo_forward_icon(browser):
    hm_screen.verify_quizzo_forward_icon(browser)

# scenario 24  
@when('User taps on quizzo card')
def tap_on_quizzo(browser):
    hm_screen.verify_quizzo_card(browser)
    hm_screen.click_on_quizzo_card(browser)


@then('Verify that user should be navigate to <QuizzoScreen>')
def quizzo_screen(browser):
    hm_screen.verify_quizzo_screen(browser)


# scenario 25
@given('Set the Byjus corner content in the back end')
def check_byjus_backend(browser):
    pass


@then(parsers.parse('Verify that in byjus corner card A header text "{text}" should be shown'))
def byjus_corner_text(browser,text):
    hm_screen.verify_byjus_corner_card(browser)
    hm_screen.verify_byjus_corner_text(browser, text)


@then('Text icon with Title of the Article in the bottom of the card')
def byjus_card_bottom(browser):
    hm_screen.verify_byjus_corner_card_bottom_text(browser)


@then('See All text with Forward button at the end')
def see_all(browser):
    hm_screen.verify_byjus_corner_seeall_forward_icon(browser)


# scenario 26
@when('User taps on any article')
def tap_on_artcle(browser):
    hm_screen.verify_byjus_corner_card(browser)
    hm_screen.click_an_article_byjus_corner(browser)


@then('Verify that User should open up in new screen with Title, Description and OtherContent items from the channel the article is from.')
def verify_article(browser):
    hm_screen.verify_byjus_corner_article_title(browser)
    hm_screen.verify_byjus_corner_article_description(browser)
    hm_screen.verify_byjus_corner_article_other_content(browser)


# scenario 27
@when('User taps on Byjus corner video')
def tap_on_byjus_corner_video(browser):
    hm_screen.verify_byjus_corner_card(browser)


@then('Verify that User should open up in new screen with <Title>, <Description> and <OtherContent> items from the channel the Video is from.')
def verify_video_article(browser):
    hm_screen.verify_byjus_corner_video_icon(browser)


# scenario 28
@when('User taps on see all button')
def tap_on_see_all(browser):
    hm_screen.verify_byjus_corner_card(browser) 
    hm_screen.verify_byjus_corner_seeall_forward_icon(browser)
    hm_screen.click_on_see_all_icon(browser)


@then('Verify that user navigates should be to <ByjuCornerScreen>')
def verify_byjus_corner_scrn(browser):
    hm_screen.verify_byjus_corner_screen(browser)


# scenario 29
@then(parsers.parse('Verify Share the App card in home screen should have a header "{text}"'))
def share_the_app(browser,text):
    hm_screen.verify_share_the_app_card(browser)
    hm_screen.verify_share_the_app_txt(browser, text)


@then('verify hero image')
def share_app_hero_image(browser):
    hm_screen.verify_share_the_app_hero_image(browser)


@then(parsers.parse('verify "{text}" text'))
def share_app_sutitle(browser,text):
    hm_screen.verify_share_the_app_subtitle_txt(browser, text)


@then('verify "Forward" button next to the text')
def share_the_app_forward(browser):
    hm_screen.verify_share_the_app_forward_icon(browser)
 
# scenario 30
@when('User share the invite link through the installed apps')
def invite_link(browser):
    hm_screen.verify_share_the_app_card(browser)
    hm_screen.click_on_share_the_app_card(browser)
    hm_screen.click_on_gmail_app_icon(browser)
    hm_screen.verify_compose_mail_send_button(browser)
    journey_loading.click_on_device_back_Btn(browser)
    journey_loading.click_on_device_back_Btn(browser)


@then('Verify that share with friends card remains in home screen')
def card_remains(browser):
    hm_screen.verify_share_the_app_card(browser)
    
# scenario 31
@when('User taps on share with friends card')
def tap_on_share(browser):
    hm_screen.verify_share_the_app_card(browser)
    hm_screen.click_on_share_the_app_card(browser)


@then('Verify that user should be shown all the app installed on phone to share the app')
def share_pop_up(browser):
    hm_screen.verify_share_the_app_pop_up(browser)


# scenario 32
@when('user taps on any installed app in phone')
def tap_on_installed_app(browser):
    hm_screen.click_on_gmail_app_icon(browser)


@then('Verify that user should be able to share the link to install the app')
def send_link(browser):
    hm_screen.verify_compose_mail_send_button(browser)
    journey_loading.click_on_device_back_Btn(browser)
    journey_loading.click_on_device_back_Btn(browser)


# scenario 33
@when('User taps on back button')
def tap_on_back(browser):
    journey_loading.click_on_device_back_Btn(browser)


@then('Verify that app should be quit')
def app_quit(browser):
    hm_screen.verify_app_quit(browser)


# scenario 36   
@given('user login to app')
def login(browser):
    pass


@when('user should have some data in app')
def some_data(browser):
    hm_screen.create_recently_learned_card(browser)
#     hm_screen.verify_recently_learned_card(browser)


@then('Verify Search icon should be present at top right of the screen')
def search_ion(browser):
    pass


@then('verify A greeting text "Good Morning/Good Afternoon/Good Evening " text  with user first name below it')
def grtng_txt(browser):
    hm_screen.verify_greeting_msg(browser)
    hm_screen.verify_user_name(browser)


@then('Hero image next to greeting text')
def grtng_txt_hero_img(browser):
    pass


@then('Badge icon with <Level No> and <Name> defined and <Analysis Icon> next to it, should be shown below the user name.')
def badge(browser):
    hm_screen.verify_badge_icon_level_name(browser)
    hm_screen.verify_analytics_icon(browser)


@then('Subject tiles should be present with icons which should be in grid view and for each subject card should be designed with the subject theme colour')
def subjects(browser):
    hm_screen.verify_subject_grid_view(browser)


@then('Recommended Learning Card along with recommended carousel')
def recommended_card_carousal(browser): 
    pass


@then('Recently Learned card should be shown below the Recommended carousel')
def recently_learned_card_carousal(browser):
    hm_screen.verify_recently_learned_card(browser)


@then('Resume (floating)card should be present below the Recommended carousel card when user starts a video/journey but not completed') 
def resume_card(browser):
    hm_screen.verify_resume_journey_card(browser)


@then('Bottom navigation bar should be shown with Home, Quizzo, More options')
def bottom_navigation(browser):
    hm_screen.verify_quizzo_card(browser)


@then('Share the app card to be present below the Recently Learned card')  
def share_the_app_card(browser):
    hm_screen.verify_share_the_app_card(browser)


@then('Default Home option should be highlighted')
def default_home(browser):
    pass


# scenario 38
@when('User taps on quizzo option under bottom navigation bar')
def quizzo_opn(browser):
    hm_screen.verify_quizzo_card(browser)
    hm_screen.click_on_quizzo_card(browser)
    
# scenario 40
@given('Launch the app')
def launch_app_for_google(browser):
    home.navigate_to_home_screen_for_varientC(browser)

@when('Tap on the goggles icon')
def tap_goggles(browser):
    hm_screen.click_on_goggles_icon(browser)

@then('Verify user should redirect to camera screen')
def camera_screen(browser):
    hm_screen.verify_camera_permission_popup(browser)
#     hm_screen.verify_camera_screen(browser)