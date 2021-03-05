from pom_pages.base_pages.ps3_plus1_screen_base import PS_3Plus1ScreenBase


class PS_3Plus1ScreenWeb(PS_3Plus1ScreenBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
