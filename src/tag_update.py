from constants.testrail import APIClient
from json import load


class TagUpdate:
    def __init__(self, run_id, _url, _user, _key):
        self.run_id = run_id
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
            if int(test["custom_automation_type"]) != 2:
                id_s.append(test['case_id'])
        return id_s

    def update_test_type(self):
        data = {'custom_automation_type': 2}
        cases_id = self.get_test_run_case_ids()
        count = 1
        for case_id in cases_id:
            self.client.send_post(f'update_case/{case_id}', data)
            print(f'{count}. updated: {case_id}')
            count += 1


if __name__ == "__main__":
    with open('config/config.json') as fp:
        _data = load(fp)["testrail"]
        _url, _user, _key = _data["url"], _data["userName"], _data['password']
    tag_update = TagUpdate(input("Enter Run-ID: "), _url, _user, _key)
    tag_update.update_test_type()
