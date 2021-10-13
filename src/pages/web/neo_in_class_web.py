import base64
import json
import os
import time
import subprocess
import requests
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    MoveTargetOutOfBoundsException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.common_methods_web import CommonMethodsWeb
import pytest_check as check
from selenium.webdriver.support import expected_conditions as ec


class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class NeoInClass(CommonMethodsWeb):
    def __init__(self, driver):
        self.driver = driver
        self.obj = CommonMethodsWeb(driver)
        self.action = ActionChains(self.driver)
        super().__init__(self.driver)
        self.student_cards = "//div[contains(@class,'streamList__streamItem')]"
        self.student_video_container = "//div[contains(@class,'neo_cl_StreamCard')]/div[contains(@class,'neo_cl_VideoContainer')]"
        self.request_message = "//div[@class='bottomContainer__requestMessage']"
        self.stream_list = '//section[@class="streamList__itemList"]'
        self.profile_cards = "//div[contains(@class,'profileCard bottomContainer')]"
        self.info_tip_close = "//div[@class='infoTip__closeBtn']"
        self.focus_mode_icon = "//div[contains(@class,'presentation__focusIcon')]"
        self.full_screen_presentation = "//div[contains(@class,'presentation--fullScreenMode')]"
        self.toast_container = "//div[@class='ToastContainer']"
        self.toast_container_title = "//div[contains(@class,'focusMessageTitle')]"
        self.toast_container_subtitle = "//div[contains(@class,'focusMessageSubTitle')]"
        self.blank_slide = "//div[contains(@class,'presentation__slide--blank')]"
        self.presentation_container = "//div[contains(@class,'presentation__container')]"
        self.presentation_text_area = "//textarea[@class='readonly-textarea' or 'editable-textarea']"
        self.student_card_names = "//div[contains(@class,'neo_cl_StreamCard__name')]"
        self.neo_presentation = "//div[@class='presentation']"
        self.full_screen_toggle = "//div[contains(@class,'presentation__fullScreenToggle')]"
        self.class_info_popup = "//div[@class='classInfo__infoPopup']"
        self.class_info_popup_tutor_name = "//div[@class='classInfo__tutorName']"
        self.class_info_popup_topic_name = "//div[@class='classInfo__topicName']"
        self.class_info_popup_date_time = "//div[@class='classInfo__dateTime']"
        self.class_info_popup_desc = "//div[@class='classInfo__desc']"
        self.global_icon_video = '//div[contains(@class,"topContainer--action_icon")]/img[@alt="cam"]'
        self.global_icon_audio = '//div[contains(@class,"topContainer--action_icon")]/img[@alt="mic"]'
        self.handraise_icon = "//img[contains(@src,'/static/media/raisehand')]"
        self.hand_raised_icon = "//div[text()='Hand raised']"
        self.thumb_icon = "//img[contains(@src,'/static/media/thumb')]"
        self.kebab_menu = "//img[contains(@src,'/static/media/menu')]"
        self.student_video = '//img[contains(@src,"/static/media/cam")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.student_audio = '//img[contains(@src,"/static/media/mic")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.student_video_off = '//img[contains(@src,"/static/media/cam-off")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.thumbs_sticker_icon = '//img[contains(@src,"/static/media/thumbDark")]/parent::div[contains(@class,"iconWrapper icon icon--marginLeft icon--whitebg")]'
        self.student_audio_off = '//img[contains(@src,"/static/media/mic-off")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.student_video_off_by_tutor = '//img[contains(@src,"/static/media/camera-off-gray-icon")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.student_audio_off_by_tutor = '//img[contains(@src,"/static/media/mic_off_icon_gray")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.session_topic_inclass = "//div[contains(@class,'classInfo__text classInfo__text--mobileTxt')]"
        self.class_info_icon = "//div[contains(@class,'classInfo__infoIcon')]"
        self.facing_issues_btn = "//span[text()='Facing issues?']"
        self.student_exit_class = "//span[text()='Exit class']"
        self.facing_issue_header = '//div[@class="reportIssue__header"]'
        self.checked_issue_text = '//label[contains(@class,"activeItem")]//span[contains(@class,"MuiFormControlLabel-label")]'
        self.type_something_inputcard = '//input[@placeholder="Type something"]'
        self.checked_issue_radio_button = '//label[contains(@class,"activeItem")]//div'
        self.others_option_comment = "//input[@id='outlined-basic']"
        self.facing_issues_label = '//span[contains(@class,"MuiFormControlLabel-label")]'
        self.extra_tips = "//div[@class='extraTips']"
        self.close_icon_in_facing_issues = '//*[@class="MuiSvgIcon-root"]/parent::div[@class="closePopup"]'
        self.email_icon = "//img[@class='reportSubmitted__icon']"
        self.helpline_no_in_facing_issue = '//span[@class="reportIssue__helpLineNoColor"]'
        self.header_text_in_exit_popup = '//*[contains(text(),"Are you sure")]'
        self.exit_img_in_exit_popup = '//img[@class="exitClass__icon"]'
        self.stayback_in_exit_popup = "//div[text()='Stay Back']"
        self.exit_class_in_exit_popup = "//span[text()='Exit Class']"
        self.rating_popup_header = '//div[contains(@class,"Component-title")]'
        self.rating_popup_close_icon = '//*[contains(@class,"MuiSvgIcon-root Component-closeIcon")]'
        self.text_in_rating_popup = "//div[text()='How was your class?']"
        self.facing_issue_options = ('xpath', "//label[contains(@class,'MuiFormControlLabel-root')]")
        self.rating_options = "//div[contains(@class,'rating__item')]"
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
        self.chat_container = "//div[@class='cardWrapper']"
        self.chat_by_me_name = ".//div[@class='nameContainer isMe']"
        self.chat_sender = ".//div[@class='nameContainer']"
        self.chat_message = ".//div[@class='messageBox']"
        self.chat_by_tutor = "//div[@class='text isTutor']"
        self.chat_by_me = "//div[@class = 'chatCard isMe']"
        self.send_chat_button = "//*[@class='sendAction']"
        self.chat_header = "//div[@class='chatContainer__chatheader']"
        self.chat_container_title = ".//div[@class='chatContainer__title']"
        self.chat_member_count = ".//span[@class='chatContainer__count']"
        self.tutor_name = "//span[@class = 'tutorStreamCard__name--big']"
        self.tutor_title = "//span[@class = 'tutorStreamCard__name--small']"
        self.tutor_thumbnail = "//div[@class = 'neo_cl_VideoContainer__overlay']"
        self.tutor_controls_container = "//div[@class='iconWrapper tutorStreamCard__icon']"
        self.tutor_video = "//div[@class='tutorStreamCard']//div[contains(@id,'agora-video-player-track')]"
        self.chat_controls = ".//*[@class='iconWrapper__icon']"
        self.student_cards_items = "//div[@class='streamList__streamItem']"
        self.current_student_card = "//div[@class='streamList__streamItem streamList__streamItem--localStream']"
        self.learn_login_url = 'https://learn-staging.byjus.com/login'
        self.sticker_item = "//*[@class='emojiItem']"
        self.byju_home_icon = "//span[@class='MuiButton-label']"
        self.byjus_login_number_field = "//input[@id='enterNumber']"
        self.next_button = "//div[@class='nextButtonLanding']"
        self.login_otp_field = "//input[@class='inputEleOTP']"
        self.otp_proeed_button = "//button[@class='PLbuttonEle']"
        self.home_join_field = "//span[@class='MuiIconButton-label']"
        self.tlms_otp_tab = "//li[@id='otp']"
        self.tlms_otp_tab_list = ".//li[@id='mobile_otps']"
        self.tlms_mobile_field = '//input[@id="q_mobile_no"]'
        self.tlms_otp_submit = '//input[@name="commit"]'
        self.tlms_otp_number_field = './/*[@class="col col-otp"]'
        self.home_byjus_classes_button = "//div[contains(text(),'Byju’s Classes')]"
        self.home_join_button = "//span[contains(text(),'JOIN')]"
        self.mic_video_buttons_on_join_screen = "//div[@class = 'stream--overlay_icon']"
        self.sticker_onchat = '//img[contains(@src,"chat_stickers")]' # "//div[@class= 'message']"
        self.emoji_icon = "//*[@class='emoji']"
        self.raise_hand_button = "//div[@class='iconWrapper icon icon--marginLeft icon--whitebg']"
        self.raise_hand_text = "//div[@class='bottomContainer__raiseHandText']"
        self.low_hand_text = "//div[@class='insideClass__lowerHandMessage']"

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

        self.celebrations_icons = '//div[@class="reactionButton__types reactionButton__types--visible"]'
        self.floating_emojis = "//span[contains(@class,'floaters')]"
        self.like_btn = "//img[contains(@src,'/static/media/classes-emoji-like')]"
        self.clap_btn = "//img[contains(@src,'/static/media/classes-emoji-clap')]"
        self.heart_btn = "//img[contains(@src,'/static/media/classes-emoji-heart')]"
        self.curious_btn = "//img[contains(@src,'/static/media/classes-emoji-curious')]"
        self.chat_member_count = ".//span[@class='chatContainer__count']"
        self.stop_full_screen =  "//img[@class='iconWrapper__icon']"

        # inclass
        self.weak_signal_indicator = '//*[@class="neo_cl_SignalStrength--text weak"]'
        self.students_right_arrow = '//div[contains(@class,"streamList__scrollerBtns streamList__scrollerBtns--right")]'
        self.students_left_arrow = '//div[contains(@class,"streamList__scrollerBtns streamList__scrollerBtns--left")]'
        self.discuss_doubt_msg = '//div[@class="bottomContainer__requestMessage"]'
        self.play_video_btn = "//*[contains(@src,'/static/media/playVideo')]"
        self.pause_video_btn = "//*[contains(@src,'/static/media/pauseVideo')]"
        self.mic_disabled_by_tutor = '(//*[contains(@src,"/static/media/mic_off_icon_gray")])[1]'
        self.student_cam_on = '//img[contains(@src,"/static/media/cam-on")]/parent::div[contains(@class,"iconWrapper icon icon--marginRight icon")]'
        self.student_speaking = "//div[@class='neo_cl_StreamCard__borderLayer neo_cl_StreamCard__borderLayer--active streamBorderLayerClass']"
        self.byjus_logo = '//*[@alt="titleLogo"]'

        # pre-class experience
        self.photo_edit_icon = "//div[@class='image']/img[@alt='camera']"
        self.current_student_bubble = "//div[contains(@class,'animation active')]"
        self.change_pp_header = "//span[text()='Change profile photo']"
        self.upload_photo_link = "//div[@class='uploadImageWrapper']/img[@class='changeProfile__uploadPhotoBody']"
        self.close_popup_icon = "//div[@class='closePopup']"
        self.photo_popup_header = "//span[text()='Adjust photo' or text()='Change profile photo']"
        self.current_student_bubble_pp = "//div[contains(@class,'animation active')]/img"
        self.photo_approval_pending = "//div[@class='name-image show-name pending']/div[text()='Approval Pending']"
        self.current_approved_name_image = "//div[@class='name-image show-name']//div[text()='You']"
        self.upload_photo_input = "//input[@class='uploadStudentPhotos']"
        self.change_photo = "//span[text()='Change']"
        self.save_photo = "//span[text()='Save']"
        self.pro_photo_crop_box = "//div[@class='cropper-crop-box']"

    def home_click_on_join(self):
        self.obj.wait(2)
        self.obj.wait_for_clickable_element_webdriver("//span[text()='JOIN']")
        self.obj.button_click('JOIN')

    def click_on_future_join_card(self, future_card_num):
        self.obj.wait(2)
        future_join_elements = self.obj.get_elements(("xpath","//img[@class='timerIcon']//parent::div/parent::div//div[@class='btnCard']//div/a/span[text()='JOIN']"))
        join_button_elt = self.obj.get_element(("xpath","//span[text()='JOIN']"))
        self.driver.execute_script("arguments[0].scrollIntoView(true);",join_button_elt)
        future_join_elements[future_card_num - 1].click()

    def join_neo_session(self):
        self.obj.wait_for_locator_webdriver("//div[contains(@class,'neo_cl_Button')]")
        self.obj.wait_for_clickable_element_webdriver("//div[contains(@class,'neo_cl_Button')]")
        time.sleep(3)
        self.obj.element_click(("xpath", "//div[contains(@class,'neo_cl_Button')]"))



    def join_not_started_session(self):
        try:
            elements = self.get_elements(("xpath","//div[@class = 'type-video masterOrRegularCardContainer']"))
            for element in elements:
                try:
                    timer_element_displayed = self.get_child_element(element,"xpath",".//div[@class = 'future-join-text']").is_displayed()
                except:
                    timer_element_displayed = False

                if timer_element_displayed:
                    self.get_child_element(element,"xpath",".//span[@class = 'MuiButton-label']").click()
                    break
        except:
            pass

    # streamCardContainer
    def get_all_student_names(self):
        student_names = []
        cards = self.obj.get_elements(('xpath', self.student_card_names))
        for card in cards:
            student_name = card.get_attribute('innerHTML')
            student_names.append(student_name)
        return student_names

    def get_no_of_student_cards_displayed(self):
        try:
            numb = 0
            cards = self.obj.get_elements(('xpath', self.student_card_names))
            for card in cards:
                if card.is_displayed():
                    numb += 1

            return numb
        except:
            return  0

    def get_student_video_status(self):
        student_video_status = {}
        cards = self.obj.get_elements(('xpath', self.student_card_names))
        video_cards = self.obj.get_elements(('xpath', self.student_video_container))
        for i in range(len(cards)):
            student_name = cards[i].get_attribute('innerHTML')
            stream_id = video_cards[i].get_attribute('id')
            try:
                self.obj.get_element(
                    ('xpath',
                     "//div[@id='" + stream_id + "']/div[@class ='neo_cl_NameCard localNameCardClass' or @class ='neo_cl_NameCard nameCardClass']"))
                student_video_status.update({student_name: False})
            except NoSuchElementException:
                student_video_status.update({student_name: True})
        print(student_video_status)
        return student_video_status

    def get_student_audio_status(self):
        student_audio_status = {}
        cards = self.obj.get_elements(('xpath', self.student_card_names))
        video_cards = self.obj.get_elements(('xpath', self.student_video_container))
        for i in range(len(cards)):
            student_name = cards[i].get_attribute('innerHTML')
            stream_id = video_cards[i].get_attribute('id')
            try:
                self.obj.get_element(('xpath',
                                      "//div[@id='" + stream_id + "']//div[contains(@class,'neo_cl_StreamCard__icon--withRebBg neo_cl_StreamCard__icon--unvisible')]"))
                student_audio_status.update({student_name: True})
            except NoSuchElementException:
                student_audio_status.update({student_name: False})
        print(student_audio_status)
        return student_audio_status

    def get_request_message(self):
        return self.obj.get_element(('xpath', self.request_message)).text

    def verify_alignment_stream_list(self):
        self.obj.wait_for_locator_webdriver(self.stream_list)
        display_block = self.obj.get_element(('xpath', self.stream_list)).value_of_css_property('display')
        content_alignment = self.obj.get_element(('xpath', self.stream_list)).value_of_css_property('justify-content')
        if display_block == 'grid' and content_alignment == 'center':
            return True
        else:
            return False

    # returns bottom container profile card details, profile card name or profile picture src if attached
    def get_profile_cards(self):
        profile_card_details = []
        cards = self.obj.get_elements(('xpath', "//div[@class ='neo_cl_VideoContainer__profilePic']"))
        for card in cards:
            # student_name = card.get_attribute('innerHTML')
            profile_pic_src = card.find_element_by_xpath(".//img").get_attribute("src")
            profile_card_details.append(profile_pic_src)
        return profile_card_details

    def close_info_tip(self):
        self.obj.element_click(('xpath', self.info_tip_close))

    # focus mode
    def is_focus_mode_icon_present(self):
        self.obj.wait_for_locator_webdriver(self.focus_mode_icon)
        if self.obj.is_element_present(('xpath', self.focus_mode_icon)):
            return ReturnType(True, 'focus mode is displayed')
        else:
            return ReturnType(False, 'focus mode is not present')

    def focus_mode_class_info(self):
        element_to_hover_over = self.obj.get_element(("xpath", "//div[@class='presentation__view']"))
        hover = self.action.move_to_element(element_to_hover_over)
        hover.perform()
        class_info = []
        info_elements = self.obj.get_elements(('xpath', "//div[contains(@class,'classInfo__text')]"))
        for element in info_elements:
            class_info.append(element.text)
        return class_info

    def focus_mode_switch_present(self):
        return self.obj.is_element_present(('xpath', "//div[@class='focus-mode-container']/label[@class='switch']"))

    def is_full_screen_presentation_present(self):
        self.obj.wait_for_locator_webdriver(self.full_screen_presentation)
        return self.obj.is_element_present(('xpath', self.full_screen_presentation))

    def get_focus_mode_toast_message(self):
        title = self.obj.get_element(('xpath', self.toast_container_title)).text
        subtitle = self.obj.get_element(('xpath', self.toast_container_subtitle)).text
        return [title, subtitle]

    def focus_mode_bottom_container_not_active(self):
        element = self.obj.get_element(
            ('xpath', "//section[contains(@class,'insideClass__bottomContainer--fullScreenMode')]"))
        index = element.value_of_css_property('z-index')
        position = element.value_of_css_property('position')
        background_color = element.value_of_css_property('background-color')  # transparent - rgba(0, 0, 0, 0)
        return ReturnType(True, 'bottom container controls are not active on screen') if all(
            [position == 'fixed', background_color == 'rgba(0, 0, 0, 0)', index == '4']) \
            else ReturnType(False, 'bottom container controls are still active on screen')

    def focus_mode_transition(self):
        element = self.obj.get_element(
            ('xpath', "//section[contains(@class,'insideClass__bottomContainer--fullScreenMode')]"))
        try:
            transition_value = element.value_of_css_property('transition')
            return transition_value
        except:
            return False

    def global_video_icon_present(self):
        return self.obj.is_element_present(('xpath', self.global_icon_video))

    def global_audio_icon_present(self):
        return self.obj.is_element_present(('xpath', self.global_icon_audio))

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
        time.sleep(2)
        self.obj.wait_for_locator_webdriver(self.presentation_container)
        elements = self.obj.get_elements(('xpath', self.presentation_text_area))
        actual_text_whiteboard = []
        for element in elements:
            actual_text_whiteboard.append(element.text)
        return True if (text in actual_text_whiteboard) else False

    def change_browser_size(self, width='default', height='default'):
        if width == height == 'default':
            self.driver.maximize_window()
        else:
            self.driver.set_window_size(width, height)

    # parameter :expected_colors_list like ['rgba(255, 199, 0, 1)']
    def verify_colors_in_student_whiteboard(self, expected_colors_list):
        self.obj.wait_for_locator_webdriver(self.presentation_text_area)
        elements = self.obj.get_elements(('xpath', self.presentation_text_area))
        flag = False
        for expected_color in expected_colors_list:
            for element in elements:
                color_code = element.value_of_css_property('color')
                if color_code == expected_color:
                    flag = True
                    break
        return flag

    # parameter :expected_shapes_list like ['circle', 'square', 'rectangle', 'triangle']
    def verify_shapes_in_student_whiteboard(self, expected_shapes_list):
        time.sleep(2)
        self.obj.wait_for_locator_webdriver(self.blank_slide)
        element = self.obj.get_element(('xpath', self.presentation_container))
        shapes_list = self.obj.detect_shapes(element)
        a = set(expected_shapes_list)
        b = set(shapes_list)
        print("-----------------")
        print(a)
        print(b)
        val = ((a & b) == a)
        return val

    # bottom container
    def is_hand_raise_icon_present(self):
        self.obj.wait_for_locator_webdriver(self.handraise_icon)
        return self.obj.is_element_present(('xpath', self.handraise_icon))

    def verify_hand_raised(self):
        self.obj.wait_for_locator_webdriver(self.thumb_icon)
        if self.obj.is_element_present(('xpath', self.hand_raised_icon)):
            return True
        else:
            self.obj.element_click(('xpath', self.handraise_icon))
            self.obj.wait_for_locator_webdriver(self.hand_raised_icon)
            return self.obj.is_element_present(('xpath', self.hand_raised_icon))

    def verify_lower_hand_tooltip(self):
        self.obj.wait_for_locator_webdriver(self.thumb_icon)
        if self.obj.is_element_present(('xpath', self.hand_raised_icon)):
            self.obj.element_click(('xpath', self.hand_raised_icon))
            self.obj.wait_for_element_visible(('xpath', self.lower_your_hand_tootip))
            return self.obj.is_element_present(('xpath', self.lower_your_hand_tootip))
        else:
            self.obj.is_element_present(('xpath', self.handraise_icon))
            self.obj.element_click(('xpath', self.handraise_icon))
            self.obj.element_click(('xpath', self.hand_raised_icon))
            self.obj.wait_for_element_visible(('xpath', self.lower_your_hand_tootip))
            return self.obj.is_element_present(('xpath', self.lower_your_hand_tootip))

    def is_thumb_icon_present(self):
        self.obj.wait_for_locator_webdriver(self.thumb_icon)
        if self.obj.is_element_present(('xpath', self.thumb_icon)):
            return True
        else:
            return False

    def is_floating_emojis_present(self):
        self.obj.wait_for_locator_webdriver(self.floating_emojis)
        if self.obj.is_element_present(('xpath', self.floating_emojis)):
            return ReturnType(True, 'floaters are displayed')
        else:
            return ReturnType(False, 'floaters are not displayed')

    def click_on_thumb_icon(self):
        self.obj.wait_for_locator_webdriver(self.thumb_icon)
        time.sleep(3)
        self.obj.element_click(('xpath', self.thumb_icon))

    def get_the_no_of_elements(self):
        ele = self.obj.get_elements(
            ('xpath', "//script[@type='text/javascript' and @rel = 'nofollow' and contains(@src,'type=push')]"))
        return len(ele)

    def is_celebrations_icons_present(self):
        self.obj.wait_for_locator_webdriver(self.celebrations_icons)
        if self.obj.is_element_present(('xpath', self.celebrations_icons)):
            return ReturnType(True, 'celebrations icons are displayed')
        else:
            return ReturnType(False, 'celebrations icons are not displayed')

    def is_reactions_icons_present(self):
        self.obj.wait_for_locator_webdriver(self.celebrations_icons)
        if self.obj.is_element_present(('xpath', self.like_btn)) and \
                self.obj.is_element_present(('xpath', self.clap_btn)) and \
                self.obj.is_element_present(('xpath', self.heart_btn)) and \
                self.obj.is_element_present(('xpath', self.curious_btn)):
            return ReturnType(True, 'celebrations icons are displayed')
        else:
            return ReturnType(False, 'celebrations icons are not displayed')

    def select_any_celebration_symbol(self, celeb_symbol):
        self.obj.wait_for_clickable_element_webdriver(self.celebrations_icons)
        try:
            option = self.obj.get_element(
                ('xpath', "//img[contains(@src,'/static/media/classes-emoji-" + celeb_symbol + "')]"))
            option.click()
            self.obj.wait(1)
            return True
        except:
            return False

    def celebration_highlighted(self, celeb_symbol):
        self.obj.wait_for_clickable_element_webdriver(self.celebrations_icons)
        try:
            option = self.obj.get_element(
                ('xpath', "//img[contains(@src,'/static/media/classes-emoji-" + celeb_symbol + "')]"))
            return option.is_enabled()
        except:
            return False

    def is_exit_class_btn_present(self):
        self.obj.wait_for_locator_webdriver(self.student_exit_class)
        return self.obj.is_element_present(('xpath', self.student_exit_class))

    def click_on_exit_class_in_student(self):
        self.obj.wait_for_clickable_element_webdriver(self.student_exit_class)
        self.obj.element_click(('xpath', self.student_exit_class))

    def verify_header_in_exit_class_popup(self):
        self.obj.wait_for_locator_webdriver(self.header_text_in_exit_popup)
        ele = self.obj.get_element(('xpath', self.header_text_in_exit_popup)).text
        return True if "Are you sure you want to end the class?" in ele else False

    def is_exit_image_in_exit_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.exit_img_in_exit_popup)
        return self.obj.is_element_present(('xpath', self.exit_img_in_exit_popup))

    def is_stayback_in_exit_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.stayback_in_exit_popup)
        return self.obj.is_element_present(('xpath', self.stayback_in_exit_popup))

    def is_exitclass_in_exit_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.exit_class_in_exit_popup)
        return self.obj.is_element_present(('xpath', self.exit_class_in_exit_popup))

    def click_on_stayback_in_exit_popup(self):
        self.obj.wait_for_locator_webdriver(self.stayback_in_exit_popup)
        return self.obj.element_click(('xpath', self.stayback_in_exit_popup))

    def click_on_exit_class_in_exit_popup(self):
        self.obj.wait_for_locator_webdriver(self.exit_class_in_exit_popup)
        return self.obj.element_click(('xpath', self.exit_class_in_exit_popup))

    # facing issues
    def is_kebab_menu_present(self):
        self.obj.wait_for_locator_webdriver(self.kebab_menu)
        return self.obj.is_element_present(('xpath', self.kebab_menu))

    def click_on_kebab_menu(self):
        self.obj.wait_for_clickable_element_webdriver(self.kebab_menu)
        self.obj.element_click(('xpath', self.kebab_menu))

    def is_facing_issues_option_present(self):
        self.obj.wait_for_locator_webdriver(self.facing_issues_btn)
        return self.obj.is_element_present(('xpath', self.facing_issues_btn))

    def button_click(self, text):
        self.obj.button_click(text)

    def is_close_icon_in_facing_issues_present(self):
        self.obj.wait_for_locator_webdriver(self.close_icon_in_facing_issues)
        return self.obj.is_element_present(('xpath', self.close_icon_in_facing_issues))

    def click_on_close_icon_for_facing_issues_popup(self):
        self.obj.wait_for_locator_webdriver(self.close_icon_in_facing_issues)
        self.obj.element_click(('xpath', self.close_icon_in_facing_issues))

    def is_helpline_no_in_facing_issues_present(self):
        self.obj.wait_for_locator_webdriver(self.helpline_no_in_facing_issue)
        return self.obj.is_element_present(('xpath', self.helpline_no_in_facing_issue))

    def verify_issue_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.facing_issue_header)
        ele = self.obj.get_element(('xpath', self.facing_issue_header)).text
        return True if "Choose the issue you are facing" in ele and self.obj.is_element_present(
            ('xpath', "//div[@class='reportIssue']")) else False

    def select_any_option_in_facing_issue(self, string_val):
        options = self.obj.get_elements(self.facing_issue_options)
        for option in options:
            if option.text in string_val:
                option.click()
                break

    def verify_issue_checked(self, expected_issue):
        return ReturnType(True, 'Student able to select issue') if self.obj.get_element(
            ('xpath', self.checked_issue_text)).text == expected_issue \
            else ReturnType(False, 'Unable to select radio button for issue %s' % expected_issue)

    def verify_bold_font_selected_issue(self):
        font = self.obj.get_element(('xpath', self.checked_issue_text)).value_of_css_property('font-family')
        return ReturnType(True, 'selected issue is in bold') if font == 'Gotham-Medium' \
            else ReturnType(False, 'selected issue is not in bold')

    def provide_other_comments(self, comment_text):
        self.obj.enter_text(comment_text, ('xpath', self.others_option_comment))

    def get_all_issues_list(self):
        issues_list = []
        issue_elements = self.obj.get_elements(('xpath', self.facing_issues_label))
        for issue_element in issue_elements:
            issues_list.append(issue_element.text)
        return issues_list

    def get_selected_issue_radio_btn_color(self, expected_color):
        self.obj.wait_for_locator_webdriver(self.checked_issue_radio_button)
        element = self.obj.get_element(('xpath', self.checked_issue_radio_button))
        color_code = element.value_of_css_property('color')
        return ReturnType(True, 'sky color is present') if color_code == expected_color \
            else ReturnType(False, 'sky color is not present for radio button.Found %s' % color_code)

    def verify_extra_tips(self, text):
        flag = self.obj.is_element_present(('xpath', self.extra_tips)) and self.obj.is_text_match(text)
        return ReturnType(True, 'Extra tips present') if flag \
            else ReturnType(False, 'Extra tips is not present')

    def extra_tips_alignment(self):
        try:
            left_aligned = self.obj.get_element(('xpath', self.extra_tips)).value_of_css_property('margin-left')
            display_block = self.obj.get_element(('xpath', self.extra_tips)).value_of_css_property('display')
            if left_aligned is not None and display_block is not None:
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def is_text_match(self, text):
        return self.obj.is_text_match(text)

    def verify_issue_response_text(self):
        self.obj.wait_for_locator_webdriver(self.issue_response_text)
        ele = self.obj.get_element(('xpath', self.issue_response_text)).text
        flag = "We got your issue!" in ele
        check.equal(flag, True, "the text in popup doesn't match")

    def verify_text_above_report_btn(self):
        self.obj.wait_for_locator_webdriver(self.facing_issue_header)
        ele = self.obj.get_element(('xpath', self.issue_still_persists_text)).text
        return True if "Issue still Persists?" in ele else False

    def scroll_down_facing_issues_popup(self, length):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_elements_by_css_selector('.MuiFormControlLabel-label')[length - 1])

    def is_report_now_btn_in_facing_issues_present(self):
        self.obj.wait_for_locator_webdriver(self.facing_issue_header)
        return self.obj.is_element_present(('xpath', self.report_now_btn))

    def is_report_now_btn_enabled(self):
        self.obj.wait_for_locator_webdriver(self.facing_issue_header)
        element = self.obj.get_element(('xpath', self.report_now_btn))
        parent_classname = self.driver.execute_script('return arguments[0].parentNode.className', element)
        if 'Button--disabled' in parent_classname:
            return ReturnType(False, 'Report now button is disabled')
        else:
            return ReturnType(True, 'Report now button is enabled')

    def click_on_report_now_btn(self):
        self.obj.element_click(('xpath', self.report_now_btn))

    def is_email_icon_present_and_text(self):
        self.obj.wait_for_locator_webdriver(self.email_icon)
        value = self.obj.get_element(('xpath', "//div[@class='reportIssue__submitted']/p")).text
        return [self.obj.is_element_present(('xpath', self.email_icon)), value]

    def submitted_popup_disappear(self):
        self.obj.wait_for_invisibility_of_element(('xpath', "//*[@class='timeRemaining']"), 10)
        return self.obj.is_element_present(('xpath', "//*[@class='reportIssue__submitted']"))

    def page_refresh_issue_popup_disappear(self):
        self.obj.page_refresh()
        return self.obj.is_element_present(('xpath', self.facing_issue_header))

    def page_refresh_issue_submitted_issue_popup_disappear(self):
        self.obj.page_refresh()
        return self.obj.is_element_present(('xpath', "//*[@class='reportIssue__submitted']"))

    def get_inclass_student_video_status(self):
        self.obj.wait_for_locator_webdriver(self.student_video)
        if self.obj.is_element_present(('xpath', self.student_video_off_by_tutor)):
            return "DISABLED"
        elif self.obj.is_element_present(('xpath', self.student_video_off)):
            return "OFF"
        else:
            return "ON"

    def get_inclass_student_audio_status(self):
        self.obj.wait_for_locator_webdriver(self.student_audio)
        if self.obj.is_element_present(('xpath', self.student_audio_off_by_tutor)):
            return "DISABLED"
        elif self.obj.is_element_present(('xpath', self.student_audio_off)):
            return "OFF"
        else:
            return "ON"

    def click_on_inclass_audio_icon(self):
        self.obj.wait_for_clickable_element_webdriver(self.student_audio)
        audio_icon = self.obj.get_element(("xpath", self.student_audio))
        audio_icon.click()
        time.sleep(2)

    def click_on_inclass_video_icon(self):
        self.obj.wait_for_clickable_element_webdriver(self.student_video)
        video_icon = self.obj.get_element(("xpath", self.student_video))
        video_icon.click()
        time.sleep(2)

    def turn_on_off_student_mic(self, action):
        audio_status = self.get_inclass_student_audio_status()
        if all([audio_status != action, audio_status != 'DISABLED']):
            self.click_on_inclass_audio_icon()

    def turn_on_off_student_video(self, action):
        video_status = self.get_inclass_student_video_status()
        if all([video_status != action, video_status != 'DISABLED']):
            self.click_on_inclass_video_icon()

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

    # session details
    def is_session_topic_inclass_present(self):
        self.obj.wait_for_locator_webdriver(self.session_topic_inclass)
        if self.obj.is_element_present(('xpath', self.session_topic_inclass)):
            return ReturnType(True, 'session topic is displayed')
        else:
            return ReturnType(False, 'session topic is not present')

    def get_session_topic_name_inclass(self):
        self.obj.wait_for_locator_webdriver(self.session_topic_inclass)
        topic = self.obj.get_element(('xpath', self.session_topic_inclass)).text
        subject_topic = topic.split(": ")
        return [subject_topic[0], subject_topic[1]]

    def is_session_topic_icon_present(self):
        self.obj.wait_for_locator_webdriver(self.class_info_icon)
        return self.obj.is_element_present(('xpath', self.class_info_icon))

    def click_on_class_info_icon(self):
        self.obj.wait_for_locator_webdriver(self.class_info_icon)
        self.obj.element_click(('xpath', self.class_info_icon))

    def get_classinfo_popup_session_details(self):
        class_info_details_dict = {}
        self.obj.wait_for_locator_webdriver(self.class_info_popup_topic_name)
        tutor_name = self.obj.get_element(('xpath', self.class_info_popup_tutor_name)).text
        class_info_details_dict.update({"Tutor": tutor_name})
        subject_topic = self.obj.get_element(('xpath', self.class_info_popup_topic_name)).text
        elements = subject_topic.split(": ")
        class_info_details_dict.update({"Subject": elements[0], "Topic": elements[1]})
        session_date_time = self.obj.get_element(('xpath', self.class_info_popup_date_time)).text
        class_info_details_dict.update({"Session Time": session_date_time})
        session_desc = self.obj.get_element(('xpath', self.class_info_popup_desc)).text
        class_info_details_dict.update({"Session Description": session_desc})
        return class_info_details_dict

    def tap_outside_dialog_layout(self):
        try:
            self.action.move_by_offset(100, 100).double_click().perform()
        except:
            pass

    def is_class_info_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.class_info_popup)
        return self.obj.is_element_present(('xpath', self.class_info_popup))

    # rating popup
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
            options = self.obj.get_elements(('xpath', self.rating_options))
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

    # in class presentation
    def is_image_presented(self):
        try:
            element = self.obj.get_element(("xpath", "//div[@class='presentation__view']"))
            element2 = self.obj.get_child_element(element, "xpath",
                                                  ".//div[@class='presentation__slide presentation__slide--common presentation__slide--posRelative']")
            return ReturnType(True, "Image is being presented") if element2 else ReturnType(False,
                                                                                            "Image is not being presented")
        except:
            return ReturnType(False, "Image is not being presented")

    def get_presented_screen_url(self):
        try:
            element = self.obj.get_element(("xpath", "//div[@class='presentation__view']"))
            element2 = self.obj.get_child_element(element, "xpath",
                                                  ".//div[@class='presentation__slide presentation__slide--common presentation__slide--posRelative']")
            url = element2.get_attribute("innerHTML").split("src=")[1].split("alt=")[0].replace('"', '')
            return url
        except:
            return None

    def is_blank_screen_presented(self):
        try:
            element = self.obj.get_element(("xpath", "//div[@class='presentation__view']"))
            element2 = self.obj.get_child_element(element, "xpath",
                                                  ".//div[@class='presentation__slide presentation__slide--common presentation__slide--blank']")
            return ReturnType(True, "Blank screen is being presented") if element2 else ReturnType(True,
                                                                                                   "Blank screen  is not being presented")
        except:
            return ReturnType(False, "Blank screen is not being presented")

    def is_video_being_presented(self):
        try:
            self.obj.wait_for_locator_webdriver("//div[@class='presentation__view']")
            element = self.obj.get_element(("xpath", "//div[@class='presentation__view']"))
            element2 = self.obj.get_child_element(element, "xpath", ".//div[@class='presentation__slide']")
            return ReturnType(True, "Video is being presented") if element2 else ReturnType(False,
                                                                                            "Video is not being presented")
        except:
            return ReturnType(False, "Video is not being presented")

    # video session
    def presentation_alignment(self):
        try:
            self.obj.wait_for_locator_webdriver(self.neo_presentation)
            alignment = self.obj.get_element(
                ('xpath', "//div[@class='presentation__slideView']")).value_of_css_property('justify-content')
            if alignment == 'center':
                return ReturnType(True, "Presented Image/Video is center aligned as expected")
            else:
                return ReturnType(False, "Presented Image/Video is not center aligned as expected")
        except NoSuchElementException:
            return ReturnType(False, "Alignment property is not found")

    def verify_presentation_dimension_ratio(self):
        try:
            self.obj.wait_for_locator_webdriver(self.presentation_container)
            presentation_container = self.driver.find_element_by_xpath(self.presentation_container)
            size = presentation_container.size
            canvas_width = int(size['width'])
            canvas_height = int(size['height'])
            ratio = format(canvas_width / canvas_height, ".2f")
            return ReturnType(True, "slide displayed on the whiteboard is of size 16:9") if any(
                [ratio == format(16 / 9, ".2f")]) else \
                ReturnType(False, "slide displayed on the whiteboard is not of size 16:9")
        except:
            ReturnType(False, "Tutor not presenting anything in neo session")

    def hover_over_full_screen_toggle(self):
        element_to_hover_over = self.obj.get_element(("xpath", self.full_screen_toggle))
        hover = self.action.move_to_element(element_to_hover_over)
        hover.perform()


    def get_full_screen_toggle_visibility(self):
        self.obj.wait_for_locator_webdriver(self.full_screen_toggle)
        full_screen_toggle_elt = self.obj.get_element(('xpath', self.full_screen_toggle))
        visibility = full_screen_toggle_elt.value_of_css_property('visibility')
        return visibility

    def is_minimize_full_screen_present(self):
        return self.obj.is_element_present(
            ("xpath", "//div[@class='iconWrapper icon icon--whitebg icon--marginLeft icon--lightBlack']"))

    def get_video_src(self):
        video_url = self.driver.find_element_by_xpath("//div[@class='shaka-video-container']/video")
        video_src = video_url.get_attribute("src")
        print(video_src)
        return video_src

    def hover_over_and_verify_bottom_container_focus_mode(self):
        element_to_hover_over = self.obj.get_element(("xpath", "//div[@class='presentation__view']"))
        hover = self.action.move_to_element(element_to_hover_over)
        try:
            hover.perform()
        except ElementNotInteractableException:
            pass
        flag1 = self.is_hand_raise_icon_present()
        flag2 = self.is_thumb_icon_present()
        flag3 = self.is_kebab_menu_present()
        flag4 = self.is_turn_on_camera_tooltip_present()
        return ReturnType(True,
                          "hover over presentation it shows all controls; camera, Raise/Lower hand thumbs up icon and menu option") \
            if any((flag1, flag2, flag3, flag4)) else ReturnType(False, "hover over presentation it shows all controls")

    def hover_over_and_verify_bottom_container_full_screen(self):
        element_to_hover_over = self.obj.get_element(("xpath", "//div[@class='presentation__view']"))
        hover = self.action.move_to_element(element_to_hover_over)
        hover.perform()
        flag1 = self.is_hand_raise_icon_present()
        flag2 = self.is_thumb_icon_present()
        flag3 = self.is_kebab_menu_present()
        flag4 = self.is_turn_on_camera_tooltip_present()
        flag5 = self.is_turn_on_mic_tooltip_present()
        return ReturnType(True, "hover over presentation it shows all controls; camera, mic, Raise/Lower hand, "
                                "thumbs up icon and menu option") \
            if any((flag1, flag2, flag3, flag4, flag5)) else ReturnType(False, "Bottom container controls are not "
                                                                               "shown on hover over presentation")

    def is_presentation_displayed(self):
        flag1 = self.is_image_presented().result
        flag2 = self.is_blank_screen_presented().result
        flag3 = self.is_video_being_presented().result
        return ReturnType(True, "Presentation is being displyed") if any((flag1, flag2, flag3)) else ReturnType(False,
                                                                                                                "Presentation is not being displayed")

    def do_full_screen_presentation(self):
        self.wait_for_element_visible(("xpath", "//div[@class='iconWrapper icon icon--marginRight']"))
        maximize_icon = self.obj.get_element(("xpath", "//div[@class='iconWrapper icon icon--marginRight']"))
        try:
            self.action.move_to_element(maximize_icon).click().perform()
        except:
            pass

    def minimize_full_screen_presentation(self):
        try:
            self.obj.get_element(('xpath', self.presentation_container)).click()
            minimize_icon = self.obj.get_element(("xpath", "//img[contains(@src,'/static/media/fullscreenOn')]"))
            minimize_icon.click()
        except:
            pass

    def are_emojis_displayed(self):
        try:
            element = self.obj.get_element(("xpath", "//div[@class='neo_cl_Reaction']"))
            elements = self.obj.get_child_elements(element, "xpath", ".//*")
            return ReturnType(True, "Emojis are  being displayed") if len(elements) > 0 else ReturnType(False,
                                                                                                        "Emojis are not being displayed")
        except:
            return ReturnType(False, "Emojis are not being displayed")

    # chat forum

    # this method returns a list of tuples (user, text)
    def get_all_chats(self):
        chat_elements = []
        try:

            elements = self.obj.get_elements(("xpath", "//div[@class='cardWrapper']"))
            chat_elements = []
            for element in elements:
                try:
                    sender = self.obj.get_child_element(element, "xpath", ".//div[@class='nameContainer isMe']").text
                except:
                    sender = self.obj.get_child_element(element, "xpath", ".//div[@class='nameContainer']").text
                chat_text = self.obj.get_child_element(element, "xpath", ".//div[@class='messageBox']").text
                chat_elements.append((sender, chat_text))
            return chat_elements
        except:
            return chat_elements

    def verify_tutor_messages_are_left_alligned(self, text="Hi I am tutor"):
        self.wait_for_element_visible(("xpath", self.chat_by_tutor))
        try:
            tutor_chat_elements = self.get_elements(("xpath", self.chat_by_tutor))

            for tutor_chat_element in tutor_chat_elements:
                if tutor_chat_element.text == text:
                    return ReturnType(True, "Tutor chat elements are left aligned")
            return ReturnType(False, "Tutor chat elements are not left aligned")
        except:
            return ReturnType(False, "Tutor chat elements are not left aligned")

    def verify_other_student_messages_are_left_alligned(self, text="Hi I am another student"):
        time.sleep(4)
        chats = self.get_all_chats()

        for chat in chats:
            if text == chat[1]:
                return ReturnType(True, "other student messages are left aligned")
        return ReturnType(False, "other student messages are left aligned")

    def verify_student_messages_are_right_alligned(self, text="Hi I am student"):
        self.wait_for_element_visible(("xpath", self.chat_by_me))
        elements = self.get_elements(("xpath", self.chat_by_me))
        time.sleep(5)
        for element in elements:
            child_element = self.get_child_element(element, "xpath", self.chat_message)
            if child_element.text == text:
                return ReturnType(True, "Student chat elements are right aligned")
        return ReturnType(False, "Student chat elements are right aligned")

    def send_chat(self, text=""):
        try:
            flag_sticker_displayed = self.get_element(("xpath", self.sticker_item)).is_displayed()
        except:
            flag_sticker_displayed = False

        if  flag_sticker_displayed:
            element = self.get_element(("xpath","//div[@class='chatCard isMe']"))
            self.action.move_to_element(element).click().perform()
        self.obj.wait_for_clickable_element_webdriver("//*[@class='sendAction']")
        self.obj.wait_for_element_visible(('xpath', '//input[@placeholder="Type something"]'))
        self.obj.get_element(('xpath', '//input[@placeholder="Type something"]')).send_keys(text)
        element = self.driver.find_element("xpath", "//*[@class='sendAction']")
        element.click()

    def type_chat(self, text=""):
        self.get_element(('xpath', self.type_something_inputcard)).send_keys(text)

    def verify_a_text_in_chat(self, text):
        chats = self.get_all_chats()

        for chat_item in chats:
            if chat_item[1] == text:
                return ReturnType(True, " Chat text is found")
        return ReturnType(False, "Chat text is not found")

    def verify_chat_elements(self):
        try:
            time.sleep(3)
            self.send_chat(text="Hi")
            element = self.obj.get_element(("xpath", "//div[@class='chatContainer__chatheader']"))
            class_forum = self.obj.get_child_element(element, "xpath", ".//div[@class='chatContainer__title']").text
            check.equal(class_forum.lower(), "class forum", "Chat Forum not displayed")
            flag = self.obj.get_child_element(element, "xpath", ".//div[@class='chatContainer__title']").is_displayed()
            check.equal(flag, True, "Icon element not displayed")
            student_count = self.obj.get_child_element(element, "xpath", ".//span[@class='chatContainer__count']").text
            flag = (int(student_count) > 0)
            check.equal(flag, True, "Student count not displayed")
            flag = self.obj.get_element(('xpath', '//input[@placeholder="Type something"]')).is_displayed()
            check.equal(flag, True, "Chat input not displayed")
            flag = self.obj.get_element(("xpath", "//*[@class='sendAction']")).is_displayed()
            check.equal(flag, True, "Send chat button not displayed")
        except:
            check.equal(False, True, "Chat elements incorrectly displayed")

    def verify_chat_elements_element_wise(self, element_type):
        element = self.get_element(("xpath", self.chat_header))
        if element_type.lower() == 'students count':
            student_count = self.get_child_element(element, "xpath", self.chat_member_count).text
            flag = (int(student_count) > 0)
            return ReturnType(True, "Student number is greaater") if flag else ReturnType(False,
                                                                                          "Student number is greaater")
        elif element_type.lower() == "type something":
            flag = self.get_element(("xpath", "//input[@placeholder='Type something']")).is_displayed()
            return ReturnType(True, " Type Something is displayed on chat box") if flag else ReturnType(False,
                                                                                                        "Type some "
                                                                                                        "thing is not "
                                                                                                        "displayed on "
                                                                                                        "place holder")
        elif element_type.lower() == "tutor name":
            flag = self.get_element(("xpath", self.tutor_name)).is_displayed()
            return ReturnType(True, "Tutor name is shown ") if flag else ReturnType(False, "Tutor name is not shown ")
        elif element_type.lower() == 'tutor tag':
            flag = self.get_element(("xpath", self.tutor_title)).is_displayed()
            return ReturnType(True, "Tutor tag is shown ") if flag else ReturnType(False, "Tutor tag is not shown ")

        elif element_type.lower() == 'tutor thumbnail':
            flag = self.get_element(("xpath", self.tutor_thumbnail)).is_deplayed()
            return ReturnType(True, "Tutor thumbnail is shown ") if flag else ReturnType(False,
                                                                                         "Tutor thumbnail is shown ")

    # tutorStreamCard
    def verify_tutor_ui_elements(self, tutor_name='Test Automation'):
        try:
            tut_name = self.obj.get_element(("xpath", "//span[@class='tutorStreamCard__name--big']")).text
            check.equal(tut_name.lower(), tutor_name.lower(), "Tutor name is not correct")
            tut_name_small = self.obj.get_element(("xpath", "//span[@class='tutorStreamCard__name--small']")).text
            check.equal(tut_name_small.lower(), '(tutor)', "Tutor name small is not correct")
        except:
            check.equal(True, False, "Tutor ui element not present")

    def is_tutor_video_on(self):
        try:
            self.obj.wait_for_element_visible(self.tutor_video)
            if self.obj.is_element_present(('xpath', self.tutor_video)):
                return ReturnType(True, "Tutor camera is on")
            else:
                return ReturnType(False, "Tutor camera is off")
        except:
            return ReturnType(False, "Tutor camera is off")

    def is_tutor_mute(self):
        elements = self.obj.get_elements(("xpath", "//div[@class='iconWrapper tutorStreamCard__icon']"))
        try:
            for element in elements:
                if "mic_off" in element.get_attribute("innerHTML"):
                    return ReturnType(True, "Tutor  is mute")

            return ReturnType(False, "Tutor is unmute")
        except:
            return ReturnType(False, "Tutor is unmute")

    def get_no_of_students_card(self):
        elements = self.obj.get_elements(("xpath", "//div[@class='streamList__streamItem']"))
        elements.append(
            self.obj.get_elements(
                ("xpath", "//div[@class='streamList__streamItem streamList__streamItem--localStream']")))
        return len(elements)

    def get_students_from_stream_card(self):
        names = []
        try:
            elements = self.obj.get_elements(("xpath", "//div[@class='streamList__streamItem']"))

            for element in elements:
                name = self.obj.get_child_element(element, "xpath",
                                                  './/div[@class="streamNameClass neo_cl_StreamCard__name '
                                                  'neo_cl_StreamCard__name--nameMaxWidth neo_cl_StreamCard__name--rounded '
                                                  'neo_cl_StreamCard__name--remote"]').text
                names.append(name)

            my_name = self.obj.get_child_element(
                self.obj.get_element(
                    ("xpath", "//div[@class='streamList__streamItem streamList__streamItem--localStream']")),
                "xpath",
                './/div[@class="streamNameClass neo_cl_StreamCard__name neo_cl_StreamCard__name--nameMaxWidth '
                'neo_cl_StreamCard__name--rounded neo_cl_StreamCard__name--local"]').text
            names.append(my_name)
            return names
        except:
            return names

    def get_audio_status_of_student(self, student_name):
        try:
            elements = self.obj.get_elements(("xpath", "//div[@class='streamList__streamItem']"))

            for element in elements:
                name = self.obj.get_child_element(element, "xpath",
                                                  './/div[@class="streamNameClass neo_cl_StreamCard__name '
                                                  'neo_cl_StreamCard__name--nameMaxWidth neo_cl_StreamCard__name--rounded '
                                                  'neo_cl_StreamCard__name--remote"]').text
                if student_name.lower() == name.lower():
                    audio_status = self.obj.get_child_element(elements[1], "xpath",
                                                              ".//div[@class='neo_cl_StreamCard__icon--withRebBg neo_cl_StreamCard__icon']").is_diplayed()
                    return ReturnType(True, "Audio is on") if audio_status else ReturnType(False, "Audio is off")
        except:
            return ReturnType(False, "Audio is off")

    def set_wifi_connection_off(self):
        self.obj.set_wifi_connection_off()

    def set_wifi_connection_on(self):
        self.obj.set_wifi_connection_on()

    def navigate_to_byjus_classes_screen(self):
        self.wait_for_element_visible(("xpath", self.home_byjus_classes_button))
        self.element_click(("xpath", self.home_byjus_classes_button))

    def join_session_from_home_page(self):
        self.wait_for_element_visible(("xpath", self.tlms_mobile_field))
        self.element_click(("xpath", self.home_join_button))

    def join_neo_session_from_classes_page_paid(self):
        self.wait_for_element_visible(("xpath", "//span[@class = 'MuiTab-wrapper']"))

        self.wait_for_element_visible(("xpath", "//div[@class='btnCard']"))
        elements = self.get_elements(("xpath", "//div[@class='listViewContainer']"))
        element = self.get_child_element(elements[1], "xpath",
                                         ".//div[@class='type-video masterOrRegularCardContainer']")
        self.get_child_element(element, "xpath", ".//div[@class='btnCard']").click()
        self.turn_off_mic_from_student_join_page()
        self.turn_off_video_from_student_join_page()
        self.wait_for_clickable_element_webdriver("//span[contains(text(),'Join Class')]")

        self.element_click(("xpath", "//span[contains(text(),'Join Class')]"))

    def turn_off_mic_from_student_join_page(self):
        self.wait_for_element_visible(("xpath", self.mic_video_buttons_on_join_screen))
        elements = self.get_elements(("xpath", self.mic_video_buttons_on_join_screen))

        for ele in elements:
            try:
                self.get_child_element(ele, "xpath", ".//img[@alt='mic']").click()
            except:
                pass

    def turn_off_video_from_student_join_page(self):
        self.wait_for_element_visible(("xpath", self.mic_video_buttons_on_join_screen))
        elements = self.get_elements(("xpath", self.mic_video_buttons_on_join_screen))

        for ele in elements:
            try:
                self.get_child_element(ele, "xpath", ".//img[@alt='cam']").click()
            except:
                pass

    def verify_sticker_displayed(self):
        try:

            self.wait_for_element_visible(("xpath", self.sticker_onchat))
            flag = self.get_element(("xpath", self.sticker_onchat)).is_displayed()
            return  ReturnType(True, " Sticker is being displayed") if flag else ReturnType(False, " Sticker is not being displayed")
        except:
            return ReturnType(False, " Sticker is not being displayed")

    def send_sticker(self):
        try:
            flag_sticker_displayed = self.get_element(("xpath", self.sticker_item)).is_displayed()
        except:
            flag_sticker_displayed = False

        if not flag_sticker_displayed:
            self.element_click(("xpath", self.emoji_icon))
        self.wait_for_element_visible(("xpath", self.sticker_item))
        self.get_element(("xpath", self.sticker_item)).click()

    def verify_no_of_default_stickers(self):
        try:
            self.wait_for_element_visible(("xpath", self.sticker_item))
            stickers = self.get_elements(("xpath", self.sticker_item))
            flag = len(stickers) == 8
            return ReturnType(True, "All eight default stickers are shown") if flag else ReturnType(False,
                                                                                                    "All eight "
                                                                                                    "default stickers "
                                                                                                    "are not shown")
        except:
            return ReturnType(False,
                              "All eight default stickers are not shown")

    def click_on_sticker_icon(self):
        self.wait_for_element_visible(("xpath", self.emoji_icon))
        self.get_element(("xpath", self.emoji_icon)).click()

    def close_sticker_menu(self):
        self.element_click(("xpath","//div[@class = 'self.chat_by_me']"))

    def raise_hand(self):
        if not self.verify_hand_is_raised().result:
            self.wait_for_clickable_element_webdriver(
                (self.raise_hand_button))
            self.get_element(("xpath", self.raise_hand_button)).click()

    def unraise_hand(self):
        if self.verify_hand_is_raised().result:
            self.get_element(("xpath", self.raise_hand_text)).click()

    def verify_lower_hand_text_is_displayed(self):
        try:
            text = self.get_element(("xpath", self.low_hand_text)).text
            flag = 'You lowered your hand. Incase if you have any doubt, you can raise hand so that tutor can approach you.' == text
            return ReturnType(True, "Lower hand message is shown and correct") if flag else ReturnType(False,
                                                                                                       "Lower hand message is shown and not correct")
        except:
            ReturnType(False,
                       "Lower hand message is not shown")

    def verify_hand_is_raised(self):
        try:
            self.wait_for_element_visible(("xpath", self.raise_hand_text))
            flag = self.get_element(("xpath", self.raise_hand_text)).is_displayed()
            return ReturnType(True, "Hand is raised") if flag else ReturnType(False, "Hand is not raised")
        except:
            return ReturnType(False, "Hand is not raised")

    def verify_wifi_off_inchat_displayed(self):
        try:
            flag = self.get_element(("xpath", "//div[@class='chatFooter']")).is_diplayed()
            return ReturnType(True, "wifi off in chat box displayed") if flag else ReturnType(False,
                                                                                              "wifi off in chat box not displayed")
        except:
            return ReturnType(False, "wifi off in chat box not displayed")

    def current_student_has_video_enlarged(self):
        try:
            self.wait_for_element_visible(("xpath", "//div[@class='neo_cl_StreamCard__borderLayer neo_cl_StreamCard__borderLayer--active streamBorderLayerClass"))
            element = self.get_element(("xpath",
                                     "//div[@class='neo_cl_StreamCard__borderLayer neo_cl_StreamCard__borderLayer--active streamBorderLayerClass']"))
            text = element.find_element_by_xpath("..").text
            if text.lower() == 'you' or 'you' in text.lower():
                return ReturnType(True, "Current student has video enlarged")
            else:
                return ReturnType(False, "Current student has not video enlarged")
        except:
            return ReturnType(False, "Current student has not video enlarged")

    def hover_over_info_button(self):
        if not self.verify_info_pop_up().result:

            self.wait_for_element_visible(("xpath", self.class_info_icon))
            self.element_click(("xpath", self.class_info_icon))

    def close_info_pop_up(self):
        element = self.get_element(("xpath", "//div[@class = 'classInfo__infoPopup']"))
        if element.is_displayed():
            self.wait_for_element_visible(("xpath",self.class_info_icon))
            self.element_click(("xpath", self.class_info_icon))

    def hover_over_reaction_button(self):
        element = self.get_element(("xpath", self.thumbs_sticker_icon))
        self.action.move_to_element(element).click().perform()

    def verify_info_pop_up(self, subject_name='Biology: Control and Coordination'):
        try:
            flag = self.get_element(("xpath", "//div[@class = 'classInfo__infoPopup']")).is_displayed()
            text = self.get_element(("xpath", "//div[@class = 'classInfo__topicName']")).text
            flag2 = (text == subject_name)
            flag3 = self.get_element(("xpath", "//div[@class = 'classInfo__dateTime']")).is_displayed()

            return ReturnType(True, " info popup elements are correct and shown") if all((flag3, flag2,
                                                                                          flag)) else ReturnType(False,
                                                                                                                 "info "
                                                                                                                 "popup "
                                                                                                                 "elements are incorrect or not shown")

        except:
            return ReturnType(False, "info popup elements are incorrect or not shown")

    def is_continue_btn_enabled(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        element = self.obj.get_element(('xpath', self.continue_btn_in_rating_popup))
        parent_classname = self.driver.execute_script('return arguments[0].parentNode.className', element)
        if 'Button--disabled' in parent_classname:
            return ReturnType(False, 'continue button is disabled')
        else:
            return ReturnType(True, 'continue button is enabled')

    # by default the cam and mic is 'on' so passing the parameters as cam and mic on

    def join_neo_session_student(self, mic_status, cam_status):
        self.obj.wait_for_locator_webdriver("//div[contains(@class,'neo_cl_Button')]")
        self.obj.element_click(("xpath", "//img[contains(@src,'/static/media/" + mic_status + "')]"))
        time.sleep(2)
        self.obj.element_click(("xpath", "//img[contains(@src,'/static/media/" + cam_status + "')]"))
        time.sleep(2)
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

    def get_selected_emoji_color(self, expected_color):
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

    def switch_to_alt_window(self):
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def is_reaction_icon_disbled(self):
        self.obj.wait_for_locator_webdriver(self.celebrations_icons)
        element = self.obj.get_element(('xpath', self.celebrations_icons))
        parent_classname = self.driver.execute_script('return arguments[0].parentNode.className', element)
        if 'Button--disabled' in parent_classname:
            return ReturnType(False, 'submit button is disabled')
        else:
            return ReturnType(True, 'submit button is enabled')

    def set_network_flaky(self):
        self.obj.set_wifi_connection_off()

    def verify_student_count(self, element_type):
        element = self.obj.get_element(("xpath", self.session_topic_inclass))
        if element_type.lower() == 'students count':
            student_count = self.obj.get_element(("xpath", self.chat_member_count)).text
            flag = (int(student_count) > 0)
            return ReturnType(True, "Student number is greaater") if flag else ReturnType(False,
                                                                                          "Student number is greater")

    def click_on_session_topic(self):
        self.obj.wait_for_element_visible(("xpath", self.session_topic_inclass))
        self.obj.element_click(("xpath", self.session_topic_inclass))

    def refresh_and_join_the_session(self, mic_status, cam_status):
        self.obj.page_refresh()
        self.join_neo_session_student(mic_status, cam_status)

    def tool_tip_message(self, message):
        try:
            tooltip_elements = self.get_elements(("xpath", "//span[@class = 'neo_cl_ToolTipText']"))
            selected_tool_tip_element = None
            for element in tooltip_elements:
                if element.text == message:
                    selected_tool_tip_element = element
                    break
            flag = selected_tool_tip_element.is_displayed()
            return ReturnType(True, "Tool tip message {}  is being shown".format(message)) if flag else ReturnType(
                False, "Tool tip message {}  is not being shown".format(message))
        except:
            return ReturnType(False, "Tool tip message {}  is not being shown".format(message))

    def turn_on_off_mic(self, status):
        try:
            if status.lower() == 'on':
                self.wait_for_element_visible(("xpath", "//img[@class = 'iconWrapper__icon']"))
                elements = self.get_elements(
                    ("xpath", "//div[@class = 'iconWrapper icon icon--marginRight icon--off']"))
                for element in elements:
                    if "mic-off" in element.get_attribute("innerHTML"):
                        element.click()
                        break
            else:
                self.wait_for_element_visible(("xpath", "//img[@class = 'iconWrapper__icon']"))
                elements = self.get_elements(("xpath", "//div[@class = 'iconWrapper icon icon--marginRight icon--on']"))
                for element in elements:
                    if "mic-on" in element.get_attribute("innerHTML"):
                        element.click()
                        break

        except:
            pass

    def turn_on_off_camera(self, status):
        try:
            if status.lower() == 'on':
                self.wait_for_element_visible(("xpath", "//img[@class = 'iconWrapper__icon']"))
                elements = self.get_elements(
                    ("xpath", "//div[@class = 'iconWrapper icon icon--marginRight icon--off']"))
                for element in elements:
                    if "cam-off" in element.get_attribute("innerHTML"):
                        element.click()
                        break
            else:
                self.wait_for_element_visible(("xpath", "//img[@class = 'iconWrapper__icon']"))
                elements = self.get_elements(("xpath", "//div[@class = 'iconWrapper icon icon--marginRight icon--on']"))
                for element in elements:
                    if "cam-on" in element.get_attribute("innerHTML"):
                        element.click()
                        break
        except:
            pass

    def is_weak_signal_present(self):
        self.obj.wait_for_locator_webdriver(self.weak_signal_indicator)
        if self.obj.is_element_present(('xpath', self.weak_signal_indicator)):
            return ReturnType(True, 'weak signal indicator is displayed')
        else:
            return ReturnType(False, 'weak signal indicator is not present')

    def is_discuss_doubt_msg_present(self):
        try:
            self.obj.wait_for_locator_webdriver\
                (self.discuss_doubt_msg)
            ele = self.obj.get_element(('xpath', self.discuss_doubt_msg))
            if 'Tutor want to discuss doubt with you. Please turn on your camera' in ele.text:
                return ReturnType(True, 'the text in popup doesnt match')
            else:
                return ReturnType(False, 'the text in popup doesnt match')
        except:
            return ReturnType(False, 'the text in popup doesnt match')

    def click_on_hand_raise(self):
        time.sleep(5)
        self.obj.wait_for_clickable_element_webdriver(self.handraise_icon)
        self.obj.element_click(('xpath', self.handraise_icon))

    def is_play_pause_btn_present(self):
        self.obj.wait_for_locator_webdriver(self.focus_mode_icon)
        if self.obj.is_element_present(('xpath', self.pause_video_btn)) or self.obj.is_element_present(
                ('xpath', self.play_video_btn)):
            return ReturnType(True, 'play or pause btn is displayed')
        else:
            return ReturnType(False, 'play or pause btn is not present')

    def mic_cam_status_in_focus_mode(self):
        self.obj.wait_for_locator_webdriver(self.focus_mode_icon)
        if self.obj.is_element_present(('xpath', self.mic_disabled_by_tutor)) and \
                self.obj.is_element_present(('xpath', self.student_video_off)) or \
                self.obj.is_element_present(('xpath', self.student_cam_on)):
            return ReturnType(True, 'mic and cam status are displayed as expected')
        else:
            return ReturnType(False, 'mic and cam status are not displayed as expected')

    def is_student_speaking(self):
        self.obj.wait_for_locator_webdriver(self.student_speaking)
        if self.obj.is_element_present(('xpath', self.student_speaking)):
            return ReturnType(True, 'student audio is on and speaking')
        else:
            return ReturnType(False, 'none of the students are speaking')

    def verify_users_in_chronological_order(self, user1, user2, user3):
        users = self.obj.get_elements(('xpath', '//div[contains(@class,"streamNameClass")]'))
        user_name = [user1, user2, user3]
        for i, user in enumerate(users):
            print(user.text)
            if user_name[i] == user.text:
                print(user_name[i])
            else:
                return ReturnType(False, 'users are not in chronological order')

        return ReturnType(True, 'users are in chronological order')

    def navigate_to_home_click_on_join(self):
        self.obj.element_click(('xpath', self.byjus_logo))
        self.home_click_on_join()

    def verify_ask_question_popup_is_displayed(self,
                                               message='Tutor want to discuss doubt with you. Please turn on your mic and camera'):
        try:
            element = self.get_element(("xpath", "//div[@class = 'bottomContainer__profile']"))
            flag = element.is_displayed()
            text = self.get_element(("xpath", "//div[@class= 'bottomContainer__requestMessage']")).text
            flag2 = message == text
            elements = self.get_elements(("xpath",
                                          "//div[@class = 'profileCard bottomContainer__profileCard bottomContainer__profileCard--main']"))
            elements += self.get_elements(("xpath",
                                           "//div[@class = 'profileCard bottomContainer__profileCard bottomContainer__profileCard--sec']"))
            flag3 = len(elements) > 0
            return ReturnType(True, "Ask question pop is verified and correct") if all(
                (flag, flag2, flag3)) else ReturnType(False, "Ask question pop is not correct or displayed")
        except:
            return ReturnType(False, "Ask question pop is not correct or displayed")

    def click_on_camera_mic_disabled(self):
        elements = self.obj.get_elements(("xpath", "//div[@class='iconWrapper tutorStreamCard__icon']"))
        try:
            for element in elements:
                if "camera-off" in element.get_attribute("innerHTML"):
                    element.click()
            for element in elements:
                if "mic_off" in element.get_attribute("innerHTML"):
                    element.click()

            return ReturnType(False, "Tutor camera or mic is clickable")
        except:
            return ReturnType(True, "Tutor camera or mic is not clickable")

    def are_steam_student_arrow_button_displayed(self):
        try:
            flag_left = self.get_element(("xpath",
                                          "//div[@class = 'streamList__scrollerBtns streamList__scrollerBtns--left streamList__scrollerBtns--disabled']")).is_displayed()
            flag_right = self.get_element(
                ("xpath", "//div[@class = 'streamList__scrollerBtns streamList__scrollerBtns--right']")).is_displayed()

            return ReturnType(True, "Stream arrow buttons are displayed") if all(
                (flag_right, flag_left)) else ReturnType(False, "Stream arrow buttons are not displayed")
        except:
            return ReturnType(False, "Stream arrow buttons are not displayed")

    def scroll_students_card(self, towards='right'):
        try:
            if towards.lower() == 'right':
                self.element_click(
                    ("xpath", "//div[@class = 'streamList__scrollerBtns streamList__scrollerBtns--right']"))
            else:
                self.element_click(("xpath",
                                    "//div[@class = 'streamList__scrollerBtns streamList__scrollerBtns--left']"))
        except:
            pass

    def verify_students_after_scrolling_left(self):
        try:
            elements = self.get_elements(
                ("xpath", "//div[@class= 'streamList__streamItem streamList__streamItem--localStream']"))
            elements += self.get_elements(("xpath", "//div[@class= 'streamList__streamItem']"))
            initial_number = len(elements)
            self.scroll_students_card(towards='left')
            elements = self.get_elements(
                ("xpath", "//div[@class= 'streamList__streamItem streamList__streamItem--localStream']"))
            elements += self.get_elements(("xpath", "//div[@class= 'streamList__streamItem']"))
            final_number = len(elements)
            flag = final_number >= initial_number

            return ReturnType(True, "Students are scrolled to left if clicked on left arrow") if flag else ReturnType(
                False, "Students are not scrolled to left if clicked on left arrow")
        except:
            return ReturnType(False, "Students are not scrolled to left if clicked on left arrow")

    def verify_students_after_scrolling_right(self):
        try:
            elements = self.get_elements(
                ("xpath", "//div[@class= 'streamList__streamItem streamList__streamItem--localStream']"))
            elements += self.get_elements(("xpath", "//div[@class= 'streamList__streamItem']"))
            initial_number = len(elements)
            self.scroll_students_card()
            elements = []
            elements = self.get_elements(
                ("xpath", "//div[@class= 'streamList__streamItem streamList__streamItem--localStream']"))
            elements += self.get_elements(("xpath", "//div[@class= 'streamList__streamItem']"))
            final_number = len(elements)
            flag = final_number >= initial_number

            return ReturnType(True, "Students are scrolled to right if clicked on right arrow") if flag else ReturnType(
                False, "Students are not scrolled to right if clicked on right arrow")
        except:
            return ReturnType(False, "Students are not scrolled to right if clicked on right arrow")

    def scroll_till_end_on_student_card(self):
        try:
            while (True):
                self.scroll_students_card()
                if self.get_element(("xpath",
                                     "//div[@class = 'streamList__scrollerBtns streamList__scrollerBtns--right streamList__scrollerBtns--disabled']")).is_displayed():
                    return ReturnType(True, "Able to scroll to rightmost")
        except:
            return ReturnType(False, "Not able to scroll to rightmost")

    def scroll_till_left_end_on_student_card(self):
        try:
            while (True):
                self.scroll_students_card(towards="left")
                if self.get_element(("xpath",
                                     "//div[@class = 'streamList__scrollerBtns streamList__scrollerBtns--left streamList__scrollerBtns--disabled']")).is_displayed():
                    return ReturnType(True, "Able to scroll to leftmost")
        except:
            return ReturnType(False, "Not able to scroll to lefttmost")

    def verify_hand_is_raised_for_student(self, student_name='you'):
        if student_name == 'you':
            return self.verify_hand_is_raised()
        else:
            try:
                elements = self.get_elements(("xpath", "//div[@class = 'neo_cl_StreamCard neo_cl_StreamCard__basic streamContainer']"))
                required_student = None
                for element in elements:
                    self.action.move_to_element(element).perform()
                    name = self.get_child_element(element, "xpath",
                                                  ".//div[@class = 'neo_cl_VideoContainer__overlay_view  neo_cl_VideoContainer__overlay_view--bottomLeft']").text
                    if name.lower() == student_name.lower():
                        required_student = element
                        break
                if required_student is not None:
                    try:
                        flag = self.get_child_element(required_student, "xpath",
                                                      ".//div[@class = 'neo_cl_StreamCard__icon--withDarkBlackBg neo_cl_StreamCard__icon']").is_displayed()
                        return ReturnType(True, "Student raise hand icon is shown") if flag else ReturnType(False,
                                                                                                            "Student raise hand icon is shown")
                    except:
                        return ReturnType(False, "Raise hand icon is not displayed")
                else:
                    return ReturnType(False, "Student card is not shown with name {}".format(student_name))
            except:
                return ReturnType(False, "Student card is not shown with name {}".format(student_name))

    def verify_hands_down_message(self):
        try:
            self.wait_for_element_visible(("xpath","//div[@class = 'messageClass__toastContent']"))
            flag = self.get_element(("xpath","//div[@class = 'messageClass__toastContent']")).is_displayed()
            return ReturnType(True, "Tutor hands down message is displayed") if flag else ReturnType(False, "Tutor hands down message is not displayed")
        except:
            return ReturnType(False, "Tutor hands down message is not displayed")

    def verify_thumbs_reaction_icon_displayed(self):
        try:
            flag = self.get_element(("xpath",self.thumbs_sticker_icon)).is_displayed()
            return ReturnType(True,"Thumb icon is displayed") if flag else ReturnType(False,"Thumb icon is not being displayed")

        except:
            return ReturnType(False, "Thumb icon is not being displayed")

    def click_on_reaction_thumb_icon(self):
        self.wait_for_element_visible(("xpath", self.thumbs_sticker_icon))
        self.get_element(("xpath", self.thumbs_sticker_icon)).click()

    def is_chat_disabled_message_dislayed(self, message = 'Live Chat is disabled'):
        try:
            text = self.get_element(("xpath", "//div[@class = 'chatFooter']")).text
            return ReturnType(True, "Chat disabled message is displayed") if text == message else  ReturnType(False, "Chat disabled message is now displayed")
        except:
            return ReturnType(False, "Chat disabled message is not displayed")


    def verify_other_student_mic_cam_cannt_be_controlled(self):
        try:
            WebDriverWait(self.driver, 2).until(
                ec.element_to_be_clickable((By.XPATH, "neo_cl_StreamCard__icon--withRebBg neo_cl_StreamCard__icon")))
            return ReturnType(False, "other student mic camera are controllable")
        except:
            return ReturnType(True, "other student mic camera are not controllable")

    # pre-class experience
    def is_photo_edit_icon_present(self):
        self.wait_for_locator_webdriver(self.photo_edit_icon)
        return self.obj.is_element_present(("xpath", self.photo_edit_icon))

    def click_photo_edit_icon(self):
        self.wait_for_locator_webdriver(self.current_student_bubble)
        self.obj.element_click(("xpath", self.current_student_bubble))
        self.obj.element_click(("xpath", self.photo_edit_icon))

    def verify_change_profile_photo_popup(self):
        self.wait_for_locator_webdriver(self.change_pp_header)
        flag1 = self.obj.is_element_present(("xpath",self.change_pp_header))
        flag2 = self.obj.is_element_present(("xpath", self.upload_photo_link))
        return flag1 and flag2

    def close_profile_photo_popup(self):
        self.obj.element_click(("xpath", self.close_popup_icon))
        self.obj.wait_for_invisibility_of_element(("xpath", self.close_popup_icon))
        flag = self.obj.is_element_present(("xpath", self.photo_popup_header))
        return flag

    def upload_photo(self, file):
        self.click_photo_edit_icon()
        current_location = os.path.dirname(os.path.abspath(__file__))
        location = os.path.normpath(os.path.join(current_location, file))
        self.obj.wait_for_locator_webdriver(self.upload_photo_input)
        self.get_element(('xpath', self.upload_photo_input)).send_keys(location)

    def upload_profile_photo_api(self, image_file):
        url = "https://api.tllms.com/staging/tutor_plus_web/web/neo/students/profile"

        current_location = os.path.dirname(os.path.abspath(__file__))
        location = os.path.normpath(os.path.join(current_location, image_file))
        test_file = open(location, "rb")
        b64file = base64.b64encode(test_file.read())
        base64_image = "data:image/jpeg;base64," + b64file.decode('ascii')
        payload = {"profile_photo": base64_image}

        access_token = self.driver.execute_script("return window.localStorage.getItem('accessToken');")
        user_details = self.driver.execute_script("return window.localStorage.getItem('reduxPersist:user');")
        user_details_dict = json.loads(user_details)
        user_id = user_details_dict['user']['id']
        headers = {'authorization': 'Bearer ' + access_token, 'x-tnl-user-id': str(user_id)}

        response = requests.put(url, payload, headers=headers)
        if response.ok:
            print("Upload completed successfully!")
        else:
            print("Failed due to %s " %response.reason)
            # print(response.text)
        return response.ok

    def verify_adjust_photo_popup(self):
        try:
            crop_box = self.obj.get_element(("xpath",self.pro_photo_crop_box))
            before_adjust_transform_px = crop_box.value_of_css_property('transform').replace('matrix(','').replace(')','').split(",")
            self.action.drag_and_drop_by_offset(crop_box, 30, 0).perform()
            after_adjust_transform_px = crop_box.value_of_css_property('transform').replace('matrix(','').replace(')','').split(",")
            return ReturnType(True,"Adjusted profile photo to right by 30 pixels") if int(float(before_adjust_transform_px[4])) + 30 == int(float(after_adjust_transform_px[4])) \
                else ReturnType(False,"Photo did not get adjusted to right by 30 pixels")
        except:
            return ReturnType(False,"Photo did not get adjusted to right by 30 pixels")

    def click_on_change_button(self):
        self.obj.wait_for_locator_webdriver(self.change_photo)
        self.obj.element_click(("xpath", self.change_photo))

    def save_selected_photo(self):
        self.obj.wait_for_locator_webdriver(self.save_photo)
        self.obj.element_click(("xpath", self.save_photo))

    def verify_photo_approval_pending(self):
        self.obj.wait_for_locator_webdriver(self.current_student_bubble_pp)
        flag1 = self.obj.is_element_present(("xpath", self.photo_approval_pending))
        flag2 = self.obj.is_element_present(("xpath", self.current_student_bubble_pp))
        return flag1 and flag2

    def verify_toast_message(self, expected_message):
        time.sleep(1)
        self.obj.wait_for_locator_webdriver(self.toast_container)
        message = self.obj.get_element(("xpath", self.toast_container)).text
        return True if message == expected_message else False

    def page_refresh(self):
        self.obj.page_refresh()

    def approved_profile_pic_visible(self):
        self.obj.wait_for_locator_webdriver(self.current_student_bubble_pp)
        flag1 = self.obj.is_element_present(("xpath", self.current_approved_name_image))
        flag2 = self.obj.is_element_present(("xpath", self.current_student_bubble_pp))
        return flag1 and flag2

    def close_toast_message(self):
        self.obj.wait_for_locator_webdriver("//span[@class='MuiIconButton-label']")
        self.obj.element_click(('xpath', "//span[@class='MuiIconButton-label']"))

    def get_current_student_bubble(self, profile_name):
        self.obj.wait_for_locator_webdriver(self.current_student_bubble_pp)
        card = self.obj.get_element(('xpath', self.current_student_bubble_pp))
        profile_pic_src = card.get_attribute("src")
        name_first_letter = profile_name[0]
        if "https://static.tllms.com/assets/k12/premium_online/byjus_classes/common/initial_avatars/" + name_first_letter + ".png" == profile_pic_src:
            return ReturnType(True, "Initial avatar/name first letter is shown on bubble")
        else:
            return ReturnType(False, "Initial avatar/name first letter is not displayed on bubble")

    def hover_over_student_bubble_approval_pending(self):
        try:
            self.wait_for_locator_webdriver(self.current_student_bubble)
            before_hover_over_bubble = self.obj.get_element(("xpath", self.current_student_bubble)).value_of_css_property('transform').replace('matrix(','').replace(')','').split(",")
            # self.obj.element_click(("xpath", self.current_student_bubble))
            hov = self.action.move_to_element(self.obj.get_element(("xpath", self.current_student_bubble)))
            hov.click().perform()
            after_hover_over_bubble = self.obj.get_element(("xpath", self.current_student_bubble)).value_of_css_property('transform').replace('matrix(','').replace(')','').split(",")
            a = float(before_hover_over_bubble[0])
            b = float(after_hover_over_bubble[0])
            return ReturnType(True, "Student bubble hovered over") if a < b else ReturnType(False, "Student bubble did not get hovered over")
        except Exception as e:
            return ReturnType(False, "Unable to hover over student bubble due to exception %s" % str(e))