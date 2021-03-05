from pom_pages.android_pages.ps_home_screen_android import PS_Homescreen_Android
from pom_pages.web_pages.ps_home_screen_web import PSHomescreenWeb
from constants.platform import Platform
from pom_pages.web_pages.student_session_web import StudentSessionWeb
from pom_pages.android_pages.student_session import StudentSessionAndroid


class StudentSessionFactory():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            student_session = StudentSessionWeb(driver)
        elif platform == Platform.ANDROID.value:
            student_session = StudentSessionAndroid(driver)
        return student_session
