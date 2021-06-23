# Module Owner - Prasanth C
from pages.base.trialclass_base import TrialClassBase


class TrialClassWeb(TrialClassBase):
    def __init__(self, driver):
        self.driver = driver
