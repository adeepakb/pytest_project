from constants.platform import *


class Login:
    @staticmethod
    def get_page(driver, platform):
        if platform == Platform.ANDROID.value:
            from pages.android.application_login import Login
            login = Login(driver)
        elif platform == Platform.WEB.value:
            raise NotImplementedError(f"application login page for '{platform.WEB.name}' is not yet implemented.")
        elif platform == Platform.API.value:
            raise NotImplementedError(f"application login page for '{platform.API.name}' is not yet implemented.")
        elif platform == Platform.IOS.value:
            raise NotImplementedError(f"application login page for '{platform.IOS.name}' is not yet implemented.")
        elif platform == Platform.MWEB.value:
            raise NotImplementedError(f"application login page for '{platform.MWEB.name}' is not yet implemented.")
        else:
            raise KeyError(f"'{platform}' dose not map to any key.")
        return login
