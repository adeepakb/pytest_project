"""
**Test Management**:

All the common methods related to the testrail has been implemented here.

Using TestRail API, updating the test run results with comments and status,
fetching the feature file(s) from the testrail, deleting the feature files from the local
and many more functionalities has been implemented.

TestRail base URL and user credentials such as username and password
or API token are all fetched from the JSON (config.json) file.

"""
import datetime
from enum import Enum
from cryptography.fernet import Fernet
from constants.testrail import *
from constants.constants import *
from constants.load_json import *
import glob
import json
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

key = os.getenv('SECRET')
f = Fernet(key)
encrypted_data = get_data('../config/config.json', 'encrypted_data', 'token')
decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))
testrail_url = decrypted_data['testrail']['url']
testrail_username = decrypted_data['testrail']['userName']
testrail_password = decrypted_data['testrail']['password']

custom_Tag_Dict = {1: 'Video', 2: 'Sanity', 3: 'BVT'}
custom_Tag_List = [1, 2, 3]


# by enum we are assigning the values of custom_auto_status
class TestingType(Enum):
    MANUAL = 1
    AUTOMATION = 2


def get_testrail_client():
    """
    Create a APIClient instance.

    The ``client.user`` and ``client.password`` can be set from JSON or provide directly here.

    :returns: A APIClient object
    :rtype: APIClient
    """
    client = APIClient(testrail_url)
    client.user = testrail_username
    client.password = testrail_password
    return client


def get_section(section_id):
    """
    Get the details about the section by providing section_id

    :param section_id: ID of the section
    :type section_id: str
    :return: A dict containing the result of the request.
    :rtype: str | dict
    """
    client = get_testrail_client()
    section = client.send_get('get_section/' + section_id)
    return section


def delete_feature_files():
    """
    Delete all the feature files.

    :return: None
    """
    f_files = glob.glob(PATH('../tests/features/*.feature'))
    for f in f_files:
        os.remove(f)


def create_feature_file(suite_id, project_id):
    """
    Create the feature file(s) for the given *project_ID*, *suite_id*

    :param project_id: ID of the project.
    :param suite_id: ID of the suite that belongs to same *project_id*. Example: `S123`
    :type suite_id: str
    :type project_id: str
    :return: None

    """
    delete_feature_files()
    client = APIClient('https://tnl.testrail.io/')
    client.user = testrail_username
    client.password = testrail_password
    suite = client.send_get('get_suite/' + suite_id)
    feature_name = suite['name'].replace(" ", "_")
    cases = client.send_get('get_cases/' + project_id + '&suite_id=' + suite_id)

    print(cases)

    currenttime = datetime.datetime.now()
    curstr = currenttime.__str__().replace("-", "").replace(":", "").replace(" ", "")[0:12]

    f = None

    filedata = None
    section_id_1 = 0
    section_id_2 = 1
    count = 0
    tag_name = None
    for case in cases:
        if case['custom_automation_type'] == TestingType.AUTOMATION.value:

            section_id_1 = section_id_2

            section_id_2 = case['section_id']

            if section_id_1 != section_id_2:
                try:
                    f.write(filedata)
                    f.close()
                except:
                    print('')
                f = open(PATH('../tests/features/' + str(get_section(str(section_id_2))['name']) + '.feature'), "w+")
                tag = str(get_section(str(section_id_2))['name'])
                print(tag)
                tag_name = tag.split(' ')
                print(str(section_id_2))
                filedata = 'Feature: ' + str(get_section(str(section_id_2))['name']) + '\n'
                count += 1
            if case['title'] is not None:
                if 'happyflow' in str(case['title']):
                    filedata += ('\n\n' + "@" + tag_name[0])
                    filedata += ('\n' + case['title'].strip())
                else:
                    filedata += ('\n\nScenario: ' + case['title'].strip())
            if case['custom_given'] is not None:
                str_given = case['custom_given'].strip()
                if '\r\n' in str_given:
                    str1 = str_given.split('\r\n')
                    filedata += ('\n\tGiven ' + str1[0])

                    for i in range(len(str1)):
                        if i >= 1:
                            filedata += ('\n\t' + str1[i])
                else:
                    filedata += ('\n\tGiven ' + case['custom_given'].strip())
            if case['custom_when'] is not None:
                str_given = case['custom_when'].strip()
                if '\r\n' in str_given:
                    str1 = str_given.split('\r\n')
                    filedata += ('\n\tWhen ' + str1[0])

                    for i in range(len(str1)):
                        if i >= 1:
                            filedata += ('\n\t' + str1[i])
                else:
                    filedata += ('\n\tWhen ' + case['custom_when'].strip())
            if case['custom_then'] is not None:
                str_given = case['custom_then'].strip()
                if '\r\n' in str_given:
                    str1 = str_given.split('\r\n')
                    filedata += ('\n\tThen ' + str1[0])

                    for i in range(len(str1)):
                        if i >= 1:
                            filedata += ('\n\t' + str1[i])
                else:
                    filedata += ('\n\tThen ' + case['custom_then'].strip())

    f.write(filedata)
    f.close()
    print('Number of feature file created = ' + str(count))


# this method is used to fetch the feature files from test run
def create_feature_from_run(suite_ID, project_ID, run_ID):
    delete_feature_files()
    client = APIClient('https://tnl.testrail.io/')
    client.user = testrail_username
    client.password = testrail_password
    suite = client.send_get('get_suite/' + suite_ID)
    feature_name = suite['name'].replace(" ", "_")
    cases = client.send_get('get_tests/' + run_ID)
    print(cases)

    currenttime = datetime.datetime.now()
    curstr = currenttime.__str__().replace("-", "").replace(":", "").replace(" ", "")[0:12]

    f = None

    filedata = None
    section_id_1 = 0
    section_id_2 = 1
    count = 0
    no_of_featrure_files = 0
    for case in cases:
        if case['custom_automation_type'] == TestingType.AUTOMATION.value:
            case_suite = client.send_get('get_case/' + str(case['case_id']))
            section_id_1 = section_id_2
            section_id_2 = case_suite['section_id']

            f = open(PATH('../tests/features/' + str(get_section(str(section_id_2))['name']) + '.feature'), "a+")

            if section_id_1 != section_id_2:
                try:
                    no_of_featrure_files += 1
                    scenario_count = 0
                    print('\n' + str(get_section(str(section_id_2))['name']))
                    filedata = 'Feature: ' + str(get_section(str(section_id_2))['name'])
                    f.write(filedata)
                except:
                    print('')

            if case['custom_tags'] != None:
                filedata = ('\n\n')
                for i in case['custom_tags']:

                    if i in custom_Tag_List:
                        filedata += ("@" + custom_Tag_Dict[i] + ' ')
            count += 1

            if case['title'] != None:
                if 'happyflow' in str(case['title']):
                    filedata += ('\n' + case['title'].strip())
                else:
                    filedata += ('\nScenario: ' + case['title'].strip())
            scenario_count += 1
            print(scenario_count)
            print(case['title'].strip())

            if case['custom_given'] != None:
                strGiven = case['custom_given'].strip()
                if '\r\n' in strGiven:
                    str1 = strGiven.split('\r\n')
                    filedata += ('\n\tGiven ' + str1[0])

                    for i in range(len(str1)):
                        if i >= 1:
                            filedata += ('\n\t' + str1[i])
                else:
                    filedata += ('\n\tGiven ' + case['custom_given'].strip())
            if case['custom_when'] != None:
                strGiven = case['custom_when'].strip()
                if '\r\n' in strGiven:
                    str1 = strGiven.split('\r\n')
                    filedata += ('\n\tWhen ' + str1[0])

                    for i in range(len(str1)):
                        if i >= 1:
                            filedata += ('\n\t' + str1[i])
                else:
                    filedata += ('\n\tWhen ' + case['custom_when'].strip())

            if case['custom_then'] != None:
                strGiven = case['custom_then'].strip()
                if '\r\n' in strGiven:
                    str1 = strGiven.split('\r\n')
                    filedata += ('\n\tThen ' + str1[0])

                    for i in range(len(str1)):
                        if i >= 1:
                            filedata += ('\n\t' + str1[i])
                else:
                    filedata += ('\n\tThen ' + case['custom_then'].strip())

            f.write(filedata)
            f.close()
    print('Number of feature file created = ' + str(no_of_featrure_files))
    print('Number of test cases in feature files = ' + str(count))


def update_testrail(case_id, run_id, result_flag, step, exc_msg, elapsed_time, testing_device, app_version):
    """
    Update the result to testrail for the particular *run_id* and *case_id* with appropriate
    comments and status.
    The status will set accordingly whether or not an exception occurs during test execution.
    :param case_id: ID of the case of the particular test case. Example: `C12345`
    :param run_id: ID of the run, can be found under **Test Runs and Results**. Example: `R123`
    :param result_flag: is set True/False based on whether or not exception has occurred
    :param step: Failed step name if exception has occurred else *None* is set.
    :param exc_msg: Exception stack trace is set if exception occurred else *All test steps have passed* is set.
    :param elapsed_time: execution time of each scenario
    :param testing_device: device on which test execution was carried out
    :param app_version: app version
    :type case_id: str
    :type run_id: str
    :type result_flag: bool
    :type step: str
    :type exc_msg: str
    :type elapsed_time: str
    :type testing_device: str
    :type app_version: str
    :return: `True` if update was successful and `False` if there is an Exception
    :rtype: bool
    """
    update_flag = False
    client = get_testrail_client()
    status_id = 1 if result_flag is True else 5
    if not result_flag:
        exc_msg = "Failed Step Name: %s\n%s" % (step, exc_msg)
    if run_id is not None:
        result = client.send_post('add_result_for_case/%s/%s' % (run_id, case_id),
                                  {'status_id': status_id,
                                   'comment': exc_msg + '\nTested on device model : %s' % testing_device,
                                   'elapsed': elapsed_time,
                                   'version': app_version})
        print("Status: %s" % result)
        print('Updated test result for case: %s in test run: %s ' % (case_id, run_id))
    return update_flag


def get_project_id(project_name):
    """
    Get the ID of the project for the specified project name

    :param project_name: Name of the project as string. Example: `tutor_plus_automation`
    :type project_name: str
    :return: The ID of the specified project name
    :rtype: str
    """
    client = get_testrail_client()
    project_id = None
    projects = client.send_get('get_projects')
    for project in projects:
        if project['name'] == project_name:
            project_id = project['id']
            # project_found_flag=True
            break
    print("project id is:" + project_id)
    return project_id


def get_run_and_case_id_of_a_scenario(test_run_name, scenario_name, project_id, suite_id):
    """
    Get the ``run_id`` and ``case_id`` for the given name of the test run and scenario,
    ID of the project and suite

    :param project_id: ID of the valid and existing project.
    :param suite_id: ID of the suite that can found under **Test Suite and Cases**. Example: `S123`
    :param test_run_name: name of the run module that is created under
        **Test Run and Results** belongs to same suite. Example: `student_session`, `white_board_module`
    :param scenario_name: name of the scenario of any valid and existing test case.
        Example: `Scenario: Verify all elements of login screen`
    :type test_run_name: str
    :type scenario_name: str
    :type project_id: str
    :type suite_id: str
    :return: The list containing run-ID and case-ID
    :rtype: list[str]
    """
    client = get_testrail_client()
    suite = client.send_get('get_suite/' + suite_id)
    run_id = None
    data = []
    test_runs_dict = client.send_get('get_runs/%s' % project_id)
    test_runs = test_runs_dict['runs']
    # print("*************",test_runs)
    for test_run in test_runs:
        if test_run['name'] == test_run_name:
            run_id = test_run['id']
            break
    data.append(str(run_id))
    cases_dict = client.send_get('get_tests/' + str(run_id))
    cases = cases_dict['tests']
    # print(cases)
    for case in cases:
        if case['title'] == scenario_name:
            case_suite = client.send_get('get_case/' + str(case['case_id']))
            data.append(str(case_suite['id']))
            return data


# returns a list of API available reports by project
def get_testrail_reports(project_ID, report_name):
    client = get_testrail_client()
    reports = client.send_get('get_reports/' + str(project_ID))
    report_id = None
    for report in reports:
        if report['name'] == report_name:
            report_id = report['id']
    return report_id


# executes the report identified using the report_id parameter and returns URLs for accessing the reports
def run_testrail_reports(report_id):
    client = get_testrail_client()
    report = client.send_get('/run_report/' + str(report_id))
    report_url = report['report_url']
    return report_url


# to fetch latest result id
def get_latest_result_id(run_id,case_id):
    client = get_testrail_client()
    test_results = client.send_get('get_results_for_case/%s/%s' % (run_id, case_id))
    for test_result in test_results:
        if test_result is not None:
            print(test_result['id'])
            return test_result['id']

# Add attachment to test result
def add_attachment_to_result(run_id,case_id, attachment):
    client = get_testrail_client()
    result_id = get_latest_result_id(run_id,case_id)
    response = client.send_post('add_attachment_to_result/%s' % (result_id),attachment)
    print(response)


# update execution time for existing test run
def update_run_for_execution_time(run_id, duration):
    client = get_testrail_client()
    response = client.send_post('update_run/%s' % run_id, {'description': 'Total execution time %s' % duration})
    print(response)


def get_run_id(test_run_name, project_name):
    """
    Get the `run_id` for the given name of the test run and name of the project.

    :param project_name: name of the valid and existing project. Example: `tutor_plus_automation`
    :param test_run_name: name of the run module that is created under **Test Run and Results**.
        belongs to same project. Example: `student_session`, `white_board_module`
    :type project_name: str
    :type test_run_name: str
    :return: the run ID for the specified test run and project name.
    :rtype: str
    """
    run_id = None
    client = get_testrail_client()
    project_id = get_project_id(project_name)
    test_runs = client.send_get('get_runs/%s' % project_id)
    for test_run in test_runs:
        if test_run['name'] == test_run_name:
            run_id = test_run['id']
            break
    return run_id


def get_custom_field_scenario(test_run_name, scenario_name, project_id):
    client = get_testrail_client()
    run_id = None
    test_runs_dict = client.send_get('get_runs/%s' % project_id)
    for test_run in test_runs_dict['runs']:
        if test_run['name'] == test_run_name:
            run_id = test_run['id']
            break
    cases = client.send_get('get_tests/' + str(run_id))['tests']
    for case in cases:
        return True if case['title'] == scenario_name and case['custom_merged_case'] == 1 else False
