from pytest_bdd import scenarios, given, when, then

from pages.android.homepage import HomePage
from utilities.base_page import BaseClass
from pages.android.Journeyloadingscreen import JourneyLoadingScreen

driver = fixture = 'driver'
baseClass = BaseClass()
home = HomePage(driver)
journey_start=JourneyLoadingScreen(driver)
"""storing the feature file name"""
featureFileName = "Journey loading screen"

# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')

# scenario 1
@given('Launch the app online')
def launch_app(driver):
    # journey_start.switch_to_wifi(driver)
    # code = getdata(Login_Credentials,'login_details2', 'code')
    # countrycode = getdata(Login_Credentials,'login_details2', 'country_code')
    # mobno = getdata(Login_Credentials,'login_details2', 'mobile_no')
    # otp = getdata(Login_Credentials,'login_details2','OTP')
    home.navigate_to_home_screen(driver)
    pass

@when('User is in journey loading Screen')
def personalized_chapter_screen(driver):
    home.select_subject_mathematics(driver)
#     journey_start.switch_to_twoG(driver)
    journey_start.verify_personaised_screen(driver)
    journey_start.click_on_journey_card(driver)


@then('Verify "Back arrow" on top left corner of the screen')
def back_arrow(driver):
    journey_start.verify_back_arrow(driver)


@then('Verify <Chapter name>')
def chapter_name(driver):
    journey_start.verify_chapter_name(driver)


@then('Verify image')
def image(driver):
    pass


@then('Verify "Hi <Username>! Analysing your learning profile to find the best path for you" text')
def msg(driver):
    journey_start.verify_msg(driver)


# scenario 2
@given('user is in journey loading screen')
def personalized_chapter_screen1(driver):
    home.select_subject_mathematics(driver)
#     journey_start.switch_to_twoG(driver)
    journey_start.click_on_journey_card(driver)
    journey_start.click_on_device_back_Btn(driver)


@when('User taps on back button')
def click_on_back(driver):
    # journey_loading.click_on_device_back_Btn(driver)
    pass


@then('Verify that user should be redirected to <PersonalisedChapterListScreen>')
def personalised_screen(driver):
    journey_start.verify_personaised_screen(driver)


# scenario 3
@given('User opens the journey for the first time')
def open_journey_first_time(driver):
    home.select_subject_mathematics(driver)
    journey_start.scroll_up_with_highlight_journey(driver)
    journey_start.click_on_new_journey_card(driver)


@when('User is in journey loading screen')
def journey_loading(driver):
    journey_start.verify_journey_loading_screen(driver)


@then('Verify that user should navigate to <JourneyMapScreen> after the loading screen')
def journey_map_screen(driver):
    journey_start.verify_journey_map_screen(driver)


@then('Verify formation of map should start')
def map_formation(driver):
    pass


@then('Verify the nodes appear with node names followed by node arrangement')
def node_names(driver):
    journey_start.nodes(driver)


# scenario 4
@given('Launch the app online.')
def app_online(driver):
#     journey_start.switch_to_wifi(driver)
    home.navigate_to_home_screen(driver)
    


@given('User opens already downloaded journey')
def already_loaded_journey(driver):
    home.select_subject_mathematics(driver)
    journey_start.scroll_up_with_highlight_journey(driver)
    journey_start.click_on_already_taken_journey_card(driver)


@then('Verify auto load the node which user need to continue to proceed the journey')
def auto_load_node(driver):
    journey_start.verify_resource_screen(driver)
    
    