'''it is use for login purpose, registered user can log in by entering the mobile number'''
import pytest
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
from Constants.load_json import *
from Utilities.common_methods import CommonMethods


featureFileName = "LoginScenarios"
CommonMethods = CommonMethods()


class LoginPage():
    
    noneOftheAbove_xpath = (By.XPATH,"//android.widget.Button[@text='None of the above']")
    register_dialog_btn = (By.ID, "com.byjus.thelearningapp:id/primaryAction")
    allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    Btn_next_id = (By.ID, "com.byjus.thelearningapp:id/btnLogin")
    txt_phoneNum_id = (By.ID, "com.byjus.thelearningapp:id/etPhoneNumber")
    get_started_id = (By.ID, "com.byjus.thelearningapp:id/buttonGetStarted")
    login_link_id = (By.ID, "com.byjus.thelearningapp:id/tvLoginBl")
    Dropdown_country_id = (By.ID, "com.byjus.thelearningapp:id/spnrCountry")
    Login_TileTxt_xpath = (By.XPATH, "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp:id/llHeaderTextParent']//android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/header_title_text']")
    SeeuAgainTxt_xpath = (By.XPATH, "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp:id/llHeaderTextParent']//android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/header_subtitle_text']")
    Dropdown_CountryCodeTxt_id = (By.ID, "com.byjus.thelearningapp:id/drop_down_text_view")
    loginPageVerify_id = (By.XPATH, "//android.widget.TextView[@text='Login']")
    MobileNumTxtBx_id = (By.ID, "com.byjus.thelearningapp:id/etPhoneNumber")
    invalidMobNo_Message_id = (By.ID, "com.byjus.thelearningapp:id/tvPhoneError")
    otpText_id = (By.ID, "com.byjus.thelearningapp:id/tvWeWillSendOtp")
    newAcc_id = (By.ID, "com.byjus.thelearningapp:id/tvCreateNewAccountTxt")
    verifyText_xpath = (By.XPATH, "//android.widget.TextView[@text='Verify']")
    otp_TitleText = (By.ID, "com.byjus.thelearningapp:id/header_title_text")
    register_dialogMsg = (By.ID, "com.byjus.thelearningapp:id/dialog_message")
    chooseCourse_Title_xpath = (By.XPATH, "//android.widget.TextView[@text='your course']")
    tapOutsideDialogBox_id = (By.ID, "com.byjus.thelearningapp:id/touch_outside")
    dialogMessage_id = (By.ID, "com.byjus.thelearningapp:id/dialog_message")
    firstItemInCountryXCodeList_xpath = (By.XPATH, "//android.widget.TextView[@text='India (+91)']")
    lastItemInCountryXCodeList_xpath = (By.XPATH, "//android.widget.TextView[@text='Zimbabwe (+263)']")
    registerBtnInDialog_id = (By.ID, "com.byjus.thelearningapp:id/primaryAction")
    registerLink_id = (By.ID, "com.byjus.thelearningapp:id/tvRegister")
    dialogBoxUnregisteredNo_id = (By.ID, "com.byjus.thelearningapp:id/dialog_layout")
    skipBtn_id = (By.ID, "com.byjus.thelearningapp:id/buttonSkip")
    class8th_xpath = (By.XPATH,"//android.widget.Button[@text='8th']")
    back_button_id = (By.ID,"com.byjus.thelearningapp:id/backNav")
            
    def allowPopUp(self,driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.allow_btn_id, 3):
                CommonMethods.elementClick(driver, self.allow_btn_id)
                logging.info('Allowed device Location')
                CommonMethods.elementClick(driver, self.allow_btn_id)
                logging.info('Allowed your Contacts')  
            elif CommonMethods.wait_for_element_visible(driver, self.noneOftheAbove_xpath, 3):
                CommonMethods.elementClick(driver, self.noneOftheAbove_xpath)  
            else:
                logging.info('Permission are not allowed') 
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'allowPopUp')    
        except:
            CommonMethods.exception(driver, featureFileName, 'allowPopUp')
        
    def navigateToLoginPage(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.loginPageVerify_id, 3):
                logging.info('App Navigated to Login Screen Successfully')
            elif CommonMethods.wait_for_element_visible(driver, self.allow_btn_id, 3):
                CommonMethods.elementClick(driver, self.allow_btn_id)
                CommonMethods.elementClick(driver, self.allow_btn_id)
                check = CommonMethods.wait_for_element_visible(driver, self.loginPageVerify_id, 3)
                if check == True:
                    logging.info('App Navigated to Login Screen Successfully')
                elif CommonMethods.wait_for_element_visible(driver, self.skipBtn_id, 3):
                    CommonMethods.elementClick(driver, self.skipBtn_id)
                    CommonMethods.wait_for_element_visible(driver, self.chooseCourse_Title_xpath, 5)
                    CommonMethods.elementClick(driver, self.class8th_xpath)
                    CommonMethods.wait_for_element_visible(driver, self.noneOftheAbove_xpath, 7)
                    CommonMethods.elementClick(driver, self.noneOftheAbove_xpath)
                    CommonMethods.elementClick(driver, self.login_link_id)
                    self.navigateToLoginPage(driver)
            elif CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                CommonMethods.run('adb shell pm clear com.byjus.thelearningapp')
                CommonMethods.run('adb shell am start -n com.byjus.thelearningapp/com.byjus.app.onboarding.activity.SplashActivity')
                self.navigateToLoginPage(driver)    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'navigateToLoginPage')    
        except:
            CommonMethods.exception(driver, featureFileName, 'navigateToLoginPage')
    
    def enterMobileNo(self,driver):
        CommonMethods.enterText(self, driver,getdata(PATH('../Test_data/login_data.json'),"login_details","mob_no"), self.txt_phoneNum_id, "id")
 
        
    def click_on_next(self,driver):
        CommonMethods.elementClick(self,driver,self.Btn_next_id)
        
     
    def clickOnLoginLink(self,driver):
        CommonMethods.elementClick(self,driver,self.login_link_id)
         
         
    def verifyMobileNum_TxtBx(self,driver):
        try:
            check = CommonMethods.isElementPresent(self,driver,self.txt_phoneNum_id)
            if(check == True):
                pass
            else:
                logging.ERROR('Mobile Number Text Box is Not Present')
                logging.ERROR("Failed Locator in Method verifyMobileNum_TxtBx")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(self, driver, featureFileName, 'verifyMobileNum_TxtBx')
             
    def verifyHeaderSubtitle_Txt(self,driver,text1,text2):
        try:
            logging.info(text1)
            logging.info(text2)
            title = CommonMethods.getTextOfElement(self,driver,self.Login_TileTxt_xpath,"xpath")
            logging.info(title)
            subTitle = CommonMethods.getTextOfElement(self,driver,self.SeeuAgainTxt_xpath,"xpath")
            logging.info(subTitle)
            if title==text1 and subTitle==text2 :
                logging.info(' Header and Sub Title Text verified Successfully ')
            else:
                logging.info('Header and Sub Title Text did not match')
                logging.info("Failed Locator in Method verifyHeaderSubtitle_Txt")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method verifyHeaderSubtitle_Txt")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
             
    def tapOnCountryCode(self,driver):
        try:
            check = CommonMethods.elementClick(driver,self.Dropdown_country_id)
            if(check == True):
                logging.info('Clicked On Country Code Drop down')
            else:
                logging.error('Failed to Tap On Country Code')
                logging.error("Failed Locator in Method tapOnCountryCode")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tapOnCountryCode')
             
        except:
            CommonMethods.exception(driver,featureFileName,'tapOnCountryCode')
             
    def selectTheCountryCode(self,driver,countryCode):
        try:
            check = CommonMethods.scrollToElementAndClick(driver,countryCode)
            if check == True:
                logging.info(countryCode+' is Selected')
            else:
                logging.error('Failed to select Country Code')
                logging.error("Failed Locator in Method selectTheCountryCode")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'selectTheCountryCode')
             
        except:
            CommonMethods.exception(driver,featureFileName,'selectTheCountryCode')
             
    def verifyCountryCode(self,driver,actualcountryCode):
        try:
            countryCode = CommonMethods.getTextOfElement(driver,self.Dropdown_CountryCodeTxt_id)
            check = CommonMethods.verifyTwoText(actualcountryCode,countryCode)
             
            if check == True:
                logging.info(actualcountryCode+" and "+countryCode+" are same and verified")
            else:
                logging.error('Failed to verify Country Code')
                logging.error("Failed Locator in Method verifyCountryCode")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyCountryCode')
             
        except:
            CommonMethods.exception(driver,featureFileName,'verifyCountryCode')
             
             
    def verifyAppIsInLoginPage(self,driver):
        try:
#             if CommonMethods.isElementPresent(driver, self.noneOftheAbove_xpath):
#                 CommonMethods.elementClick(driver,self.noneOftheAbove_xpath)
            check = CommonMethods.isElementPresent(driver,self.loginPageVerify_id)
            if CommonMethods.isElementPresent(driver, self.noneOftheAbove_xpath):
                CommonMethods.elementClick(driver,self.noneOftheAbove_xpath)
            if check == True:
                pass
            else:
                logging.info('Failed in Launching Login Page')
                logging.info("Failed Locator in Method verifyAppIsInLoginPage")
                pytest.fail("Failed Due to Locator in Login Page")
    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyAppIsInLoginPage') 
               
        except :
            CommonMethods.exception(driver, featureFileName,'verifyAppIsInLoginPage')
       
                 
    def verifyGccCountriesList(self,driver):
        try:
            countryList = getdata(PATH('../Test_data/login_data.json'),"login_details","mob_no")
            check = CommonMethods.scrollToElement(self,driver,self.loginPageVerify_id1,"id")
         
            if check == True:
                logging.info('Sucessfully Login Page verified')
            else:
                logging.info('Failed in Launching Login Page')
                logging.info("Failed Locator in Method verifyAppIsInLoginPage")
                pytest.fail("Failed Due to Locator in Login Page")
    
        except NoSuchElementException:
            logging.info("Failed Locator in Method verifyAppIsInLoginPage")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
             
        except :
            logging.info("Failed Locator in Method verifyAppIsInLoginPage")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")        
             
    def tapsOnMobileNumberField(self,driver):
        try:
            check = CommonMethods.elementClick(driver,self.MobileNumTxtBx_id)
            if check == True:
                logging.info('User cliked on mobile num field')
            else:
                logging.info('Failed in Tapping Mobile Text Box')
                logging.info("Failed Locator in Method tapOnMobileNumberField")
                pytest.fail("Failed Due to Locator in Login Page")
    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tapsOnMobileNumberField') 
               
        except :
            CommonMethods.exception(driver, featureFileName,'tapsOnMobileNumberField')  
     
    def verifynumericKeypadActive(self,driver):
        try:
            check = CommonMethods.isKeyBoardShown(driver)
            if check == True:
                logging.info('Numeric key board is shown')
                driver.back()
                sleep(3)
            else:
                logging.info('Failed to show the Keyboard')
                logging.info("Failed Locator in Method verifynumericKeypadActive")
                pytest.fail("Failed Due to Locator in Login Page")
    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifynumericKeypadActive') 
               
        except :
            CommonMethods.exception(driver, featureFileName,'verifynumericKeypadActive') 
             
    def verifyAcceptsNumericOnly(self,driver):
        try:
            CommonMethods.enterText(driver,"123456",self.MobileNumTxtBx_id)
            sleep(2)
            txtToCheck = CommonMethods.getTextOfElement(driver,self.MobileNumTxtBx_id)
            sleep(1)
            check = txtToCheck.isdigit()
            sleep(1)
            if check == True:
                pass
            else:
                logging.info('Failed to show the Keyboard')
                logging.info("Failed Locator in Method verifyAcceptsNumericOnly")
                pytest.fail("Failed Due to Locator in Login Page")
    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyAcceptsNumericOnly') 
               
        except :
            CommonMethods.exception(driver, featureFileName,'verifyAcceptsNumericOnly')   
             
 
    def enterUnRegisteredMobileNo(self,driver,mobNum):
        try:
            CommonMethods.enterText(self, driver,mobNum, self.txt_phoneNum_id, "id")
     
        except NoSuchElementException:
            logging.info("Failed Locator in Method enterUnRegisteredMobileNo")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Locator in Method enterUnRegisteredMobileNo")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")   
 
    def verifyInvalidMobNoMessage(self,driver):
        try:
#             expected=getdata(PATH('../Test_data/login_data.json'),"login_details","invalid_mobno_msg")
            actual=CommonMethods.getTextOfElement(self,driver,self.invalidMobNo_Message_id,"id")
            check=CommonMethods.verifyTwoText(self,actual,getdata(PATH('../Test_data/login_data.json'),"login_details","invalid_mobno_msg"))
             
            if check == True:
                logging.info('Invalid message is correct')
            else:
                logging.info('Failed in Launching Login Page')
                logging.info("Invalid message is Incorrect")
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except :
            logging.info("Failed Locator in Method verifyInvalidMobNoMessage")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page") 
             
    def verifyTextPresent(self,driver,text):
        try:
            check = CommonMethods.findText(driver,text)
            if check == True:
                logging.info(text+' is present and verified')
            else:
                logging.error('Failed in Finding the text '+text)
                CommonMethods.takeScreenShot(driver,featureFileName)
                pytest.fail("Failed in login page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyTextPresent')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyTextPresent')
             
    def verifyErrorMsg(self, driver, error_msg):
        try:
            check1 = CommonMethods.wait_for_element_visible(driver, self.invalidMobNo_Message_id, 3)
            expec_err_msg = error_msg
            actual_err_msg = CommonMethods.getAttributeOfElement(driver, 'text', self.invalidMobNo_Message_id)
            check2 = CommonMethods.verifyTwoText(expec_err_msg, actual_err_msg)
            if check1 and check2:
                logging.info('Error message verified successfully')
            else:
                logging.error('Failed in Finding the text ')
                CommonMethods.takeScreenShot(driver,featureFileName)
                pytest.fail("Failed in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyErrorMsg')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyErrorMsg')
             
    def verifyButtonPresent(self,driver,text):
        try:
            check = CommonMethods.findButton(driver,text)
            if check == True:
                logging.info(text+' button is verified')
            else:
                logging.info(text+" Button not Present in the Screen")
                logging.info('Failed in Finding Button '+text)
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyButtonPresent')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyButtonPresent')
         
     
    def verifyLinkPresent(self,driver,text):
        try:
            check = CommonMethods.findLink(driver,text)
            if check == True:
                logging.info(text+' link is Verified')
            else:
                logging.error(text+" Link not Present in the Screen")
                logging.error('Failed in Finding Link '+text)
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyLinkPresent')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyLinkPresent')     
 
    def enterText(self,driver,text):
        try:
            check = CommonMethods.enterText(self,driver,text,self.MobileNumTxtBx_id,"id")
            sleep(2)
            if check == True:
                logging.info(text+ " entered Successfully")
            else:
                logging.info(text+" Failed to enter the text")
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            logging.info("Failed Locator in Method enterText")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method enterText")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")  
             
    def tapOnNextBtn(self,driver):
        try: 
            if CommonMethods.wait_for_element_visible(driver, self.Btn_next_id, 3):
                CommonMethods.elementClick(driver, self.Btn_next_id)
                logging.info('Clicked on Next Button Successfully')
            else:
                logging.error("Failed to click Next Button")
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tapOnNextBtn')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'tapOnNextBtn')
             
    def verifyEnterValidNum(self,driver,text):
        try:
            ErrTxt = CommonMethods.getTextOfElement(self,driver,self.invalidMobNo_Message_id,"id")
             
            if ErrTxt == text:
                logging.info("Error message is Displayed Successfully")
            else:
                logging.info("Failed to Display Error Message")
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            logging.info("Failed Locator in Method verifyEnterValidNum")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method verifyEnterValidNum")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")
             
    def verifyOTPText(self,driver,expected):
        try:
            check = CommonMethods.scrollToElement(self,driver,expected)
            if check == True:
                logging.info(expected+ " is present in the Screen")
            else:
                logging.info("Failed to Display "+expected )
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            logging.info("Given "+expected+" is inCorrect or not Present ")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method verifyOTPText")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")
             
             
    def verifyNextBtn(self,driver):
        try:
            check = CommonMethods.isElementPresent(self,driver,self.Btn_next_id,"id")
            if check == True:
                logging.info("Next Button is Present in Login Page")
            else:
                logging.info("Next Button is Not Present in Login Page")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException:
            logging.info("Given Locator is not visible or not found")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method verifyNextBtn")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")
             
    def verifyCreateNewAcc(self,driver,expected):
        try:
            newAccText = CommonMethods.getTextOfElement(self,driver,self.newAcc_id,"id")
                 
        except NoSuchElementException:
            logging.info("Given "+expected+" is inCorrect or not Present ")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method verifyOTPText")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")
             
    def enterMobileNum(self,driver,mobNum):
        try:
            check = CommonMethods.enterText(self,driver,mobNum,self.MobileNumTxtBx_id,"id")
            if check == True:
                logging.info(mobNum+ ' Entered Successfully')
            else:
                logging.info(mobNum+' failed to Enter')
                 
        except NoSuchElementException:
            logging.info("Given "+mobNum+" is inCorrect or not Present ")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method enterMobileNum")
            CommonMethods.takeScreenShot(self,driver,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")
    
    def verifyDialogMessage(self, driver, message):
        try:
            actual = CommonMethods.getTextOfElement(self, driver, self.dialogMessage_id)
            check = CommonMethods.verifyTwoText(self, actual, message)
             
            if check == True:
                logging.info('Invalid message is correct')
            else:
                logging.info('Failed in Launching Login Page')
                logging.info("Invalid message is Incorrect")
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except :
            logging.info("Failed Locator in Method verifyInvalidMobNoMessage")
            CommonMethods.takeScreenShot(self, driver, featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
 
    def clickOnRegisterLink(self, driver):
        try:
            check = CommonMethods.elementClick(self, driver, self.registerLink_id, "id")
            if(check == True):
                logging.info('Sucessfully Tapped On Register Link')
            else:
                logging.info('Failed to Tap On Register Link')
                logging.info("Failed Locator in Method clickOnRegisterLink")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method clickOnRegisterLink")
            pytest.fail("Failed Due to Locator in Login Page")        
 
    def checkRegisterBtnInDialog(self, driver):
        try:
            check = CommonMethods.isElementPresent(self, driver, self.registerBtnInDialog_id, "id")
            if(check == True):
                logging.info('Register Button is displayed')
            else:
                logging.info('Register Button is not present')
                logging.info("Failed Locator in Method checkRegisterBtnInDialog")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method checkRegisterBtnInDialog")
            pytest.fail("Failed Due to Locator in Login Page")  
             
    def checkDialogBoxDisplay(self, driver):
        try:
            check = CommonMethods.isElementPresent(self, driver, self.dialogBoxUnregisteredNo_id, "id")
            if(check == True):
                logging.info('Dialog box for unregistered no is displayed')
            else:
                logging.info('Dialog box is not present')
                logging.info("Failed Locator in Method checkDialogBoxDisplay")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method checkDialogBoxDisplay")
            pytest.fail("Failed Due to Locator in Login Page")  
 
    def clickOnRegisterBtnInDialogBox(self, driver):
        try:
            check = CommonMethods.elementClick(driver, self.registerBtnInDialog_id)
            if(check == True):
                pass
            else:
                logging.info('Register button is not present')
                logging.info("Failed Locator in Method clickOnRegisterBtnInDialogBox")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'clickOnRegisterBtnInDialogBox')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'clickOnRegisterBtnInDialogBox')  
 
 
    def clickOutsideToDismisDialogBox(self, driver):
        try:
            check = CommonMethods.elementClick(self, driver, self.tapOutsideDialogBox_id, "id")
            if(check == True):
                logging.info('clicked outside the dialog box')
            else:
                logging.info('dialog box is not present')
                logging.info("Failed Locator in Method clickOutsideToDismisDialogBox")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method clickOutsideToDismisDialogBox")
            pytest.fail("Failed Due to Locator in Login Page")  
 
    def verifyDialogBoxDismiss(self, driver):
        try:
            check = CommonMethods.isElementPresent(self, driver, self.dialogBoxUnregisteredNo_id, "id")
#             check = checkDialogBoxDisplay(driver)
            logging.info(check)
            if (check == False):
                logging.info('Dialog box is dismissed')
            else:
                logging.info('dialog box is not dismissed')
                logging.info("Failed Locator in Method verifyDialogBoxDismiss")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method verifyDialogBoxDismiss")
            pytest.fail("Failed Due to Locator in Login Page") 
             
    def clickOnDeviceBackButton(self, driver):
        try:
            driver.back()
        except :
            logging.info("failed in clicking on device back button")
            logging.info("Failed in Method clickOnDeviceBackButton")
            pytest.fail("failed in clicking on device back button")
             
    def checkLoginLinkPresence(self, driver):
        try:
            check = CommonMethods.isElementPresent(self, driver, self.login_link_id, "id")
            if(check == False):
                logging.info('Login link is not displaying so app is closed')
            else:
                logging.info('Login link is present')
                logging.info("Failed in Method checkLoginLinkPresence")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method checkLoginLinkPresence")
            pytest.fail("Failed Due to Locator in Login Page")
             
    def verifyMobileFieldAutofilled(self,driver):
        try:
            check = CommonMethods.verifyTextisPresent(driver,self.Dropdown_CountryCodeTxt_id)
            if check == True:
                logging.info('Mobiled number field is Auto filled')
            else:
                logging.info('Failed due to Mobile Number was not AutoFilled')
                CommonMethods.takeScreenShot(driver,featureFileName)
                pytest.fail("Failed in login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyMobileFieldAutofilled')
                     
        except :
            CommonMethods.exception(driver, featureFileName, 'verifyMobileFieldAutofilled')
             
    def verifyCountryCodeDrpDwn(self,driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.Dropdown_CountryCodeTxt_id, 3)
            if check == True:
                logging.info('Country Code Drop down is visible')
            else:
                logging.error('Failed due to Country code drop down is not present')
                CommonMethods.takeScreenShot(self,driver,featureFileName)
                pytest.fail("Failed in login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyMobileFieldAutofilled')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyMobileFieldAutofilled')
  
    def enterNumInBx(self,driver,data):
        try:
            check = CommonMethods.enterText(driver,data,self.txt_phoneNum_id)
            CommonMethods.hideKeyboard(driver)
            if check == True:
                logging.info(data+' entered successfully')
            else:
                logging.error('Failed in Enterin the text to Text Bx')
                CommonMethods.takeScreenShot(self,driver,featureFileName)
                pytest.fail("Failed in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'enterNumInBx')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'enterNumInBx')
            
    def verifyOTPscreen(self,driver):
        try:
            sleep(3)
            CommonMethods.wait_for_locator(driver, self.otp_TitleText, 15)
            check = CommonMethods.isElementPresent(driver, self.otp_TitleText)
            if check == True:
                logging.info('Verified OTP screen Successfully')
            else:
                logging.info('Failed in OTP Screen')
                CommonMethods.takeScreenShot(driver,featureFileName)
                pytest.fail("Failed in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyOTPscreen')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyOTPscreen')
             
    def tap_on_back_button(self,driver):
        try:
            CommonMethods.click_on_device_back_btn(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tap_on_back_button')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'tap_on_back_button')
             
    def verifynotRegistered(self,driver):
        try:
            
            check = CommonMethods.wait_for_element_visible(driver, self.register_dialogMsg, 3)
            if check == True:
                logging.info('Verified Not Registered')
            else:
                logging.info('Failed in Finding the text in method verifynotRegistered ')
                CommonMethods.takeScreenShot(driver,featureFileName)
                pytest.fail("Failed in "+os.path.basename(self.__class__.__name__))
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifynotRegistered')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifynotRegistered')
             
    def verifyRegisterBtn(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.register_dialog_btn, 3):
                logging.info('Verified Register Button')
            else:
                logging.info('Failed in Finding the text in method verifynotRegistered ')
                CommonMethods.takeScreenShot(driver,featureFileName)
                pytest.fail("Failed in "+os.path.basename(self.__class__.__name__))
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyRegisterBtn')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyRegisterBtn')
             
    def verifyNotRegisterPageDismissed(self,driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.register_dialog_btn, 3)
            if check == False:
                logging.info('Phone number is not registered is dismissed')
            else:
                logging.error('Failed in closing Registered Page in method verifyNotRegisterPageDismissed ')
                CommonMethods.takeScreenShot(driver,featureFileName)
                pytest.fail("Failed in "+os.path.basename(self.__class__.__name__))
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyNotRegisterPageDismissed')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyNotRegisterPageDismissed')
 
    def tapOnScreenOutsideDialogBx(self,driver):
        try:
            CommonMethods.run('adb shell input tap 100 100')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tapOnScreenOutsideDialogBx')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'tapOnScreenOutsideDialogBx')
             
    def verifyChooseYourCoursePage(self,driver):
        try:
            check = CommonMethods.isElementPresent(driver,self.chooseCourse_Title_xpath)
            if check == True:
                pass
            else:
                logging.info('Failed in verifyChooseYourCoursePage method ')
                CommonMethods.takeScreenShot(driver,featureFileName)
                pytest.fail("Failed in "+os.path.basename(self.__class__.__name__))
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyChooseYourCoursePage')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyChooseYourCoursePage')
             
    def tapOnLink(self,driver,text):
        try:
            check = CommonMethods.clickLink(driver,text)
            if check == True:
                pass
            else:
                logging.info(text+" Link not Present in the Screen")
                logging.info('Failed in Finding Link '+text)
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tapOnLink')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'tapOnLink')
             
    def verifyAppIsClosed(self,driver,text):
        try:
            check = CommonMethods.isAppActive(driver,text)
            if check == 3:
                pass
            else:
                logging.error(" App is Not Closed")
                pytest.fail("App is not closed")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyAppIsClosed')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyAppIsClosed')