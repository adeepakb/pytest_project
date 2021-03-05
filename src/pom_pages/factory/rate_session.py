from constants.platform import Platform
from pom_pages.android_pages.rate_session_android import  Dashboard
from pom_pages.web_pages.rate_session_web import RateSessionWeb


class RateSession():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            dashboard = RateSessionWeb(driver)
        elif platform == Platform.ANDROID.value:
            dashboard = Dashboard(driver)
        return dashboard
