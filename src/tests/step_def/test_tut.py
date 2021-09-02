from pytest_bdd import scenarios, given, when, then, parsers
from pytest import fixture

from utilities.neo_tute_mentoring import NeoTute

feature_file_name = 'test_tut'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def test_tut(driver):
    test_tut = NeoTute(driver)
    yield test_tut



@given("navigate to start screen page of tut")
def step_impl(test_tut):
    test_tut.join_class()
