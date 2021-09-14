import re
from datetime import time
from io import BytesIO
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from constants.load_json import get_data
from utilities.common_methods_web import CommonMethodsWeb
import pytest_check as check

class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class NeoInClass:
    def __init__(self, driver):
        self.driver = driver
        self.obj = CommonMethodsWeb(driver)
        self.action = ActionChains(self.driver)

        self.student_cards = "//div[contains(@class,'streamList__streamItem')]"
        self.student_video_container = "//div[contains(@class,'neo_cl_StreamCard')]/div[@class='neo_cl_VideoContainer']"
        self.request_message = "//div[@class='bottomContainer__requestMessage']"
        self.profile_cards = "//div[contains(@class,'profileCard bottomContainer')]"
        self.info_tip_close = "//div[@class='infoTip__closeBtn']"
        self.focus_mode_icon = "//div[contains(@class,'presentation__focusIcon')]"
        self.full_screen_presentation = "//div[contains(@class,'presentation--fullScreenMode')]"
        self.toast_container = "//div[@class='ToastContainer']"
        self.toast_container_title = "//div[contains(@class,'focusMessageTitle')]"
        self.toast_container_subtitle = "//div[contains(@class,'focusMessageSubTitle')]"
        self.blank_slide = "//div[contains(@class,'presentation__slide--blank')]"
        self.presentation_container = "//div[contains(@class,'presentation__container')]"
        self.presentation_text_area = "//textarea[@class='readonly-textarea']"

        self.handraise_icon = "//img[contains(@src,'/static/media/raisehand')]"
        self.hand_raised_icon = "//div[text()='Hand raised']"
        self.thumb_icon = "//img[contains(@src,'/static/media/thumb')]"
        self.kebab_menu = "//img[contains(@src,'/static/media/menu')]"
        self.student_video = '//img[contains(@src,"/static/media/cam")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.student_audio = '//img[contains(@src,"/static/media/mic")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.student_video_off = '//img[contains(@src,"/static/media/cam-off")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.student_audio_off = '//img[contains(@src,"/static/media/mic-off")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.student_video_off_by_tutor = '//img[contains(@src,"/static/media/camera-off-gray-icon")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.student_audio_off_by_tutor = '//img[contains(@src,"/static/media/mic_off_icon_gray")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.session_topic_inclass = "//div[contains(@class,'classInfo__text classInfo__text--mobileTxt')]"
        self.session_topic_icon = "//div[contains(@class,'classInfo__infoIcon')]"
        self.facing_issues_btn = "//span[text()='Facing issues?']"
        self.student_exit_class = "//span[text()='Exit class']"
        self.facing_issue_header = '//div[@class="reportIssue__header"]'
        self.close_icon_in_facing_issues = '//*[@class="MuiSvgIcon-root"]/parent::div[@class="closePopup"]'
        self.helpline_no_in_facing_issue = '//span[@class="reportIssue__helpLineNoColor"]'
        self.header_text_in_exit_popup = '//*[contains(text(),"Are you sure")]'
        self.exit_img_in_exit_popup = '//img[@class="exitClass__icon"]'
        self.stayback_in_exit_popup = "//div[text()='Stay Back']"
        self.exit_class_in_exit_popup = "//span[text()='Exit Class']"
        self.rating_popup_header = '//div[contains(@class,"Component-title")]'
        self.rating_popup_close_icon = '//*[contains(@class,"MuiSvgIcon-root Component-closeIcon")]'
        self.text_in_rating_popup = "//div[text()='How was your class?']"
        self.facing_issue_options = (By.XPATH, '//*[@class="MuiFormGroup-root"]')
        self.rating_options = (By.XPATH, "//div[contains(@class,'rating__item')]")
        self.turn_on_cam_tooltip = "//span[text()='Turn on Camera']"
        self.turn_off_cam_tooltip = "//span[text()='Turn off Camera']"
        self.turn_on_mic_tooltip = "//span[text()='Turn on Microphone']"
        self.turn_off_mic_tooltip = "//span[text()='Turn off Microphone']"
        self.cam_disabled_tooltip = "//span[text()='Camera disabled by tutor']"
        self.mic_disabled_tooltip = "//span[text()='Microphone disabled by tutor']"
        self.feedback_options = '//div[@class="rating__card-item"]'
        self.continue_btn_in_rating_popup = "//span[text()='Continue']"
        self.feedback_submit_btn = "//span[text()='Submit']"
        self.tutor_details_in_feedback = '//div[@class="tutor__details"]'
        self.header_text_in_feedback = "//div[text()='How was your experience with your tutor?']"
        self.text_in_thank_you_popup = "//div[text()='Thank you for your feedback!']"
        self.report_now_btn = "//span[text()='Report Now']"
        self.issue_still_persists_text = "//div[text()='Issue still Persists?']"
        self.suggested_tips_for_issues = '//div[@class="extraTips"]'
        self.issue_response_text = "//*[text()='We got your issue!']"
        self.lower_your_hand_tootip = "//*[text()='You lowered your hand. Incase if you have any doubt, you can raise hand so that tutor can approach you.']"
#

        self.join_btn = "//span[text()='JOIN']"
        self.comments_textbox = '//*[@placeholder="Add your comments here"]'
        self.star_option = '//img[@alt="Terrible"]'
        self.tutor_name_in_feedback = '//div[@class="name"]/parent::div[@class="tutor__details"]'
        self.tutor_avatar_in_feedback = '//img[@alt="tutor avatar"]/parent::div[@class="tutor__details"]'
        self.selected_rating_option = '//img[contains(@src,"/static/media/terrible_active")]'
        self.selected_bad_rating_option = '//img[contains(@src,"/static/media/not_good_active")]'
        self.selected_okay_rating_option = '//img[contains(@src,"/static/media/okay_active")]'
        self.selected_good_rating_option = '//img[contains(@src,"/static/media/good_active")]'
        self.selected_great_rating_option = '//img[contains(@src,"/static/media/awesome_active")]'
        self.what_did_you_like_text = "//div[text()='What did you like the most?']"
        self.what_could_be_improved_text = "//div[text()='What could be improved?']"

    # streamCardContainer
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
                self.obj.get_element(
                    ('xpath', "//div[@id='" + stream_id + "']/div[@class='neo_cl_VideoContainer__profilePic']"))
                student_video_status.update({student_name: False})
            except NoSuchElementException:
                student_video_status.update({student_name: True})
        return student_video_status

    def get_student_audio_status(self):
        student_audio_status = {}
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

    def get_request_message(self):
        return self.obj.get_element(('xpath', self.request_message)).text

    # returns bottom container profile card details, profile card name or profile picture src if attached
    def get_profile_cards(self):
        profile_card_details = []
        cards = self.obj.get_elements(('xpath', "//div[contains(@class,'profileCard bottomContainer')]"))
        for card in cards:
            student_name = card.text
            if student_name == '':
                profile_pic_src = card.find_element_by_xpath(".//img").get_attribute("src")
                profile_card_details.append(profile_pic_src)
            else:
                profile_card_details.append(student_name)
        print(profile_card_details)
        return profile_card_details

    def close_info_tip(self):
        self.obj.element_click(('xpath', self.info_tip_close))

    # focus mode
    def is_focus_mode_icon_present(self):
        self.obj.wait_for_locator_webdriver(self.focus_mode_icon)
        return self.obj.is_element_present(('xpath', self.focus_mode_icon))

    def focus_mode_class_info(self):
        class_info = []
        info_elements = self.obj.get_elements(('xpath', "//div[contains(@class,'classInfo__text')]"))
        for element in info_elements:
            class_info.append(element.text)
        return class_info

    def is_full_screen_presentation_present(self):
        self.obj.wait_for_locator_webdriver(self.full_screen_presentation)
        return self.obj.is_element_present(('xpath', self.full_screen_presentation))

    def get_focus_mode_toast_message(self):
        title = self.obj.get_element(('xpath', self.toast_container_title)).text
        subtitle = self.obj.get_element(('xpath', self.toast_container_subtitle)).text
        return [title, subtitle]

    # whiteboard
    def is_blank_slide_present(self):
        self.obj.wait_for_locator_webdriver(self.blank_slide)
        return self.obj.is_element_present(('xpath', self.blank_slide))

    def get_text_from_image_and_verify(self, text):
        # element = self.obj.get_element(('xpath', self.presentation_container))
        # png = element.screenshot_as_png
        # im = Image.open(BytesIO(png))
        # im.save('verify_tutor_canvas_text.png')
        # img_text = self.obj.get_text_from_image('verify_tutor_canvas_text')
        self.obj.wait_for_locator_webdriver(self.presentation_container)
        elements = self.obj.get_elements(('xpath', self.presentation_text_area))
        actual_text_whiteboard = []
        for element in elements:
            actual_text_whiteboard.append(element.text)
        return True if (text in actual_text_whiteboard) else False

    # parameter :expected_colors_list like ['rgba(255, 199, 0, 1)']
    def verify_colors_in_student_whiteboard(self,expected_colors_list):
        self.obj.wait_for_locator_webdriver(self.presentation_text_area)
        elements = self.obj.get_elements(('xpath',self.presentation_text_area))
        flag = False
        for expected_color in expected_colors_list:
            for element in elements:
                color_code = element.value_of_css_property('color')
                if color_code == expected_color:
                    flag = True
                    break
        return flag

    # parameter :expected_shapes_list like ['circle', 'square', 'rectangle', 'triangle']
    def verify_shapes_in_student_whiteboard(self,expected_shapes_list):
        self.obj.wait_for_locator_webdriver(self.blank_slide)
        element = self.obj.get_element(('xpath',self.presentation_container))
        shapes_list = self.obj.detect_shapes(element)
        return True if (set(shapes_list) == set(expected_shapes_list)) else False

#bottom container

    def is_hand_raise_icon_present(self):
        self.obj.wait_for_locator_webdriver(self.handraise_icon)
        return self.obj.is_element_present(('xpath', self.handraise_icon))

    def verify_hand_raised(self):
        self.obj.wait_for_locator_webdriver(self.thumb_icon)
        if self.obj.is_element_present(('xpath', self.hand_raised_icon)):
            return True
        else:
            self.obj.element_click(('xpath', self.handraise_icon))
            return self.obj.is_element_present(('xpath', self.hand_raised_icon))

    def verify_lower_hand_tooltip(self):
        self.obj.wait_for_locator_webdriver(self.thumb_icon)
        if self.obj.is_element_present(('xpath', self.hand_raised_icon)):
            self.obj.element_click(('xpath', self.hand_raised_icon))
            return self.obj.is_element_present(('xpath', self.lower_your_hand_tootip))
        else:
            self.obj.is_element_present(('xpath', self.handraise_icon))
            self.obj.element_click(('xpath', self.handraise_icon))
            self.obj.element_click(('xpath', self.hand_raised_icon))
            return self.obj.is_element_present(('xpath', self.lower_your_hand_tootip))

    def is_thumb_icon_present(self):
        self.obj.wait_for_locator_webdriver(self.thumb_icon)
        return self.obj.is_element_present(('xpath', self.thumb_icon))

    def click_on_thumb_icon(self):
        self.obj.element_click(('xpath', self.thumb_icon))

    def select_any_celebration_symbol(self, celeb_symbol):
        try:
            option = self.obj.get_elements(('xpath', "//img[contains(@src,'/static/media/classes-emoji-"+celeb_symbol+"')]"))
            self.action.move_to_element(option).click().perform()
        except:
            check.equal(False, True, "Couldn't click on the option")

    def is_kebab_menu_present(self):
        # self.obj.wait_for_locator_webdriver(self.kebab_menu)
        # return self.obj.is_element_present(('xpath', self.kebab_menu))
        flag = self.obj.is_element_present(('xpath', self.kebab_menu))
        return ReturnType(True, 'Extra tips present') if flag \
        else ReturnType(False, 'Extra tips is not present')

    def click_on_kebab_menu(self):
        self.obj.wait_for_clickable_element_webdriver(self.kebab_menu)
        self.obj.element_click(('xpath', self.kebab_menu))

    def is_facing_issues_option_present(self):
        self.obj.wait_for_locator_webdriver(self.facing_issues_btn)
        return self.obj.is_element_present(('xpath', self.facing_issues_btn))

    def is_exit_class_btn_present(self):
        self.obj.wait_for_locator_webdriver(self.student_exit_class)
        return self.obj.is_element_present(('xpath', self.student_exit_class))

    def click_on_exit_class_in_student(self):
        self.obj.wait_for_clickable_element_webdriver(self.student_exit_class)
        self.obj.element_click(('xpath', self.student_exit_class))

    def verify_header_in_exit_class_popup(self):
        self.obj.wait_for_locator_webdriver(self.header_text_in_exit_popup)
        ele = self.obj.get_element(('xpath', self.header_text_in_exit_popup)).text
        assert "Are you sure you want to end the class?" in ele, "the text in popup doesn't match"

    def is_exit_image_in_exit_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.exit_img_in_exit_popup)
        return self.obj.is_element_present(('xpath', self.exit_img_in_exit_popup))

    def is_stayback_in_exit_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.stayback_in_exit_popup)
        return self.obj.is_element_present(('xpath', self.stayback_in_exit_popup))

    def is_exitclass_in_exit_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.exit_class_in_exit_popup)
        return self.obj.is_element_present(('xpath', self.exit_class_in_exit_popup))

    def click_on_exit_class_in_exit_popup(self):
        self.obj.wait_for_clickable_element_webdriver(self.exit_class_in_exit_popup)
        self.obj.element_click(('xpath', self.exit_class_in_exit_popup))

    def is_close_icon_in_facing_issues_present(self):
        self.obj.wait_for_locator_webdriver(self.close_icon_in_facing_issues)
        return self.obj.is_element_present(('xpath', self.close_icon_in_facing_issues))

    def click_on_close_icon_for_facing_issues_popup(self):
        self.obj.element_click(('xpath', self.close_icon_in_facing_issues))

    def is_helpline_no_in_facing_issues_present(self):
        self.obj.wait_for_locator_webdriver(self.helpline_no_in_facing_issue)
        return self.obj.is_element_present(('xpath', self.helpline_no_in_facing_issue))

    def select_any_option_in_facing_issue(self, string_val):
        try:
            options = self.obj.get_elements(self.facing_issue_options)
            for option in options:
                if option.text in string_val:
                    option.click()
                    break
        except:
            check.equal(False, True, "Couldn't click on the option")

    def verify_issue_response_text(self):
        self.obj.wait_for_locator_webdriver(self.issue_response_text)
        ele = self.obj.get_element(('xpath', self.issue_response_text)).text
        flag = "We got your issue!" in ele
        check.equal(flag, True, "the text in popup doesn't match")

    def verify_text_above_report_btn(self):
        self.obj.wait_for_locator_webdriver(self.facing_issue_header)
        ele = self.obj.get_element(('xpath', self.issue_still_persists_text)).text
        flag = "Issue still Persists?" in ele
        check.equal(flag, True, "the text in popup doesn't match")

    def is_report_now_btn_in_facing_issues_present(self):
        self.obj.wait_for_locator_webdriver(self.facing_issue_header)
        return self.obj.is_element_present(('xpath', self.report_now_btn))

    def click_on_report_now_btn(self):
        self.obj.element_click(('xpath', self.report_now_btn))

    def is_suggested_tips_present(self):
        self.obj.wait_for_locator_webdriver(self.facing_issue_header)
        return self.obj.is_element_present(('xpath', self.suggested_tips_for_issues))

    def get_inclass_student_video_status(self):
        student_video_status = {}
        self.obj.wait_for_locator_webdriver(self.student_video)
        try:
            if self.obj.is_element_present(('xpath', self.student_video_off)):
                student_video_status["video_disbled_desc"]="off by student"
                student_video_status["video_disbled_status"] = False
                return student_video_status
            elif self.obj.is_element_present(('xpath', self.student_video_off_by_tutor)):
                student_video_status["video_disbled_desc"] = "off by tutor"
                student_video_status["video_disbled_status"] = False
                return student_video_status
        except(NoSuchElementException):
            student_video_status["video_disbled_desc"] = "on by student"
            student_video_status["video_disbled_status"] = True
            return student_video_status


    def get_inclass_student_audio_status(self):
        student_audio_status = {}
        self.obj.wait_for_locator_webdriver(self.student_audio)
        try:
            if self.obj.is_element_present(('xpath', self.student_audio_off)):
                student_audio_status["video_disbled_desc"] = "off by student"
                student_audio_status["video_disbled_status"] = False
                return student_audio_status
            elif self.obj.is_element_present(('xpath', self.student_audio_off_by_tutor)):
                student_audio_status["video_disbled_desc"] = "off by tutor"
                student_audio_status["video_disbled_status"] = False
                return student_audio_status
        except(NoSuchElementException):
            student_audio_status["video_disbled_desc"] = "on by student"
            student_audio_status["video_disbled_status"] = True
            return student_audio_status


    def hover_on_inclass_audio_icon(self):
        audio_icon = self.obj.get_element(("xpath", self.student_audio))
        self.action.move_to_element(audio_icon).perform()

    def hover_on_inclass_video_icon(self):
        video_icon = self.obj.get_element(("xpath", self.student_video))
        self.action.move_to_element(video_icon).perform()

    def is_turn_on_camera_tooltip_present(self):
        self.obj.wait_for_locator_webdriver(self.helpline_no_in_facing_issue)
        return self.obj.is_element_present(('xpath', self.turn_on_cam_tooltip))

    def is_turn_off_camera_tooltip_present(self):
        self.obj.wait_for_locator_webdriver(self.helpline_no_in_facing_issue)
        return self.obj.is_element_present(('xpath', self.turn_off_cam_tooltip))

    def is_turn_on_mic_tooltip_present(self):
        self.obj.wait_for_locator_webdriver(self.helpline_no_in_facing_issue)
        return self.obj.is_element_present(('xpath', self.turn_on_mic_tooltip))

    def is_turn_off_mic_tooltip_present(self):
        self.obj.wait_for_locator_webdriver(self.helpline_no_in_facing_issue)
        return self.obj.is_element_present(('xpath', self.turn_off_mic_tooltip))

    def is_cam_disabled_tooltip_present(self):
        self.obj.wait_for_locator_webdriver(self.helpline_no_in_facing_issue)
        return self.obj.is_element_present(('xpath', self.cam_disabled_tooltip))

    def is_mic_disabled_tooltip_present(self):
        self.obj.wait_for_locator_webdriver(self.helpline_no_in_facing_issue)
        return self.obj.is_element_present(('xpath', self.mic_disabled_tooltip))

#session details

    def is_session_topic_inclass_present(self):
        self.obj.wait_for_locator_webdriver(self.session_topic_inclass)
        return self.obj.is_element_present(('xpath', self.session_topic_inclass))

    def verify_session_topic_name_inclass(self, topictext):
        self.obj.wait_for_locator_webdriver(self.session_topic_inclass)
        topic = self.obj.get_element(('xpath', self.session_topic_inclass)).text
        element_topic = topic.split(": ")
        flag = topictext == element_topic[1]
        check.equal(flag, True, "topic is different")

    def is_session_topic_icon_present(self):
        self.obj.wait_for_locator_webdriver(self.session_topic_icon)
        return self.obj.is_element_present(('xpath', self.session_topic_icon))

#rating popup

    def verify_header_in_rating_popup(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        ele = self.obj.get_element(('xpath', self.rating_popup_header))
        if "Rate your experience" in ele.text:
            return ReturnType(True, 'the text in popup doesnt match')
        else:
            return ReturnType(False, 'the text in popup doesnt match')

    def is_close_icon_in_rating_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_close_icon)
        return self.obj.is_element_present(('xpath', self.rating_popup_close_icon))

    def click_on_close_icon_in_rating(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_close_icon)
        self.obj.element_click(('xpath', self.rating_popup_close_icon))

    def verify_the_text_in_rating_popup(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        ele = self.obj.get_element(('xpath', self.text_in_rating_popup))
        if "How was your class" in ele.text:
            return ReturnType(True, 'the text in popup doesnt match')
        else:
            return ReturnType(False, 'the text in popup doesnt match')

    def select_any_option_in_rating(self, rating_opt):
        try:
            options = self.obj.get_elements(self.rating_options)
            for option in options:
                if option.text in rating_opt:
                    option.click()
                    break
        except:
            check.equal(False, True, "Couldn't click on the option")

    def is_continue_btn_in_rating_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.feedback_submit_btn)
        return self.obj.is_element_present(('xpath', self.continue_btn_in_rating_popup))

    def click_on_continue_btn_in_rating_popup(self):
        self.obj.element_click(('xpath', self.continue_btn_in_rating_popup))

    def is_submit_button_in_feedback_present(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        return self.obj.is_element_present(('xpath', self.feedback_submit_btn))

    def click_on_submit_button_in_feedback(self):
        self.obj.element_click(('xpath', self.feedback_submit_btn))

    def verify_the_feedback_text(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        ele = self.obj.get_element(('xpath', self.header_text_in_feedback))
        if "How was your experience with your tutor?" in ele.text:
            return ReturnType(True, 'the text in popup doesnt match')
        else:
            return ReturnType(False, 'the text in popup doesnt match')

    def select_any_feedback_option(self, feedback_opt):
        try:
            fb_options = self.obj.get_elements(('xpath', self.feedback_options))
            for option in fb_options:
                if option.text in feedback_opt:
                    option.click()
                    break
        except:
            check.equal(False, True, "Couldn't click on the option")

    def verify_text_in_Thank_you_popup(self):
        self.obj.wait_for_locator_webdriver(self.text_in_thank_you_popup)
        ele = self.obj.get_element(('xpath', self.text_in_thank_you_popup))
        if "Thank you for your feedback!" in ele.text:
            return ReturnType(True, 'the text in popup doesnt match')
        else:
            return ReturnType(False, 'the text in popup doesnt match')

  #
    def home_click_on_join(self):
        self.obj.wait_for_element_visible(('xpath',"//span[text()='JOIN']"), 5)
        self.obj.button_click('JOIN')

    def is_continue_btn_enabled(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        element = self.obj.get_element(('xpath', self.continue_btn_in_rating_popup))
        parent_classname = self.driver.execute_script('return arguments[0].parentNode.className', element)
        if 'Button--disabled' in parent_classname:
            return ReturnType(False, 'continue button is disabled')
        else:
            return ReturnType(True, 'continue button is enabled')

    def join_neo_session(self):
        self.obj.wait(10)
        self.obj.wait_for_locator_webdriver("//div[contains(@class,'neo_cl_Button')]")
        self.obj.element_click(("xpath", "//img[contains(@src,'/static/media/mic-on')]"))
        self.obj.element_click(("xpath", "//img[contains(@src,'/static/media/cam-on')]"))
        self.obj.wait_for_clickable_element_webdriver("//div[contains(@class,'neo_cl_Button')]")
        self.obj.element_click(("xpath", "//div[contains(@class,'neo_cl_Button')]"))

    def is_submit_btn_enabled(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        element = self.obj.get_element(('xpath', self.feedback_submit_btn))
        parent_classname = self.driver.execute_script('return arguments[0].parentNode.className', element)
        if 'Button--disabled' in parent_classname:
            return ReturnType(False, 'submit button is disabled')
        else:
            return ReturnType(True, 'submit button is enabled')

    def is_rating_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        if self.obj.is_element_present(('xpath', self.rating_popup_header)):
            return ReturnType(True, 'rating popup is displayed')
        else:
            return ReturnType(False, 'rating popup is not present')

    def verify_selected_emoji_color(self, expected_color):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        element = self.obj.get_element(('xpath', self.star_option))
        color_code = element.value_of_css_property('color')
        return ReturnType(True, 'yellow color is displayed') if color_code == expected_color \
            else ReturnType(False, 'color is doesnot match with expected color %s' % color_code)

    def is_star_options_present_in_rating_popup(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        if self.obj.is_element_present(('xpath', self.rating_options)):
            return ReturnType(True, 'rating options are displayed')
        else:
            return ReturnType(False, 'rating options are not present')

    def is_tutor_details_present_in_popup(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        if self.obj.is_element_present(('xpath', self.tutor_avatar_in_feedback)) and \
            self.obj.is_element_present(('xpath', self.tutor_name_in_feedback)):
            return ReturnType(True, 'tutor details are displayed')
        else:
            return ReturnType(False, 'tutor details are not present')

    def is_selected_rating_option_present(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        if self.obj.is_element_present(('xpath', self.selected_rating_option)):
            return ReturnType(True, 'rating option is selected')
        else:
            return ReturnType(False, 'rating option is not selected')

    def verify_the_what_did_you_like_text(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        ele = self.obj.get_element(('xpath', self.what_did_you_like_text))
        if "What did you like the most?" in ele.text:
            return ReturnType(True, 'the text in popup doesnt match')
        else:
            return ReturnType(False, 'the text in popup doesnt match')

    def verify_multiple_selected_rating_options(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        if self.obj.is_element_present(('xpath', self.selected_rating_option)) or \
                self.obj.is_element_present(('xpath', self.selected_bad_rating_option)) or \
                self.obj.is_element_present(('xpath', self.selected_okay_rating_option)) or \
                self.obj.is_element_present(('xpath', self.selected_good_rating_option)) and \
                self.obj.is_element_present(('xpath', self.selected_great_rating_option)):
            return ReturnType(True, 'multiple rating options are selected')
        else:
            return ReturnType(False, 'multiple options can not be selected')

    def verify_the_what_could_be_improved_text(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        ele = self.obj.get_element(('xpath', self.what_could_be_improved_text))
        if "What could be improved?" in ele.text:
            return ReturnType(True, 'the text in popup doesnt match')
        else:
            return ReturnType(False, 'the text in popup doesnt match')

    def is_add_your_comments_box_present(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        if self.obj.is_element_present(('xpath', self.comments_textbox)):
            return ReturnType(True, 'comments box is displayed')
        else:
            return ReturnType(False, 'comments box is not displayed')

    def enter_comments_in_comments_box(self, text):
        self.obj.wait_for_locator_webdriver(self.comments_textbox)
        self.obj.enter_text(text, ('xpath', self.comments_textbox))
