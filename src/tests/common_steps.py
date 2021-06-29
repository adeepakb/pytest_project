from random import choice
from time import sleep

from pytest import fixture
from pytest_bdd import given, when, then, parsers
import pytest_check as check

from constants.platform import Platform
from pages.android.Hamburgermenu import Hamburger
from pages.android.homepage import HomePage
from pages.android.personalizedChapterList import PersonalizedChapterList
from pages.android.Journeyloadingscreen import JourneyLoadingScreen
from pages.android.Journeymapscreen import JourneyMapScreen
from pages.android.Librarychapterlistscreen import LibraryChapterListsScreen
import pytest_check as check
from pages.factory.know_more import KnowMoreTestFactory
from pages.factory.monthly_test import MonthlyTestFactory
from pages.android.Hamburgermenu import Hamburger


class Context:
    pass


@fixture
def db():
    context = Context()
    yield context


@fixture
def home(driver):
    home = HomePage(driver)
    yield home


@fixture
def personalize(driver):
    personalize = PersonalizedChapterList(driver)
    yield personalize


@fixture
def journey_map(driver):
    journey_map = JourneyMapScreen(driver)
    yield journey_map


@fixture
def journey_loading(driver):
    journey_loading = JourneyLoadingScreen(driver)
    yield journey_loading


@fixture
def know_more(request, driver):
    platform_list = request.config.getoption("platform")
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        know_more = KnowMoreTestFactory().get_page(driver, Platform.ANDROID.value)
        yield know_more
    else:
        raise NotImplementedError()


@fixture
def library(driver):
    library = LibraryChapterListsScreen(driver)
    yield library


@given('Launch the app online')
def launch_app(home):
    home.navigate_to_home_screen()


@given('User is in Personalized Chapter list screen')
def personalized_chapter_screen(home):
    home.select_subject_mathematics()


@given('User is in Personalized chapter list screen')
def personalized_chapter_screen(home, personalize):
    home.select_subject_mathematics()
    personalize.verify_personalised_chapter_list_screen()
    personalize.go_up_with_respect_to_highlight_journey()


@when('User is in personalized chapter list screen.')
def personalised_chapter_3_line(home, personalize):
    home.select_subject_mathematics()
    personalize.verify_personalised_chapter_list_screen()


@when('User is in personalized chapter list screen')
def personalised_list(home, personalize):
    home.select_subject_mathematics()
    personalize.verify_personalised_chapter_list_screen()
    personalize.go_up_with_respect_to_highlight_journey()


@when('User is in Personalized chapter list screen')
def personalized_chapter_screen_two(home):
    home.select_subject_mathematics()


# ==============================================================================================================
#                                             BYJU'S Classes Common Steps
# ==============================================================================================================

@fixture
def login(driver, request):
    platform_list = request.config.getoption("platform")
    from pages.factory.application_login_factory import Login
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        login_in = Login().get_page(driver, Platform.ANDROID.value)
        yield login_in
    else:
        raise NotImplementedError()


@fixture
def std_board(driver, request):
    platform_list = request.config.getoption("platform")
    from pages.factory.student_dashboard_otm_factory import StudentDashboardOneToMegaFactory
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        std_board = StudentDashboardOneToMegaFactory().get_page(driver, Platform.ANDROID.value)
        yield std_board
    else:
        raise NotImplementedError()


@fixture
def ssn_req(driver, request):
    platform_list = request.config.getoption("platform")
    from pages.factory.session_requisite_factory import SessionRequisiteFactory
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        ssn_req = SessionRequisiteFactory().get_page(driver, Platform.ANDROID.value)
        yield ssn_req
    else:
        raise NotImplementedError()


@fixture
def m_class(driver, request):
    platform_list = request.config.getoption("platform")
    from pages.factory.masterclass_factory import MasterClassFactory
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        m_class = MasterClassFactory().get_page(driver, Platform.ANDROID.value)
        yield m_class
    else:
        raise NotImplementedError()


@given('launch the app and navigate to home screen')
def launch_and_nav_to_home(login):
    if login.toggle_wifi_connection('on'):
        login.driver.close_app()
        login.driver.activate_app(login.driver.capabilities['appPackage'])
    login.implicit_wait_for(15)
    #login.verify_home_screen()
    login.implicit_wait_for(15)


@given('navigate to one to mega home screen')
@when('navigate to one to mega home screen')
@then('navigate to one to mega home screen')
@given("navigate to byju's classes home screen")
def nav_to_mega_home(login):
    login.click_on_premium_school()


@then(parsers.re(
    'attach (?P<req_type>(?:in|pre|post|all '
    '(?:pre|post|pre and post|pre and in|in and post)|two '
    '(?:pre|post|in))) requisites (?P<req_content>'
    '(?:k12_video |assessment |journey |practice |k3_video |video |))for '
    '(?P<this_day>(?:tomorrow|today|yesterday|completed|up next)) session'
))
@when(parsers.re(
    'attach (?P<req_type>(?:in|pre|post|all '
    '(?:pre|post|pre and post|pre and in|in and post)|two '
    '(?:pre|post|in))) requisites (?P<req_content>'
    '(?:k12_video |assessment |journey |practice |k3_video |video |))for '
    '(?P<this_day>(?:tomorrow|today|yesterday|completed|up next)) session'
))
@given(parsers.re(
    'attach (?P<req_type>(?:in|pre|post|all '
    '(?:pre|post|pre and post|pre and in|in and post)|two '
    '(?:pre|post|in))) requisites (?P<req_content>'
    '(?:k12_video |assessment |journey |practice |k3_video |video |))for '
    '(?P<this_day>(?:tomorrow|today|yesterday|completed|up next)) session'
))
def step_impl(db, tllms, req_type, req_content, this_day):
    req = req_type.split()
    if 'and' in req:
        req.remove('and')
        req_type = '_'.join(req)
    elif len(req) == 2:
        req_content, req_type = req
    try:
        user_profile = db.user_profile
    except AttributeError:
        user_profile = 'user_1'
    try:
        topic_name = db.topic_name
    except AttributeError:
        topic_name = None
    tllms.attach_requisite_group(
        grade="8", req_type=req_type, asset_type=req_content.strip(),
        days=this_day, profile='login_details_3', user_profile=user_profile,
        sub_profile='profile_1')


@when('verify completed session cards should be displayed')
def verify_completed_session(std_board):
    details = std_board.is_completed_sessions_displayed()
    check.equal(details.result, True.details.reason)


@then('verify completed session cards should be displayed')
def then_verify_completed_session(std_board):
    details = std_board.is_completed_sessions_displayed()
    check.equal(details.result, True.details.reason)


@when(parsers.re('switch (?P<state>(?:off|on)) the device wifi'))
def device_wifi_state(std_board, state):
    std_board.toggle_wifi_connection(state)


@then(parsers.re('switch (?P<state>(?:off|on)) the device wifi'))
def device_wifi_state(std_board, state):
    std_board.toggle_wifi_connection(state)


@then('verify up next session is displayed')
@when('verify up next session is displayed')
def step_impl(std_board):
    details = std_board.is_up_next_displayed()
    check.equal(details.result, True, details.reason)


@then('scroll up next to the top')
def step_impl(std_board):
    std_board.scroll_up_next_top()


@when('tap on app back button')
def tap_on_app_back(std_board):
    std_board.click_app_back_btn()


@then('tap on app back button')
def tap_on_app_back(std_board):
    std_board.click_app_back_btn()


@when('tap on device back button')
def step_impl(std_board):
    std_board.click_back()


@then('tap on device back button')
def step_impl(std_board):
    std_board.click_back()


@when('tap on device back or app back button')
@then('tap on device back or app back button')
def step_impl(std_board):
    choice((std_board.click_back, std_board.click_app_back_btn))()


@then('verify user is navigated one to mega home screen')
@then('verify user landed on student dashboard screen')
def verify_one_to_mega_home_screen(std_board):
    assert std_board.is_one_to_mega_screen_displayed()


@then('verify that for up coming session pre requisite are displayed')
def step_impl(std_board):
    pre_req, post_req = True, False
    displayed = std_board.is_pre_post_requisite_displayed(pre=pre_req, post=post_req, session='upcoming')
    check.equal(displayed.result, True, displayed.reason)
    flag1 = pre_req is displayed.result
    flag2 = post_req is not displayed.result
    check.equal(flag1, True, "Pre resuisite is not displayed")
    check.equal(flag2, True, "Post requisites is displayed")


@when(parsers.re('verify text "(?P<text>(.*))".*'))
def verify_text(std_board, text):
    text_displayed = std_board.verify_is_text_displayed(text)
    check.equal(text_displayed, True, text_displayed + f' The text "{text}" is not displayed.')


@then(parsers.re('verify text "(?P<text>(.*))".*'))
def verify_text(std_board, text):
    text_displayed = std_board.verify_is_text_displayed(text)
    check.equal(text_displayed, True, text_displayed + f' The text "{text}" is not displayed.')


@when(parsers.re('tap on (?:any |)(?P<t>(?:future|completed|tomorrow|up next)) session card'))
def tap_on_upcoming_card(std_board, t):
    std_board.click_on_card(t)


@then(parsers.re('tap on (?:any |)(?P<t>(?:future|completed|tomorrow|up next)) session card'))
def tap_on_upcoming_card(std_board, t):
    std_board.click_on_card(t)


@then(parsers.re('verify (?P<s_t>(?:subject|topic)) (?P<n_i>(?:name|icon)).*'))
def verify_content_desc(ssn_req, std_board, s_t, n_i):
    std_board.login.implicit_wait_for(0)
    check.equal(ssn_req.verify_content_description(s_t, n_i), True, "Content Description is wrong")
    std_board.login.implicit_wait_for(15)


@then(parsers.re('verify (?P<c_t>(?:calendar|clock)).*'))
def verify_content_desc(ssn_req, std_board, c_t):
    std_board.login.implicit_wait_for(0)
    check.equal(ssn_req.verify_content_description(c_t), True, "Calender time not verified")
    std_board.login.implicit_wait_for(15)


@when(parsers.re('verify (?P<tp_tm>(?:topic|time|date)) (?P<cnt_typ>(?:(description|details))).*'))
@then(parsers.re('verify (?P<tp_tm>(?:topic|time|date)) (?P<cnt_typ>(?:(description|details))).*'))
def verify_content_desc(std_board, tp_tm, cnt_typ):
    std_board.login.implicit_wait_for(0)
    check.equal(ssn_req.verify_content_description(tp_tm, cnt_typ), True, "Time is worng")
    std_board.login.implicit_wait_for(15)


@then(parsers.re('verify (?P<tp_tm>(?:topic|time|date)) (?P<cnt_typ>(?:(description|details))).*'))
def verify_content_desc(ssn_req, std_board, tp_tm, cnt_typ):
    std_board.login.implicit_wait_for(15)
    check.equal(ssn_req.verify_content_description(tp_tm, cnt_typ), True,
                " {} {} are not verified".format(tp_tm, cnt_typ))
    std_board.login.implicit_wait_for(15)


@when(parsers.re('verify (?P<b_type>(?i:get help|app back|retry|rate now)) button.*'))
def verify_button_displayed(std_board, b_type):
    std_board.login.implicit_wait_for(0)
    check.equal(std_board.is_button_displayed(b_type), True, "{} button is not being displayed".format(b_type))
    std_board.login.implicit_wait_for(15)


@then(parsers.re('verify (?P<b_type>(?i:get help|app back|retry|rate now)) button.*'))
def verify_button_displayed(std_board, b_type):
    std_board.login.implicit_wait_for(0)
    check.equal(std_board.is_button_displayed(b_type), True, "{} button is not bring diplayed".format(b_type))
    std_board.login.implicit_wait_for(15)


@when('tap on completed tab')
def tap_on_completed_tab(std_board):
    check.equal(std_board.ps_home_page_tab('Completed'), True, "Could not click on completed tab")


@when('verify user navigated to home screen')
@then('verify user navigated to home screen')
def step_impl(login):
    home_activity = "HomeActivity"
    login.wait_activity(home_activity)
    current_activity = login.driver.current_activity.split(".")[-1]
    check.equal(home_activity, current_activity, "home scree might not be loaded.")


@then('verify tick icon')
def verify_completed_check_mark(std_board):
    details = std_board.is_completed_check_displayed()
    check.equal(details.result, True, details.reason)


@when('verify user is navigated to session details screen')
def verify_session_details_screen(std_board):
    details = std_board.is_screen_displayed("Session Details")
    check.equal(details.result, True, details.reason)


@then('verify user is navigated to session details screen')
def then_verify_session_details_screen(std_board):
    details = std_board.is_screen_displayed("Session Details")
    check.equal(details.result, True, details.reason)


@when(parsers.re('verify (?P<tab_name>(?i:for you|completed))(?: sessions|) tab is highlighted'))
def verify_completed_session_tab_highlighted(std_board, tab_name):
    tab_name = tab_name.capitalize()
    check.equal(std_board.ps_home_page_tab(tab_name, check=True), True, "{} tab is not highlighted".format(tab_name))


@then(parsers.re('verify (?P<tab_name>(?i:for you|completed))(?: sessions|) tab is highlighted'))
def verify_completed_session_tab_highlighted(std_board, tab_name):
    tab_name = tab_name.capitalize()
    check.equal(std_board.ps_home_page_tab(tab_name, check=True), True, "{} tab is not highlighted".format(tab_name))


@then('verify the toggle sessions for you and completed sessions')
def step_impl(std_board):
    std_board.ps_home_page_tab("Completed")
    check.equal(std_board.ps_home_page_tab("Completed", check=True), True, "Completed tab is not highlighted")
    std_board.ps_home_page_tab("For you")
    check.equal(std_board.ps_home_page_tab("For you", check=True), True, "For you tab is not highlighted")


@then('verify that for completed session both pre and post requisites are displayed')
def step_impl(std_board):
    pre_req, post_req = True, True
    displayed = std_board.is_pre_post_requisite_displayed(pre_req, post_req)
    assert pre_req is displayed and post_req is displayed


@then('verify that for completed session post requisite is displayed')
def step_impl(std_board):
    pre_req, post_req = False, True
    displayed = std_board.is_pre_post_requisite_displayed(pre_req, post_req)
    check.equal(displayed, True, displayed.reason)
    flag1 = pre_req is not displayed
    check.equal(flag1, True, displayed.reason + " Pre requisite is displayed")
    flag2 = post_req is displayed
    check.equal(flag2, True, displayed.reason + " Post requisite is  not  displayed")


@then('verify that for up next session pre requisites are displayed')
def step_impl(std_board):
    pre_req, post_req = True, False
    displayed = std_board.is_pre_post_requisite_displayed(pre_req, post_req, session='upcoming')
    check.equal(displayed, True, displayed.reason)
    flag1 = pre_req is displayed
    check.equal(flag1, True, displayed.reason + " Pre requisite is not displayed")
    flag2 = post_req is not displayed
    check.equal(flag2, True, displayed.reason + " Post requisite is displayed")


@then('verify if more then two requisites are attached "see more" option is displayed')
def step_impl(ssn_req):
    details = ssn_req.is_see_more_option_displayed()
    check.equal(details.result, True, details.reason)


@then('verify "see more" option is not displayed if the post requisite contain only two resource type')
def step_impl(ssn_req):
    details = ssn_req.is_see_more_option_displayed()
    check.equal(details.result, False, details.reason)


@when('verify post requisite is attached for completed session')
def step_impl(std_board):
    details = std_board.is_post_requisite_attached()
    check.equal(details.result, True, details.reason)


@then('verify post requisite is attached for completed session')
def step_impl(std_board):
    details = std_board.is_post_requisite_attached()
    check.equal(details.result, True, details.reason)


@then('on tap of see more option')
def step_impl(std_board):
    std_board.click_on_see_more()


@then('verify a video card should be shown in the session detail screen')
def step_impl(ssn_req):
    ssn_req.verify_requisite_details(dtls='video')


@then('verify user is landed on premium school screen')
def verify_user_on_ps_screen(std_board):
    assert std_board.is_screen_displayed("Classes")


@then('tap on the video')
def step_impl(std_board):
    std_board.tap_on_req_grp('video')


@then('verify the video is playing')
def step_impl(ssn_req):
    check.equal(ssn_req.verify_video_playing(), True, "Videos is not playing")


@then('verify user is able to complete the video')
def step_impl(ssn_req):
    details = ssn_req.complete_video()
    check.equal(details.result, True, details.reason)


@then('verify all video player elements')
def step_impl(ssn_req):
    check.equal(ssn_req.verify_video_player_elements(), True, "All videos player elements are not displayed")


@given('last session should be ended and should not be rated')
def step_impl(login, std_board, db):
    login.toggle_wifi_connection('on')
    # login.verify_home_screen()
    login.implicit_wait_for(15)
    db.user_profile = 'user_1'
    check.equal(std_board.complete_last_session(rate_action='skip', db=db), True,
                "Last session was not ended and rating was not done")


@given('last session should be ended and should not be rated and verify feedback screen')
def step_impl(login, std_board, db):
    login.verify_home_screen()
    check.equal(std_board.complete_last_session(rate_action='skip', rate_activity_check=True, db=db), True,
                "Last session was not ended or rated successfully")


@given('last session should be ended and should be rated')
def step_impl(db, std_board):
    db.user_profile = 'user_2'
    check.equal(std_board.complete_last_session(rate_action='rate', db=db),
                "Last session was not ended and rated successfully")


@then('verify that user is able to access all post requisites attached to the session')
def step_impl(std_board):
    check.equal(std_board.is_all_post_requisite_accessible(), True,
                "User is not able to access all post requisites attatched to the session")
# ------------------------------------------------------------------------
    assert std_board.is_all_post_requisite_accessible()


@when('Tap on hamburger menu')
@when('Tap on the Hamburger menu at the left corner on the home screen')
def step_impl(know_more):
    detail = know_more.click_on_hamburger()
    check.equal(detail.result, True, detail.reason)


@when('verify that the Left nav is displayed')
def ham_verify(driver):
    Hamburg = Hamburger(driver)
    Hamburg.hamburger_verify(driver, click=False)


@then('Verify that in the left nav "Byjus classes-Know more" option is present')
def step_impl(driver, know_more):
    detail = know_more.verify_know_more_displayed()
    check.equal(detail.result, True, detail.reason)


@then('Verify that in the left nav "Byjus classes-Know more" option is not present')
def step_impl(driver, know_more):
    detail = know_more.verify_know_more_displayed()
    check.equal(detail.result, False, detail.reason)


@when('Tap on the "Byjus classes" option on the left nav')
@when('tap on "Byjus classes" option on the left nav')
@then('tap on the "Byjus classes-Know more" option in the left nav')
@then('Tap on the "Byjus classes" option on the left nav')
@when('Tap on the "Byjus classes" option on the left nav')
def step_impl(driver, know_more):
    detail = know_more.tap_on_byjus_classes_in_hamburger()
    check.equal(detail.result, True, detail.reason)


@then('verify  "Byjus classes-Know more" option is responsive')
def step_impl(driver, know_more):
    detail = know_more.validate_know_more()
    check.equal(detail.result, True, detail.reason)


@given('switch to offline')
@then('switch to offline')
@when('switch to offline')
def step_impl(driver, know_more):
    detail = know_more.select_online_offline_mode("offline")
    check.equal(detail.result, True, detail.reason)


@given('switch to online')
@when('switch to online')
@then('switch to online')
def step_impl(driver, know_more):
    detail = know_more.select_online_offline_mode("ALL_NETWORK_ON")
    check.equal(detail.result, True, detail.reason)


@then('verify that user is navigated to "Book a free class" screen')
@then('verify that the user is navigated to the "Book a free class" screen')
def step_impl(driver, know_more):
    detail = know_more.verify_book_free_class_screen()
    check.equal(detail.result, True, detail.reason)


@given("login as user with free account")
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_3').switch_profile()


@given("login with non booked user")
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


@when('tap on "Book" button')
@then('tap on "Book" button')
def step_impl(know_more, m_class):
    detail = know_more.tap_on_book_button()
    check.equal(detail.result, True, detail.reason)
    detail = m_class.verify_booking_screen()
    check.equal(detail.result, True, detail.reason)


@then('verify user is able to book a session')
def step_impl(know_more, m_class, db):
    detail = know_more.book_a_session(db=db)
    check.equal(detail.result, True, detail.reason)
    detail = know_more.verify_and_close_booked_screen(db=db)
    check.equal(detail.result, True, detail.reason)
    print()


@given('relaunch the app')
@then('relaunch the app')
def step_impl(know_more, m_class, db):
    detail = know_more.relaunch_app()
    check.equal(detail.result, True, detail.reason)
