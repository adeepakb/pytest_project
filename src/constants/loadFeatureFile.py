import os
import sys
# import test_management
# from test_management import *
from constants.test_management import *


def fetch_featurefile(suite_ID, project_ID, run_ID):
    create_feature_from_run(suite_ID, project_ID, run_ID)


suite_name = "Byju's Classes"
if suite_name == 'Regression_PremiumApp_Automation':
    fetch_featurefile("160", "13", "184")
elif suite_name == 'Sanity_PremiumApp_Automation':
    fetch_featurefile("160", "13", "256")
elif suite_name == "Byju's Classes":
    fetch_featurefile("199", "24", "503")
