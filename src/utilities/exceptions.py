"""
Base exception module
"""


class AppBaseException(Exception):
    pass


class TimeOutError(AppBaseException):

    def __init__(self, timeout):
        """
        :type timeout: int
        """
        self.timeout = timeout

    def __str__(self):
        return f"unable to start/complete the action waited upto {self.timeout}sec, try to increase the timeout."


class ElementNotFoundError(AppBaseException):

    def __init__(self, element_name: str, screen_name: str):
        self.element = element_name
        self.screen = screen_name

    def __str__(self):
        return f"element '{self.element}' could not be located in '{self.screen}' screen."


class DeviceUnavailableException(AppBaseException):
    def __init__(self, message):
        self.adb_error = message

    def __str__(self):
        return f"No device(s) connected, make sure device(s) are available and connected to the port." \
               f"\nOriginal Error: '{self.adb_error}'."


class ConnectionStateError(AppBaseException):
    def __str__(self):
        return "Unable to set/modify connection status.\nPossible Cause: Airplane mode is enabled."


class ConnectionTimeoutError(TimeOutError):

    def __str__(self):
        return f"max retries exceed, no known network(s) available."


class ElementNotFoundWarning(Warning):
    pass


class ActivityNotFoundException(AppBaseException):
    pass


class UnknownUserProfile(AppBaseException):
    pass


class DateError(AppBaseException):
    pass


class RequisiteException(AppBaseException):
    def __init__(self, *msg):
        self.msg = msg

    def __str__(self):
        return ("%s requisite group has no %s" % self.msg).lstrip(' ')


class AssetTypeError(RequisiteException):
    def __init__(self, group, asset):
        super().__init__(group.title(), "asset of type '%s'" % asset)

    def __str__(self):
        return super().__str__()


class RequisiteTypeError(RequisiteException):
    def __init__(self, group):
        super().__init__('', "requisite of type '%s'" % group)

    def __str__(self):
        return super().__str__()


class CookiesLookupError(AppBaseException):
    pass


class SessionNotFoundError(AppBaseException):
    pass


class SessionNotEndedError(AppBaseException):
    pass


class SessionEndedError(AppBaseException):
    pass


class SessionNotCompletedError(AppBaseException):
    pass


class SessionResetException(AppBaseException):
    pass


class InvalidModeSelection(AppBaseException):
    pass


class AttachmentError(AppBaseException):
    pass


class ClassRoomNotFoundError(AppBaseException):
    pass


class TPCMSBaseException(AppBaseException):
    pass


class SlotUpdateError(TPCMSBaseException):
    pass
