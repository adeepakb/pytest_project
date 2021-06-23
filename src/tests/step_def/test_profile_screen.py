from pytest_bdd import scenarios, given, when, then, parsers

from time import sleep

from pages.android.homepage import HomePage
from utilities.BasePage import BaseClass
from pages.android.homescreen import HomeScreen
from pages.android.profileScreen import ProfileScreen
from utilities.interrupt import *
from utilities.API_methods import *

driver = fixture = 'driver'
baseClass = BaseClass()
home = HomePage(driver)
home_screen = HomeScreen(driver)
profile = ProfileScreen(driver)

"""storing the feature file name"""
featureFileName = "Profile Screen"

# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')


# scenario 1
@given('Launch the App')
def launch_for_new_user(driver):
    home.navigate_to_home_screen(driver)
    pass


@given('User enroll course for first time')
@given('User is new user')
def new_account(driver):
    pass


@given('user taps on profile card on hamburger menu')
def tap_on_profile_card(driver):
    home_screen.verify_home_screen(driver)
    home_screen.click_on_hamburger_menu(driver)
    profile.click_on_home_drawr_forward_icon(driver)


@then(parsers.parse('Verify that message should be shown "{text}"'))
@then(parsers.parse('My badges below that profile name with text "{text}"'))
def no_badges(driver, text):
    profile.verify_no_badges_text(driver, text)


# scenario 2
@given('Launch the App online')
def launch_app(driver):
    set_connection_type(driver, 'WIFI_ONLY')
    home.navigate_to_home_screen(driver)


@given('User is Logged In user with some data.')
def loged_in(driver):
    pass


#
@when('User is in profile screen')
def profile_screen(driver):
    profile.verify_profile_screen(driver)


@then('Verify that back arrow on the top left corner')
def back_arrow(driver):
    profile.verify_back_arrow(driver)


@then('Profile Image beside Profile name (Default Avatar) with Edit option')
def avtar(driver):
    profile.verify_avtar_and_edit_opn(driver)


@then('Profile Name below the profile image.')
def profile_name(driver):
    profile.verify_profile_name(driver)


@then('My badges below that profile name with badges name.')
def badges(driver):
    profile.verify_badges_and_badges_list(driver)


@then('Course Selection drop down below the profile name')
def course_selection(driver):
    profile.verify_course_selection(driver)


@then('Profile Completeness Progression in Percentage')
def profile_completeness(driver):
    profile.verify_profile_completion_and_percentage(driver)


# scenario 3
@given('Launch app on offline')
def launch_offline(driver):
    code = get_data(Login_Credentials, 'login_details2', 'code')
    countrycode = get_data(Login_Credentials, 'login_details2', 'country_code')
    mobno = get_data(Login_Credentials, 'login_details2', 'mobile_no')
    otp = get_data(Login_Credentials, 'login_details2', 'OTP')
    home.navigate_to_home_screen(driver)
    home_screen.click_on_hamburger_menu(driver)
    profile.click_on_home_drawr_forward_icon(driver)
    profile.select_offline_mode(driver)


@given('User is in profile screen')
def profile_screen_offline(driver):
    profile.verify_profile_screen(driver)


@when('User taps on profile image')
def tap_profile(driver):
    profile.click_on_profile_image(driver)


# scenario 4
@when('User switch the grade')
def switch_grade(driver):
    profile.click_on_grade_selection_dropdown(driver)


@then(parsers.parse('Verify that page is loading and toast message "{text}" should be displayed.'))
def page_loading_toast(driver, text):
    profile.select_any_course(driver)
    profile.verify_empty_field_error(driver, text)
    set_connection_type(driver, 'WIFI_ONLY')


# scenario 5
@given('Launch the app')
def launch_with_profile(driver):
    set_connection_type(driver, 'WIFI_ONLY')
    home.navigate_to_home_screen(driver)
    home_screen.click_on_hamburger_menu(driver)
    profile.click_on_home_drawr_forward_icon(driver)


@then('Verify that User should be displayed popup with list of avatars')
def avtar_popup(driver):
    profile.verify_avtar_pop_up(driver)


# scenario 6
@when('User is in Avatar popup')
def verify_avtar_popup(driver):
    profile.click_on_profile_image(driver)
    profile.verify_avtar_pop_up(driver)


@then('Verify that avatar label and list avatar should be displayed')
def list_avtar(driver):
    profile.verify_avtar_label_and_list_of_avtars(driver)


# scenario 7
@given('User is in Avatar popup')
def avtar_pop_up(driver):
    profile.click_on_profile_image(driver)
    profile.verify_avtar_pop_up(driver)


@when('User selects the profile image')
def profile_image(driver):
    profile.select_pro_image_from_avtars(driver)


@then('Verify that user navigate back to profile screen and profile image should be changed')
def changed_pro_image(driver):
    profile.verify_profile_image_if_selected(driver)


# scenario 8
@when('User taps on device back button')
def device_bck_btn(driver):
    click_on_back_button(driver)


@then('Verify that popup should be dismissed')
def avtar_popup_dismissed(driver):
    profile.verify_avtar_pop_up(driver)


# scenario 9
@when('User comes out of popup without selecting an avatar')
def without_selecting_pro_image(driver):
    click_on_back_button(driver)


@then('Verify that Old image should be retained in profile screen')
def old_image_retained(driver):
    profile.verify_profile_image_if_not_selected(driver)


# scenario 10
@when('User taps on course selection drop down')
def select_course(driver):
    profile.click_on_grade_selection_dropdown(driver)


@then('Verify that user should taken to bottom sheet dialog with list of all courses')
def course_bottom_sheet(driver):
    profile.verify_course_bottom_sheet_dialog(driver)


# scenario11
@given('user is in profile screen')
def profile_select(driver):
    home_screen.click_on_hamburger_menu(driver)
    profile.click_on_home_drawr_forward_icon(driver)


@when('User is in course selection sheet')
def course_selection_sheet(driver):
    profile.verify_course_bottom_sheet_dialog(driver)


@then(
    'Verify that change your grade label and list of all  Courses like 6th grade, 7th grade, 8th grade, 9th grade, 10th grade, 11th & 12th grade, 4th grade, 5th grade, 11th Grade - Commerce, Bank PO, Campus Recruitment, CAT, IAS, GRE, GMAT with radio button option should be displayed')
def course_list(driver):
    profile.all_courses(driver)


# scenario 12
@given('User taps on course selection drop down')
def select_course1(driver):
    profile.click_on_grade_selection_dropdown(driver)


@when('User taps on any course')
def select_any_course(driver):
    #     profile.select_any_course(driver)
    pass


@then('Verify that user switches the course')
def switch_the_courese(driver):
    profile.selected_course_with_radio_btn(driver)


@then(parsers.parse('it should display a toast message "{text}"'))
def course_text_msg(driver, text):
    profile.verify_grade_change_toast_msg(driver, text)
    profile.switch_to_8th_grade(driver)


# scenario 13
@then('Verify that tick mark should be shown for enrolled user')
def enrolled_course(driver):
    profile.check_enrolled_courses(driver)


# scenario 14
@then('Verify that radio button is selected for current course')
def radio_btn_enabled(driver):
    profile.check_course_radio_btn_enabled(driver)


# @scenario 15
@when('tap on device back button')
def back_button(driver):
    click_on_back_button(driver)


@then('Verify that course selection dialog should be dismissed')
def course_dialog_dismissed(driver):
    profile.verify_course_bottom_sheet_dialog(driver)


#  scenario 16   
@then('should have "Earn Your First Badge" button')
def earn_badge_btn(driver):
    profile.verify_earn_badge_btn(driver)


# scenario 17
@given('User earned few badges')
def earned_badges(driver):
    pass


@then('Verify that all badges and see all forward arrow should be displayed')
def all_badges_see_all(driver):
    profile.verify_three_badges_and_see_all(driver)


# scenario 18
@given('User earned three badges')
def earned_three_badges(driver):
    profile.verify_only_three_badges(driver)


@then('Verify that only three badges should be displayed')
def displayed_badges(driver):
    profile.verify_only_three_badges(driver)


# scenario 19
@when('User taps on see all button under my badges')
def tap_on_badge_see_all(driver):
    profile.click_on_badge_see_all_icon(driver)


@then('Verify that user should be navigate to "Earned Badges Screen"')
def badge_screen(driver):
    profile.verify_badges_screen(driver)


# scenario 20

@then(parsers.parse('Verify that profile completion section is "{percentage}" by default'))
def default_profile_completion(driver, percentage):
    profile.verify_profile_completion_percentage(driver, percentage)


# scenario 21 
@given('Launch the app Online')
def launch_app_for_gender_updation(driver):
    home.navigate_to_home_screen(driver)
    home_screen.click_on_hamburger_menu(driver)
    profile.click_on_home_drawr_forward_icon(driver)


@when('User update gender in profile details')
def update_gender_first(driver):
    profile.update_gender(driver)


@then(parsers.parse('Verify that profile completion section updates to "{percentage}"'))
def profile_percentage_85(driver, percentage):
    profile.verify_profile_completion_percentage(driver, percentage)


# scenario 22 
@given('Launch the App Online')
def launch_app_for_bday_updation(driver):
    pass


@when('User update Date of Birth in profile details')
def update_bday_first(driver):
    profile.update_bday(driver)


#  scenario23   
@when('User updates both date of birth and gender in profile details')
def bday_gender_update(driver):
    profile.update_gender(driver)
    profile.update_bday(driver)


@then(parsers.parse('Verify that profile completion section updates to "{percentage}"'))
def bday_gender_percentage(driver, percentage):
    profile.verify_profile_completion_percentage(driver, percentage)


# scenario 27
@when('user is in profile screen')
def profile_select2(driver):
    home_screen.click_on_hamburger_menu(driver)
    profile.click_on_home_drawr_forward_icon(driver)
    profile.verify_profile_screen(driver)


@then('Verify that mobile number field should be displayed')
def verify_phone(driver):
    profile.verify_phn_no_and_icon(driver)


# scenario 28
@given('Launch the app online')
def launch_app2(driver):
    home.navigate_to_home_screen(driver)


@then('Verify that mobile number has a phone icon to the left and a <Edit> icon to the right should be displayed')
def phn_edit_icon(driver):
    profile.verify_phn_no_and_icon(driver)
    profile.verify_phn_no_edit_icon(driver)


# scenario 29  
@when('User taps on edit of mobile number field')
def tap_on_mobile_edit(driver):
    profile.click_phn_no_edit(driver)


@then(
    'Verify that Edit icon should displays a pop-up "Please enter your phone number" with options to switch country code and enter mobile number with submit button')
def feilds_in_edit_phon_popup(driver):
    profile.verify_feilds_in_edit_phn_popup(driver)
    profile.verify_submit_btn_edit_phn_popup(driver)


# scenario 30    
@when('Remove the existing mobile number')
def remove_no(driver):
    profile.click_phn_no_edit(driver)
    profile.remove_existing_mob_no(driver)


@when('User taps on submit button')
def tap_on_submit(driver):
    profile.click_submit_btn_edit_phn_popup(driver)


@then(parsers.parse('Verify that "{text}" error message should be displayed'))
def error_msg(driver, text):
    profile.verify_empty_phn_no_error_msg(driver, text)


# scenario 31
@when('User enter invalid mobile number')
def invalid_no(driver):
    profile.click_phn_no_edit(driver)
    profile.enter_invalid_mob_no(driver)
    profile.click_submit_btn_edit_phn_popup(driver)


# scenario 32
@when('User taps on device back button /anywhere outside that popup')
def tap_outside(driver):
    profile.click_phn_no_edit(driver)
    profile.touch_outside_phn_popup(driver)


@then('Verify that user redirects to profile screen')
@then('Verify that popup should be dismissed')
@then('Verify that change number popup should be displayed')
def number_pop_up_dissmissed(driver):
    profile.verify_profile_screen(driver)


# scenario 33
@when('User taps on submit button with existing mobile number')
def exixting_number(driver):
    profile.click_phn_no_edit(driver)
    profile.click_submit_btn_edit_phn_popup(driver)


@then(parsers.parse('Verify that "{text}" error message should be displayed'))
def verify_same_no_error(driver, text):
    profile.verify_same_no_error_msg(driver, text)


# scenario 34
@when('User changes the mobile number')
def change_number(driver):
    profile.click_phn_no_edit(driver)
    profile.enter_new_mob_no(driver)
    profile.click_submit_btn_edit_phn_popup(driver)


@then('Verify that user should be navigate to OTP screen')
def otp_screen(driver):
    profile.verify_otp_screen(driver)


# scenario 35
@when('User taps on cancel button on popup')
def tap_on_cancel(driver):
    profile.click_phn_no_edit(driver)
    profile.click_on_cancel_btn_in_phn_popup(driver)


# scenario 36
@then('<Gender>')
def verify_gender(driver):
    profile.verify_gender_icon(driver)


@then('<Birthday>')
def verify_birthday(driver):
    profile.verify_bday_icon(driver)


# scenario 37
@then(parsers.parse('Verify that gender should be displayed like "{text}"'))
def gender_txt2(driver, text):
    profile.scroll_down(driver)
    profile.verify_gender_icon_text(driver, text)


# scenario38
@when('User taps on edit button of gender in edit profile screen')
def edit_gender(driver):
    profile.click_profile_edit_icon(driver)
    profile.click_on_gender_field(driver)


@then('Verify that user redirects to edit gender profile screen.')
def edit_gender_screen(driver):
    profile.verify_gender_drop_down(driver)


# scenario 39
@when('User taps on edit button of birthday in edit profile screen')
def edit_bday(driver):
    profile.click_profile_edit_icon(driver)
    profile.click_on_birthday_field(driver)


@then('Verify that user redirects to edit birthday profile screen.')
def edit_bday_screen(driver):
    profile.verify_calender_popup(driver)


# scenario 40
@when('User taps on edit button of profile details')
def tap_edit_profile(driver):
    profile.click_profile_edit_icon(driver)


@then('Verify that user redirects to edit profile screen.')
def edit_profile_screen1(driver):
    profile.verify_edit_profile_screen(driver)


# scenario 41
@given('User is in edit profile screen')
def edit_profile(driver):
    home_screen.click_on_hamburger_menu(driver)
    profile.click_on_home_drawr_forward_icon(driver)
    #     profile.select_offline_mode(driver)
    profile.click_profile_edit_icon(driver)
    profile.verify_edit_profile_screen(driver)


@when('User taps on back arrow')
def back_arrow1(driver):
    profile.click_back_arrow(driver)


# scenario 42  
@when('User is in edit profile screen')
def edit_screen2(driver):
    home_screen.click_on_hamburger_menu(driver)
    profile.click_on_home_drawr_forward_icon(driver)
    profile.click_profile_edit_icon(driver)
    profile.verify_edit_profile_screen(driver)


@then(parsers.parse('A text "{text}" below the app back arrow'))
def edit_profile_text(driver, text):
    profile.verify_edit_profile_text(driver, text)


@then('Name field with icon')
def name_icon(driver):
    profile.verify_edit_name_field_and_icon(driver)


@then('Email field with icon')
def email_icon2(driver):
    profile.verify_email_icon_and_value(driver)


@then('Gender field with icon')
def gender_and_icon(driver):
    profile.verify_gender_icon(driver)
    profile.verify_gender_edit_field(driver)


@then('Location field with icon')
def location_and_icon(driver):
    profile.verify_location_field_and_icon(driver)


@then('Birthday field with icon')
def bday_and_icon(driver):
    profile.verify_bday_icon(driver)
    profile.verify_birthday_edit_field(driver)


@then('"Save" button bottom of the page')
def save_btn(driver):
    profile.verify_save_button(driver)


# scenario 43
@when('User taps on name field')
def tap_on_name(driver):
    profile.click_on_name_field(driver)


@then('Verify that location field should be editable')
@then('Verify that email field should be editable')
@then('Verify that name field should be editable')
def editable(driver):
    profile.check_field_editable(driver)


# scenario 44
@when('User taps on email field')
def tap_on_email(driver):
    profile.click_on_email_field(driver)


# scenario 45
@when('User taps on gender field')
def tap_on_gender(driver):
    profile.click_on_gender_field(driver)


@then('Verify that gender drop down displayed and any one should be selectable')
def gender_selection(driver):
    profile.verify_gender_drop_down(driver)


# scenario 46
@when('User taps on location field')
def tap_on_location(driver):
    profile.click_on_location_field(driver)


# scenario 47
@when('User taps on auto detect')
def tap_on_location_auto_detect(driver):
    profile.tap_on_location_icon1(driver)


@then('Verify that it should detect current location')
def verify_current_location(driver):
    profile.handle_gps_location_popup(driver)
    profile.get_location(driver)


@when('User selects future date')
def future_date(driver):
    profile.enter_future_date_in_bday_field(driver, "2021")


@then('Verify that future date resets to current year and should allow only valid dates')
def future_date_reset(driver):
    profile.get_bday_date(driver)


# scenario 50
@when('User taps on set button in calendar popup')
def tap_on_calender_set_btn(driver):
    pass


@then('Verify that calendar popup should update the date')
def updated_date(driver):
    profile.verify_updated_bday_date_in_calender(driver)


# scenario 51
@when('User taps on cancel button in calendar popup')
def cancel_calender_popup(driver):
    profile.verify_calender_popup(driver)
    profile.click_on_cancel_btn_in_phn_popup(driver)


@then('Verify that calendar popup should be dismissed')
def calender_popup_dismissed(driver):
    profile.verify_edit_profile_screen(driver)


# scenario 52
@when('User delete the name')
def delete_name(driver):
    profile.clear_name_field(driver)
    profile.hide_keyboard(driver)


@when('taps on save button')
def tap_on_save(driver):
    profile.click_save_button(driver)


@then(parsers.parse('Verify that error message "{text}" should be displayed.'))
@then(parsers.parse('Verify that error message "{text}" should be displayed.'))
@then(parsers.parse('Verify that error message "{text}" should be displayed'))
def name_error(driver, text):
    profile.verify_empty_field_error(driver, text)


#  scenario 53    
@when('User delete the email address')
def delete_email(driver):
    profile.clear_email_field(driver)
    profile.hide_keyboard(driver)


# scenario 54
@when('User deletes the location data')
def delete_location(driver):
    profile.clear_location_field(driver)
    profile.hide_keyboard(driver)


# scenario 55
@when('User enter all profile details')
def enter_all_data(driver):
    profile.verify_all_edit_profile_fields(driver)


@then('Verify that user should be redirects to profile screen with toast message <profile have been updated>')
def verify_profile_toast(driver):
    profile.verify_profile_updation_toast(driver)


# scenario 57
@when('User taps on sign out button')
def tap_on_sign_out(driver):
    profile.scroll_down(driver)
    profile.click_on_sign_out(driver)


@then('Verify that bottom sheet dialog displayed')
def sign_out_bottom_dialog(driver):
    profile.verify_sign_out_bottom_sheet(driver)


# scenario 58
@when('User is in sign out bottom sheet dialog')
def redirect_to_sign_out_dialog(driver):
    profile.scroll_down(driver)
    profile.click_on_sign_out(driver)
    profile.verify_sign_out_bottom_sheet(driver)


@then('Verify that Label <Sign out> should be displayed')
def sign_out_label(driver):
    profile.verify_sign_out_text_in_dialog(driver)


@then(parsers.parse('Text "{text}" message'))
def sign_out_bottom_sheet_msg(driver, text):
    profile.verify_sign_out_dialog_msg(driver, text)


@then('CTA <Yes> and <Cancel>')
def yes_and_cancel(driver):
    profile.verify_sign_out_dialog_yes_and_cancel_btn(driver)


# scenario 59   
@when('User taps on yes button in sign out dialog sheet')
@when('User taps on yes button')
def tap_on_yes(driver):
    profile.click_on_sign_out_dialog_yes_btn(driver)


@then('Verify that user redirects to login screen')
def login_screen(driver):
    profile.verify_login_page(driver)


# scenario 60
@when('User taps on cancel button')
def tap_on_cancel2(driver):
    profile.click_on_sign_out_dialog_cancel_btn(driver)


@then('Verify that bottom sheet dialog should be dismissed')
def verify_sign_out_popup_dismissed(driver):
    profile.verify_sign_out_bottom_sheet(driver)


# scenario 61  
@when('User is on offline')
def user_offline(driver):
    profile.select_offline_mode(driver)


@then(parsers.parse('Verify that toast message "{text}" should be displayed.'))
def offline_toast_msg(driver, text):
    profile.verify_sign_out_no_internet(driver, text)
    sleep(2)
    set_connection_type(driver, 'WIFI_ONLY')


# scenario 79
@then('verify Phone Number field with icon in Account details')
def acc_phn(driver):
    profile.verify_phn_no_and_icon(driver)


@then('An Edit icon should be shown next to this field click on edit icon')
def phn_edit(driver):
    profile.click_phn_no_edit(driver)


@then('Phone number field should accept only numeric values.')
def phn_numeric(driver):
    profile.verify_phn_no_and_text(driver)


# scenario 80
@given('User taps on profile card on hamburger menu')
def hamburger_menu(driver):
    profile.navigate_to_profile_card(driver)


@then('Verify that Profile Details has all fields <Name>')
@then('verify Profile Name with icon and should be Pre Filled')
def profile_name_icon(driver):
    profile.scroll_down(driver)
    profile.verify_profile_name_icon(driver)


@then('<Email>')
@then('verify Email with icon and should be Pre Filled')
def email_icon(driver):
    profile.verify_email_icon_and_value(driver)


@then('<Location>')
@then('verify Location with icon and should be Pre Filled')
def loc_icon(driver):
    profile.verify_phn_no_and_text(driver)


@then(parsers.parse('verify gender with icon with "{text}" text'))
def gender_txt(driver, text):
    profile.verify_gender_icon_text(driver, text)


@then(parsers.parse('Verify that date of birth should be displayed like "{birthday_text}"'))
@then(parsers.parse('verify birthday with icon with "{birthday_text}" text'))
def bday_txt(driver, birthday_text):
    profile.verify_bday_icon_text(driver, birthday_text)


@then('<SignOut>')
@then('Sign out button with icon')
def sign_out(driver):
    profile.verify_sign_out_and_image(driver)
