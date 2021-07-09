import json
import os
import time
import jenkins
import requests
import subprocess
from constants.load_json import get_data
from cryptography.fernet import Fernet
key = os.getenv('SECRET')
f = Fernet(key)
encrypted_data = get_data('../config/config.json', 'encrypted_data', 'token')
decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))
udid = decrypted_data['desired_cap']['udid']
token = decrypted_data['adb_connect']['token']


class BuildFeatureJob():
    # def __init__(self):
    #
    #     branch = os.getenv('branch')
    #     env = os.getenv('env')
    #     variant = os.getenv('variant')
    #
    #     j = jenkins.Jenkins('https://builds.byjus.com/',
    #                         username='reshma.nair@byjus.com', password='1d4b7f1a039c21beef54b2a861aeb8f9')
    #     branch_parameters = dict(branch=branch, env=env, variant=variant)
    #     j.build_job('B2C-Feature', parameters=branch_parameters, token='1d4b7f1a039c21beef54b2a861aeb8f9')
    #     time.sleep(10)
    #     print("B2C Feature job started running branch %s env %s variant %s" % (branch, env, variant))
    #     while True:
    #         if j.get_job_info('B2C-Feature')['lastCompletedBuild']['number'] == \
    #                 j.get_job_info('B2C-Feature')['lastBuild'][
    #                     'number']:
    #             print("Last ID %s, Current ID %s" % (j.get_job_info('B2C-Feature')['lastCompletedBuild']['number'],
    #                                                  j.get_job_info('B2C-Feature')['lastBuild']['number']))
    #             break
    #         time.sleep(10)
    #     last_build_number = j.get_job_info('B2C-Feature')['lastCompletedBuild']['number']
    #     # last_build_number = 2224
    #     build_info = j.get_build_info('B2C-Feature', last_build_number)
    #
    #     if build_info['result'] == 'SUCCESS':
    #         print("B2C-Feature Build %d is Successful" % last_build_number)
    #         log = j.get_build_console_output('B2C-Feature', last_build_number)
    #         print(log)
    #         artifact = build_info['artifacts'][0]
    #         artifact_displaypath = artifact['displayPath']
    #         apk_url = 'https://builds.byjus.com/job/B2C-Feature/' + str(
    #             last_build_number) + '/artifact/app/build/outputs/apk/ByjusPremium/release/' + artifact_displaypath
    #         r = requests.Request('GET', apk_url)
    #         response = j.jenkins_request(r)
    #         print("Downloading latest apk ", apk_url)
    #         with open("app.apk", "wb") as f:
    #             f.write(response.content)
    #
    #         self.lock_or_unlock_device('lock')
    #         serial = self.connect_adb_api()
    #         self.connect_to_adb(serial)
    #
    #         print("Installing latest apk ", apk_url)
    #         stdout, stderr = subprocess.Popen('adb install -r ../../tests/step_def/app.apk', shell=True,
    #                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
    #         output = stdout.decode("ascii")
    #         if "Success" not in output or "1 file pushed." not in output:
    #             raise Exception("Failed to install app due to error %s" % output)
    #         print("latest apk installed successfully " + artifact_displaypath)
    #         subprocess.Popen('adb disconnect ' + serial, shell=True, stdout=subprocess.PIPE,
    #                          stderr=subprocess.STDOUT).communicate()
    #         self.lock_or_unlock_device('unlock')
    #
    #     else:
    #         print("B2C-Feature latest build Failed")
    #         log = j.get_build_console_output('B2C-Feature', last_build_number)
    #         f = open('log_buildFail.txt', 'w')
    #         f.write(log)
    #         f.close()


    # build b2c feature job for app2 apk, download artifact ,connect to headspin device and install apk on it
    def build_and_install_apk(self):
        branch = os.getenv('branch')
        env = os.getenv('env')
        variant = os.getenv('variant')

        j = jenkins.Jenkins('https://builds.byjus.com/',
                            username='reshma.nair@byjus.com', password='1d4b7f1a039c21beef54b2a861aeb8f9')
        branch_parameters = dict(branch=branch, env=env, variant=variant)
        j.build_job('B2C-Feature', parameters=branch_parameters, token='1d4b7f1a039c21beef54b2a861aeb8f9')
        time.sleep(10)
        print("B2C Feature job started running branch %s env %s variant %s" % (branch, env, variant))
        while True:
            if j.get_job_info('B2C-Feature')['lastCompletedBuild']['number'] == \
                    j.get_job_info('B2C-Feature')['lastBuild'][
                        'number']:
                print("Last ID %s, Current ID %s" % (j.get_job_info('B2C-Feature')['lastCompletedBuild']['number'],
                                                     j.get_job_info('B2C-Feature')['lastBuild']['number']))
                break
            time.sleep(10)
        last_build_number = j.get_job_info('B2C-Feature')['lastCompletedBuild']['number']
        # last_build_number= 2248
        build_info = j.get_build_info('B2C-Feature', last_build_number)

        if build_info['result'] == 'SUCCESS':
            print("B2C-Feature Build %d is Successful" % last_build_number)
            log = j.get_build_console_output('B2C-Feature', last_build_number)
            print(log)
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
            stdout, stderr = subprocess.Popen('adb install -r ../../tests/step_def/app.apk', shell=True,
                                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
            output = stdout.decode("ascii")
            if "Success" not in output or "1 file pushed." not in output:
                raise Exception("Failed to install app due to error %s" % output)
            print("latest apk installed successfully " + artifact_displaypath)
            subprocess.Popen('adb disconnect ' + serial, shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT).communicate()
            self.lock_or_unlock_device('unlock')

        else:
            print("B2C-Feature latest build Failed")
            log = j.get_build_console_output('B2C-Feature', last_build_number)
            f = open('log_buildFail.txt', 'w')
            f.write(log)
            f.close()

    # adb connect to headspin device
    @staticmethod
    def connect_to_adb(serial):
        connected = False
        for i in range(5):
            subprocess.Popen('adb connect ' + serial, shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT).communicate()
            stdout, stderr = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE,
                                              stderr=subprocess.STDOUT).communicate()
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

    # to lock or unlock the headspin device
    @staticmethod
    def lock_or_unlock_device(flag):
        if flag == 'lock':
            url = "https://api-dev.headspin.io/v0/adb/" + udid + "/lock"
        else:
            url = "https://api-dev.headspin.io/v0/adb/" + udid + "/unlock"
        headers = {'Authorization': 'Bearer ' + token
                   }
        r = requests.post(url, headers=headers)
        if r.status_code == 200:
            print("headspin device %s successful" %flag)

    # to call the connect API to get the current port number details and host
    @staticmethod
    def connect_adb_api():
        url = "https://api-dev.headspin.io/v0/adb/" + udid + "/connect"
        headers = {'Authorization': 'Bearer ' + token
                   }
        r = requests.post(url, headers=headers)
        if r.status_code == 200:
            print("adb api connect successful")
        json_data = json.loads(r.text)
        serial = json_data['serial']
        return serial
