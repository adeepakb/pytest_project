from POM_Pages.Android_pages.ps_home_screen_android import PS_Homescreen_Android
from POM_Pages.Web_pages.ps_home_screen_web import PSHomescreenWeb
from Constants.platform import Platform
from POM_Pages.Web_pages.student_session_web import StudentSessionWeb
from POM_Pages.Android_pages.student_session import StudentSession


class StudentSessionFactory():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            student_session = StudentSessionWeb(driver)
        elif platform == Platform.ANDROID.value:
            student_session = StudentSession(driver)
        return student_session
