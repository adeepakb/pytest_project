from constants.test_management import get_testrail_reports,run_testrail_reports
# This should be called finally after execution of test suite.
# This would generate report at runtime as per testrail API Template and
# mail will be triggered to respective people added there.

report_id = get_testrail_reports("13")
run_testrail_reports(report_id)
