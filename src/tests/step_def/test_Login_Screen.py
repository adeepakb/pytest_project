from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.loginpage import LoginPage
from Utilities.BasePage import BaseClass
from Utilities.generic_methods import GenericMethods

browser = fixture = 'browser'
baseClass = BaseClass()
login = LoginPage()

"""storing the feature file name"""
featureFileName = "Login Screen"

"""configuring the Logging Files"""
baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given('Launch the app online')
def launchApp(browser):
    pass


@when('Navigate to Login screen')
def NavigateToLoginPage_when(browser):
#     login.navigateToLoginPage(browser)
    GenericMethods.navigate_to_login_page(browser, '8th')


@then(parsers.parse('Verify the "{text}" text'))
def verifyTextInScreen(browser,text):
    login.verifyTextPresent(browser,text)
    

@then("Mobile Number field with auto filled country code")
def textBxAutoFilled(browser):
    login.verifyMobileFieldAutofilled(browser)
        
        
@then(parsers.parse('Verify the "{text}" Button'))
def verifyButtonInScreen(browser,text):
    login.verifyButtonPresent(browser,text)


@then(parsers.parse('Verify the "{text}" Link'))
def verifyListInScreen(browser,text):
    login.verifyLinkPresent(browser,text)
     
     
@given("Launch the app online and Navigate to Login screen")
def NavigateToLoginPage(browser): 
    login.allowPopUp(browser)
    login.navigateToLoginPage(browser)

    
@when("User taps on Country Code menu")
def tapOnCountryCode(browser): 
    login.tapOnCountryCode(browser)
    
    
@then("Verify Country Code should be a drop down menu")
def verify_code_drp_dwn(browser):
    login.verifyCountryCodeDrpDwn(browser)
    
    
@when('select any <countryCode> from the drop down')
def selectTheCountry(browser,countryCode): 
    login.selectTheCountryCode(browser,countryCode)


@then('Verify selected <code> should be shown in country code field')
def verifyCountryCode(browser,code):
    login.verifyCountryCode(browser,code)
    

@when('User taps on Mobile Number field')
def tap_on_mobile_field(browser): 
    login.tapsOnMobileNumberField(browser)
    
    
@then("Verify numeric keypad gets activated")
def verifynumericKeypad(browser):
    login.verifynumericKeypadActive(browser)
    
    
@then("should accept only Numeric values")
def verifyAcceptsNumeric(browser):
    login.verifyAcceptsNumericOnly(browser)
    
    
@when('Enters <DigitsBelow7> Mobile Number field')
def enter_text_7digit(browser,DigitsBelow7): 
    login.enterNumInBx(browser,DigitsBelow7)


@when("taps on Next Button")   
@then("taps on Next Button")
def tapsOnLoginBtn(browser):
    login.tapOnNextBtn(browser) 


@then(parsers.parse('Verify error message "{error_msg}" is displayed below mobile number field'))
def verifyErrormsg(browser, error_msg):
    login.verifyErrorMsg(browser, error_msg)
    

@when('enters <DigitsAbove15> in Mobile Number field')
def enter_text_15digit(browser,DigitsAbove15): 
    login.enterNumInBx(browser,DigitsAbove15)


@when('User enters valid <MobileNumber>')
def enter_valid_num(browser, MobileNumber): 
    login.enterNumInBx(browser, MobileNumber)


@then('User should navigate to LoginOTPVerificationScreen')
def verify_otp_screen(browser):
    login.verifyOTPscreen(browser)   
    

@then('Verify App should be closed')
def VerifyAppClosed(browser):
    login.VerifyAppClosed(browser)
    
    
@then('Verify the "This phone number is not registered. Please register to continue" text')
def verifynotRegistered(browser):
    login.verifynotRegistered(browser)
    
    
@then(parsers.parse('Verify "{Register}" button'))
def verifyRegisterBtn(browser):
    login.verifyRegisterBtn(browser)  
    

@then('Verify "Phone number is not registered" bottom sheet dialog dismissed')
def verifynotRegisterPage(browser):
    login.verifyNotRegisterPageDismissed(browser)
    

@then('tap outside the dialog')
def tapOnScreen(browser):
    login.tapOnScreenOutsideDialogBx(browser)
    
#Scenario
@then('tap on Register button')
def tapsOnRegisterBtn(browser):
    login.clickOnRegisterBtnInDialogBox(browser)
    
@then('Verify user is redirected to "ChooseYourCourse" screen')
def verifyChooseYourCoursePage(browser):
    login.verifyChooseYourCoursePage(browser)
    

@when(parsers.parse('tap on "{text}" Link'))
def tapOnLink(browser,text):
    login.tapOnLink(browser,text)   


@when('User enters <UnregisteredNnumber> in Mobile Number Field')
def enterUnregistedNum(browser,UnregisteredNnumber): 
    login.enterNumInBx(browser,UnregisteredNnumber)


@given('User enters <UnregisteredNnumber> in Mobile Number Field')
def enter_unregisted_num(browser,UnregisteredNnumber): 
    login.enterNumInBx(browser,UnregisteredNnumber)
 
 
@when('taps on Device back button')      
@then('taps on Device back button')
def tapOnDeviceBckBtn(browser):
    login.tap_on_back_button(browser)
    
    
@then('Verify <App> should be closed')
def verifyAppIsClosed(browser,App):
    login.verifyAppIsClosed(browser,App)