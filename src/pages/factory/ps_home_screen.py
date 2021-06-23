from pages.android.ps_home_screen_android import PS_Homescreen_Android
from pages.web_pages.ps_home_screen_web import PSHomescreenWeb
from constants.platform import Platform


class PSHomescreenFactory():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            home_screen = PSHomescreenWeb(driver)
        elif platform == Platform.ANDROID.value:
            home_screen = PS_Homescreen_Android(driver)
        return home_screen
