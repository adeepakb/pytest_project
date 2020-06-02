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
            
    def allowPopUp(self,browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.allow_btn_id, 3):
                CommonMethods.elementClick(browser, self.allow_btn_id)
                logging.info('Allowed device Location')
                CommonMethods.elementClick(browser, self.allow_btn_id)
                logging.info('Allowed your Contacts')  
            elif CommonMethods.wait_for_element_visible(browser, self.noneOftheAbove_xpath, 3):
                CommonMethods.elementClick(browser, self.noneOftheAbove_xpath)  
            else:
                logging.info('Permission are not allowed') 
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'allowPopUp')    
        except:
            CommonMethods.exception(browser, featureFileName, 'allowPopUp')
        
    def navigateToLoginPage(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.loginPageVerify_id, 3):
                logging.info('App Navigated to Login Screen Successfully')
            elif CommonMethods.wait_for_element_visible(browser, self.allow_btn_id, 3):
                CommonMethods.elementClick(browser, self.allow_btn_id)
                CommonMethods.elementClick(browser, self.allow_btn_id)
                check = CommonMethods.wait_for_element_visible(browser, self.loginPageVerify_id, 3)
                if check == True:
                    logging.info('App Navigated to Login Screen Successfully')
                elif CommonMethods.wait_for_element_visible(browser, self.skipBtn_id, 3):
                    CommonMethods.elementClick(browser, self.skipBtn_id)
                    CommonMethods.wait_for_element_visible(browser, self.chooseCourse_Title_xpath, 5)
                    CommonMethods.elementClick(browser, self.class8th_xpath)
                    CommonMethods.wait_for_element_visible(browser, self.noneOftheAbove_xpath, 7)
                    CommonMethods.elementClick(browser, self.noneOftheAbove_xpath)
                    CommonMethods.elementClick(browser, self.login_link_id)
                    self.navigateToLoginPage(browser)
            elif CommonMethods.wait_for_element_visible(browser, self.back_button_id, 3):
                CommonMethods.run('adb shell pm clear com.byjus.thelearningapp')
                CommonMethods.run('adb shell am start -n com.byjus.thelearningapp/com.byjus.app.onboarding.activity.SplashActivity')
                self.navigateToLoginPage(browser)    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'navigateToLoginPage')    
        except:
            CommonMethods.exception(browser, featureFileName, 'navigateToLoginPage')
    
    def enterMobileNo(self,browser):
        CommonMethods.enterText(self, browser,getdata(PATH('../Test_data/login_data.json'),"login_details","mob_no"), self.txt_phoneNum_id, "id")
 
        
    def click_on_next(self,browser):
        CommonMethods.elementClick(self,browser,self.Btn_next_id)
        
     
    def clickOnLoginLink(self,browser):
        CommonMethods.elementClick(self,browser,self.login_link_id)
         
         
    def verifyMobileNum_TxtBx(self,browser):
        try:
            check = CommonMethods.isElementPresent(self,browser,self.txt_phoneNum_id)
            if(check == True):
                pass
            else:
                logging.ERROR('Mobile Number Text Box is Not Present')
                logging.ERROR("Failed Locator in Method verifyMobileNum_TxtBx")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(self, browser, featureFileName, 'verifyMobileNum_TxtBx')
             
    def verifyHeaderSubtitle_Txt(self,browser,text1,text2):
        try:
            logging.info(text1)
            logging.info(text2)
            title = CommonMethods.getTextOfElement(self,browser,self.Login_TileTxt_xpath,"xpath")
            logging.info(title)
            subTitle = CommonMethods.getTextOfElement(self,browser,self.SeeuAgainTxt_xpath,"xpath")
            logging.info(subTitle)
            if title==text1 and subTitle==text2 :
                logging.info(' Header and Sub Title Text verified Successfully ')
            else:
                logging.info('Header and Sub Title Text did not match')
                logging.info("Failed Locator in Method verifyHeaderSubtitle_Txt")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method verifyHeaderSubtitle_Txt")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
             
    def tapOnCountryCode(self,browser):
        try:
            check = CommonMethods.elementClick(browser,self.Dropdown_country_id)
            if(check == True):
                logging.info('Clicked On Country Code Drop down')
            else:
                logging.error('Failed to Tap On Country Code')
                logging.error("Failed Locator in Method tapOnCountryCode")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tapOnCountryCode')
             
        except:
            CommonMethods.exception(browser,featureFileName,'tapOnCountryCode')
             
    def selectTheCountryCode(self,browser,countryCode):
        try:
            check = CommonMethods.scrollToElementAndClick(browser,countryCode)
            if check == True:
                logging.info(countryCode+' is Selected')
            else:
                logging.error('Failed to select Country Code')
                logging.error("Failed Locator in Method selectTheCountryCode")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'selectTheCountryCode')
             
        except:
            CommonMethods.exception(browser,featureFileName,'selectTheCountryCode')
             
    def verifyCountryCode(self,browser,actualcountryCode):
        try:
            countryCode = CommonMethods.getTextOfElement(browser,self.Dropdown_CountryCodeTxt_id)
            check = CommonMethods.verifyTwoText(actualcountryCode,countryCode)
             
            if check == True:
                logging.info(actualcountryCode+" and "+countryCode+" are same and verified")
            else:
                logging.error('Failed to verify Country Code')
                logging.error("Failed Locator in Method verifyCountryCode")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyCountryCode')
             
        except:
            CommonMethods.exception(browser,featureFileName,'verifyCountryCode')
             
             
    def verifyAppIsInLoginPage(self,browser):
        try:
#             if CommonMethods.isElementPresent(browser, self.noneOftheAbove_xpath):
#                 CommonMethods.elementClick(browser,self.noneOftheAbove_xpath)
            check = CommonMethods.isElementPresent(browser,self.loginPageVerify_id)
            if CommonMethods.isElementPresent(browser, self.noneOftheAbove_xpath):
                CommonMethods.elementClick(browser,self.noneOftheAbove_xpath)
            if check == True:
                pass
            else:
                logging.info('Failed in Launching Login Page')
                logging.info("Failed Locator in Method verifyAppIsInLoginPage")
                pytest.fail("Failed Due to Locator in Login Page")
    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyAppIsInLoginPage') 
               
        except :
            CommonMethods.exception(browser, featureFileName,'verifyAppIsInLoginPage')
       
                 
    def verifyGccCountriesList(self,browser):
        try:
            countryList = getdata(PATH('../Test_data/login_data.json'),"login_details","mob_no")
            check = CommonMethods.scrollToElement(self,browser,self.loginPageVerify_id1,"id")
         
            if check == True:
                logging.info('Sucessfully Login Page verified')
            else:
                logging.info('Failed in Launching Login Page')
                logging.info("Failed Locator in Method verifyAppIsInLoginPage")
                pytest.fail("Failed Due to Locator in Login Page")
    
        except NoSuchElementException:
            logging.info("Failed Locator in Method verifyAppIsInLoginPage")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
             
        except :
            logging.info("Failed Locator in Method verifyAppIsInLoginPage")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")        
             
    def tapsOnMobileNumberField(self,browser):
        try:
            check = CommonMethods.elementClick(browser,self.MobileNumTxtBx_id)
            if check == True:
                logging.info('User cliked on mobile num field')
            else:
                logging.info('Failed in Tapping Mobile Text Box')
                logging.info("Failed Locator in Method tapOnMobileNumberField")
                pytest.fail("Failed Due to Locator in Login Page")
    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tapsOnMobileNumberField') 
               
        except :
            CommonMethods.exception(browser, featureFileName,'tapsOnMobileNumberField')  
     
    def verifynumericKeypadActive(self,browser):
        try:
            check = CommonMethods.isKeyBoardShown(browser)
            if check == True:
                logging.info('Numeric key board is shown')
                browser.back()
                sleep(3)
            else:
                logging.info('Failed to show the Keyboard')
                logging.info("Failed Locator in Method verifynumericKeypadActive")
                pytest.fail("Failed Due to Locator in Login Page")
    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifynumericKeypadActive') 
               
        except :
            CommonMethods.exception(browser, featureFileName,'verifynumericKeypadActive') 
             
    def verifyAcceptsNumericOnly(self,browser):
        try:
            CommonMethods.enterText(browser,"123456",self.MobileNumTxtBx_id)
            sleep(2)
            txtToCheck = CommonMethods.getTextOfElement(browser,self.MobileNumTxtBx_id)
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
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyAcceptsNumericOnly') 
               
        except :
            CommonMethods.exception(browser, featureFileName,'verifyAcceptsNumericOnly')   
             
 
    def enterUnRegisteredMobileNo(self,browser,mobNum):
        try:
            CommonMethods.enterText(self, browser,mobNum, self.txt_phoneNum_id, "id")
     
        except NoSuchElementException:
            logging.info("Failed Locator in Method enterUnRegisteredMobileNo")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Locator in Method enterUnRegisteredMobileNo")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")   
 
    def verifyInvalidMobNoMessage(self,browser):
        try:
#             expected=getdata(PATH('../Test_data/login_data.json'),"login_details","invalid_mobno_msg")
            actual=CommonMethods.getTextOfElement(self,browser,self.invalidMobNo_Message_id,"id")
            check=CommonMethods.verifyTwoText(self,actual,getdata(PATH('../Test_data/login_data.json'),"login_details","invalid_mobno_msg"))
             
            if check == True:
                logging.info('Invalid message is correct')
            else:
                logging.info('Failed in Launching Login Page')
                logging.info("Invalid message is Incorrect")
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except :
            logging.info("Failed Locator in Method verifyInvalidMobNoMessage")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page") 
             
    def verifyTextPresent(self,browser,text):
        try:
            check = CommonMethods.findText(browser,text)
            if check == True:
                logging.info(text+' is present and verified')
            else:
                logging.error('Failed in Finding the text '+text)
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed in login page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyTextPresent')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyTextPresent')
             
    def verifyErrorMsg(self, browser, error_msg):
        try:
            check1 = CommonMethods.wait_for_element_visible(browser, self.invalidMobNo_Message_id, 3)
            expec_err_msg = error_msg
            actual_err_msg = CommonMethods.getAttributeOfElement(browser, 'text', self.invalidMobNo_Message_id)
            check2 = CommonMethods.verifyTwoText(expec_err_msg, actual_err_msg)
            if check1 and check2:
                logging.info('Error message verified successfully')
            else:
                logging.error('Failed in Finding the text ')
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyErrorMsg')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyErrorMsg')
             
    def verifyButtonPresent(self,browser,text):
        try:
            check = CommonMethods.findButton(browser,text)
            if check == True:
                logging.info(text+' button is verified')
            else:
                logging.info(text+" Button not Present in the Screen")
                logging.info('Failed in Finding Button '+text)
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyButtonPresent')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyButtonPresent')
         
     
    def verifyLinkPresent(self,browser,text):
        try:
            check = CommonMethods.findLink(browser,text)
            if check == True:
                logging.info(text+' link is Verified')
            else:
                logging.error(text+" Link not Present in the Screen")
                logging.error('Failed in Finding Link '+text)
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyLinkPresent')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyLinkPresent')     
 
    def enterText(self,browser,text):
        try:
            check = CommonMethods.enterText(self,browser,text,self.MobileNumTxtBx_id,"id")
            sleep(2)
            if check == True:
                logging.info(text+ " entered Successfully")
            else:
                logging.info(text+" Failed to enter the text")
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            logging.info("Failed Locator in Method enterText")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method enterText")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")  
             
    def tapOnNextBtn(self,browser):
        try: 
            if CommonMethods.wait_for_element_visible(browser, self.Btn_next_id, 3):
                CommonMethods.elementClick(browser, self.Btn_next_id)
                logging.info('Clicked on Next Button Successfully')
            else:
                logging.error("Failed to click Next Button")
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tapOnNextBtn')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'tapOnNextBtn')
             
    def verifyEnterValidNum(self,browser,text):
        try:
            ErrTxt = CommonMethods.getTextOfElement(self,browser,self.invalidMobNo_Message_id,"id")
             
            if ErrTxt == text:
                logging.info("Error message is Displayed Successfully")
            else:
                logging.info("Failed to Display Error Message")
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            logging.info("Failed Locator in Method verifyEnterValidNum")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method verifyEnterValidNum")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")
             
    def verifyOTPText(self,browser,expected):
        try:
            check = CommonMethods.scrollToElement(self,browser,expected)
            if check == True:
                logging.info(expected+ " is present in the Screen")
            else:
                logging.info("Failed to Display "+expected )
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            logging.info("Given "+expected+" is inCorrect or not Present ")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method verifyOTPText")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")
             
             
    def verifyNextBtn(self,browser):
        try:
            check = CommonMethods.isElementPresent(self,browser,self.Btn_next_id,"id")
            if check == True:
                logging.info("Next Button is Present in Login Page")
            else:
                logging.info("Next Button is Not Present in Login Page")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException:
            logging.info("Given Locator is not visible or not found")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method verifyNextBtn")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")
             
    def verifyCreateNewAcc(self,browser,expected):
        try:
            newAccText = CommonMethods.getTextOfElement(self,browser,self.newAcc_id,"id")
                 
        except NoSuchElementException:
            logging.info("Given "+expected+" is inCorrect or not Present ")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method verifyOTPText")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")
             
    def enterMobileNum(self,browser,mobNum):
        try:
            check = CommonMethods.enterText(self,browser,mobNum,self.MobileNumTxtBx_id,"id")
            if check == True:
                logging.info(mobNum+ ' Entered Successfully')
            else:
                logging.info(mobNum+' failed to Enter')
                 
        except NoSuchElementException:
            logging.info("Given "+mobNum+" is inCorrect or not Present ")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
                     
        except :
            logging.info("Failed Due to Exception in method enterMobileNum")
            CommonMethods.takeScreenShot(self,browser,featureFileName)
            pytest.fail("Failed Due to Exception in Login Page")
    
    def verifyDialogMessage(self, browser, message):
        try:
            actual = CommonMethods.getTextOfElement(self, browser, self.dialogMessage_id)
            check = CommonMethods.verifyTwoText(self, actual, message)
             
            if check == True:
                logging.info('Invalid message is correct')
            else:
                logging.info('Failed in Launching Login Page')
                logging.info("Invalid message is Incorrect")
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except :
            logging.info("Failed Locator in Method verifyInvalidMobNoMessage")
            CommonMethods.takeScreenShot(self, browser, featureFileName)
            pytest.fail("Failed Due to Locator in Login Page")
 
    def clickOnRegisterLink(self, browser):
        try:
            check = CommonMethods.elementClick(self, browser, self.registerLink_id, "id")
            if(check == True):
                logging.info('Sucessfully Tapped On Register Link')
            else:
                logging.info('Failed to Tap On Register Link')
                logging.info("Failed Locator in Method clickOnRegisterLink")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method clickOnRegisterLink")
            pytest.fail("Failed Due to Locator in Login Page")        
 
    def checkRegisterBtnInDialog(self, browser):
        try:
            check = CommonMethods.isElementPresent(self, browser, self.registerBtnInDialog_id, "id")
            if(check == True):
                logging.info('Register Button is displayed')
            else:
                logging.info('Register Button is not present')
                logging.info("Failed Locator in Method checkRegisterBtnInDialog")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method checkRegisterBtnInDialog")
            pytest.fail("Failed Due to Locator in Login Page")  
             
    def checkDialogBoxDisplay(self, browser):
        try:
            check = CommonMethods.isElementPresent(self, browser, self.dialogBoxUnregisteredNo_id, "id")
            if(check == True):
                logging.info('Dialog box for unregistered no is displayed')
            else:
                logging.info('Dialog box is not present')
                logging.info("Failed Locator in Method checkDialogBoxDisplay")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method checkDialogBoxDisplay")
            pytest.fail("Failed Due to Locator in Login Page")  
 
    def clickOnRegisterBtnInDialogBox(self, browser):
        try:
            check = CommonMethods.elementClick(browser, self.registerBtnInDialog_id)
            if(check == True):
                pass
            else:
                logging.info('Register button is not present')
                logging.info("Failed Locator in Method clickOnRegisterBtnInDialogBox")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'clickOnRegisterBtnInDialogBox')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'clickOnRegisterBtnInDialogBox')  
 
 
    def clickOutsideToDismisDialogBox(self, browser):
        try:
            check = CommonMethods.elementClick(self, browser, self.tapOutsideDialogBox_id, "id")
            if(check == True):
                logging.info('clicked outside the dialog box')
            else:
                logging.info('dialog box is not present')
                logging.info("Failed Locator in Method clickOutsideToDismisDialogBox")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method clickOutsideToDismisDialogBox")
            pytest.fail("Failed Due to Locator in Login Page")  
 
    def verifyDialogBoxDismiss(self, browser):
        try:
            check = CommonMethods.isElementPresent(self, browser, self.dialogBoxUnregisteredNo_id, "id")
#             check = checkDialogBoxDisplay(browser)
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
             
    def clickOnDeviceBackButton(self, browser):
        try:
            browser.back()
        except :
            logging.info("failed in clicking on device back button")
            logging.info("Failed in Method clickOnDeviceBackButton")
            pytest.fail("failed in clicking on device back button")
             
    def checkLoginLinkPresence(self, browser):
        try:
            check = CommonMethods.isElementPresent(self, browser, self.login_link_id, "id")
            if(check == False):
                logging.info('Login link is not displaying so app is closed')
            else:
                logging.info('Login link is present')
                logging.info("Failed in Method checkLoginLinkPresence")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException :
            logging.info("Failed Locator in Method checkLoginLinkPresence")
            pytest.fail("Failed Due to Locator in Login Page")
             
    def verifyMobileFieldAutofilled(self,browser):
        try:
            check = CommonMethods.verifyTextisPresent(browser,self.Dropdown_CountryCodeTxt_id)
            if check == True:
                logging.info('Mobiled number field is Auto filled')
            else:
                logging.info('Failed due to Mobile Number was not AutoFilled')
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed in login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifyMobileFieldAutofilled')
                     
        except :
            CommonMethods.exception(browser, featureFileName, 'verifyMobileFieldAutofilled')
             
    def verifyCountryCodeDrpDwn(self,browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.Dropdown_CountryCodeTxt_id, 3)
            if check == True:
                logging.info('Country Code Drop down is visible')
            else:
                logging.error('Failed due to Country code drop down is not present')
                CommonMethods.takeScreenShot(self,browser,featureFileName)
                pytest.fail("Failed in login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyMobileFieldAutofilled')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyMobileFieldAutofilled')
  
    def enterNumInBx(self,browser,data):
        try:
            check = CommonMethods.enterText(browser,data,self.txt_phoneNum_id)
            CommonMethods.hideKeyboard(browser)
            if check == True:
                logging.info(data+' entered successfully')
            else:
                logging.error('Failed in Enterin the text to Text Bx')
                CommonMethods.takeScreenShot(self,browser,featureFileName)
                pytest.fail("Failed in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'enterNumInBx')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'enterNumInBx')
            
    def verifyOTPscreen(self,browser):
        try:
            sleep(3)
            CommonMethods.wait_for_locator(browser, self.otp_TitleText, 15)
            check = CommonMethods.isElementPresent(browser, self.otp_TitleText)
            if check == True:
                logging.info('Verified OTP screen Successfully')
            else:
                logging.info('Failed in OTP Screen')
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyOTPscreen')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyOTPscreen')
             
    def tap_on_back_button(self,browser):
        try:
            CommonMethods.click_on_device_back_btn(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_back_button')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_back_button')
             
    def verifynotRegistered(self,browser):
        try:
            
            check = CommonMethods.wait_for_element_visible(browser, self.register_dialogMsg, 3)
            if check == True:
                logging.info('Verified Not Registered')
            else:
                logging.info('Failed in Finding the text in method verifynotRegistered ')
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed in "+os.path.basename(self.__class__.__name__))
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifynotRegistered')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifynotRegistered')
             
    def verifyRegisterBtn(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.register_dialog_btn, 3):
                logging.info('Verified Register Button')
            else:
                logging.info('Failed in Finding the text in method verifynotRegistered ')
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed in "+os.path.basename(self.__class__.__name__))
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyRegisterBtn')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyRegisterBtn')
             
    def verifyNotRegisterPageDismissed(self,browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.register_dialog_btn, 3)
            if check == False:
                logging.info('Phone number is not registered is dismissed')
            else:
                logging.error('Failed in closing Registered Page in method verifyNotRegisterPageDismissed ')
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed in "+os.path.basename(self.__class__.__name__))
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyNotRegisterPageDismissed')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyNotRegisterPageDismissed')
 
    def tapOnScreenOutsideDialogBx(self,browser):
        try:
            CommonMethods.run('adb shell input tap 100 100')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tapOnScreenOutsideDialogBx')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'tapOnScreenOutsideDialogBx')
             
    def verifyChooseYourCoursePage(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser,self.chooseCourse_Title_xpath)
            if check == True:
                pass
            else:
                logging.info('Failed in verifyChooseYourCoursePage method ')
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed in "+os.path.basename(self.__class__.__name__))
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyChooseYourCoursePage')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyChooseYourCoursePage')
             
    def tapOnLink(self,browser,text):
        try:
            check = CommonMethods.clickLink(browser,text)
            if check == True:
                pass
            else:
                logging.info(text+" Link not Present in the Screen")
                logging.info('Failed in Finding Link '+text)
                pytest.fail("Failed Due to Locator in Login Page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tapOnLink')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'tapOnLink')
             
    def verifyAppIsClosed(self,browser,text):
        try:
            check = CommonMethods.isAppActive(browser,text)
            if check == 3:
                pass
            else:
                logging.error(" App is Not Closed")
                pytest.fail("App is not closed")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyAppIsClosed')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyAppIsClosed')