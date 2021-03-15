from pages.base.ps_home_screen_base import PSHomeScreenBase


class PSHomescreenWeb(PSHomeScreenBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
