from pages.android.ps_3plus1_screen_android import  PS_3Plus1ScreenAndroid
from pages.web.ps_3plus1screen_web import PS_3Plus1ScreenWeb
from pages.web.instruction_dialog_web import InstrcutionDialogWeb
from pages.android.instruction_dialog_android import InstructionDialogAndroid
from constants.platform import Platform


class InstructionDialog():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            instruction_dialog = InstrcutionDialogWeb(driver)
        elif platform == Platform.ANDROID.value:
            instruction_dialog = InstructionDialogAndroid(driver)
        return instruction_dialog
