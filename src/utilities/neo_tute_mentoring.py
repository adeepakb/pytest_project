import json
import os
import time
import logging
from cryptography.fernet import Fernet
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from constants.load_json import get_data
from utilities.common_methods_web import CommonMethodsWeb
from utilities.staging_tlms import Stagingtlms
import pytest_check as check


class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class NeoTute(CommonMethodsWeb):
    def __init__(self, driver):
        self.driver = driver
        self.tlms = Stagingtlms(driver)
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.chrome_options.add_argument("--use-fake-device-for-media-stream")
        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
        key = os.getenv('SECRET')
        f = Fernet(key)
        encrypted_data = get_data('../config/config.json', 'encrypted_data', 'token')
        self.decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))
        super().__init__(self.chrome_driver)
        self.action = ActionChains(self.chrome_driver)
        self.obj = CommonMethodsWeb(self.chrome_driver)

        self.login_email = "//input[@id='email']"
        self.login_submit = "//button[@type='submit']"
        self.sign_in_with_google_email = "//input[@type='email']"
        self.sign_in_next = "//span[contains(text(),'Next')]"
        self.sign_in_password = "//input[@type='password']"
        self.tllms_mentoring = "//li[@id='mentoring']"
        self.session_login_button = "//span[contains(text(),'LOGIN')]"
        self.neo_start_button = "//div[contains(@class,'neo_cl_Button')]"
        self.blank_slide_presented = "//div[@class='presentation-name']/div/span[text()=' Blank Slide']"
        self.presentation = '//*[@class = "presentationContainer"]'
        self.toggle_draw_checkbox = '//input[@name= "toggle-toolbox"]'
        self.selector_icon = "//img[contains(@src,'Toolbar_Selection_Normal')]"
        self.pen_icon = "//img[contains(@src,'Toolbar_Pen_Normal')]"
        self.laser_pointer_icon = "//img[contains(@src,'Toolbar_Marker_Normal')]"
        self.shapes_select = "//img[@alt='subscriptUrl']"
        self.rectangle_icon = "//img[contains(@src,'Toolbar_Rectangle_Normal')]"
        self.ellipse_icon = "//img[contains(@src,'Toolbar_Ellipse_Normal')]"
        self.polygon_icon = "//img[contains(@src,'Toolbar_Polygon_Normal')]"
        self.star_icon = "//img[contains(@src,'Toolbar_Star_Normal')]"
        self.line_icon = "//img[contains(@src,'Toolbar_Line_Normal')]"
        self.text_icon = "//img[contains(@src,'Toolbar_Text_Normal')]"
        self.eraser_icon = "//img[contains(@src,'Toolbar_Eraser_Normal')]"
        self.clear_icon = "//img[contains(@src,'Toolbar_Delete_Normal')]"
        self.color_icon = "//div[@class='tool-box-cell-color']"
        self.size_icon = "//div[@class='tool-box-cell-font']"
        self.palette_slider = "//input[@class='palette-stroke-slider']"
        self.video = '//div[@class = "videoPresentation false"]'

        self.global_control_video_icon_on = '//div[@class="topContainer--action_icon"]/img[@alt="cam"]'
        self.global_control_video_icon_off = '//div[@class="topContainer--action_icon red-bg"]/img[@alt="cam"]'
        self.global_control_audio_icon_on = '//div[@class="topContainer--action_icon"]/img[@alt="mic"]'
        self.global_control_audio_icon_off = '//div[@class="topContainer--action_icon red-bg"]/img[@alt="mic"]'
        self.focus_mode = "//img[@alt='chat']"
        self.tutor_controls_video_icon = '//div[contains(@class,"tutorCard--red_icon")]/img[@alt="cam"]'
        self.tutor_controls_audio_icon = '//div[contains(@class,"tutorCard--red_icon")]/img[@alt="mic"]'

        self.input_card = "//div[@class='chatInputCard']"
        self.send_icon = "//*[@class='sendAction']"
        self.chat_toggle = '//span[@class= "MuiSwitch-root"]'
        self.chat_container = '//div[@class= "chatWidgetContainer"]'
        self.type_something_inputcard = '//input[@placeholder="Type something"]'
        self.reply_button = "//div[@class='replyBtn']"
        self.reply_close = "//div[@class='prevMessage']/div[@class='closeBtn']"
        self.reply_message_by_tutor = "//div[@class='prevMessage']/following-sibling::div//div[@class='text isTutor']"
        self.reply_to_message_text = "//div[@class='closeBtn']/following-sibling::div[2]"
        self.ban = "//*[@class='action']"
        self.ban_student_cancel = "//div[@class='popupActionButton' and text()='Cancel']"
        self.ban_student_ban = "//div[@class='popupActionButton' and text()='Ban']"
        self.ban_student_popup = "//div[@class ='popupWrapper']"
        self.approve_message = "//*[@id='approve_svg__b']"
        self.reject_message = "//*[@id='reject_svg__b']"
        self.emoji_icon = "//*[@class='emoji']"
        self.sticker_item = "//*[@class='emojiItem']"
        self.sticker_onchat = '//img[contains(@src,"chat_stickers")]'
        self.message_block_container = "//div[@class='blockContainer']"
        self.chat_widget_view = ".//div[@class='chatWidgetMessageView']"
        self.chatWidgetMessageView_tutor = ("css", '.chatWidgetMessageView .chatCard.isMe')
        self.chatWidgetMessageView_student = ("xpath", "//div[@class = 'text']")

        self.stream_card_name = "//div[contains(@class,'tuteStreamNameClass neo_cl_StreamCard__name')]"
        self.stream_card_profilepic = "//div[@class='neo_cl_VideoContainer__profilePic']"
        self.stream_card_unmute_icon = "//div[contains(@class,'neo_cl_StreamCard__icon--withRebBg neo_cl_StreamCard__icon--unvisible')]"
        self.student_cards = "//div[@class='steamCardContainer']"
        self.student_card_menu = ".//div[contains(@class,'neo_cl_StreamCard__icon--menuOption')]"
        self.student_card_pin_student_icon = "//div[contains(@class,'neo_cl_VideoContainer__overlay_view--bottomLeft')]/div/div[contains(@class,'neo_cl_StreamCard__icon')]"
        self.student_card_ask_question_icon = "//div[contains(@class,'neo_cl_VideoContainer__overlay_view--bottomCenter')]/div/div[contains(@class,'neo_cl_StreamCard__icon')]"
        self.student_video_container = "//div[contains(@class,'neo_cl_StreamCard')]/div[contains(@class,'neo_cl_VideoContainer')]"
        self.relaunch_error = "//*[contains(@class ,'Mui-error')]"
        self.neo_dashborad_class = "xpath", "//div[@class='neoDashboard__classInfo']"
        self.start_class_button = "xpath", "//span[contains(text(), 'Start Class')]"
        self.end_button = "xpath", "//span[contains(text(), 'End Class')]"
        self.topic_header = "xpath", "//div[@class='sessionPlan__header']"
        self.session_plan_content = "xpath", '//div[@class = "sessionPlan_content"]'
        self.session_id_ui = "xpath", '//div[@class= "sessionId"]'
        self.tab_item = "xpath", '//div[@class = "tabViewContainer__tabViewText"]'
        self.student_cards_details = "xpath", "//div[@class='studentsDetails__outer']"
        self.approve_button = "xpath", ".//div[@class='neo_cl_Button Button--primary Button--rounded']"
        self.student_detail_toast = "//div[@class='studentsDetails__toastIcon']"
        self.close_toast = "xpath", "//div[@class='neo_cl_ToastIcon']"
        self.student_name = "xpath", ".//div[@class='student-name']"
        self.reject_buttpn = "xpath", ".//div[@class='reject']"
        self.review_image = "xpath","//div[@class='studentsDetails__approve']/div[@class='review-image']"
        self.toast_message = "xpath","//*[@class='studentsDetails__toastMsg']"
        self.student_details_name = "//div[@class='studentsDetails__container']/div[@class='student-name']"
        self.profile_card_src = "//div[@class='studentsDetails__container']/div/img"
        self.second_approve_btn = "//div[contains(@class,'neo_cl_Button Button--secondary Button--rounded Button--block-width')]/span[text()='Approve']"
        self.second_reject_btn = "//div[contains(@class,'neo_cl_Button Button--secondary Button--rounded Button--block-width')]/span[text()='Reject']"
        self.pp_review_close = "//img[@alt='close']"
        self.pp_review_image = "//div[@class='reviewImage']"
        self.newly_updated_pp = "//div[@class='reviewImage']/img"

        self.play_pause = "xpath", "xpath", "//div[@class='play-pause']"
        self.full_screen_icon = "xpath", "//div[@class='full-screen']"
        self.mute_unmute = "xpath", "//div[@class='volume-control']"
        self.time_elapsed = "xpath", "//div[@class='time-elapsed']"
        self.video_presentation = "xpath", ".//div[@class='videoPresentation false']"
        self.image_presentation = "xpath", ".//div[@class='imagePresentation']"
        self.add_slide = "//span[text()='Add New Slide']"
        self.signal_icon = '//div[@class="topContainer--signal"]'
        self.chat_icon = "//img[@alt='chat']/parent::div[contains(@Class,'topContainer--action_icon')]"
        self.audio_icon = "//img[@alt='mic']/parent::div[contains(@Class,'topContainer--action_icon')]"
        self.video_icon = "//img[@alt='cam']/parent::div[contains(@Class,'topContainer--action_icon')]"
        self.cam_off = "//img[contains(@src,'cam-off')]/parent::div[contains(@Class,'topContainer--action_icon')]"
        self.mic_off = "//img[contains(@src,'mic-off')]/parent::div[contains(@Class,'topContainer--action_icon')]"
        self.cam_on= "//img[contains(@src,'cam-on')]/parent::div[contains(@Class,'topContainer--action_icon')]"
        self.mic_on = "//img[contains(@src,'mic-on')]/parent::div[contains(@Class,'topContainer--action_icon')]"
        self.chat_off = "//img[contains(@src,'chat-off')]/parent::div[contains(@Class,'topContainer--action_icon')]"
        self.chat_on = "//img[contains(@src,'chat-on')]/parent::div[contains(@Class,'topContainer--action_icon')]"
        self.timer = '//div[@class="topContainer--timer"]'
        self.slides_names = '//div[contains(@class,"slide__slide_name")]'
        self.tutor_card = '//div[@class="tutorCard"]'
        self.tutor_cam = "//img[@alt='cam']/parent::div[contains(@Class,'tutorCard--icon')]"
        self.tutor_mic = "//img[@alt='mic']/parent::div[contains(@Class,'tutorCard--icon')]"
        self.tutor_cam_on = "(//img[contains(@src,'cam-off')]/parent::div[contains(@Class,'tutorCard--icon tutorCard--red_icon tutorCard--hide')])[1]"
        self.tutor_mic_on = "(//img[contains(@src,'mic-off')]/parent::div[contains(@Class,'tutorCard--icon tutorCard--red_icon tutorCard--hide')])[1]"
        self.continue_class_btn = "//span[text()='Continue class']"
        self.end_class_in_popup = "//span[text()='End class']"
        self.end_Class_button = "//span[text()='End Class']"
        self.focus_popup = '//div[@class="focus-mode-popup"]'
        self.blank_slide = "//*[text()='Blank Slide']"
        self.text_in_popup = '//div[@class="text"]'
        self.slide_name_in_presentation = '//*[@class="slide-name"]'
        self.present_new_slide = "//*[text()='Blank Slide']/parent::div/parent::div[contains(@class,'neo_cl_slide')]/div/div/div/div/div//*[local-name()='svg']"
        self.zoom_in_new_slide = '//*[text()="Blank Slide"]/parent::div/parent::div[contains(@class,"neo_cl_slide")]/div/div[3]'
        self.slide_title_in_description = '//div[@class="sessionSlide--slideTitle"]'
        self.slide_description = '//div[@class="sessionSlide--slideContent cke_editable"]'
        self.delete_blank_slide = "(//div[@class='slide__content_box']//div[@class='neo_cl_icon']//div[1]//*[local-name()='svg'])[1]"
        self.presentaion_name = "xpath", "//div[@class='presentation-name']"
        self.floating_emojis = "//span[contains(@class,'floaters')]"

    def login_as_tutor(self):
        email = self.decrypted_data['staging_access']['email']
        password = self.decrypted_data['staging_access']['password']
        self.chrome_driver.get('https://staging.tllms.com/admin')
        self.chrome_driver.maximize_window()
        self.obj.wait_for_locator_webdriver(self.login_email)
        self.obj.enter_text(email, ('xpath', self.login_email))
        self.obj.wait_for_locator_webdriver(self.login_submit)
        self.obj.element_click(('xpath', self.login_submit))
        self.obj.wait_for_locator_webdriver(self.sign_in_with_google_email)
        self.obj.enter_text(email, ('xpath', self.sign_in_with_google_email))
        self.obj.get_element(('xpath',self.sign_in_with_google_email)).send_keys(Keys.ENTER)
        self.obj.wait_for_clickable_element_webdriver(self.sign_in_password)
        self.obj.enter_text(password, ('xpath', self.sign_in_password))
        self.obj.get_element(('xpath', self.sign_in_password)).send_keys(Keys.ENTER)

    def start_neo_session(self,login_data="neo_login_detail1", user='student1',date ='today'):
        url = self.tlms.get_tutor_url('neo', login_data= login_data, user=user, date = date)
        self.login_as_tutor()
        self.obj.wait_for_locator_webdriver(self.tllms_mentoring)
        self.chrome_driver.get(url)
        self.obj.wait_for_locator_webdriver(self.session_login_button)
        self.obj.element_click(('xpath', self.session_login_button))
        self.obj.wait_for_clickable_element_webdriver(self.neo_start_button)
        time.sleep(3)
        self.obj.element_click(('xpath', self.neo_start_button))
        return url

    # Session slides -> whiteboard
    def is_blank_slide_selected(self):
        self.obj.wait_for_locator_webdriver(self.blank_slide_presented)
        return self.obj.is_element_present(('xpath', self.blank_slide_presented))

    def toggle_draw_option(self, text):
        current_toggle_status = self.check_toggle_state()
        if text == "off" and current_toggle_status:
            self.obj.wait_for_locator_webdriver(self.toggle_draw_checkbox)
            self.obj.element_click(('xpath', self.toggle_draw_checkbox))
        elif text == "on" and (not current_toggle_status):
            self.obj.wait_for_locator_webdriver(self.toggle_draw_checkbox)
            self.obj.element_click(('xpath', self.toggle_draw_checkbox))

    def click_on_selector_icon(self):
        self.obj.wait_for_locator_webdriver(self.selector_icon)
        self.obj.element_click(('xpath', self.selector_icon))

    def click_on_pen_icon(self):
        self.obj.wait_for_locator_webdriver(self.pen_icon)
        self.obj.element_click(('xpath', self.pen_icon))

    def click_on_laser_pointer(self):
        self.obj.wait_for_locator_webdriver(self.laser_pointer_icon)
        self.obj.element_click(('xpath', self.laser_pointer_icon))

    def laser_pointer_present(self):
        self.obj.wait_for_locator_webdriver(self.laser_pointer_icon)
        source = self.obj.get_element(('xpath', "//div[@class='netless-whiteboard cursor-laserPointer']")).value_of_css_property('cursor')
        if "data:image/svg+xml" in source:
            return True
        else:
            return False

    # shape : rectangle, ellipse, polygon, star, line
    def select_any_shape(self, shape):
        self.obj.wait_for_locator_webdriver(self.shapes_select)
        locator = getattr(self, "%s_icon" % shape, None)
        self.obj.element_click(('xpath', self.shapes_select))
        self.obj.element_click(('xpath', locator))

    def click_on_text_icon(self):
        self.obj.wait_for_locator_webdriver(self.text_icon)
        self.obj.element_click(('xpath', self.text_icon))

    def click_on_eraser_icon(self):
        self.obj.wait_for_locator_webdriver(self.eraser_icon)
        self.obj.element_click(('xpath', self.eraser_icon))

    def click_on_clear_icon(self):
        self.obj.wait_for_locator_webdriver(self.clear_icon)
        self.obj.element_click(('xpath', self.clear_icon))

    def verify_colors_palette(self):
        self.obj.element_click(('xpath', self.color_icon))
        colors_elts = self.obj.get_elements(('css', 'div.cell-color'))
        colors_list = []
        # red,orange, violet,blue,yellow,green,black,grey,white
        for i in range(0, 9):
            color = colors_elts[i].value_of_css_property('background-color')
            colors_list.append(color)
        if colors_list == ['rgba(255, 37, 37, 1)', 'rgba(255, 152, 93, 1)', 'rgba(180, 45, 191, 1)',
                           'rgba(19, 105, 233, 1)', 'rgba(255, 199, 0, 1)', 'rgba(81, 222, 31, 1)',
                           'rgba(48, 52, 58, 1)', 'rgba(183, 183, 183, 1)', 'rgba(255, 255, 255, 1)']:
            return True
        else:
            return False

    def select_size(self, action, size):
        self.obj.element_click(('xpath', self.size_icon))
        for i in range(size):
            if action == "increment":
                self.obj.enter_text(Keys.RIGHT, ('xpath', self.palette_slider))
            elif action == "decrement":
                self.obj.enter_text(Keys.LEFT, ('xpath', self.palette_slider))

    def is_icon_selected(self, icon):
        xpath = getattr(self, "%s_icon" % icon, None)
        if xpath is None:
            raise
        self.obj.wait_for_locator_webdriver(xpath)
        element = self.obj.get_element(('xpath', xpath))
        parent_classname = self.chrome_driver.execute_script('return arguments[0].parentNode.className', element)
        if 'tool-box-cell-selected' in parent_classname:
            return ReturnType(True, icon + " Icon is selected")
        else:
            return ReturnType(False, icon + " Icon is not selected")

    def draw_shapes_on_neo_tutor_whiteboard(self):
        self.obj.wait_for_locator_webdriver(self.blank_slide_presented)
        canvas = self.obj.get_element(('xpath', self.presentation))
        self.select_any_shape('ellipse')
        self.action.drag_and_drop_by_offset(canvas, 52, 54).perform()
        self.select_any_shape('polygon')
        self.action.drag_and_drop_by_offset(canvas, -80, -30).perform()
        self.select_any_shape('rectangle')
        self.action.drag_and_drop_by_offset(canvas, 35, 20).perform()
        # self.action.drag_and_drop_by_offset(canvas, -50, 70).perform()

    def perform_text_action_on_neo_tutor_whiteboard(self, text):
        self.obj.wait_for_locator_webdriver(self.blank_slide_presented)
        self.click_on_text_icon()
        canvas = self.obj.get_element(('xpath', '//*[@class = "whiteboardView"]'))
        canvas.click()
        self.action.move_to_element(canvas).click().pause(2).send_keys(text).perform()

    def select_color(self, index):
        self.obj.element_click(('xpath', self.color_icon))
        colors_elts = self.obj.get_elements(('css', 'div.cell-color'))
        colors_elts[index].click()

    def fill_colors_on_tutor_whiteboard(self):
        self.obj.wait_for_locator_webdriver(self.blank_slide_presented)
        canvas = self.obj.get_element(('xpath', self.presentation))
        self.select_any_shape('ellipse')
        self.select_color(1)  # red color
        self.action.drag_and_drop_by_offset(canvas, 302, 320).perform()
        self.select_color(2)  # orange color
        self.action.drag_and_drop_by_offset(canvas, 169, -200).perform()
        self.select_color(3)  # violet color
        self.action.drag_and_drop_by_offset(canvas, 50, 50).perform()
        self.select_color(4)  # blue color
        self.action.drag_and_drop_by_offset(canvas, -50, 70).perform()
        self.select_color(5)  # yellow  color
        self.action.drag_and_drop_by_offset(canvas, -180, -250).perform()

    # Class forum
    def is_type_something_text_present(self):
        self.obj.wait_for_locator_webdriver(self.type_something_inputcard)
        return self.obj.is_element_present(('xpath', self.type_something_inputcard))

    def check_toggle_state(self):
        checked_flag = self.obj.is_element_present(('xpath', "//*[contains(@class,'Mui-checked')]"))
        return checked_flag

    def is_toggle_present(self):
        self.obj.wait_for_locator_webdriver(self.chat_toggle)
        return self.obj.is_element_present(('xpath', self.chat_toggle))

    def toggle_chat(self, text):
        current_toggle_status = self.check_toggle_state()
        if text == "off" and current_toggle_status:
            self.obj.wait_for_locator_webdriver(self.chat_toggle)
            self.obj.element_click(('xpath', self.chat_toggle))
        elif text == "on" and (not current_toggle_status):
            self.obj.wait_for_locator_webdriver(self.chat_toggle)
            self.obj.element_click(('xpath', self.chat_toggle))

    def send_message_in_chat(self, text):
        timeout = 15
        while timeout:
            try:
                self.obj.enter_text(text, ('xpath', self.type_something_inputcard))
                self.obj.enter_text(Keys.RETURN, ('xpath', self.type_something_inputcard))
                # self.obj.enter_text(text, ('xpath', self.type_something_inputcard))
                # self.obj.enter_text(Keys.RETURN, ('xpath', self.type_something_inputcard))
                break
            except (NoSuchElementException, ElementNotInteractableException):
                timeout -= 5
                logging.debug('chat is not displayed')

    def is_chat_box_present(self):
        self.obj.wait_for_locator_webdriver(self.chat_container)
        return self.obj.is_element_present(('xpath', self.chat_container))

    def verify_student_name_present(self, user_name):
        if self.obj.is_element_present(('xpath', "//*[text()='" + user_name + "']")):
            return ReturnType(True, "student name is present")
        else:
            return ReturnType(False, "student name is not present")

    def is_message_present_for_tutor(self, text):
        self.wait_for_locator_webdriver("//*[@class='text' and text()='" + text + "']")
        if self.obj.is_element_present(('xpath', "//*[@class='text' and text()='" + text + "']")):
            return ReturnType(True, "Student's message present at tutor side")
        else:
            return ReturnType(False, "Student's message not present at tutor side")

    def is_reply_btn_clickable(self,reply_to_message_text):
        try:
            self.obj.wait_for_clickable_element_webdriver(self.reply_button)
            enabled = self.obj.get_element(('xpath', "//div[text()='" + reply_to_message_text + "']/parent::div/parent::div/div[@class='replyBtn']")).is_enabled()
            self.obj.element_click(('xpath',"//div[text()='" + reply_to_message_text + "']/parent::div/parent::div/div[@class='replyBtn']"))
            return ReturnType(True, "reply button is clickable") if enabled else ReturnType(False, "reply button is not clickable")
        except NoSuchElementException:
            return ReturnType(False, "reply button is not present and clickable")

    def verify_reply_chat_box(self):
        self.obj.wait_for_element_visible(("xpath",self.reply_close))
        flag1 = self.obj.is_element_present(("xpath",self.reply_close))
        flag2 = self.obj.is_element_present(("xpath",self.input_card))
        return flag1 and flag2

    def click_close_reply_message(self,student_message):
        self.obj.wait_for_element_visible(("xpath", self.reply_close))
        self.obj.element_click(("xpath", self.reply_close))
        self.obj.wait_for_invisibility_of_element(("xpath", self.reply_close))
        return self.selected_message_present_on_reply(student_message)

    def selected_message_present_on_reply(self,reply_to_message_text):
        try:
            if self.obj.get_element(('xpath',self.reply_to_message_text)).text == reply_to_message_text:
                return ReturnType(True,"Selected message displayed when User click 'Reply' option")
            else:
                return ReturnType(False, "Message not matching with expected %s when User click 'Reply'" % reply_to_message_text)
        except NoSuchElementException:
            return ReturnType(False, "Selected message not displayed when User click 'Reply' option")

    def reply_to_message(self, reply_to_message_text, reply_message):
        self.obj.element_click(('xpath', "//div[text()='" + reply_to_message_text + "']/parent::div/parent::div/div[@class='replyBtn']"))
        self.send_message_in_chat(reply_message)

    def is_reply_message_present(self,expected_message):
        self.wait_for_locator_webdriver(self.reply_message_by_tutor)
        actual_message = self.obj.get_element(('xpath',self.reply_message_by_tutor)).text
        if actual_message == expected_message:
            return ReturnType(True, "Tutor's reply message  to student is present")
        else:
            return ReturnType(False, "Tutor's reply message  to student is not present on screen")

    def is_send_button_enabled(self):
        try:
            self.obj.wait_for_clickable_element_webdriver(self.send_icon)
            enabled = self.obj.get_element(('xpath',self.send_icon)).is_enabled()
            return ReturnType(True, "send button is clickable") if enabled else ReturnType(False,"send button is not clickable")
        except NoSuchElementException:
            return ReturnType(False, "send button is not present")

    def click_on_sticker_icon(self):
        self.wait_for_element_visible(("xpath", self.emoji_icon))
        self.get_element(("xpath", self.emoji_icon)).click()

    def verify_no_of_default_stickers(self):
        try:
            self.wait_for_element_visible(("xpath", self.sticker_item))
            stickers = self.get_elements(("xpath", self.sticker_item))
            flag = len(stickers) == 11
            return ReturnType(True, "All 11 default stickers are shown") if flag else ReturnType(False,"All 11 default stickers are not shown")
        except NoSuchElementException:
            return ReturnType(False,"Stickers are not shown")

    def send_sticker_tutor(self):
        self.element_click(("xpath", self.emoji_icon))
        self.wait_for_element_visible(("xpath", self.sticker_item))
        self.get_element(("xpath", self.sticker_item)).click()

    def is_sticker_displayed_tutor(self):
        try:
            self.wait_for_element_visible(("xpath", self.sticker_onchat))
            return ReturnType(True, " Sticker is being displayed") if self.obj.is_element_present(("xpath", self.sticker_onchat))\
                else ReturnType(False, "Sticker is not being displayed")
        except NoSuchElementException:
            return ReturnType(False, " Sticker is not being displayed")

    def tap_outside_dialog_layout(self):
        try:
            self.action.move_by_offset(100, 100).double_click().perform()
        except:
            pass

    def get_student_name_chat(self):
        name_set = set()
        students_elts = self.obj.get_elements(('xpath',self.message_block_container))
        for elt in students_elts:
            student_name = elt.text
            name_set.add(student_name)
        return name_set

    def verify_chat_elements_tutor(self):
        self.obj.wait_for_locator_webdriver(self.chat_widget_view)
        flag1 = self.obj.is_element_present(("xpath", self.chat_widget_view))
        flag2 = self.obj.is_element_present(("xpath", self.emoji_icon))
        flag3 = self.obj.is_element_present(('xpath', self.type_something_inputcard))
        flag4 = self.obj.is_element_present(("xpath", self.send_icon))
        return flag1 and flag2 and flag3 and flag4

    def is_tutor_message_right_aligned(self):
        try:
            tutor_chat_elements = self.obj.get_elements(self.chatWidgetMessageView_tutor)
            for tutor_chat_element in tutor_chat_elements:
                if tutor_chat_element.value_of_css_property('text-align') == '-webkit-right':
                    return ReturnType(True, "Tutor chat elements are right aligned")
                else:
                    return ReturnType(False, "Tutor chat elements are not right aligned")
        except NoSuchElementException:
            return ReturnType(False, "Tutor chat elements are not present")

    def is_student_message_left_aligned(self):
        try:
            student_chat_elements = self.obj.get_elements(self.chatWidgetMessageView_student)
            for student_chat_element in student_chat_elements:
                if student_chat_element.value_of_css_property('text-align') == 'left':
                    return ReturnType(True, "Tutor chat elements are left aligned")
                else:
                    return ReturnType(False, "Tutor chat elements are not left aligned")
        except NoSuchElementException:
            return ReturnType(False, "Studengt chat elements are not present")

    def page_refresh_and_rejoin(self):
        self.driver.refresh()
        self.obj.wait_for_clickable_element_webdriver(self.neo_start_button)
        self.obj.element_click(('xpath', self.neo_start_button))

    def change_browser_size(self, width='default', height='default'):
        if width == height == 'default':
            self.driver.maximize_window()
        else:
            self.driver.set_window_size(width, height)

    def verify_ban_approve_reject_present(self):
        is_ban_present = self.obj.is_element_present(('xpath', self.ban))
        is_approve_present = self.obj.is_element_present(('css', '#approve_svg__b'))
        is_reject_present = self.obj.is_element_present(('css', '#reject_svg__b'))
        if is_ban_present and is_approve_present and is_reject_present:
            return ReturnType(True, 'Ban button , Approve button and Reject button are shown')
        else:
            return ReturnType(False, 'Ban button displayed - %s , Approve button displayed- %s , Reject button '
                                     'displayed - %s ' % is_ban_present % is_approve_present % is_reject_present)

    def tap_on_approve_message(self):
        self.obj.wait_for_clickable_element_webdriver(self.approve_message)
        elements = self.obj.get_elements(('xpath', "//*[@class='action']"))
        elements[2].click()

    def tap_on_reject_message(self):
        self.obj.wait_for_clickable_element_webdriver(self.reject_message)
        elements = self.obj.get_elements(('xpath', "//*[@class='action']"))
        elements[1].click()

    def tap_ban_icon(self):
        self.obj.wait_for_clickable_element_webdriver(self.ban)
        self.obj.element_click(('xpath', self.ban))

    def is_ban_options_and_buttons_present(self):
        self.obj.wait_for_locator_webdriver(self.ban_student_popup)
        expected_option_list = ['Inappropriate Content', 'Abusive Language', 'Content Sharing', 'Others']
        actual_option_list = []
        options = self.obj.get_elements(('xpath', "//div[@class='popupOption']"))
        if len(options):
            return ReturnType(False, "Zero ban options")
        for option in options:
            value = option.text
            actual_option_list.append(value)
        if self.obj.is_element_present(('xpath', self.ban_student_cancel)):
            if self.obj.is_element_present(('xpath', self.ban_student_ban)):
                if expected_option_list == actual_option_list:
                    return ReturnType(True,
                                      "All Ban options - Inappropriate Content, Abusive Language, Content Sharing, Others are present")
                else:
                    return ReturnType(False,
                                      "Ban options - Inappropriate Content, Abusive Language, Content Sharing, Others are not present")
            else:
                return ReturnType(False, "Ban button is not present")
        else:
            return ReturnType(False, "Cancel button is not present")

    def is_default_ban_option_present(self):
        is_checked = self.obj.get_element(('xpath', '//input[@value = "inappropriate_content"]')).get_attribute(
            'checked')
        if is_checked:
            return ReturnType(True, "In Ban the student pop-up , Inappropriate Content should be selected by default")
        else:
            return ReturnType(False, "In Ban the student pop-up , Inappropriate Content is not selected by default")

    def is_ban_cancel_present(self):
        self.obj.element_click(('xpath', self.ban_student_cancel))
        if self.obj.is_element_present(('xpath', self.ban_student_popup)):
            return ReturnType(True, "On clicking on Cancel button the pop-up went off")
        else:
            return ReturnType(False, "On clicking on Cancel button the pop-up did not go off")

    def ban_student(self, student_name):
        # ban student and return whether Banned student messages are still be shown/not
        self.obj.wait_for_locator_webdriver(self.ban_student_popup)
        self.obj.element_click(('xpath', self.ban_student_ban))
        if self.obj.is_element_present(('xpath', "//*[text()='" + student_name + "']")):
            return ReturnType(True, "clicking on Ban button user is banned and banned student messages are shown")
        else:
            return ReturnType(False, "banned student messages are not present")

    def scroll_messages_from_top_to_bottom(self):
        msg_elements = self.obj.get_elements(('css', 'div.message'))
        length = len(msg_elements)
        self.chrome_driver.execute_script("arguments[0].scrollIntoView(true);", msg_elements[length - 1])

    # steamCardContainer
    def get_all_student_names(self):
        student_names = []
        cards = self.obj.get_elements(('xpath', self.student_cards))
        for card in cards:
            student_name = card.text
            student_names.append(student_name)
        print(student_names)
        return student_names

    def get_student_video_status(self):
        student_video_status = {}
        cards = self.obj.get_elements(('xpath', self.student_cards))
        video_cards = self.obj.get_elements(('xpath', self.student_video_container))
        for i in range(len(cards)):
            student_name = cards[i].text
            stream_id = video_cards[i].get_attribute('id')
            try:
                self.obj.get_element(('xpath', "//div[@id='" + stream_id + "']/div[@class='neo_cl_NameCard_container' or contains(@class,'neo_cl_VideoContainer__profilePic')]"))
                student_video_status.update({student_name.split('\n')[-1]: False})
            except NoSuchElementException:
                student_video_status.update({student_name: True})
        return student_video_status

    def get_student_audio_status(self):
        student_audio_status = {}
        self.obj.wait(1)
        cards = self.obj.get_elements(('xpath', self.student_cards))
        video_cards = self.obj.get_elements(('xpath', self.student_video_container))
        for i in range(len(cards)):
            student_name = cards[i].text
            stream_id = video_cards[i].get_attribute('id')
            try:
                self.obj.get_element(('xpath',
                                      "//div[@id='" + stream_id + "']//div[contains(@class,'neo_cl_StreamCard__icon--withRebBg neo_cl_StreamCard__icon--unvisible')]"))
                student_audio_status.update({student_name: True})
            except NoSuchElementException:
                student_audio_status.update({student_name: False})
        return student_audio_status

    # menu_item options : Pin Student,Unpin student, Ask Question,Remove from Ask Question,View Performance, Send An Award
    def click_on_menu_option(self, expected_student_name, menu_item):
        self.obj.wait_for_locator_webdriver(self.student_cards)
        cards = self.obj.get_elements(('xpath', self.student_cards))
        for card in cards:
            actual_student_name = card.text
            if expected_student_name == actual_student_name or expected_student_name in actual_student_name:
                menu_icon = self.get_child_element(card, "xpath", self.student_card_menu)
                self.chrome_driver.execute_script("arguments[0].click();", menu_icon)
                self.wait_for_clickable_element_webdriver(".//div[text()='" + menu_item + "']")
                try:
                    self.get_child_element(card, 'xpath', ".//div[text()='" + menu_item + "']").click()
                except NoSuchElementException:
                    pass
                break

    def is_pin_student_icon_displayed(self, expected_student_name):
        cards = self.obj.get_elements(('xpath', self.student_cards))
        video_cards = self.obj.get_elements(('xpath', self.student_video_container))
        for i in range(len(cards)):
            actual_student_name = cards[i].text
            stream_id = video_cards[i].get_attribute('id')
            if expected_student_name == actual_student_name:
                try:
                    self.obj.get_element(('xpath',
                                          "//div[@id='" + stream_id + "']//div[contains(@class,'neo_cl_VideoContainer__overlay_view--bottomLeft')]/div/div[contains(@class,'neo_cl_StreamCard__icon')]"))
                    return True
                except NoSuchElementException:
                    return False

    def is_ask_question_icon_displayed(self, expected_student_name):
        try:
            self.obj.wait_for_locator_webdriver(self.student_cards)
            cards = self.obj.get_elements(('xpath', self.student_cards))
            video_cards = self.obj.get_elements(('xpath', self.student_video_container))
            for i in range(len(cards)):
                actual_student_name = cards[i].text
                stream_id = video_cards[i].get_attribute('id')
                if expected_student_name == actual_student_name:
                    try:
                        self.obj.wait_for_locator_webdriver(("//div[@id='" + stream_id + "']//div[contains(@class,'neo_cl_VideoContainer__overlay_view--bottomCenter')]/div/div[contains(@class,'neo_cl_StreamCard__icon')]"))
                        self.obj.get_element(('xpath',"//div[@id='" + stream_id + "']//div[contains(@class,'neo_cl_VideoContainer__overlay_view--bottomCenter')]/div/div[contains(@class,'neo_cl_StreamCard__icon')]"))
                        return True
                    except NoSuchElementException:
                        return False
        except NoSuchElementException:
            return False

    def is_hand_raise_icon_displayed(self, expected_student_name):
        try:
            self.obj.wait_for_locator_webdriver(self.student_cards)
            cards = self.obj.get_elements(('xpath', self.student_cards))
            video_cards = self.obj.get_elements(('xpath', self.student_video_container))
            for i in range(len(cards)):
                actual_student_name = cards[i].text
                stream_id = video_cards[i].get_attribute('id')
                if expected_student_name == actual_student_name:
                    try:
                        self.obj.wait_for_locator_webdriver(("//div[@id='"+stream_id+"']//div[contains(@class,'neo_cl_VideoContainer__overlay_view--center')]/div/div[contains(@class,'neo_cl_StreamCard__icon--raiseHand')]"))
                        self.obj.get_element(('xpath',"//div[@id='"+stream_id+"']//div[contains(@class,'neo_cl_VideoContainer__overlay_view--center')]/div/div[contains(@class,'neo_cl_StreamCard__icon--raiseHand')]"))
                        return True
                    except NoSuchElementException:
                        return False
        except NoSuchElementException:
            return False

    def join_a_neo_session_as_tutor(self, **kwargs):
        db = kwargs['db']
        self.wait_for_element_visible(("xpath", self.neo_dashborad_class), timeout=50)
        sessions = self.get_element(self.neo_dashborad_class)
        for session in sessions:
            try:
                if self.get_child_element(session, "xpath",
                                          ".//div[@class='neo_cl_Button Button--secondary Button--rounded']") \
                        .is_displayed():
                    db.topic_name = self.get_child_element(session, "xpath",
                                                           ".//div[@class='chapter-name']").text
                    db.grade_subject = self.get_child_element(session, "xpath",
                                                              ".//div[@class='subject-standard']").text
                    self.get_child_element(session, "xpath",
                                           ".//div[@class='neo_cl_Button Button--secondary Button--rounded']").click()
                    break
            except:
                continue

    def verify_start_button(self):
        self.wait_for_element_visible(self.chrome_driver, self.start_class_button)
        try:
            if self.get_element(self.start_class_button).is_displayed():
                return ReturnType(True, "Start Button is displayed")
            else:
                return ReturnType(False, "Start Button is not displayed")
        except:
            return ReturnType(False, "Start Button is not displayed")

    def start_the_session(self):
        try:
            self.wait_for_element_visible(self.chrome_driver, self.start_class_button)
            self.element_click(self.start_class_button)
            self.wait_for_element_visible(self.chrome_driver, self.end_button, timeout=30)
            check.equal(self.get_element(self.end_button).is_displayed(), True,
                        "End Class Button is not shown after clicking on start button")

        except:
            check.equal(False, True, "Not able to click on start class button")

    def verify_topic_name(self, **kwargs):
        db = kwargs['db']
        grade_subject = db.grade_subject.split("\n")
        topic_name = db.topic_name.split("\n")
        try:
            self.wait_for_element_visible(self.chrome_driver, self.topic_header)
            header = self.get_element(self.topic_header).text
            header = header.split("\n")
            return ReturnType(True, "Topic name is correct") if header[0] in topic_name else ReturnType(False,
                                                                                                        "Topic name is incorrect ")
        except:
            return ReturnType(False,
                              "Topic name is incorrect ")

    def verify_session_id(self):
        try:
            session_id = self.chrome_driver.current_url.split("/")[-1]
            session_id_in_UI = self.get_element(self.session_id_ui).text
            flag = session_id in session_id_in_UI
            return ReturnType(True, "Session id is being shown correctly") if flag else ReturnType(True,
                                                                                                   "Session id is being shown incorrectly {}".format(
                                                                                                       session_id))
        except:
            return ReturnType(False, "Session id is being shown incorrectly")

    def click_on_session_plan(self):
        self.click_on_tab_item(tab_name="Session Plan")

    def verify_session_plan_is_displayed(self, pdf_url=None):
        try:
            pdf_url_from_UI = \
                self.get_element(self.session_plan_content).get_attribute(
                    "innerHTML").split('"')[1::2][0]

            return ReturnType(True, "pdf url is correct") if pdf_url_from_UI == pdf_url else ReturnType(False,
                                                                                                        "pdf url is incorrect")
        except:
            return ReturnType(False,
                              "no pdf is shown")

    # student details
    def get_number_of_students_in_student_details(self):
        try:
            self.obj.wait_for_locator_webdriver(self.student_details_name)
            elements = self.get_elements(('xpath',self.student_details_name))
            return len(elements)
        except:
            return 0

    def get_all_names_student_details(self):
        student_names = []
        self.obj.wait_for_locator_webdriver(self.student_details_name)
        cards = self.get_elements(('xpath',self.student_details_name))
        for card in cards:
            student_name = card.text
            student_names.append(student_name)
        return student_names

    def get_img_src_for_all_students(self):
        all_profile_card_details = {}
        self.obj.wait_for_locator_webdriver(self.profile_card_src)
        cards = self.get_elements(('xpath', self.student_details_name))
        profile_cards = self.obj.get_elements(('xpath',self.profile_card_src))
        for i in range(len(profile_cards)):
            student_name = cards[i].text
            profile_src = profile_cards[i].get_attribute("src")
            all_profile_card_details.update({i+1: [student_name,profile_src]})
        print(all_profile_card_details)
        return all_profile_card_details

    def verify_approve_reject_review_buttons(self):
        try:
            self.obj.wait_for_locator_webdriver(self.student_details_name)
            self.driver.execute_script("arguments[0].scrollIntoView(true);",self.obj.get_element(self.review_image))
            self.wait_for_element_visible(self.review_image)
            flag1 = self.obj.is_element_present(self.approve_button)
            flag2 = self.obj.is_element_present(self.review_image)
            flag3 = self.obj.is_element_present(self.reject_buttpn)
            return flag1 and flag2 and flag3
        except NoSuchElementException:
            return False

    def review_present_under_image(self):
        self.obj.wait_for_element_visible(self.review_image)
        return self.obj.is_element_present(self.review_image)

    def click_on_review(self):
        self.obj.wait_for_element_visible(self.review_image)
        self.obj.element_click(self.review_image)

    def click_on_close_pp_review_popup(self):
        self.obj.wait_for_locator_webdriver(self.pp_review_close)
        self.obj.element_click(('xpath', self.pp_review_close))

    def verify_new_pp_review_popup(self):
        try:
            flag1 = self.obj.is_element_present(('xpath', self.second_approve_btn))
            flag2 = self.obj.is_element_present(('xpath', self.second_reject_btn))
            flag3 = self.obj.is_element_present(('xpath', self.pp_review_close))
            review_image_elt = self.obj.get_element(("xpath",self.newly_updated_pp))
            flag4 = 'https://tutoring-doubts-bucket.s3.ap-southeast-1.amazonaws.com/user_profile_images/students/' in review_image_elt.get_attribute("src")
            return flag1 and flag2 and flag3 and flag4
        except NoSuchElementException:
            return False

    def text_on_pp_review_popup(self):
        self.obj.wait_for_locator_webdriver(self.pp_review_image)
        text = self.obj.get_element(("xpath",self.pp_review_image)).text
        return text

    def approve_profile_pic(self, name=None):
        try:
            self.wait_for_element_visible(self.student_cards_details)
            elements = self.get_elements(self.student_cards_details)
            for element in elements:
                if self.get_child_element(element, *self.student_name).text.lower() == name.lower():
                    self.chrome_driver.execute_script("arguments[0].scrollIntoView(true);", self.get_child_element(element, *self.student_name))
                    self.wait_for_element_visible(self.approve_button)
                    self.element_click(self.approve_button)
                    self.wait_for_locator_webdriver(self.student_detail_toast)
                    if self.is_element_present(('xpath',self.student_detail_toast)) and \
                            self.obj.get_element(self.toast_message).text == "You have approved %s's profile picture"%name:
                        self.wait_for_element_visible(self.close_toast)
                        self.element_click(self.close_toast)
                        return ReturnType(True, "Approved profile pic")
                    else:
                        return ReturnType(False, "Couldn't approve profile pic")
            else:
                return ReturnType(False, "No student found for approving profile pic")
        except:
            return ReturnType(False, "Couldn't approve profile pic")

    def reject_profile_pic(self, name=None):
        try:
            self.wait_for_element_visible(self.student_cards_details)
            elements = self.get_elements(self.student_cards_details)
            for element in elements:
                self.get_child_element(element, *self.student_name)
                if self.get_child_element(element, *self.student_name).text.lower() == name.lower():
                    self.chrome_driver.execute_script("arguments[0].scrollIntoView(true);",self.get_child_element(element, *self.student_name))
                    self.wait_for_element_visible(self.reject_buttpn)
                    self.get_child_element(element,*self.reject_buttpn).click()
                    self.wait_for_locator_webdriver(self.student_detail_toast)
                    if self.is_element_present(('xpath', self.student_detail_toast)) and \
                            self.obj.get_element(self.toast_message).text == "You have rejected %s's profile picture"%name:
                        self.element_click(self.close_toast)
                        return ReturnType(True, "Rejected profile pic")
                    else:
                        return ReturnType(False, "Couldn't reject profile pic")
            else:
                return ReturnType(False, "No student found for rejecting profile pic")

        except:
            return ReturnType(False, "Couldn't approve profile pic")

    def play_pause_the_video(self):
        try:
            self.get_element(self.play_pause).click()
        except NoSuchElementException:
            check.equal(True, False, "Couldn't play or pause video")

    def verify_video_full_screen(self):
        try:
            flag = self.get_element(("xpath",
                                     "//div[@class='full-screenMode playerWrapper']")).is_displayed()
            return ReturnType(True, "video full screen is being displayed") if flag else ReturnType(True,
                                                                                                    "video full screen is being displayed")
        except NoSuchElementException:
            ReturnType(True,"video full screen is being displayed")

    def maximize_video(self):
        try:
            self.chrome_driver.find_element_by_xpath(self.full_screen_icon).click()
            if self.verify_video_full_screen().result:
                return ReturnType(True, "Video is maximized")
            else:
                return ReturnType(False, "Video is not maximized")
        except NoSuchElementException:
            return ReturnType(True, "Video is maximized")

    def minimize_video(self):
        try:
            self.get_element(self.full_screen_icon).click()
            if not self.verify_video_full_screen().result:
                return ReturnType(True, "Video is minimized")
            else:
                return ReturnType(False, "Video is not maximized")
        except NoSuchElementException:
            return ReturnType(True, "Video is maximized")

    def mute_unmute_video(self):
        try:
            self.get_element(self.mute_unmute).click()
        except NoSuchElementException:
            check.equal(False, True, "Couldn't unmute the video")

    def is_volume_slider_present(self):
        self.obj.wait_for_element_visible(('xpath', "//input[@class='input-range']"))
        return self.obj.is_element_present(('xpath', "//input[@class='input-range']"))

    def select_volume(self, action, size):
        volume_control_icon = self.obj.get_element(self.mute_unmute)
        hover = self.action.move_to_element(volume_control_icon)
        hover.perform()
        previous_volume = self.obj.get_element(('xpath', "//input[@class='input-range']")).get_attribute('value')
        for i in range(size):
            if action == "increment":
                self.obj.enter_text(Keys.ARROW_UP, ('xpath', "//input[@class='input-range']"))
                current_volume = self.obj.get_element(('xpath', "//input[@class='input-range']")).get_attribute('value')
                return True if current_volume > previous_volume else False
            elif action == "decrement":
                self.obj.enter_text(Keys.ARROW_DOWN, ('xpath', "//input[@class='input-range']"))
                current_volume = self.obj.get_element(('xpath', "//input[@class='input-range']")).get_attribute('value')
                return True if current_volume < previous_volume else False

    def get_time_elapsed_in_video(self):
        return self.get_element(self.time_elapsed).text

    def verify_video_is_presented(self):
        try:
            container = self.get_element(self.presentation_container)
            flag = self.get_child_element(container, *self.video_presentation).is_displayed()
            return ReturnType(True, "Video is being presented") if flag else ReturnType(False,"Video is not being presented")
        except NoSuchElementException:
            return ReturnType(False,"Video is not being presented")

    def verify_image_is_presented(self):
        try:
            container = self.get_element(self.presentation_container)
            flag = self.get_child_element(container, *self.image_presentation).is_displayed()
            return ReturnType(True, "Image is being presented") if flag else ReturnType(False,"Image is not being presented")
        except NoSuchElementException:
            return ReturnType(False, "Image is not being presented")

    def verify_blank_screen_presented(self):
        container = self.get_element(self.presentation_container)
        try:
            flag1 = self.get_child_element(container, *self.image_presentation).is_displayed()
        except:
            flag1 = False
        try:
            flag2 = self.get_child_element(container, *self.video_presentation).is_displayed()
        except:
            flag2 = False
        flag = any((flag1, flag2))
        return ReturnType(False, " Blank screen is not presented") if flag else ReturnType(True,
                                                                                           "Blank screen is presented")

    def verify_slide_presentation_with_slide_number(self, slide_no=1):
        try:
            text = self.get_element(self.presentaion_name).text
            text = text.split(":")[-1].strip()
            check.equal(slide_no == int(text), True, "slide number is incorrect")
        except:
            check.equal(True, False, "Slide number is not shown in presentation")

    def verify_video_elements(self):
        flag = self.verify_video_is_presented()
        check.equal(flag.result, True, flag.reason)
        try:

            flag = self.get_element(self.play_pause).is_displayed()
            check.equal(flag, True, "Play pause button not displayed")
            flag = self.get_element(self.full_screen_icon).is_displayed()
            check.equal(flag, True, "Full screen button  not displayed")
            flag = self.get_element(self.mute_unmute).is_displayed()
            check.equal(flag, True, "Mute unmute button  not displayed")
            flag = self.get_element(self.time_elapsed).is_displayed()
            check.equal(flag, True, "Time elapsed button  not displayed")
        except:
            check.equal(False, True, "Video Elements not displayed")

    def scroll_from_top_to_bottom(self, length):
        self.chrome_driver.execute_script("arguments[0].scrollIntoView(true);",
                                          self.chrome_driver.find_elements_by_css_selector('.neo_cl_slide')[length - 1])

    def present_any_slide(self,select_slide_num):
        self.click_on_tab_item(tab_name="Session Slides")
        self.obj.wait_for_locator_webdriver(self.add_slide)
        slide_select_icon = self.obj.get_element(('css',
                                                  "div.droppableList__slide_drag_item:nth-child(%s) div.neo_cl_slide.slide--mode-presenter div.slide__img_box div.slide__actions_wrapper div:nth-child(2) div.neo_cl_icon div:nth-child(1) > svg:nth-child(1)" % select_slide_num))
        slide_select_icon.click()
        self.obj.wait_for_locator_webdriver("//div[@class = 'presentationContainer']")


    def stop_presentation(self, select_slide_num):
        try:
            displayed = self.get_element(("xpath", "//div[@class = 'presentationContainer']")).is_displayed()
        except:
            displayed = False
        if displayed:
            self.click_on_tab_item(tab_name="Session Slides")
            self.obj.wait(1)
            slide_select_icon = self.obj.get_element(('css',
                                                      "div.droppableList__slide_drag_item:nth-child(%s) div.neo_cl_slide.slide--mode-presenter div.slide__img_box div.slide__actions_wrapper div:nth-child(2) div.neo_cl_icon div:nth-child(1) > svg:nth-child(1)" % select_slide_num))
            slide_select_icon.click()

    def find_video_slide(self):
        self.wait_for_locator_webdriver(self.add_slide)
        slide_cards = self.obj.get_elements(('css',".neo_cl_slide"))
        for slide_card in slide_cards:
            try:
                card_name_obj = slide_card.find_element_by_xpath(".//div//div[@class='slide__slide_name']")
                card_name = card_name_obj.get_attribute("innerHTML")
                if card_name == 'Blank Slide':
                    self.obj.element_click(('xpath',"//div[@class='slide__slide_name' and text()='Blank Slide']/parent::div//div/div[@class='neo_cl_icon']"))
                    continue
                card_src = slide_card.find_element_by_xpath(".//div/div/img").get_attribute("src")
                if 'defaultVideoThumbnail' in card_src :
                    slide_num = slide_card.get_attribute("innerText").split('\n')[0].lstrip("0")
                    return int(slide_num)
                else:
                    continue
            except NoSuchElementException:
                return None

    def active_presentation_slide_number(self):
        try:
            self.wait_for_locator_webdriver(self.add_slide)
            active_content= self.obj.get_element(("css",".slide--active div.slide__content_box div.slide__slide_number"))
            active_slide_num = active_content.text
            return int(active_slide_num.lstrip("0"))
        except:
            return None

    # Top container

    def is_audio_icon_present(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.audio_icon))

    def is_video_icon_present(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.video_icon))

    def is_chat_icon_present(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.chat_icon))

    def is_signal_icon_present(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.signal_icon))

    def is_end_class_button_present(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.end_Class_button))

    def is_timer_present(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.timer))

    def is_tutor_card_present(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.tutor_card))

    def is_tutor_mic_present(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.tutor_mic))

    def is_tutor_video_present(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.tutor_cam))

    def get_video_status(self):
        try:
            self.wait_for_element_visible(('xpath', self.cam_off))
            if self.is_element_present(('xpath', self.cam_off)):
                return ReturnType(False, "cam is off")
            else:
                return ReturnType(True, "cam is on")
        except(NoSuchElementException):
            return ReturnType(True, "cam is on")

    def get_audio_status(self):
        try:
            self.obj.wait_for_locator_webdriver(self.mic_off)
            if self.is_element_present(('xpath', self.mic_off)):
                return ReturnType(False, "mic is off")
        except NoSuchElementException:
            return ReturnType(True, "mic is on")

    def set_students_camera(self,status = "off"):
        try:
            if status.lower() == 'off':
                if self.get_video_status().result:
                    self.element_click(("xpath",self.cam_on))
            else:
                if not self.get_video_status().result:
                    self.element_click(("xpath", self.cam_off))
        except:
            pass

    def set_students_mic(self,status = 'off'):
        try:
            if status.lower()== 'off':
                if self.get_audio_status().result:
                    self.element_click(("xpath",self.mic_on))
            else:
                if not self.get_audio_status().result:
                    self.element_click(("xpath",self.mic_off))
        except:
            pass

    def get_chat_status(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        try:
            if self.is_element_present(('xpath', self.chat_off)):
                return ReturnType(False, "chat is off")
        except(NoSuchElementException):
            return ReturnType(True, "chat is on")

    def get_global_video_status(self):
        if self.is_element_present(('xpath', self.global_control_video_icon_on)):
            return ReturnType(True, "Global video icon is on")
        elif self.is_element_present(('xpath', self.global_control_video_icon_off)):
            return ReturnType(False, "Global video icon is off")
        else:
            return ReturnType(False, "Global mic icon is not present")

    def get_global_audio_status(self):
        if self.is_element_present(('xpath', self.global_control_audio_icon_on)):
            return ReturnType(True, "Global audio icon is on")
        elif self.is_element_present(('xpath', self.global_control_audio_icon_off)):
            return ReturnType(False, "Global audio icon is off")
        else:
            return ReturnType(None, "Global audio icon is not present")


    def get_tutor_video_status(self):
        try:
            self.wait_for_locator_webdriver(self.signal_icon)
            if self.is_element_present(('xpath', self.tutor_cam_on)):
                return ReturnType(True, "cam is on")
            else:
                return ReturnType(False, "cam is off")
        except(NoSuchElementException):
            return ReturnType(False, "cam is off")

    def get_tutor_audio_status(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        try:
            if self.is_element_present(('xpath', self.tutor_mic_on)):
                return ReturnType(True, "mic is on")
            else:
                return ReturnType(False, "mic is off")
        except(NoSuchElementException):
            return ReturnType(False, "mic is off")

    # status : on/off
    def select_focus_mode(self,status):
        time.sleep(2)
        self.wait_for_locator_webdriver("//label[@class='switch']")
        self.wait_for_locator_webdriver("//span[@class='on']")
        if status == 'on':
            self.element_click(("xpath","//span[@class='off']"))
        else:
            self.element_click(("xpath", "//span[@class='on']"))
        time.sleep(1)

    def verify_the_focus_mode(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        if self.is_element_present(('xpath', self.mic_off)) and \
                self.is_element_present(('xpath', self.chat_off)) and \
                self.is_element_present(('xpath', self.focus_popup)):
            return True
        else:
            self.element_click(('xpath', self.audio_icon))
            self.element_click(('xpath', self.chat_icon))
            return self.is_element_present(('xpath', self.focus_popup))

    def click_on_end_class(self):
        self.wait_for_clickable_element_webdriver(self.signal_icon)
        self.element_click(('xpath', self.end_Class_button)
                           )

    def verify_text_in_end_class_popup(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        ele = self.get_element(('xpath', self.text_in_popup)).text
        assert "Are you sure you want to end the class?" in ele, "the text in popup doesn't match"

    def is_continue_class_button_present_in_popup(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.continue_class_btn))

    def is_end_class_button_present_in_popup(self):
        self.wait_for_locator_webdriver(self.signal_icon)
        return self.is_element_present(('xpath', self.end_class_in_popup))

    def click_on_tab_item(self, tab_name='Session Plan'):
        try:
            self.obj.wait_for_element_visible(self.tab_item)
            items = self.get_elements(self.tab_item)
            for item in items:
                if item.text.replace("\n", " ") == tab_name:
                    item.click()
                    break
        except:
            check.equal(False, True, "Couldn't click on tab item {}".format(tab_name))

    def click_on_session_slides(self):
        self.click_on_tab_item(tab_name="Session Slides")

    # Add slide

    def click_on_newly_added_slide(self):
        elements = self.chrome_driver.find_elements_by_xpath(self.blank_slide)
        length = len(elements)
        self.scroll_from_top_to_bottom(length)
        elements[0].click()

    def is_present_icon_available_on_new_slide(self):
        self.wait_for_locator_webdriver(self.add_slide)
        return self.is_element_present(('xpath', self.present_new_slide))

    def is_zoom_icon_present_on_new_slide(self):
        self.wait_for_locator_webdriver(self.add_slide)
        return self.is_element_present(('xpath', self.zoom_in_new_slide))

    def is_delete_icon_present_on_new_slide(self):
        self.wait_for_locator_webdriver(self.blank_slide)
        return self.is_element_present(('xpath', self.delete_blank_slide))

    def is_add_slide_present(self):
        self.wait_for_locator_webdriver(self.add_slide)
        return self.is_element_present(('xpath', self.add_slide))

    def click_on_add_slide(self):
        self.wait_for_clickable_element_webdriver(self.add_slide)
        self.element_click(('xpath', self.add_slide))

    def click_on_delete_slide(self):
        self.wait_for_clickable_element_webdriver(self.add_slide)
        self.element_click(('xpath', self.delete_blank_slide))

    def verify_new_slide_can_be_presented(self):
        self.click_on_add_slide()
        self.chrome_driver.find_element_by_xpath(self.present_new_slide).click()
        new_slide = self.chrome_driver.find_element_by_xpath(self.blank_slide).text
        assert new_slide == self.chrome_driver.find_element_by_xpath(
            self.slide_name_in_presentation).text, "new slide is not presentable"

    def add_slide_between_slides(self, slide_no):
        self.wait_for_locator_webdriver(self.add_slide)
        elements = self.chrome_driver.find_elements_by_xpath(self.slides_names)
        len(elements)
        elements[slide_no].click()
        self.click_on_add_slide()
        self.wait_for_locator_webdriver(self.blank_slide)
        elements = self.chrome_driver.find_elements_by_xpath(self.slides_names)
        assert "Blank Slide" in elements[slide_no + 1].text, "Slide is not added under the expected slide"

    # slide description

    def click_on_any_slide(self, slide_no):
        self.wait_for_locator_webdriver(self.add_slide)
        self.wait_for_locator_webdriver(self.add_slide)
        elements = self.chrome_driver.find_elements_by_xpath(self.slides_names)
        len(elements)
        elements[slide_no].click()

    def is_slide_no_present_in_description(self):
        self.wait_for_locator_webdriver(self.blank_slide)
        return self.is_element_present(('xpath', self.slide_title_in_description))

    def is_slide_description_present(self):
        self.wait_for_locator_webdriver(self.add_slide)
        return self.is_element_present(('xpath', self.slide_description))

    def wait_for_locator_webdriver(self, locator_value, timeout=15):
        try:
            WebDriverWait(self.chrome_driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            return False

    def wait_for_clickable_element_webdriver(self, locator_value, timeout=15):
        try:
            WebDriverWait(self.chrome_driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        except TimeoutException:
            return False


    def get_url_of_presented_slide(self, select_slide_num):
        self.click_on_tab_item(tab_name="Session Slides")
        slide_select_icon = self.obj.get_element(('css',
                                                  "div.droppableList__slide_drag_item:nth-child(%s) div.neo_cl_slide.slide--mode-presenter div.slide__img_box div.slide__actions_wrapper div:nth-child(2) div.neo_cl_icon div:nth-child(1) > svg:nth-child(1)" % select_slide_num))

        url = slide_select_icon.get_attribute("innerHTML").split("src=")[1].split("alt=")[0].replace('"', '')
        return url

    def turn_tutor_video_on_off(self, status='off'):
        try:
            if status.lower() == 'on':
                self.obj.wait_for_locator_webdriver("//div[@class = 'tutorCard--icon tutorCard--grey_icon tutorCard--red_icon']")
                elements = self.get_elements(("xpath", "//div[@class = 'tutorCard--icon tutorCard--grey_icon tutorCard--red_icon']"))
                desired_element = None
                for element in elements:
                    if "cam-off" in element.get_attribute('innerHTML'):
                        desired_element = element.find_element_by_xpath("//img")
                        break
                self.action.move_to_element(desired_element).click().perform()
                time.sleep(2)
            else:
                self.obj.wait_for_locator_webdriver("//div[@class = 'tutorCard--icon tutorCard--grey_icon']")
                elements = self.get_elements(("xpath", "//div[@class = 'tutorCard--icon tutorCard--grey_icon']"))
                desired_element = None
                for element in elements:
                    if "cam-on" in element.get_attribute('innerHTML'):
                        desired_element = element
                        break
                self.action.move_to_element(desired_element).click().perform()
                time.sleep(2)
        except:
            pass

    def turn_tutor_audio_on_off(self, status='off'):
        try:
            if status.lower() == 'on':
                self.obj.wait_for_locator_webdriver("//div[@class = 'tutorCard--icon tutorCard--grey_icon tutorCard--red_icon']")
                elements = self.get_elements(("xpath", "//div[@class = 'tutorCard--icon tutorCard--grey_icon tutorCard--red_icon']"))
                desired_element = None
                for element in elements:
                    if "mic-off" in element.get_attribute('innerHTML'):
                        desired_element = element.find_element_by_xpath("//img")
                        break
                self.action.move_to_element(desired_element).click().perform()
                time.sleep(2)
            else:
                self.obj.wait_for_locator_webdriver("//div[@class = 'tutorCard--icon tutorCard--grey_icon']")
                elements = self.get_elements(("xpath", "//div[@class = 'tutorCard--icon tutorCard--grey_icon']"))
                desired_element = None
                for element in elements:
                    if "mic-on" in element.get_attribute('innerHTML'):
                        desired_element = element
                        break
                self.action.move_to_element(desired_element).click().perform()
                time.sleep(2)
        except:
            pass

    def is_floating_emojis_present_in_tute(self):
        self.obj.wait_for_locator_webdriver(self.floating_emojis)
        if self.obj.is_element_present(('xpath', self.floating_emojis)):
            return ReturnType(True, 'floaters are displayed')
        else:
            return ReturnType(False, 'floaters are not displayed')

    def enable_disable_chat(self, flag = "enable"):
        if flag == "enable":
            self.wait_for_clickable_element_webdriver(self.chat_off)
            self.element_click(("xpath",self.chat_off))
        elif flag == "disable":
            self.wait_for_clickable_element_webdriver(self.chat_on)
            self.element_click(("xpath", self.chat_on))
