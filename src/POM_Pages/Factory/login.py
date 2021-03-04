from POM_Pages.Android_pages.login_android import LoginAndroid
from POM_Pages.Web_pages.login_web import LoginWeb
from Constants.platform import Platform


class LoginFactory():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            login = LoginWeb(driver)
        elif platform == Platform.ANDROID.value:
            login = LoginAndroid(driver)
        return login
