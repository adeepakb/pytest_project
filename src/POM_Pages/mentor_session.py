import time
import logging
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from subprocess import getoutput
from Utilities.common_methods import CommonMethods
from POM_Pages.staging_tlms import Stagingtlms
from Constants.load_json import getdata
from Utilities.tutor_common_methods import TutorCommonMethods


class MentorSession:
    def __init__(self, driver):
        self.driver = driver
        self.obj = TutorCommonMethods(driver)
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.tlms = Stagingtlms(driver)
        self.tutor_white_board = '//*[@class = "whiteboardCanvas"]'
        self.highlighter_icon = "//img[contains(@src,'select.b2bc79b8.svg')]"
        self.pen_icon = "//img[contains(@src,'pen.026479fc.svg')]"
        self.eraser_icon = "//img[contains(@src,'eraser.73769529.svg')]"
        self.text_icon = "//img[contains(@src,'text.4b6d2121.svg')]"
        self.filler_icon = "//img[contains(@src,'highlighter.dee931ad.svg')]"
        self.square_icon = "//img[contains(@src,'shape-square.db53c1cd.svg')]"
        self.triangle_icon = "//img[contains(@src,'shape-triangle.5bd96830.svg')]"
        self.circle_icon = "//img[contains(@src,'shape-circle.a77153c9.svg')]"
        self.line_icon = "//img[contains(@src,'shape-line.702ef493.svg')]"
        self.byjus_icon = "//img[contains(@src,'data:image/png')]"
        self.subject = '//*[@class = "subjectText"]'
        self.topic = '//*[@class = "topicText"]'
        self.video = '//div[@id = "agora_local"]'
        self.chat_container = '//div[@class= "chatContainer"]'
        self.chat_toggle = '//span[@class= "MuiSwitch-root"]'
        self.live_chat_close= "//img[@class='chatCloseIcon']"
        self.end_button_timer= '//*[@class= "session-button timer"]'
        self.end_button ='//*[text() = "End Session Now"]'
        self.slides_container = '//*[@class= "slidesContainer"]'
        self.add_slide = '//*[@class= "add-slide-btn"]'
        self.up_arrow_button = '//*[@class= "fa fa-angle-up"]'
        self.global_controls = '//*[@class= "global-control-container"]'
        self.global_control_video_icon = "//img[contains(@src,'disable-audio.6a0b8e10.svg')]"
        self.global_control_audio_icon = "//img[contains(@src,'disable-video-copy.084b1401.svg')]"
        self.type_something_inputcard = '//input[@placeholder="Type something"]'
        self.tutor_controls_video_icon = "//img[contains(@src,'teacherVideo.34e0603d.svg')]"
        self.tutor_controls_audio_icon = "//img[contains(@src,'teacherMic.23f0c5c4.svg')]"
        self.selected_slide_on_whiteboard = "//div[@class='slide-preview-container']/div[@class='slide-view-container']/img"
        self.relaunch_error = "//*[contains(@class ,'Mui-error')]"
        self.chat_icon ="//img[@src='/static/media/chatPopup.3398527e.svg']"

    def is_white_board_present(self):
        self.wait_for_locator_webdriver(self.tutor_white_board)
        return self.chrome_driver.find_element_by_xpath(self.tutor_white_board).is_displayed()

    def is_highlighter_icon_present(self):
        self.wait_for_locator_webdriver(self.highlighter_icon)
        return self.chrome_driver.find_element_by_xpath(self.highlighter_icon).is_displayed()

    def is_pen_icon_present(self):
        self.wait_for_locator_webdriver(self.pen_icon)
        return self.chrome_driver.find_element_by_xpath(self.pen_icon).is_displayed()

    def is_eraser_icon_present(self):
        self.wait_for_locator_webdriver(self.eraser_icon)
        return self.chrome_driver.find_element_by_xpath(self.eraser_icon).is_displayed()

    def is_filler_icon_present(self):
        self.wait_for_locator_webdriver(self.filler_icon)
        return self.chrome_driver.find_element_by_xpath(self.filler_icon).is_displayed()

    def is_square_icon_present(self):
        self.wait_for_locator_webdriver(self.square_icon)
        return self.chrome_driver.find_element_by_xpath(self.square_icon).is_displayed()

    def is_triangle_icon_present(self):
        self.wait_for_locator_webdriver(self.triangle_icon)
        return self.chrome_driver.find_element_by_xpath(self.triangle_icon).is_displayed()

    def is_circle_icon_present(self):
        self.wait_for_locator_webdriver(self.circle_icon)
        return self.chrome_driver.find_element_by_xpath(self.circle_icon).is_displayed()

    def is_line_icon_present(self):
        self.wait_for_locator_webdriver(self.line_icon)
        return self.chrome_driver.find_element_by_xpath(self.line_icon).is_displayed()

    def verify_colors_palette(self):
        colors = self.chrome_driver.find_elements_by_css_selector('.colorBox')
        color_one = colors[0].value_of_css_property('background-color')
        color_two = colors[1].value_of_css_property('background-color')
        color_three = colors[2].value_of_css_property('background-color')
        color_four = colors[3].value_of_css_property('background-color')
        color_five = colors[4].value_of_css_property('background-color')
        color_six = colors[5].value_of_css_property('background-color')
        color_one_border = self.chrome_driver.find_elements_by_css_selector('.colorOuterBox')[0].value_of_css_property(
            'border')

        assert all([color_one == 'rgba(51, 51, 51, 1)', color_one_border == '1px solid rgb(51, 51, 51)',
                    color_two == 'rgba(51, 51, 51, 1)', color_three == 'rgba(41, 134, 255, 1)',
                    color_four == 'rgba(0, 200, 83, 1)', color_five == 'rgba(233, 29, 41, 1)',
                    color_six == 'rgba(234, 126, 0, 1)'])

    def verify_size_icons(self):
        eraser_size = self.chrome_driver.find_elements_by_css_selector('.eraserSizeBox')
        eraser_size_1 = eraser_size[0].size
        eraser_size_2 = eraser_size[1].size
        eraser_size_3 = eraser_size[2].size
        assert all([eraser_size_1 == {'height': 4, 'width': 4}, eraser_size_2 == {'height': 8, 'width': 8},
                    eraser_size_3 == {'height': 16, 'width': 16}])

    def is_byjus_icon_present(self):
        self.wait_for_locator_webdriver(self.byjus_icon)
        return self.chrome_driver.find_element_by_xpath(self.byjus_icon).is_displayed()

    def get_subject_name(self):
        self.wait_for_locator_webdriver(self.subject)
        return self.chrome_driver.find_element_by_xpath(self.subject).text

    def get_topic_name(self):
        self.wait_for_locator_webdriver(self.topic)
        return self.chrome_driver.find_element_by_xpath(self.topic).text

    def is_video_present(self):
        self.wait_for_locator_webdriver(self.video)
        return self.chrome_driver.find_element_by_xpath(self.video).is_displayed()

    def is_chat_box_present(self):
        self.wait_for_locator_webdriver(self.chat_container)
        return self.chrome_driver.find_element_by_xpath(self.chat_container).is_displayed()

    def is_toggle_present(self):
        self.wait_for_locator_webdriver(self.chat_toggle)
        return self.chrome_driver.find_element_by_xpath(self.chat_toggle).is_displayed()

    def is_end_button_present(self):
        self.wait_for_locator_webdriver(self.end_button)
        return self.chrome_driver.find_element_by_xpath(self.end_button).is_displayed()

    def tutor_end_session(self):
        self.wait_for_clickable_element_webdriver(self.end_button_timer)
        self.chrome_driver.find_element_by_xpath(self.end_button_timer).click()
        self.wait_for_clickable_element_webdriver(self.end_button)
        self.chrome_driver.find_element_by_xpath(self.end_button).click()
        self.wait_for_locator_webdriver("//button[@class = 'endBtn']")
        self.chrome_driver.find_element_by_xpath("//button[@class = 'endBtn']").click()

    def close_mentor_session_tab(self):
        self.chrome_driver.close()

    def is_slides_container_and_material_present(self):
        elements = self.chrome_driver.find_elements_by_css_selector('.slide-list-card')
        for i in elements:
            image = i.find_element_by_tag_name("img")
            img_src = image.get_attribute("src")
            print(img_src)
            assert img_src is not None, "Teaching material is not present"

        self.wait_for_locator_webdriver(self.slides_container)
        return self.chrome_driver.find_element_by_xpath(self.slides_container).is_displayed()

    def is_add_slide_present(self):
        self.wait_for_locator_webdriver(self.add_slide)
        return self.chrome_driver.find_element_by_xpath(self.add_slide).is_displayed()

    def click_global_controls_up_arrow_icon(self):
        self.wait_for_locator_webdriver(self.up_arrow_button)
        self.chrome_driver.find_element_by_xpath(self.up_arrow_button).click()

    def verify_global_controls_text(self):
        self.wait_for_locator_webdriver(self.global_controls)
        text = self.chrome_driver.find_element_by_xpath(self.global_controls).text
        assert text == 'Global Controls', "Global Controls text is not present"

    def is_global_control_video_icon_present(self):
        self.wait_for_locator_webdriver(self.global_control_video_icon)
        return self.chrome_driver.find_element_by_xpath(self.global_control_video_icon).is_displayed()

    def is_global_control_audio_icon_present(self):
        self.wait_for_locator_webdriver(self.global_control_audio_icon)
        return self.chrome_driver.find_element_by_xpath(self.global_control_audio_icon).is_displayed()

    def wait_for_locator_webdriver(self, locator_value):
        try:
            WebDriverWait(self.chrome_driver, 15).until(EC.presence_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_clickable_element_webdriver(self, locator_value):
        try:
            WebDriverWait(self.chrome_driver, 15).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def toggle_chat(self, text):
        self.wait_for_clickable_element_webdriver(self.chat_icon)
        self.chrome_driver.find_element_by_xpath(self.chat_icon).click()
        current_toggle_status = self.check_toggle_state()
        if text == "off" and current_toggle_status:
            self.wait_for_locator_webdriver(self.chat_toggle)
            self.chrome_driver.find_element_by_xpath(self.chat_toggle).click()
            self.wait_for_clickable_element_webdriver(self.live_chat_close)
            self.chrome_driver.find_element_by_xpath(self.live_chat_close).click()
        elif text == "on" and (not current_toggle_status):
            self.wait_for_locator_webdriver(self.chat_toggle)
            self.chrome_driver.find_element_by_xpath(self.chat_toggle).click()
            self.wait_for_clickable_element_webdriver(self.live_chat_close)
            self.chrome_driver.find_element_by_xpath(self.live_chat_close).click()
        else:
            pass

    def check_toggle_state(self):
        try:
            checked_flag = self.chrome_driver.find_element_by_xpath(
                "//*[contains(@class,'Mui-checked')]").is_displayed()
        except NoSuchElementException:
            checked_flag = False
        return checked_flag

    def click_on_add_slide(self):
        self.wait_for_clickable_element_webdriver(self.add_slide)
        self.chrome_driver.find_element_by_xpath(self.add_slide).click()

    def add_slide_and_verify(self, count):
        time.sleep(5)
        length_before_addslide = len(self.chrome_driver.find_elements_by_css_selector('div.slide-list-card'))
        for i in range(count):
            self.click_on_add_slide()
        time.sleep(5)
        length_after_addslide = len(self.chrome_driver.find_elements_by_css_selector('div.slide-list-card'))
        assert length_after_addslide == length_before_addslide + count, " new slide/slides not added"
        return length_after_addslide

    def page_refresh(self):
        self.chrome_driver.refresh()

    def is_new_slide_present_after_refresh(self, length_after_addslide):
        time.sleep(5)
        elements = self.chrome_driver.find_elements_by_xpath("//*[@class='slide-list-card']")
        print("length", len(elements))
        assert len(elements) == length_after_addslide, "Newly added slide is not present after refresh"

    def click_on_newly_added_slide(self):
        elements = self.chrome_driver.find_elements_by_css_selector('.slide-list-card')
        length = len(elements)
        self.scroll_from_top_to_bottom(length)
        elements[length - 1].click()
        time.sleep(5)

    def verify_type_something_text(self):
        self.wait_for_locator_webdriver(self.type_something_inputcard)
        assert self.chrome_driver.find_element_by_xpath(
            self.type_something_inputcard).is_displayed(), "Type something text is not present"

    def verify_zero_online_text(self):
        self.wait_for_locator_webdriver("//*[@class='online']")
        assert self.chrome_driver.find_element_by_xpath(
            "//*[@class='online']").text == 'Online', "Online text is not present"

    def scroll_from_top_to_bottom(self, length):
        self.chrome_driver.execute_script("arguments[0].scrollIntoView(true);",
                                          self.chrome_driver.find_elements_by_css_selector('.slide-list-card')[
                                              length - 1])

    def verify_user_scrolled_to_bottom(self, length):
        elements = self.chrome_driver.find_elements_by_css_selector('.slide-list-card')
        for i in range(length - 1, length - 6, -1):
            present = elements[i].is_displayed()
            assert present, "Bottom slides are not visible.User did not scroll to bottom"

    def click_on_highlighter_icon(self):
        self.wait_for_locator_webdriver(self.highlighter_icon)
        self.chrome_driver.find_element_by_xpath(self.highlighter_icon).click()

    def click_on_pen_icon(self):
        self.wait_for_locator_webdriver(self.pen_icon)
        self.chrome_driver.find_element_by_xpath(self.pen_icon).click()

    def click_on_eraser_icon(self):
        self.wait_for_locator_webdriver(self.eraser_icon)
        self.chrome_driver.find_element_by_xpath(self.eraser_icon).click()

    def click_on_text_icon(self):
        self.wait_for_locator_webdriver(self.text_icon)
        self.chrome_driver.find_element_by_xpath(self.text_icon).click()

    def click_on_square_icon(self):
        self.wait_for_locator_webdriver(self.square_icon)
        self.chrome_driver.find_element_by_xpath(self.square_icon).click()

    def click_on_triangle_icon(self):
        self.wait_for_locator_webdriver(self.triangle_icon)
        self.chrome_driver.find_element_by_xpath(self.triangle_icon).click()

    def click_on_circle_icon(self):
        self.wait_for_locator_webdriver(self.circle_icon)
        self.chrome_driver.find_element_by_xpath(self.circle_icon).click()

    def click_on_line_icon(self):
        self.wait_for_locator_webdriver(self.line_icon)
        self.chrome_driver.find_element_by_xpath(self.line_icon).click()

    def is_icon_selected(self, icon):
        xpath = getattr(self, "%s_icon" % icon, None)
        if xpath is None:
            raise
        self.wait_for_locator_webdriver(xpath)
        element = self.chrome_driver.find_element_by_xpath(xpath)
        parent_classname = self.chrome_driver.execute_script('return arguments[0].parentNode.className', element)
        assert 'toolActiveBtn' in parent_classname, "Icon is not selected"

    def enable_student_audio_and_video_by_global_controls(self):
        self.click_global_controls_up_arrow_icon()
        self.wait_for_locator_webdriver(self.global_control_video_icon)
        self.chrome_driver.find_element_by_xpath(self.global_control_video_icon).click()
        self.wait_for_locator_webdriver(self.global_control_audio_icon)
        self.chrome_driver.find_element_by_xpath(self.global_control_audio_icon).click()

    def disable_tutor_video(self):
        self.wait_for_clickable_element_webdriver(self.tutor_controls_video_icon)
        self.chrome_driver.find_element_by_xpath(self.tutor_controls_video_icon).click()

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

    def draw_shapes_on_mentor_whiteboard(self):
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver(self.tutor_white_board)
        self.add_slide_and_verify(1)
        self.click_on_newly_added_slide()
        canvas = self.chrome_driver.find_element_by_xpath(self.tutor_white_board)
        self.click_on_circle_icon()
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, 302, 304).perform()
        self.click_on_triangle_icon()
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, -160, -180).perform()
        self.click_on_square_icon()
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, 35, 35).perform()
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, -50, 70).perform()

    def perform_text_action_on_mentor_whiteboard(self, text):
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver(self.tutor_white_board)
        self.add_slide_and_verify(1)
        self.click_on_newly_added_slide()
        self.click_on_text_icon()
        actions = ActionChains(self.chrome_driver)
        canvas = self.chrome_driver.find_element_by_xpath(self.tutor_white_board)
        actions.move_to_element(canvas).click().send_keys(text).perform()

    def fill_colors_on_tutor_whiteboard(self):
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver(self.tutor_white_board)
        self.add_slide_and_verify(1)
        self.click_on_newly_added_slide()
        canvas = self.chrome_driver.find_element_by_xpath(self.tutor_white_board)
        colors = self.chrome_driver.find_elements_by_css_selector('.colorBox')
        self.click_on_circle_icon()
        colors[1].click()  # black color
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, 302, 320).perform()
        colors[2].click()  # blue color
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, 169, -200).perform()
        colors[3].click()  # green color
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, 50, 50).perform()
        colors[4].click()  # red color
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, -50, 70).perform()
        colors[5].click()  # orange color
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, -180, -250).perform()

    def verify_selected_slide_on_whiteboard(self):
        self.wait_for_locator_webdriver(self.selected_slide_on_whiteboard)
        image = self.chrome_driver.find_element_by_xpath(self.selected_slide_on_whiteboard)
        img_src = image.get_attribute("src")
        assert img_src is not None, "Teaching material slide is not present on whiteboard"

    def verify_whiteboard_dimension_ratio(self):
        canvas = self.chrome_driver.find_element_by_xpath(self.tutor_white_board)
        size = canvas.size
        canvas_width = int(size['width'])
        canvas_height = int(size['height'])
        ratio = canvas_width / canvas_height
        print(ratio)
        assert any([ratio == 4 / 3, ratio == 16 / 9]), "slide displayed on the whiteboard is not of size 4:3 or 16:9"

    def is_vertical_scrollbar_present(self):
        self.wait_for_locator_webdriver(self.tutor_white_board)
        scroll_height = self.chrome_driver.execute_script(
            'document.getElementsByClassName("whiteboardCanvas")[0].scrollHeight')
        client_height = self.chrome_driver.execute_script(
            'document.getElementsByClassName("whiteboardCanvas")[0].clientHeight')
        if scroll_height > client_height:
            print("Vertical Scrollbar is present")
            return True
        else:
            return False

    def login_as_tutor(self):
        path = '../../config/config.json'
        email = str(getdata(path, 'staging_access', 'email'))
        password = str(getdata(path, 'staging_access', 'password'))
        self.chrome_driver.get('https://staging.tllms.com/admin')
        self.chrome_driver.maximize_window()
        self.wait_for_locator_webdriver("//input[@id='email']")
        self.chrome_driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        self.wait_for_locator_webdriver("//button[@type='submit']")
        self.chrome_driver.find_element_by_xpath("//button[@type='submit']").click()
        self.wait_for_locator_webdriver("//input[@type='email']")
        self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
        self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(Keys.ENTER)
        # self.wait_for_clickable_element_webdriver("//*[contains(text(),'Next')]")
        # self.chrome_driver.execute_script("arguments[0].click();",self.chrome_driver.find_element_by_xpath("//*[contains(text(),'Next')]"))
        self.wait_for_clickable_element_webdriver("//input[@type='password']")
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(Keys.ENTER)
        # self.wait_for_locator_webdriver("//*[contains(text(),'Next')]")
        # self.chrome_driver.execute_script("arguments[0].click();",
        #                                   self.chrome_driver.find_element_by_xpath("//*[contains(text(),'Next')]"))

    def start_tutor_session(self):
        url = self.tlms.get_tutor_url()
        self.login_as_tutor()
        self.wait_for_locator_webdriver("//li[@id='mentoring']")
        self.chrome_driver.get(url)
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
        return url

    def verify_tutor_unable_to_join_session_again(self):
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
        self.wait_for_locator_webdriver(self.relaunch_error)
        error_message = self.chrome_driver.find_element_by_xpath(self.relaunch_error).text
        assert (
                    'Your session is ended' in error_message), "Tutor is able to join session again even after ending session"
        self.chrome_driver.close()

    def reopen_chrome_browser(self, tutor_url):
        self.chrome_driver = webdriver.Chrome()
        self.login_as_tutor()
        self.wait_for_locator_webdriver("//li[@id='mentoring']")
        self.chrome_driver.get(tutor_url)
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
