import datetime
import os
import sys
from enum import Enum
from constants.testrail import *
from constants.constants import *
from constants.load_json import *
import json
import glob
from ntpath import split

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

testrail_file = CONFIG_PATH
testrail_url = getdata(testrail_file, 'testrail', 'url')
testrail_username = getdata(testrail_file, 'testrail', 'userName')
testrail_password = getdata(testrail_file, 'testrail', 'password')
custom_Tag_Dict = {1: 'Video', 2: 'Sanity', 3: 'BVT'}
custom_Tag_List = [1, 2, 3]


# by enum we are assigning the values of custom_autostatus
class Autostatus(Enum):
    Manual = 1
    Automated = 2
    Non_Automatable = None


member_autostaus_automatable = Autostatus.Non_Automatable
automation_updated_tag = Autostatus.Automated


def get_testrail_client():
    "Get the TestRail account credentials from the config file"
    # Get the TestRail Url
    client = APIClient(testrail_url)
    # Get and set the TestRail User and Password
    client.user = testrail_username
    client.password = testrail_password
    return client


def get_section(section_ID):
    client = get_testrail_client()
    section = client.send_get('get_section/' + section_ID)
    return section


def delete_feature_files():
    f_files = glob.glob(PATH('../tests/features/*.feature'))
    for f in f_files:
        os.remove(f)


# this is the method used for fetching the feature files from suite
def create_feature_file(suite_ID, project_ID, run_ID):
    delete_feature_files()
    client = APIClient('https://tnl.testrail.io/')
    client.user = testrail_username
    client.password = testrail_password
    suite = client.send_get('get_suite/' + suite_ID)
    feature_name = suite['name'].replace(" ", "_")
    cases = client.send_get('get_cases/' + project_ID + '&suite_id=' + suite_ID)

    print(cases)

    currenttime = datetime.datetime.now()
    curstr = currenttime.__str__().replace("-", "").replace(":", "").replace(" ", "")[0:12]

    f = None

    filedata = None
    section_id_1 = 0
    section_id_2 = 1
    count = 0

    for case in cases:
        if case['custom_autostatus'] == member_autostaus_automatable.value:

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
                #                 print(tag)
                tag_name = tag.split(' ')
                #                 print (str(section_id_2))
                filedata = 'Feature: ' + str(get_section(str(section_id_2))['name']) + '\n'
                count += 1

            if case['title'] != None:

                if 'happyflow' in str(case['title']):
                    filedata += ('\n\n' + "@" + tag_name[0])
                    filedata += ('\n' + case['title'].strip())
                else:
                    filedata += ('\n\nScenario: ' + case['title'].strip())
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
        if case['custom_automation_type'] == 2:
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


#    ------------------------------------------------------------------------


# Update the result in TestRail using send_post function.
# Parameters for add_result_for_case is the combination of run id and case id.
# status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
def update_testrail(case_id, run_id, result_flag, step, excp_msg):
    "Update TestRail for a given run_id and case_id"
    update_flag = False
    # Get the TestRail client account details
    client = get_testrail_client()
    status_id = 1 if result_flag is True else 5
    #     print("result flag is "+result_flag)
    print(excp_msg)
    print(step)
    if run_id is not None:
        try:
            result = client.send_post('add_result_for_case/%s/%s' % (run_id, case_id),
                                      {'status_id': status_id, 'comment': step})
        except:
            print('Exception in update_testrail() updating TestRail.')
        else:
            print('Updated test result for case: %s in test run: %s ' % (case_id, run_id))

    return update_flag


# to featch the project id
def get_project_id(project_name):
    "Get the project ID using project name"
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


# this method is used to fetch the test data from rum
def get_test_case_data_from_run(suite_ID, project_ID, run_ID):
    client = get_testrail_client()
    cases = client.send_get('get_tests/' + run_ID)
    #     print(cases)
    for case in cases:
        #         if case['custom_autostatus'] != 3:
        #                     case_suite = client.send_get('get_case/' + str(case['case_id']))
        print(case)


# to fetch run id and case id of a particular scenario
def get_run_and_case_id_of_a_scenario(test_run_name, scenario_name, project_ID, suite_ID):
    client = get_testrail_client()
    suite = client.send_get('get_suite/' + suite_ID)
    run_id = None
    data = []
    test_runs = client.send_get('get_runs/%s' % (project_ID))
    #     print(test_runs)
    for test_run in test_runs:
        if test_run['name'] == test_run_name:
            run_id = test_run['id']
            break
    data.append(str(run_id))
    cases = client.send_get('get_tests/' + str(run_id))
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


# to fetch the run id by giving test run name
def get_run_id(test_run_name, project_name):
    "Get the run ID using test name and project name"
    run_id = None
    client = get_testrail_client()
    project_id = get_project_id(project_name)
    try:
        test_runs = client.send_get('get_runs/%s' % (project_id))
    except:
        print('Exception in update_testrail() updating TestRail.')
        return None
    else:
        for test_run in test_runs:
            if test_run['name'] == test_run_name:
                run_id = test_run['id']
                break
        return run_id
