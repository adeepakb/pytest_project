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
from utilities.common_methods_web import CommonMethodsWeb


class NeoTute:
    def __init__(self, driver):
        self.driver = driver
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
        self.tlms = Stagingtlms(driver)

        self.add_slide = "//span[text()='Add New Slide']"
        self.whiteboard = "//div[@class='whiteboardView']"
        self.slides_container = '//div[@class= "neo_cl_SlideList"]'
        self.selected_slide_on_whiteboard = "//img[@alt='imageSlide']"

        self.presentation = '//*[@class = "presentationContainer"]'
        self.toggle_draw = '//input[@name= "toggle-toolbox"]'
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

        self.video = '//div[@class = "videoPresentation false"]'

        self.global_control_video_icon = '//div[@class="topContainer--action_icon red-bg"]/img[@alt="cam"]'
        self.global_control_audio_icon = '//div[@class="topContainer--action_icon red-bg"]/img[@alt="mic"]'
        self.focus_mode = "//img[@alt='chat']"
        self.tutor_controls_video_icon = '//div[contains(@class,"tutorCard--red_icon")]/img[@alt="cam"]'
        self.tutor_controls_audio_icon = '//div[contains(@class,"tutorCard--red_icon")]/img[@alt="mic"]'

        self.chat_container = '//div[@class= "chatWidgetContainer"]'
        self.type_something_inputcard = '//input[@placeholder="Type something"]'
        self.chat_toggle = '//span[@class= "MuiSwitch-root"]'

        self.relaunch_error = "//*[contains(@class ,'Mui-error')]"
        self.end_button = '//span[text()= "End Class"]'

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

    def start_tutor_session(self):
        url = self.tlms.get_tutor_url()
        self.login_as_tutor()
        self.wait_for_locator_webdriver("//li[@id='mentoring']")
        self.chrome_driver.get(url)
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
        return url

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

    # session slides
    def is_slides_container_and_material_present(self):
        elements = self.chrome_driver.find_elements_by_css_selector('div.slide__img')
        for i in elements:
            image = i.find_element_by_tag_name("img")
            img_src = image.get_attribute("src")
            print(img_src)
            assert img_src is not None, "Teaching material is not present"
        self.wait_for_locator_webdriver(self.slides_container)
        return self.chrome_driver.find_element_by_xpath(self.slides_container).is_displayed()

    # session slides -> add slide
    def is_add_slide_present(self):
        self.wait_for_locator_webdriver(self.add_slide)
        return self.chrome_driver.find_element_by_xpath(self.add_slide).is_displayed()

    def click_on_add_slide(self):
        self.wait_for_clickable_element_webdriver(self.add_slide)
        self.chrome_driver.find_element_by_xpath(self.add_slide).click()

    def add_slide_and_verify(self, count):
        length_before_addslide = len(self.chrome_driver.find_elements_by_css_selector('div.neo_cl_slide'))
        for i in range(count):
            self.click_on_add_slide()
        time.sleep(5)
        length_after_addslide = len(self.chrome_driver.find_elements_by_css_selector('div.neo_cl_slide'))
        assert length_after_addslide == length_before_addslide + count, " new slide/slides not added"
        return length_after_addslide

    def page_refresh(self):
        self.chrome_driver.refresh()

    def is_new_slide_present_after_refresh(self, length_after_addslide):
        # time.sleep(5)
        elements = self.chrome_driver.find_elements_by_css_selector('div.neo_cl_slide')
        print("length", len(elements))
        assert len(elements) == length_after_addslide, "Newly added slide is not present after refresh"

    def click_on_newly_added_slide(self):
        elements = self.chrome_driver.find_elements_by_css_selector('div.neo_cl_slide')
        length = len(elements)
        self.scroll_from_top_to_bottom(length)
        elements[length - 1].click()
        # time.sleep(5)

    def scroll_from_top_to_bottom(self, length):
        self.chrome_driver.execute_script("arguments[0].scrollIntoView(true);",
                                          self.chrome_driver.find_elements_by_css_selector('.neo_cl_slide')[length - 1])

    def verify_user_scrolled_to_bottom(self, length):
        elements = self.chrome_driver.find_elements_by_css_selector('.neo_cl_slide')
        for i in range(length - 1, length - 6, -1):
            present = elements[i].is_displayed()
            assert present, "Bottom slides are not visible.User did not scroll to bottom"

    def verify_selected_slide_on_whiteboard(self):
        self.wait_for_locator_webdriver(self.selected_slide_on_whiteboard)
        image = self.chrome_driver.find_element_by_xpath(self.selected_slide_on_whiteboard)
        img_src = image.get_attribute("src")
        assert img_src is not None, "Teaching material slide is not present on whiteboard"

    # Session slides -> whiteboard
    def is_white_board_present(self):
        self.wait_for_locator_webdriver(self.whiteboard)
        return self.chrome_driver.find_element_by_xpath(self.whiteboard).is_displayed()

    def toggle_draw(self, text):
        current_toggle_status = self.check_toggle_state()
        if text == "off" and current_toggle_status:
            self.wait_for_locator_webdriver(self.toggle_draw)
            self.chrome_driver.find_element_by_xpath(self.toggle_draw).click()
        elif text == "on" and (not current_toggle_status):
            self.wait_for_locator_webdriver(self.toggle_draw)
            self.chrome_driver.find_element_by_xpath(self.toggle_draw).click()

    def is_selector_icon_present(self):
        self.wait_for_locator_webdriver(self.selector_icon)
        return self.chrome_driver.find_element_by_xpath(self.selector_icon).is_displayed()

    def is_pen_icon_present(self):
        self.wait_for_locator_webdriver(self.pen_icon)
        return self.chrome_driver.find_element_by_xpath(self.pen_icon).is_displayed()

    def is_eraser_icon_present(self):
        self.wait_for_locator_webdriver(self.eraser_icon)
        return self.chrome_driver.find_element_by_xpath(self.eraser_icon).is_displayed()

    def is_rectangle_icon_present(self):
        self.wait_for_locator_webdriver(self.rectangle_icon)
        return self.chrome_driver.find_element_by_xpath(self.rectangle_icon).is_displayed()

    def is_polygon_icon_present(self):
        self.wait_for_locator_webdriver(self.polygon_icon)
        return self.chrome_driver.find_element_by_xpath(self.polygon_icon).is_displayed()

    def is_ellipse_icon_present(self):
        self.wait_for_locator_webdriver(self.ellipse_icon)
        return self.chrome_driver.find_element_by_xpath(self.ellipse_icon).is_displayed()

    def is_line_icon_present(self):
        self.wait_for_locator_webdriver(self.line_icon)
        return self.chrome_driver.find_element_by_xpath(self.line_icon).is_displayed()

    def verify_colors_palette(self):
        self.chrome_driver.find_elements_by_xpath("//div[@class='tool-box-cell']")[0].click()
        colors_elts = self.chrome_driver.find_elements_by_css_selector('div.cell-mid-color')
        colors_list = []
        # red,orange, violet,blue,yellow,green,black,grey,white
        for i in range(0, 9):
            color = colors_elts[i].value_of_css_property('background-color')
            colors_list.append(color)
        assert colors_list == ['rgb(255, 37, 37)', 'rgb(255, 152, 93)', 'rgb(180, 45, 191)', 'rgb(19, 105, 233)',
                               'rgb(255, 199, 0)','rgb(81, 222, 31)', 'rgb(48, 52, 58)', 'rgb(183, 183, 183)', 'rgb(255, 255, 255)']

    # tool box size method to be implemented

    def click_on_selector_icon(self):
        self.wait_for_locator_webdriver(self.selector_icon)
        self.chrome_driver.find_element_by_xpath(self.selector_icon).click()

    def click_on_pen_icon(self):
        self.wait_for_locator_webdriver(self.pen_icon)
        self.chrome_driver.find_element_by_xpath(self.pen_icon).click()

    def click_on_eraser_icon(self):
        self.wait_for_locator_webdriver(self.eraser_icon)
        self.chrome_driver.find_element_by_xpath(self.eraser_icon).click()

    def click_on_text_icon(self):
        self.wait_for_locator_webdriver(self.text_icon)
        self.chrome_driver.find_element_by_xpath(self.text_icon).click()

    def click_on_rectangle_icon(self):
        self.wait_for_locator_webdriver(self.rectangle_icon)
        self.chrome_driver.find_element_by_xpath(self.rectangle_icon).click()

    def click_on_polygon_icon(self):
        self.wait_for_locator_webdriver(self.polygon_icon)
        self.chrome_driver.find_element_by_xpath(self.polygon_icon).click()

    def click_on_ellipse_icon(self):
        self.wait_for_locator_webdriver(self.ellipse_icon)
        self.chrome_driver.find_element_by_xpath(self.ellipse_icon).click()

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
        assert 'tool-box-cell-selected' in parent_classname, "Icon is not selected"

    def draw_shapes_on_neo_tutor_whiteboard(self):
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver(self.presentation)
        self.add_slide_and_verify(1)
        self.click_on_newly_added_slide()
        canvas = self.chrome_driver.find_element_by_xpath(self.presentation)
        self.click_on_ellipse_icon()
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, 302, 304).perform()
        self.click_on_polygon_icon()
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, -160, -180).perform()
        self.click_on_rectangle_icon()
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, 35, 35).perform()
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, -50, 70).perform()

    def perform_text_action_on_neo_tutor_whiteboard(self, text):
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver(self.presentation)
        self.add_slide_and_verify(1)
        self.click_on_newly_added_slide()
        self.click_on_text_icon()
        actions = ActionChains(self.chrome_driver)
        canvas = self.chrome_driver.find_element_by_xpath(self.presentation)
        actions.move_to_element(canvas).click().send_keys(text).perform()

    def fill_colors_on_tutor_whiteboard(self):
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver(self.presentation)
        self.add_slide_and_verify(1)
        self.click_on_newly_added_slide()
        canvas = self.chrome_driver.find_element_by_xpath(self.presentation)
        self.chrome_driver.find_elements_by_xpath("//div[@class='tool-box-cell']")[0].click()
        colors_elts = self.chrome_driver.find_elements_by_css_selector('div.cell-mid-color')
        self.click_on_ellipse_icon()
        colors_elts[1].click()  # red color
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, 302, 320).perform()
        colors_elts[2].click()  # orange color
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, 169, -200).perform()
        colors_elts[3].click()  # violet color
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, 50, 50).perform()
        colors_elts[4].click()  # blue color
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, -50, 70).perform()
        colors_elts[5].click()  # yellow  color
        ActionChains(self.chrome_driver).drag_and_drop_by_offset(canvas, -180, -250).perform()

    # Class forum
    def verify_type_something_text(self):
        self.wait_for_locator_webdriver(self.type_something_inputcard)
        assert self.chrome_driver.find_element_by_xpath(
            self.type_something_inputcard).is_displayed(), "Type something text is not present"

    def verify_zero_online_text(self):
        self.wait_for_locator_webdriver("//*[@class='online']")
        assert self.chrome_driver.find_element_by_xpath(
            "//*[@class='online']").text == 'Online', "Online text is not present"

    def check_toggle_state(self):
        try:
            checked_flag = self.chrome_driver.find_element_by_xpath( "//*[contains(@class,'Mui-checked')]").is_displayed()
        except NoSuchElementException:
            checked_flag = False
        return checked_flag

    def toggle_chat(self, text):
        current_toggle_status = self.check_toggle_state()
        if text == "off" and current_toggle_status:
            self.wait_for_locator_webdriver(self.chat_toggle)
            self.chrome_driver.find_element_by_xpath(self.chat_toggle).click()
        elif text == "on" and (not current_toggle_status):
            self.wait_for_locator_webdriver(self.chat_toggle)
            self.chrome_driver.find_element_by_xpath(self.chat_toggle).click()
        else:
            pass

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

    def is_toggle_present(self):
        self.wait_for_locator_webdriver(self.chat_toggle)
        return self.chrome_driver.find_element_by_xpath(self.chat_toggle).is_displayed()

    # Video
    def is_video_present(self):
        self.wait_for_locator_webdriver(self.video)
        return self.chrome_driver.find_element_by_xpath(self.video).is_displayed()

    def get_video_src_from_neo_tute(self):
        video_url = self.chrome_driver.find_element_by_xpath(
            "//div[@class='shaka-video-container']/video").is_displayed()
        video_src = video_url.get_attribute("src")
        print(video_src)
        return video_src

    # End session
    def is_end_button_present(self):
        self.wait_for_locator_webdriver(self.end_button)
        return self.chrome_driver.find_element_by_xpath(self.end_button).is_displayed()

    def tutor_end_session(self):
        self.wait_for_clickable_element_webdriver(self.end_button)
        self.chrome_driver.find_element_by_xpath(self.end_button).click()
        self.wait_for_locator_webdriver("//button[@class = 'endBtn']")
        self.chrome_driver.find_element_by_xpath("//button[@class = 'endBtn']").click()

    def verify_tutor_unable_to_join_session_after_session_ended(self):
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
        self.wait_for_locator_webdriver(self.relaunch_error)
        error_message = self.chrome_driver.find_element_by_xpath(self.relaunch_error).text
        assert ('Your session is ended' in error_message), "Tutor is able to join session again even after ending session"
        self.chrome_driver.close()

    def reopen_chrome_browser(self, tutor_url):
        self.chrome_driver = webdriver.Chrome()
        self.login_as_tutor()
        self.wait_for_locator_webdriver("//li[@id='mentoring']")
        self.chrome_driver.get(tutor_url)
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()

    def close_mentor_session_tab(self):
        self.chrome_driver.close()

    # Student details
    def verify_student_details(self):
        student_details_container = self.chrome_driver.find_element_by_xpath(
            '//div[@class="studentsDetails__container"]')
        assert len(student_details_container) is 25, "Capacity of neo class 25 as expected"

    def verify_student_name(self):
        student_name_elts = self.chrome_driver.find_elements_by_xpath('//div[@class="student-name"]')
        for elt in student_name_elts:
            student_name = elt.text
            if student_name is not None:
                return False
        return True

    def verify_student_profile(self):
        count = 0
        try:
            student_profile_elts = self.chrome_driver.find_elements_by_xpath("//img[@alt='profile']")
            for elt in student_profile_elts:
                count = count + 1
            if count is 25:
                return True
            else:
                return False
        except NoSuchElementException:
            return False
