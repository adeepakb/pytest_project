from pom_pages.base_pages.ps_home_screen_base import PSHomeScreenBase


class PSHomescreenWeb(PSHomeScreenBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
