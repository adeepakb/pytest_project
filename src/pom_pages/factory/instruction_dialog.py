from pom_pages.android_pages.ps_3plus1_screen_android import  PS_3Plus1ScreenAndroid
from pom_pages.web_pages.ps_3plus1screen_web import PS_3Plus1ScreenWeb
from pom_pages.web_pages.instruction_dialog_web import InstrcutionDialogWeb
from pom_pages.android_pages.instruction_dialog_android import InstructionDialogAndroid
from constants.platform import Platform


class InstructionDialog():

    def get_page(self, driver, platform):
        if platform == Platform.WEB.value:
            instruction_dialog = InstrcutionDialogWeb(driver)
        elif platform == Platform.ANDROID.value:
            instruction_dialog = InstructionDialogAndroid(driver)
        return instruction_dialog
