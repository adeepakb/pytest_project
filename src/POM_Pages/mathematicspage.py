
from appium import webdriver
from time import sleep



class MathematicsPage():
    def __init__(self, driver):
        
        self.first_video = "//android.widget.TextView[@text='Numbers and Its Properties' and @index = 1]"
        self.library_toggle_btn = "com.byjus.thelearningapp:id/optionalNav"
        self.page_header="com.byjus.thelearningapp:id/header_subtitle_text"
        
    def clickOnTopic(self,browser):
        browser.find_element_by_xpath(self.first_video).click()
        
        
    
    def clickOnToggleButton(self,browser):
        browser.find_element_by_id(self.library_toggle_btn).click()
    
    def scrollUpVideos(self,browser):
        pass
    def scrollDownVideos(self,browser):
        pass
    def clickOnVideoCard(self,browser):
        browser.find_element_by_xpath(self.first_video).click()
        
    def findText(self,browser):
        t=browser.find_element_by_id(self.page_header)
        t.gettext()
        print(t)
