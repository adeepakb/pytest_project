from pytest import fixture
from pytest_bdd import scenarios, given, when, then

from utilities.staging_tllms import Stagingtllms

feature_file_name = 'Post Requisites and its resource type'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def tllms(driver):
    staging = Stagingtllms(driver)
    yield staging


@given("launch the browser and login to tutor plus staging cms")
def step_impl(tllms):
    tllms.login_to_staging(cms=True)


@then('verify forward icons are displayed')
def step_impl(ssn_req):
    ssn_req.verify_requisite_details(dtls='forward_icons')


@then('verify the attached assessment is present')
def step_impl(ssn_req):
    ssn_req.verify_requisite_details(dtls='assessment')


@when('verify the attached video is present')
def step_impl(ssn_req):
    ssn_req.verify_requisite_details(dtls='video')


@then('verify the attached video is present')
def step_impl(ssn_req):
    ssn_req.verify_requisite_details(dtls='video')


@then('verify on tap of "see more" remaining post requisite is displayed')
def step_impl(ssn_req):
    assert ssn_req.verify_requisite_details()


@then('verify the user is navigated to the session details screen where all the tagged resource types are shown')
def step_impl(std_board, ssn_req):
    assert std_board.is_session_details_displayed()
    assert std_board.is_post_requisite_attached()
    assert ssn_req.is_all_requisites_attached()


@then('verify that user should be able to watch video in portrait and landscape modes')
def step_impl(ssn_req):
    assert ssn_req.is_video_landscape_playable()


@then('verify that completed session is the first card in the for you tab')
def step_impl(std_board):
    assert std_board.is_completed_first_card()
