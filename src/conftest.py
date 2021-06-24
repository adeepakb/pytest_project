import re
import time
import traceback
import os
import sys
import pytest
import subprocess
import logging
from constants.platform import Platform
from utilities.BasePage import BaseClass
from utilities.pre_execution import BuildFeatureJob
from selenium.common.exceptions import InvalidSessionIdException
from utilities.base_page import BaseClass
from utilities.common_methods import CommonMethods
from utilities.pre_execution import BuildFeatureJob
from constants.test_management import *
#from constants.loadFeatureFile import fetch_feature_file
from tests.common_steps import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
sys.path.append(PATH('constants/'))
from constants.test_management import *

from tests.common_steps import *

base_class = BaseClass()
# CommonMethods = CommonMethods()
#feature_job = BuildFeatureJob()


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    #feature_job.build_and_install_apk()
    yield
    # Create report on demand via  API at the end of the session
    suitename = os.getenv('suite')
    if suitename == "Byju's Classes":
        report_id = get_testrail_reports(24, 'Regression Run (Summary) %date%')
        run_testrail_reports(report_id)
    elif suitename == 'Sanity_PremiumApp_Automation':
        report_id = get_testrail_reports(24, 'Sanity Run (Summary) %date%')
        run_testrail_reports(report_id)


def pytest_addoption(parser):
    parser.addoption("--platform", action="append")


def capture_screenshot(request, feature_name):
    driver = request.getfixturevalue("driver")
    timestamp = datetime.datetime.now().strftime("%d-%m-%y, %H-%M-%S")
    screenshot_filename = feature_name + " " + timestamp + ".png"
    driver.get_screenshot_as_file(screenshot_filename)
    return screenshot_filename


@pytest.fixture()
def driver(request):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        android_driver = base_class.setup_android()
        # feature_job.lock_or_unlock_device('lock')
        # serial = feature_job.connect_adb_api()
        # feature_job.connect_to_adb(serial)
        yield android_driver
        # subprocess.Popen('adb disconnect ' + serial, shell=True, stdout=subprocess.PIPE,
        #                  stderr=subprocess.STDOUT).communicate()
        android_driver.quit()
    elif Platform.WEB.name in platform_list:
        chrome_driver = base_class.setup_browser()
        yield chrome_driver
        chrome_driver.quit()
    else:
        platform = platform_list[-1]
        raise NotImplementedError(f"'{platform}' is not yet implemented.")


# ---------------------------testrail updation--------------------
def py_test():
    """
    Create and update the local-variable and reuse the same when required.
    Will not be available across the test file(s) unless imported.
     :returns: None
    """
    pass


def pytest_bdd_before_scenario(feature):
    """
       Called before each scenario is executed.
       Initialize the ``exception`` variable in ``py_test`` method.
       :returns: None
       """
    py_test.exception = None
    py_test.start = time.time()
    feature_name = feature.name
    if feature_name == 'Register Screen':
        subprocess.Popen('adb shell pm clear com.byjus.thelearningapp.premium', shell=True)
    logging.info(feature_name)
    # This code is used to make "No Reset" false before launching the app"
    if feature_name == 'Register Screen' or feature_name == 'Register OTP Verification Screen':
        subprocess.Popen('adb shell pm clear com.byjus.thelearningapp.premium', shell=True)


def pytest_bdd_before_step(step):
    py_test.step_name = step.name


def pytest_bdd_step_func_lookup_error(step):
    """
    Called when step lookup failed.
    Update the value ``True`` of ``py_test.exception`` as exception occurred.
    :type step: Step
    :returns: None
    """
    py_test.exception = True
    py_test.failed_step_name = step.name


def pytest_bdd_step_validation_error(step):
    """
    Called when step failed to validate.
    Update the value ``True`` of ``py_test.exception`` as exception occurred.
    :type step: Step
    :returns: None
    """
    py_test.exception = True
    py_test.failed_step_name = step.name


def pytest_bdd_step_error(step):
    """
    Called when step function failed to execute.
    Update the value ``True`` of ``py_test.exception`` as exception occurred.
    :type step: Step
    :returns: None
    """
    py_test.exception = True
    py_test.failed_step_name = step.name


def pytest_bdd_after_scenario(request, feature, scenario):
    """
    Called after scenario is executed even if one of steps has failed.
    Occurred exceptions during test execution is written to ``sys.stderr``
    with appropriate information, the same will be written on console.
    The exit status is updated with valid message to the
    `testrail <https://tnl.testrail.com/index.php?/dashboard>`_
    :type scenario: Scenario
    :type feature: Feature
    :var str suite_name: Name of the `TestSuite`
    :return: None
    .. note:: If there occurs an exception during the testrail update,
        the results might not reflect on the testrail.
    """
    e_type, value, tb = sys.exc_info()
    summaries = traceback.format_exception(e_type, value, tb)
    prj_path_only = os.path.abspath(os.getcwd() + "/../..")
    feature_name = feature.name
    scenario_name = scenario.name
    app_version = base_class.get_current_app_version()
    elapsed_time = int(time.time() - py_test.__getattribute__('start'))
    py_test.elapsed = str(elapsed_time) + 's'
    suite_name = os.getenv('suite')
    #data = get_run_and_case_id_of_a_scenario(suite_name, scenario.name, "24", "199")
    if py_test.__getattribute__("exception") or value:
        trc = re.findall(r'Traceback.*', ''.join(summaries))[-1] + "\n"
        _exception = list(filter(lambda summary:
                                 prj_path_only in summary or
                                 summaries.index(summary) == 0 or
                                 ("exception" in summary.lower() and prj_path_only in summary) or
                                 ("error" in summary.lower() and prj_path_only in summary), summaries))
        while _exception.count(trc) > 0:
            _exception.remove(trc)
        _exception.insert(0, trc)
        _exception.append(summaries[-1])
        _exception = "".join(_exception)
        screenshot_filename = capture_screenshot(request,feature_name)
        if not value:
            step_name = py_test.__getattribute__('failed_step_name')
        else:
            step_name = py_test.__getattribute__('step_name')
        stdout_err = (
                "\n" + "=" * 100 +
                "Failures" + "=" * 100 +
                "\nFailed Feature Name: %s\nFailed Scenario Name: %s\nFailed Step Name: %s\n"
                % (feature_name, scenario_name, step_name) +
                "-" * 50 + "Test Exception" + "-" * 50 + "\n" + _exception +
                "=" * 100 + "Failures" + "=" * 100
        )
        sys.stderr.writelines(stdout_err)
        # update_testrail(data[1], data[0], False, step_name, _exception)
        # add_attachment_to_result(data[0], data[1], screenshot_filename)
    else:
        msg_body = "all steps are passed"
        # update_testrail(data[1], data[0], True, msg_body, 'passed')
        # update_testrail(data[1], data[0], True, msg_body, 'passed', py_test.elapsed, app_version)
    file = '../../config/chrome_session.json'
    try:
        os.unlink(file)
    except FileNotFoundError:
        pass


def pytest_sessionfinish():
    for file in ['../../config/login.pkl', '../../config/chrome_session.json']:
        try:
            os.unlink(file)
        except FileNotFoundError:
            pass
