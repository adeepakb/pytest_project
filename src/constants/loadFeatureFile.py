from constants.test_management import *


def fetch_feature_file(suite_id, run_id):
    create_feature_from_run(suite_id, run_id)


suite_name = os.getenv('suite')
if suite_name == 'Regression_PremiumApp_Automation':
    fetch_feature_file("160", "184")
elif suite_name == 'Sanity_PremiumApp_Automation':
    fetch_feature_file("160", "256")
elif suite_name == "Byju's Classes":
    fetch_feature_file("160", "246")
