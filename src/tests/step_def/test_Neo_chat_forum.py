import time

from pytest_bdd import scenarios, given, when, then, parsers
from pytest import fixture

from constants.constants import Login_Credentials
from constants.load_json import get_data
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
from utilities.neo_tute_mentoring import NeoTute

feature_file_name = 'Chat Forum'
import pytest_check as check

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def test_tut(driver):
    test_tut = NeoTute(driver)
    yield test_tut


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
def neo_in_class(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.ANDROID.value)
        yield neo_in_class
    elif Platform.WEB.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.WEB.value)
        yield neo_in_class


@fixture()
def login_in(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in



@given("Student launches in-class and navigate to home page")
def step_impl(login_in):
    student1_details = get_data(Login_Credentials, 'neo_login_detail2', 'student3')
    login_in.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@given("student navigates to byjus classes screen")
def step_impl(neo_in_class):
    neo_in_class.navigate_to_byjus_classes_screen()


@given('click on "JOIN" button in home page')
@when('click on "JOIN" button in home page')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()


@when("student join neo session")
@then("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()


@then("Verify the chat section Class Forum below the tutor's screen.")
def step_impl(neo_in_class):
    neo_in_class.verify_chat_elements()


@then("Verify that students count besides chat Forum.")
def step_impl(neo_in_class):
    neo_in_class.verify_chat_elements_element_wise(element_type='students count')


@then(parsers.parse('Verify that "{text}" in chat Forum.'))
def step_impl(neo_in_class, text):
    neo_in_class.verify_chat_elements_element_wise(element_type=text)


@then("Verify messages when users typed  any combination of alphanumeric & special characters in the chat box.")
def step_impl(neo_in_class):
    time.sleep(3)
    neo_in_class.send_chat(text='a1!2% N n')
    time.sleep(2)
    detail = neo_in_class.verify_a_text_in_chat(text='a1!2% N n')
    check.equal(detail.result, True, detail.reason)


@then(
    "Verify that text wrapping should happen without truncation or spill over the window when texts include multiple lines.")
def step_impl(neo_in_class):
    neo_in_class.send_chat(text='HI I am \n Tester')
    time.sleep(3)
    detail = neo_in_class.verify_a_text_in_chat(text='HI I am')
    check.equal(detail.result, True, detail.reason)
    detail = neo_in_class.verify_a_text_in_chat(text='Tester')
    check.equal(detail.result, True, detail.reason)


@when(
    "Student sends sticker")
def step_impl(neo_in_class):
    neo_in_class.send_sticker()


@then(
    "Verify sticker is shown in chat")
def step_impl(neo_in_class):
    neo_in_class.send_sticker()
    detail = neo_in_class.verify_sticker_displayed()
    check.equal(detail.result, True, detail.reason)


@when('student raises hand')
def step_impl(neo_in_class):
    neo_in_class.raise_hand()


@when('student lower hand')
def step_impl(neo_in_class):
    neo_in_class.unraise_hand()


@then('verify student hand is raised')
def step_impl(neo_in_class):
    detail = neo_in_class.verify_hand_is_raised()
    check.equal(detail.result, True, detail.reason)


@then('verify lower hand message is displayed')
def step_impl(neo_in_class):
    detail = neo_in_class.verify_lower_hand_text_is_displayed()
    check.equal(detail.result, True, detail.reason)


@then('student rejoins the session')
def step_impl(neo_in_class,login_in):
    login_in.relaunch_staging()
    neo_in_class.home_click_on_join()
    neo_in_class.join_neo_session()


@given("tutor start the session")
def step_impl(test_tut):
    test_tut.start_neo_session(login_data="neo_login_detail2", user='student1')


@when('tutor unraises hand for student')
def step_impl(test_tut):
    profile_cards = test_tut.click_on_menu_option(expected_student_name='Viviktha', menu_item='Hands Down')


@then("student's hand is unraised")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_hand_is_raised()
    check.equal(detail.result, False, detail.reason)


@when("wifi is turned off")
def step_impl(neo_in_class):
    neo_in_class.set_wifi_connection_off()


@when("students types random chat message")
def step_impl(neo_in_class):
    neo_in_class.type_chat("Hi Test")


@when("click on sticker icon")
def step_impl(neo_in_class):
    neo_in_class.click_on_sticker_icon()


@then("verify no message is sent in the chat")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_wifi_off_inchat_displayed()
    check.equal(detail.result, True, detail.reason)


@then("Verify that stickers option when user clicked on expand (upward arrow) beside emojis in chat forum & then selects sticker option.")
@then("Verify that by default 2 rows of stickers are showing in sticker menu with a scroll option.")
def step_impl(neo_in_class):
    neo_in_class.click_on_sticker_icon()
    detail = neo_in_class.verify_no_of_default_stickers()
    check.equal(detail.result, True, detail.reason)
    neo_in_class.close_sticker_menu()


@when("tutor types the chat")
def step_impl(test_tut):
    test_tut.send_message_in_chat(text="Hi I am tutor")


@when("student sends chat message")
def step_impl(neo_in_class):
    neo_in_class.send_chat(text="Hi I am student")


@given("another student joins the session")
@when("another student joins the session")
def step_impl(test_student_2,login_in):
    login_in.login_and_navigate_to_home_screen('+91-', '2013795859', otp=None)
    test_student_2.home_click_on_join()
    test_student_2.join_neo_session()


@when("another student sends a chat")
def step_impl(test_student_2):
    test_student_2.send_chat("Hi I am another student")


@then("verify tutor messages are left alligned")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_tutor_messages_are_left_alligned(text="Hi I am tutor")
    check.equal(detail.result, True, detail.reason)


@then("verify other student chats are left alligned")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_other_student_messages_are_left_alligned(text= "Hi I am another student")
    check.equal(detail.result, True, detail.reason)


@then("Verify that logged user messages is right aligned.")
@then("verify student chat is right alligned")
def step_impl(neo_in_class):
    neo_in_class.send_chat(text='Hi I am student')
    time.sleep(2)
    detail = neo_in_class.verify_student_messages_are_right_alligned(text="Hi I am student")
    check.equal(detail.result, True, detail.reason)


@then("Verify tutor's thumbnail in the chat forum.")
@then("Verify that tutor's name & tutor tag with time is showing in the chat forum.")
@then("verify tutor name is shown in tutor box")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_chat_elements_element_wise(element_type=  "Tutor name")
    check.equal(detail.result, True, detail.reason)
    detail = neo_in_class.verify_chat_elements_element_wise(element_type="Tutor tag")
    check.equal(detail.result, True, detail.reason)


@then("Verify when more than one students sent messages in chat box at the same time.")
def step_impl(neo_in_class,student2_neo,student2):
    neo_in_class.send_chat(text='Hi I am student')
    student2_details = get_data(Login_Credentials, 'neo_login_detail2', 'student4')
    student2.login_and_navigate_to_home_screen(student2_details['code'], student2_details['mobile_no'], otp=None)
    student2_neo.home_click_on_join()
    student2_neo.join_neo_session()
    time.sleep(2)
    student2_neo.send_chat("Hi I am another student")
    time.sleep(2)
    detail = neo_in_class.verify_student_messages_are_right_alligned(text="Hi I am student")
    check.equal(detail.result, True, detail.reason)
    detail = neo_in_class.verify_other_student_messages_are_left_alligned(text="Hi I am another student")
    check.equal(detail.result, True, detail.reason)


@then("Verify that sticker sent in chat shouldn't be distorted.")
@then("Verify stickers in chat when user selects any sticker from the list.")
def step_impl(neo_in_class):
    neo_in_class.send_sticker()
    detail = neo_in_class.verify_sticker_displayed()
    check.equal(detail.result, True, detail.reason)


@then("Verify that chat forum when multiple users sent stickers at the same time.")
def step_impl(neo_in_class,student2_neo,student2):
    neo_in_class.send_sticker()
    detail = neo_in_class.verify_sticker_displayed()
    check.equal(detail.result, True, detail.reason)
    student2_neo.send_sticker()
    detail = student2_neo.verify_sticker_displayed()
    check.equal(detail.result, True, detail.reason)


@then("Verify that raised hands option  in chat forum when logged in user raised hand.")
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, True, details.reason)




@then('Verify that "You lowered hand" message when logged in student lowers hand.')
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    neo_in_class.unraise_hand()
    detail = neo_in_class.verify_lower_hand_text_is_displayed()
    check.equal(detail.result, True, detail.reason)


@then('Verify the state of "Lower Hand" button if user leaves and then rejoins the session .')
def step_impl(neo_in_class,login_in):
    neo_in_class.unraise_hand()
    login_in.relaunch_staging()
    neo_in_class.home_click_on_join()
    neo_in_class.join_neo_session()
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, False, details.reason)


@then('Verify that if a student has raised hand and the tutor lowers the hand for that student, text Lower Hand button should again change to Raise Hand and button goes to default state')
def step_impl(neo_in_class,test_tut):
    neo_in_class.raise_hand()
    student1_details = get_data(Login_Credentials, 'neo_login_detail2', 'student3')
    test_tut.click_on_menu_option(expected_student_name=student1_details['name'], menu_item='Hands Down')
    time.sleep(1)
    details = neo_in_class.verify_hands_down_message()
    check.equal(details.result, True, details.reason)


@then('Verify that when student clicks on Lower Hand button, button should change to Raise Hand button. Also on the chat forum same should be notified as You lowered hand')
def step_impl(neo_in_class):
    neo_in_class.unraise_hand()
    time.sleep(3)
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, False, details.reason)


@then("Verify typing messages when the network is flaky.")
@then('Verify that messages should not get posted while user is typing and network goes off.')
def step_impl(neo_in_class):
    time.sleep(2)
    neo_in_class.set_wifi_connection_off()
    neo_in_class.send_chat(text='Hi I am student network test')
    time.sleep(1)
    detail = neo_in_class.verify_a_text_in_chat(text='Hi I am student network test')
    check.equal(detail.result, False, detail.reason)
    neo_in_class.set_wifi_connection_on()


@then('Verify that messages is showing in the chat when user sent & then network goes off.')
def step_impl(neo_in_class):
    neo_in_class.send_chat(text='Hi I am student network test1')
    neo_in_class.set_wifi_connection_off()
    time.sleep(1)
    detail = neo_in_class.verify_a_text_in_chat(text='Hi I am student network test1')
    check.equal(detail.result, True, detail.reason)
    neo_in_class.set_wifi_connection_on()


@then('Verify that all the messages from tutor side is left aligned.')
def step_impl(neo_in_class,test_tut):
    test_tut.send_message_in_chat(text="Hi I am tutor")
    detail = neo_in_class.verify_tutor_messages_are_left_alligned(text="Hi I am tutor")
    check.equal(detail.result, True, detail.reason)


@then("Verify that all the messages from other students side is left aligned.")
def step_impl(neo_in_class,student2_neo):
    student2_neo.send_chat("Hi I am another student")
    detail = neo_in_class.verify_other_student_messages_are_left_alligned(text= "Hi I am another student")
    check.equal(detail.result, True, detail.reason)

@then("Verify message count in Class Forum when tutor send messages")
def step_impl(neo_in_class,test_tut):
    initial_no =len(neo_in_class.get_all_chats())
    test_tut.send_message_in_chat(text="Hi I am tutor")
    time.sleep(5)
    final_no = len(neo_in_class.get_all_chats())
    flag = (final_no==initial_no+1)
    check.equal(flag, True, "Message count is not increased when tutor types a message")


@then("Verify that logged in user message shows first then tutor's reply when tutor responds to any doubts.")
@then("Verify the message count in tutor's reply  when tutor replies to students message.")
def step_impl(neo_in_class,test_tut):
    neo_in_class.send_chat("This is for reply")
    initial_no = len(neo_in_class.get_all_chats())
    test_tut.reply_to_message(reply_to_message_text = 'This is for reply', reply_message ='This is tutor reply')
    final_no =len(neo_in_class.get_all_chats())
    flag = (final_no == initial_no + 1)
    check.equal(flag, True, "Message count is not increased when tutor replies a message")



@then('Verify that "Text input is temporarily disabled for all " shows when tutor disables the chat option.')
def step_impl(neo_in_class,test_tut):
    test_tut.enable_disable_chat(flag = "disable")
    detail = neo_in_class.is_chat_disabled_message_dislayed(message = 'Live Chat is disabled')
    check.equal(detail.result, True, detail.reason)
    test_tut.enable_disable_chat(flag="enable")


@then("Verify that students cant type when message is disabled from the tutor's end.")
def step_impl(neo_in_class,test_tut):
    test_tut.enable_disable_chat(flag = "disable")
    try:
        neo_in_class.send_chat("This message wont be sent")
        flag = True
    except:
        flag = False
    detail = neo_in_class.verify_a_text_in_chat(text='This message wont be sent')
    check.equal(detail.result or flag, False, detail.reason)
    test_tut.enable_disable_chat(flag="enable")


@then("Verify the Class Forum when student throttles network to Offline")
@then("Verify that students chat is disabled and network goes off when he/she rejoin chat must be in disabled state.")
def step_impl(neo_in_class,test_tut,login_in):
    test_tut.enable_disable_chat(flag="disable")
    login_in.relaunch_staging()
    neo_in_class.home_click_on_join()
    neo_in_class.join_neo_session()
    detail = neo_in_class.is_chat_disabled_message_dislayed(message='Live Chat is disabled')
    check.equal(detail.result, True, detail.reason)
    test_tut.enable_disable_chat(flag="enable")


@then("Verify that Tutor messages should be displayed when student's network goes off & he reconnects to the session.")
def step_impl(neo_in_class):
    messages_init =  neo_in_class.get_all_chats()
    neo_in_class.set_wifi_connection_off()
    neo_in_class.set_wifi_connection_on()
    messages_finale =  neo_in_class.get_all_chats()
    check.equal(messages_finale, messages_init, "Messages are not same when student goes offline then online ")


@then("Verify that students chat is enabled and network goes off when he/she rejoin chat must be in the same state.")
def step_impl(neo_in_class, test_tut, login_in):
    test_tut.enable_disable_chat(flag="enable")
    login_in.relaunch_staging()
    neo_in_class.home_click_on_join()
    neo_in_class.join_neo_session()
    detail = neo_in_class.is_chat_disabled_message_dislayed(message='Live Chat is disabled')
    check.equal(detail.result, False , detail.reason)



