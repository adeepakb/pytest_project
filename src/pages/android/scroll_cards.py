from appium.webdriver.common.touch_action import TouchAction


class ScrollCards:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def element_location_and_size(element, dimension=None, co_ordinates=None):
        if co_ordinates is None:
            if "height" == dimension:
                return element.size['height']
            elif "width" == dimension:
                return element.size['width']
        elif dimension is None:
            if "x" == co_ordinates:
                return element.location['x']
            elif "y" == co_ordinates:
                return element.location['y']
        return None

    def scroll_by_card(self, start_element, end_element, coincide='bottom', buffer=2):
        action = TouchAction(self.driver)
        start_element_width = self.element_location_and_size(start_element, dimension='width') // 2
        start_x = self.element_location_and_size(start_element, co_ordinates='x') + start_element_width
        start_element_height = self.element_location_and_size(start_element, dimension='height')
        start_y = self.element_location_and_size(start_element, co_ordinates='y') + start_element_height - buffer
        end_y = self.element_location_and_size(end_element, co_ordinates='y') + buffer
        action.press(x=start_x, y=start_y).wait(5000).move_to(x=start_x, y=end_y).release().perform()

    def scroll_by_element(self, start_element, end_element, direction='up', coincide='top'):
        action = TouchAction(self.driver)
        start_x = self.element_location_and_size(start_element, co_ordinates='x')
        if coincide == 'top':
            start_y = self.element_location_and_size(start_element, co_ordinates='y')
        elif coincide == 'bottom':
            start_y = self.element_location_and_size(start_element, co_ordinates='y') +\
                    self.element_location_and_size(start_element, dimension='height') - 10
        else:
            raise TypeError(f"can only coincide 'top' or 'bottom' not '{coincide}'.") from None
        end_x = self.element_location_and_size(start_element, co_ordinates='x')
        if direction == 'down':
            end_y = self.element_location_and_size(end_element, co_ordinates='y') +\
                    self.element_location_and_size(end_element, dimension='height') - 10
        else:
            end_y = self.element_location_and_size(end_element, co_ordinates='y')
        action.press(x=start_x, y=start_y).wait(5000).move_to(x=end_x, y=end_y).release().perform()
