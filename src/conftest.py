"""
This module is auto-discovered during the test execution.
All the common fixture(s) and hook(s) are implemented here,
as they get executed on priority which will be available
across the test file(s). It is good practice to keep this
module closer to the directory root.

.. code-block:: python
    :caption: next_gen/conftest.py

    from pytest import fixture
    @fixture
    def add_any():
        def add_val(a, b):
            return a + b
    return add_val

.. code-block:: python
    :caption: next_gen/tests/test_example.py

    from pytest import mark

    @mark.parametrize(("a", "b"), [(10, 20)])
    def test_add(add_any, a, b):
        print("Value added", add_any(a, b))
"""
import sys
from os import unlink
from logging import info
from re import findall
from subprocess import Popen, PIPE, STDOUT
from traceback import format_exception

from selenium.common.exceptions import InvalidSessionIdException

from constants.test_management import *
from tests.common_steps import *
from constants.platform import *
from constants.loadFeatureFile import fetch_featurefile


# @pytest.fixture(scope="session", autouse=True)
# def setup_teardown():
#     feature_job.build_and_install_apk()
#     yield
#     # Create report on demand via  API at the end of the session
#     suitename = os.getenv('suite')
#     if suitename == 'Regression_PremiumApp_Automation':
#         report_id = get_testrail_reports(13, 'Regression Run (Summary) %date%')
#         run_testrail_reports(report_id)
#     elif suitename == 'Sanity_PremiumApp_Automation':
#         report_id = get_testrail_reports(13, 'Sanity Run (Summary) %date%')
#         run_testrail_reports(report_id)

@fixture
def driver(request, base_class, feature_job):
    platform_list = request.config.getoption("platform")
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        android_driver = base_class.setup_android()
        feature_job.lock_or_unlock_device('lock')
        serial = feature_job.connect_adb_api()
        feature_job.connect_to_adb(serial)
        yield android_driver
        Popen('adb disconnect ' + serial, shell=True, stdout=PIPE, stderr=STDOUT).communicate()
        try:
            android_driver.quit()
        except InvalidSessionIdException:
            """mostly socket was already hung up"""
            pass
    elif Platform.WEB.name.lower() == platform_list[-1].lower():
        chrome_driver = base_class.setup_browser()
        yield chrome_driver
        chrome_driver.quit()
    else:
        platform = platform_list[-1]
        raise NotImplementedError(f"'{platform}' is not yet implemented.")


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
    feature_name = feature.name
    if feature_name == 'Register Screen':
        Popen('adb shell pm clear com.byjus.thelearningapp.premium', shell=True)
    info(feature_name)
    # This code is used to make "No Reset" false before launching the app"
    if feature_name == 'Register Screen' or feature_name == 'Register OTP Verification Screen':
        Popen('adb shell pm clear com.byjus.thelearningapp.premium', shell=True)


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


def pytest_bdd_after_scenario(feature, scenario):
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
    summaries = format_exception(e_type, value, tb)
    prj_path_only = os.path.abspath(os.getcwd() + "/../..")
    feature_name = feature.name
    scenario_name = scenario.name
    suite_name = os.getenv('suite')
    data = get_run_and_case_id_of_a_scenario(suite_name, scenario.name, "13", "160")
    if py_test.__getattribute__("exception") or value:
        trc = findall(r'Traceback.*', ''.join(summaries))[-1] + "\n"
        _exception = list(filter(lambda summary:
                                 prj_path_only in summary or
                                 summaries.index(summary) == 0 or
                                 ("exception" in summary.lower() and prj_path_only in summary) or
                                 ("error" in summary.lower() and prj_path_only in summary) or
                                 summaries.index(summary) == (len(summaries) - 1), summaries))
        while _exception.count(trc) > 0:
            _exception.remove(trc)
        _exception.insert(0, trc)
        _exception = "".join(_exception)
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
        update_testrail(data[1], data[0], False, step_name, _exception)
    else:
        msg_body = "all steps are passed"
        update_testrail(data[1], data[0], True, msg_body, 'passed')


def pytest_sessionfinish():
    for file in ['../../config/login.pkl', '../../config/chrome_session.json']:
        try:
            unlink(file)
        except FileNotFoundError:
            pass
