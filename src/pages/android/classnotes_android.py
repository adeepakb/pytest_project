import os
import re
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from pages.android.login_android import LoginAndroid
from pages.base.classnotes_base import ClassNotesBase
from utilities.staging_tlms import Stagingtlms
from utilities.tutor_common_methods import TutorCommonMethods
import subprocess


class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class ClassNotesAndroid(ClassNotesBase):
    def __init__(self, driver):
        self.driver = driver
        self.login = LoginAndroid(driver)
        self.action = TouchAction(driver)
        self.tlms = Stagingtlms(driver)
        self.obj = TutorCommonMethods(driver)
        package_name = self.driver.capabilities['appPackage'] + ':id'
        self.classNotesImg = f'{package_name}/classNotesImg'
        self.session_header = f'{package_name}/session_header'
        self.requisite_list = f'{package_name}/requisite_item_list'
        self.classnotes_size = f'{package_name}/classnotesSize'
        self.requisite_title = f'{package_name}/tvRequisiteTitle'
        self.title = f'{package_name}/tvTitle'
        self.classnotes_img = f'{package_name}/classNotesImg'
        self.arrow_btn = f'{package_name}/arrow_btn'
        self.new_tag = f'{package_name}/classnotesNewTag'
        self.processing = f'{package_name}/downloadingProgressbar'
        self.post_req_session = f'{package_name}/cvSession'
        self.req_content = f'{package_name}/llRequisiteContentLyt'
        self.more_options = '//android.widget.ImageView[@content-desc="More options"]'
        self.pdf_view = 'com.google.android.apps.docs:id/pdf_view'
        self.app_name = 'android:id/text1'
        self.sem_title = 'android:id/sem_title_default'
        self.dialog_layout = f'{package_name}/dialog_layout'
        self.dialog_title = f'{package_name}/dialog_title'
        self.save_button = 'android:id/button1'
        self.save_to_drive_title = "com.google.android.apps.docs:id/title"

    def is_classnote_icon_present(self):
        if self.obj.is_element_present('id', self.classNotesImg):
            return ReturnType(True, 'classnote icon beside class-note text is present')
        else:
            return ReturnType(False, 'classnote icon beside class-note text is not present')

    def is_download_icon_present(self):
        if self.obj.is_element_present('id', self.arrow_btn):
            return ReturnType(True, 'classnote Download button is present')
        else:
            return ReturnType(False, 'classnote Download button is not present')

    def tap_on_first_session_card(self):
        session_cards_list = self.obj.get_elements('id', self.session_header)
        if len(session_cards_list) == 0:
            raise Exception("No cards present in booking screen")
        card = session_cards_list[0]
        card.click()

    def is_requisite_list(self):
        try:
            self.obj.wait_for_locator('id', self.requisite_list)
            if self.obj.is_element_present('id', self.requisite_list):
                return ReturnType(True, 'requisite is displayed')
        except NoSuchElementException:
            return ReturnType(False, 'requisite is not displayed')

    def click_on_download(self):
        self.obj.wait_for_locator('id', self.arrow_btn)
        self.obj.element_click('id', self.arrow_btn)
        # self.obj.wait_for_invisibility_of_element('id', self.classnotes_size, 20)

    def classnote_processing(self):
        self.obj.wait_for_locator('id', self.processing)
        if self.obj.is_element_present('id', self.processing):
            return ReturnType(True, 'File is processing')
        else:
            return ReturnType(False, 'File is not processing')

    def is_assets_in_pdf_format(self):
        files = self.obj.execute_command('adb shell ls /storage/emulated/0/Download')[0]
        print(len(files))
        if len(files) is 0:
            return ReturnType(False, 'Class note was not downloaded')
        for file in files.split(b'\n')[:-1]:
            if file.endswith(b'.pdf'):
                return ReturnType(True, 'Downloaded material is in pdf format')
            elif not file.endswith(b'.pdf'):
                return ReturnType(False, 'Downloaded material is not in pdf format')

    def all_tagged_resource_types(self):
        try:
            sessions = self.obj.get_elements('id', self.post_req_session)
            titles = self.obj.get_elements('id', self.title)
            if len(sessions) == 0 or len(titles) == 0:
                raise Exception("Under Completed tab, post requisite card is not present")
            items = ["ClassNote", "K12 video", "Journey"]
            for title in titles:
                print(title.text)
            count = 0
            for i in range(0, 3):
                title = titles[i].text
                if (title == items[i]) and sessions[i].is_enabled():
                    count += 1
            if count == 3:
                return ReturnType(True, 'All 3 tagged resources are present in app')
            else:
                return ReturnType(False, "3 resources are tagged in cms, but only %d resources are present" % count)
        except NoSuchElementException:
            return ReturnType(False, 'post requisite sessions are not present')

    def verify_classnotes_present_to_download(self):
        titles = self.obj.get_elements('id', self.requisite_title)
        if len(titles) == 0:
            raise Exception("post requisite card is not present")
        classnotes_size = self.obj.get_element_text('id', self.classnotes_size)
        m = re.match("([0-9]|1[1-5]) MB", classnotes_size)
        if (titles[0].text == 'ClassNote') and self.obj.is_element_present('id', self.arrow_btn) and (
                m is not None):
            return ReturnType(True, 'Class Note card is present and Pdf size displayed below the down Arrow Button')
        else:
            return ReturnType(False,
                              'Class Note card is not present and Pdf size displayed below the down Arrow Button')

    def verify_forward_icon_present(self):
        req_cards = self.obj.get_elements('id', self.req_content)
        if len(req_cards) == 0:
            raise Exception("post requisite card is not present")
        for card in req_cards:
            try:
                if self.obj.child_element_by_id(card, self.arrow_btn).is_enabled():
                    return ReturnType(True, 'Forward icon is present for downloaded class notes')
            except NoSuchElementException:
                return ReturnType(False, 'Forward icon is not present for downloaded class notes')

    def verify_or_select_pdf_viewer(self):
        self.obj.wait_for_locator('id', self.sem_title)
        panel_title = self.obj.get_element('id', self.sem_title).text
        open_with_apps = self.obj.get_elements('id', self.app_name)
        if len(open_with_apps) == 0:
            raise Exception("Select pdf viewer panel is not present")
        for app in open_with_apps:
            if panel_title == 'Open with':
                if app.text in ["Drive PDF Viewer", "OneDrive PDF Viewer"]:
                    app.click()
                    return ReturnType(True, 'User was asked to select pdf viewer from options to open file')
                else:
                    return ReturnType(False, 'PDF viewer options are not shown to user')
            else:
                return ReturnType(False, '"Open with" title is not present in the panel')

    def verify_pdf_viewer_options(self):
        req_contents = self.obj.get_elements('id', self.req_content)
        if len(req_contents) == 0:
            raise Exception("post requisite card is not present")
        for card in req_contents:
            self.obj.child_element_by_id(card, self.arrow_btn).click()
            break
        return self.verify_or_select_pdf_viewer()

    def tap_classnotes_forward_icon_and_verify(self):
        req_contents = self.obj.get_elements('id', self.req_content)
        if len(req_contents) == 0:
            raise Exception("post requisite card is not present")
        for card in req_contents:
            self.obj.child_element_by_id(card, self.arrow_btn).click()
            self.verify_or_select_pdf_viewer()
            try:
                self.obj.is_element_present('id', self.pdf_view)
                return ReturnType(True, 'pdf file did open')
            except NoSuchElementException:
                return ReturnType(False, 'pdf file did not open')

    def click_on_pdf_download_option(self):
        self.obj.wait_for_locator('xpath', self.more_options)
        self.obj.element_click('xpath', self.more_options)
        self.obj.click_link('Download')

    def verify_share_file_options(self):
        self.obj.element_click('xpath', self.more_options)
        self.obj.click_link('Send file…')
        self.obj.wait_for_locator('id', self.app_name)
        share_apps = self.obj.get_elements('id', self.app_name)
        if len(share_apps) == 0:
            raise Exception("Share via app option is not present")
        for app in share_apps:
            if app.text == "Save to Drive" or app.text == "Drive":
                app.click()
                self.obj.wait_for_locator('id', self.save_to_drive_title)
                self.driver.back()
                self.obj.element_click('id', self.save_button)
                upload_check_limit = 15  # Avoided using while True condition or hardcoded wait time
                while upload_check_limit > 0:
                    if self.obj.is_android_notification_present('Uploading 1 file'):
                        upload_check_limit -= 1
                        continue
                    if self.obj.is_android_notification_present('Uploaded 1 file'):
                        self.obj.click_back()
                        return ReturnType(True, 'PDF uploaded to Drive')
                    self.obj.click_back()
                    return ReturnType(False, 'PDF uploaded message is not present')

    def verify_no_pdf_viewer_message(self):
        req_contents = self.obj.get_elements('id', self.req_content)
        if len(req_contents) == 0:
            raise Exception("post requisite card is not present")
        for card in req_contents:
            self.obj.child_element_by_id(card, self.arrow_btn).click()
            break
        if (self.obj.is_element_present('id', self.dialog_layout) and
                self.obj.get_element_text('id',
                                          self.dialog_title) == 'No application available to open this file' and
                self.obj.is_button_displayed('Go to Play Store') and
                self.obj.is_text_match('Cancel')):
            return ReturnType(True, 'Message displayed when no pdf viewer is present to open file')
        elif not (self.obj.is_element_present('id', self.dialog_layout)):
            return ReturnType(False, 'Dialog layout is not present when no pdf viewer app is present in the device')
        elif not (
                self.obj.get_element_text('id', self.dialog_title) == 'No application available to open this file'):
            return ReturnType(False, 'No application available to open this file message is not displayed')
        elif not (self.obj.is_button_displayed('Go to Play Store')):
            return ReturnType(False, 'Go to Play Store message is not displayed')
        elif not (self.obj.is_text_match('Cancel')):
            return ReturnType(False, 'Cancel button is not present in the panel')

    def login_to_cms_staging(self):
        self.tlms.login_to_cms_staging()

    def upload_class_note_morethan_15mb(self):
        self.tlms.upload_class_note('ClassNotesPDF.pdf')

    def verify_classnote_upload_error(self):
        if self.tlms.verify_classnote_upload_error() is True:
            return ReturnType(True, 'Error message is displayed when classnotes pdf is more than 15 MB')
        else:
            return ReturnType(False, 'Error message is not displayed when classnotes pdf is more than 15 MB')

    def upload_incorrect_format_class_note(self):
        self.tlms.upload_class_note('ClassNotesPNG.png')

    def incorrect_note_format_error(self):
        if self.tlms.incorrect_note_format_error() is True:
            return ReturnType(True, 'Error message is displayed when uploaded classnotes is in png format')
        else:
            return ReturnType(False, 'Error message is not displayed when uploaded classnotes is in png format')

    def update_post_requisite_class_note(self, requisite_name, class_note_id):
        self.tlms.update_post_requisite_class_note(requisite_name, class_note_id)

    def uninstall_pdf_reader_apps(self):
        self.driver.remove_app("com.trustedapp.pdfreaderpdfviewer")
        self.driver.remove_app("com.microsoft.skydrive")

    def install_app(self, apk):
        current_location = os.path.dirname(os.path.abspath(__file__))
        location = os.path.normpath(os.path.join(current_location, "../../../files/" + apk + ""))
        stdout, stderr = subprocess.Popen('adb install -r ' + location + '', shell=True, stdout=subprocess.PIPE,
                                          stderr=subprocess.STDOUT).communicate()
        output = stdout.decode("ascii")
        print(output)
        if "Success" not in output:
            raise Exception("Failed to install app due to error %s" % output)

    # def install_pdf_reader_apps(self):
    #     self.install_app('com.microsoft.skydrive.apk')
    #     self.install_app('com.trustedapp.pdfreaderpdfviewer.apk')