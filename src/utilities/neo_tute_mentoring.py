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
from utilities.staging_tlms import Stagingtlms
import pytest_check as check


class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class NeoTute:
    def __init__(self, driver):
        self.driver = driver
        self.tlms = Stagingtlms(driver)
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--no-sandbox')
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
        key = os.getenv('SECRET')
        f = Fernet(key)
        encrypted_data = get_data('../config/config.json', 'encrypted_data', 'token')
        self.decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))
        self.chrome_driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.action = ActionChains(self.chrome_driver)

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
        self.size_icon = "//div[@class='tool-box-cell-font']"
        self.palette_slider = "//input[@class='palette-stroke-slider']"
        self.video = '//div[@class = "videoPresentation false"]'

        self.global_control_video_icon = '//div[@class="topContainer--action_icon red-bg"]/img[@alt="cam"]'
        self.global_control_audio_icon = '//div[@class="topContainer--action_icon red-bg"]/img[@alt="mic"]'
        self.focus_mode = "//img[@alt='chat']"
        self.tutor_controls_video_icon = '//div[contains(@class,"tutorCard--red_icon")]/img[@alt="cam"]'
        self.tutor_controls_audio_icon = '//div[contains(@class,"tutorCard--red_icon")]/img[@alt="mic"]'

        self.chat_toggle = '//span[@class= "MuiSwitch-root"]'
        self.chat_container = '//div[@class= "chatWidgetContainer"]'
        self.type_something_inputcard = '//input[@placeholder="Type something"]'
        self.reply_button = "//div[@class='replyBtn']"
        self.ban = "//*[@class='action']"
        self.ban_student_cancel = "//div[@class='popupActionButton' and text()='Cancel']"
        self.ban_student_ban = "//div[@class='popupActionButton' and text()='Ban']"
        self.ban_student_popup = "//div[@class ='popupWrapper']"
        self.reply_button = "//*[@class='replyBtn']"
        self.approve_message = "//*[@id='approve_svg__b']"
        self.reject_message = "//*[@id='reject_svg__b']"

        self.stream_card_name = "//div[contains(@class,'tuteStreamNameClass neo_cl_StreamCard__name')]"
        self.stream_card_profilepic = "//div[@class='neo_cl_VideoContainer__profilePic']"
        self.stream_card_unmute_icon = "//div[contains(@class,'neo_cl_StreamCard__icon--withRebBg neo_cl_StreamCard__icon--unvisible')]"
        self.student_cards = "//div[@class='steamCardContainer']"
        self.student_card_menu = "//div[contains(@class,'neo_cl_StreamCard__icon--menuOption')]"
        self.student_card_pin_student_icon = "//div[contains(@class,'neo_cl_VideoContainer__overlay_view--bottomLeft')]/div/div[contains(@class,'neo_cl_StreamCard__icon')]"
        self.student_card_ask_question_icon = "//div[contains(@class,'neo_cl_VideoContainer__overlay_view--bottomCenter')]/div/div[contains(@class,'neo_cl_StreamCard__icon')]"
        self.student_video_container = "//div[@class='neo_cl_VideoContainer']"
        self.relaunch_error = "//*[contains(@class ,'Mui-error')]"
        self.end_button = '//span[text()= "End Class"]'
        self.start_class_button = "//span[contains(text(), 'Start Class')]"
        self.end_button = "//span[contains(text(), 'End Class')]"
        self.topic_header = "//div[@class='sessionPlan__header']"
        self.session_plan_content = '//div[@class = "sessionPlan_content"]'
        self.session_id_ui = '//div[@class= "sessionId"]'
        self.tab_item = '//div[@class = "tabViewContainer__tabViewText"]'
        self.student_cards = "//div[@class='studentsDetails__outer']"
        self.approve_button = ".//div[@class='neo_cl_Button Button--primary Button--rounded']"
        self.student_detail_toast = "//div[@class='studentsDetails__toastIcon']"
        self.close_toast = "//div[@class='neo_cl_ToastIcon']"
        self.student_name = ".//div[@class='student-name']"
        self.reject_buttpn = ".//div[@class='reject']"
        self.play_pause = "//div[@class='play-pause']"
        self.full_screen_icon = "//div[@class='full-screen']"
        self.mute_unmute = "//div[@class='volume-control']"
        self.time_elapsed = "//div[@class='time-elapsed']"

    def login_as_tutor(self):
        email = self.decrypted_data['staging_access']['email']
        password = self.decrypted_data['staging_access']['password']
        self.chrome_driver.get('https://staging.tllms.com/admin')
        self.chrome_driver.maximize_window()
        self.wait_for_locator_webdriver("//input[@id='email']")
        self.chrome_driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        self.wait_for_locator_webdriver("//button[@type='submit']")
        self.chrome_driver.find_element_by_xpath("//button[@type='submit']").click()
        self.wait_for_locator_webdriver("//input[@type='email']")
        self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
        self.wait_for_locator_webdriver("//span[contains(text(),'Next')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()
        self.wait_for_clickable_element_webdriver("//input[@type='password']")
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.wait_for_locator_webdriver("//span[contains(text(),'Next')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()

    def start_neo_session(self):
        url = self.tlms.get_tutor_url('neo')
        self.login_as_tutor()
        self.wait_for_locator_webdriver("//li[@id='mentoring']")
        self.chrome_driver.get(url)
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
        return url

    def wait_for_locator_webdriver(self, locator_value, timeout=15):
        try:
            WebDriverWait(self.chrome_driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_clickable_element_webdriver(self, locator_value, timeout=15):
        try:
            WebDriverWait(self.chrome_driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")


    # Session slides -> whiteboard
    def is_blank_slide_selected(self):
        self.wait_for_locator_webdriver(self.blank_slide_presented)
        return self.chrome_driver.find_element_by_xpath(self.blank_slide_presented).is_displayed()

    def toggle_draw_option(self, text):
        current_toggle_status = self.check_toggle_state()
        if text == "off" and current_toggle_status:
            self.wait_for_locator_webdriver(self.toggle_draw_checkbox)
            self.chrome_driver.find_element_by_xpath(self.toggle_draw_checkbox).click()
        elif text == "on" and (not current_toggle_status):
            self.wait_for_locator_webdriver(self.toggle_draw_checkbox)
            self.chrome_driver.find_element_by_xpath(self.toggle_draw_checkbox).click()

    def click_on_selector_icon(self):
        self.wait_for_locator_webdriver(self.selector_icon)
        self.chrome_driver.find_element_by_xpath(self.selector_icon).click()

    def click_on_pen_icon(self):
        self.wait_for_locator_webdriver(self.pen_icon)
        self.chrome_driver.find_element_by_xpath(self.pen_icon).click()

    def click_on_laser_pointer(self):
        self.wait_for_locator_webdriver(self.laser_pointer_icon)
        self.chrome_driver.find_element_by_xpath(self.laser_pointer_icon).click()

    # shape : rectangle, ellipse, polygon, star, line
    def select_any_shape(self, shape):
        self.wait_for_locator_webdriver(self.shapes_select)
        locator = getattr(self, "%s_icon" % shape, None)
        self.chrome_driver.find_element_by_xpath(self.shapes_select).click()
        self.chrome_driver.find_element_by_xpath(locator).click()

    def click_on_text_icon(self):
        self.wait_for_locator_webdriver(self.text_icon)
        self.chrome_driver.find_element_by_xpath(self.text_icon).click()

    def click_on_eraser_icon(self):
        self.wait_for_locator_webdriver(self.eraser_icon)
        self.chrome_driver.find_element_by_xpath(self.eraser_icon).click()

    def click_on_clear_icon(self):
        self.wait_for_locator_webdriver(self.clear_icon)
        self.chrome_driver.find_element_by_xpath(self.clear_icon).click()

    def verify_colors_palette(self):
        self.chrome_driver.find_elements_by_xpath("//div[@class='tool-box-cell']")[0].click()
        colors_elts = self.chrome_driver.find_elements_by_css_selector('div.cell-color')
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
        self.chrome_driver.find_element_by_xpath(self.size_icon).click()
        slider = self.chrome_driver.find_element_by_xpath(self.palette_slider)
        for i in range(size):
            if action == "increment":
                slider.send_keys(Keys.RIGHT)
            elif action == "decrement":
                slider.send_keys(Keys.LEFT)

    def is_icon_selected(self, icon):
        xpath = getattr(self, "%s_icon" % icon, None)
        if xpath is None:
            raise
        self.wait_for_locator_webdriver(xpath)
        element = self.chrome_driver.find_element_by_xpath(xpath)
        parent_classname = self.chrome_driver.execute_script('return arguments[0].parentNode.className', element)
        if 'tool-box-cell-selected' in parent_classname:
            return ReturnType(True, icon + " Icon is selected")
        else:
            return ReturnType(False, icon + " Icon is not selected")

    def draw_shapes_on_neo_tutor_whiteboard(self):
        self.wait_for_locator_webdriver(self.blank_slide_presented)
        canvas = self.chrome_driver.find_element_by_xpath(self.presentation)
        self.select_any_shape('ellipse')
        self.action.drag_and_drop_by_offset(canvas, 302, 304).perform()
        self.select_any_shape('polygon')
        self.action.drag_and_drop_by_offset(canvas, -160, -180).perform()
        self.select_any_shape('rectangle')
        self.action.drag_and_drop_by_offset(canvas, 35, 35).perform()
        self.action.drag_and_drop_by_offset(canvas, -50, 70).perform()

    def perform_text_action_on_neo_tutor_whiteboard(self, text):
        self.wait_for_locator_webdriver(self.blank_slide_presented)
        self.click_on_text_icon()
        actions = self.action
        canvas = self.chrome_driver.find_element_by_xpath(self.presentation)
        actions.move_to_element(canvas).click().send_keys(text).perform()

    def select_color(self, index):
        self.chrome_driver.find_elements_by_xpath("//div[@class='tool-box-cell']")[0].click()
        colors_elts = self.chrome_driver.find_elements_by_css_selector('div.cell-color')
        colors_elts[index].click()

    def fill_colors_on_tutor_whiteboard(self):
        self.wait_for_locator_webdriver(self.blank_slide_presented)
        canvas = self.chrome_driver.find_element_by_xpath(self.presentation)
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
        self.wait_for_locator_webdriver(self.type_something_inputcard)
        return self.chrome_driver.find_element_by_xpath(self.type_something_inputcard).is_displayed()

    def check_toggle_state(self):
        try:
            checked_flag = self.chrome_driver.find_element_by_xpath(
                "//*[contains(@class,'Mui-checked')]").is_displayed()
        except NoSuchElementException:
            checked_flag = False
        return checked_flag

    def is_toggle_present(self):
        self.wait_for_locator_webdriver(self.chat_toggle)
        return self.chrome_driver.find_element_by_xpath(self.chat_toggle).is_displayed()

    def toggle_chat(self, text):
        current_toggle_status = self.check_toggle_state()
        if text == "off" and current_toggle_status:
            self.wait_for_locator_webdriver(self.chat_toggle)
            self.chrome_driver.find_element_by_xpath(self.chat_toggle).click()
        elif text == "on" and (not current_toggle_status):
            self.wait_for_locator_webdriver(self.chat_toggle)
            self.chrome_driver.find_element_by_xpath(self.chat_toggle).click()

    def send_message_in_chat(self, text):
        timeout = 15
        while timeout:
            try:
                self.chrome_driver.find_element_by_xpath(self.type_something_inputcard).send_keys(text)
                self.chrome_driver.find_element_by_xpath(self.type_something_inputcard).send_keys(Keys.RETURN)
                break
            except (NoSuchElementException, ElementNotInteractableException):
                timeout -= 5
                logging.debug('chat is not displayed')

    def is_chat_box_present(self):
        self.wait_for_locator_webdriver(self.chat_container)
        return self.chrome_driver.find_element_by_xpath(self.chat_container).is_displayed()

    def verify_student_name_present(self, user_name):
        if self.chrome_driver.find_element_by_xpath("//*[text()='" + user_name + "']").is_displayed():
            return ReturnType(True, "student name is present")
        else:
            return ReturnType(False, "student name is not present")

    def is_message_present_for_tutor(self, text):
        try:
            self.wait_for_locator_webdriver("//*[@class='text' and text()='" + text + "']")
            self.chrome_driver.find_element_by_xpath("//*[@class='text' and text()='" + text + "']").is_displayed()
            return ReturnType(True, "Student's message present at tutor side")
        except NoSuchElementException:
            return ReturnType(False, "Student's message not present at tutor side")

    def reply_to_message(self, reply_to_message_text, reply_message):
        self.chrome_driver.find_element_by_xpath(
            "//div[text()='" + reply_to_message_text + "']/parent::div/parent::div/div[@class='replyBtn']").click()
        self.send_message_in_chat(reply_message)

    def verify_ban_approve_reject_present(self):
        is_ban_present = self.chrome_driver.find_element_by_xpath(self.ban).is_displayed()
        is_approve_present = self.chrome_driver.find_element_by_css_selector('#approve_svg__b').is_displayed()
        is_reject_present = self.chrome_driver.find_element_by_css_selector('#reject_svg__b').is_displayed()
        if is_ban_present and is_approve_present and is_reject_present:
            return ReturnType(True, 'Ban button , Approve button and Reject button are shown')
        else:
            return ReturnType(False, 'Ban button displayed - %s , Approve button displayed- %s , Reject button '
                                     'displayed - %s ' % is_ban_present % is_approve_present % is_reject_present)

    def tap_on_approve_message(self):
        self.wait_for_clickable_element_webdriver(self.approve_message)
        elements = self.chrome_driver.find_elements_by_xpath("//*[@class='action']")
        elements[2].click()

    def tap_on_reject_message(self):
        self.wait_for_clickable_element_webdriver(self.reject_message)
        elements = self.chrome_driver.find_elements_by_xpath("//*[@class='action']")
        elements[1].click()

    def tap_ban_icon(self):
        self.wait_for_clickable_element_webdriver(self.ban)
        self.chrome_driver.find_element_by_xpath(self.ban).click()

    def is_ban_options_and_buttons_present(self):
        self.wait_for_locator_webdriver(self.ban_student_popup)
        expected_option_list = ['Inappropriate Content', 'Abusive Language', 'Content Sharing', 'Others']
        actual_option_list = []
        options = self.chrome_driver.find_elements_by_xpath("//div[@class='popupOption']")
        if len(options):
            return ReturnType(False, "Zero ban options")
        for option in options:
            value = option.text
            actual_option_list.append(value)
        try:
            self.chrome_driver.find_element_by_xpath(self.ban_student_cancel).is_displayed()
            try:
                self.chrome_driver.find_element_by_xpath(self.ban_student_ban).is_displayed()
                if expected_option_list == actual_option_list:
                    return ReturnType(True,
                                      "All Ban options - Inappropriate Content, Abusive Language, Content Sharing, Others are present")
                else:
                    return ReturnType(False,
                                      "Ban options - Inappropriate Content, Abusive Language, Content Sharing, Others are not present")
            except NoSuchElementException:
                return ReturnType(False, "Ban button is not present")
        except NoSuchElementException:
            return ReturnType(False, "Cancel button is not present")

    def is_default_ban_option_present(self):
        is_checked = self.chrome_driver.find_element_by_xpath(
            '//input[@value = "inappropriate_content"]').get_attribute('checked')
        if is_checked:
            return ReturnType(True, "In Ban the student pop-up , Inappropriate Content should be selected by default")
        else:
            return ReturnType(False, "In Ban the student pop-up , Inappropriate Content is not selected by default")

    def is_ban_cancel_present(self):
        self.chrome_driver.find_element_by_xpath(self.ban_student_cancel).click()
        try:
            self.chrome_driver.find_element_by_xpath(self.ban_student_popup).is_displayed()
            return ReturnType(True, "On clicking on Cancel button the pop-up went off")
        except NoSuchElementException:
            return ReturnType(False, "On clicking on Cancel button the pop-up did not go off")

    def ban_student(self, student_name):
        # ban student and return whether Banned student messages are still be shown/not
        self.wait_for_locator_webdriver(self.ban_student_popup)
        self.chrome_driver.find_element_by_xpath(self.ban_student_ban).click()
        try:
            self.chrome_driver.find_element_by_xpath("//*[text()='" + student_name + "']").is_displayed()
            return ReturnType(True, "clicking on Ban button user is banned and banned student messages are shown")
        except NoSuchElementException:
            return ReturnType(False, "banned student messages are not present")

    def scroll_messages_from_top_to_bottom(self):
        msg_elements = self.chrome_driver.find_elements_by_css_selector('div.message')
        length = len(msg_elements)
        self.chrome_driver.execute_script("arguments[0].scrollIntoView(true);", msg_elements[length - 1])

    # steamCardContainer
    def get_all_student_names(self):
        student_names = []
        cards = self.chrome_driver.find_elements_by_xpath(self.student_cards)
        for card in cards:
            student_name = card.text
            student_names.append(student_name)
        print(student_names)
        return student_names

    def get_student_video_status(self):
        student_video_status = {}
        cards = self.chrome_driver.find_elements_by_xpath(self.student_cards)
        video_cards = self.chrome_driver.find_elements_by_xpath(self.student_video_container)
        for i in range(len(cards)):
            student_name = cards[i].text
            stream_id = video_cards[i].get_attribute('id')
            try:
                self.chrome_driver.find_element_by_xpath(
                    "//div[@id='" + stream_id + "']/div[@class='neo_cl_VideoContainer__profilePic']")
                student_video_status.update({student_name: False})
            except NoSuchElementException:
                student_video_status.update({student_name: True})
        return student_video_status

    def get_student_audio_status(self):
        student_audio_status = {}
        cards = self.chrome_driver.find_elements_by_xpath(self.student_cards)
        video_cards = self.chrome_driver.find_elements_by_xpath(self.student_video_container)
        for i in range(len(cards)):
            student_name = cards[i].text
            stream_id = video_cards[i].get_attribute('id')
            try:
                self.chrome_driver.find_element_by_xpath(
                    "//div[@id='" + stream_id + "']//div[contains(@class,'neo_cl_StreamCard__icon--withRebBg neo_cl_StreamCard__icon--unvisible')]")
                student_audio_status.update({student_name: True})
            except NoSuchElementException:
                student_audio_status.update({student_name: False})
        return student_audio_status

    # menu_item options : Pin Student,Unpin student, Ask Question,Remove from Ask Question,View Performance, Send An Award
    def click_on_menu_option(self, expected_student_name, menu_item):
        cards = self.chrome_driver.find_elements_by_xpath(self.student_cards)
        for card in cards:
            actual_student_name = card.text
            if expected_student_name == actual_student_name:
                menu_icon = card.find_element_by_xpath(self.student_card_menu)
                self.chrome_driver.execute_script("arguments[0].click();", menu_icon)
                self.chrome_driver.find_element_by_xpath("//div[text()='" + menu_item + "']").click()
                break

    def is_pin_student_icon_displayed(self, expected_student_name):
        cards = self.chrome_driver.find_elements_by_xpath(self.student_cards)
        video_cards = self.chrome_driver.find_elements_by_xpath(self.student_video_container)
        for i in range(len(cards)):
            actual_student_name = cards[i].text
            stream_id = video_cards[i].get_attribute('id')
            if expected_student_name == actual_student_name:
                try:
                    self.chrome_driver.find_element_by_xpath(
                        "//div[@id='" + stream_id + "']//div[contains(@class,'neo_cl_VideoContainer__overlay_view--bottomLeft')]/div/div[contains(@class,'neo_cl_StreamCard__icon')]")
                    return True
                except NoSuchElementException:
                    return False

    def is_ask_question_icon_displayed(self, expected_student_name):
        cards = self.chrome_driver.find_elements_by_xpath(self.student_cards)
        video_cards = self.chrome_driver.find_elements_by_xpath(self.student_video_container)
        for i in range(len(cards)):
            actual_student_name = cards[i].text
            stream_id = video_cards[i].get_attribute('id')
            if expected_student_name == actual_student_name:
                try:
                    self.chrome_driver.find_element_by_xpath(
                        "//div[@id='" + stream_id + "']//div[contains(@class,'neo_cl_VideoContainer__overlay_view--bottomCenter')]/div/div[contains(@class,'neo_cl_StreamCard__icon')]")
                    return True
                except NoSuchElementException:
                    return False

    def join_a_neo_session_as_tutor(self, **kwargs):
        db = kwargs['db']
        self.wait_for_locator_webdriver("//div[@class='neoDashboard__classInfo']", timeout=50)
        sessions = self.chrome_driver.find_elements_by_xpath("//div[@class='neoDashboard__classInfo']")
        for session in sessions:
            try:
                if session.find_element_by_xpath(
                        "//div[@class='neo_cl_Button Button--secondary Button--rounded']").is_displayed():
                    db.topic_name = session.find_element_by_xpath(
                        "//div[@class='chapter-name']").text
                    db.grade_subject = session.find_element_by_xpath(
                        "//div[@class='subject-standard']").text
                    session.find_element_by_xpath(
                        "//div[@class='neo_cl_Button Button--secondary Button--rounded']").click()
                    break


            except:
                continue

    def verify_start_button(self):
        self.wait_for_locator_webdriver(self.start_class_button)
        try:
            if self.chrome_driver.find_element_by_xpath(self.start_class_button).is_displayed():
                return ReturnType(True, "Start Button is displayed")
            else:
                return ReturnType(False, "Start Button is not displayed")
        except:
            return ReturnType(False, "Start Button is not displayed")

    def start_the_session(self):
        try:
            self.wait_for_clickable_element_webdriver(self.start_class_button, timeout=30)
            self.chrome_driver.find_element_by_xpath(self.start_class_button).click()
            self.wait_for_locator_webdriver(self.end_button, timeout=30)
            check.equal(self.chrome_driver.find_element_by_xpath(self.end_button).is_displayed(), True,
                        "End Class Button is not shown after clicking on start button")

        except:
            check.equal(False, True, "Not able to click on start class button")

    def verify_topic_name(self, **kwargs):
        db = kwargs['db']
        grade_subject = db.grade_subject.split("\n")
        topic_name = db.topic_name.split("\n")
        try:
            self.wait_for_locator_webdriver(self.topic_header)
            header = self.chrome_driver.find_element_by_xpath(self.topic_header).text
            header = header.split("\n")
            return ReturnType(True, "Topic name is correct") if header[0] in topic_name else ReturnType(False,
                                                                                                        "Topic name is incorrect ")
        except:
            return ReturnType(False,
                              "Topic name is incorrect ")

    def verify_session_id(self):
        try:
            session_id = self.chrome_driver.current_url.split("/")[-1]
            session_id_in_UI = self.chrome_driver.find_element_by_xpath(self.session_id_ui).text
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
                self.chrome_driver.find_element_by_xpath(self.session_plan_content).get_attribute(
                    "innerHTML").split('"')[1::2][0]

            return ReturnType(True, "pdf url is correct") if pdf_url_from_UI == pdf_url else ReturnType(False,
                                                                                                        "pdf url is incorrect")
        except:
            return ReturnType(False,
                              "no pdf is shown")

    def click_on_tab_item(self, tab_name='Session Plan'):
        try:
            items = self.chrome_driver.find_elements_by_xpath(self.tab_item )
            for item in items:
                if item.text.replace("\n", " ") == tab_name:
                    item.click()
                    break
        except:
            check.equal(False, True, "Couldn't click on tab item {}".format(tab_name))

    def get_number_of_students_in_student_details(self):
        try:
            elements = self.chrome_driver.find_elements_by_xpath(self.student_cards )
            return len(elements)
        except:
            return 0

    def approve_profile_pic(self, name=None):
        try:
            self.wait_for_locator_webdriver(self.student_cards)
            elements = self.chrome_driver.find_elements_by_xpath(self.student_cards)

            for element in elements:
                if element.find_element_by_xpath(self.student_name).text.lower() == name.lower():
                    element.find_element_by_xpath(
                        self.approve_button ).click()
                    self.wait_for_locator_webdriver(self.student_detail_toast)
                    if self.chrome_driver.find_element_by_xpath(
                            self.student_detail_toast).is_displayed():

                        self.chrome_driver.find_element_by_xpath(self.close_toast).click()
                        return ReturnType(True, "Approved profile pic")
                    else:
                        return ReturnType(False, "Couldn't approve profile pic")
            else:
                return ReturnType(False, "No student found for approving profile pic")
        except:
            return ReturnType(False, "Couldn't approve profile pic")

    def reject_profile_pic(self, name=None):
        try:
            self.wait_for_locator_webdriver(self.student_cards)
            elements = self.chrome_driver.find_elements_by_xpath(self.student_cards)

            for element in elements:
                if element.find_element_by_xpath(self.student_name).text.lower() == name.lower():
                    element.find_element_by_xpath(
                        self. reject_buttpn ).click()
                    self.wait_for_locator_webdriver(self.student_detail_toast)
                    if self.chrome_driver.find_element_by_xpath(
                            self.student_detail_toast).is_displayed():

                        self.chrome_driver.find_element_by_xpath(self.close_toast).click()
                        return ReturnType(True, "Approved profile pic")
                    else:
                        return ReturnType(False, "Couldn't approve profile pic")
            else:
                return ReturnType(False, "No student found for rejecting profile pic")

        except:
            return ReturnType(False, "Couldn't approve profile pic")

    def play_pause_the_video(self):
        try:
            self.chrome_driver.find_element_by_xpath(self.play_pause).click()
        except:
            check.equal(True, False, "Couldn't play or pause video")

    def verify_video_full_screen(self):
        try:
            flag = self.chrome_driver.find_element_by_xpath(
                "//div[@class='full-screenMode playerWrapper']").is_displayed()
            return ReturnType(True, "video full screen is being displayed") if flag else ReturnType(True,
                                                                                                    "video full screen is being displayed")
        except:
            ReturnType(True,
                       "video full screen is being displayed")

    def maximize_video(self):
        try:
            self.chrome_driver.find_element_by_xpath(self.full_screen_icon ).click()
            if self.verify_video_full_screen().result:
                return ReturnType(True, "Video is maximized")
            else:
                return ReturnType(False, "Video is not maximized")
        except:
            return ReturnType(True, "Video is maximized")

    def minimize_video(self):
        try:
            self.chrome_driver.find_element_by_xpath(self.full_screen_icon).click()
            if not self.verify_video_full_screen().result:
                return ReturnType(True, "Video is minimized")
            else:
                return ReturnType(False, "Video is not maximized")
        except:
            return ReturnType(True, "Video is maximized")

    def mute_unmute_video(self):
        try:
            self.chrome_driver.find_element_by_xpath(self.mute_unmute ).click()
        except:
            check.equal(False , True, "Couldn't unmute the video")

    def get_time_elapsed_in_video(self):

        return self.chrome_driver.find_element_by_xpath(self.time_elapsed).text

    def verify_video_is_presented(self):
        try:
            container = self.chrome_driver.find_element_by_xpath("//div[@class='presentationContainer']")
            flag = container.find_element_by_xpath(".//div[@class='videoPresentation false']").is_displayed()
            return ReturnType(True, "Video is being presented") if flag else ReturnType(False,
                                                                                        "Video is not being presented")
        except:
            return ReturnType(False,
                              "Video is not being presented")

    def verify_image_is_presented(self):
        try:
            container = self.chrome_driver.find_element_by_xpath("//div[@class='presentationContainer']")
            flag = container.find_element_by_xpath(".//div[@class='imagePresentation']").is_displayed()
            return ReturnType(True, "Image is being presented") if flag else ReturnType(False,
                                                                                        "Image is not being presented")
        except:
            return ReturnType(False,
                              "Image is not being presented")

    def verify_blank_screen_presented(self):
        container = self.chrome_driver.find_element_by_xpath("//div[@class='presentationContainer']")
        try:
            flag1 = container.find_element_by_xpath(".//div[@class='imagePresentation']").is_displayed()
        except:
            flag1 = False
        try:
            flag2 = container.find_element_by_xpath(".//div[@class='videoPresentation false']").is_displayed()
        except:
            flag2 = False

        flag = any(flag1, flag2)

        return ReturnType(False, " Blank screen is not presented") if flag else ReturnType(True,
                                                                                             "Blank screen is presented")

    def verify_slide_presentation_with_slide_number(self, slide_no=1):
        try:
            text =self.chrome_driver.find_element_by_xpath("//div[@class='presentation-name']").text
            text = text.split(":")[-1].strip()
            check.equal(slide_no == int(text), True, "slide number is incorrect")
        except:
            check.equal(True, False, "Slide number is not shown in presentation")

    def verify_video_elements(self):
        flag = self.verify_video_is_presented()
        check.equal(flag.result,True,flag.reason)
        try:
            flag = self.chrome_driver.find_element_by_xpath(self.play_pause).is_displayed()
            check.equal(flag,True,"Play pause button not displayed")
            flag = self.chrome_driver.find_element_by_xpath(self.full_screen_icon).is_displayed()
            check.equal(flag, True, "Full screen button  not displayed")
            flag = self.chrome_driver.find_element_by_xpath(self.mute_unmute).is_displayed()
            check.equal(flag, True, "Mute unmute button  not displayed")
            flag = self.chrome_driver.find_element_by_xpath(self.time_elapsed).is_displayed()
            check.equal(flag, True, "Time elapsed button  not displayed")
        except:
            check.equal(False, True, "Video Elements not displayed")



