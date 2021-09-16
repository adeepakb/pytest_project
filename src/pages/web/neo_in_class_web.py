import time

from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from utilities.common_methods_web import CommonMethodsWeb
import pytest_check as check


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
        self.rating_options = ('xpath', "//div[contains(@class,'rating__item')]")
        self.turn_on_cam_tooltip = "//span[text()='Turn on Camera']"
        self.turn_off_cam_tooltip = "//span[text()='Turn off Camera']"
        self.turn_on_mic_tooltip = "//span[text()='Turn on Microphone']"
        self.turn_off_mic_tooltip = "//span[text()='Turn off Microphone']"
        self.cam_disabled_tooltip = "//span[text()='Camera disabled by tutor']"
        self.mic_disabled_tooltip = "//span[text()='Microphone disabled by tutor']"
        self.feedback_options = '//div[@class="rating__card-item"]'
        self.continue_btn_in_rating_popup = "//span[text()='Continue']"
        self.feedback_submit_btn = "//div[text()='Submit']"
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
        self.tutor_name = "//div[@class = 'tutorStreamCard__name--big']"
        self.tutor_title = "//div[@class = 'tutorStreamCard__name--small']"
        self.tutor_thumbnail = "//div[@class = 'neo_cl_VideoContainer__overlay']"
        self.tutor_controls_container = "//div[@class='iconWrapper tutorStreamCard__icon']"
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
        self.sticker_onchat = "//div[@class= 'message']"
        self.emoji_icon = "//*[@class='emoji']"
        self.raise_hand = "//div[@class='iconWrapper icon icon--marginLeft icon--whitebg']"
        self.raise_hand_text = "//div[@class='bottomContainer__raiseHandText']"
        self.low_hand_text = "//div[@class='insideClass__lowerHandMessage']"

    def home_click_on_join(self):
        self.obj.wait_for_element_visible(('xpath',"//span[text()='JOIN']"))
        self.obj.button_click('JOIN')

    def join_neo_session(self):
        self.obj.wait_for_locator_webdriver("//div[contains(@class,'neo_cl_Button')]")
        self.obj.wait_for_clickable_element_webdriver("//div[contains(@class,'neo_cl_Button')]")
        time.sleep(3)
        self.obj.element_click(("xpath","//div[contains(@class,'neo_cl_Button')]"))

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
            option = self.obj.get_elements(
                ('xpath', "//img[contains(@src,'/static/media/classes-emoji-" + celeb_symbol + "')]"))
            self.action.move_to_element(option).click().perform()
        except:
            check.equal(False, True, "Couldn't click on the option")

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

    def select_any_option_in_facing_issue(self, string_val):
        options = self.obj.get_elements(self.facing_issue_options)
        for option in options:
            if option.text in string_val:
                option.click()
                break

    def verify_issue_checked(self, expected_issue):
        return ReturnType(True, 'Student able to select issue') if self.obj.get_element(('xpath', self.checked_issue_text)).text == expected_issue \
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

    def is_text_match(self,text):
        return self.obj.is_text_match(text)

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

    def is_email_icon_present(self):
        self.obj.wait_for_locator_webdriver(self.email_icon)
        return self.obj.is_element_present(('xpath',self.email_icon))

    def submitted_popup_disappear(self):
        self.obj.wait_for_invisibility_of_element(('xpath',"//*[@class='timeRemaining']"),10)
        return self.obj.is_element_present(('xpath',"//*[@class='reportIssue__submitted']"))

    def page_refresh_issue_popup_disappear(self):
        self.obj.page_refresh()
        return self.obj.is_element_present(('xpath',self.facing_issue_header))

    def page_refresh_issue_submitted_issue_popup_disappear(self):
        self.obj.page_refresh()
        return self.obj.is_element_present(('xpath',"//*[@class='reportIssue__submitted']"))

    def get_inclass_student_video_status(self):
        student_video_status = {}
        self.obj.wait_for_locator_webdriver(self.student_video)
        try:
            if self.obj.is_element_present(('xpath', self.student_video_off)):
                student_video_status["video_disbled_desc"] = "off by student"
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

    # session details

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

    # rating popup
    def verify_header_in_rating_popup(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        ele = self.obj.get_element(('xpath', self.rating_popup_header)).text
        flag = "Rate your experience" in ele
        check.equal(flag, True, "the text in popup doesn't match")

    def is_close_icon_in_rating_popup_present(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_close_icon)
        return self.obj.is_element_present(('xpath', self.rating_popup_close_icon))

    def verify_the_text_in_rating_popup(self):
        self.obj.wait_for_locator_webdriver(self.rating_popup_header)
        ele = self.obj.get_element(('xpath', self.text_in_rating_popup)).text
        flag = "How was your class" in ele
        check.equal(flag, True, "the text in popup doesn't match")

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
        ele = self.obj.get_element(('xpath', self.header_text_in_feedback)).text
        flag = "How was your experience with your tutor?" in ele
        check.equal(flag, True, "the text in popup doesn't match")

    def select_any_feedback_option(self, feedback_opt):
        try:
            options = self.obj.get_elements(self.feedback_options)
            for option in options:
                if option.text in feedback_opt:
                    option.click()
                    break
        except:
            check.equal(False, True, "Couldn't click on the option")

    def verify_text_in_Thank_you_popup(self):
        self.obj.wait_for_locator_webdriver(self.text_in_thank_you_popup)
        ele = self.obj.get_element(('xpath', self.text_in_thank_you_popup)).text
        flag = "Thank you for your feedback!" in ele
        check.equal(flag, True, "the text in popup doesn't match")

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

            element = self.obj.get_element(("xpath", "//div[@class='presentation__view']"))
            element2 = self.obj.get_child_element(element, "xpath",".//div[@class='presentation__slide']")
            return ReturnType(True, "Video is being presented") if element2 else ReturnType(False,
                                                                                            "Video is not being presented")
        except:
            return ReturnType(False, "Video is not being presented")

    def is_presentation_displayed(self):
        flag1 = self.is_image_presented().result
        flag2 = self.is_blank_screen_presented().result
        flag3 = self.is_video_being_presented()
        return ReturnType(True, "Presentation is being displyed") if any((flag1, flag2, flag3)) else ReturnType(False,
                                                                                                                "Presentation is not being displayed")

    def do_full_screen_presentation(self):
        maximize_icon = self.obj.get_element(("xpath", "//div[@class='iconWrapper icon icon--marginRight']"))
        self.action.move_to_element(maximize_icon).click().perform()

    def minimize_full_screen_presentation(self):
        maximize_icon = self.obj.get_element(
            ("xpath", "//div[@class='iconWrapper icon icon--whitebg icon--marginLeft icon--lightBlack']"))
        self.action.move_to_element(maximize_icon).click().perform()

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
        try:
            tutor_chat_elements = self.get_elements(("xpath", self.chat_by_tutor))

            for tutor_chat_element in tutor_chat_elements:
                if tutor_chat_element.text == text:
                    return ReturnType(True, "Tutor chat elements are left aligned")
            return ReturnType(False, "Tutor chat elements are not left aligned")
        except:
            return ReturnType(False, "Tutor chat elements are not left aligned")

    def verify_other_student_messages_are_left_alligned(self, text="Hi I am another student"):
        chats = self.get_all_chats()

        for chat in chats:
            if text == chat[1]:
                return ReturnType(True, "other student messages are left aligned")
        return ReturnType(False, "other student messages are left aligned")

    def verify_student_messages_are_right_alligned(self, text="Hi I am student"):
        elements = self.get_elements(("xpath",self.chat_by_me))

        for element in elements:
            child_element = self.get_child_element(element, "xpath", self.chat_message)
            if child_element.text == text:
                return ReturnType(True, "Student chat elements are right aligned")
        return ReturnType(False, "Student chat elements are right aligned")

    def send_chat(self, text=""):
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
        return ReturnType(True, "Chat text is not found")

    def verify_chat_elements(self):
        try:
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
        elif element_type.lower == "tutor name":
            flag = self.get_element(("xpath", self.tutor_name)).is_displayed()
            return ReturnType(True, "Tutor name is shown ") if flag else ReturnType(False, "Tutor name is not shown ")
        elif element_type.lower() == 'tutor tag':
            flag = self.get_element(("xpath", self.tutor_title)).is_displayed()
            return ReturnType(True, "Tutor tag is shown ") if flag else ReturnType(False, "Tutor tag is not shown ")

        elif element_type.lower() == 'tutor thumbnail':
            flag = self.get_element(("xpath",self.tutor_thumbnail)).is_deplayed()
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
        elements = self.obj.get_elements(("xpath", "//div[@class='iconWrapper tutorStreamCard__icon']"))
        try:
            child_element = self.obj.get_child_element(elements[1], "xpath", ".//*[@class='iconWrapper__icon']")
            flag = self.action.move_to_element(child_element).click().perform()
            flag2 = self.obj.get_child_element(elements[1], "xpath",
                                           ".//*[@class='iconWrapper__icon']").is_displayed()
            return ReturnType(True, "Tutor  Video is on.") if not flag2 else ReturnType(False,
                                                                                        "Tutor  Video is not on.")
        except:
            return ReturnType(True, "Tutor  Video is  on. except")

    def is_tutor_unmute(self):
        try:
            elements = self.obj.get_elements(("xpath", "//div[@class='iconWrapper tutorStreamCard__icon']"))
            child_element = self.obj.get_child_element(elements[0], "xpath", ".//*[@class='iconWrapper__icon']")
            flag = self.action.move_to_element(child_element).click().perform()
            flag2 = self.obj.get_child_element(elements[0], "xpath",
                                           ".//*[@class='iconWrapper__icon']").is_displayed()
            return ReturnType(False, "Tutor is not unmute.") if flag2 else ReturnType(True, "Tutor is unmute")
        except:
            return ReturnType(True, "Tutor is unmute. except")

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

    def launch_student_webiste(self, mobile_number="2013795859"):
        try:
            self.chrome_driver.get(self.learn_login_url)
            self.wait_for_element_visible("xpath", self.byju_home_icon)
            self.element_click(("xpath",self.byju_home_icon))

            self.enter_text(mobile_number, ("xpath", self.byjus_login_number_field))
            self.element_click(('xpath', self.next_button))
            self.wait_for_element_visible(("xpath",self.login_otp_field))
            otp = self.get_otp(mobile_number)
            self.enter_text(otp, ("xpath", self.login_otp_field))
            self.element_click(("xpath",self.otp_proeed_button))
            self.wait_for_element_visible(("xpath", self.tlms_mobile_field))
        except:
            raise Exception('Student home page not launched')

    def get_otp(self, mobile_number):
        try:
            self.tlms.login_to_staging()
            self.wait_for_element_visible_driver(self.chrome_driver_tlms, ("xpath", self.tlms_otp_tab))
            self.chrome_driver_tlms.find_element_by_xpath(self.tlms_otp_tab).click()
            self.chrome_driver_tlms.find_element_by_xpath(self.tlms_otp_tab_list).click()
            self.chrome_driver_tlms.find_element_by_xpath(self.tlms_mobile_field).send_keys(
                "+91-" + mobile_number)
            self.chrome_driver_tlms.find_element_by_xpath(self.tlms_otp_submit)
            self.chrome_driver_tlms.find_element_by_xpath(self.tlms_otp_submit).click()
            element = self.chrome_driver_tlms.find_elements_by_xpath('//*[@class="odd"]')
            otp_text = self.chrome_driver_tlms.find_element_by_xpath(self.tlms_otp_number_field).text
            return otp_text
        except:
            raise Exception("Otp not found")

    def navigate_to_byjus_classes_screen(self):
        self.wait_for_element_visible(("xpath", self.home_byjus_classes_button))
        self.element_click(("xpath", self.home_byjus_classes_button))

    def join_session_from_home_page(self):
        self.wait_for_element_visible(("xpath",self.tlms_mobile_field))
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
        elements = self.get_elements(("xpath",self.mic_video_buttons_on_join_screen))

        for ele in elements:
            try:
                self.get_child_element(ele, "xpath", ".//img[@alt='cam']").click()
            except:
                pass

    def verify_sticker_displayed(self):

        elements = self.get_elements(("xpath",self.sticker_onchat))

        for element in elements:
            if "src" in element.get_attribute('innerHTML'):
                return ReturnType(True, " Sticker is being displayed")
        return ReturnType(False, " Sticker is not being displayed")

    def send_sticker(self):
        self.get_element(("xpath", self.emoji_icon)).click()
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

    def raise_hand(self):
        self.wait_for_element_visible(
            ("xpath",self.raise_hand))
        self.get_element(("xpath", self.raise_hand)).click()

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
            self.wait_for_element_visible(("xpath",self.raise_hand_text))
            flag = self.get_element(("xpath",self.raise_hand_text)).is_displayed()
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
