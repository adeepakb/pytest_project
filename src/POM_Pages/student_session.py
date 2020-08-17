import logging
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from Utilities.tutor_common_methods import TutorCommonMethods
from src.Constants.load_json import getdata
from src.POM_Pages.application_login import Login
from Utilities.common_methods import CommonMethods

CommonMethods = CommonMethods()
class StudentSession:
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.action = TouchAction(driver)
        self.login = Login(driver)
        self.driver = driver
        self.dots_icon = '//*[contains(@resource-id, "loadingDots")]'
        self.tutor_icon = '//*[contains(@resource-id, "llTopicLyt")]/android.widget.ImageView'
        self.subject = '//*[contains(@resource-id, "tvTopicSubject")]'
        self.title = '//*[contains(@resource-id, "tvTopicTitle")]'
        self.student_white_board = '//*[contains(@resource-id, "WhiteBoard")]'
        self.student_video_icon = '//*[contains(@resource-id, "ivVideoImage")]'
        self.student_mic_icon = '//*[contains(@resource-id, "ivAudioImage")]'
        self.student_video_container = '//*[contains(@resource-id, "localVideoViewContainer")]/android.view.View'
        self.student_chat = '//*[@class = "android.widget.EditText"]'
        self.student_chat_dialog = '//*[contains(@resource-id, "textInputLayoutChat")]'
        self.student_chat_send = '//*[contains(@resource-id, "ivSendImage")]'
        self.student_chat_disabled = '//*[@text="LiveChat is disabled"]'
        self.chat_container = '//*[contains(@resource-id, "flChatViewLyt")]/android.webkit.WebView/android.webkit.WebView'
        self.profile_back_button = '//*[contains(@resource-id, "roundedNavButton")]'
        self.teaching_material_slide_image = '//android.view.View[2]/android.view.View/android.widget.Image'
        self.tutor_video_container = '//*[contains(@resource-id, "remoteVideoViewContainer")]'
        self.bottom_sheet_dialog = '//*[contains(@resource-id, "design_bottom_sheet")]'
        self.dialog_layout = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/dialog_layout"]'
        self.bottom_dialog_title = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/tvTitle"]'
        self.bottom_dialog_cancel = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/tvCancel"]'
        self.custom_panel = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/customPanel"]'
        self.custom_panel_download = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/download_button"]'
        self.tutor_video_container_status = '//*[contains(@resource-id, "remoteVideoViewContainer")]/android.view.View'

    def verify_button(self, text):
        self.obj.is_button_displayed(text)
        self.obj.is_button_enabled(text)

    def is_dots_icon_displayed(self):
        data_off_icon_displayed = self.obj.get_element('xpath', self.dots_icon).is_displayed()
        is_enabled = self.obj.get_element('xpath', self.dots_icon).is_enabled()
        if data_off_icon_displayed and is_enabled:
            return True
        return False

    def is_tutor_icon_displayed(self):
        tutor_icon_displayed = self.obj.get_element('xpath', self.tutor_icon).is_displayed()
        is_enabled = self.obj.get_element('xpath', self.tutor_icon).is_enabled()
        if tutor_icon_displayed and is_enabled:
            return True
        return False

    def verify_subject_name(self, subject_value):
        subject = self.driver.find_element_by_xpath(self.subject).text
        assert subject == subject_value, 'Subject name is not correct'

    def verify_chapter_name(self, topic_title):
        chapter = self.driver.find_element_by_xpath(self.title).text
        print(chapter)
        assert topic_title in chapter, 'Chapter name is not correct'

    def is_white_board_present(self):
        return self.obj.is_element_present('xpath', self.student_white_board)

    def is_student_video_icon_enabled(self):
        is_enabled = self.obj.get_element('xpath', self.student_video_icon).get_attribute("clickable")
        return is_enabled

    def is_student_mic_option_enabled(self):
        is_enabled = self.obj.get_element('xpath', self.student_mic_icon).get_attribute("clickable")
        return is_enabled

    def is_student_video_screen_present(self):
        return self.obj.is_element_present('xpath', self.student_video_container)

    def is_student_chat_enabled(self):
        if self.obj.is_element_present('xpath', self.student_chat) and not (
                self.obj.is_element_present('xpath', self.student_chat_disabled)):
            return True
        else:
            return False

    def tap_on_chat_textbox(self):
        self.obj.get_element('xpath', self.student_chat).click()

    def verify_student_chat_dialog(self):
        return self.obj.is_element_present('xpath', self.student_chat_dialog)

    def tap_on_chat_dialog(self):
        self.obj.get_element('xpath', self.student_chat_dialog).click()

    def click_back(self):
        self.obj.click_back()

    def is_keyboard_shown(self):
        assert self.obj.is_keyboard_shown(), "Device keypad not enabled"

    def enter_text_in_chat(self, message):
        self.obj.get_element('xpath', self.student_chat).send_keys(message)

    def verify_entered_chat(self, message):
        assert message == self.obj.get_element('xpath', self.student_chat).text, "Chat text verification failed"

    def tap_on_chat_send(self):
        self.obj.get_element('xpath', self.student_chat_send).click()

    def verify_student_sent_text(self, message):
        self.obj.is_element_present('xpath', '//android.view.View[@text="' + message + '"]')

    def is_student_sent_text_visible(self, message):
        return self.obj.get_element('xpath', '//android.view.View[@text="' + message + '"]').is_displayed()

    def reset_and_login_with_otp(self):
        self.obj.execute_command('adb shell pm clear com.byjus.tutorplus')
        self.obj.execute_command('adb shell monkey -p com.byjus.tutorplus -c android.intent.category.LAUNCHER 1')
        self.login.allow_deny_permission(["Allow", "Allow", "Allow"])
        self.login.enter_reg_mobile_number()
        self.login.click_on_next()
        self.login.enter_otp()
        self.download_materials_for_session()
        self.cancel_join_session_dialog()

    # navigate to home page and verify student profile.
    # If not the expected user, reset and login
    def verify_student_profile(self):
        profile_name = None
        self.download_materials_for_session()
        self.cancel_join_session_dialog()
        try:
            if self.obj.is_element_present('xpath', '//*[contains(@resource-id, "ClassroomAvatarImg")]'):
                self.obj.get_element('xpath', '//*[contains(@resource-id, "ClassroomAvatarImg")]').click()
                expected_mobile_number = self.obj.get_element('xpath',
                                                              '//*[contains(@resource-id, "mobile_number")]').text
                profile_name = self.obj.get_element('xpath', '//*[contains(@resource-id, "tvName")]').text
                account_details = '../../config/config.json'
                actual_mobile_number = str(getdata(account_details, 'account_details', 'mobile'))

                if expected_mobile_number == actual_mobile_number:
                    logging.info('classroom page verified')
                    self.obj.get_element('xpath', self.profile_back_button).click()
                else:
                    logging.info('Not expected user')
                    self.reset_and_login_with_otp()
            else:
                self.reset_and_login_with_otp()
        except:
            logging.info('Error in verifying classroom page')
        return profile_name

    def speed_test(self):
        try:
            if self.obj.is_text_match("Speedtest"):
                self.obj.wait_for_locator('xpath', '//*[contains(@resource-id, "btButton")]', 15)
                if self.obj.is_element_present('xpath', '//*[contains(@resource-id, "btButton")]'):
                    self.obj.get_element('xpath', '//*[contains(@resource-id, "btButton")]').click()
            else:
                pass
        except (StaleElementReferenceException, NoSuchElementException):
            pass

    def tap_on_cancel(self):
        self.obj.get_element('xpath', '//*[contains(@resource-id, "secondaryAction")]').click()

    def verify_offline_dialog_disappeared(self):
        self.obj.wait_for_invisibility_of_element('xpath', '//*[contains(@resource-id, "dialog_layout")]')

    def is_teaching_material_present(self):
        self.obj.wait_for_locator('xpath', self.teaching_material_slide_image)
        img_src_text = self.obj.get_element('xpath', self.teaching_material_slide_image).text
        assert img_src_text is not None, "teaching material slide is not present in student screen"

    def tap_on_video_icon(self):
        self.obj.wait_for_locator('xpath', self.student_video_icon)
        self.obj.get_element('xpath', self.student_video_icon).click()

    def tap_on_audio_mic_icon(self):
        self.obj.wait_for_locator('xpath', self.student_mic_icon)
        self.obj.get_element('xpath', self.student_mic_icon).click()

    def is_tutor_video_muted_and_black_screen_displayed(self, rgb_color_code):
        self.obj.verify_element_color('xpath', self.tutor_video_container, rgb_color_code, 0)

    def tap_on_disabled_chat(self):
        self.obj.get_element('xpath', self.student_chat_disabled).click()

    def scroll_chat_container(self):
        el = self.obj.get_element('xpath', self.chat_container)
        start_x = el.location['x'] + (el.size['width'] / 2)
        start_y = el.location['y'] + el.size['height']
        end_y = el.location['y']
        self.action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()

    def verify_shapes_in_student_whiteboard(self):
        self.obj.wait_for_locator('xpath', self.student_white_board)
        element = self.obj.get_element('xpath', self.student_white_board)
        shapes_list = self.obj.detect_shapes(element)
        expected_shapes_list = ['circle', 'square', 'rectangle', 'triangle']
        assert (set(shapes_list) == set(expected_shapes_list)), "All shapes are not detected in student session"

    def get_text_from_image_and_verify(self, text):
        self.obj.wait_for_locator('xpath', self.student_white_board)
        element = self.obj.get_element('xpath', self.student_white_board)
        self.obj.capture_screenshot(element, 'verify_tutor_canvas_text')
        img_text = self.obj.get_text_from_image('verify_tutor_canvas_text')
        assert (text == img_text), "tutor text message is not displayed on white screen"

    def verify_colors_in_student_whiteboard(self):
        self.obj.wait_for_locator('xpath', self.student_white_board)
        colors = self.obj.get_all_colors_present('xpath', self.student_white_board)
        expected_colors_list = [(51, 51, 51), (41, 134, 255), (234, 126, 0), (233, 29, 41), (0, 200, 83)]
        all_color_codes = [color for (_, color) in colors]
        match = None
        for i in range(5):
            flag = False
            for j in range(len(all_color_codes)):
                match = self.obj.root_mean_square_error(expected_colors_list[i], all_color_codes[j])
                if match < 15:
                    flag = True
                    print(match)
                    break
            assert (flag is True), "Text color " + expected_colors_list[i] + " is not as expected"

    def cancel_join_session_dialog(self):
        device = CommonMethods.get_device_type(self.driver)
        if device == 'tab':
            if self.obj.is_element_present('xpath', self.bottom_sheet_dialog):
                self.obj.element_click('xpath', self.bottom_dialog_cancel)
        elif device == 'mobile':
            if self.obj.is_element_present('xpath', self.dialog_layout):
                self.obj.element_click('xpath', self.bottom_dialog_cancel)
        else:
            logging.info("Failed in Method cancel_join_session_dialog")

    def download_materials_for_session(self):
        if self.obj.is_element_present('xpath', self.custom_panel):
            self.obj.element_click('xpath', self.custom_panel_download)
            self.login.wait_for_element_not_to_be_present('//*[contains(@resource-id, "messageTv")]',20)
        else:
            pass

    def check_camera_turned_on_or_off(self, text):
        if text == 'OFF':
            assert not self.obj.is_element_present('xpath',
                                                   self.tutor_video_container_status), "Camera access is not off"
        elif text == 'ON':
            assert self.obj.is_element_present('xpath', self.tutor_video_container_status), "Camera access is not on"
