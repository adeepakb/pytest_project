from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from pom_pages.base_pages.student_session_base import StudentSessionBase
from utilities.tutor_common_methods import TutorCommonMethods
from pom_pages.android_pages.login_android import LoginAndroid
from utilities.common_methods import CommonMethods

CommonMethods = CommonMethods()

featureFileName = "Session Flow"


class StudentSessionAndroid(StudentSessionBase):
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.action = TouchAction(driver)
        self.login = LoginAndroid(driver)
        self.driver = driver
        self.dots_icon = '//*[contains(@resource-id, "loadingDots")]'
        self.tutor_icon = '//*[contains(@resource-id, "llTopicLyt")]/android.widget.ImageView'
        self.subject = '//*[contains(@resource-id, "tvTopicSubject")]'
        self.title = '//*[contains(@resource-id, "tvTopicTitle")]'
        self.exo_content = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/exo_content_frame"]'
        self.exo_overlay = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/exo_overlay"]'
        self.player_view = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/player_view"]'
        self.show_chat = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/fbShowChatBtn"]'
        self.student_chat = '//*[@class = "android.widget.EditText"]'
        self.student_chat_dialog = '//*[contains(@resource-id, "textInputLayoutChat")]'
        self.student_chat_send = '//*[contains(@resource-id, "ivSendImage")]'
        self.chat_container = '//*[contains(@resource-id, "flChatViewLyt")]/android.webkit.WebView/android.webkit.WebView'
        self.chat_close_icon = '//*[contains(@resource-id, "flChatViewLyt")]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.widget.Image'
        self.profile_back_button = '//*[contains(@resource-id, "roundedNavButton")]'
        self.dialog_layout = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/dialog_layout"]'
        self.live_chat_header = "//android.view.View[@text='Live Chat']"
        self.chat_popup = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/etChatInputText"]'
        self.student_chat_disabled = '//*[@text="Live Chat is disabled"]'
        self.exo_pause = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/exo_pause"]'
        self.exo_play = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/exo_play"]'
        self.exo_progress_bar = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/exo_progress"]'
        self.join_now = 'com.byjus.thelearningapp.premium:id/card_strip_btn'

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

    def is_student_chat_enabled(self):
        if self.obj.is_element_present('xpath', self.student_chat) and not (
                self.obj.is_element_present('xpath', self.student_chat_disabled)):
            return True
        else:
            return False

    def tap_on_disabled_chat(self):
        self.obj.wait_for_locator('xpath', self.student_chat_disabled)
        self.obj.get_element('xpath', self.student_chat_disabled).click()

    def is_chat_icon_displayed(self):
        self.obj.wait_for_locator('xpath', self.show_chat)
        return self.obj.is_element_present('xpath', self.show_chat)

    def is_live_chat_displayed(self):
        self.obj.wait_for_locator('xpath', self.live_chat_header)
        return self.obj.is_element_present('xpath', self.live_chat_header)

    def is_chat_close_icon_displayed(self):
        self.obj.wait_for_locator('xpath', self.chat_close_icon)
        return self.obj.is_element_present('xpath', self.chat_close_icon)

    def tap_on_chat_icon(self):
        self.obj.wait_for_locator('xpath', self.show_chat)
        self.obj.get_element('xpath', self.show_chat).click()

    def tap_on_join_now(self):
        self.obj.wait_for_locator('id', self.join_now)
        self.obj.get_element('id', self.join_now).click()

    def close_chat(self):
        self.obj.wait_for_locator('xpath', self.chat_close_icon)
        self.obj.get_element('xpath', self.chat_close_icon).click()

    def tap_on_chat_textbox(self):
        self.obj.wait_for_locator('xpath', self.student_chat)
        self.obj.get_element('xpath', self.student_chat).click()

    def tap_outside_dialog_layout(self):
        self.action.tap(None, x=100, y=100).release().perform()

    def video_elements_present(self):
        self.obj.wait_for_locator('xpath', self.player_view, 10)
        return self.obj.is_element_present('xpath', self.player_view) and \
               self.obj.is_element_present('xpath', self.exo_content) and \
               self.obj.is_element_present('xpath', self.exo_overlay)

    def verify_student_chat_dialog(self):
        return self.obj.is_element_present('xpath', self.student_chat_dialog)

    def tap_on_chat_dialog(self):
        self.obj.wait_for_locator('xpath', self.student_chat_dialog)
        self.obj.get_element('xpath', self.student_chat_dialog).click()

    def is_emoji_present(self):
        return self.obj.is_element_present('xpath', "//*[@class='emoji']")

    def is_cursor_present(self):
        is_element_focused = self.obj.get_element('xpath', self.chat_popup).get_attribute('focused')
        return is_element_focused

    def click_back(self):
        self.obj.click_back()

    def is_keyboard_shown(self):
        assert self.obj.is_keyboard_shown(), "Device keypad not enabled"

    def enter_text_in_chat(self, message):
        self.obj.wait_for_locator('xpath', self.student_chat)
        self.obj.get_element('xpath', self.student_chat).send_keys(message)

    def verify_entered_chat(self, message):
        assert message == self.obj.get_element('xpath', self.student_chat).text, "Chat text verification failed"

    def tap_on_chat_send(self):
        self.obj.wait_for_locator('xpath', self.student_chat_send)
        self.obj.get_element('xpath', self.student_chat_send).click()

    def verify_message_at_student_side(self, message):
        # self.obj.is_element_present('xpath', '//android.view.View[@text="' + message + '"]')
        text_present = False
        for element in self.obj.get_elements('xpath', '//android.view.View'):
            view_text = element.text
            if message in view_text:
                text_present = True
                break
        return text_present

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
        self.obj.wait_for_locator('xpath', '//*[contains(@resource-id, "secondaryAction")]')
        self.obj.get_element('xpath', '//*[contains(@resource-id, "secondaryAction")]').click()

    def verify_offline_dialog_disappeared(self):
        self.obj.wait_for_invisibility_of_element('xpath', '//*[contains(@resource-id, "dialog_layout")]')

    def scroll_chat_container(self):
        el = self.obj.get_element('xpath', self.chat_container)
        start_x = el.location['x'] + (el.size['width'] / 2)
        start_y = el.location['y'] + el.size['height']
        end_y = el.location['y']
        self.action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()

    def is_video_play_present(self):
        return self.obj.is_element_present('id', self.exo_play)

    def is_video_pause_progress_bar_present(self):
        return self.obj.is_element_present('id', self.exo_pause)

    def is_video_progress_bar_present(self):
        return self.obj.is_element_present('id', self.exo_progress_bar)
