import time

from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.constants import Login_Credentials
from constants.load_json import get_data
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute

scenarios('../features/Pre-Class Experience.feature')


@fixture()
def login_in(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in


@fixture()
def neo_in_class(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.ANDROID.value)
        yield neo_in_class
    elif Platform.WEB.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.WEB.value)
        yield neo_in_class


@fixture()
def neo_tute(driver):
    neo_tute = NeoTute(driver)
    yield neo_tute



@fixture()
def student2(request):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student2 = LoginFactory().get_page(None, Platform.ANDROID.value)
        yield student2
    elif Platform.WEB.name in platform_list:
        student2 = LoginFactory().get_page(None, Platform.WEB.value)
        yield student2


@fixture()
def student2_neo(request, student2):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student2_neo = NeoInClassFactory().get_page(student2.driver, Platform.ANDROID.value)
        yield student2_neo
    elif Platform.WEB.name in platform_list:
        student2_neo = NeoInClassFactory().get_page(student2.driver, Platform.WEB.value)
        yield student2_neo


@fixture()
def mweb_login(request):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        mweb_login = LoginFactory().get_page(None, Platform.ANDROID.value)
        yield mweb_login
    elif Platform.WEB.name in platform_list:
        mweb_login = LoginFactory().get_page(None, Platform.WEB.value)
        yield mweb_login


@fixture()
def mweb_student(request, mweb_login):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        mweb_student = NeoInClassFactory().get_page(mweb_login.driver, Platform.ANDROID.value)
        yield mweb_student
    elif Platform.WEB.name in platform_list:
        mweb_student = NeoInClassFactory().get_page(mweb_login.driver, Platform.WEB.value)
        yield mweb_student



@given("launch the application online as neo user and navigate to home screen")
def navigate_to_one_to_many_and_mega_user(login_in):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    login_in.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@given("tutor start the session")
def step_impl(neo_tute):
    # TODO Needs to be updated to fetch from DB. For time being, below workaround
    neo_tute.start_neo_session(login_data="neo_login_detail1", user='student1', date="tomorrow")


@when('click on "JOIN" button in home page')
def step_impl(login_in,neo_in_class):
    login_in.click_on_byjus_classes_card()
    neo_in_class.click_on_future_join_card(1)


@then('Verify the profile photo edit functionality when user clicks on edit icon')
def step_impl(neo_in_class):
    neo_in_class.click_photo_edit_icon()


@then('Verify the "Change profile photo" pop up when user selects "Use Camera" option.')
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_change_profile_photo_popup(),True,"Verify the Change profile photo pop up")


@then('Verify that student able to close, change profile photo pop up by tapping on close icon')
def step_impl(neo_in_class):
    check.equal(neo_in_class.close_profile_photo_popup(),False,"Student able to close, change profile photo pop up by tapping on close icon")


@then('Verify adjusting image by drag image option in Adjust Photo pop up.')
def step_impl(neo_in_class):
    neo_in_class.upload_photo("../../../files/SamplePNG.png")
    details =neo_in_class.verify_adjust_photo_popup()
    check.equal(details.result, True,details.reason)


@then('Verify that student able to close, Adjust photo pop up by tapping on close icon')
def step_impl(neo_in_class):
    check.equal(neo_in_class.close_profile_photo_popup(),False,"Student able to close, Adjust photo pop up by tapping on close icon")


@then('Verify that student able to change photo by tapping on change icon')
def step_impl(neo_in_class):
    neo_in_class.upload_photo("../../../files/SamplePNG.png")
    neo_in_class.click_on_change_button()
    check.equal(neo_in_class.verify_change_profile_photo_popup(), True, "Student clicked on change button and Change profile photo pop up present")
    neo_in_class.close_profile_photo_popup()


@then('Verify that student able to save photo by tapping on Save icon')
def step_impl(neo_in_class):
    neo_in_class.upload_photo("../../../files/SamplePNG.png")
    neo_in_class.save_selected_photo()


@then("Verify the student's name bubble when photo approval is pending.")
@then('Verify the approval pending flash message when user uploads a photo for user profile.')
@then("Verify that till the time photo is in review state, student will see own photo with overlay text shown as per zeplin")
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_photo_approval_pending(),True,"Verified student's name bubble when uploaded photo approval is pending")


@then("Verify hovering over student's name bubble when uploaded photo approval is pending.")
def step_impl(neo_in_class):
    neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    details = neo_in_class.hover_over_student_bubble_approval_pending()
    check.equal(details.result, True, details.reason)


@then('Verify that once tutor approves photo will be visible to student only if student refresh screen')
def step_impl(neo_tute,neo_in_class):
    neo_tute.click_on_tab_item(tab_name="Student Details")
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    neo_tute.approve_profile_pic(student1_details['name'])
    check.equal(neo_in_class.approved_profile_pic_visible(), False,"Approved photo not visible to student before student refresh screen")
    neo_in_class.page_refresh()
    check.equal(neo_in_class.approved_profile_pic_visible(),True,"Approved photo visible to student after student refresh screen")


@then('Verify the congratulations flash message when uploaded photo gets approved.')
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_toast_message('Congratulations! Your profile photo is approved.'), True, "Congratulations flash message when uploaded photo gets approved.")
    neo_in_class.close_toast_message()


@then('Verify the edit button in bubble before & after photo gets approved')
def step_impl(neo_in_class):
    check.equal(neo_in_class.is_photo_edit_icon_present(), True,"Edit button in bubble is still present after photo approved")


@then('Verify the rejected flash message upon when user uploads a photo for user profile.')
def step_impl(neo_tute,neo_in_class):
    neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    neo_tute.click_on_tab_item(tab_name="Class Forum")
    neo_tute.click_on_tab_item(tab_name="Student Details")
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    neo_tute.reject_profile_pic(student1_details['name'])
    neo_in_class.page_refresh()
    check.equal(neo_in_class.verify_toast_message('Your profile picture wasn`t approved. Please try uploading another picture'),
                True, "Rejected flash message displayed when user uploads photo and tutor rejects")
    neo_in_class.close_toast_message()


@then('Verify the bubble when uploaded photo gets rejected for the logged in user.')
def step_impl(neo_in_class):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    details = neo_in_class.get_current_student_bubble(student1_details['name'])
    check.equal(details.result, True, details.reason)


@then('Verify the error message when internet connection is lost while uploading an image')
def step_impl(neo_in_class):
    neo_in_class.set_network_flaky()
    neo_in_class.click_photo_edit_icon()
    check.equal(neo_in_class.verify_toast_message('Network error, please check your connection and retry'), True, "Error message displayed when internet connection is lost")
    neo_in_class.close_profile_photo_popup()
    neo_in_class.close_toast_message()
    neo_in_class.set_wifi_connection_on()

@then('Verify that student can upload photo only in JPEG,JPG,PNG format')
def step_impl(neo_in_class):
    flag1 = neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    check.equal(flag1, True,"Student can upload photo in JPEG,JPG,PNG format")
    flag2 = neo_in_class.upload_profile_photo_api("../../../files/SamplePDF.pdf")
    check.equal(flag2, False, "Student cannot upload photo other than JPEG,JPG,PNG format")


@then('Verify that maximum size allowed for photo should be upto 3MB')
def step_impl(neo_in_class):
    flag = neo_in_class.upload_profile_photo_api("../../../files/SampleJPG5mb.jpg")
    check.equal(flag, False, "Upload failed as maximum size allowed for photo is upto 3MB")


@then('Verify uploading photos with different resolutions and sizes in the change profile photo pop up.')
def step_impl(neo_in_class):
    flag1 = neo_in_class.upload_profile_photo_api("../../../files/SampleJPG1mb.jpg")
    print(flag1)
    flag2 = neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    print(flag2)
    check.equal(flag1 and flag2, True, "Photo upload successful for different resolutions and sizes")


@given("Launch the application online in mobile")
def login_as_neo_user(login_in):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    login_in.login_for_neo_class_mweb(student1_details['code'], student1_details['mobile_no'], otp=None)

@then('Verify the display of bubble screen')
def step_impl(neo_in_class):
    details = neo_in_class.is_students_bubbles_present()
    check.equal(details.result, True, details.reason)

@then('verify the display of scroll bar in landscape mode')
@then('Verify the scroll feature in PreClass screen on a mobile browser')
@then('Verify the bubble screen should be scrollable')
def step_impl(neo_in_class):
    details = neo_in_class.is_scroll_present()
    check.equal(details.result, True, details.reason)

@then('Verify that Save and Cancel button is present in Profile Photo pop up in web browser')
def step_impl(neo_in_class):
    neo_in_class.click_photo_edit_icon()
    neo_in_class.upload_photo("../../../files/SamplePNG.png")
    details = neo_in_class.verify_profile_photo_popup()
    check.equal(details.result, True, details.reason)


@then('Verify the animation of student bubbles present in PreClass screen')
def step_impl(neo_in_class):
    details = neo_in_class.verify_bubble_animation_preclass_screen()
    check.equal(details.result, True, details.reason)

@then('Verify the user login name and the name displayed in the pre class screen')
def step_impl(neo_in_class):
    student1_details = get_data(Login_Credentials, 'neo_login_detail3', 'student2')
    details = neo_in_class.verify_user_login_name(student1_details['name'])
    check.equal(details.result, True, details.reason)


@then('verify the pre class screen in offline mode')
def step_impl(neo_in_class):
    neo_in_class.set_network_flaky()
    details = neo_in_class.is_network_failed_toast_msg_present()
    check.equal(details.result, True, details.reason)

@then('Verify the pre-class screen in landscape mode')
@then('Verify the PreClass screen in landscape mode in mobile browser')
@then('Verify that class info screen should be as per zeplin')
def step_impl(neo_in_class):
    details = neo_in_class.verify_class_info_screen()
    check.equal(details.result, True, details.reason)

@then('Verify the font of session description in landscape mode in mobile browser')
def step_impl(neo_in_class):
    details = neo_in_class.verify_font_of_session_description('Gotham-Book')
    check.equal(details.result, True, details.reason)

@then('Verify the pre class screen when topic description text is too long read more/readless should be displayed')
def step_impl(neo_in_class):
    details = neo_in_class.verify_session_description_in_preclass_screen()
    check.equal(details.result, True, details.reason)

@then('verify the pre class timer when the screen is running in the background')
def step_impl(neo_in_class):
    details = neo_in_class.verify_timer_in_preclass()
    check.equal(details.result, True, details.reason)

@then('verify the pre class timer when the screen is locked or kept idle')
def step_impl(neo_in_class):
    details = neo_in_class.verify_timer_countdown_in_preclass()
    check.equal(details.result, True, details.reason)




@then("Verify the student name on greeting message and student bubble")
@then("Verify the Student's greeting message on the landing screen.")
def step_impl(neo_in_class):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    student_name = student1_details['name']
    details = neo_in_class.preclass_verify_greeting_message(name = student_name)
    check.equal(details.result, True, details.reason)


@then("Verify the list of students bubble on the screen before the class starts.")
def step_impl(neo_in_class):
    time.sleep(3)
    details = neo_in_class.preclass_verify_bubbles()
    check.equal(details.result, True, details.reason)


@then("Verify that edit icon should be displayed for the logged in user's name bubble")
def step_impl(neo_in_class):
    details =neo_in_class.preclass_verify_current_student_edit_button()
    check.equal(details.result,True,details.reason)


@then("Verify the student's name bubbles when any student joins the session.")
def step_impl(student2, student2_neo,neo_in_class):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student2')
    student2.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)
    student2_neo.navigate_to_byjus_classes_screen()
    student2_neo.join_not_started_session()
    details = neo_in_class.preclass_verify_bubble_displayed(profile_name = student1_details['name'])
    check.equal(details.result, True, details.reason)


@then("Verify the student's name bubbles when any student exists the session.")
def step_impl(student2,neo_in_class):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student2')
    student2.driver.close()
    details = neo_in_class.preclass_verify_bubble_displayed(profile_name = student1_details['name'])
    check.equal(details.result, True, details.reason)


@then("Verify the slider present in PreClass screen")
@then("Verify scroll functionality below the students bubble list.")
def step_impl(neo_in_class):
    details = neo_in_class.is_scroll_bar_working()
    check.equal(details.result, True, details.reason)


@then("Verify that display timer countdown on screen.")
def step_impl(neo_in_class):
    details = neo_in_class.preclass_is_timer_displayed()
    check.equal(details.result, True, details.reason)


@then("Verify the tutor name & image on screen.")
def step_impl(neo_in_class):
    details = neo_in_class.preclass_verify_tutor_name(name = "Test Automation")
    check.equal(details.result, True, details.reason)
    details =neo_in_class.preclass_verify_tutor_thumbnail()
    check.equal(details.result, True, details.reason)


@then("Verify the texts when user clicks on Read More option.")
@then("Verify that subject & topic name should be displayed correctly.")
def step_impl(neo_in_class):
    details = neo_in_class.preclass_verify_subject_topic_name(name = 'Control and Coordination')
    check.equal(details.result, True, details.reason)


@then("Verify the bubble when user hover other student's name.")
def step_impl(neo_in_class):
    details = neo_in_class.verify_hover_over_bubble(name="You")
    check.equal(details.result, True, details.reason)


@then("Verify clicking on Byjus logo at the top left corner.")
def step_impl(neo_in_class):
    details = neo_in_class.preclass_click_on_logo()
    check.equal(details.result, True, details.reason)


@given("Launch the application online in mobile")
def login_as_neo_user(mweb_login):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student3')
    mweb_login.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)
    mweb_login.maximize_to_web()


@then("Verify the student name on greeting message and student bubble")
def step_impl(mweb_student):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student3')
    student_name = student1_details['name']
    details = mweb_student.preclass_verify_greeting_message(name = student_name)
    check.equal(details.result, True, details.reason)


@then("Verify the Student name on the bubble present in PreClass screen")
def step_impl(mweb_student):
    details = mweb_student.verify_hover_over_bubble(name="You")
    check.equal(details.result, True, details.reason)


@then("Verify the slider present in PreClass screen")
def step_impl(mweb_student):
    details = mweb_student.is_scroll_bar_working()
    check.equal(details.result, True, details.reason)


@then("student join neo session for next day for mobile web")
def login_as_neo_user(mweb_login,mweb_student):
    mweb_login.click_on_byjus_classes_card()
    mweb_student.click_on_future_join_card(1)
