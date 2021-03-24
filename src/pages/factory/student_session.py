from pages.android.ps_home_screen_android import PS_Homescreen_Android
from pages.web_pages.ps_home_screen_web import PSHomescreenWeb
from constants.platform import Platform
from pages.web_pages.student_session_web import StudentSessionWeb
from pages.android.student_session import StudentSessionAndroid


class StudentSessionFactory():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            student_session = StudentSessionWeb(driver)
        elif platform == Platform.ANDROID.value:
            student_session = StudentSessionAndroid(driver)
        return student_session
