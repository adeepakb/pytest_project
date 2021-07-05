"""It contains all common elements and functionalities available to all pages."""

from typing import Any, Text, List, Union, TypeVar, Optional, Tuple
from appium.webdriver.webelement import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait as WaitClass
from selenium.webdriver.common import alert

WaitInstance = TypeVar('WaitInstance', bound=WaitClass)
AlertInstance = TypeVar('AlertInstance', bound=alert)

class TutorCommonMethods:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = None
        ...

    @staticmethod
    def _by(__o: Text) -> Any: ...

    def webdriver_wait(self, timeout: Union[int, float]) -> WaitInstance: ...

    def wait_for_locator(self, l_type: Text, l_value: Text, timeout: Union[int, float]) -> None : ...

    def wait_for_invisibility_of_element(self, l_type: Text, l_value: Text, timeout: int) -> None : ...

    @staticmethod
    def wait_for_alert(driver: WebDriver, timeout: Union[int, float]) -> AlertInstance: ...

    def wait_for_clickable(self, driver: WebDriver, l_type: Text, l_value: Text, timeout: Union[int, float]) -> None: ...

    def fluent_wait(self,l_type: Text, l_value: Text) -> None: ...

    @staticmethod
    def execute_command(command_exe: Text) -> object: ...

    def take_screen_shot(self, filename: Text) -> None: ...

    def get_element(self, l_type: Text, l_value: Text) -> WebElement: ...

    def get_elements(self, l_type: Text, l_value: Text) -> List[WebElement]: ...

    def element_click(self, l_type: Optional[Text] = None, l_value: Optional[Text] = None, element:Optional[WebElement] = None) -> None: ...

    def child_element_by_id(self, element: WebElement,id_locator_value: Text) -> Any: ...

    def child_element_click_by_id(self, element: WebElement, id_locator_value: Text) -> None: ...

    def child_element_text(self, element: WebElement, id_locator_value: Text) -> Any: ...

    def child_element_displayed(self, element: WebElement, id_locator_value: Text) -> Any: ...

    def enter_text(self, text: Text, l_type: Text, l_value: Text) -> None: ...

    def clear_data(self, l_type: Text, l_value: Text) -> None: ...

    def is_text_match(self, text: Text) -> bool: ...

    def is_button_displayed(self, text: Text) -> bool: ...

    def button_click(self, text: Text) -> None: ...

    def is_button_enabled(self, text: Text ) -> bool: ...

    def verify_element_color(
            self, l_type: Optional[Text], l_value: Optional[Text],
            rgb_color_code: Union[Text, Tuple, List],index: int, element: Optional[WebElement]) -> Text: ...

    def root_mean_square_error(self, foreground_color, target_color) ->  float: ...

    def is_link_displayed(self, text: Text) -> bool: ...

    def click_link(self, text: Text) -> None: ...

    def scroll_to_element(self, text: Text) -> Union[WebElement, bool]: ...

    def is_scrolled_and_element_clicked(self, text: Text) -> bool: ...

    def is_element_present(self, l_type: Text, l_value: Text) -> bool: ...

    def hide_keyboard(self) -> bool: ...

    def get_element_text(self, l_type: Text, l_value: Text) -> Text: ...

    def get_element_attr(self, text: Text, l_type: Text, l_value: Text) -> Text: ...

    def is_text_displayed(self, l_type: Text, l_value: Text) -> bool: ...

    def is_keyboard_shown(self) -> bool: ...

    def click_back(self) -> None: ...

    def get_current_package(self) -> Any: ...

    def click_on_device_btn(self, text: Text) -> bool: ...

    def take_app_foreground(self, app_package: Text) -> bool: ...

    def query_app_state(self, text:Text) -> Any: ...

    def toggle_wifi_connection(self, text) -> None: ...

    def capture_screenshot(self,element,filename)-> None: ...

    def detect_shapes(self,element) -> List: ...

    def get_text_from_image(self,filename)  -> Text: ...

    def get_all_colors_present(
            self, l_type: Optional[Text], l_value: Optional[Text],
            element: Optional[WebElement]) -> Optional[List[Tuple[int, Any]]]: ...

    def clear_app_from_recents(self) -> None: ...

    @staticmethod
    def compare_images(image1:Text, image2:Text) -> Any: ...

    def takeScreenShot(self, featureFileName)  -> Any: ...

    def noSuchEleExcept(self, featureFileName, methodName) -> Any: ...

    def exception(self, featureFileName, methodName) -> Any: ...

    def get_device_type(self) -> Text: ...

    def wait_activity(self, activity_name: str, timeout=int) -> bool: ...

    def is_android_notification_present(self, expected_notification:Text)-> bool: ...

    def is_child_element_present(self, parent_element, locator_type, locator_value)-> bool: ...
