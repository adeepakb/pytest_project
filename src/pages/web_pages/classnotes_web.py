from pages.base.classnotes_base import ClassNotesBase


class ClassNotesWeb(ClassNotesBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
