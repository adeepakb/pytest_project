import re
import traceback
import os
import pytest
from _pytest._code.code import ExceptionInfo
from pytest_bdd import scenarios, given, when, then, parsers, scenario
import os
import sys
import subprocess
import logging
from time import sleep
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from Utilities.BasePage import BaseClass
from Utilities.common_methods import CommonMethods
from Utilities.pre_execution import BuildFeatureJob
from Utilities.interrupt import *
from Utilities import common_methods

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
sys.path.append(PATH('Constants/'))
from Constants.test_management import *
from Constants.loadFeatureFile import fetch_featurefile

baseClass = BaseClass()
CommonMethods = CommonMethods()
feature_job = BuildFeatureJob()


@pytest.fixture()
def driver():
    driver = baseClass.driverSetup()
    feature_job.lock_or_unlock_device('lock')
    serial = feature_job.connect_adb_api()
    feature_job.connect_to_adb(serial)
    yield driver
    subprocess.Popen('adb disconnect ' + serial, shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT).communicate()
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def configure():
    suite_name = os.getenv('suite')
    if suite_name == 'Regression_PremiumApp_Automation':
        fetch_featurefile("160", "13", "184")
    elif suite_name == 'Sanity_PremiumApp_Automation':
        fetch_featurefile("160", "13", "256")
    feature_job.build_and_install_apk()
    yield
    # Create report on demand via  API at the end of the session
    if suite_name == 'Regression_PremiumApp_Automation':
        report_id = get_testrail_reports(13, 'Regression Run (Summary) %date%')
        run_testrail_reports(report_id)
    elif suite_name == 'Sanity_PremiumApp_Automation':
        report_id = get_testrail_reports(13, 'Sanity Run (Summary) %date%')
        run_testrail_reports(report_id)


# ---------------------------testrail updation--------------------
testrail_file = CONFIG_PATH
testrail_url = getdata(testrail_file, 'testrail', 'url')
testrail_username = str(getdata(testrail_file, 'testrail', 'userName'))
testrail_password = str(getdata(testrail_file, 'testrail', 'password'))
step_error_flag = ""
exception_msg = ""
failed_step_name = ""


# fetch the feature file name
def pytest_bdd_before_scenario(request, feature, scenario):
    #     appium_service.start()
    py_test.exception = None

    global featureFileName
    featureFileName = feature.name
    if featureFileName == 'Register Screen':
        CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')

    logging.info(featureFileName)

    # logging.info(featureFileName)

    # This code is usesd to make "No Reset" false before launching the app"
    if featureFileName == 'Register Screen' or featureFileName == 'Register OTP Verification Screen':
        CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')

    global step_error_flag
    step_error_flag = True
    global exception_msg
    exception_msg = " "
    global failed_step_name
    failed_step_name = ""


def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    global step_error_flag
    py_test.step_name = step.name
    step_error_flag = True
    logging.info(step_error_flag)


# Called when step lookup failed
# if error occurred in step defination than this method will execute
def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception):
    logging.info("step fail")
    py_test.exception = True
    py_test.failed_step_name = step.name
    global step_error_flag
    step_error_flag = True
    logging.info(step_error_flag)
    logging.info("failing in this step --> " + step.name)
    global failed_step_name
    failed_step_name = "failing in this step --> " + step.name
    global exception_msg
    exception_msg = exception


# Called when step failed to validate
def pytest_bdd_step_validation_error(request, feature, scenario, step, step_func, step_func_args, exception):
    logging.info("step error")
    py_test.exception = True
    py_test.failed_step_name = step.name
    global step_error_flag
    step_error_flag = True
    logging.info(step_error_flag)
    logging.info("failing in this step --> " + step.name)
    global failed_step_name
    failed_step_name = "failing in this step --> " + step.name
    global exception_msg
    exception_msg = exception


# if error occurred in test file functions than this method will execute
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    logging.info("step error")
    py_test.exception = True
    py_test.failed_step_name = step.name
    global step_error_flag
    step_error_flag = True
    logging.info(step_error_flag)
    logging.info("failing in this step --> " + step.name)
    global failed_step_name
    failed_step_name = "failing in this step --> " + step.name
    global exception_msg
    exception_msg = exception


# this will execute after each and every successful step
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    try:
        logging.info("completed successfully--> " + step.name + " step")
        global step_error_flag
        step_error_flag = False
        logging.info(step_error_flag)
    except:
        print('......................')


def py_test():
    """
    Create and update the local-variable and reuse the same when required.
    Will not be available across the test file(s) unless imported.
     :returns: None
    """
    pass


# this will execute after scenario no matter it is passed or failed
def pytest_bdd_after_scenario(request, feature, scenario):
    # logging.info(step_error_flag)
    logging.info("after scenario")
    '''
    updating result to testrail
    '''
    data = None
    #     ProjectID = test_management.get_project_id("Learning App")
    suitename = os.getenv('suite')
    data = get_run_and_case_id_of_a_scenario(suitename, scenario.name, "13", "160")
    e_type, value, tb = sys.exc_info()
    summaries = traceback.format_exception(e_type, value, tb)
    prj_path_only = os.path.abspath(os.getcwd() + "/../..")
    if py_test.__getattribute__("exception"):
        trc = re.findall(r'Traceback.*', ''.join(summaries))[-1] + "\n"
        _exception = list(filter(lambda summary:
                                 prj_path_only in summary or
                                 summaries.index(summary) == 0 or
                                 summaries.index(summary) == (len(summaries) - 1), summaries))
        while _exception.count(trc) > 1:
            _exception.remove(trc)
        _exception = "".join(_exception)
        stdout_err = (
                             "=" * 45 + "Failures" + "=" * 45 +
                             "\nFailed Feature Name: %s\nFailed Scenario Name: %s\nFailed Step Name: %s\n" +
                             "-" * 30 + "Test Exception" + "-" * 30 + "\n" + _exception + "=" * 45 + "Failures" +
                             "=" * 45
                     ) % (feature.name, scenario.name, py_test.__getattribute__('failed_step_name'))
        sys.stderr.writelines(stdout_err)
        update_testrail(data[1], data[0], False, py_test.__getattribute__('failed_step_name'), _exception)
    elif value:
        trc = re.findall(r'Traceback.*', ''.join(summaries))[-1] + "\n"
        _exception = list(filter(lambda summary:
                                 prj_path_only in summary or
                                 summaries.index(summary) == 0 or
                                 summaries.index(summary) == (len(summaries) - 1), summaries))
        while _exception.count(trc) > 1:
            _exception.remove(trc)
        _exception = "".join(_exception)
        stdout_err = (
                             "=" * 45 + "Failures" + "=" * 45 +
                             "\nFailed Feature Name: %s\nFailed Scenario Name: %s\nFailed Step Name: %s\n" +
                             "-" * 30 + "Test Exception" + "-" * 30 + "\n" + _exception + "=" * 45 + "Failures" +
                             "=" * 45
                     ) % (feature.name, scenario.name, py_test.__getattribute__('step_name'))
        sys.stderr.writelines(stdout_err)
        update_testrail(data[1], data[0], False, py_test.__getattribute__('step_name'), _exception)
    else:
        update_testrail(data[1], data[0], True, "all steps are passed", 'passed')
