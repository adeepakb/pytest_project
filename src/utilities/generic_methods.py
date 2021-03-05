import logging
from utilities.common_methods import CommonMethods
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

CommonMethods = CommonMethods()
f = open("../../test_data/featureFileName.txt","r")
# f = open("C:/EclipseWorkspaces/csse120/K12_master/src/test_data/featureFileName.txt","r")
featureFileName = f.read()


class GenericMethods():
#     On boarding screen locators
    allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    skipBtn_id = (By.ID, "com.byjus.thelearningapp:id/buttonSkip")
    
#    Choose you course locators
    chooseCourse_Title_xpath = (By.XPATH, "//android.widget.TextView[@text='your course']")
    
#    Register Page locators
    noneOftheAbove_xpath = (By.XPATH,"//android.widget.Button[@text='None of the above']")
    login_link_id = (By.ID, "com.byjus.thelearningapp:id/tvLoginBl")
    
#     Login Screen Locators
    loginPageVerify_id = (By.XPATH, "//android.widget.TextView[@text='Login']")
    
    
#    home Page Locators
    back_button_id = (By.ID,"com.byjus.thelearningapp:id/backNav")
    homescreen_corana_dialog_ok_btn = (By.XPATH,"//android.widget.TextView[@text = 'OK']")
    
    """
    This method is used to navigate to login page 
     
    """
    @classmethod
    def navigate_to_login_page(cls, browser, grade) -> None:
        try:
            grade_sel = grade
            grade_select_xpath = (By.XPATH,"//android.widget.Button[@text=\'"+grade_sel+"\']")
            if CommonMethods.wait_for_element_visible(browser, GenericMethods.loginPageVerify_id, 7):
                logging.info('App Navigated to Login Screen Successfully')
            elif CommonMethods.wait_for_element_visible(browser, GenericMethods.allow_btn_id, 7):
                CommonMethods.elementClick(browser, GenericMethods.allow_btn_id)
                CommonMethods.elementClick(browser, GenericMethods.allow_btn_id)
                check = CommonMethods.wait_for_element_visible(browser, GenericMethods.loginPageVerify_id, 7)
                if check == True:
                    logging.info('App Navigated to Login Screen Successfully')
                elif CommonMethods.wait_for_element_visible(browser, GenericMethods.skipBtn_id, 7):
                    CommonMethods.elementClick(browser, GenericMethods.skipBtn_id)
                    CommonMethods.wait_for_element_visible(browser, GenericMethods.chooseCourse_Title_xpath, 7)
                    CommonMethods.elementClick(browser, grade_select_xpath)
                    CommonMethods.wait_for_element_visible(browser, GenericMethods.noneOftheAbove_xpath, 7)
                    CommonMethods.elementClick(browser, GenericMethods.noneOftheAbove_xpath)
                    CommonMethods.elementClick(browser, GenericMethods.login_link_id)
                    GenericMethods.navigate_to_login_page(browser, grade_sel)
            else: 
                CommonMethods.run('adb shell pm clear com.byjus.thelearningapp')
                CommonMethods.run('adb shell am start -n com.byjus.thelearningapp/com.byjus.app.onboarding.activity.SplashActivity')
                GenericMethods.navigate_to_login_page(browser, grade_sel)    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'navigate_to_login_page')    
        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_login_page')
        
