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
from Utilities.interrupt import *
from Utilities import common_methods

PATH = lambda p: os.path.abspath(
   os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('Constants/'))
from Constants.test_management import *

os.system("start /B start cmd.exe @cmd /k appium -a 127.0.0.1 -p 4723")
 
#appium_service = AppiumService()
baseClass = BaseClass()
CommonMethods = CommonMethods()
 
 
@pytest.fixture()
def browser():
    browser = baseClass.driverSetup()
    yield browser
    browser.quit()
    

# ---------------------------testrail updation--------------------
# testrail_file = CONFIG_PATH
# testrail_url = getdata(testrail_file, 'testrail', 'url')
# testrail_username = str(getdata(testrail_file, 'testrail', 'userName'))
# testrail_password = str(getdata(testrail_file, 'testrail', 'password'))
# step_error_flag = ""
# exception_msg= ""
# failed_step_name=""
#
# # fetch the feature file name
# def pytest_bdd_before_scenario(request, feature, scenario):
# #     appium_service.start()
#     global featureFileName
#     featureFileName = feature.name
#     if featureFileName == 'Register Screen':
#         CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')
#
#     logging.info(featureFileName)
#
#     # logging.info(featureFileName)
#
#     #This code is usesd to make "No Reset" false before launching the app"
#     if featureFileName == 'Register Screen' or featureFileName == 'Register OTP Verification Screen':
#         CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')
#
#     global step_error_flag
#     step_error_flag = True
#     global exception_msg
#     exception_msg = " "
#     global failed_step_name
#     failed_step_name = ""
#
#
# def pytest_bdd_before_step(request, feature, scenario, step, step_func):
#     global step_error_flag
#     step_error_flag = True
#     logging.info(step_error_flag)
#
#
# # Called when step lookup failed
# # if error occurred in step defination than this method will execute
# def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception):
#     logging.info("step fail")
#     global step_error_flag
#     step_error_flag = True
#     logging.info(step_error_flag)
#     logging.info("failing in this step --> " + step.name)
#     global failed_step_name
#     failed_step_name = "failing in this step --> " + step.name
#     global exception_msg
#     exception_msg = exception
#
#
# # Called when step failed to validate
# def pytest_bdd_step_validation_error(request, feature, scenario, step, step_func, step_func_args, exception):
#     logging.info("step error")
#     global step_error_flag
#     step_error_flag = True
#     logging.info(step_error_flag)
#     logging.info("failing in this step --> " + step.name)
#     global failed_step_name
#     failed_step_name = "failing in this step --> " + step.name
#     global exception_msg
#     exception_msg = exception
#
# # if error occurred in test file functions than this method will execute
# def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
#     logging.info("step error")
#     global step_error_flag
#     step_error_flag = True
#     logging.info(step_error_flag)
#     logging.info("failing in this step --> " + step.name)
#     global failed_step_name
#     failed_step_name = "failing in this step --> " + step.name
#     global exception_msg
#     exception_msg = exception
#
# # this will execute after each and every successful step
# def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
#     try:
#         logging.info("completed successfully--> " + step.name + " step")
#         global step_error_flag
#         step_error_flag = False
#         logging.info(step_error_flag)
#     except:
#         print ('......................')
#
# # this will execute after scenario no matter it is passed or failed
# def pytest_bdd_after_scenario(request, feature, scenario):
#     # logging.info(step_error_flag)
#     logging.info("after scenario")
#     '''
#     updating result to testrail
#     '''
#     data = None
# #     ProjectID = test_management.get_project_id("Learning App")
#     suitename = "PremiumApp_Automation"
#
#
#     data = get_run_and_case_id_of_a_scenario(suitename, scenario.name, "13", "160")
#
#
#     print("========================data after scenario")
#     logging.info(exception_msg)
#     logging.info(step_error_flag)
#     logging.info(failed_step_name)
#     try:
#         if step_error_flag == True:
#             update_testrail(data[1], data[0], False,failed_step_name,exception_msg)
#             logging.info(scenario.name + " , scenario is failed")
#         elif step_error_flag == False:
#             update_testrail(data[1], data[0], True,"all steps are passed",'passed')
#             logging.info(scenario.name + " , scenario is passed")
#     except:
#         logging.info("error occurred while updating the test result in test rail")
#
#
