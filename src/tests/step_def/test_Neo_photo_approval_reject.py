import pytest_check as check
from pytest_bdd import scenarios, given, then, when
from pytest import fixture
from constants.constants import Login_Credentials
from constants.load_json import get_data
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
from utilities.neo_tute_mentoring import NeoTute

scenarios('../features/Tute-Photo Aproval,Rejection.feature')


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
def neo_tutor_1(driver):
    neo_tutor_1 = NeoTute(driver)
    yield neo_tutor_1


@fixture()
def neo_tutor_2(driver):
    neo_tutor_2 = NeoTute(driver)
    yield neo_tutor_2


@given("launch the application online as neo user and navigate to home screen")
def navigate_to_one_to_many_and_mega_user(login_in):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    login_in.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@given("tutor start the session")
def step_impl(neo_tutor_1):
    neo_tutor_1.start_neo_session()


@when('click on "JOIN" button in home page')
def step_impl(login_in,neo_in_class):
    login_in.click_on_byjus_classes_card()
    neo_in_class.click_on_future_join_card(1)


@then('Verify the element present in student detail screen as per zeplin')
@then('Verify that batch students details  are present in student detail screen')
def step_impl(neo_tutor_1):
    neo_tutor_1.click_on_tab_item(tab_name="Student Details")
    student_names = neo_tutor_1.get_all_names_student_details()
    check.equal(all(student_name is not None for student_name in student_names), True,"Student details present")
    check.equal(len(student_names) <= 25,True, "Max 25 students present")


@then("Verify the name and student first letter is present in the case when user not uploaded any image")
def step_impl(neo_tutor_1):
    all_profile_card_details = neo_tutor_1.get_img_src_for_all_students()
    for profile_card in  all_profile_card_details.values():
        student_name = profile_card[0]
        actual_profile_src = profile_card[1]
        if not 'https://tutoring-doubts-bucket.s3.ap-southeast-1.amazonaws.com/user_profile_images/students/' in actual_profile_src :
            expected_profile_src = "https://static.tllms.com/assets/k12/premium_online/byjus_classes/common/initial_avatars/%s.png"%student_name[0]
            flag = (expected_profile_src == actual_profile_src)
            check.equal(flag, True, "Student first letter is present in the case when user not uploaded any image")


@then('Verify that Approve ,Reject and Review is present on the card')
def step_impl(neo_in_class,neo_tutor_1):
    neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    neo_tutor_1.click_on_tab_item(tab_name="Class Forum")
    neo_tutor_1.click_on_tab_item(tab_name="Student Details")
    check.equal(neo_tutor_1.verify_approve_reject_review_buttons(),True,"Approve,Reject,Review text shown on the card")


@then('Verify that review option shown below the image')
def step_impl(neo_tutor_1):
    check.equal(neo_tutor_1.review_present_under_image(),True,"Review option shown below the image")


@then("Verify that newly updated image along with  'x' updated the profile. Please approve and review text shown on the card")
def step_impl(neo_tutor_1):
    neo_tutor_1.click_on_review()
    check.equal(neo_tutor_1.verify_new_pp_review_popup(),True,"Newly updated image ,Approve,review text,close icon shown on the review image popup")


@then('Verify that tapping on review "x" "new profile picture text"  along with image and Reject, Approve btn should be present')
def step_impl(neo_tutor_1):
    student_name = get_data(Login_Credentials, 'neo_login_detail1', 'student1')['name']
    check.equal("%s's New Profile Picture"%student_name in neo_tutor_1.text_on_pp_review_popup(),True,"new profile picture text present on review screen")


@then('Verify the close btn fuctionality on review screen')
def step_impl(neo_tutor_1):
    neo_tutor_1.click_on_close_pp_review_popup()


@then('Verify the text "You have approved x profile picture" toast message appears when tute approves along with close icon')
def step_impl(neo_tutor_1):
    neo_tutor_1.click_on_tab_item(tab_name="Student Details")
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    details = neo_tutor_1.approve_profile_pic(student1_details['name'])
    check.equal(details.result,True,details.reason)


@then('Verify the text "You have rejected x profile picture" toast message appears when tute reject along with close icon')
def step_impl(neo_tutor_1,neo_in_class):
    neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    neo_tutor_1.click_on_tab_item(tab_name="Class Forum")
    neo_tutor_1.click_on_tab_item(tab_name="Student Details")
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    details = neo_tutor_1.reject_profile_pic(student1_details['name'])
    check.equal(details.result, True, details.reason)


@then('Verify the approve request card when user change image for second time')
def step_impl(neo_tutor_1,neo_in_class):
    neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    neo_tutor_1.click_on_tab_item(tab_name="Class Forum")
    neo_tutor_1.click_on_tab_item(tab_name="Student Details")
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    details = neo_tutor_1.approve_profile_pic(student1_details['name'])
    check.equal(details.result,True,details.reason)


@then('Verify validation message is displayed when Tute approves/rejects photo approval request while internet connection is interrupted')
def step_impl(neo_tutor_1,neo_in_class):
    neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    neo_in_class.set_wifi_connection_off()
    neo_tutor_1.click_on_tab_item(tab_name="Class Forum")
    neo_tutor_1.click_on_tab_item(tab_name="Student Details")
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    details = neo_tutor_1.approve_profile_pic(student1_details['name'])
    check.equal(details.result,True,details.reason)
    neo_in_class.set_wifi_connection_on()


@then("Verify that tute able to approve or reject pending profiles only on next session")
def step_impl(neo_tutor_2,neo_in_class):
    neo_tutor_2.start_neo_session(login_data="neo_login_detail1", user='student1', date="tomorrow")
    neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    neo_tutor_2.click_on_tab_item(tab_name="Student Details")
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    details = neo_tutor_2.approve_profile_pic(student1_details['name'])
    check.equal(details.result, True, details.reason)
    neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    neo_tutor_2.click_on_tab_item(tab_name="Class Forum")
    neo_tutor_2.click_on_tab_item(tab_name="Student Details")
    details = neo_tutor_2.reject_profile_pic(student1_details['name'])
    check.equal(details.result, True, details.reason)
