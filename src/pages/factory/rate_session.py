from constants.platform import Platform
from pages.android.rate_session_android import  Dashboard
from pages.web.rate_session_web import RateSessionWeb


class RateSession():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            dashboard = RateSessionWeb(driver)
        elif platform == Platform.ANDROID.value:
            dashboard = Dashboard(driver)
        return dashboard
