#import numpy as np
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from utilities.common_methods import CommonMethods
from pages.android.homescreen import HomeScreen
from utilities.interrupt import *
from utilities.Image_methods import *

featureFileName = "Profile Screen"
CommonMethods = CommonMethods()
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


class ProfileScreen():
    back_arrow = (By.ID, "com.byjus.thelearningapp.premium:id/backNav")
    avtar_with_edit = (By.ID, "com.byjus.thelearningapp.premium:id/edit_relyt_avatar")
    profile_name = (By.ID, "com.byjus.thelearningapp.premium:id/tvUserName")
    my_badged_text = (By.ID, "com.byjus.thelearningapp.premium:id/tvBadgeTitle")
    badges_list = (By.ID, "com.byjus.thelearningapp.premium:id/rvBadgeList")

    profile_completion_text = (By.ID, "com.byjus.thelearningapp.premium:id/profile_completeness_text")
    profile_completion_progress = (By.ID, "com.byjus.thelearningapp.premium:id/progress_profile")
    profile_completion_percentage = (By.ID, "com.byjus.thelearningapp.premium:id/profile_completeness_percent")
    account_details_title = (By.ID, "com.byjus.thelearningapp.premium:id/account_details_title")
    acc_phone_image = (By.ID, "com.byjus.thelearningapp.premium:id/phone_image")
    acc_mobile_number = (By.ID, "com.byjus.thelearningapp.premium:id/mobile_number")
    acc_phn_no_edit = (By.ID, "com.byjus.thelearningapp.premium:id/phone_number_cta")
    change_no_phn_text_box = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    sign_out_image = (By.ID, "com.byjus.thelearningapp.premium:id/signout_image")
    sign_out_text = (By.ID, "com.byjus.thelearningapp.premium:id/signout")
    bday_image = (By.ID, "com.byjus.thelearningapp.premium:id/birthday_image")
    add_bday_text = (By.ID, "com.byjus.thelearningapp.premium:id/birthday")
    location_image = (By.ID, "com.byjus.thelearningapp.premium:id/location_image")
    location_text = (By.ID, "com.byjus.thelearningapp.premium:id/location")
    gender_image = (By.ID, "com.byjus.thelearningapp.premium:id/gender_image")
    gender_text = (By.ID, "com.byjus.thelearningapp.premium:id/gender")
    gender_value_selected = (By.ID, "com.byjus.thelearningapp.premium:id/top_text_view")
    mail_image = (By.ID, "com.byjus.thelearningapp.premium:id/mail_image")
    mail_text = (By.ID, "com.byjus.thelearningapp.premium:id/mail")
    name_image = (By.ID, "com.byjus.thelearningapp.premium:id/name_image")
    name_text = (By.ID, "com.byjus.thelearningapp.premium:id/name")
    profile_details = (By.ID, "com.byjus.thelearningapp.premium:id/profile_details")
    home_drawer_forward_arrow = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_imgvw_arrow_right")
    ham_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/roundedNavButton")
    profile_name_hamburger = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_txtvw_profile_name")

    avtar_label = (By.ID, "com.byjus.thelearningapp.premium:id/account_details_title")
    avtar_list = (By.ID, "com.byjus.thelearningapp.premium:id/avatar_list_view")
    avtar_images = (By.XPATH,
                    "//androidx.recyclerview.widget.RecyclerView/descendant::android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/avatar_image']")

    grade_selection = (By.ID, "com.byjus.thelearningapp.premium:id/tvGrade")
    course_bottom_sht_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/design_bottom_sheet")
    change_ur_grade_label = (By.ID, "com.byjus.thelearningapp.premium:id/account_details_title")
    all_courses_text = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/descendant::android.widget.TextView")
    grade_change_toast_msg = (By.ID, "com.byjus.thelearningapp.premium:id/snackbar_text")
    #     enrolled_courses = (By.XPATH,"//android.widget.RelativeLayout/descendant::android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/course_enrolled_view']")
    radio_btn = (By.XPATH, "//android.widget.RelativeLayout/descendant::android.widget.RadioButton")
    enrolled_courses = (By.XPATH,
                        "//android.widget.RelativeLayout/descendant::android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/course_enrolled_view']/preceding-sibling::android.widget.TextView")

    my_badges_see_all_icon = (By.ID, "com.byjus.thelearningapp.premium:id/badges_show_all_lyt")
    three_badges = (By.XPATH,
                    "//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/llBadgeContainerLyt']")
    earned_badge_in_badges_screen = (By.ID, "com.byjus.thelearningapp.premium:id/header_title_text")

    edit_profile_details = (By.ID, "com.byjus.thelearningapp.premium:id/profile_details_cta")
    edit_profile_text_in_edit_profile_cereen = (By.ID, "com.byjus.thelearningapp.premium:id/header_title_text")
    gender_male = (By.XPATH, "//android.widget.TextView[@text='Male']")
    bday_drop_down = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    bday_drop_down_set_btn = (By.ID, "com.byjus.thelearningapp.premium:id/primaryAction")
    profile_save_btn = (By.ID, "com.byjus.thelearningapp.premium:id/saveDetails")
    edit_name = (By.ID, "com.byjus.thelearningapp.premium:id/name")
    edit_mail = (By.ID, "com.byjus.thelearningapp.premium:id/mail")
    edit_city = (By.ID, "com.byjus.thelearningapp.premium:id/city")
    gender_list = (By.XPATH, "//android.widget.ListView")
    gender_list_elements = (
    By.XPATH, "//android.widget.ListView/descendant::android.widget.TextView[not(@text = 'Gender')]")

    calender_pop_text = (By.ID, "com.byjus.thelearningapp.premium:id/profile_datepicker_dialog_selected_date_textview")
    calender_date_picker = (By.ID, "com.byjus.thelearningapp.premium:id/profile_datepicker_dialog_datepicker")
    calender_year_change = (By.XPATH, "//android.widget.NumberPicker[@index=2]/android.widget.EditText")
    calender_cancel_btn = (By.ID, "com.byjus.thelearningapp.premium:id/secondaryAction")
    calender_previous_year = (By.XPATH, "//android.widget.NumberPicker[@index=2]/android.widget.Button[@index=0]")

    mob_no_edit_popup = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    mob_no_pop_up_msg = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_message")
    country_code_in_popup = (By.ID, "com.byjus.thelearningapp.premium:id/spnrCountry")
    phone_no_in_popup = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    submit_btn_in_popup = (By.ID, "com.byjus.thelearningapp.premium:id/primaryAction")
    cancel_btn_in_popup = (By.ID, "com.byjus.thelearningapp.premium:id/secondaryAction")
    invalid_mob_no_msg = (By.ID, "com.byjus.thelearningapp.premium:id/tvPhoneError")
    entered_same_no_toast = (By.XPATH, "//android.widget.Toast[@text='android.widget.Toast']")
    already_login_bottom_sheet = (By.ID, "com.byjus.thelearningapp.premium:id/design_bottom_sheet")
    OtpTxtBx_id = (By.ID, "com.byjus.thelearningapp.premium:id/etOTP")
    toast_profile_updation = (By.XPATH, "//android.widget.Toast[@text='Profile has been updated']")

    gps_msg = (By.ID, "com.google.android.gms:id/message")
    gps_no_thanks_btn = (By.ID, "android:id/button2")

    sign_out_bottom_sheet_dialog_text = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_title")
    sign_out_dialog_msg = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_message")
    sign_out_dialog_yes_btn = (By.ID, "com.byjus.thelearningapp.premium:id/primaryAction")
    sign_out_dialog_cancel_btn = (By.ID, "com.byjus.thelearningapp.premium:id/secondaryAction")
    connect_net_snake_bar = (By.ID, "com.byjus.thelearningapp.premium:id/snackbar_text")
    login_page_verify = (By.XPATH, "//android.widget.TextView[@text='Login']")
    no_internet_snake_bar = (By.ID, "com.byjus.thelearningapp.premium:id/snackbar_text")
    unable_to_connect_toast = (By.XPATH, "//android.widget.Toast[@text='Unable to connect to internet']")

    no_badges_text = (By.XPATH, "//android.widget.TextView[@text='You don't have any badges.']")
    earn_first_badge_btn = (By.ID, "com.byjus.thelearningapp.premium:id/btEarnFirstBadge")

    def __init__(self, driver):
        self.driver = driver
        self.home_screen = HomeScreen(driver)

    def verify_profile_screen(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.avtar_with_edit, 10)
            pro_screen = CommonMethods.isElementPresent(driver, self.avtar_with_edit)
            if pro_screen == True:
                logging.info('profile screen is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_profile_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_profile_screen')

    def verify_back_arrow(self, driver):
        try:
            back_arrow = CommonMethods.isElementPresent(driver, self.back_arrow)
            if back_arrow == True:
                logging.info('back arrow is displayed on top left corner')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_back_arrow')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_back_arrow')

    def verify_avtar_and_edit_opn(self, driver):
        try:
            avtar_edit_opn = CommonMethods.isElementPresent(driver, self.avtar_with_edit)
            if avtar_edit_opn == True:
                logging.info('profile image avtar and edit option are displayd')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_avtar_and_edit_opn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_avtar_and_edit_opn')

    def verify_profile_name(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.profile_name)
            if check == True:
                pro_name = CommonMethods.getTextOfElement(driver, self.profile_name)
            logging.info("profile name : " + pro_name + " is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_profile_name')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_profile_name')

    def verify_badges_and_badges_list(self, driver):
        try:
            badges = CommonMethods.isElementPresent(driver, self.my_badged_text)
            badges_list = CommonMethods.isElementPresent(driver, self.badges_list)
            if badges and badges_list == True:
                logging.info('profile image avtar and edit option are displayd')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_avtar_and_edit_opn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_avtar_and_edit_opn')

    def verify_course_selection(self, driver):
        try:
            grade_selection = CommonMethods.isElementPresent(driver, self.grade_selection)
            if grade_selection == True:
                logging.info("Course Selection drop down is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_course_selection')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_course_selection')

    def verify_profile_completion_and_percentage(self, driver):
        try:
            profile_completion_title = CommonMethods.isElementPresent(driver, self.profile_completion_text)
            profile_completion_progressio_bar = CommonMethods.isElementPresent(driver,
                                                                               self.profile_completion_progress)
            profile_completion_percentage = CommonMethods.isElementPresent(driver, self.profile_completion_percentage)
            if profile_completion_title and profile_completion_progressio_bar and profile_completion_percentage == True:
                percentages = CommonMethods.getTextOfElement(driver, self.profile_completion_percentage)
                logging.info("profile completion title with progression bar and percentages : " + str(
                    percentages) + " are displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_profile_completion_and_percentage')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_profile_completion_and_percentage')

    def verify_sign_out_and_image(self, driver):
        try:
            sign_out = CommonMethods.isElementPresent(driver, self.sign_out_text)
            sign_out_image = CommonMethods.isElementPresent(driver, self.sign_out_image)
            if sign_out and sign_out_image == True:
                logging.info('sign out title and image are displayd')
            else:
                self.scroll_down(driver)
                if sign_out and sign_out_image == True:
                    logging.info('sign out title and image are displayd')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_sign_out_and_image')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_sign_out_and_image')

    def click_on_home_drawr_forward_icon(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.home_drawer_forward_arrow, 10)
            CommonMethods.elementClick(driver, self.home_drawer_forward_arrow)
            logging.info('Successfully Tapped On home drawer forward arrow')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_home_drawr_forward_icon')

    def verify_phn_no_and_icon(self, driver):
        try:
            phn_no = CommonMethods.isElementPresent(driver, self.acc_mobile_number)
            phnno_icon = CommonMethods.isElementPresent(driver, self.acc_phone_image)
            if phn_no and phnno_icon == True:
                logging.info('phone number and phone icon are displayd')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_phn_no_and_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_phn_no_and_icon')

    def verify_phn_no_edit_icon(self, driver):
        try:
            phn_edit = CommonMethods.isElementPresent(driver, self.acc_phn_no_edit)
            if phn_edit == True:
                logging.info('Phone no edit icon is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_phn_no_edit_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_phn_no_edit_icon')

    def click_phn_no_edit(self, driver):
        try:
            phn_edit = CommonMethods.isElementPresent(driver, self.acc_phn_no_edit)
            if phn_edit == True:
                logging.info('Phone no edit icon is displayed')
                CommonMethods.elementClick(driver, self.acc_phn_no_edit)
                logging.info('Successfully Tapped phone edit icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_phn_no_edit')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_phn_no_edit')

    def verify_phn_no_and_text(self, driver):
        try:
            phn_no_box = CommonMethods.isElementPresent(driver, self.change_no_phn_text_box)
            if phn_no_box == True:
                phn_no_text = CommonMethods.getTextOfElement(driver, self.change_no_phn_text_box)
                check = phn_no_text.isdigit()
                if check == True:
                    logging.info('phone number field is accepting numeric only')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_phn_no_and_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_phn_no_and_icon')

    def navigate_to_profile_card(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.ham_btn_id, 5):
                CommonMethods.elementClick(driver, self.ham_btn_id)
                CommonMethods.wait_for_locator(driver, self.profile_name_hamburger, 5)
                CommonMethods.elementClick(driver, self.profile_name_hamburger)

            else:
                logging.info('profile_card Not Found')
                pytest.fail("Failed due to Hamburger Menu")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_profile_card')

        except:
            CommonMethods.exception(driver, featureFileName, 'hamburger_verify')

    def verify_profile_name_icon(self, driver):
        try:
            profile_name = CommonMethods.isElementPresent(driver, self.profile_name)
            profile_icon = CommonMethods.isElementPresent(driver, self.name_image)
            if profile_name and profile_icon == True:
                logging.info('profile name and image are displayed')
                profile_name_text = CommonMethods.getTextOfElement(driver, self.profile_name)
                logging.info("profile name pre filled value is : " + profile_name_text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_phn_no_and_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_phn_no_and_icon')

    def verify_email_icon_and_value(self, driver):
        try:
            email = CommonMethods.isElementPresent(driver, self.mail_text)
            email_icon = CommonMethods.isElementPresent(driver, self.mail_image)
            if email and email_icon == True:
                logging.info('mail and mail icon are displayed')
                email_value = CommonMethods.getTextOfElement(driver, self.mail_text)
                logging.info("email pre filled value is : " + email_value)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_email_icon_and_value')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_email_icon_and_value')

    def verify_loc_icon_and_value(self, driver):
        try:
            loc = CommonMethods.isElementPresent(driver, self.location_text)
            loc_icon = CommonMethods.isElementPresent(driver, self.location_image)
            if loc and loc_icon == True:
                logging.info('location and location icon are displayed')
                loc_value = CommonMethods.getTextOfElement(driver, self.location_text)
                logging.info("location pre filled value is : " + loc_value)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_loc_icon_and_value')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_loc_icon_and_value')

    def verify_gender_icon_text(self, driver, text):
        try:
            gender = CommonMethods.isElementPresent(driver, self.gender_text)
            gender_icon = CommonMethods.isElementPresent(driver, self.gender_image)
            if gender and gender_icon == True:
                logging.info('gender field and gender icon are displayed')
                gender_txt = CommonMethods.getTextOfElement(driver, self.gender_text)
                if text == gender_txt:
                    logging.info("text in gender field is : " + gender_txt)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_gender_icon_text')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_gender_icon_text')

    def verify_bday_icon_text(self, driver, text):
        try:
            bday = CommonMethods.isElementPresent(driver, self.add_bday_text)
            bday_icon = CommonMethods.isElementPresent(driver, self.bday_image)
            if bday and bday_icon == True:
                logging.info('birthday field and birthday icon are displayed')
                birthdy_txt = CommonMethods.getTextOfElement(driver, self.add_bday_text)
                if text == birthdy_txt:
                    logging.info("text in birthday field is : " + birthdy_txt)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_bday_icon_text')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_bday_icon_text')

    def scroll_down(self, driver):
        sleep(3)
        driver.swipe(300, 600, 300, 50)

    def select_offline_mode(self, driver):
        try:
            set_connection_type(driver, 'offline')
            logging.info("enabled offline mode")
        except:
            CommonMethods.exception(driver, featureFileName, 'select_offline_mode')

    #
    def click_on_profile_image(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.avtar_with_edit, 8)
            CommonMethods.elementClick(driver, self.avtar_with_edit)
            logging.info('Successfully Tapped On profile image')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_profile_image')

    def verify_avtar_pop_up(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.avtar_label, 2)
            avtar_pop_up = CommonMethods.isElementPresent(driver, self.avtar_label)
            if avtar_pop_up == True:
                logging.info('avtar pop up is displayed')
            elif avtar_pop_up == False:
                logging.info('avtar pop up is not displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_avtar_pop_up')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_avtar_pop_up')

    def verify_avtar_label_and_list_of_avtars(self, driver):
        try:
            avtar_label = CommonMethods.isElementPresent(driver, self.avtar_label)
            avtars = CommonMethods.isElementPresent(driver, self.avtar_list)
            if avtar_label and avtars == True:
                logging.info('avtars label is displayed')
                logging.info('list of avtars is displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_avtar_label_and_list_of_avtars')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_avtar_label_and_list_of_avtars')

    def select_pro_image_from_avtars(self, driver):
        try:
            avtars = CommonMethods.isElementPresent(driver, self.avtar_list)
            if avtars == True:
                images = CommonMethods.getElements(driver, self.avtar_images)
                images[1].click()
                logging.info('selected 2nd image from avtars list')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'select_pro_image_from_avtars')
        except:
            CommonMethods.exception(driver, featureFileName, 'select_pro_image_from_avtars')

    def verify_profile_image_if_selected(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.avtar_with_edit)
            if check == True:
                logging.info('avtar image is changed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_profile_image_if_selected')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_profile_image_if_selected')

    def verify_profile_image_if_not_selected(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.avtar_with_edit)
            if check == True:
                logging.info('avtar image is not changed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_profile_image_if_not_selected')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_profile_image_if_not_selected')

    def click_on_grade_selection_dropdown(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.grade_selection, 10)
            CommonMethods.elementClick(driver, self.grade_selection)
            logging.info('clicked on grade selection drop down')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_grade_selection_dropdown')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_grade_selection_dropdown')

    def verify_course_bottom_sheet_dialog(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.course_bottom_sht_dialog)
            if check == True:
                logging.info('course bottom sheet dialog is displayed')
            else:
                logging.info('course bottom sheet dialog is not displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_course_bottom_sheet_dialog')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_course_bottom_sheet_dialog')

    def all_courses(self, driver):
        try:
            dict_of_course = []
            for i in range(0, 2):
                course_list = CommonMethods.getElements(driver, self.all_courses_text)
                for i in course_list:
                    dict_of_course.append(i.text)
                driver.swipe(300, 600, 300, 100)
            logging.info(dict_of_course)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'all_courses')
        except:
            CommonMethods.exception(driver, featureFileName, 'all_courses')
        return dict_of_course

    def select_any_course(self, driver):
        try:
            course_list = self.all_courses(driver)
            driver.swipe(300, 400, 300, 850)
            logging.info("selecting course is : " + course_list[1])
            #             course_list[2]
            grade_xpath = (By.XPATH, "//android.widget.TextView[@text='" + course_list[1] + "']")
            CommonMethods.elementClick(driver, grade_xpath)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'select_any_course')
        except:
            CommonMethods.exception(driver, featureFileName, 'select_any_course')
        return course_list[2]

    def verify_grade_change_toast_msg(self, driver, text):
        try:
            CommonMethods.wait_for_element_visible(driver, self.grade_change_toast_msg, 5)
            check = CommonMethods.isElementPresent(driver, self.grade_change_toast_msg)
            if check == True:
                actual_text = CommonMethods.getTextOfElement(driver, self.grade_change_toast_msg)
                if actual_text == text:
                    logging.info("Displayed toast message is :" + actual_text)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_grade_change_toast_msg')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_grade_change_toast_msg')

    def selected_course_with_radio_btn(self, driver):
        try:
            text = self.select_any_course(driver)
            perticular_course_radio_btn = (By.XPATH,
                                           "//android.widget.RelativeLayout/descendant::android.widget.TextView[@text='" + text + "']/preceding-sibling::android.widget.RadioButton")
            radio_btn = CommonMethods.getElement(driver, perticular_course_radio_btn)
            check = radio_btn.is_enabled()
            if check == True:
                logging.info("course is selected")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'selected_course_with_radio_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'selected_course_with_radio_btn')

    def switch_to_8th_grade(self, driver):
        try:
            CommonMethods.click_on_device_back_btn(driver)
            self.home_screen.switch_grade(driver, '8th Grade')
            logging.info("switched to 8th grade")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'switch_to_8th_grade')
        except:
            CommonMethods.exception(driver, featureFileName, 'switch_to_8th_grade')

    def check_enrolled_courses(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.course_bottom_sht_dialog, 5)
            dict_of_enrolled_courses = []
            for i in range(0, 2):
                enrolled_courses_list = CommonMethods.getElements(driver, self.enrolled_courses)
                for i in enrolled_courses_list:
                    dict_of_enrolled_courses.append(i.text)
                driver.swipe(300, 600, 300, 100)
            logging.info(dict_of_enrolled_courses)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_enrolled_courses')
        except:
            CommonMethods.exception(driver, featureFileName, 'check_enrolled_courses')

    def check_course_radio_btn_enabled(self, driver):
        try:
            perticular_course_radio_btn = (By.XPATH,
                                           "//android.widget.RelativeLayout/descendant::android.widget.TextView[@text='8th Grade']/preceding-sibling::android.widget.RadioButton")
            radio_btn = CommonMethods.getElement(driver, perticular_course_radio_btn)
            check = radio_btn.is_enabled()
            if check == True:
                logging.info("for selected course radio button is enabled")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_course_radio_btn_enabled')
        except:
            CommonMethods.exception(driver, featureFileName, 'check_course_radio_btn_enabled')

    def verify_three_badges_and_see_all(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.my_badged_text, 10)
            check_badges = CommonMethods.getElements(driver, self.three_badges)

            if check_badges != None:
                logging.info("badges are present and total badges are " + str(len(check_badges)))
            check_see_all = CommonMethods.isElementPresent(driver, self.my_badges_see_all_icon)
            if check_see_all == True:
                logging.info("see all icon is present")
            else:
                logging.info("see all icon is not present because badges are less than 3")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_three_badges_and_see_all')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_three_badges_and_see_all')

    def verify_only_three_badges(self, driver):
        try:
            check_badges = CommonMethods.getElements(driver, self.three_badges)
            if check_badges != None:
                logging.info("badges are present and total badges are" + str(len(check_badges)))
            else:
                logging.info("no earned badges are present")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_three_badges_and_see_all')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_three_badges_and_see_all')

    def click_on_badge_see_all_icon(self, driver):
        try:
            see_all = CommonMethods.isElementPresent(driver, self.my_badges_see_all_icon)
            if see_all == True:
                CommonMethods.elementClick(driver, self.my_badges_see_all_icon)
                logging.info("successfully clicked on my badges see all icon")
            else:
                logging.info("see all icon is not present")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_badge_see_all_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_badge_see_all_icon')

    def verify_badges_screen(self, driver):
        try:
            see_all = CommonMethods.isElementPresent(driver, self.earned_badge_in_badges_screen)
            if see_all == True:
                logging.info("badges screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_badges_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_badges_screen')

    def verify_profile_completion_percentage(self, driver, text):
        try:
            profile_percent_ele = CommonMethods.isElementPresent(driver, self.profile_completion_percentage)
            text = str(text)
            if profile_percent_ele == True:
                profile_percent = CommonMethods.getTextOfElement(driver, self.profile_completion_percentage)
                profile_percent = str(profile_percent)
                if text == '70%' and profile_percent == text:
                    logging.info("default profile completion percentage is 70%")
                elif text == '100%' and profile_percent == text:
                    logging.info("profile completion percentage is 100%")
                elif text == '85%' and profile_percent == text:
                    logging.info("profile completion percentage is 85%")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_profile_completion_percentage')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_profile_completion_percentage')

    def update_gender(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.edit_profile_details, 5)
            edit_profile = CommonMethods.isElementPresent(driver, self.edit_profile_details)
            if edit_profile == True:
                CommonMethods.elementClick(driver, self.edit_profile_details)
                CommonMethods.wait_for_element_visible(driver, self.gender_text, 5)
                gender_opn = CommonMethods.isElementPresent(driver, self.gender_text)
                if gender_opn == True:
                    CommonMethods.elementClick(driver, self.gender_text)
                    CommonMethods.wait_for_element_visible(driver, self.gender_male, 5)
                    CommonMethods.elementClick(driver, self.gender_male)
                    CommonMethods.wait_for_element_visible(driver, self.profile_save_btn, 5)
                    CommonMethods.elementClick(driver, self.profile_save_btn)
                    logging.info("gender is updated")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'update_gender')
        except:
            CommonMethods.exception(driver, featureFileName, 'update_gender')

    def update_bday(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.edit_profile_details, 5)
            edit_profile = CommonMethods.isElementPresent(driver, self.edit_profile_details)
            if edit_profile == True:
                CommonMethods.elementClick(driver, self.edit_profile_details)
                CommonMethods.wait_for_element_visible(driver, self.add_bday_text, 5)
                bday_opn = CommonMethods.isElementPresent(driver, self.add_bday_text)
                if bday_opn == True:
                    CommonMethods.elementClick(driver, self.add_bday_text)
                    CommonMethods.wait_for_element_visible(driver, self.bday_drop_down, 5)
                    bday_opn_drop_down = CommonMethods.isElementPresent(driver, self.bday_drop_down)
                    if bday_opn_drop_down == True:
                        CommonMethods.wait_for_element_visible(driver, self.bday_drop_down_set_btn, 5)
                        CommonMethods.elementClick(driver, self.bday_drop_down_set_btn)
                        CommonMethods.wait_for_element_visible(driver, self.profile_save_btn, 5)
                        CommonMethods.elementClick(driver, self.profile_save_btn)
                    logging.info("Birthday is updated")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'update_bday')
        except:
            CommonMethods.exception(driver, featureFileName, 'update_bday')

    def verify_feilds_in_edit_phn_popup(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.mob_no_edit_popup, 5)
            check = CommonMethods.isElementPresent(driver, self.mob_no_edit_popup)
            if check == True:
                logging.info("Edit phone pop up is displayed")
                check_message = CommonMethods.isElementPresent(driver, self.mob_no_pop_up_msg)
                check_country_code = CommonMethods.isElementPresent(driver, self.country_code_in_popup)
                check_phone_no = CommonMethods.isElementPresent(driver, self.phone_no_in_popup)
                if check_message and check_country_code and check_phone_no == True:
                    message_text = CommonMethods.getTextOfElement(driver, self.mob_no_pop_up_msg)
                    logging.info("Text is : " + message_text)
                    logging.info("country code field is present")
                    logging.info("Phone number field is present")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_feilds_in_edit_phn_popup')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_feilds_in_edit_phn_popup')

    def verify_submit_btn_edit_phn_popup(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.mob_no_edit_popup, 5)
            check = CommonMethods.isElementPresent(driver, self.mob_no_edit_popup)
            if check == True:
                check_submit_btn = CommonMethods.isElementPresent(driver, self.submit_btn_in_popup)
                if check_submit_btn == True:
                    logging.info("Submit button is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_submit_btn_edit_phn_popup')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_submit_btn_edit_phn_popup')

    def remove_existing_mob_no(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.mob_no_edit_popup, 5)
            check = CommonMethods.isElementPresent(driver, self.mob_no_edit_popup)
            if check == True:
                check_phn_no = CommonMethods.isElementPresent(driver, self.phone_no_in_popup)
                if check_phn_no == True:
                    CommonMethods.enterText(driver, "", self.phone_no_in_popup)
                    logging.info("cleared data from phone number field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'remove_existing_mob_no')
        except:
            CommonMethods.exception(driver, featureFileName, 'remove_existing_mob_no')

    def click_submit_btn_edit_phn_popup(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.mob_no_edit_popup, 5)
            check = CommonMethods.isElementPresent(driver, self.mob_no_edit_popup)
            if check == True:
                check_submit_btn = CommonMethods.isElementPresent(driver, self.submit_btn_in_popup)
                if check_submit_btn == True:
                    CommonMethods.elementClick(driver, self.submit_btn_in_popup)
                    logging.info("Clicked on submit button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_submit_btn_edit_phn_popup')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_submit_btn_edit_phn_popup')

    def verify_empty_phn_no_error_msg(self, driver, text):
        try:
            CommonMethods.wait_for_element_visible(driver, self.mob_no_edit_popup, 5)
            check = CommonMethods.isElementPresent(driver, self.invalid_mob_no_msg)
            if check == True:
                text_msg = CommonMethods.getTextOfElement(driver, self.invalid_mob_no_msg)
                if text == text_msg:
                    logging.info("error message is : " + text_msg)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_empty_phn_no_error_msg')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_empty_phn_no_error_msg')

    def enter_invalid_mob_no(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.mob_no_edit_popup, 5)
            check = CommonMethods.isElementPresent(driver, self.mob_no_edit_popup)
            if check == True:
                check_phn_no = CommonMethods.isElementPresent(driver, self.phone_no_in_popup)
                if check_phn_no == True:
                    CommonMethods.enterText(driver, "", self.phone_no_in_popup)
                    CommonMethods.enterText(driver, "1234", self.phone_no_in_popup)
                    logging.info("1234 invalid mobile number is entered in phone number field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_invalid_mob_no')
        except:
            CommonMethods.exception(driver, featureFileName, 'enter_invalid_mob_no')

    def touch_outside_phn_popup(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.mob_no_edit_popup, 5)
            check = CommonMethods.isElementPresent(driver, self.avtar_with_edit)
            if check == False:
                while check == False:
                    click_on_back_button(driver)
                    check = CommonMethods.isElementPresent(driver, self.avtar_with_edit)
            logging.info("Successfully clicked, outside the phone pop up")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'touch_outside_phn_popup')
        except:
            CommonMethods.exception(driver, featureFileName, 'touch_outside_phn_popup')

    def verify_same_no_error_msg(self, driver, text):
        try:
            CommonMethods.wait_for_element_visible(driver, self.mob_no_edit_popup, 5)
            text_msg = CommonMethods.getTextOfElement(driver, self.entered_same_no_toast)
            if text_msg == text:
                logging.info("error message is : " + text_msg)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_same_no_error_msg')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_same_no_error_msg')

    def enter_new_mob_no(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.mob_no_edit_popup, 5)
            check = CommonMethods.isElementPresent(driver, self.mob_no_edit_popup)
            if check == True:
                check_phn_no = CommonMethods.isElementPresent(driver, self.phone_no_in_popup)
                if check_phn_no == True:
                    CommonMethods.enterText(driver, "1234567890", self.phone_no_in_popup)
                    logging.info("1234567890  mobile number is entered in phone number field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_new_mob_no')
        except:
            CommonMethods.exception(driver, featureFileName, 'enter_new_mob_no')

    def verify_otp_screen(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.OtpTxtBx_id, 5)
            if check == True:
                CommonMethods.isElementPresent(driver, self.OtpTxtBx_id)
                logging.info("otp screen is verified ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_otp_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_otp_screen')

    def click_on_cancel_btn_in_phn_popup(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.cancel_btn_in_popup, 5)
            check = CommonMethods.isElementPresent(driver, self.cancel_btn_in_popup)
            if check == True:
                CommonMethods.hideKeyboard(driver)
                CommonMethods.elementClick(driver, self.cancel_btn_in_popup)
                logging.info("Successfully clicked on cancel button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_cancel_btn_in_phn_popup')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_cancel_btn_in_phn_popup')

    def verify_gender_icon(self, driver):
        try:
            gender = CommonMethods.isElementPresent(driver, self.gender_text)
            gender_icon = CommonMethods.isElementPresent(driver, self.gender_image)
            if gender and gender_icon == True:
                logging.info('gender field and gender icon are displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_gender_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_gender_icon')

    def verify_bday_icon(self, driver):
        try:
            bday = CommonMethods.isElementPresent(driver, self.add_bday_text)
            bday_icon = CommonMethods.isElementPresent(driver, self.bday_image)
            if bday and bday_icon == True:
                logging.info('birthday field and birthday icon are displayed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_bday_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_bday_icon')

    def click_profile_edit_icon(self, driver):
        try:
            CommonMethods.scrollToElement(driver, "Profile Details")
            CommonMethods.wait_for_element_visible(driver, self.edit_profile_details, 10)
            profile_edit = CommonMethods.isElementPresent(driver, self.edit_profile_details)
            if profile_edit == True:
                CommonMethods.elementClick(driver, self.edit_profile_details)
                logging.info('Successfully Tapped on profile edit icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_profile_edit_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_profile_edit_icon')

    def verify_edit_profile_screen(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.edit_profile_text_in_edit_profile_cereen, 5)
            check = CommonMethods.isElementPresent(driver, self.edit_profile_text_in_edit_profile_cereen)
            if check == True:
                logging.info("edit profile screen is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_edit_profile_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_edit_profile_screen')

    def click_back_arrow(self, driver):
        try:
            profile_edit_back = CommonMethods.isElementPresent(driver, self.back_arrow)
            if profile_edit_back == True:
                CommonMethods.elementClick(driver, self.back_arrow)
                logging.info('Successfully Tapped on profile back arrow')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_back_arrow')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_back_arrow')

    def check_field_editable(self, driver):
        try:
            sleep(3)
            check = CommonMethods.isKeyBoardShown(driver)
            if check == True:
                logging.info('yes this field is editable and keyboard is shown ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_field_editable')
        except:
            CommonMethods.exception(driver, featureFileName, 'check_field_editable')

    def click_on_name_field(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.edit_name)
            if check == True:
                CommonMethods.elementClick(driver, self.edit_name)
                logging.info("Taped on name field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_name_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_name_field')

    def click_on_email_field(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.edit_mail)
            if check == True:
                CommonMethods.elementClick(driver, self.edit_mail)
                logging.info("Taped on email field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_email_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_email_field')

    def click_on_location_field(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.edit_city)
            if check == True:
                CommonMethods.elementClick(driver, self.edit_city)
                logging.info("Taped on location field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_location_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_location_field')

    def click_on_gender_field(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.gender_text)
            if check == True:
                CommonMethods.elementClick(driver, self.gender_text)
                logging.info("Taped on gender field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_gender_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_gender_field')

    def verify_gender_drop_down(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.gender_list, 5)
            check = CommonMethods.isElementPresent(driver, self.gender_list)
            if check == True:
                logging.info("Gender list is displayed")
                gender_values = CommonMethods.getElements(driver, self.gender_list_elements)
                for i in gender_values:
                    logging.info(i.text)
                    if i.text == 'Female':
                        i.click()
                        logging.info("Female is selected from the gender list")
                    CommonMethods.wait_for_element_visible(driver, self.gender_value_selected, 5)
                    get_gender_value = CommonMethods.getTextOfElement(driver, self.gender_value_selected)
                    logging.info(get_gender_value)
                    if get_gender_value == 'Female':
                        logging.info("able to select one value from gender drop down")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_gender_drop_down')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_gender_drop_down')

    def tap_on_location_icon1(self, driver):
        try:
            if CommonMethods.isElementPresent(driver, self.edit_city):
                element = CommonMethods.getElement(driver, self.edit_city)
                loc = element.rect
                x = loc['x']
                y = loc['y']
                height = loc['height']
                width = loc['width']
                x2 = (x + width) - 5
                y2 = (y + height) - 5
                CommonMethods.run('adb shell input tap {} {}'.format(x2, y2))
                logging.info("successfully clicked on location auto detector")
            else:
                logging.error('Failed to tap on location icon')
                pytest.fail('Failed to tap on location icon')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_location_icon1')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_location_icon1')

    def get_location(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.edit_city)
            if check == True:
                text = CommonMethods.getTextOfElement(driver, self.edit_city)
                logging.info("current location is " + text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'get_location')
        except:
            CommonMethods.exception(driver, featureFileName, 'get_location')

    def handle_gps_location_popup(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.gps_msg)
            if check == True:
                logging.info("Turn on GPS popup is displayed")
                CommonMethods.elementClick(driver, self.gps_no_thanks_btn)
                logging.info("successfully clicked on GPS popup's no thanks button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'handle_gps_location_popup')
        except:
            CommonMethods.exception(driver, featureFileName, 'handle_gps_location_popup')

    def enter_future_date_in_bday_field(self, driver, future_year):
        try:
            bday_opn = CommonMethods.isElementPresent(driver, self.add_bday_text)
            if bday_opn == True:
                CommonMethods.elementClick(driver, self.add_bday_text)
                CommonMethods.wait_for_element_visible(driver, self.bday_drop_down, 5)
                bday_opn_drop_down = CommonMethods.isElementPresent(driver, self.bday_drop_down)
                if bday_opn_drop_down == True:
                    CommonMethods.wait_for_element_visible(driver, self.calender_year_change, 5)
                    CommonMethods.elementClick(driver, self.calender_year_change)
                    logging.info("user is entering future year = " + future_year)
                    CommonMethods.enterText(driver, future_year, self.calender_year_change)
                    calender_header_text = CommonMethods.getTextOfElement(driver, self.calender_pop_text)
                    CommonMethods.elementClick(driver, self.bday_drop_down_set_btn)
                    date = CommonMethods.getTextOfElement(driver, self.add_bday_text)
                    logging.info(date)
                return calender_header_text
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_future_date_in_bday_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'enter_future_date_in_bday_field')

    def get_bday_date(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.add_bday_text)
            if check == True:
                txt = CommonMethods.getTextOfElement(driver, self.add_bday_text)
                logging.info(txt)
                return txt
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'get_bday_date')
        except:
            CommonMethods.exception(driver, featureFileName, 'get_bday_date')

    def verify_updated_bday_date_in_calender(self, driver):
        try:
            bday_opn = CommonMethods.isElementPresent(driver, self.add_bday_text)
            if bday_opn == True:
                CommonMethods.elementClick(driver, self.add_bday_text)
                CommonMethods.wait_for_element_visible(driver, self.bday_drop_down, 5)
                bday_opn_drop_down = CommonMethods.isElementPresent(driver, self.bday_drop_down)
                if bday_opn_drop_down == True:
                    previous_text = str(CommonMethods.getTextOfElement(driver, self.calender_pop_text))
                    CommonMethods.wait_for_element_visible(driver, self.calender_previous_year, 5)
                    CommonMethods.elementClick(driver, self.calender_previous_year)
                    changed_text = str(CommonMethods.getTextOfElement(driver, self.calender_pop_text))
                    CommonMethods.elementClick(driver, self.bday_drop_down_set_btn)
                    logging.info(previous_text)
                    logging.info(changed_text)
                    if previous_text != changed_text:
                        logging.info("Birthday date is updated ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_updated_bday_date')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_updated_bday_date')

    def verify_calender_popup(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.add_bday_text, 5)
            check = CommonMethods.isElementPresent(driver, self.add_bday_text)
            if check == True:
                CommonMethods.elementClick(driver, self.add_bday_text)
                CommonMethods.wait_for_element_visible(driver, self.bday_drop_down, 5)
                bday_opn_drop_down = CommonMethods.isElementPresent(driver, self.bday_drop_down)
                if bday_opn_drop_down == True:
                    logging.info("Birthday calender pop up is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_calender_popup')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_calender_popup')

    def click_on_birthday_field(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.add_bday_text)
            if check == True:
                CommonMethods.elementClick(driver, self.add_bday_text)
                logging.info("Taped on birthday field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_birthday_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_birthday_field')

    def verify_gender_edit_field(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.gender_text)
            if check == True:
                logging.info("Gender field is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_gender_edit_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_gender_edit_field')

    def verify_birthday_edit_field(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.add_bday_text)
            if check == True:
                logging.info("Birthday field is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_birthday_edit_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_birthday_edit_field')

    def verify_save_button(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.profile_save_btn)
            if check == True:
                logging.info("save button is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_save_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_save_button')

    def verify_edit_profile_text(self, driver, text):
        try:
            check = CommonMethods.isElementPresent(driver, self.edit_profile_text_in_edit_profile_cereen)
            if check == True:
                get_edit_text = CommonMethods.getTextOfElement(driver, self.edit_profile_text_in_edit_profile_cereen)
                if get_edit_text == text:
                    logging.info("edit profile text is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_edit_profile_text')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_edit_profile_text')

    def verify_edit_name_field_and_icon(self, driver):
        try:
            check1 = CommonMethods.isElementPresent(driver, self.name_image)
            check2 = CommonMethods.isElementPresent(driver, self.name_text)
            if check1 and check2 == True:
                logging.info("edit profile name and icon are displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_edit_name_field_and_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_edit_name_field_and_icon')

    def verify_location_field_and_icon(self, driver):
        try:
            check1 = CommonMethods.isElementPresent(driver, self.edit_city)
            check2 = CommonMethods.isElementPresent(driver, self.location_image)
            if check1 and check2 == True:
                logging.info("edit location field and icon are displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_location_field_and_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_location_field_and_icon')

    def clear_name_field(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.name_text, 5)
            name_field = CommonMethods.getElement(driver, self.name_text)
            name_field.clear()
            logging.info("cleared the name field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'clear_name_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'clear_name_field')

    def click_save_button(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.profile_save_btn)
            if check == True:
                CommonMethods.elementClick(driver, self.profile_save_btn)
                logging.info("clicked on save button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_save_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_save_button')

    def hide_keyboard(self, driver):
        try:
            check = CommonMethods.isKeyBoardShown(driver)
            if check == True:
                CommonMethods.hideKeyboard(driver)
                logging.info("hide displayed keyboard")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'hide_keyboard')
        except:
            CommonMethods.exception(driver, featureFileName, 'hide_keyboard')

    def verify_empty_field_error(self, driver, text):
        # sleep(2)
        # imagefilepath = screenshot(driver)
        # found_txt = get_text_from_image(driver,imagefilepath,text)
        # if found_txt == text:
        #     logging.info("error text is : "+text)
        try:
            sleep(4)
            imagefilepath = screenshot(driver)
            found_txt = get_text_from_image(driver, imagefilepath, text)
            if found_txt == text:
                logging.info("error text is : " + text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_empty_field_error')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_empty_field_error')

    def clear_email_field(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.edit_mail, 5)
            email_field = CommonMethods.getElement(driver, self.edit_mail)
            email_field.clear()
            logging.info("cleared the email field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'clear_email_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'clear_email_field')

    def clear_location_field(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.edit_city, 5)
            city_field = CommonMethods.getElement(driver, self.edit_city)
            city_field.clear()
            logging.info("cleared the email field")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'clear_location_field')
        except:
            CommonMethods.exception(driver, featureFileName, 'clear_location_field')

    def verify_all_edit_profile_fields(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.edit_profile_text_in_edit_profile_cereen, 5)
            check_name = CommonMethods.isElementPresent(driver, self.name_text)
            check_mail = CommonMethods.isElementPresent(driver, self.mail_text)
            check_gender = CommonMethods.isElementPresent(driver, self.gender_text)
            check_city = CommonMethods.isElementPresent(driver, self.edit_city)
            check_bday = CommonMethods.isElementPresent(driver, self.add_bday_text)
            check_all = (check_name and check_mail and check_gender and check_city and check_bday)
            if check_all == True:
                name_value = CommonMethods.getTextOfElement(driver, self.name_text)
                mail_value = CommonMethods.getTextOfElement(driver, self.mail_text)
                gender_value = CommonMethods.getTextOfElement(driver, self.gender_text)
                city_value = CommonMethods.getTextOfElement(driver, self.edit_city)
                bday_value = CommonMethods.getTextOfElement(driver, self.add_bday_text)
                if (name_value and mail_value and gender_value and city_value and bday_value) != None:
                    logging.info("all fields are filled")
        #                     CommonMethods.elementClick(driver, self.profile_save_btn)
        #                     logging.info("successfully clicked on Save button")
        #                     check_toast = CommonMethods.isElementPresent(driver, self.toast_profile_updation)
        #                     if check_toast == True:
        #                         logging.info("toast message is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_all_edit_profile_fields')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_all_edit_profile_fields')

    def verify_profile_updation_toast(self, driver):
        try:
            check_toast = CommonMethods.isElementPresent(driver, self.toast_profile_updation)
            if check_toast == True:
                logging.info("toast message is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_profile_updation_toast')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_profile_updation_toast')

    def click_on_sign_out(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.sign_out_text, 10)
            check_signout = CommonMethods.isElementPresent(driver, self.sign_out_text)
            if check_signout == True:
                CommonMethods.elementClick(driver, self.sign_out_text)
                logging.info("Clicked on sign out")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_sign_out')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_sign_out')

    def verify_sign_out_bottom_sheet(self, driver):
        try:
            check_signout = CommonMethods.isElementPresent(driver, self.sign_out_bottom_sheet_dialog_text)
            if check_signout == True:
                logging.info("sign out bottom sheet dialog is displayed")
            elif check_signout == False:
                logging.info("sign out bottom sheet dialog is dismissed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_sign_out_bottom_sheet')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_sign_out_bottom_sheet')

    def verify_sign_out_text_in_dialog(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.sign_out_bottom_sheet_dialog_text, 5)
            check_signout = CommonMethods.isElementPresent(driver, self.sign_out_bottom_sheet_dialog_text)
            if check_signout == True:
                logging.info("sign out text is present in sign out bottom sheet dialog")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_sign_out_text_in_dialog')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_sign_out_text_in_dialog')

    def verify_sign_out_dialog_msg(self, driver, text):
        try:
            check_signout = CommonMethods.isElementPresent(driver, self.sign_out_dialog_msg)
            if check_signout == True:
                dialog_text = CommonMethods.getTextOfElement(driver, self.sign_out_dialog_msg)
                logging.info(dialog_text)
                if dialog_text == text:
                    logging.info("sign out bottom sheet dialog message is : " + dialog_text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_sign_out_dialog_msg')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_sign_out_dialog_msg')

    def verify_sign_out_dialog_yes_and_cancel_btn(self, driver):
        try:
            check_yes = CommonMethods.isElementPresent(driver, self.sign_out_dialog_yes_btn)
            check_cancel = CommonMethods.isElementPresent(driver, self.sign_out_dialog_cancel_btn)
            if check_yes and check_cancel == True:
                logging.info("Yes ans Cancel buttons are present in sign out bottom sheet dialog")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_sign_out_dialog_yes_and_cancel_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_sign_out_dialog_yes_and_cancel_btn')

    def click_on_sign_out_dialog_yes_btn(self, driver):
        try:
            check_yes = CommonMethods.isElementPresent(driver, self.sign_out_dialog_yes_btn)
            if check_yes == True:
                CommonMethods.elementClick(driver, self.sign_out_dialog_yes_btn)
                logging.info("clicked on Yes button in sign out bottom sheet dialog")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_sign_out_dialog_yes_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_sign_out_dialog_yes_btn')

    def verify_login_page(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.login_page_verify)
            if check == True:
                logging.info("Login Page is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_login_page')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_login_page')

    def click_on_sign_out_dialog_cancel_btn(self, driver):
        try:
            check_cancel = CommonMethods.isElementPresent(driver, self.sign_out_dialog_cancel_btn)
            if check_cancel == True:
                CommonMethods.elementClick(driver, self.sign_out_dialog_cancel_btn)
                logging.info("clicked on Cancel button in sign out bottom sheet dialog")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_sign_out_dialog_cancel_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_sign_out_dialog_cancel_btn')

    def verify_sign_out_no_internet(self, driver, text):
        try:
            CommonMethods.wait_for_element_visible(driver, self.no_internet_snake_bar, 5)
            no_internet_text = CommonMethods.getTextOfElement(driver, self.no_internet_snake_bar)
            if no_internet_text == text:
                logging.info("no internet bar is displayed and text is : " + no_internet_text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_sign_out_no_internet')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_sign_out_no_internet')

    def verify_no_badges_text(self, driver, text):
        try:
            CommonMethods.wait_for_element_visible(driver, self.no_badges_text, 5)
            no_badge = CommonMethods.isElementPresent(driver, self.sign_out_dialog_cancel_btn)
            if no_badge == True:
                no_badges_text = CommonMethods.getTextOfElement(driver, self.no_internet_snake_bar)
                if no_badges_text == text:
                    logging.info("no badges is displayed and text is : " + no_badges_text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_no_badges_text')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_no_badges_text')

    def verify_earn_badge_btn(self, driver):
        try:
            earn_b = CommonMethods.isElementPresent(driver, self.earn_first_badge_btn)
            if earn_b == True:
                logging.info("Earn your first badge button is displayed")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_earn_badge_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_earn_badge_btn')

    def verify_unable_to_connect_toast(self, driver, text):
        try:
            CommonMethods.wait_for_element_visible(driver, self.unable_to_connect_toast, 5)
            no_internet_text = CommonMethods.getTextOfElement(driver, self.unable_to_connect_toast)
            logging.info(no_internet_text)
            logging.info(text)
            if no_internet_text == text:
                logging.info("no internet toast is displayed and text is : " + no_internet_text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_unable_to_connect_toast')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_unable_to_connect_toast')
