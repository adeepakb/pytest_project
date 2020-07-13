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
from Constants.constants import CONFIG_PATH, Login_Credentials
from Constants.load_json import getdata
from Utilities.API_methods import *

browser = fixture = 'browser'
baseClass = BaseClass()
home = HomePage(browser)
home_screen = HomeScreen(browser)
profile = ProfileScreen(browser)

"""storing the feature file name"""
featureFileName = "Profile Screen"

# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')


# scenario 1
@given('Launch the App')
def launch_for_new_user(browser):
    home.navigate_to_home_screen(browser)
    pass


@given('User enroll course for first time')
@given('User is new user')
def new_account(browser):
    pass


@given('user taps on profile card on hamburger menu')
def tap_on_profile_card(browser):
    home_screen.verify_home_screen(browser)
    home_screen.click_on_hamburger_menu(browser)
    profile.click_on_home_drawr_forward_icon(browser)


@then(parsers.parse('Verify that message should be shown "{text}"'))
@then(parsers.parse('My badges below that profile name with text "{text}"'))
def no_badges(browser, text):
    profile.verify_no_badges_text(browser, text)


# scenario 2
@given('Launch the App online')
def launch_app(browser):
    set_connection_type(browser, 'WIFI_ONLY')
    home.navigate_to_home_screen(browser)


@given('User is Logged In user with some data.')
def loged_in(browser):
    pass


#
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


# scenario 3
@given('Launch app on offline')
def launch_offline(browser):
    code = getdata(Login_Credentials, 'login_details2', 'code')
    countrycode = getdata(Login_Credentials, 'login_details2', 'country_code')
    mobno = getdata(Login_Credentials, 'login_details2', 'mobile_no')
    otp = getdata(Login_Credentials, 'login_details2', 'OTP')
    home.navigate_to_home_screen(browser)
    home_screen.click_on_hamburger_menu(browser)
    profile.click_on_home_drawr_forward_icon(browser)
    profile.select_offline_mode(browser)


@given('User is in profile screen')
def profile_screen_offline(browser):
    profile.verify_profile_screen(browser)


@when('User taps on profile image')
def tap_profile(browser):
    profile.click_on_profile_image(browser)


# scenario 4
@when('User switch the grade')
def switch_grade(browser):
    profile.click_on_grade_selection_dropdown(browser)


@then(parsers.parse('Verify that page is loading and toast message "{text}" should be displayed.'))
def page_loading_toast(browser, text):
    profile.select_any_course(browser)
    profile.verify_empty_field_error(browser, text)
    set_connection_type(browser, 'WIFI_ONLY')


# scenario 5
@given('Launch the app')
def launch_with_profile(browser):
    set_connection_type(browser, 'WIFI_ONLY')
    home.navigate_to_home_screen(browser)
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


# scenario 10
@when('User taps on course selection drop down')
def select_course(browser):
    profile.click_on_grade_selection_dropdown(browser)


@then('Verify that user should taken to bottom sheet dialog with list of all courses')
def course_bottom_sheet(browser):
    profile.verify_course_bottom_sheet_dialog(browser)


# scenario11
@given('user is in profile screen')
def profile_select(browser):
    home_screen.click_on_hamburger_menu(browser)
    profile.click_on_home_drawr_forward_icon(browser)


@when('User is in course selection sheet')
def course_selection_sheet(browser):
    profile.verify_course_bottom_sheet_dialog(browser)


@then(
    'Verify that change your grade label and list of all  Courses like 6th grade, 7th grade, 8th grade, 9th grade, 10th grade, 11th & 12th grade, 4th grade, 5th grade, 11th Grade - Commerce, Bank PO, Campus Recruitment, CAT, IAS, GRE, GMAT with radio button option should be displayed')
def course_list(browser):
    profile.all_courses(browser)


# scenario 12
@given('User taps on course selection drop down')
def select_course1(browser):
    profile.click_on_grade_selection_dropdown(browser)


@when('User taps on any course')
def select_any_course(browser):
    #     profile.select_any_course(browser)
    pass


@then('Verify that user switches the course')
def switch_the_courese(browser):
    profile.selected_course_with_radio_btn(browser)


@then(parsers.parse('it should display a toast message "{text}"'))
def course_text_msg(browser, text):
    profile.verify_grade_change_toast_msg(browser, text)
    profile.switch_to_8th_grade(browser)


# scenario 13
@then('Verify that tick mark should be shown for enrolled user')
def enrolled_course(browser):
    profile.check_enrolled_courses(browser)


# scenario 14
@then('Verify that radio button is selected for current course')
def radio_btn_enabled(browser):
    profile.check_course_radio_btn_enabled(browser)


# @scenario 15
@when('tap on device back button')
def back_button(browser):
    click_on_back_button(browser)


@then('Verify that course selection dialog should be dismissed')
def course_dialog_dismissed(browser):
    profile.verify_course_bottom_sheet_dialog(browser)


#  scenario 16   
@then('should have "Earn Your First Badge" button')
def earn_badge_btn(browser):
    profile.verify_earn_badge_btn(browser)


# scenario 17
@given('User earned few badges')
def earned_badges(browser):
    pass


@then('Verify that all badges and see all forward arrow should be displayed')
def all_badges_see_all(browser):
    profile.verify_three_badges_and_see_all(browser)


# scenario 18
@given('User earned three badges')
def earned_three_badges(browser):
    profile.verify_only_three_badges(browser)


@then('Verify that only three badges should be displayed')
def displayed_badges(browser):
    profile.verify_only_three_badges(browser)


# scenario 19
@when('User taps on see all button under my badges')
def tap_on_badge_see_all(browser):
    profile.click_on_badge_see_all_icon(browser)


@then('Verify that user should be navigate to "Earned Badges Screen"')
def badge_screen(browser):
    profile.verify_badges_screen(browser)


# scenario 20

@then(parsers.parse('Verify that profile completion section is "{percentage}" by default'))
def default_profile_completion(browser, percentage):
    profile.verify_profile_completion_percentage(browser, percentage)


# scenario 21 
@given('Launch the app Online')
def launch_app_for_gender_updation(browser):
    home.navigate_to_home_screen(browser)
    home_screen.click_on_hamburger_menu(browser)
    profile.click_on_home_drawr_forward_icon(browser)


@when('User update gender in profile details')
def update_gender_first(browser):
    profile.update_gender(browser)


@then(parsers.parse('Verify that profile completion section updates to "{percentage}"'))
def profile_percentage_85(browser, percentage):
    profile.verify_profile_completion_percentage(browser, percentage)


# scenario 22 
@given('Launch the App Online')
def launch_app_for_bday_updation(browser):
    pass


@when('User update Date of Birth in profile details')
def update_bday_first(browser):
    profile.update_bday(browser)


#  scenario23   
@when('User updates both date of birth and gender in profile details')
def bday_gender_update(browser):
    profile.update_gender(browser)
    profile.update_bday(browser)


@then(parsers.parse('Verify that profile completion section updates to "{percentage}"'))
def bday_gender_percentage(browser, percentage):
    profile.verify_profile_completion_percentage(browser, percentage)


# scenario 27
@when('user is in profile screen')
def profile_select2(browser):
    home_screen.click_on_hamburger_menu(browser)
    profile.click_on_home_drawr_forward_icon(browser)
    profile.verify_profile_screen(browser)


@then('Verify that mobile number field should be displayed')
def verify_phone(browser):
    profile.verify_phn_no_and_icon(browser)


# scenario 28
@given('Launch the app online')
def launch_app2(browser):
    home.navigate_to_home_screen(browser)


@then('Verify that mobile number has a phone icon to the left and a <Edit> icon to the right should be displayed')
def phn_edit_icon(browser):
    profile.verify_phn_no_and_icon(browser)
    profile.verify_phn_no_edit_icon(browser)


# scenario 29  
@when('User taps on edit of mobile number field')
def tap_on_mobile_edit(browser):
    profile.click_phn_no_edit(browser)


@then(
    'Verify that Edit icon should displays a pop-up "Please enter your phone number" with options to switch country code and enter mobile number with submit button')
def feilds_in_edit_phon_popup(browser):
    profile.verify_feilds_in_edit_phn_popup(browser)
    profile.verify_submit_btn_edit_phn_popup(browser)


# scenario 30    
@when('Remove the existing mobile number')
def remove_no(browser):
    profile.click_phn_no_edit(browser)
    profile.remove_existing_mob_no(browser)


@when('User taps on submit button')
def tap_on_submit(browser):
    profile.click_submit_btn_edit_phn_popup(browser)


@then(parsers.parse('Verify that "{text}" error message should be displayed'))
def error_msg(browser, text):
    profile.verify_empty_phn_no_error_msg(browser, text)


# scenario 31
@when('User enter invalid mobile number')
def invalid_no(browser):
    profile.click_phn_no_edit(browser)
    profile.enter_invalid_mob_no(browser)
    profile.click_submit_btn_edit_phn_popup(browser)


# scenario 32
@when('User taps on device back button /anywhere outside that popup')
def tap_outside(browser):
    profile.click_phn_no_edit(browser)
    profile.touch_outside_phn_popup(browser)


@then('Verify that user redirects to profile screen')
@then('Verify that popup should be dismissed')
@then('Verify that change number popup should be displayed')
def number_pop_up_dissmissed(browser):
    profile.verify_profile_screen(browser)


# scenario 33
@when('User taps on submit button with existing mobile number')
def exixting_number(browser):
    profile.click_phn_no_edit(browser)
    profile.click_submit_btn_edit_phn_popup(browser)


@then(parsers.parse('Verify that "{text}" error message should be displayed'))
def verify_same_no_error(browser, text):
    profile.verify_same_no_error_msg(browser, text)


# scenario 34
@when('User changes the mobile number')
def change_number(browser):
    profile.click_phn_no_edit(browser)
    profile.enter_new_mob_no(browser)
    profile.click_submit_btn_edit_phn_popup(browser)


@then('Verify that user should be navigate to OTP screen')
def otp_screen(browser):
    profile.verify_otp_screen(browser)


# scenario 35
@when('User taps on cancel button on popup')
def tap_on_cancel(browser):
    profile.click_phn_no_edit(browser)
    profile.click_on_cancel_btn_in_phn_popup(browser)


# scenario 36
@then('<Gender>')
def verify_gender(browser):
    profile.verify_gender_icon(browser)


@then('<Birthday>')
def verify_birthday(browser):
    profile.verify_bday_icon(browser)


# scenario 37
@then(parsers.parse('Verify that gender should be displayed like "{text}"'))
def gender_txt2(browser, text):
    profile.scroll_down(browser)
    profile.verify_gender_icon_text(browser, text)


# scenario38
@when('User taps on edit button of gender in edit profile screen')
def edit_gender(browser):
    profile.click_profile_edit_icon(browser)
    profile.click_on_gender_field(browser)


@then('Verify that user redirects to edit gender profile screen.')
def edit_gender_screen(browser):
    profile.verify_gender_drop_down(browser)


# scenario 39
@when('User taps on edit button of birthday in edit profile screen')
def edit_bday(browser):
    profile.click_profile_edit_icon(browser)
    profile.click_on_birthday_field(browser)


@then('Verify that user redirects to edit birthday profile screen.')
def edit_bday_screen(browser):
    profile.verify_calender_popup(browser)


# scenario 40
@when('User taps on edit button of profile details')
def tap_edit_profile(browser):
    profile.click_profile_edit_icon(browser)


@then('Verify that user redirects to edit profile screen.')
def edit_profile_screen1(browser):
    profile.verify_edit_profile_screen(browser)


# scenario 41
@given('User is in edit profile screen')
def edit_profile(browser):
    home_screen.click_on_hamburger_menu(browser)
    profile.click_on_home_drawr_forward_icon(browser)
    #     profile.select_offline_mode(browser)
    profile.click_profile_edit_icon(browser)
    profile.verify_edit_profile_screen(browser)


@when('User taps on back arrow')
def back_arrow1(browser):
    profile.click_back_arrow(browser)


# scenario 42  
@when('User is in edit profile screen')
def edit_screen2(browser):
    home_screen.click_on_hamburger_menu(browser)
    profile.click_on_home_drawr_forward_icon(browser)
    profile.click_profile_edit_icon(browser)
    profile.verify_edit_profile_screen(browser)


@then(parsers.parse('A text "{text}" below the app back arrow'))
def edit_profile_text(browser, text):
    profile.verify_edit_profile_text(browser, text)


@then('Name field with icon')
def name_icon(browser):
    profile.verify_edit_name_field_and_icon(browser)


@then('Email field with icon')
def email_icon2(browser):
    profile.verify_email_icon_and_value(browser)


@then('Gender field with icon')
def gender_and_icon(browser):
    profile.verify_gender_icon(browser)
    profile.verify_gender_edit_field(browser)


@then('Location field with icon')
def location_and_icon(browser):
    profile.verify_location_field_and_icon(browser)


@then('Birthday field with icon')
def bday_and_icon(browser):
    profile.verify_bday_icon(browser)
    profile.verify_birthday_edit_field(browser)


@then('"Save" button bottom of the page')
def save_btn(browser):
    profile.verify_save_button(browser)


# scenario 43
@when('User taps on name field')
def tap_on_name(browser):
    profile.click_on_name_field(browser)


@then('Verify that location field should be editable')
@then('Verify that email field should be editable')
@then('Verify that name field should be editable')
def editable(browser):
    profile.check_field_editable(browser)


# scenario 44
@when('User taps on email field')
def tap_on_email(browser):
    profile.click_on_email_field(browser)


# scenario 45
@when('User taps on gender field')
def tap_on_gender(browser):
    profile.click_on_gender_field(browser)


@then('Verify that gender drop down displayed and any one should be selectable')
def gender_selection(browser):
    profile.verify_gender_drop_down(browser)


# scenario 46
@when('User taps on location field')
def tap_on_location(browser):
    profile.click_on_location_field(browser)


# scenario 47
@when('User taps on auto detect')
def tap_on_location_auto_detect(browser):
    profile.tap_on_location_icon1(browser)


@then('Verify that it should detect current location')
def verify_current_location(browser):
    profile.handle_gps_location_popup(browser)
    profile.get_location(browser)


@when('User selects future date')
def future_date(browser):
    profile.enter_future_date_in_bday_field(browser, "2021")


@then('Verify that future date resets to current year and should allow only valid dates')
def future_date_reset(browser):
    profile.get_bday_date(browser)


# scenario 50
@when('User taps on set button in calendar popup')
def tap_on_calender_set_btn(browser):
    pass


@then('Verify that calendar popup should update the date')
def updated_date(browser):
    profile.verify_updated_bday_date_in_calender(browser)


# scenario 51
@when('User taps on cancel button in calendar popup')
def cancel_calender_popup(browser):
    profile.verify_calender_popup(browser)
    profile.click_on_cancel_btn_in_phn_popup(browser)


@then('Verify that calendar popup should be dismissed')
def calender_popup_dismissed(browser):
    profile.verify_edit_profile_screen(browser)


# scenario 52
@when('User delete the name')
def delete_name(browser):
    profile.clear_name_field(browser)
    profile.hide_keyboard(browser)


@when('taps on save button')
def tap_on_save(browser):
    profile.click_save_button(browser)


@then(parsers.parse('Verify that error message "{text}" should be displayed.'))
@then(parsers.parse('Verify that error message "{text}" should be displayed.'))
@then(parsers.parse('Verify that error message "{text}" should be displayed'))
def name_error(browser, text):
    profile.verify_empty_field_error(browser, text)


#  scenario 53    
@when('User delete the email address')
def delete_email(browser):
    profile.clear_email_field(browser)
    profile.hide_keyboard(browser)


# scenario 54
@when('User deletes the location data')
def delete_location(browser):
    profile.clear_location_field(browser)
    profile.hide_keyboard(browser)


# scenario 55
@when('User enter all profile details')
def enter_all_data(browser):
    profile.verify_all_edit_profile_fields(browser)


@then('Verify that user should be redirects to profile screen with toast message <profile have been updated>')
def verify_profile_toast(browser):
    profile.verify_profile_updation_toast(browser)


# scenario 57
@when('User taps on sign out button')
def tap_on_sign_out(browser):
    profile.scroll_down(browser)
    profile.click_on_sign_out(browser)


@then('Verify that bottom sheet dialog displayed')
def sign_out_bottom_dialog(browser):
    profile.verify_sign_out_bottom_sheet(browser)


# scenario 58
@when('User is in sign out bottom sheet dialog')
def redirect_to_sign_out_dialog(browser):
    profile.scroll_down(browser)
    profile.click_on_sign_out(browser)
    profile.verify_sign_out_bottom_sheet(browser)


@then('Verify that Label <Sign out> should be displayed')
def sign_out_label(browser):
    profile.verify_sign_out_text_in_dialog(browser)


@then(parsers.parse('Text "{text}" message'))
def sign_out_bottom_sheet_msg(browser, text):
    profile.verify_sign_out_dialog_msg(browser, text)


@then('CTA <Yes> and <Cancel>')
def yes_and_cancel(browser):
    profile.verify_sign_out_dialog_yes_and_cancel_btn(browser)


# scenario 59   
@when('User taps on yes button in sign out dialog sheet')
@when('User taps on yes button')
def tap_on_yes(browser):
    profile.click_on_sign_out_dialog_yes_btn(browser)


@then('Verify that user redirects to login screen')
def login_screen(browser):
    profile.verify_login_page(browser)


# scenario 60
@when('User taps on cancel button')
def tap_on_cancel2(browser):
    profile.click_on_sign_out_dialog_cancel_btn(browser)


@then('Verify that bottom sheet dialog should be dismissed')
def verify_sign_out_popup_dismissed(browser):
    profile.verify_sign_out_bottom_sheet(browser)


# scenario 61  
@when('User is on offline')
def user_offline(browser):
    profile.select_offline_mode(browser)


@then(parsers.parse('Verify that toast message "{text}" should be displayed.'))
def offline_toast_msg(browser, text):
    profile.verify_sign_out_no_internet(browser, text)
    sleep(2)
    set_connection_type(browser, 'WIFI_ONLY')


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
@given('User taps on profile card on hamburger menu')
def hamburger_menu(browser):
    profile.navigate_to_profile_card(browser)


@then('Verify that Profile Details has all fields <Name>')
@then('verify Profile Name with icon and should be Pre Filled')
def profile_name_icon(browser):
    profile.scroll_down(browser)
    profile.verify_profile_name_icon(browser)


@then('<Email>')
@then('verify Email with icon and should be Pre Filled')
def email_icon(browser):
    profile.verify_email_icon_and_value(browser)


@then('<Location>')
@then('verify Location with icon and should be Pre Filled')
def loc_icon(browser):
    profile.verify_phn_no_and_text(browser)


@then(parsers.parse('verify gender with icon with "{text}" text'))
def gender_txt(browser, text):
    profile.verify_gender_icon_text(browser, text)


@then(parsers.parse('Verify that date of birth should be displayed like "{birthday_text}"'))
@then(parsers.parse('verify birthday with icon with "{birthday_text}" text'))
def bday_txt(browser, birthday_text):
    profile.verify_bday_icon_text(browser, birthday_text)


@then('<SignOut>')
@then('Sign out button with icon')
def sign_out(browser):
    profile.verify_sign_out_and_image(browser)
