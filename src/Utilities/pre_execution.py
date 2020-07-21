import json
import time
import jenkins
import requests
import subprocess
from Constants.constants import CONFIG_PATH
from Constants.load_json import getdata


class BuildFeatureJob():
    def __init__(self):
        j = jenkins.Jenkins('https://builds.byjus.com/', username='testautomation@byjus.com',
                            password='5a7b8f02aec0c2a7c5d4c348a1c7a590')

        build_num = j.get_job_info('qa_app2')['lastBuild']['number']
        build_info = j.get_build_info('qa_app2', build_num)
        build_info_actions = build_info['actions']
        parameters = build_info_actions[0]['parameters']
        print(parameters)
        branch = parameters[0]['value']
        env = parameters[1]['value']
        variant = parameters[2]['value']

        branch_parameters = dict(branch=branch, env=env, variant=variant)
        j.build_job('B2C-Feature', parameters=branch_parameters, token='5a7b8f02aec0c2a7c5d4c348a1c7a590')
        time.sleep(10)
        while True:
            print('Running....')
            if j.get_job_info('B2C-Feature')['lastCompletedBuild']['number'] == \
                    j.get_job_info('B2C-Feature')['lastBuild'][
                        'number']:
                print("Last ID %s, Current ID %s" % (j.get_job_info('B2C-Feature')['lastCompletedBuild']['number'],
                                                     j.get_job_info('B2C-Feature')['lastBuild']['number']))
                break
            time.sleep(10)
        print('Stop....')
        last_build_number = j.get_job_info('B2C-Feature')['lastCompletedBuild']['number']
        print("last_build_number", last_build_number)
        build_info = j.get_build_info('B2C-Feature', last_build_number)

        if build_info['result'] == 'SUCCESS':
            print("Build "+last_build_number+" is Successful")
            artifact = build_info['artifacts'][0]
            artifact_displaypath = artifact['displayPath']
            apk_url = 'https://builds.byjus.com/job/B2C-Feature/' + str(
                last_build_number) + '/artifact/app/build/outputs/apk/ByjusPremium/release/' + artifact_displaypath
            r = requests.Request('GET', apk_url)
            response = j.jenkins_request(r)
            print("Downloading latest apk ", apk_url)
            with open("app.apk", "wb") as f:
                f.write(response.content)

            self.lock_or_unlock_device('lock')
            serial = self.connect_adb_api()
            self.connect_to_adb(serial)

            print("Installing latest apk ", apk_url)
            stdout, stderr = subprocess.Popen('adb install -r ../../tests/step_def/app.apk', shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
            print("adb install status ", stdout, stderr)
            output = stdout.decode("ascii")
            if "Success" not in output or "1 file pushed." not in output:
                raise Exception("Failed to install app due to error %s" % output)
            print("latest apk installed successfully " + artifact_displaypath)
            subprocess.Popen('adb disconnect ' + serial, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
            self.lock_or_unlock_device('unlock')

        else:
            print("Build Failed")
            log = j.get_build_console_output('B2C-Feature', last_build_number)
            f = open('log_buildFail.txt', 'w')
            f.write(log)
            f.close()


    @staticmethod
    def connect_to_adb(serial):
        connected = False
        for i in range(5):
            subprocess.Popen('adb connect ' + serial, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
            stdout, stderr = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
            stdout = stdout.decode('ascii')
            print("adb devices %s" % stdout)
            if serial in stdout and "unauthorized" not in stdout and "offline" not in stdout:
                print("adb connected successfully")
                connected = True
                break
            print("Connection failed, retrying...")
            time.sleep(2 + i)

        if not connected:
            raise Exception("Failed to connect to device")

    @staticmethod
    def lock_or_unlock_device(flag):
        if flag == 'lock':
            url = "https://api-dev.headspin.io/v0/adb/" + getdata(CONFIG_PATH, 'desired_cap', 'udid') + "/lock"
        else:
            url = "https://api-dev.headspin.io/v0/adb/" + getdata(CONFIG_PATH, 'desired_cap', 'udid') + "/unlock"
        headers = {'Authorization': 'Bearer ' + getdata(CONFIG_PATH, 'adb_connect', 'token')
                   }
        r = requests.post(url, headers=headers)
        print(r.status_code)

    @staticmethod
    def connect_adb_api():
        url = "https://api-dev.headspin.io/v0/adb/" + getdata(CONFIG_PATH, 'desired_cap', 'udid') + "/connect"
        headers = {'Authorization': 'Bearer ' + getdata(CONFIG_PATH, 'adb_connect', 'token')
                   }
        r = requests.post(url, headers=headers)
        print(r.status_code)
        json_data = json.loads(r.text)
        serial = json_data['serial']
        return serial
