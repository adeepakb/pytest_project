from json import load
import argparse
import textwrap
from constants.testrail import APIClient


class TagUpdate:
    def __init__(self, _url, _user, _key, **kwargs):
        self.update_to = kwargs["update_to"]
        if self.update_to.lower() == "test cases":
            self.sid = kwargs["suite_id"]
            self.pid = kwargs["project_id"]
            self.key = "id"
        else:
            self.run_id = kwargs["run_id"]
            self.key = "case_id"
        self.client = self.auth_access(_url, _user, _key)

    @staticmethod
    def auth_access(_url, _user, _key):
        _client = APIClient(_url)
        _client.user = _user
        _client.password = _key
        return _client

    def get_test_run_case_ids(self):
        id_s = list()
        tests = self.client.send_get(f'get_tests/{self.run_id}')
        for test in tests:
            if test["custom_automation_type"] is None:
                id_s.append(test['case_id'])
            elif int(test["custom_automation_type"]) != 2:
                id_s.append(test['case_id'])
        return id_s

    def update_test_type(self):
        data = {'custom_automation_type': 2}
        count = 1
        if self.update_to.lower() == "test runs":
            cases_id = self.get_test_run_case_ids()
        elif self.update_to.lower() == "test cases":
            cases_id = self.get_suite_case_ids()
        else:
            raise NotImplementedError()
        for case_id in cases_id:
            self.client.send_post(f'update_case/{case_id}', data)
            print(f'{count}. updated: {case_id}')
            count += 1

    def get_suite_case_ids(self):
        id_s = list()
        cases = self.client.send_get("get_cases/%s&suite_id=%s" % (self.pid, self.sid))
        for test in cases:
            if int(test["custom_automation_type"]) != 2:
                id_s.append(test[self.key])
        return id_s


if __name__ == "__main__":
    with open('config/config.json') as fp:
        _data = load(fp)["testrail"]
        _url, _user, _key = _data["url"], _data["userName"], _data['password']
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                                                TESTRAIL TAG UPDATE!
            --------------------------------------------------------------------------------------------
            Update the "Testing Type" field to "Automation" on the testrail for the created TEST RUN or
            for the existing TEST SUITE based on the argument(s) passed.
            
            Provide the "Project-ID" (i.e., P1 as -p 1) and the "Suite-ID" (i.e., S120 as -s 120) to
            update the complete TEST SUITE or provide the "Run-ID" (i.e., R123 as -r 123) to update the
            complete TEST RUN.

            Note:
            If any argument one of the argument contains "Run-ID" (i.e., -r 123) then all the other
            arguments are ignored and update will happen only for that particular TEST RUN.
        '''))
    parser.add_argument("-r", "--run_id", help="Provide the RunID. Eg., -r 100")
    parser.add_argument("-s", "--suite_id", help="Provide the SuiteID. Eg., -s 100")
    parser.add_argument("-p", "--project_id", help="Provide the ProjectID. Eg., -p 1")
    args = parser.parse_args()
    if args.run_id is not None:
        tag_update = TagUpdate(_url, _user, _key, run_id=args.run_id, update_to="test runs")
    elif args.project_id is not None and args.suite_id is not None:
        tag_update = TagUpdate(_url, _user, _key,
                               project_id=args.project_id, suite_id=args.suite_id, update_to="test cases")
    else:
        raise TypeError("either 'Run-ID' must be provided or 'Project-ID' and 'Suite-ID' must be provided.")
    tag_update.update_test_type()
