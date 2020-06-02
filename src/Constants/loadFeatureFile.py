import os
import sys
# import test_management
# from test_management import *
from Constants.test_management import *


def fetch_featurefile(suite_ID, project_ID, run_ID):
    create_feature_from_run(suite_ID, project_ID, run_ID)
    
fetch_featurefile("141", "6", "136")

