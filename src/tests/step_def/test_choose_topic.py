from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers
from src.POM_Pages.application_login import Login
from src.POM_Pages.session_popup import SessionAlert
from src.POM_Pages.student_dashboard import StudentDashboard
from src.POM_Pages.choose_topic import ChooseTopic

feature_file_name = 'choose_topic'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def choose_topic(browser):
    chs_tpic = ChooseTopic(browser)
    yield chs_tpic


@fixture
def std_board(browser):
    stud_b = StudentDashboard(browser)
    yield stud_b


@fixture
def login_in(browser):
    login_in = Login(browser)
    yield login_in


@fixture
def context_db():
    yield dict()


@given('Launch the tutor app online')
def launch_app(login_in):
    login_in.implicit_wait_for(15)


@given('navigate to one to many student dashboard screen')
def given_navigate_dashboard_screen(login_in, browser):
    try:
        login_in.click_on_premium_school()
        pop_up_displayed = SessionAlert(browser)
        pop_up_displayed.cancel_join_session()
    except AssertionError:
        login_in.click_on_one_to_many()


@when('navigate to one to many student dashboard screen')
def navigate_dashboard_screen(login_in, choose_topic, browser):
    try:
        choose_topic.click_on_premium_school()
        pop_up_displayed = SessionAlert(browser)
        pop_up_displayed.cancel_join_session()
    except AssertionError:
        login_in.click_on_one_to_many()


@when("tap on any future scheduled session card")
def tap_on_future_card(std_board):
    std_board.click_on_future_card()


@then('verify topic description')
def verify_topic_desc_details(std_board):
    topic_desc_displayed = std_board.is_topic_desc_displayed()
    assert topic_desc_displayed, "Topic description not displayed."


@then('verify SESSION DETAILS card is displayed')
def verify_session_details_displayed(std_board):
    session_dtls_card_displayed = std_board.is_session_details_card_displayed()
    assert session_dtls_card_displayed is True, "Details card is not displayed."


@then("verify session details card is loaded")
def then_verify_session_details_card(std_board):
    verify_session_details_displayed(std_board)


@then(parsers.parse('verify text "{text}" should be displayed'))
def verify_session_details_text(std_board, text):
    text_displayed = std_board.is_session_details_text_displayed()
    assert text_displayed is True, "'SESSION DETAILS' text is not displayed."


@then('verify subject name is displayed')
def verify_session_dtls_subj_name(std_board):
    subj_displayed = std_board.is_subject_name_displayed()
    assert subj_displayed is True, "The subject name is not displayed."


@then("verify subject name should be displayed")
def then_verify_subject_name_displayed(std_board):
    verify_session_dtls_subj_name(std_board)


@then('verify topic name is displayed')
def verify_session_dtls_topic_name(std_board):
    topic_name = std_board.is_topic_name_displayed()
    assert topic_name is True, "The topic name is not displayed"


@then("verify topic name should be displayed")
def then_verify_topic_name(std_board):
    verify_session_dtls_topic_name(std_board)


@then('verify calender icon followed by date format DD MMM,Day is displayed')
def verify_calendar_icon_and_details(std_board):
    calendar_details = std_board.is_calendar_details_displayed()
    assert calendar_details is True, "Calendar details is not displayed correctly."


@then("verify date,month,day details should be displayed")
def then_verify_calender_details(std_board):
    verify_calendar_icon_and_details(std_board)


@then('verify time icon followed by HH:MM AM/PM details are displayed')
def verify_time_icon_and_details(std_board):
    time_details = std_board.is_time_details_displayed()
    assert time_details is True, "Time details is not displayed correctly."


@then("verify time details should be displayed")
def then_verify_time_details(std_board):
    verify_time_icon_and_details(std_board)


@then("verify topic description details should be displayed")
def then_verify_topic_desc(std_board):
    verify_topic_desc_details(std_board)


@then("verify choose a topic to learn card should be displayed")
def verify_choose_topic_card_title(std_board):
    title_displayed = std_board.is_choose_topic_card_title_displayed()
    assert title_displayed is True, "'Choose a topic to learn' text is not displayed."


@then('verify text Learn what you want text should be displayed in choose a topic to learn card')
def verify_text_of_choose_topic_card_displayed(std_board):
    sub_txt = std_board.is_subtext_of_choose_topic_displayed()
    assert sub_txt is True, "'Learn what you want' sub text is not displayed."


@then('verify Change topic card is displayed if session starts in post 2 days')
def verify_card_detail_change_topic(std_board):
    change_topic_card_displayed = std_board.is_choose_topic_displayed()
    assert change_topic_card_displayed, "OPPS! 'Choose Topic' card not displayed."


@when('switch off the device data')
def switch_connectivity_off(std_board):
    while True:
        msg = std_board.is_one_to_many_screen_displayed()
        if msg:
            break
    std_board.toggle_wifi_connection('off')


@then("verify Choose Topic button is displayed")
def verify_choose_topic_button_displayed(std_board):
    verify_card_detail_change_topic(std_board)


@then('verify text you can choose a topic till 4 days prior to the session below the choose a topic to learn card')
def verify_message_of_session_details(std_board):
    message_txt = std_board.is_message_of_session_details_displayed()
    assert message_txt is True, "Message of SESSION DETAILS is not displayed."


@when("tap on choose topic button")
@then('tap on choose topic button')
def tap_on_choose_topic(std_board):
    std_board.tap_on_choose_topic()


@then("verify change topic section is displayed")
def verify_change_topic_section(std_board):
    msg_status = std_board.is_change_topic_section_displayed()
    assert msg_status is True, "'CHANGE TOPIC' section is displayed."


@when('verify by default "UP NEXT" session card should be selected')
@then('verify by default "UP NEXT" session card should be selected')
def verify_up_next_selected(std_board):
    card_selected = std_board.is_up_next_card_selected()
    assert card_selected is True, "UP NEXT label may not be displayed or chapter name does not match"


@then("verify topics are displayed under change topic section")
def verify_change_topic_section(std_board):
    section_displayed = std_board.is_topics_displayed_under_change_topic()
    assert section_displayed is True, "Change Topic Section is not displayed."


@then('verify "Done" button is displayed')
def verify_done_button_displayed(std_board):
    button_displayed = std_board.is_done_button_displayed()
    assert button_displayed is True, "'Done' button not displayed."


@then("verify close button is displayed")
def verify_close_button_displayed(std_board):
    close_button_displayed = std_board.is_close_button_displayed()
    assert close_button_displayed is True, "Close button is not displayed."


@then("tap on any topic which is displayed under change topic section")
def tap_on_any_topic(std_board):
    std_board.tap_on_any_change_topic()


@then("verify selected topic button is highlighted")
def verify_button_topic_highlighted(std_board):
    button_selected = std_board.is_radio_button_selected()
    assert button_selected, "Button is may not be selected."


@then('verify Retry button should be displayed')
def verify_retry_button(login_in):
    button_displayed = login_in.is_button_displayed("Retry")
    assert button_displayed is True, f"Button Retry is not displayed"


@then('switch on the device data')
def switch_connectivity_on(std_board):
    std_board.toggle_wifi_connection('on')


@then('tap on Retry button')
def tap_on_retry(std_board):
    std_board.tap_button_retry()


@then('verify respective session details are loaded')
def verify_session_details_card_all(std_board):
    details_match = std_board.verify_session_details()
    assert details_match is True, "Details dosen't not match."


@when('tap on any session card')
@then('tap on any session card')
def tap_on_random_card(std_board):
    std_board.random_card().click()


@then("tap on Done button")
def tap_on_done_button(std_board):
    std_board.tap_done_button()


@then("tap on close button")
def tap_on_close_button(std_board):
    std_board.tap_on_close_button()


@then("verify user is on session details card")
def verify_user_on_session_details(std_board):
    details_displayed = std_board.is_session_details_card_displayed()
    assert details_displayed is True, "Session details card not displayed."


@then(parsers.parse('verify text "{text}" with icon'))
def verify_wifi_validation_text(std_board, text):
    error_msg_displayed = std_board.is_wifi_relevant_msg_displayed(text)
    error_image_displayed = std_board.is_session_details_error_image_displayed()
    assert error_msg_displayed and error_image_displayed is True, "Either image or appropriate message is not displayed"


@then(parsers.parse('verify text "{text}".'))
def verify_text_check_connection(std_board, text):
    check_conn_text_displyd = std_board.is_text_check_connection_displayed(text)
    assert check_conn_text_displyd is True, f"The text '{text}' is not displayed or content might be changed."


@then("verify session details card is loaded with all the required elements")
def verify_details_card_loaded(std_board):
    std_board.is_all_details_displayed_match()


@when("Verify by default up next session card get highlighted.")
def verify_default_up_next_selected(std_board):
    card_selected = std_board.is_up_next_card_selected()
    assert card_selected is True, "UP NEXT card is not selected."


@then("verify if next session is scheduled with in 2 days, then session starts cards shown with days remaining count")
def verify_session_starts_card(std_board):
    typ_val = std_board.is_date_count_displayed()
    assert typ_val is True or typ_val is None, "Could not find the count down timer."


@then('verify if next session is scheduled post 2 days, then "Choose topic" card should be shown.')
def verify_choose_topic_card(std_board):
    date_counter_displayed = std_board.is_choose_topic_displayed()
    assert date_counter_displayed is True, "Date Counter may not be displayed."


@then("Verify if next session starts with in 1 day then session countdown timer will be shown.")
def verify_count_down_timer(std_board):
    timer_displayed = std_board.is_timer_displayed()
    assert timer_displayed is True, "Timer may not be displayed."


@then('verify if next session countdown timer reaches the session start time, then "JOIN NOW" button should be shown')
def verify_join_now_button(std_board):
    button_displayed = std_board.is_join_now_button_displayed()
    assert button_displayed is True, "'Join Now' button not displayed."


@then("verify respective session details card should be loaded")
def step_impl(std_board):
    details_match = std_board.is_respective_card_displayed()
    assert details_match is True, "Details does not match."


@then("Verify if next session is in prior to 2 days the session starts card should be shown")
def step_impl(std_board):
    text_displayed = std_board.is_your_session_starts_text_displayed()
    assert text_displayed is True, "'Your session starts in' text not displayed"


@then(
    'verify  text "You can choose a topic till 2 days prior to the session" should not be shown under session starts '
    'card.')
def step_impl(std_board):
    text_not_displayed = std_board.is_you_can_choose_topic_text_not_displayed()
    assert text_not_displayed is True, "Text 'You can choose topic' is displayed."


@when('Verify by default next session card should be highlighted.')
def verify_up_next_selected(choose_topic):
    up_next_check = choose_topic.is_up_next_card_selected()
    assert up_next_check is True, "'UP NEXT' card may not be displayed or not selected."


@then('Verify "Up Next" badge should be present on the next session card.')
def is_up_next_badge_selected(choose_topic):
    up_next_label_check = choose_topic.is_up_next_badge_displayed()
    assert up_next_label_check is True, "'UP NEXT' card may not be displayed"


@given('Select a session card which is post 2 days from current date.')
def given_select_session_post_two_days(choose_topic):
    choose_topic.click_on_card_day()


@when('Select a session card which is post 2 days from current date.')
def select_session_post_two_days(choose_topic):
    choose_topic.click_on_card_day()


@given('Session details card with <Choose Topics> card loads.')
def given_verify_choose_topic_card_loaded(choose_topic):
    topic_displayed = choose_topic.is_choose_topic_card_displayed()
    assert topic_displayed is True, "OOPS!, 'Choose Topic' card might not be displayed."


@when('Session details card with <Choose Topics> card loads.')
def verify_choose_topic_card_loaded(choose_topic):
    topic_displayed = choose_topic.is_choose_topic_card_displayed()
    assert topic_displayed is True, "OOPS!, 'Choose Topic' card might not be displayed."


@given('Tap on <Choose topic> button.')
def given_click_on_choose_topic(choose_topic):
    choose_topic.click_on_choose_topic()


@when('Tap on <Choose topic> button.')
def click_on_choose_topic(choose_topic):
    choose_topic.click_on_choose_topic()


@when('<Change Topic> card will load with list of topics.')
def verify_choose_topic_list(choose_topic):
    topic_list_displayed = choose_topic.is_choose_topic_list_displayed()
    assert topic_list_displayed is True, "choose topic list might not be displayed."


@then('Verify user should be able to scroll the <Choose Topic> list on both upwards and downwards.')
def verify_list_scrollable(choose_topic):
    topic_changed = choose_topic.is_list_scrollable()
    assert topic_changed is True, "topic card list might not be scrollabel."


@when('Select the other topic from choose topics card.')
def select_random_topic_list(choose_topic, context):
    random_topic = choose_topic.click_on_random_topic()
    context['topic'] = random_topic


@when('Tap on <DONE> button')
def click_done_button(choose_topic):
    choose_topic.click_on_done_button()


@given('verify CHANGE TOPIC card is displayed')
def given_verify_change_topic_card_displayed(choose_topic):
    change_topic_displayed = choose_topic.is_change_topic_card_displayed()
    assert change_topic_displayed is True, "'Change Topic' is not displayed or content might be changed."


@when('verify CHANGE TOPIC card is displayed')
def verify_change_topic_card_displayed(choose_topic):
    change_topic_displayed = choose_topic.is_change_topic_card_displayed()
    assert change_topic_displayed is True, "'Change Topic' is not displayed or content might be changed."


@given('verify list of topics are shown with radio button')
def given_verify_list_and_radio_buttons_displayed(choose_topic):
    details_displayed = choose_topic.is_radio_buttons_and_topic_list_displayed()
    assert details_displayed is True, "Could not find the elements, either radio buttons or topic list not displayed. "


@when('verify list of topics are shown with radio button')
def verify_list_and_radio_buttons_displayed(choose_topic):
    details_displayed = choose_topic.is_radio_buttons_and_topic_list_displayed()
    assert details_displayed is True, "Could not find the elements, either radio buttons or topic list not displayed. "


@then('Verify that user should be able to select only one topic from the topics list.')
def verify_only_card_selected(choose_topic):
    only_one_topic_selected = choose_topic.is_only_one_topic_selected()
    assert only_one_topic_selected is True, "May be more than on topic selected."


@then('Verify for selected topic, list of sub topics associated should be shown.')
def verify_sub_topic_list_displayed(choose_topic):
    raise NotImplementedError


@when('tap on radio button')
def tap_on_radio_button(choose_topic, context_db):
    assoc_topic_txt = choose_topic.click_on_random_topic_radio_button()
    context_db['selected_topic'] = assoc_topic_txt


@when('verify user is able to select the particular topic on taping on radio button.')
def verify_associated_topic_selected(choose_topic, context_db):
    topic_selected = choose_topic.is_particular_topic_selected(context_db['selected_topic'])
    assert topic_selected is True, "Particular topic not selected"


@when('verify subtopics are displayed for the selected topic')
def verify_particular_sub_topic_displayed(choose_topic, context_db):
    sub_topic_displayed = choose_topic.is_subtopics_displayed(context_db['selected_topic'])
    assert sub_topic_displayed is True, "Sub topic is not displayed for the selected topic"


@when('select another topic by tapping on radio button')
def tap_on_another_topic(choose_topic, context_db):
    assoc_topic_txt = choose_topic.click_on_random_topic_radio_button()
    context_db['selected_topic'] = assoc_topic_txt


@when('verify only one topic should be selected at a time with associated subtopics')
def verify_only_one_topic_selected(choose_topic, context_db):
    topic_selected_once = choose_topic.is_only_one_topic_selected()
    sub_topic_displayed = choose_topic.is_subtopics_displayed(context_db['selected_topic'])
    assert all((topic_selected_once, sub_topic_displayed)) is True, "more than on topic selected or" \
                                                                    "associated subtopic might notbe displayed."


@then("Verify that selected topic should be updated in both 'SESSION DETAILS' and 'SCHEDULED SESSION' card")
def verify_topic_changed(choose_topic, context_db):
    details_match = choose_topic.is_topic_changed(context_db['selected_topic'])
    assert details_match is True, "OPPS!, details after changing the topic does not match."


@then('Verify that choose topic card color should be displayed based on subject.')
def verify_subject_choose_topic_color_match(choose_topic):
    choose_topic.verify_color_two()
