import time
import jenkins
import requests
import subprocess
from Constants.constants import CONFIG_PATH
from Constants.load_json import getdata
from Utilities.BasePage import BaseClass

baseClass = BaseClass()


class BuildFeatureJob():
    def __init__(self):
        j = jenkins.Jenkins('https://builds.byjus.com/', username='testautomation@byjus.com',
                            password='5a7b8f02aec0c2a7c5d4c348a1c7a590')
        branch_parameters = dict(branch='origin/feature/app2_phase3', env='staging', variant='ByjusPremium')
        j.build_job('B2C-Feature', parameters=branch_parameters, token='5a7b8f02aec0c2a7c5d4c348a1c7a590')
        time.sleep(10)
        while True:
            print('Running....')
            if j.get_job_info('B2C-Feature')['lastCompletedBuild']['number'] == j.get_job_info('B2C-Feature')['lastBuild'][
                'number']:
                print("Last ID %s, Current ID %s" % (j.get_job_info('B2C-Feature')['lastCompletedBuild']['number'],
                                                     j.get_job_info('B2C-Feature')['lastBuild']['number']))
                break
        time.sleep(3)
        print('Stop....')
        last_build_number = j.get_job_info('B2C-Feature')['lastCompletedBuild']['number']
        print("last_build_number", last_build_number)
        build_info = j.get_build_info('B2C-Feature', last_build_number)

        if build_info['result'] == 'SUCCESS':
            print("Build Success")
            artifact = build_info['artifacts'][0]
            artifact_displaypath = artifact['displayPath']
            apk_url = 'https://builds.byjus.com/job/B2C-Feature/' + str(last_build_number) + '/artifact/app/build/outputs/apk/ByjusPremium/release/' + artifact_displaypath
            r = requests.Request('GET', apk_url)
            response = j.jenkins_request(r)
            with open("app.apk", "wb") as f:
                f.write(response.content)

            baseClass.driverSetup()
            time.sleep(5)
            subprocess.Popen('adb connect ' + getdata(CONFIG_PATH, 'adb_connect', 'headspin_device'), shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
            time.sleep(2)
            val = subprocess.Popen('adb install -r ../../tests/step_def/app.apk', shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
            print("adb install status ", val)
            print(artifact_displaypath + " is installed successfully")

        else:
            print("Build Failed")
            log = j.get_build_console_output('B2C-Feature', last_build_number)
            f = open('log_buildFail.txt', 'w')
            f.write(log)
            f.close()
