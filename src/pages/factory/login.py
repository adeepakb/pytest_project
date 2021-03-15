from pages.android.login_android import LoginAndroid
from pages.web.login_web import LoginWeb
from constants.platform import Platform


class LoginFactory():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            login = LoginWeb(driver)
        elif platform == Platform.ANDROID.value:
            login = LoginAndroid(driver)
        return login
