from pages.web_pages.trialclass_web import TrialClassWeb
from pages.android.trialclass_android import TrailClassAndroid
from constants.platform import Platform


class TrialClassFactory():

    def get_page(self, driver, platform):
        if platform == Platform.ANDROID.value:
            trial_class = TrailClassAndroid(driver)
        elif platform == Platform.WEB.value:
            trial_class = TrialClassWeb(driver)
        return trial_class
