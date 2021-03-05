from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pom_pages.factory.login import LoginFactory
from pom_pages.factory.ps_3plus1screen import PS_3Plus1Screen
from pom_pages.android_pages.homepage import HomePage
from pom_pages.android_pages.ps_home_screen_android import PS_Homescreen_Android
scenarios('../features/3+1.feature')


@fixture()
def login_in(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in

@fixture
def ps_home_screen(request,driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        ps_home_screen = PS_3Plus1Screen().get_page(driver, Platform.ANDROID.value)
        yield ps_home_screen
    elif Platform.WEB.name in platform_list:
        ps_home_screen = PS_3Plus1Screen().get_page(driver, Platform.WEB.value)
        yield ps_home_screen


@given("launch the app online as 3+1 user and navigate to home screen")
def navigate_to_one_to_many_and_mega_user(driver):
    HomePage(driver).navigate_to_three_plus_one_user(driver)


@when("tap on premium school card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()
    login_in.click_on_link('See all')


@then('verify that the classroom screen consists of "For You" tab')
def verify_dashboard(login_in):
    login_in.text_match("Classes")
    login_in.text_match("For you")


@then("tap on revision session")
def tap_on_revision_session(login_in):
    login_in.click_on_link("SELECT A TOPIC")


@then(parsers.parse('verify that the session details screen consist of text "{text}"'))
@then(parsers.parse('verify text "{text}"'))
def verify_text(login_in, text):
    assert login_in.text_match(text), "text is not displayed"


@then('verify "date" is displayed with the calendar icon')
def is_calendar_with_date_present(ps_home_screen):
    assert ps_home_screen.is_calendar_with_date_present(), "Date is not displayed with the calendar icon"


@then('verify "time" is displayed with the timestamp')
def is_timestamp_with_time_present(ps_home_screen):
    assert ps_home_screen.is_timestamp_with_time_present(), "time is not displayed with the timestamp icon"


@then('verify forward icon')
def is_forward_button_present(ps_home_screen):
    assert ps_home_screen.is_forward_button_present(), "forward icon is not present"


@then('verify back icon is present')
def is_back_button_present(ps_home_screen):
    assert ps_home_screen.is_back_button_present(), "back icon is not present"


@then('verify that in "For you" tab both mandatory and optional session is displayed')
def verify_optional_mandatory_class_present(ps_home_screen):
    assert ps_home_screen.verify_optional_mandatory_class_present(), "both mandatory and optional session is not " \
                                                                     "displayed "


@then(parsers.parse('verify "{text1}" and "{text2}" tabs'))
def verify_tabs(ps_home_screen,text1, text2):
    ps_home_screen.verify_ps_tabs(text1)
    ps_home_screen.verify_ps_tabs(text2)


@then('verify date and time is displayed')
def is_date_time_present(ps_home_screen):
    ps_home_screen.is_date_time_present()


@then('verify that for mandatory session user should not be able to change the topic')
def verify_change_topic_not_present_mandatory_session(ps_home_screen):
    ps_home_screen.verify_change_topic_not_present_mandatory_session()


@then('verify the revision session consist of both fixed date, time and date-time format')
def verify_date_time_format(ps_home_screen):
    ps_home_screen.verify_date_time_format()


@then('tap on choose topic card user is navigated to choose the topic screen')
def tap_choose_topic_and_verify(login_in):
    login_in.click_on_link("Choose your topic")
    assert login_in.text_match("Choose your topic"), "user not navigated to choose the topic screen"


@then('verify choose topic screen consist of the topic list with radio button')
def verify_topic_select_button(ps_home_screen):
    assert ps_home_screen.verify_topic_select_button(), "choose topic screen does not consist of the topic list with radio button"


@then(parsers.parse('verify "{text}" button is present'))
def verify_button(login_in, text):
    login_in.is_button_displayed(text)


@then('tap on back icon user is navigated to session details screen')
def tap_back_icon_and_verify(ps_home_screen, login_in):
    ps_home_screen.tap_back_icon()
    assert login_in.text_match("Session Details"), "User is not navigated to session details screen"


@then(parsers.parse('tap on "{text}" tab'))
def tap_on_tab(ps_home_screen, text):
    ps_home_screen.tap_on_tab(text)


@then('verify revision session not booked is not displayed in a completed session tab')
def tap_choose_topic_and_verify(login_in):
    assert not login_in.text_match(
        "EXTRA SESSION"), "revision session not booked is  displayed in a completed session tab"


@then('find latest mandatory topic')
def find_latest_mandatory_topic(ps_home_screen):
    global latest_topic
    latest_topic = ps_home_screen.find_latest_mandatory_topic()


@then('verify that topic list consist of topics which are mandatory && occurred in past')
def verify_choose_topic_title(ps_home_screen):
    assert ps_home_screen.verify_choose_topic_title(latest_topic), "choose topic list doesn't consist of topics which are mandatory && occurred in past"


@then('select first topic from the list')
def select_first_topic(ps_home_screen):
    ps_home_screen.select_first_topic()


@then(parsers.parse('tap on "{text}" button'))
def verify_button(login_in, text):
    login_in.button_click(text)


@then(parsers.parse('verify in "{text1}" tab the revision topic should be displayed with tag "{text2}"'))
def verify_dashboard(login_in, ps_home_screen,text1, text2):
    ps_home_screen.verify_ps_tabs(text1)
    login_in.text_match(text2)


@then('verify user should has booked revision class')
def verify_extra_session_booked(ps_home_screen):
    assert ps_home_screen.verify_extra_session_booked(), "user does not have any booked revision class"


@then('tap on booked revision class')
def tap_on_booked_extra_session(ps_home_screen):
    ps_home_screen.tap_on_booked_extra_session()


@then('verify the selected topic summary is displayed')
def is_session_desc_present(ps_home_screen):
    assert ps_home_screen.is_session_desc_present(), "selected topic summary is not displayed"


@then('verify that within the freeze period the user is able to change the revision topic')
def change_topic_and_verify(ps_home_screen):
    ps_home_screen.change_topic_and_verify()
