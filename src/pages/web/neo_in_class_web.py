import re
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

    def is_thumb_icon_present(self):
        self.obj.wait_for_locator_webdriver(self.thumb_icon)
        return self.obj.is_element_present(('xpath', self.thumb_icon))

    def is_kebab_menu_present(self):
        self.obj.wait_for_locator_webdriver(self.kebab_menu)
        return self.obj.is_element_present(('xpath', self.kebab_menu))

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

    def is_close_icon_in_facing_issues_present(self):
        self.obj.wait_for_locator_webdriver(self.close_icon_in_facing_issues)
        return self.obj.is_element_present(('xpath', self.close_icon_in_facing_issues))

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

    def get_inclass_student_video_status(self):
        self.obj.wait_for_locator_webdriver(self.student_video)
        try:
            if self.obj.is_element_present(('xpath', self.student_video_off)):
                return ReturnType(False, "off by student")
            elif self.obj.is_element_present(('xpath', self.student_video_off_by_tutor)):
                return ReturnType(False, "off by tutor")
        except(NoSuchElementException):
            return ReturnType(True, "cam is on")

    def get_inclass_student_audio_status(self):
        self.obj.wait_for_locator_webdriver(self.student_audio)
        try:
            if self.obj.is_element_present(('xpath', self.student_audio_off)):
                return ReturnType(False, "off by student")
            elif self.obj.is_element_present(('xpath', self.student_audio_off_by_tutor)):
                return ReturnType(False, "off by tutor")
        except(NoSuchElementException):
            return ReturnType(True, "mic is on")


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

    # in class presentation

    # def join_class(self):
    #     self.chrome_driver.get("https://learn-staging.byjus.com/live-classes/457828")
    #     self.send_chat()
    #     print()

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
            element2 = self.obj.get_child_element(element, "xpath",
                                              ".//div[@class='presentation__slide']")
            return ReturnType(True, "Video is being presented") if element2 else ReturnType(False,
                                                                                            "Video is not being "
                                                                                            "presented")
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
                                                                                                        "Emojis are "
                                                                                                        "not being "
                                                                                                        "displayed")
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

    def send_chat(self, text=""):
        self.obj.get_element(('xpath', '//input[@placeholder="Type something"]')).send_keys(text)
        element = self.driver.find_element("xpath", "//*[@class='sendAction']")
        element.click()

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
            self.obj.get_elements(("xpath", "//div[@class='streamList__streamItem streamList__streamItem--localStream']")))
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
