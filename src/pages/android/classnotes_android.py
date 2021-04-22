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
        self.toast = '//android.widget.Toast'
        self.dialog_layout = f'{package_name}/dialog_layout'
        self.dialog_title = f'{package_name}/dialog_title'

    def is_classnote_icon_present(self):
        return self.obj.is_element_present('id', self.classNotesImg)

    def is_download_icon_present(self):
        return self.obj.is_element_present('id', self.arrow_btn)

    def tap_on_first_session_card(self):
        session_cards_list = self.obj.get_elements('id', self.session_header)
        card = session_cards_list[0]
        card.click()

    def is_requisite_list(self):
        self.obj.wait_for_locator('id', self.requisite_list)
        return self.obj.is_element_present('id', self.requisite_list)

    def click_on_download(self):
        self.obj.wait_for_locator('id', self.arrow_btn)
        self.obj.element_click('id', self.arrow_btn)
        # self.obj.wait_for_invisibility_of_element('id', self.classnotes_size, 20)

    def classnote_processing(self):
        self.obj.wait_for_locator('id', self.processing)
        return self.obj.is_element_present('id', self.processing)

    def is_assets_in_pdf_format(self):
        files = self.obj.execute_command('adb shell ls /storage/emulated/0/Download')[0]
        for file in files.split(b'\n')[:-1]:
            if file.endswith(b'.pdf'):
                return ReturnType(True, 'Downloaded material is in pdf format')
            else:
                return ReturnType(False, 'Downloaded material is not in pdf format')

    def all_tagged_resource_types(self):
        self.obj.is_text_match('Session Details')
        self.obj.is_text_match('Revision Material')
        sessions = self.obj.get_elements('id', self.post_req_session)
        titles = self.obj.get_elements('id', self.title)
        items = ["ClassNote", "K12 video", "Journey"]
        for title in titles:
            print(title.text)
        count = 0
        for i in range(0, 3):
            title = titles[i].text
            if (title == items[i]) and sessions[i].is_enabled():
                count += 1
        if count == 3:
            return ReturnType(True, 'Verify all tagged resources are present')
        else:
            return ReturnType(False, 'Verify all tagged resources are not present')

    def verify_classnotes_present_to_download(self):
        titles = self.obj.get_elements('id', self.requisite_title)
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
        for app in open_with_apps:
            if app.text in ["Drive PDF Viewer", "OneDrive PDF Viewer"] and panel_title == 'Open with':
                app.click()
                return ReturnType(True, 'User was asked to select pdf viewer to open')
            else:
                return ReturnType(False, 'User was not asked to select pdf viewer to open')

    def verify_pdf_viewer_options(self):
        req_contents = self.obj.get_elements('id', self.req_content)
        for card in req_contents:
            self.obj.child_element_by_id(card, self.arrow_btn).click()
            break
        return self.verify_or_select_pdf_viewer()

    def tap_classnotes_forward_icon_and_verify(self):
        req_contents = self.obj.get_elements('id', self.req_content)
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
        share_apps = self.obj.get_elements('id', self.app_name)
        for app in share_apps:
            if app.text == "Save to Drive":
                app.click()
                self.obj.button_click('Save')
                if self.obj.get_element('xpath', self.toast).text == "Your 1 file is being uploaded to: My Drive":
                    return ReturnType(True, 'pdf share file successful')
                else:
                    return ReturnType(False, 'pdf share file not successful')

    def verify_no_pdf_viewer_message(self):
        req_contents = self.obj.get_elements('id', self.req_content)
        for card in req_contents:
            self.obj.child_element_by_id(card, self.arrow_btn).click()
            break
        if (self.obj.is_element_present('id', self.dialog_layout) and
                self.obj.get_element_text('id', self.dialog_title) == 'No application available to open this file' and
                self.obj.is_button_displayed('Go to Play Store') and
                self.obj.is_text_match('Cancel')):
            return ReturnType(True, 'Message displayed when no pdf viewer is present to open file')
        else:
            return ReturnType(False, 'No message displayed when no pdf viewer is present to open file')

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

    def install_pdf_reader_apps(self):
        self.install_app('com.microsoft.skydrive.apk')
        self.install_app('com.trustedapp.pdfreaderpdfviewer.apk')