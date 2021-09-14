from constants.platform import Platform
from pages.web.neo_in_class_web import NeoInClass


class NeoInClassFactory:
    @staticmethod
    def get_page(driver, platform):
        if platform == Platform.WEB.value:
            neo_in_class = NeoInClass(driver)
        elif platform == Platform.ANDROID.value:
            raise NotImplementedError(f"application login page for '{platform.WEB.name}' is not yet implemented.")
        elif platform == Platform.API.value:
            raise NotImplementedError(f"application login page for '{platform.API.name}' is not yet implemented.")
        elif platform == Platform.IOS.value:
            raise NotImplementedError(f"application login page for '{platform.IOS.name}' is not yet implemented.")
        elif platform == Platform.MWEB.value:
            raise NotImplementedError(f"application login page for '{platform.MWEB.name}' is not yet implemented.")
        else:
            raise KeyError(f"'{platform}' dose not map to any key.")
        return neo_in_class
