import logging
import time
from selenium.common.exceptions import NoSuchElementException
from constants.load_json import getdata
from pom_pages.base_pages.instruction_dialog_base import InstructionDialogBase
from constants.constants import Login_Credentials


class InstrcutionDialogWeb(InstructionDialogBase):
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
