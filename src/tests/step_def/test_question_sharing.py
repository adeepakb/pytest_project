from time import sleep
import subprocess
from selenium.webdriver.common import keys
from appium import webdriver
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from POM_Pages.Question_Sharing import QuestionSharing
from Utilities.BasePage import BaseClass
browser = fixture = 'browser'


baseClass = BaseClass()
questionSharing =QuestionSharing(browser)
featureFileName = 'Question Sharing'


baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""

scenarios('../features/' + featureFileName + '.feature')

@given('Launch the app online and navigate to Home screen')
def loginapp(browser):
    questionSharing.navigate_to_home_screen(browser)

@given('Navigate to bookmark question screen')
def navigate_to_bookmark_question_screen(browser):
    questionSharing.navigate_to_bookmark_question_screen(browser)


@when('Tap on Share option')
def tap_on_share_icon(browser):
    questionSharing.tap_on_share_icon(browser)

    
@then('Verify that user should be able to see Share with pop up with different sharing apps installed in the device.')
def verify_share_with_popup_and_list(browser):
    questionSharing.verify_share_with_popup_and_list(browser)


@given('Tap on Share option')
def tap_on_share_icon1(browser):
    questionSharing.tap_on_share_icon(browser)

    
@when(parsers.parse('Select "{option}" option in Share with popup'))
def select_option_to_share(browser,option):
    questionSharing.select_option_to_share(browser,option)


@when('Enter recipient <EmailId>')
def enter_recipient_mail_id(browser,EmailId):
    questionSharing.enter_recipient_mail_id(browser,EmailId)

    
@when('Tap on send button')
def tap_on_gmail_send_option(browser):
    questionSharing.tap_on_gmail_send_option(browser)

    
@then('Verify that user should be able to share the question to the recipient mail id')
def verify_mail_is_sent(browser):
    questionSharing.verify_mail_is_sent(browser)
    
@then('Verify that user should navigate to compose mail screen')
def verify_gmail_compose_screen(browser):
    questionSharing.verify_gmail_compose_screen(browser)
    

@then(parsers.parse('Verify the subject "{text}"'))
def verify_subject_in_mailcompose_scn(browser,text):
    questionSharing.verify_subject_in_mailcompose_scn(browser,text)


@then(parsers.parse('Verify the description "{text}" along with link to navigate to Byjus app'))
def verify_body_text_in_a_mail(browser,text):
    questionSharing.verify_descriptiontext_and_link_in_a_mail(browser,text)


@when('Tap on share option for more than 6 times')    
@when('Tap on share option for 6 times')
def get_share_limit_reached_btmsheet_dialog(browser):
    questionSharing.get_share_limit_reached_btmsheet_dialog(browser)


@then(parsers.parse('Verify the "{text}" label'))
@when(parsers.parse('Verify that user should get "{text}" bottom sheet dialog'))
@then(parsers.parse('Verify that user should get "{text}" bottom sheet dialog'))
def verify_bottom_sheet_dialog(browser,text):
    questionSharing.verify_bottom_sheet_dialog(browser,text)


@then('Verify the bookmarked question image')
def verify_attached_screenshot(browser):
    questionSharing.verify_attached_screenshot(browser)


@then(parsers.parse('Verify the "{text}" button'))
def verify_the_button(browser,text):
    questionSharing.verify_the_button(browser,text)

  
@then(parsers.parse('Verify the "{text}" text'))
def verify_the_text(browser,text):
    questionSharing.verify_the_text(browser,text)


@then('Verify that A hero image should be present on bottom sheet dialog')
def verify_hero_image(browser):
    questionSharing.verify_hero_image(browser)


@when('Tap on "Close" button')
def tap_on_primaryActionBtn(browser):
    questionSharing.tap_on_primaryActionBtn(browser)    


@then('Verify that Share limit reached bottom sheet dialog should disappear')
def bottom_sheet_dialog_dismissed(browser):
    questionSharing.bottom_sheet_dialog_dismissed(browser)
    
@when('Select recipient to share content')
def select_recipient_share_in_whatsapp(browser):
    questionSharing.select_recipient_share_in_whatsapp(browser)
    
@then('Verify the bookmarked question image attached')
def verify_attached_photo(browser):
    questionSharing.verify_attached_photo(browser)
    
@then(parsers.parse('Verify the description "{text}" along with link to navigate to Byjus app in whats app'))
def verify_descriptiontext_and_link_in_a_whatsapp(browser,text):
    questionSharing.verify_descriptiontext_and_link_in_a_whatsapp(browser,text)
    
@then('Verify that user should navigate to messages screen')
def verify_attached_photo_sms(browser):
    questionSharing.verify_attached_photo_sms(browser)

@then('Verify the bookmarked question image in SMS')
def user_is_in_messages_screen(browser):
    questionSharing.user_is_in_messages_screen(browser)

@then(parsers.parse('Verify the description "{text}" along with link to navigate to Byjus app in SMS'))
def verify_descriptiontext_and_link_in_a_sms(browser,text):
    questionSharing.verify_descriptiontext_and_link_in_a_sms(browser,text)
   
