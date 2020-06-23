from appium.webdriver.common.touch_action import TouchAction


class ScrollCards:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def element_location_and_size(element, dimension=None, ordinates=None):
        if ordinates is None:
            if "height" == dimension:
                return element.size['height']
            elif "width" == dimension:
                return element.size['width']
        elif dimension is None:
            if "x" == ordinates:
                return element.location['x']
            elif "y" == ordinates:
                return element.location['y']
        return None

    def scroll_by_card(self, start_element, end_element):
        action = TouchAction(self.driver)
        start_x = self.element_location_and_size(start_element, dimension='width') // 2
        start_y = self.element_location_and_size(start_element, ordinates='y')
        end_x = self.element_location_and_size(start_element, dimension='width') // 2
        end_y = self.element_location_and_size(end_element, ordinates='y')
        action.press(x=start_x, y=start_y).wait(5000).move_to(x=end_x, y=end_y).release().perform()

    def scroll_by_element(self, start_element, end_element, direction='up'):
        action = TouchAction(self.driver)
        start_x = self.element_location_and_size(start_element, ordinates='x')
        start_y = self.element_location_and_size(start_element, ordinates='y')
        end_x = self.element_location_and_size(start_element, ordinates='x')
        if direction == 'down':
            end_y = self.element_location_and_size(end_element, ordinates='y') +\
                    self.element_location_and_size(end_element, dimension='height')
        else:
            end_y = self.element_location_and_size(end_element, ordinates='y')
        action.press(x=start_x, y=start_y).wait(5000).move_to(x=end_x, y=end_y).release().perform()
