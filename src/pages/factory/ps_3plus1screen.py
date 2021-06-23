from pages.android.ps_3plus1_screen_android import  PS_3Plus1ScreenAndroid
from pages.web_pages.ps_3plus1screen_web import PS_3Plus1ScreenWeb
from pages.web_pages.ps_home_screen_web import PSHomescreenWeb
from constants.platform import Platform


class PS_3Plus1Screen():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            home_screen = PS_3Plus1ScreenWeb(driver)
        elif platform == Platform.ANDROID.value:
            home_screen = PS_3Plus1ScreenAndroid(driver)
        return home_screen
