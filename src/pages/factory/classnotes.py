from pages.android.classnotes_android import ClassNotesAndroid
from pages.web_pages.classnotes_web import ClassNotesWeb
from constants.platform import Platform


class ClassNotesFactory():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            classnotes = ClassNotesWeb(driver)
        elif platform == Platform.ANDROID.value:
            classnotes = ClassNotesAndroid(driver)
        return classnotes
