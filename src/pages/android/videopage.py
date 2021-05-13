import logging
import pytest
from time import sleep
from constants.load_json import *
from utilities.common_methods import CommonMethods
from constants.constants import CONFIG_PATH, Login_Credentials
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from io import BytesIO
import random
from utilities.generic_methods import GenericMethods

f = open("../../test_data/featureFileName.txt", "r")
featureFileName = f.read()

CommonMethods = CommonMethods()
data_file = CONFIG_PATH
video_name = None


class VideoPage:
    videoProgressTimeBfr = None
    videoProgressTimeAfter = None
    chapter_name = None
    auto_play_switch_color = None
    next_video_title = None
    chapter_name_video_list = None

    subject_rgb_lst = set()
    chapter_rgb_lst = set()

    current_playing_video_name = None
    video_start_time = None
    video_start_time_portrait = None
    video_start_time_landscape = None
    video_sub_title_name = None
    title_of_next_video = None

    def __init__(self, driver):
        self.driver = driver

    register_page_email_txt_bx = (By.ID, "com.byjus.thelearningapp.premium:id/etEmail")
    register_page_register_btn = (By.ID, "com.byjus.thelearningapp.premium:id/btnRegister")
    register_page_name_field = (By.ID, "com.byjus.thelearningapp.premium:id/etName")
    login_register_btn = (By.ID, "com.byjus.thelearningapp.premium:id/primaryAction")
    registration_name_field = (By.ID, "com.byjus.thelearningapp.premium:id/etName")
    multiple_accounts_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_linearlayout")
    user_profile_name = (By.ID, "com.byjus.thelearningapp.premium:id/tv_profile_name")
    profile_select_radio_button = (By.ID, "com.byjus.thelearningapp.premium:id/profile_select_radio_button")
    continue_button = (By.ID, "com.byjus.thelearningapp.premium:id/tv_submit")
    register_btn = (By.ID, "com.byjus.thelearningapp.premium:id/btnRegister")
    chooseCourse_Title_xpath = (By.XPATH, "//android.widget.TextView[@text='your course']")
    maths_subject = (By.XPATH, "//android.widget.TextView[@text='Mathematics']")
    toast_msg = (By.XPATH, "//android.widget.Toast")
    practice_continue_btn = (By.ID, "com.byjus.thelearningapp.premium:id/primaryAction")
    practice_submit_btn = (By.ID, "com.byjus.thelearningapp.premium:id/action_morph_btn")
    practice_2nd_answer = (
    By.XPATH, "//android.widget.ListView//android.view.View[@index=1]//android.view.View[@index=1]")
    practice_start_practice_btn = (By.ID, "com.byjus.thelearningapp.premium:id/tvStartPractice")
    loginPageVerify_id = (By.XPATH, "//android.widget.Button[@text='Login']")
    welcome_button = (By.ID, "com.byjus.thelearningapp.premium:id/welcomeButton")
    homescreen_corana_dialog_ok_btn = (By.XPATH, "//android.widget.TextView[@text = 'OK']")
    homescreen_corana_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    profile_header_id = (By.ID, "com.byjus.thelearningapp.premium:id/llHeaderTextParent")
    profile_name = (By.ID, "com.byjus.thelearningapp.premium:id/header_title_text")
    profile_mob_num = (By.ID, "com.byjus.thelearningapp.premium:id/mobile_number")
    back_button_id = (By.ID, "com.byjus.thelearningapp.premium:id/backNav")
    user_name_profile_page = (By.ID, "com.byjus.thelearningapp.premium:id/tvUserName")
    profile_name_hamburger = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_imgvw_arrow_right")
    account_details_title = (By.ID, "com.byjus.thelearningapp.premium:id/account_details_title")
    phone_num = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    country_Code = (By.ID, "com.byjus.thelearningapp.premium:id/spnrCountry")
    video = (By.XPATH, "//android.widget.ImageView[@instance='2']")
    Btn_test = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_list_item_test_txtvw")
    Btn_practice = (By.ID, "com.byjus.thelearningapp.premium:id/practice_mode_bottom_txtvw")
    Btn_play_pause = (By.XPATH, "//android.widget.ImageView[@instance='3']")
    loginBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/btnLogin")
    OtpTxtBx_id = (By.ID, "com.byjus.thelearningapp.premium:id/etOTP")
    librayBtn_id = (By.XPATH, "//android.widget.Button[@text='Library']")
    personalizeScreen_xpath = (By.XPATH, "//android.widget.Button[@text='Personalised']")
    first_videoLnk_xpath = (By.XPATH,
                            "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group' and @index=1]/androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_videos_lstvw']/android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_cardview' and @index = 0]")
    video_frame_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_subtitles")
    chapter_videoLnk_elements = (By.XPATH,
                                 "//android.widget.ImageView[@resource-id = 'com.byjus.thelearningapp.premium:id/chapter_video_thumbnail_imgvw']")
    tab_chapter_videoLnk_elements = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_view_group")
    video_pause_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_pause")
    video_play_btn = (By.ID, "com.byjus.thelearningapp.premium:id/exo_play")
    video_play_next_btn = (By.ID, "com.byjus.thelearningapp.premium:id/ivNext")
    video_play_previous_btn = (By.ID, "com.byjus.thelearningapp.premium:id/ivPrevious")
    videoPlayingNow_xpath = (By.XPATH,
                             "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']/android.widget.LinearLayout[@index=0]//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
    google_termsBtn_id = (By.ID, "com.android.chrome:id/terms_accept")
    nextBtn_id = (By.ID, "com.android.chrome:id/next_button")
    negativeBtn_id = (By.ID, "com.android.chrome:id/negative_button")
    progressTime_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_position")
    remaingTime_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_duration")
    ten_sec_fwd_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_ffwd")
    ten_sec_bkwd_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_rew")
    byjusAppPackage = "com.byjus.thelearningapp.premium"
    skipBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/buttonSkip")
    overlay_skip_btn = (By.ID, "com.byjus.thelearningapp.premium:id/overlay_skip")
    video1stLink_xpath = (By.XPATH,
                          "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']/android.widget.LinearLayout[@index=0]")
    allow_btn_id = (By.XPATH, "//*[contains(@resource-id, 'permission_allow_button')]")
    none_of_the_above_id = (By.ID, "com.google.android.gms:id/cancel")
    select_8th_grade = (By.XPATH, "//android.widget.Button[@text='8th']")
    video_time_remaining = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv")
    video_test_lnk = (By.XPATH, "//android.widget.TextView[@text = 'Test']")
    video_practice_lnk = (By.XPATH, "//android.widget.TextView[@text = 'Practice']")
    video_comming_soon_dialog_popup = (By.XPATH,
                                       "//android.widget.TextView[@text='Coming Soon' and @resource-id = 'com.byjus.thelearningapp.premium:id/dialog_title']")
    chapter_name_text = (By.XPATH,
                         "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_list_view']//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/header_title_text']")

    #    subject page
    subject_title_id = (By.ID, "com.byjus.thelearningapp.premium:id/title")

    #     Video Player Screen Locators
    screen_orientation_id = (By.ID, "com.byjus.thelearningapp.premium:id/orientation_toggle")
    video_backBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/back")
    videoSpeed_up_dwnIcon_id = (By.ID, "com.byjus.thelearningapp.premium:id/playback_speed")
    video_subtitileIcon_id = (By.ID, "com.byjus.thelearningapp.premium:id/subtitle_tracks")
    video_mutipleAudioTracks_id = (By.ID, "com.byjus.thelearningapp.premium:id/audio_tracks")
    video_settingIcon_id = (By.ID, "com.byjus.thelearningapp.premium:id/settings")
    video_progressBar_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_progress")
    videoPauseBtn_id2 = "com.byjus.thelearningapp.premium:id/exo_pause"
    video_1stLnk = (By.XPATH,
                    "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']/android.widget.LinearLayout[@index=0]//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
    video_video_frame_id = (By.ID, "com.byjus.thelearningapp.premium:id/videoViewLayout")
    video_auto_play_buttom_sheet = (By.ID, "com.byjus.thelearningapp.premium:id/design_bottom_sheet")
    video_name_list_elements = (By.ID, "com.byjus.thelearningapp.premium:id/videoName")
    video_grades_elements = (By.ID, "com.byjus.thelearningapp.premium:id/course_view_group")
    ham_bookmark = (By.XPATH, ("//android.widget.TextView[@text='Bookmarks']"))
    video_title_on_player = (By.ID, "com.byjus.thelearningapp.premium:id/tvVideoName")
    practice_back_arrow_btn = (By.ID, "com.byjus.thelearningapp.premium:id/roundedNavButton")

    #   VideoPlayer List Screen
    video_1st_list_lnk_text = (By.XPATH,
                               "//androidx.recyclerview.widget.RecyclerView//android.widget.LinearLayout[@index = 0]//android.widget.TextView[@resource-id = 'com.byjus.thelearningapp.premium:id/videoName']")
    video_list_lnk_xpath = (By.XPATH,
                            "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view' and @index=1]//android.widget.LinearLayout[@index=0]")
    video_tab__sub_1st_video_lnk = (By.XPATH,
                                    "//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group' and @index = 1]")
    video_title_in_list_id = (By.ID, "com.byjus.thelearningapp.premium:id/video_title_2")
    video_title = (By.ID, "com.byjus.thelearningapp.premium:id/video_title_2")
    video_name_list = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName']")
    video_auto_cancelBtn_id = (By.XPATH, "//android.widget.TextView[@text = 'Cancel']")
    video_tab_auto_cancel_btn = (By.ID, "com.byjus.thelearningapp.premium:id/btnCancelAutoPlay")
    video_chapter_name_id = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_title_2")
    video_list_view_id = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_videos_lstvw")
    video_share_icon_id = (By.ID, "com.byjus.thelearningapp.premium:id/ivShare")
    video_bookmark_icon_id = (By.ID, "com.byjus.thelearningapp.premium:id/bookmark")
    video_topic_videos_id = (By.ID, "com.byjus.thelearningapp.premium:id/videoName")
    video_progress_tab_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_progress")
    video_tab_video_lst_1st_video = (By.XPATH,
                                     "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout[@index=0]")
    video_tab_video_lst_1st_video_title = (By.XPATH,
                                           "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']/android.widget.LinearLayout[@index=0]//android.widget.TextView[@index = 1]")
    video_tab_video_player_close_btn = (By.ID, "com.byjus.thelearningapp.premium:id/video_list_close")
    video_player_list_lay = (By.ID, "com.byjus.thelearningapp.premium:id/video_list_lay")
    video_grade_selection_btn = (By.ID, "com.byjus.thelearningapp.premium:id/tvGrade")
    mob_video_title_on_player = (By.ID, "com.byjus.thelearningapp.premium:id/videoTitle")
    analysis_screen_start_test = (By.ID, "com.byjus.thelearningapp.premium:id/analytics_empty_state_start")

    #     video Locator for tab
    video_list_btn_tab = (By.ID, 'com.byjus.thelearningapp.premium:id/video_list')
    video_list_close_btn_tab = (By.ID, 'com.byjus.thelearningapp.premium:id/video_list_close')
    video_tab_videoframe = (By.ID, "com.byjus.thelearningapp.premium:id/exo_subtitles")
    video_buffering = (By.ID, "com.byjus.thelearningapp.premium:id/exo_buffering")
    video_badge_close_btn = (By.ID, "com.byjus.thelearningapp.premium:id/ivCloseBtn")
    video_auto_enable_switch = (By.ID, "com.byjus.thelearningapp.premium:id/swAutoplay")
    video_play_list_elements = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName']")
    video_practice_lnk = (By.XPATH, "//android.widget.TextView[@text = 'Practice']")
    video_auto_play_btn = (By.ID, "com.byjus.thelearningapp.premium:id/autoPlayProgressView")
    video_videos_list_in_video_list_lay_elements = (By.ID, "com.byjus.thelearningapp.premium:id/videoItem")
    tab_videos_list_elements = (By.ID, "com.byjus.thelearningapp.premium:id/videoItem")
    test_page_id = (By.ID, "com.byjus.thelearningapp.premium:id/chaptertest_recyclerview")
    #     video Locators for tab
    video_frame_pause_btn = (By.ID, "com.byjus.thelearningapp.premium:id/ivPlay")
    video_play_pause_btn = (By.XPATH,
                            "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/center_area']//android.widget.ImageButton")
    video_10s_bckwrd_text = (By.XPATH,
                             "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/center_area']//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp.premium:id/exo_rew']//android.widget.TextView")
    video_10s_frwrd_text = (By.XPATH,
                            "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/center_area']//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp.premium:id/exo_ffwd']//android.widget.TextView")

    #     Video Auto Enable
    video_next_video_title = (By.XPATH,
                              "//android.widget.LinearLayout[@resource-id = 'com.byjus.thelearningapp.premium:id/llNextVideoInfo']/android.widget.TextView[@resource-id ='com.byjus.thelearningapp.premium:id/tvNextVideoTitle']")
    tab_video_next_video_title = (By.ID, "com.byjus.thelearningapp.premium:id/tvNextVideoTitle")
    video_next_video_chapter_name = (By.XPATH,
                                     "//android.widget.LinearLayout[@resource-id = 'com.byjus.thelearningapp.premium:id/llNextVideoInfo']/android.widget.TextView[@resource-id = 'com.byjus.thelearningapp.premium:id/tvChapterName']")
    video_tab_next_video_chapter_name = (By.ID, "com.byjus.thelearningapp.premium:id/tvChapterName")
    video_up_next = (By.ID, "com.byjus.thelearningapp.premium:id/tvUpNext")
    video_video_player_chapter_txt = (By.ID, "com.byjus.thelearningapp.premium:id/tvNextVideoTitle")
    video_player_back_btn = (By.ID, "com.byjus.thelearningapp.premium:id/back")
    video_tab_player_back_btn = (By.ID, "com.byjus.thelearningapp.premium:id/backButton")
    # video_analyze_icon_btn = (By.ID,"com.byjus.thelearningapp.premium:id/home_analytics")
    video_analyze_icon_btn = (By.ID, "com.byjus.thelearningapp.premium:id/iv_analysis")
    video_keyFocus_1st_lnk = (By.XPATH,
                              "//android.widget.RelativeLayout[@resource-id='com.byjus.thelearningapp.premium:id/layout_keyfocusarea' and @index = 0]")
    video_test_icon = (By.XPATH,
                       "//android.widget.TextView[@text = 'Test']//parent::android.widget.RelativeLayout//android.widget.LinearLayout")
    video_practice_icon = (By.XPATH,
                           "//android.widget.TextView[@text = 'Practice']//parent::android.widget.RelativeLayout//android.widget.LinearLayout")
    video_test_lable = (By.XPATH,
                        "//android.widget.TextView[@text = 'Test' and @resource-id = 'com.byjus.thelearningapp.premium:id/primaryText']")
    video_practice_lable = (By.XPATH,
                            "//android.widget.TextView[@text = 'Practice' and @resource-id = 'com.byjus.thelearningapp.premium:id/primaryText']")
    video_test_x_test = (By.XPATH,
                         "//android.widget.TextView[@text = 'Test']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id ='com.byjus.thelearningapp.premium:id/secondaryText']")
    video_practice_stage_name_test = (By.XPATH,
                                      "//android.widget.TextView[@text = 'Practice']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id ='com.byjus.thelearningapp.premium:id/secondaryText']")
    video_test_right_arrow = (By.XPATH,
                              "//android.widget.TextView[@text = 'Test']//parent::android.widget.RelativeLayout//android.widget.ImageView[@resource-id ='com.byjus.thelearningapp.premium:id/right_arrow']")
    video_practice_right_arrow = (By.XPATH,
                                  "//android.widget.TextView[@text = 'Practice']//parent::android.widget.RelativeLayout//android.widget.ImageView[@resource-id ='com.byjus.thelearningapp.premium:id/right_arrow']")
    video_chapter_title_in_video_list = (By.XPATH, "//android.widget.TextView[@index = 3]")
    video_test_objective = (By.XPATH, "//android.widget.TextView[@text = 'Objective Tests']")
    video_test_subjective = (By.XPATH, "//android.widget.TextView[@text = 'Subjective Tests']")
    video_chapter_title_library_screen = (By.XPATH,
                                          "//android.widget.LinearLayout[@index = 1 and @resource-id = 'com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.TextView[@resource-id = 'com.byjus.thelearningapp.premium:id/chapter_title_view']")
    bookmark_icon = (By.XPATH, (
        "//androidx.recyclerview.widget.RecyclerView//android.widget.RelativeLayout[@index=0]//android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/ivBookmarkTag']"))
    chapterScreen_chapter_name = (By.XPATH,
                                  "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/llHeaderTextParent']//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/header_title_text']")
    video_playback_speed_dialog = (By.XPATH, "//android.widget.TextView[@text ='Playback Speed']")
    video_playback_speed_frame = (By.ID, "com.byjus.thelearningapp.premium:id/design_bottom_sheet")
    video_practice_question_screen = (By.ID, "com.byjus.thelearningapp.premium:id/practiceProgressParent")

    #     Journey Locators
    first_journey_card = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/tvSubtopicName']")
    journey_start_btn = (By.ID, "com.byjus.thelearningapp.premium:id/btnPositive")
    test_screen_start_elements = (By.XPATH, "//android.widget.TextView[@text='Analyse']")
    test_screen_Test_btn = (By.ID, "com.byjus.thelearningapp.premium:id/test_start_button")
    test_submit_Btn = (By.ID, "com.byjus.thelearningapp.premium:id/rectangleNavButton")
    noneOftheAbove_xpath = (By.ID, "com.google.android.gms:id/cancel")
    video_title_journey = (By.ID, "com.byjus.thelearningapp.premium:id/labelVideoName")
    journey_video_continue_btn = (By.ID, "com.byjus.thelearningapp.premium:id/progressAutoPlay")

    def click_on_video(self, driver):
        driver.find_element_by_id(self.video).click()

    def reset_app(self):
        CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')
        CommonMethods.run(
            'adb shell am start -n com.byjus.thelearningapp.premium/com.byjus.app.onboarding.activity.SplashActivity')

    def login_the_user(self, driver, count):
        if count == False:
            self.reset_app()
            GenericMethods.navigate_to_login_page(driver, get_data(Login_Credentials, 'login_details', 'grade'))
            self.login_to_home_page(driver)
            logging.info("successfully App resgistered with new number")
            count = True
            return count
        else:
            logging.info("Already App is resgistered with user")

    def click_test_btn(self, driver):
        driver.find_element_by_id(self.Btn_test).click()

    def tap_on_skip_btn(self, driver):
        CommonMethods.elementClick(driver, self.overlay_skip_btn)

    def click_practice_btn(self, driver):
        driver.find_element_by_id(self.Btn_practice).click()

    def reset_and_login_with_otp(self, driver):
        CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')
        CommonMethods.run(
            'adb shell am start -n com.byjus.thelearningapp.premium/com.byjus.app.onboarding.activity.SplashActivity')
        CommonMethods.accept_notification(driver, self.allow_btn_id)
        CommonMethods.wait_for_locator(driver, self.loginPageVerify_id, 5)
        CommonMethods.elementClick(driver, self.loginPageVerify_id)
        CommonMethods.click_none_of_the_above(driver, self.none_of_the_above_id)
        CommonMethods.wait_for_locator(driver, self.country_Code, 5)
        CommonMethods.elementClick(driver, self.country_Code)
        sleep(2)
        CommonMethods.scrollToElementAndClick(driver, get_data(Login_Credentials, 'login_detail3'
                                                               , 'country_code'))
        CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail3', 'mobile_no'),
                                self.phone_num)
        CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
        CommonMethods.elementClick(driver, self.loginBtn_id)
        CommonMethods.wait_for_locator(driver, self.OtpTxtBx_id, 15)
        CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail3', 'OTP'),
                                self.OtpTxtBx_id)
        if CommonMethods.wait_for_element_visible(driver, self.multiple_accounts_dialog, 5):
            profiles = CommonMethods.getElements(driver, self.user_profile_name)
            radio_buttons = CommonMethods.getElements(driver, self.profile_select_radio_button)
            for profile in profiles:
                for button in radio_buttons:
                    if profile.text == get_data(Login_Credentials, 'login_detail3', 'profile_name'):
                        button.click()
                        break
        CommonMethods.elementClick(driver, self.continue_button)

        CommonMethods.wait_for_locator(driver, self.welcome_button, 15)
        CommonMethods.elementClick(driver, self.welcome_button)

    def verify_home_page(self, driver):
        print("------------------------method")
        try:
            if CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                CommonMethods.elementClick(driver, self.back_button_id)
                CommonMethods.wait_for_locator(driver, self.profile_name_hamburger, 5)
                CommonMethods.elementClick(driver, self.profile_name_hamburger)
                CommonMethods.wait_for_locator(driver, self.user_name_profile_page, 5)
                CommonMethods.scrollToElement(driver, 'Account Details')
                CommonMethods.wait_for_locator(driver, self.profile_mob_num, 5)
                expected_mob_num = CommonMethods.getTextOfElement(driver, self.profile_mob_num)
                actual_mob_num = get_data(data_file, 'profile_credentials', 'mobileNum')
                if CommonMethods.verifyTwoText(actual_mob_num, expected_mob_num):
                    print("---------------above")
                    CommonMethods.click_on_device_back_btn(driver)
                    print("----------------------below")
                    logging.info('home page verified')
                else:
                    self.reset_and_login_with_otp(driver)
                    return True
            else:
                logging.info('user is not in Home page')
                return False
        except:
            logging.info('Error in Verifing Home Page')

    def allow_notifications(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.allow_btn_id, 5):
            CommonMethods.accept_notification(driver, self.allow_btn_id)
            CommonMethods.accept_notification(driver, self.allow_btn_id)

    def check_for_skip_btn(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.skipBtn_id, 5):
            CommonMethods.elementClick(driver, self.skipBtn_id)
            CommonMethods.wait_for_element_visible(driver, self.chooseCourse_Title_xpath, 7)
            CommonMethods.elementClick(driver, get_data(data_file, 'profile_credentials', 'grade'))
            CommonMethods.wait_for_element_visible(driver, self.noneOftheAbove_xpath, 7)
            CommonMethods.elementClick(driver, self.noneOftheAbove_xpath)
            CommonMethods.elementClick(driver, self.login_link_id)

    def user_registration(self, driver):
        grade = get_data(data_file, 'profile_credentials', 'grade')
        sub_grade = (By.XPATH, "//android.widget.Button[@text=\'" + grade + "\']")
        if CommonMethods.wait_for_element_visible(driver, self.login_register_btn, 3):
            CommonMethods.elementClick(driver, self.login_register_btn)
            CommonMethods.wait_for_element_visible(driver, self.chooseCourse_Title_xpath, 7)
            CommonMethods.elementClick(driver, sub_grade)
            CommonMethods.wait_for_element_visible(driver, self.registration_name_field, 7)
            CommonMethods.enterText(driver, "testJ", self.registration_name_field)
            CommonMethods.wait_for_element_visible(driver, self.register_btn, 5)
            CommonMethods.elementClick(driver, self.register_btn)

    def login_to_home_page(self, driver):
        self.reset_and_login_with_otp(driver)

    def verify_to_login_page(self, driver):
        self.allow_notifications(driver)
        self.check_for_skip_btn(driver)
        self.login_to_home_page(driver)

    def verify_badge(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.video_badge_close_btn, 10):
            CommonMethods.elementClick(driver, self.video_badge_close_btn)

    def verify_corana_dialog(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.homescreen_corana_dialog_ok_btn, 10):
            CommonMethods.elementClick(driver, self.homescreen_corana_dialog_ok_btn)

    def tap_on_device_back_btn(self, driver):
        sleep(3)
        CommonMethods.click_on_device_back_btn(driver)

    def tap_on_back_arrow_btn(self, driver):
        sleep(3)
        back_arrow = CommonMethods.getElement(driver, self.practice_back_arrow_btn)
        back_arrow.click()

    def navigate_to_home_screen(self, driver, text):
        try:
            sleep(10)
            subject_rgb = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")
            if CommonMethods.wait_for_element_visible(driver, self.homescreen_corana_dialog_ok_btn, 10):
                CommonMethods.elementClick(driver, self.homescreen_corana_dialog_ok_btn)
                self.verify_badge(driver)
                self.verify_home_page(driver)
                VideoPage.subject_rgb_lst = self.get_the_rgb_lst(driver, subject_rgb)
            elif CommonMethods.wait_for_element_visible(driver, self.back_button_id, 5):
                self.verify_badge(driver)
                self.verify_home_page(driver)
                VideoPage.subject_rgb_lst = self.get_the_rgb_lst(driver, subject_rgb)

            elif CommonMethods.wait_for_element_visible(driver, self.video_badge_close_btn, 5):
                self.verify_badge(driver)
            else:
                self.reset_and_login_with_otp(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigateToHomeScreen')
        except:
            CommonMethods.exception(driver, featureFileName, 'navigateToHomeScreen')

    def navigate_to_library(self, driver, sub):
        try:
            CommonMethods.wait_for_element_visible(driver, self.profile_header_id, 10)
            pythonSub_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']")
            CommonMethods.wait_for_element_visible(driver, pythonSub_xpath, 3)
            CommonMethods.elementClick(driver, pythonSub_xpath)
            if CommonMethods.isElementPresent(driver, self.personalizeScreen_xpath):
                logging.info('successfully navigated to library')
            else:
                for i in range(5):
                    CommonMethods.run('adb shell input touchscreen swipe 300 300 300 800')
                    check = CommonMethods.wait_for_element_visible(driver, self.librayBtn_id, 5)
                    if check == True:
                        break
                CommonMethods.wait_for_locator(driver, self.librayBtn_id, 10)
                CommonMethods.elementClick(driver, self.librayBtn_id)
                logging.info('successfully navigated to library')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_library')
        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_library')

    def navigate_to_personalised_Screen(self, driver, sub):
        try:
            CommonMethods.wait_for_element_visible(driver, self.profile_header_id, 10)
            pythonSub_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']")
            CommonMethods.wait_for_element_visible(driver, pythonSub_xpath, 3)
            CommonMethods.elementClick(driver, pythonSub_xpath)
            if CommonMethods.isElementPresent(driver, self.librayBtn_id):
                logging.info('successfully navigated to Personalised Screen')
            else:
                for i in range(3):
                    CommonMethods.run('adb shell input touchscreen swipe 300 300 300 800')
                    check = CommonMethods.wait_for_element_visible(driver, self.personalizeScreen_xpath, 3)
                    if check == True:
                        break
                CommonMethods.wait_for_element_visible(driver, self.personalizeScreen_xpath, 5)
                CommonMethods.elementClick(driver, self.personalizeScreen_xpath)
                logging.info('successfully navigated to Personalised Screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_personalised_Screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_personalised_Screen')

    def tap_on_chapter(self, driver, sub):
        try:
            CommonMethods.wait_for_element_visible(driver, self.profile_header_id, 10)
            pythonSub_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']")
            CommonMethods.wait_for_element_visible(driver, pythonSub_xpath, 3)
            CommonMethods.elementClick(driver, pythonSub_xpath)
            sleep(5)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_chapter')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_chapter')

    def navigateToSubjectLib2(self, driver, sub):
        try:
            driver.start_activity("com.android.chrome", "com.google.android.apps.chrome.Main")
            driver.get("https://app.byjus.com/fp1RtHwywC?infoParam=7329")
        except:
            pytest.fail("Activity Failed To start")

    def tap_on_any_video_in_sub_screen(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                sleep(3)
                ele = CommonMethods.getElements(driver, self.chapter_videoLnk_elements)
                ele_length = len(ele)
                n = random.randint(1, ele_length - 1)
                ele[n].click()
                logging.info("video is selected")
            elif device == 'tab':
                sleep(3)
                ele = CommonMethods.getElements(driver, self.tab_chapter_videoLnk_elements)
                ele_length = len(ele)
                n = random.randint(1, ele_length - 1)
                ele[n].click()
                logging.info("video is selected")
            else:
                logging.info("Failed Locator in Method tap_on_any_video_in_sub_screen")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail('Failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_any_video_in_sub_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_any_video_in_sub_screen')

    def tap_on_any_journey_card_in_sub_screen(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                CommonMethods.wait_for_element_visible(driver, self.first_journey_card, 10)
                ele = CommonMethods.getElements(driver, self.first_journey_card)
                ele[0].click()
            elif device == 'tab':
                CommonMethods.wait_for_element_visible(driver, self.first_journey_card, 10)
                ele = CommonMethods.getElements(driver, self.first_journey_card)
                ele[0].click()
            else:
                logging.info("Failed Locator in Method tap_on_any_video_in_sub_screen")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail('Failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_any_journey_card_in_sub_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_any_journey_card_in_sub_screen')

    def tap_on_start_video(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                CommonMethods.wait_for_element_visible(driver, self.journey_start_btn, 20)
                CommonMethods.elementClick(driver, self.journey_start_btn)
            elif device == 'tab':
                logging.info("handle")
            else:
                logging.info("Failed Locator in Method tap_on_start_video")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail('Failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_start_video')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_start_video')

    def verify_video_playing(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.video_list_btn_tab,
                                                      3) or CommonMethods.wait_for_element_visible(driver,
                                                                                                   self.video_list_close_btn_tab,
                                                                                                   3):
                pass
            sleep(3)
            check2 = CommonMethods.isElementPresent(driver, self.videoPlayingNow_xpath)
            CommonMethods.elementClick(driver, self.video1stLink_xpath)
            sleep(2)
            CommonMethods.elementClick(driver, self.video1stLink_xpath)
            check1 = CommonMethods.isElementPresent(driver, self.video_pause_btn_id)
            if check1 or check2:
                logging.info('video is playing successfully')
            else:
                logging.info("Failed Locator in Method verify_video_playing")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail('Failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_playing')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_playing')

    def verify_reply_next_previous_btn(self, driver):
        try:
            check1 = CommonMethods.isElementPresent(driver, self.video_play_btn)
            check2 = CommonMethods.isElementPresent(driver, self.video_play_previous_btn)
            check3 = CommonMethods.isElementPresent(driver, self.video_play_next_btn)
            self.verify_true_or_false(driver, check1, 'verify_reply_next_previous_btn', 'Reply Btn')
            self.verify_true_or_false(driver, check2, 'verify_reply_next_previous_btn', 'Previous Btn')
            self.verify_true_or_false(driver, check3, 'verify_reply_next_previous_btn', 'Next Btn')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_reply_next_previous_btn')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_reply_next_previous_btn')

    def tap_on_pause_btn(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                self.wait_till_video_load(driver)
                self.pause_video(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_pause_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_pause_btn')

    def tap_on_player_screen(self):
        CommonMethods.run('adb shell input tap 40 200')

    def verify_play_btn_in_lanscape(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                check = CommonMethods.isElementPresent(driver, self.video_play_btn)
                self.verify_true_or_false(driver, check, 'verify_play_btn_in_lanscape', 'Video play button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_play_btn_in_lanscape')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_play_btn_in_lanscape')

    def verify_video_paused(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                if CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 3):
                    logging.info('video Paused Successfully')
                else:
                    logging.info("Failed Locator in Method verify_video_paused")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            elif device == 'mobile':
                check = CommonMethods.isElementPresent(driver, self.video_play_btn)
                #                 check2 = driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']/android.widget.LinearLayout[@index=0]//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']").text
                #                 logging.info(check1)
                #                 logging.info(check2)
                #                 if check1 == True  or  'Completed' in check2  or 'Paused' in check2 :
                #                     pass
                self.verify_true_or_false(driver, check, 'verify_video_paused', 'pause btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_paused')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_paused')

    def verify_video_is_not_paused(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                if CommonMethods.wait_for_element_visible(driver, self.video_pause_btn_id, 3):
                    logging.info('video Paused Successfully')
                else:
                    logging.info("Failed Locator in Method verify_video_paused")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            elif device == 'mobile':
                check = CommonMethods.isElementPresent(driver, self.video_pause_btn_id)
                self.verify_true_or_false(driver, check, 'verify_video_paused', 'pause btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_paused')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_paused')

    def tap_on_playbtn(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                VideoPage.video_start_time = self.get_video_start_time(driver)
                if CommonMethods.elementClick(driver, self.video_play_btn):
                    logging.info('taped on play button successfully')
            elif device == 'mobile':
                check = CommonMethods.elementClick(driver, self.video_play_btn)
                if check == True:
                    pass
                else:
                    logging.info('Failed to tap on Play Button')
                    pytest.fail('Failed to tap on Play Button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_playbtn')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_playbtn')

    def custom_wait(self, sec):
        try:
            sec = int(sec)
            sleep(sec)
        except:
            logging.info("failed in Custom Wait")
            pytest.fail('Failed')

    def verify_frwd_10Sec(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                start_time = self.get_video_start_time(driver)
                self.tap_on_video_player_icon(driver, self.ten_sec_fwd_btn_id)
                self.wait_till_video_load(driver)
                end_time = self.get_video_start_time(driver)
                if end_time >= start_time + 10:
                    logging.info('video forwaded 10 sec')
                else:
                    logging.info("Failed Locator in Method verify_frwd_10Sec")
                    CommonMethods.takeScreenShot(self, driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            elif device == 'mobile':
                start_time = self.get_video_start_time(driver)
                self.tap_on_video_player_icon(driver, self.ten_sec_fwd_btn_id)
                self.wait_till_video_load(driver)
                end_time = self.get_video_start_time(driver)
                if end_time >= start_time + 10:
                    logging.info('video forwaded 10 sec')
                else:
                    logging.info("Failed Locator in Method verify_frwd_10Sec")
                    CommonMethods.takeScreenShot(self, driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_frwd_10Sec')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_frwd_10Sec')

    def tap_on_video_player_icon(self, driver, locator):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 20:
                wait_count += 1
                CommonMethods.elementClick(driver, self.video_tab_videoframe)
                flag = CommonMethods.elementClick(driver, locator)
                check = not flag
        except:
            logging.info('Error in clicking the video player icon')

    def verify_video_backwrd_10Sec(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                start_time = self.get_video_start_time(driver)
                self.tap_on_video_player_icon(driver, self.ten_sec_bkwd_btn_id)
                self.wait_till_video_load(driver)
                end_time = self.get_video_start_time(driver)
                logging.info(start_time)
                logging.info(end_time)
                if end_time < start_time:
                    logging.info('video Backward 10 sec')
                else:
                    logging.info("Failed Locator in Method verify_video_backwrd_10Sec")
                    CommonMethods.takeScreenShot(self, driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            elif device == 'mobile':
                start_time = self.get_video_start_time(driver)
                self.tap_on_video_player_icon(driver, self.ten_sec_bkwd_btn_id)
                self.wait_till_video_load(driver)
                end_time = self.get_video_start_time(driver)
                logging.info(start_time)
                logging.info(end_time)
                if end_time < start_time:
                    logging.info('video Backward 10 sec')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_backwrd_10Sec')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_backwrd_10Sec')

    def tap_on_device_home_btn(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                VideoPage.videoProgressTimeBfr = self.get_video_start_time(driver)
                CommonMethods.click_on_device_home_btn()
            elif device == 'mobile':
                VideoPage.videoProgressTimeBfr = self.get_video_start_time(driver)
                CommonMethods.click_on_device_home_btn()
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_device_home_btn')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_device_home_btn')

    def take_app_foreground(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                if CommonMethods.take_app_foreground(driver, self.byjusAppPackage):
                    logging.info('App taken to foreground')
                else:
                    logging.info("Failed Locator in Method take_app_foreground")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            elif device == 'mobile':
                if CommonMethods.take_app_foreground(driver, self.byjusAppPackage):
                    pass
                else:
                    logging.info("Failed Locator in Method take_app_foreground")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'viewAppForeground')

        except:
            CommonMethods.exception(driver, featureFileName, 'viewAppForeground')

    def navigateToLoginPage(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.skipBtn_id, 2):
                driver.find_element_by_id("com.byjus.thelearningapp.premium:id/buttonSkip").click()
                driver.find_element_by_xpath("//android.widget.Button[@text='8th']").click()
                driver.find_element_by_id("com.byjus.thelearningapp.premium:id/tvLoginBl").click()
            else:
                logging.error("failed to navigate to login page")
        except:
            logging.info('Exception occured While bringing the app foreground')

    def verify_video_playing_from_last_progress(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                #                 logging.info('entered tab')
                #                 sleep(2)
                #                 video_before_time =  self.videoProgressTimeBfr
                #                 logging.info('taken time'+video_before_time)
                #                 self.wait_till_video_load(driver)
                #                 videoProgressTimeAfter = self.get_video_start_time(driver)
                #                 logging.info('taken after time'+videoProgressTimeAfter)
                #                 sleep(2)
                #                 if videoProgressTimeAfter >= video_before_time:
                #                     logging.info('Video Resumed From last Progress')
                #                     pass
                #                 else:
                #                     logging.info("Failed Locator in Method verify_video_playing_from_last_progress")
                #                     CommonMethods.takeScreenShot(driver,featureFileName)
                #                     pytest.fail("Failed Due to Locator in Video Page")
                actual = self.get_video_start_time(driver)
                self.wait_till_video_load(driver)
                expected = VideoPage.video_start_time
                check = actual >= expected
                self.verify_true_or_false(driver, check, 'verify_video_playing_from_last_progress', "video time")
            elif device == 'mobile':
                sleep(2)
                video_before_time = VideoPage.videoProgressTimeBfr
                self.wait_till_video_load(driver)
                videoProgressTimeAfter = self.get_video_start_time(driver)
                sleep(2)
                if videoProgressTimeAfter >= video_before_time:
                    logging.info('Video Resumed From last Progress')
                else:
                    logging.info("Failed Locator in Method verify_video_playing_from_last_progress")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_playing_from_last_progress')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_playing_from_last_progress')

    def change_orientation_landscape(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == "tab":
                logging.info('video will always play in landscape mode')

            elif device == "mobile":
                VideoPage.video_start_time_portrait = self.get_video_start_time(driver)
                check = self.click_on_video_icon(driver, self.screen_orientation_id)
                if check == True:
                    logging.info('device set to landscape')
                else:
                    self.test_fail(driver, 'change_orientation_landscape')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'change_orientation_landscape')

        except:
            CommonMethods.exception(driver, featureFileName, 'change_orientation_landscape')

    def change_orientation_potrait(self, driver):
        try:
            VideoPage.video_start_time_landscape = self.get_video_start_time(driver)
            check = self.click_on_video_icon(driver, self.screen_orientation_id)
            self.verify_true_or_false(driver, check, 'change_orientation_potrait', 'screen toggle')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'change_orientation_landscape')
        except:
            CommonMethods.exception(driver, featureFileName, 'change_orientation_landscape')

    def verify_video_continue_without_pausing(self, driver):
        try:
            check = self.is_video_icon_present(driver, self.video_pause_btn_id)
            self.verify_true_or_false(driver, check, 'verify_video_continue_without_pausing', 'play button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_continue_without_pausing')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_continue_without_pausing')

    def is_video_paused(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.video_pause_btn_id, 5):
            return True
        else:
            return False

    def wait_till_video_load(self, driver):
        driver.implicitly_wait(0.1)
        loading_count = 0
        try:
            while CommonMethods.wait_for_element_visible(driver, self.video_buffering, 2) and loading_count < 75:
                loading_count += 1
                sleep(0.2)
            logging.info('video Loading done successfully')
        except:
            logging.info("Error in waiting for video to load")

    def wait_till_element_visible(self, driver, locator):
        driver.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.wait_for_element_visible(driver, locator, 1) and loading_count < 75:
                loading_count += 1
                sleep(0.2)
            logging.info('video Loading done successfully')
        except:
            logging.info('Error in waiting for the element')

    def wait_till_video_complete(self, driver, time):
        driver.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.wait_for_element_visible(driver, self.video_auto_cancelBtn_id,
                                                             2) and loading_count < time + 100:
                loading_count += 1
                sleep(0.2)
            return True
        except:
            logging.error('Error in playing the video completely')

    def pause_video(self, driver):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1
                CommonMethods.elementClick(driver, self.video_tab_videoframe)
                CommonMethods.elementClick(driver, self.video_pause_btn_id)
                flag = CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 2)
                check = not flag
        except:
            logging.info('Error in pausing the video')

    def play_video(self, driver):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1
                CommonMethods.elementClick(driver, self.video_tab_videoframe)
                if CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 3):
                    CommonMethods.elementClick(driver, self.video_play_btn)
                flag = self.is_video_icon_present(driver, self.video_pause_btn_id)
                check = not flag
        except:
            logging.info('Error in pausing the video')

    def get_x_y_coordinate(self, driver, locator):
        locator = locator
        loc = CommonMethods.get_element_location(driver, locator)
        x = loc["x"]
        y = loc["y"]
        return x, y

    def get_element_coordinates(self, driver, locator):
        try:
            loc = CommonMethods.get_size_of_element(driver, locator)
            x = loc['x']
            y = loc['y']
            height = loc['height']
            width = loc['width']
            x2 = x + width
            y2 = y + height
            return x, y, x2, y2
        except:
            return None, None, None, None

    def click_on_x_y_coordinate(self, x, y):
        try:
            CommonMethods.run('adb shell input tap {} {}'.format(x, y))
            return True
        except:
            return False

    def verify_video_back_btn(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(driver, self.video_backBtn_id)
                self.verify_true_or_false(driver, check, 'verify_video_back_btn', 'video back Button')
            elif device == 'mobile':
                CommonMethods.wait_for_locator(driver, self.video_backBtn_id, 5)
                check = CommonMethods.isElementPresent(driver, self.video_backBtn_id)
                if check == True:
                    pass
                else:
                    logging.info("Failed due to Element not visible in Method verify_video_back_btn")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_back_btn')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_back_btn')

    def verify_video_card_opened(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.video_frame_id, 10)
            self.verify_true_or_false(driver, check, 'verify_video_card_opened', 'Video screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_back_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_back_btn')

    def tap_on_app_back_button(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.video_backBtn_id, 5)
            check = CommonMethods.elementClick(driver, self.video_backBtn_id)
            self.verify_true_or_false(driver, check, 'tap_on_app_back_button', "app back button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_app_back_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_app_back_button')

    def verify_speedBtn(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(driver, self.videoSpeed_up_dwnIcon_id)
                self.verify_true_or_false(driver, check, 'verify_speedBtn', 'video speed up down icon')
        #             elif device == 'mobile':
        #                 CommonMethods.wait_for_locator(driver, self.videoSpeed_up_dwnIcon_id, 5)
        #                 check = CommonMethods.isElementPresent(driver, self.videoSpeed_up_dwnIcon_id)
        #                 if check == True:
        #                     pass
        #                 else:
        #                     logging.info("Failed due to Element not visible in Method verify_speedBtn")
        #                     CommonMethods.takeScreenShot(driver,featureFileName)
        #                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_speedBtn')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_speedBtn')

    def verify_question_page(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.video_practice_question_screen, 10)
            self.verify_true_or_false(driver, check, 'verify_question_page', 'question screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_question_page')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_question_page')

    def verify_app_redirected_to_journey_screen(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.journey_video_continue_btn, 10)
            self.verify_true_or_false(driver, check, 'verify_app_redirected_to_journey_screen', 'journey Screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_app_redirected_to_journey_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_app_redirected_to_journey_screen')

    def verify_subtitile(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(driver, self.videoSpeed_up_dwnIcon_id)
        #             elif device == 'mobile':
        #                 CommonMethods.wait_for_locator(driver, self.video_subtitileIcon_id, 5)
        #                 check = CommonMethods.isElementPresent(driver, self.video_subtitileIcon_id)
        #                 if check == True:
        #                     pass
        #                 else:
        #                     logging.info("Failed due to Element not visible in Method verify_subtitile")
        #                     CommonMethods.takeScreenShot(driver,featureFileName)
        #                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_subtitile')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_subtitile')

    def verify_multipleAudio(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(driver, self.video_mutipleAudioTracks_id)
                self.verify_true_or_false(driver, check, 'verify_multipleAudio', 'Mutiple Audio Icon')
        #             elif device == 'mobile':
        #                 CommonMethods.wait_for_locator(driver, self.video_mutipleAudioTracks_id, 5)
        #                 check = CommonMethods.isElementPresent(driver, self.video_mutipleAudioTracks_id)
        #                 if check == True:
        #                     pass
        #                 else:
        #                     logging.info("Failed due to Element not visible in Method verify_multipleAudio")
        #                     CommonMethods.takeScreenShot(driver,featureFileName)
        #                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_multipleAudio')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_multipleAudio')

    def verify_setting_icon(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(driver, self.video_settingIcon_id)
                self.verify_true_or_false(driver, check, 'verify_setting_icon', 'video setting Icon')
        #             elif device == 'mobile':
        #                 CommonMethods.wait_for_locator(driver, self.video_settingIcon_id, 5)
        #                 check = CommonMethods.isElementPresent(driver, self.video_settingIcon_id)
        #                 if check == True:
        #                     pass
        #                 else:
        #                     logging.info("Failed due to Element not visible in Method verify_setting_icon")
        #                     CommonMethods.takeScreenShot(driver,featureFileName)
        #                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_setting_icon')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_setting_icon')

    def verify_text_present(self, driver, text):
        try:
            check = CommonMethods.findText(driver, text)
            if check == True:
                logging.info(text + ' is present and verified')
            else:
                logging.error('Failed in Finding the text ' + text)
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed in login page")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyTextPresent')

        except:
            CommonMethods.exception(driver, featureFileName, 'verifyTextPresent')

    def tap_on_text_lnk(self, driver, text):
        try:
            ele = CommonMethods.find_element_of_radio_btn(driver, text)
            ele.click()
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyTextPresent')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyTextPresent')

    def tap_on_test_in_chapter_screen(self, driver):
        try:
            CommonMethods.scrollToElementAndClick(driver, 'Test')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_test_in_chapter_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_test_in_chapter_screen')

    def verify_radio_btn_text_present(self, driver, text):
        try:
            check = CommonMethods.find_radio_btn(driver, text)
            if check == True:
                logging.info(text + ' is present and verified')
            else:
                logging.error('Failed in Finding the text ' + text)
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed in login page")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_radio_btn_text_present')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_radio_btn_text_present')

    def verify_speed_down_compare_to_normal(self, driver):
        try:
            sleep(3)
            start_time = self.get_video_start_time(driver)
            sleep(16)
            end_time = self.get_video_start_time(driver)
            check = (end_time - start_time) <= 16
            self.verify_true_or_false(driver, check, 'verify_speed_down_compare_to_normal', '0.75x is shown')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_speed_down_compare_to_normal')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_speed_down_compare_to_normal')

    def verify_speed_down_compare_to_075x(self, driver):
        try:
            sleep(3)
            start_time = self.get_video_start_time(driver)
            sleep(16)
            end_time = self.get_video_start_time(driver)
            check = (end_time - start_time) <= 12
            self.verify_true_or_false(driver, check, 'verify_speed_down_compare_to_075x', '0.5x is shown')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_speed_down_compare_to_075x')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_speed_down_compare_to_075x')

    def verify_speed_up_compare_to_normal(self, driver):
        try:
            self.wait_till_video_load(driver)
            start_time = self.get_video_start_time(driver)
            self.play_video(driver)
            sleep(16)
            end_time = self.get_video_start_time(driver)
            check = (end_time - start_time) >= 16
            self.verify_true_or_false(driver, check, 'verify_speed_up_compare_to_normal', '1.25x is shown')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_speed_up_compare_to_normal')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_speed_up_compare_to_normal')

    def verify_speed_up_compare_to_125x(self, driver):
        try:
            sleep(3)
            start_time = self.get_video_start_time(driver)
            self.play_video(driver)
            sleep(16)
            end_time = self.get_video_start_time(driver)
            check = (end_time - start_time) >= 18
            self.verify_true_or_false(driver, check, 'verify_speed_up_compare_to_125x', '1.5x is shown')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_speed_up_compare_to_125x')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_speed_up_compare_to_125x')

    def verify_selected_playback_speed(self, driver, text):
        try:
            sleep(3)  # need to wait till the video loads
            self.wait_till_video_load(driver)
            element = CommonMethods.find_element_of_radio_btn(driver, text)
            check = bool(element.get_attribute('checked').capitalize())
            self.verify_true_or_false(driver, check, 'verify_selected_playback_speed', text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_selected_playback_speed')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_selected_playback_speed')

    def verify_playback_speed_buttom_sheet(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.video_playback_speed_frame)
            self.verify_true_or_false(driver, check, 'verify_playback_speed_buttom_sheet',
                                      "play back speed bottom dialog")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_playback_speed_buttom_sheet')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_playback_speed_buttom_sheet')

    def tap_on_playback_speed_icon(self, driver):
        try:
            #             device = CommonMethods.get_device_type(driver)
            #             if device == 'mobile':
            CommonMethods.wait_for_element_visible(driver, self.videoSpeed_up_dwnIcon_id, 10)
            self.tap_on_video_player_icon(driver, self.videoSpeed_up_dwnIcon_id)
            check = CommonMethods.wait_for_element_visible(driver, self.video_playback_speed_dialog, 5)
            self.verify_true_or_false(driver, check, 'tap_on_playback_speed_icon', 'Playback speed Text')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_playback_speed_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_playback_speed_icon')

    def verify_play_pause_Icon(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(driver, self.video_play_pause_btn)
                self.verify_true_or_false(driver, check, 'verify_play_pause_Icon', 'video play/pause')
        #             elif device == 'mobile':
        #                 CommonMethods.wait_for_locator(driver, self.video_play_btn, 5)
        #                 check = CommonMethods.isElementPresent(driver, self.video_play_btn)
        #                 if check == True:
        #                     pass
        #                 else:
        #                     logging.info("Failed due to Element not visible in Method verify_play_pause_Icon")
        #                     CommonMethods.takeScreenShot(driver,featureFileName)
        #                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_play_pause_Icon')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_play_pause_Icon')

    def verify_fastFrwd(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(driver, self.ten_sec_bkwd_btn_id)
                self.verify_true_or_false(driver, check, 'verify_fastFrwd', 'video fast forward Icon')
                check = self.is_video_icon_present(driver, self.video_10s_frwrd_text)
                self.verify_true_or_false(driver, check, 'verify_fastFrwd', '10 sec video fast forward Text')
        #             elif device == 'mobile':
        #                 CommonMethods.wait_for_locator(driver, self.ten_sec_bkwd_btn_id, 5)
        #                 check1 = CommonMethods.isElementPresent(driver, self.ten_sec_bkwd_btn_id)
        #                 check2 = CommonMethods.isElementPresent(driver, self.ten_sec_fwd_btn_id)
        #                 if check1 and check2:
        #                     pass
        #                 else:
        #                     logging.info("Failed due to Element not visible in Method verify_fastFrwd")
        #                     CommonMethods.takeScreenShot(driver,featureFileName)
        #                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_fastFrwd')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_fastFrwd')

    def verify_fast_backwrd_icon(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(driver, self.ten_sec_bkwd_btn_id)
                self.verify_true_or_false(driver, check, 'verify_fast_backwrd_icon', 'video fast backward')
                check = self.is_video_icon_present(driver, self.video_10s_bckwrd_text)
                self.verify_true_or_false(driver, check, 'verify_fast_backwrd_icon', '10 sec video fast backward Text')
        #             elif device == 'mobile':
        #                 CommonMethods.wait_for_locator(driver, self.ten_sec_bkwd_btn_id, 5)
        #                 check1 = CommonMethods.isElementPresent(driver, self.ten_sec_bkwd_btn_id)
        #                 check2 = CommonMethods.isElementPresent(driver, self.ten_sec_fwd_btn_id)
        #                 if check1 and check2:
        #                     pass
        #                 else:
        #                     logging.info("Failed due to Element not visible in Method verify_fastFrwd")
        #                     CommonMethods.takeScreenShot(driver,featureFileName)
        #                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_fastFrwd')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_fastFrwd')

    def verify_video_progress_bar(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(driver, self.video_progress_tab_id)
                self.verify_true_or_false(driver, check, 'verify_video_progress_bar', 'video progress bar')
        #             elif device == 'mobile':
        #                 CommonMethods.wait_for_locator(driver, self.video_progressBar_id, 5)
        #                 check = CommonMethods.isElementPresent(driver, self.video_progressBar_id)
        #                 if check == True:
        #                     pass
        #                 else:
        #                     logging.info("Failed due to Element not visible in Method verify_video_progress_bar")
        #                     CommonMethods.takeScreenShot(driver,featureFileName)
        #                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_progress_bar')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_progress_bar')

    def verify_video_fullScreen_icon(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                logging.info('Tab has no portrait mode')
            elif device == 'mobile':
                check = self.is_video_icon_present(driver, self.screen_orientation_id)
                self.verify_true_or_false(driver, check, 'verify_video_fullScreen_icon', 'orientation toggle bar')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_fullScreen_icon')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_fullScreen_icon')

    #     def tap_on_pause_btn(self,driver):
    #         try:
    #             sleep(3)
    #             orientation = CommonMethods.get_screen_orientation(driver)
    #             loc = CommonMethods.get_element_location(driver, self.videoPlayBtn_id)
    #             x = loc["x"]
    #             y = loc["y"]
    #             CommonMethods.elementClick(driver, self.videoPlayBtn_id)
    #             CommonMethods.run('adb shell input tap {} {}'.format(x, y))
    #             CommonMethods.run('adb shell input tap {} {}'.format(x, y))
    #             if orientation == 'LANDSCAPE':
    #                 pass
    #             else:
    #                 logging.info("Failed Locator in Method tap_on_pause_btn")
    #                 CommonMethods.takeScreenShot(driver, featureFileName)
    #                 pytest.fail("Failed Due to Locator in Video Page")
    #         except NoSuchElementException:
    #             CommonMethods.noSuchEleExcept(driver,featureFileName,'tap_on_pause_btn')
    #
    #         except :
    #             CommonMethods.exception(driver,featureFileName,'tap_on_pause_btn')

    def tap_on_video_from_video_list(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)

            if device == 'mobile':
                if not CommonMethods.wait_for_element_visible(driver, self.videoPlayingNow_xpath, 5):
                    CommonMethods.elementClick(driver, self.video_tab_video_lst_1st_video)

            elif device == 'tab':
                CommonMethods.wait_for_locator(driver, self.video_list_lnk_xpath, 3)
                CommonMethods.elementClick(driver, self.video_list_lnk_xpath)

            else:
                logging.info("Failed due to Element not visible in Method tap_on_video_from_video_list")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_video_from_video_list')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_video_from_video_list')

    """This method is written to verify the video playing in this we will be inspecting x y coordinates of pause btn
    and taken the time video will be palyed for 10 sec and we will check the difference and pass the method"""

    def video_should_played(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                if CommonMethods.wait_for_element_visible(driver, self.video_tab_video_player_close_btn, 2):
                    CommonMethods.elementClick(driver, self.video_tab_video_lst_1st_video)
                    if CommonMethods.wait_for_element_visible(driver, self.video_tab_video_player_close_btn, 2):
                        CommonMethods.elementClick(driver, self.video_tab_video_player_close_btn)
                self.wait_till_video_load(driver)
                before_video_time = self.get_video_start_time(driver)
                sleep(10)
                after_video_time = self.get_video_start_time(driver)
                if after_video_time > before_video_time:
                    logging.info('Video is playing successfully')
                else:
                    logging.info("Failed due to Element not visible in Method video_should_played")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
            elif device == 'mobile':
                CommonMethods.wait_for_element_visible(driver, self.video_buffering, 20)
                self.wait_till_video_load(driver)
                self.pause_video(driver)
                x, y = self.get_x_y_coordinate(driver, self.video_progressBar_id)
                CommonMethods.run('adb shell input tap {} {}'.format(x, y))
                self.wait_till_video_load(driver)
                before_video_time = self.get_video_start_time(driver)
                sleep(10)
                after_video_time = self.get_video_start_time(driver)
                if after_video_time > before_video_time:
                    logging.info('Video is playing successfully')
                else:
                    logging.info("Failed due to Element not visible in Method video_should_played")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'video_should_played')

        except:
            CommonMethods.exception(driver, featureFileName, 'video_should_played')

    """This method is written to verify the video playing in this we will be inspecting x y coordinates of pause btn
    and taken the time video will be palyed for 10 sec and we will check the difference and pass the method"""

    def Video_should_played(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                if CommonMethods.wait_for_element_visible(driver, self.video_tab_video_player_close_btn, 2):
                    CommonMethods.elementClick(driver, self.video_tab_video_lst_1st_video)
                    if CommonMethods.wait_for_element_visible(driver, self.video_tab_video_player_close_btn, 2):
                        CommonMethods.elementClick(driver, self.video_tab_video_player_close_btn)
                self.wait_till_video_load(driver)
                before_video_time = self.get_video_start_time(driver)
                sleep(10)
                after_video_time = self.get_video_start_time(driver)
                if after_video_time > before_video_time:
                    logging.info('Video is playing successfully')
                else:
                    logging.info("Failed due to Element not visible in Method video_should_played")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
            elif device == 'mobile':
                self.wait_till_video_load(driver)
                self.tap_on_video_player_icon(driver, self.video_pause_btn_id)
                #                 self.pause_video(driver)
                x, y = self.get_x_y_coordinate(driver, self.video_progressBar_id)
                CommonMethods.run('adb shell input tap {} {}'.format(x, y))
                self.wait_till_video_load(driver)
                before_video_time = self.get_video_start_time(driver)
                sleep(10)
                after_video_time = self.get_video_start_time(driver)
                if after_video_time > before_video_time:
                    logging.info('Video is playing successfully')
                else:
                    logging.info("Failed due to Element not visible in Method video_should_played")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'video_should_played')
        except:
            CommonMethods.exception(driver, featureFileName, 'video_should_played')

    def verify_video_playing_in_landscape(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                orientation = CommonMethods.get_screen_orientation(driver)
                check = orientation == 'LANDSCAPE'
                self.verify_true_or_false(driver, check, 'verify_video_playing_in_landscape', "Landscape")
            elif device == 'mobile':
                #                 check1 = not CommonMethods.wait_for_element_visible(driver, self.video_player_list_lay, 3)
                sleep(3)
                orientation = CommonMethods.get_screen_orientation(driver)
                check = orientation == 'LANDSCAPE'
                if check == True:
                    self.Video_should_played(driver)
                    VideoPage.video_start_time_landscape = self.get_video_start_time(driver)
                else:
                    logging.info("Failed due to Element not visible in Method verify_video_playing_in_landscape")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_playing_in_landscape')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_playing_in_landscape')

    def verify_video_in_potrait(self, driver):
        try:
            self.video_should_played(driver)
            check = self.is_video_icon_present(driver, self.video_pause_btn_id)
            self.video_start_time = self.get_video_start_time(driver)
            check1 = CommonMethods.wait_for_element_visible(driver, self.video_player_list_lay, 3)
            check2 = CommonMethods.wait_for_element_visible(driver, self.video_frame_id, 3)
            if check and check1 and check2:
                logging.info('Video is played successfully in portrait')
            else:
                logging.info("Failed due to Element not visible in Method video_should_played")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_in_potrait')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_in_potrait')

    def video_play_without_any_interruption_in_landscape(self, driver):
        try:
            VideoPage.video_start_time_landscape = self.get_video_start_time(driver)
            check = VideoPage.video_start_time_landscape >= VideoPage.video_start_time_portrait
            self.verify_true_or_false(driver, check, 'video_play_without_any_interruption_in_landscape', 'Potrait time')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_in_potrait')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_in_potrait')

    def video_play_without_any_interruption_in_potrait(self, driver):
        try:
            #             video_time_landscape = self.video_title_in_list_id
            VideoPage.video_start_time_portrait = self.get_video_start_time(driver)
            check = VideoPage.video_start_time_portrait >= VideoPage.video_start_time_landscape
            self.verify_true_or_false(driver, check, 'video_play_without_any_interruption_in_landscape', 'Potrait time')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_in_potrait')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_in_potrait')

    def open_subtopic_video_slider(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.video_auto_cancelBtn_id, 3):
                CommonMethods.elementClick(driver, self.video_auto_cancelBtn_id)
            CommonMethods.run('adb shell input touchscreen swipe 1272 400 600 400')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'open_subtopic_video_slider')
        except:
            CommonMethods.exception(driver, featureFileName, 'open_subtopic_video_slider')

    def get_video_start_time(self, driver):
        check = True
        time = None
        wait_count = 0
        try:
            while check and wait_count < 20:
                wait_count += 1
                CommonMethods.elementClick(driver, self.video_tab_videoframe)
                time = CommonMethods.getTextOfElement(driver, self.progressTime_id)
                if time is not None:
                    after_split = time.split(':')
                    minutes = int(after_split[0])
                    sec = int(after_split[1])
                    Total_sec = minutes * 60 + sec
                    check = False
                    return Total_sec
        except:
            logging.info('Problem in fetching start progression time')

    def get_video_title_on_player(self, driver):
        check = True
        title = None
        wait_count = 0
        try:
            while check and wait_count < 20:
                wait_count += 1
                CommonMethods.elementClick(driver, self.video_tab_videoframe)
                #                     time = self.get_element_text(driver, self.progressTime_id)
                title = CommonMethods.getTextOfElement(driver, self.video_title_on_player)
                if title is not None:
                    check = False
                    return title
        except:
            logging.info('Problem in fetching start progression time')

    def get_video_end_time(self, driver):
        check = True
        time = None
        wait_count = 0
        try:
            while check and wait_count < 20:
                wait_count += 1
                CommonMethods.elementClick(driver, self.video_tab_videoframe)
                #                     time = self.get_element_text(driver, self.progressTime_id)
                time = CommonMethods.getTextOfElement(driver, self.remaingTime_id)
                if time is not None:
                    after_split = time.split(':')
                    minutes = int(after_split[0])
                    sec = int(after_split[1])
                    Total_sec = minutes * 60 + sec
                    check = False
                    return Total_sec
        except:
            logging.info('Problem in fetching start progression time')

    def is_video_icon_present(self, driver, locator):
        check = True
        time = None
        wait_count = 0
        try:
            while check and wait_count < 10:
                wait_count += 1
                CommonMethods.elementClick(driver, self.video_tab_videoframe)
                icon = CommonMethods.wait_for_element_visible(driver, locator, 2)
                if icon == True:
                    check = False
                    return True
        except:
            return False
            logging.info('Error in searching for video icon')

    def click_on_video_icon(self, driver, locator):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 10:
                wait_count += 1
                CommonMethods.elementClick(driver, self.video_tab_videoframe)
                flag = CommonMethods.elementClick(driver, locator)
                if flag is True:
                    check = False
                    return True
        except:
            return False
            logging.info('Error in searching for video icon')

    def verify_autoloded_and_played(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                #                 self.wait_till_element_visible(driver, self.video_auto_play_btn)
                sleep(7)  # wait till the video is auto loaded
                self.wait_till_video_load(driver)
                Current_playing_actual = CommonMethods.getTextOfElement(driver, self.video_title_in_list_id)
                expected_video = self.get_text_of_video_in_list(driver, 2)
                check = Current_playing_actual == expected_video
                self.verify_true_or_false(driver, check, 'verify_autoloded_and_played', 'video played')
            elif device == 'tab':
                VideoPage.title_of_next_video = CommonMethods.getTextOfElement(driver, self.tab_video_next_video_title)
                sleep(7)
                self.wait_till_video_load(driver)
                expected_video = self.get_video_title_on_player(driver)
                check = VideoPage.title_of_next_video == expected_video
                self.verify_true_or_false(driver, check, 'verify_autoloded_and_played', 'next video verification')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_autoloded_and_played')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_autoloded_and_played')

    #

    #     def get_video_end_time(self, driver):
    #         check = True
    #         time = None
    #         wait_count = 0
    #         try:
    #             while check and wait_count < 10:
    #                 wait_count += 1
    #                 CommonMethods.elementClick(driver, self.video_tab_videoframe)
    #                 time = CommonMethods.getTextOfElement(driver, self.remaingTime_id)
    #                 if time is not None:
    #                     after_split = time.split(':')
    #                     minutes = int(after_split[0])
    #                     sec = int(after_split[1])
    #                     Total_sec = minutes*60 + sec
    #                     check = False
    #                     return Total_sec
    #         except:
    #             logging.info('Problem in fetching end progression time')

    """ Clicks on video close btn to see the video list in tab"""

    def click_on_video_player_list_btn(self, driver):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 10:
                wait_count += 1
                CommonMethods.elementClick(driver, self.video_tab_videoframe)
                CommonMethods.elementClick(driver, self.video_list_btn_tab)
                if CommonMethods.wait_for_element_visible(driver, self.video_list_close_btn_tab, 2):
                    check = False

        except:
            logging.info('Problem in Showing the Video List screen in tab')

    def verify_playingTxt_tag(self, driver, text):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                self.click_on_video_player_list_btn(driver)
                if CommonMethods.wait_for_element_visible(driver, self.video_list_close_btn_tab, 3):
                    #                     Playing text verification is not possible
                    pass


            elif device == 'mobile':
                check = CommonMethods.isElementPresent(driver, self.videoPlayingNow_xpath)
                if check == True:
                    pass
                else:
                    logging.info("Failed due to Element not visible in Method verify_playingTxt_tag")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_playingTxt_tag')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_playingTxt_tag')

    def video_should_highlighted(self, driver):
        try:
            check = False
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                title = self.get_video_title_on_player(driver)
                sleep(3)
                self.get_video_slider_window()
                elements_list = CommonMethods.getElements(driver, self.video_name_list)
                for i in range(len(elements_list)):
                    logging.info(elements_list[i].text)
                    if title == elements_list[i].text:
                        selected = elements_list[i].get_attribute("selected")
                        if selected == 'true':
                            check = True
                            logging.info(title + " is highlighted ")
                            break
            elif device == 'mobile':
                self.wait_till_autoload_completes(driver)
                CommonMethods.wait_for_element_visible(driver, self.video_title_in_list_id, 10)
                title = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_in_list_id)
                elements_list = CommonMethods.getElements(driver, self.video_name_list)
                for i in range(len(elements_list)):
                    logging.info(elements_list[i].text)
                    if title == elements_list[i].text:
                        selected = elements_list[i].get_attribute("selected")
                        if selected == 'true':
                            check = True
                            logging.info(title + " is highlighted ")
                            break
            self.verify_true_or_false(driver, check, "video_should_highlighted", "Highlight on Video List screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'video_should_highlighted')
        except:
            CommonMethods.exception(driver, featureFileName, 'video_should_highlighted')

    def verify_subtopic_videos(self, driver):
        try:
            check = False
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                elements_list = CommonMethods.getElements(driver, self.video_name_list)
                check = len(elements_list) >= 1
                self.verify_true_or_false(driver, check, 'verify_subtopic_videos', 'video lists')

            elif device == 'mobile':
                elements_list = CommonMethods.getElements(driver, self.video_name_list)
                check = len(elements_list) >= 1
                self.verify_true_or_false(driver, check, 'verify_subtopic_videos', 'video lists')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_subtopic_videos')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_subtopic_videos')

    def video_should_complete(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                #                 self.video_should_played(driver)
                #                 video_length = self.get_video_end_time(driver)
                self.select_short_video(driver)
                #                 self.wait_video_to_complete(driver, video_length)
                if CommonMethods.wait_for_element_visible(self, driver, self.video_play_btn, 3):
                    logging.info('Completed the Video Without any interaction')
                    return True
                else:
                    logging.info("Failed due to Element not visible in Method video_should_complete")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    return False
                    pytest.fail("Failed due to Element not visible in Video Page")
            elif device == 'mobile':
                #                 sleep(20)
                #                 CommonMethods.elementClick(driver, self.video1stLink_xpath)
                #                 videoLength = CommonMethods.getTextOfElement(driver, self.remaingTime_id)
                #                 videoLength = videoLength.split(':')
                #                 l1 = int(videoLength[0])*60
                #                 l2 = int(videoLength[1])+120
                #                 length = l1+l2
                #                 CommonMethods.elementClick(driver, self.video1stLink_xpath)
                #                 CommonMethods.wait_for_locator(driver, self.video_auto_cancelBtn_id,length)
                #                 check = CommonMethods.isElementPresent(driver, self.video_auto_cancelBtn_id)
                #                 if check == True:
                #                     CommonMethods.elementClick(driver,self.video_auto_cancelBtn_id)
                #                     pass
                #                 else:
                #                     logging.info("Failed due to Element not visible in Method video_should_complete")
                #                     CommonMethods.takeScreenShot(driver,featureFileName)
                #                     pytest.fail("Failed due to Element not visible in Video Page")
                self.wait_till_video_load(driver)
                end_time = self.get_video_end_time(driver)
                check = self.wait_till_video_complete(driver, end_time)
                self.verify_true_or_false(driver, check, 'video_should_complete', 'Auto cancel Button')
                return True
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'video_should_complete')

        except:
            CommonMethods.exception(driver, featureFileName, 'video_should_complete')

    def wait_video_to_complete(self, driver, wait_time):
        driver.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.wait_for_element_visible(driver, self.video_auto_cancelBtn_id,
                                                             1) and loading_count < wait_time + 100:
                loading_count += 1
                sleep(0.2)
        except:
            logging.info('Exception in Completing Videos')

    def select_short_video(self, driver):
        driver.implicitly_wait(0.1)
        list = []
        loading_count = 10
        try:
            while loading_count < 10:
                loading_count += 1
                ele = CommonMethods.getElements(self, driver, self.video_time_remaining)
                for i in len(ele):
                    ele_str = ele.text
                    res = (int(i) for i in ele_str.split() if i.isdigit())
                    list.append(res)

        except:
            logging.info('Exception in selecting the shortest video')

    def verify_start_time(self, driver):
        try:
            self.pause_video(driver)
            x, y = self.get_x_y_coordinate(driver, self.video_progressBar_id)
            CommonMethods.run('adb shell input tap {} {}'.format(x, y))
            start_time = self.get_video_start_time(driver)
            check = start_time == 0
            self.verify_true_or_false(driver, check, 'verify_start_time', 'video starting video')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_start_time')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_start_time')

    def verify_back_btn_in_subtopic_video_lst(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.video_tab_video_player_close_btn)
            self.verify_true_or_false(driver, check, 'verify_back_btn_in_subtopic_video_lst', 'video back btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_back_btn_in_subtopic_video_lst')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_back_btn_in_subtopic_video_lst')

    def verify_end_time(self, driver):
        try:
            end_time = self.get_video_end_time(driver)
            check = end_time > 0
            self.verify_true_or_false(driver, check, 'verify_start_time', 'video starting video')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_end_time')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_end_time')

    def tap_forward(self, driver):
        try:
            sleep(20)
            self.videoProgressTimeBfr = self.get_video_start_time(driver)
            self.click_on_video_icon(driver, self.ten_sec_fwd_btn_id)
            self.videoProgressTimeAfter = self.get_video_start_time(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_forward')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_forward')

    def tap_backward_10sec(self, driver):
        try:
            sleep(20)
            self.videoProgressTimeBfr = self.get_video_start_time(driver)
            self.click_on_video_icon(driver, self.ten_sec_bkwd_btn_id)
            self.videoProgressTimeAfter = self.get_video_start_time(driver)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_backward_10sec')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_backward_10sec')

    def verify_fwrd_time(self, driver):
        try:
            startTime = self.videoProgressTimeBfr
            stopTime = self.videoProgressTimeAfter
            if stopTime >= startTime:
                logging.info("Verified video 10 sec forward")
            else:
                logging.info("Failed Locator in Method verify_fwrd_time")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_fwrd_time')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_fwrd_time')

    def verify_backward_10sec(self, driver):
        try:
            startTime = self.videoProgressTimeBfr
            stopTime = self.videoProgressTimeAfter
            if stopTime < startTime:
                logging.info("Verified video 10 sec backward")
            else:
                logging.info("Failed Locator in Method verify_backward_10sec")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_backward_10sec')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_backward_10sec')

    def tap_on_practice_card(self, driver):
        try:
            CommonMethods.scrollToElementAndClick(driver, 'Start Practice')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_practice_card')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_practice_card')

    def progress_till_video_play(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.practice_start_practice_btn, 3):
                CommonMethods.elementClick(driver, self.practice_start_practice_btn)
                sleep(7)
                CommonMethods.elementClick(driver, self.practice_continue_btn)
                self.wait_for_video_in_practice(driver)
                CommonMethods.elementClick(driver, self.practice_continue_btn)
                self.pause_video(driver)
                check = CommonMethods.wait_for_element_visible(driver, self.video_settingIcon_id, 3)
                self.verify_false(driver, check, 'progress_till_video_play', 'setting icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'progress_till_video_play')
        except:
            CommonMethods.exception(driver, featureFileName, 'progress_till_video_play')

    def verify_setting_icon_not_seen(self, driver):
        try:
            self.pause_video(driver)
            check = CommonMethods.wait_for_element_visible(driver, self.video_settingIcon_id, 3)
            self.verify_false(driver, check, 'progress_till_video_play', 'setting icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_setting_icon_not_seen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_setting_icon_not_seen')

    def verify_video_screen(self, driver):
        try:
            self.pause_video(driver)
            check = CommonMethods.wait_for_element_visible(driver, self.video_title_on_player, 3)
            self.verify_true_or_false(driver, check, 'verify_video_screen', 'video frame')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_screen')

    def verify_video_title(self, driver):
        try:
            self.pause_video(driver)
            check = CommonMethods.wait_for_element_visible(driver, self.video_title_on_player, 5)
            self.verify_true_or_false(driver, check, 'verify_video_title', 'video Title')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_title')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_title')

    def verify_video_is_not_paused(self, driver):
        try:
            check = self.is_video_icon_present(driver, self.video_pause_btn_id)
            self.verify_true_or_false(driver, check, 'verify_video_title', 'video Title')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_title')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_title')

    def wait_for_video_in_practice(self, driver):
        driver.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.wait_for_element_visible(driver, self.practice_continue_btn,
                                                             2) and loading_count < 75:
                loading_count += 1
                CommonMethods.elementClick(driver, self.practice_2nd_answer)
                if CommonMethods.wait_for_element_visible(driver, self.practice_submit_btn, 5):
                    CommonMethods.elementClick(driver, self.practice_submit_btn)
                    if CommonMethods.wait_for_element_visible(driver, self.practice_submit_btn, 5):
                        CommonMethods.elementClick(driver, self.practice_submit_btn)
                    elif CommonMethods.wait_for_element_visible(driver, self.practice_continue_btn, 5):
                        logging.info("found video in practice")
                elif CommonMethods.wait_for_element_visible(driver, self.practice_start_practice_btn,
                                                            5) or CommonMethods.wait_for_element_visible(driver,
                                                                                                         self.video_badge_close_btn,
                                                                                                         5):
                    CommonMethods.elementClick(driver, self.video_badge_close_btn)
                    CommonMethods.elementClick(driver, self.practice_start_practice_btn)
        except:
            logging.info('Error in finding the video')

    #     def verify_video_in_potrait(self,driver):
    #         try:
    #             sleep(20)
    #             orientation = CommonMethods.get_screen_orientation(driver)
    #             CommonMethods.elementClick(driver, self.videoPlayingNow_xpath)
    #             sleep(5)
    #             startProgress_time = CommonMethods.getTextOfElement(driver, self.progressTime_id)
    #             CommonMethods.elementClick(driver, self.videoPlayingNow_xpath)
    #             sleep(10)
    #             CommonMethods.elementClick(driver, self.videoPlayingNow_xpath)
    #             sleep(5)
    #             endProgress_time = CommonMethods.getTextOfElement(driver, self.progressTime_id)
    #             start_time = startProgress_time.split(':')
    #             end_time = endProgress_time.split(':')
    #             start =int(start_time[1])
    #             stop = int(end_time[1])
    #             if orientation == 'PORTRAIT' and start < stop:
    #                 pass
    #             else:
    #                 logging.info("Failed Locator in Method verify_video_in_potrait")
    #                 CommonMethods.takeScreenShot(driver,featureFileName)
    #                 pytest.fail("Failed Due to Locator in Video Page")
    #         except NoSuchElementException:
    #             CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_video_in_potrait')
    #
    #         except :
    #             CommonMethods.exception(driver,featureFileName,'verify_video_in_potrait')
    def verify_video_in_landscape(self, driver):
        try:
            sleep(3)
            orientation = CommonMethods.get_screen_orientation(driver)
            loc = CommonMethods.get_element_location(driver, self.video_play_btn)
            x = loc["x"]
            y = loc["y"]
            startProgress_time = CommonMethods.getTextOfElement(driver, self.progressTime_id)
            CommonMethods.elementClick(driver, self.video_play_btn)
            sleep(10)
            # for i in range(1,6):
            CommonMethods.run('adb shell input tap {} {}'.format(x, y))
            CommonMethods.run('adb shell input tap {} {}'.format(x, y))
            # if CommonMethods.isElementPresent(driver, self.video_pause_btn_id):
            #     break
            endProgress_time = CommonMethods.getTextOfElement(driver, self.progressTime_id)
            start_time = startProgress_time.split(':')
            end_time = endProgress_time.split(':')
            start = int(start_time[1])
            stop = int(end_time[1])
            if orientation == 'LANDSCAPE' and start < stop:
                pass
            else:
                logging.info("Failed Locator in Method verify_video_in_landscape")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_in_landscape')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_in_landscape')

    def select_topic(self, driver, topic, chapter):
        try:
            CommonMethods.scrollToElement(driver, chapter)
            sleep(2)
            topic_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + topic + "\']")
            sub_chapter_xpath = (By.XPATH,
                                 "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.RelativeLayout//android.widget.TextView[@text=\'" + chapter + "\']//parent::android.widget.RelativeLayout//following::androidx.recyclerview.widget.RecyclerView")
            video_count = (By.XPATH,
                           "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.RelativeLayout//android.widget.TextView[@text=\'" + chapter + "\']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/video_count']")
            swipe_count = CommonMethods.get_swipe_count(driver, video_count)
            swipe_count = int(swipe_count[0])
            logging.info(swipe_count)
            CommonMethods.select_topic(driver, sub_chapter_xpath, topic_xpath, swipe_count)
            sleep(3)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'select_topic')

        except:
            CommonMethods.exception(driver, featureFileName, 'select_topic')

    def verify_video_chapter_name(self, driver, chapter):
        try:
            actual_text = CommonMethods.getTextOfElement(driver, self.video_chapter_name_id)
            expected_text = chapter
            check = CommonMethods.verifyTwoText(actual_text, expected_text)
            if check == True:
                pass
            else:
                logging.info("Failed Locator in Method verify_video_chapter_name")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_chapter_name')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_chapter_name')

    def verify_video_subtitle_name(self, driver, title):
        try:
            actual_text = CommonMethods.getTextOfElement(driver, self.video_title_in_list_id)
            expected_text = title
            check = CommonMethods.verifyTwoText(actual_text, expected_text)
            if check == True:
                logging.info('verified the video playing')
            else:
                logging.info("Failed Locator in Method verify_video_subtitle_name")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_subtitle_name')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_subtitle_name')

    def verify_list_view(self, driver):
        try:
            ele_list = CommonMethods.getElements(driver, self.video_list_view_id)
            for ele in ele_list:
                check = CommonMethods.isElementDisplayed(driver, ele)
                if check == True:
                    pass
                else:
                    logging.info("Failed Locator in Method verify_list_view")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_list_view')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_list_view')

    def verify_video_name(self, driver):
        try:
            sleep(15)
            video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_in_list_id)
            video_title = "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName' and @text = \'" + video_title_name + "\']"
            video_title_xapth = (By.XPATH, video_title)
            check = CommonMethods.isElementPresent(driver, video_title_xapth)
            self.verify_true_or_false(driver, check, 'verify_video_name', 'video name')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_name')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_name')

    def verify_video_thumbnail(self, driver):
        try:
            video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_in_list_id)
            video_thumbnail = (By.XPATH,
                               "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName' and @text =\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/thumbnail']")
            check = CommonMethods.isElementPresent(driver, video_thumbnail)
            self.verify_true_or_false(driver, check, 'verify_video_thumbnail', 'video thumbnail')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_thumbnail')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_thumbnail')

    def verify_video_duration(self, driver):
        try:
            video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_in_list_id)
            sleep(2)
            video_title = (By.XPATH,
                           "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
            if CommonMethods.isElementPresent(driver, video_title):
                CommonMethods.elementClick(driver, self.video1stLink_xpath)
            sleep(3)
            duration = CommonMethods.getAttributeOfElement(driver, 'text', video_title)
            check = duration.__contains__('min')
            self.verify_true_or_false(driver, check, 'verify_video_duration', 'video duration')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_duration')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_duration')

    def verify_video_progress(self, driver):
        try:
            video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_in_list_id)
            video_progress = (By.XPATH,
                              "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.ProgressBar")
            if CommonMethods.isElementPresent(driver, video_progress):
                pass
            else:
                logging.info("Failed Locator in Method verify_video_progress")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_progress')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_progress')

    def verify_min_completed(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_on_player)
                sleep(2)
                video_title = (By.XPATH,
                               "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
                duration = CommonMethods.getAttributeOfElement(driver, 'text', video_title)
                check = duration.__contains__('min | Completed')
                if check == True:
                    logging.info('xx and completed in video is verified')
                else:
                    logging.info("Failed Locator in Method verify_min_completed")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            elif device == 'mobile':
                video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_in_list_id)
                sleep(2)
                video_title = (By.XPATH,
                               "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
                duration = CommonMethods.getAttributeOfElement(driver, 'text', video_title)
                check = duration.__contains__('min | Completed')
                if check == True:
                    logging.info('xx and completed in video is verified')
                else:
                    logging.info("Failed Locator in Method verify_min_completed")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_min_completed')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_min_completed')

    def verify_progression_100_percent(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_on_player)
                sleep(2)
                progression_percent = (By.XPATH,
                                       "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.ProgressBar[@resource-id='com.byjus.thelearningapp.premium:id/video_progress_view']")
                percent = CommonMethods.getAttributeOfElement(driver, 'text', progression_percent)
                check = percent.__contains__('100')
                if check == True:
                    logging.info('Progress is 100% percent')
                else:
                    logging.info("Failed Locator in Method verify_progression_100_percent")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            elif device == 'mobile':
                video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_in_list_id)
                sleep(2)
                progression_percent = (By.XPATH,
                                       "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.ProgressBar[@resource-id='com.byjus.thelearningapp.premium:id/video_progress_view']")
                percent = CommonMethods.getAttributeOfElement(driver, 'text', progression_percent)
                check = percent.__contains__('100')
                if check == True:
                    logging.info('Progress is 100% percent')
                else:
                    logging.info("Failed Locator in Method verify_progression_100_percent")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_progression_100_percent')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_progression_100_percent')

    def tap_on_same_video(self, driver):
        try:
            sleep(2)
            video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_in_list_id)
            video_title = "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName' and @text = \'" + video_title_name + "\']"
            video_title_xapth = (By.XPATH, video_title)
            check = CommonMethods.wait_for_element_visible(driver, video_title_xapth, 3)
            if check == True:
                CommonMethods.elementClick(driver, video_title_xapth)
                logging.info('Clicked on same video')
            else:
                logging.info("Failed Locator in Method tap_on_same_video")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_same_video')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_same_video')

    def verify_video_where_it_stopped(self, driver):
        try:
            video_time_before = self.videoProgressTimeBfr
            video_time_after = self.get_element_text(driver, self.videoProgressTimeBfr)
            check1 = self.is_video_icon_present(driver, self.video_pause_btn_id)
            check2 = video_time_after == video_time_before or video_time_after

        #             else:
        #                 logging.info("Failed Locator in Method tap_on_same_video")
        #                 CommonMethods.takeScreenShot(driver,featureFileName)
        #                 pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_same_video')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_same_video')

    def verify_pause_btn(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 5)
            if check is True:
                time = CommonMethods.getTextOfElement(driver, self.progressTime_id)
                after_split = time.split(':')
                minutes = int(after_split[0])
                sec = int(after_split[1])
                Total_sec = minutes * 60 + sec
                VideoPage.videoProgressTimeBfr = Total_sec
                logging.info('Pause btn is verified')
            else:
                logging.info("Failed Locator in Method verify_pause_btn")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_pause_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_pause_btn')

    """This method will tap on pause btn in video player when video is playing"""

    def tap_pause_btn(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 3):
                logging.info('video is paused in video Player')
            else:
                sleep(2)
                self.pause_video(driver)
                logging.info('video is paused in video Player')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_pause_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_pause_btn')

    #     def tap_pause_btn(self, driver):
    #         try:
    #             if CommonMethods.isElementPresent(driver,self.videoPlayBtn_id):
    #                 pass
    #             else:
    #                 sleep(3)
    #                 video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_id)
    #                 video_title = "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName' and @text = \'" + video_title_name + "\']"
    #                 video_title_xapth = (By.XPATH, video_title)
    #                 CommonMethods.elementClick(driver,video_title_xapth)
    #         except NoSuchElementException:
    #             CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_pause_btn')
    #
    #         except:
    #             CommonMethods.exception(driver, featureFileName, 'tap_pause_btn')

    def verify_video_resumed_from_same_point(self, driver):
        try:
            self.wait_till_video_load(driver)
            videoProgressTimeAfter = self.get_video_start_time(driver)
            check = self.is_video_icon_present(driver, self.video_pause_btn_id)
            self.verify_true_or_false(driver, check, 'verify_video_resumed_from_same_point', 'Pause Btn')
            if videoProgressTimeAfter >= VideoPage.videoProgressTimeBfr:
                logging.info('Video is played and resumed from where it is stopped')
            else:
                sleep(3)
                video_title_name = CommonMethods.getAttributeOfElement(driver, 'text', self.video_title_in_list_id)
                video_title = "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName' and @text = \'" + video_title_name + "\']"
                video_title_xapth = (By.XPATH, video_title)
                CommonMethods.elementClick(driver, video_title_xapth)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_resumed_from_same_point')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_resumed_from_same_point')

    def verify_video_size_40_percent(self, driver):
        try:
            #             window_height = CommonMethods.get_window_height(driver)
            window_height = driver.get_window_size()
            video_frame_height = CommonMethods.getElement(driver, self.video_video_frame_id).size
            percent = (video_frame_height["height"] / window_height["height"]) * 100
            if percent > 30 and percent < 50:
                logging.info('Video is playing in 40% screen')
            else:
                logging.info("Failed Locator in Method verify_video_size_40_percent")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_size_40_percent')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_size_40_percent')

    def switch_to_grade(self, driver, grade):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                CommonMethods.elementClick(driver, self.back_button_id)
                CommonMethods.wait_for_locator(driver, self.profile_name_hamburger, 5)
                CommonMethods.elementClick(driver, self.profile_name_hamburger)
                selected_grade = CommonMethods.getTextOfElement(driver, self.video_grade_selection_btn)
                if selected_grade == grade:
                    CommonMethods.click_on_device_back_btn(driver)
                else:
                    CommonMethods.wait_for_element_visible(driver, self.video_grade_selection_btn, 5)
                    CommonMethods.elementClick(driver, self.video_grade_selection_btn)
                    self.select_grade(driver, grade)
                    sleep(5)
                    CommonMethods.click_on_device_back_btn(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'switch_to_grade')

        except:
            CommonMethods.exception(driver, featureFileName, 'switch_to_grade')

    def select_grade(self, driver, grade):
        driver.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.findText(driver, grade) and loading_count < 15:
                loading_count += 1
                length = len(CommonMethods.getElements(driver, self.video_grades_elements))
                x1, y1 = self.get_elements_coordinates(driver, self.video_grades_elements, length)
                x2, y2 = self.get_elements_coordinates(driver, self.video_grades_elements, 1)
                CommonMethods.run('adb shell input swipe {} {} {} {}'.format(x1, y1, x2, y2))
            if CommonMethods.findText(driver, grade):
                grade_txt = "//android.widget.TextView[@text = \'" + grade + "\']"
                sel_grade = (By.XPATH, grade_txt)
                CommonMethods.elementClick(driver, sel_grade)
                logging.info('selected grade ' + grade)
            else:
                logging.info('error in selecting the grade')
        except:
            logging.error('Error in playing the video completely')

    def verify_subtopic_name(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.video_title_in_list_id)
            if check == True:
                logging.info('Sub title name is present')
            else:
                logging.info("Failed Locator in Method verify_subtopic_name")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_subtopic_name')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_subtopic_name')

    def verify_share_bookmerks_icon(self, driver):
        try:
            check1 = CommonMethods.isElementPresent(driver, self.video_share_icon_id)
            check2 = CommonMethods.isElementPresent(driver, self.video_bookmark_icon_id)
            if check1 and check2:
                logging.info('share bookmark is present')
            else:
                logging.info("Failed Locator in Method verify_share_bookmerks_icon")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_share_bookmerks_icon')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_share_bookmerks_icon')

    def verify_topic_videos(self, driver):
        try:
            ele = CommonMethods.getElements(driver, self.video_topic_videos_id)
            if len(ele) > 2:
                pass
            else:
                logging.info("Failed Locator in Method verify_topic_videos")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_topic_videos')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_topic_videos')

    def verify_card_lnk(self, driver, card):
        try:
            lnk_name = (By.XPATH, "//android.widget.TextView[@text=\'" + card + "\']")
            CommonMethods.scrollToElement(driver, card)
            check = CommonMethods.isElementPresent(driver, lnk_name)
            if check == True:
                pass
            else:
                logging.info("Failed Locator in Method verify_card_lnk")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_card_lnk')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_card_lnk')

    def verify_chapter_name_color(self, driver):
        try:
            ele = CommonMethods.getElement(driver, self.video_title_in_list_id)
            # str = ele.getCssValue("color")
            check = False
            if check == True:
                pass
            else:
                logging.info("Failed Locator in Method verify_chapter_name_color")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_chapter_name_color')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_chapter_name_color')

    def video_progression(self, driver):
        try:
            check = self.is_video_icon_present(driver, self.video_progress_tab_id)
            self.verify_true_or_false(driver, check, 'video_progression', 'video progression')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'video_progression')
        except:
            CommonMethods.exception(driver, featureFileName, 'video_progression')

    def verify_video_stopped_loading_next_video(self, driver):
        try:
            check1 = CommonMethods.wait_for_element_visible(driver, self.video_play_next_btn, 3)
            check2 = CommonMethods.wait_for_element_visible(driver, self.video_play_previous_btn, 3)
            check = check1 or check2
            self.verify_true_or_false(driver, check, 'video_progression', 'video progression')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_stopped_loading_next_video')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_stopped_loading_next_video')

    def verify_chapter_name_color_with_subject_theme(self, driver):
        try:
            css_data = driver.find_element_by_id(
                'com.byjus.thelearningapp.premium:id/video_title_2').value_of_css_property("style")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_chapter_name_color_with_subject_theme')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_chapter_name_color_with_subject_theme')

    # Video Utility methods
    def verify_true_or_false(self, driver, check, method_name, ele_name):
        if check == True:
            logging.info('The ' + ele_name + ' is present on screen')
        else:
            logging.info("Failed due to Element not visible in " + method_name)
            CommonMethods.takeScreenShot(driver, featureFileName)
            pytest.fail("Failed due to Element not visible in Video Page")

    def verify_false(self, driver, check, method_name, ele_name):
        if check == False:
            logging.info('The ' + ele_name + ' is not present on screen')
        else:
            logging.info("Failed due to Element not visible in " + method_name)
            CommonMethods.takeScreenShot(driver, featureFileName)
            pytest.fail("Failed due to Element not visible in Video Page")

    def test_fail(self, driver, method_name):
        logging.info("Failed in " + method_name)
        CommonMethods.takeScreenShot(driver, featureFileName)
        pytest.fail("Failed in Video Page")

    def verify_video_is_playing(self, driver, frame):
        check = True
        time = None
        wait_count = 0
        try:
            while check and wait_count < 10:
                wait_count += 1
                CommonMethods.elementClick(driver, self.video_tab_videoframe)
                time = CommonMethods.getTextOfElement(driver, self.progressTime_id)
                if time is not None:
                    after_split = time.split(':')
                    minutes = int(after_split[0])
                    sec = int(after_split[1])
                    Total_sec = minutes * 60 + sec
                    check = False
                    return Total_sec
        except:
            logging.info('Problem in fetching start progression time')

    '''Only for video Scenarios'''

    def get_element_text(self, driver, locator):
        txt = None
        try:
            ele = driver.find_element(locator)
            txt = ele.text()
            if txt is not None:
                return txt
            else:
                return None
        except:
            return None

    def tap_on_first_video_lnk_and_complete(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                sleep(3)  # wait till the video start loading
                self.wait_till_video_load(driver)
                #                 self.start_the_video(driver)
                self.tap_on_first_video_lnk(driver)
                self.wait_till_video_load(driver)
                self.pause_video(driver)
                self.end_the_video(driver)
                self.wait_till_video_load(driver)
                self.play_video(driver)
                flag = CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 30)
            elif device == 'tab':
                sleep(3)  # wait till the video start loading
                self.wait_till_video_load(driver)
                self.start_the_video(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_first_video_lnk_and_complete')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_first_video_lnk_and_complete')

    def tap_on_first_video_lnk(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.video1stLink_xpath, 3):
                CommonMethods.elementClick(driver, self.video1stLink_xpath)
            self.wait_till_video_load(driver)
            self.pause_video(driver)
            x, y = self.get_x_y_coordinate(driver, self.video_progressBar_id)
            CommonMethods.run('adb shell input tap {} {}'.format(x, y))
            self.wait_till_video_load(driver)
            self.click_on_video_icon(driver, self.video_play_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_first_video_lnk')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_first_video_lnk')

    def turn_off_auto_play(self, driver):
        try:
            self.wait_till_video_load(driver)
            self.pause_video(driver)
            #             self.tap_on_video_player_icon(driver, self.video_settingIcon_id)
            CommonMethods.elementClick(driver, self.video_settingIcon_id)
            CommonMethods.wait_for_element_visible(driver, self.video_auto_enable_switch, 5)
            status = CommonMethods.getAttributeOfElement(driver, 'checked', self.video_auto_enable_switch)
            if CommonMethods.wait_for_element_visible(driver, self.video_auto_enable_switch, 3):
                if status == 'false':
                    VideoPage.auto_play_switch_color = self.get_the_rgb_lst(driver, self.video_auto_enable_switch)
                    logging.info('Autoplay is disable')
                    CommonMethods.click_on_device_back_btn(driver)
                elif status == 'true':
                    CommonMethods.elementClick(driver, self.video_auto_enable_switch)
                    VideoPage.auto_play_switch_color = self.get_the_rgb_lst(driver, self.video_auto_enable_switch)
                    CommonMethods.click_on_device_back_btn(driver)
            else:
                logging.info('Error in getting Auto play option screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'turn_off_autoplay')

        except:
            CommonMethods.exception(driver, featureFileName, 'turn_off_autoplay')

    def turn_on_auto_play(self, driver):
        try:
            self.wait_till_video_load(driver)
            #             self.pause_video(driver)
            self.tap_on_video_player_icon(driver, self.video_pause_btn_id)
            x, y = self.get_x_y_coordinate(driver, self.video_progressBar_id)
            CommonMethods.run('adb shell input tap {} {}'.format(x, y))
            #             self.pause_video(driver)
            self.tap_on_video_player_icon(driver, self.video_pause_btn_id)
            CommonMethods.elementClick(driver, self.video_settingIcon_id)
            CommonMethods.wait_for_element_visible(driver, self.video_auto_enable_switch, 5)
            status = CommonMethods.getAttributeOfElement(driver, 'checked', self.video_auto_enable_switch)
            if CommonMethods.wait_for_element_visible(driver, self.video_auto_enable_switch, 3):
                if status == 'true':
                    VideoPage.auto_play_switch_color = self.get_the_rgb_lst(driver, self.video_auto_enable_switch)
                    logging.info('Autoplay is enabled')
                    CommonMethods.click_on_device_back_btn(driver)
                elif status == 'false':
                    CommonMethods.elementClick(driver, self.video_auto_enable_switch)
                    VideoPage.auto_play_switch_color = self.get_the_rgb_lst(driver, self.video_auto_enable_switch)
                    CommonMethods.click_on_device_back_btn(driver)
            else:
                logging.info('Error in getting Auto play option screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'turn_on_auto_play')

        except:
            CommonMethods.exception(driver, featureFileName, 'turn_on_auto_play')

    def verify_purple_color(self, driver):
        try:
            purple_color = {"#6a4ac7"}
            check = purple_color.issubset(VideoPage.auto_play_switch_color)
            self.verify_true_or_false(driver, check, 'verify_purple_color', "Auto Play toggle button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_purple_color')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_purple_color')

    def verify_grey_color(self, driver):
        try:
            grey_color = {"#ececec", "#b2b2b2"}
            check = grey_color.issubset(VideoPage.auto_play_switch_color)
            self.verify_true_or_false(driver, check, 'verify_grey_color', "Auto Play toggle button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_grey_color')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_grey_color')

    def verify_video_player_previous_btn(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.video_play_previous_btn, 3)
            self.verify_false(driver, check, 'verify_video_player_previous_btn', 'previous Btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_player_previous_btn')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_player_previous_btn')

    def verify_video_player_previous_cancel_btn(self, driver):
        try:
            """Works for both mobile and tab"""
            check1 = CommonMethods.wait_for_element_visible(driver, self.video_up_next, 3)
            check2 = CommonMethods.wait_for_element_visible(driver, self.video_video_player_chapter_txt, 3)
            check3 = CommonMethods.wait_for_element_visible(driver, self.video_auto_cancelBtn_id, 3)
            self.verify_false(driver, check1, 'verify_video_player_previous_cancel_btn', 'video up next')
            self.verify_false(driver, check2, 'verify_video_player_previous_cancel_btn', 'chapter text')
            self.verify_false(driver, check3, 'verify_video_player_previous_cancel_btn', 'Cancel Btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_player_previous_cancel_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_player_previous_cancel_btn')

    def verify_video_player_next_btn(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.video_play_next_btn, 5)
            self.verify_true_or_false(driver, check, 'verify_video_player_next_btn', 'Next Btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_player_next_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_player_next_btn')

    def verify_video_player_next_btn_not_present(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.video_play_next_btn, 5)
            self.verify_false(driver, check, 'verify_video_player_next_btn_not_present', 'Next Btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_player_next_btn_not_present')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_player_next_btn_not_present')

    def tap_on_reply_icon(self, driver):
        try:
            sleep(2)
            check = CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 3)
            VideoPage.video_sub_title_name = CommonMethods.getTextOfElement(driver, self.video_title)
            if check == True:
                CommonMethods.elementClick(driver, self.video_play_btn)
                logging.info('clicked on auto replay icon')
            else:
                logging.info("Failed due to Element not visible in tap_on_reply_icon")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_player_next_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_player_next_btn')

    def verify_reply_icon(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.video_play_btn)
            self.verify_true_or_false(driver, check, 'verify_reply_icon', "Reply Button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_reply_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_reply_icon')

    """" This is used to verify whether the next arrow icon is there or not"""

    def verify_play_next_icon(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.video_play_next_btn)
            self.verify_true_or_false(driver, check, 'verify_play_next_icon', "play next Button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_play_next_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_play_next_icon')

    """"This is used to verify the current video name on the video Player"""

    def verify_current_video_name(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                actual = CommonMethods.getTextOfElement(driver, self.mob_video_title_on_player)
                expected = CommonMethods.getTextOfElement(driver, self.video_title_in_list_id)
                check = CommonMethods.verifyTwoText(actual, expected)
                self.verify_true_or_false(driver, check, 'verify_current_video_name', "title on player matches")
            elif device == 'tab':
                actual = CommonMethods.getTextOfElement(driver, self.video_title_on_player)
                expected = CommonMethods.getTextOfElement(driver, self.video_title_in_list_id)
                check = CommonMethods.verifyTwoText(actual, expected)
                self.verify_true_or_false(driver, check, 'verify_current_video_name', "title on player matches")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_current_video_name')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_current_video_name')

    """This method tap on last link in video list lay"""

    def tap_on_last_video_in_list(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                self.click_on_video_last_lnk(driver)
            elif device == 'tab':
                self.click_on_video_last_lnk(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_last_video_in_list_and_complete')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_last_video_in_list_and_complete')

    def complete_video(self, driver):
        try:
            self.wait_till_video_load(driver)
            #             self.pause_video(driver)
            self.tap_on_video_player_icon(driver, self.video_pause_btn_id)
            self.end_the_video(driver)
            self.tap_on_video_player_icon(driver, self.video_play_btn)
            check = CommonMethods.wait_for_element_visible(driver, self.video_play_btn,
                                                           60) or CommonMethods.wait_for_element_visible(driver,
                                                                                                         self.video_frame_pause_btn,
                                                                                                         60) or CommonMethods.wait_for_element_visible(
                driver, self.video_auto_cancelBtn_id, 60)
            self.verify_true_or_false(driver, check, 'complete_video', 'Play Btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'complete_video')
        except:
            CommonMethods.exception(driver, featureFileName, 'complete_video')

    def check_for_alerts(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.video_badge_close_btn, 4):
                CommonMethods.elementClick(driver, self.video_badge_close_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'complete_video')
        except:
            CommonMethods.exception(driver, featureFileName, 'complete_video')

    def seek_video_50_percent(self, driver):
        try:
            self.wait_till_video_load(driver)
            self.pause_video(driver)
            CommonMethods.run('adb shell input tap 612 770')
            VideoPage.video_start_time = self.get_video_start_time(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'seek_video_50_percent')
        except:
            CommonMethods.exception(driver, featureFileName, 'seek_video_50_percent')

    def verify_video_play_from_left(self, driver):
        try:
            self.play_video(driver)
            actual_time = self.get_video_start_time(driver)
            expected_time = VideoPage.video_start_time
            check = actual_time > expected_time
            self.verify_true_or_false(driver, check, 'verify_video_play_from_left', 'video time')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_play_from_left')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_play_from_left')

    def wait_till_autoload_completes(self, driver):
        try:
            VideoPage.next_video_title = CommonMethods.getTextOfElement(driver, self.video_next_video_title)
            CommonMethods.wait_for_element_visible(driver, self.video_auto_play_btn, 5)
            sleep(7)  # till the auto load completes
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'wait_till_autoload_completes')
        except:
            CommonMethods.exception(driver, featureFileName, 'wait_till_autoload_completes')

    def Complete_the_video_till_end(self, driver):
        try:
            self.wait_till_video_load(driver)
            self.pause_video(driver)
            self.end_the_video(driver)
            self.play_video(driver)
            check = CommonMethods.wait_for_element_visible(driver, self.video_auto_cancelBtn_id, 60)
            if check == True:
                CommonMethods.elementClick(driver, self.video_auto_cancelBtn_id)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'Complete_the_video_till_end')

        except:
            CommonMethods.exception(driver, featureFileName, 'Complete_the_video_till_end')

    def click_on_video_last_lnk(self, driver):
        try:
            CommonMethods.scrollToElement(driver, 'Practice')
            ele = CommonMethods.getElements(driver, self.video_play_list_elements)
            size = len(ele)
            ele[size - 1].click()
        except:
            logging.info('Error in clicking on last video link')

    def tap_on_2nd_video_lnk_and_complete(self, driver):
        try:
            self.click_on_2nd_video_lnk(driver)
            self.wait_till_video_load(driver)
            self.end_the_video(driver)
            self.wait_till_video_load(driver)
            self.play_video(driver)
            flag = CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 30)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_last_video_in_list_and_complete')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_last_video_in_list_and_complete')

    def get_index_of_the_playing_video(self, driver):
        try:
            ele = CommonMethods.getElements(driver, self.video_play_list_elements)
            for i in range(len(ele)):
                element = ele[i]
                check = element.get_attribute('selected')
                if check == 'true':
                    return i + 1  # index starts with zero so we are adding 1
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_last_video_in_list_and_complete')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_last_video_in_list_and_complete')

    def tap_on_second_video_lnk(self, driver):
        try:
            self.click_on_2nd_video_lnk(driver)
            self.wait_till_video_load(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_second_video_lnk')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_second_video_lnk')

    def get_text_of_video_in_list(self, driver, position):
        ele = CommonMethods.getElements(driver, self.video_play_list_elements)
        videoName = ele[position - 1].text
        return videoName

    def click_on_2nd_video_lnk(self, driver):
        try:
            ele = CommonMethods.getElements(driver, self.video_play_list_elements)
            ele[1].click()
        except:
            logging.info('Error in clicking on 2nd video link')

    def click_on_1st_video_lnk(self, driver):
        try:
            ele = CommonMethods.getElements(driver, self.video_play_list_elements)
            ele[0].click()
        except:
            logging.info('Error in clicking on 1st video link')

    def get_elements_coordinates(self, driver, locator, position):
        try:
            ele = CommonMethods.getElements(driver, locator)
            element = ele[position - 1]
            loc = element.location
            x = loc["x"]
            y = loc["y"]
            return x, y
        except:
            logging.info('Error in getting coordinate of the element')

    def get_text_of_video_lnk(self, driver, position):
        try:
            ele = CommonMethods.getElements(driver, self.video_play_list_elements)
            element_txt = ele[position - 1].text
            return element_txt
        except:
            logging.info('Error in getting the video ele link')

    def verify_auto_loading_not_present(self, driver):
        try:
            """Works for both mobile and tab"""
            check = CommonMethods.wait_for_element_visible(driver, self.video_auto_play_btn, 3)
            self.verify_false(driver, check, 'verify_auto_loading_not_present', 'auto play')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_auto_loading_not_present')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_auto_loading_not_present')

    def verify_reply_icon_is_shown(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 3)
            self.verify_true_or_false(driver, check, 'verify_reply_icon_is_shown', 'reply icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_reply_icon_is_shown')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_reply_icon_is_shown')

    def verify_previour_next_icon_is_shown(self, driver):
        try:
            check1 = CommonMethods.wait_for_element_visible(driver, self.video_play_next_btn, 3)
            self.verify_true_or_false(driver, check1, 'verify_previour_next_icon_is_shown', 'next icon')
            check2 = CommonMethods.wait_for_element_visible(driver, self.video_play_previous_btn, 3)
            self.verify_true_or_false(driver, check2, 'verify_previour_next_icon_is_shown', 'previous icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_previour_next_icon_is_shown')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_previour_next_icon_is_shown')

    def end_the_video(self, driver):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1
                #                 self.pause_video(driver)
                x1, y1, x2, y2 = self.get_element_coordinates(driver, self.video_progressBar_id)
                x2 = x2 - 33
                y2 = y2 - 22
                CommonMethods.run('adb shell input tap {} {}'.format(x2, y2))
                #                 CommonMethods.run('adb shell input touchscreen swipe {} {} {} {}'.format(x1,y2,x2, y2))
                check = not True
        except:
            logging.info("Error in ending the video")

    def start_the_video(self, driver):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1
                #                 self.pause_video(driver)
                x1, y1, x2, y2 = self.get_element_coordinates(driver, self.video_progressBar_id)
                CommonMethods.run('adb shell input tap {} {}'.format(x1, y1))
                #                 CommonMethods.run('adb shell input touchscreen swipe {} {} {} {}'.format(x1,y2,x2, y2))
                check = not True
        except:
            logging.info("Error in ending the video")

    def end_till_cancel_btn(self, driver):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1
                self.pause_video(driver)
                x1, y1, x2, y2 = self.get_element_coordinates(driver, self.video_progressBar_id)
                CommonMethods.run('adb shell input touchscreen swipe {} {} {} {}'.format(x1, y1, x2 - 10, y2 - 10))
                check = False
        except:
            logging.info("Error in ending the video")

    def verify_same_video_is_played(self, driver):
        try:
            self.wait_till_video_load(driver)
            video_title_now = CommonMethods.getTextOfElement(driver, self.video_title)
            video_title_previous = VideoPage.video_sub_title_name
            check = video_title_now == video_title_previous
            self.verify_true_or_false(driver, check, 'verify_same_video_is_played', 'video sub tile')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_same_video_is_played')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_same_video_is_played')

    def tap_on_next_btn_in_video_player(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                check = CommonMethods.wait_for_element_visible(driver, self.video_play_next_btn, 3)
                current_link_index = self.get_index_of_the_playing_video(driver)
                VideoPage.video_sub_title_name = self.get_text_of_video_lnk(driver, current_link_index + 1)
                if check == True:
                    CommonMethods.elementClick(driver, self.video_play_next_btn)
                    logging.info('clicked on next icon')
                else:
                    logging.info("Failed due to Element not visible in tap_on_next_icon")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
            elif device == 'tab':
                check = CommonMethods.wait_for_element_visible(driver, self.video_play_next_btn, 3)
                self.get_video_slider_window()
                current_link_index = self.get_index_of_the_playing_video(driver)
                VideoPage.video_sub_title_name = self.get_text_of_video_lnk(driver, current_link_index + 1)
                logging.info("nexe video name- " + VideoPage.video_sub_title_name)
                if check == True:
                    CommonMethods.elementClick(driver, self.video_list_close_btn_tab)
                    CommonMethods.elementClick(driver, self.video_play_next_btn)
                    logging.info('clicked on next icon')
                else:
                    logging.info("Failed due to Element not visible in tap_on_next_icon")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_next_btn_in_video_player')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_next_btn_in_video_player')

    def get_video_slider_window(self):
        CommonMethods.run("adb shell input touchscreen swipe 1270 350 700 350")

    def click_next_btn_video_player(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.video_play_next_btn, 10)
            VideoPage.video_sub_title_name = CommonMethods.getTextOfElement(driver, self.video_title)
            CommonMethods.elementClick(driver, self.video_play_next_btn)
            logging.info('clicked on next button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_next_btn_in_video_player')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_next_btn_in_video_player')

    def tap_on_previous_icon_in_video_player(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                check = CommonMethods.wait_for_element_visible(driver, self.video_play_previous_btn, 3)
                current_link_index = self.get_index_of_the_playing_video(driver)
                VideoPage.video_sub_title_name = self.get_text_of_video_lnk(driver, current_link_index - 1)
                if check == True:
                    CommonMethods.elementClick(driver, self.video_play_previous_btn)
                    logging.info('clicked on previous icon')
                else:
                    logging.info("Failed due to Element not visible in tap_on_previous_icon")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
            elif device == 'tab':
                check = CommonMethods.wait_for_element_visible(driver, self.video_play_previous_btn, 3)
                self.get_video_slider_window()
                current_link_index = self.get_index_of_the_playing_video(driver)
                VideoPage.video_sub_title_name = self.get_text_of_video_lnk(driver, current_link_index - 1)
                if check == True:
                    CommonMethods.elementClick(driver, self.video_list_close_btn_tab)
                    CommonMethods.elementClick(driver, self.video_play_previous_btn)
                    logging.info('clicked on next icon')
                else:
                    logging.info("Failed due to Element not visible in tap_on_previous_icon")
                    CommonMethods.takeScreenShot(driver, featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_previous_icon_in_video_player')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_previous_icon_in_video_player')

    def verify_next_video_is_played(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                sleep(7)
                self.wait_till_video_load(driver)
                video_title_now = CommonMethods.getTextOfElement(driver, self.video_title)
                video_title_previous = VideoPage.video_sub_title_name
                check = video_title_now == video_title_previous
                self.verify_true_or_false(driver, check, 'verify_next_video_is_played', 'video sub tile')
            elif device == 'tab':
                sleep(7)
                self.wait_till_video_load(driver)
                video_title_now = self.get_video_title_on_player(driver)
                #                 video_title_previous = VideoPage.video_sub_title_name
                video_title_previous = VideoPage.video_sub_title_name
                check = video_title_now == video_title_previous
                self.verify_true_or_false(driver, check, 'verify_next_video_is_played', 'video sub tile')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_next_video_is_played')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_next_video_is_played')

    def verify_previous_video_is_played(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                sleep(5)
                self.wait_till_video_load(driver)
                video_title_now = CommonMethods.getTextOfElement(driver, self.video_title)
                video_title_previous = VideoPage.video_sub_title_name
                check = video_title_now == video_title_previous
                self.verify_true_or_false(driver, check, 'verify_next_video_is_played', 'video sub tile')
            elif device == 'tab':
                self.wait_till_video_load(driver)
                video_title_now = self.get_video_title_on_player(driver)
                video_title_previous = VideoPage.video_sub_title_name
                check = video_title_now == video_title_previous
                self.verify_true_or_false(driver, check, 'verify_next_video_is_played', 'video sub tile')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_previous_video_is_played')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_previous_video_is_played')

    def tap_on_video_player_setting_icon(self, driver):
        try:
            self.pause_video(driver)
            check = CommonMethods.elementClick(driver, self.video_settingIcon_id)
            self.verify_true_or_false(driver, check, 'tap_on_video_player_setting_icon', 'setting icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_video_player_setting_icon')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_video_player_setting_icon')

    def verify_subtopic_video_slider(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.video_player_list_lay, 10)
            self.verify_true_or_false(driver, check, 'verify_subtopic_video_slider', 'setting icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_subtopic_video_slider')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_subtopic_video_slider')

    """This method will tap on cancel button once the video is completed and stores the next video title"""

    def tap_on_cancel_button(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                CommonMethods.wait_for_element_visible(driver, self.video_auto_cancelBtn_id, 10)
                VideoPage.next_video_title = CommonMethods.getTextOfElement(driver, self.video_next_video_title)
                check = CommonMethods.elementClick(driver, self.video_auto_cancelBtn_id)
                self.verify_true_or_false(driver, check, 'tap_on_cancel_button', 'cancel button')
            elif device == 'tab':
                CommonMethods.wait_for_element_visible(driver, self.video_auto_cancelBtn_id, 10)
                VideoPage.next_video_title = CommonMethods.getTextOfElement(driver, self.video_next_video_title)
                check = CommonMethods.elementClick(driver, self.video_auto_cancelBtn_id)
                self.verify_true_or_false(driver, check, 'tap_on_cancel_button', 'cancel button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_cancel_button')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_cancel_button')

    def verify_setting_bottom_sheet(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.video_auto_play_buttom_sheet)
            self.verify_true_or_false(driver, check, 'verify_setting_bottom_sheet', 'auto play switch')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_setting_bottom_sheet')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_setting_bottom_sheet')

    def verify_video_player_reply_icon(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.video_play_btn)
            self.verify_true_or_false(driver, check, 'verify_setting_bottom_sheet', 'auto play switch')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_setting_bottom_sheet')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_setting_bottom_sheet')

    def verify_back_btn_on_video(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.video_player_back_btn)
            self.verify_true_or_false(driver, check, 'verify_back_btn_on_video', 'auto play switch')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_back_btn_on_video')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_back_btn_on_video')

    def verify_previous_icon_on_video(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.video_play_previous_btn)
            self.verify_true_or_false(driver, check, 'verify_previous_icon_on_video', 'previous btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_previous_icon_on_video')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_previous_icon_on_video')

    def verify_previous_icon_not_on_video(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.video_play_previous_btn, 10)
            self.verify_false(driver, check, 'verify_previous_icon_on_video', 'previous btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_previous_icon_on_video')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_previous_icon_on_video')

    def tap_on_analysis_icon(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.video_analyze_icon_btn, 5)
            if check == True:
                CommonMethods.elementClick(driver, self.video_analyze_icon_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_analysis_icon')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_analysis_icon')

    def tap_on_keyFocus_area(self, driver):
        try:
            CommonMethods.scrollToElement(driver, 'Key focus areas')
            check = CommonMethods.wait_for_element_visible(driver, self.video_keyFocus_1st_lnk, 7)
            if check == True:
                CommonMethods.elementClick(driver, self.video_keyFocus_1st_lnk)
            elif CommonMethods.wait_for_element_visible(driver, self.analysis_screen_start_test, 7):
                CommonMethods.elementClick(driver, self.analysis_screen_start_test)
                subject = (By.XPATH, "//android.widget.TextView[@text='Physics']")
                CommonMethods.wait_for_element_visible(driver, subject, 10)
                CommonMethods.elementClick(driver, subject)
                CommonMethods.scrollToElementAndClick(driver, "Tests")
                Start = (By.XPATH, "//android.widget.TextView[@text='Start']")
                CommonMethods.wait_for_element_visible(driver, Start, 10)
                ele = CommonMethods.getElements(driver, Start)
                ele[0].click()
                CommonMethods.wait_for_element_visible(driver,
                                                       (By.ID, "com.byjus.thelearningapp.premium:id/test_start_button"),
                                                       10)
                CommonMethods.elementClick(driver, (By.ID, "com.byjus.thelearningapp.premium:id/test_start_button"))
                CommonMethods.wait_for_element_visible(driver, (By.XPATH, "//android.widget.Button[@text='Submit']"),
                                                       10)
                CommonMethods.elementClick(driver, (By.XPATH, "//android.widget.Button[@text='Submit']"))
                CommonMethods.wait_for_element_visible(driver, (By.XPATH, "//android.widget.Button[@text='Submit']"),
                                                       10)
                CommonMethods.elementClick(driver, (By.XPATH, "//android.widget.Button[@text='Submit']"))
                driver.start_activity('com.byjus.thelearningapp.premium', 'com.byjus.app.home.activity.HomeActivity')
                self.verify_corana_dialog(driver)
                self.tap_on_analysis_icon(driver)
                CommonMethods.scrollToElement(driver, 'Key focus areas')
                check = CommonMethods.wait_for_element_visible(driver, self.video_keyFocus_1st_lnk, 7)
                if check == True:
                    CommonMethods.elementClick(driver, self.video_keyFocus_1st_lnk)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_keyFocus_area')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_keyFocus_area')

    #     def end_the_video(self, driver):
    #         try:
    #             self.wait_till_video_load(driver)
    #             x,y = self.get_element_coordinates(driver, self.video_progressBar_id)
    #             self.click_on_video_icon(driver, self.video_play_btn)
    #             x2 = x-10
    #             y2 = y-10
    #             sleep(3)
    #             CommonMethods.elementClick(driver, self.video_frame_id)
    #             self.click_on_x_y_coordinate(x2, y2)
    #             CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 60)
    #         except:
    #             logging.info("Error in ending the video")

    def verify_comming_soon_on_video_card(self, driver, chapter):
        try:
            CommonMethods.scrollToElement(driver, chapter)
            comming_soon_locator = (By.XPATH,
                                    "//android.widget.TextView[@text=\'" + chapter + "\']//parent::android.widget.RelativeLayout//following-sibling::androidx.recyclerview.widget.RecyclerView//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_comingsoon_txtvw']")
            check = CommonMethods.isElementPresent(driver, comming_soon_locator)
            self.verify_true_or_false(driver, check, 'verify_comming_soon_on_video_card', 'Comming soon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_comming_soon_on_video_card')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_comming_soon_on_video_card')

    def tap_on_comming_soon_on_video_card(self, driver, chapter):
        try:
            comming_soon_locator = (By.XPATH,
                                    "//android.widget.TextView[@text=\'" + chapter + "\']//parent::android.widget.RelativeLayout//following-sibling::androidx.recyclerview.widget.RecyclerView//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_comingsoon_txtvw']")
            CommonMethods.elementClick(driver, comming_soon_locator)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_comming_soon_on_video_card')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_comming_soon_on_video_card')

    def verify_comming_soon_dialog(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.video_comming_soon_dialog_popup, 5)
            check = CommonMethods.isElementPresent(driver, self.video_comming_soon_dialog_popup)
            self.verify_true_or_false(driver, check, 'verify_comming_soon_dialog', 'Comming soon text')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_comming_soon_dialog')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_comming_soon_dialog')

    def verify_test_card_is_present(self, driver):
        try:
            CommonMethods.scrollToElement(driver, 'Test')
            CommonMethods.wait_for_element_visible(driver, self.video_test_lnk, 5)
            check = CommonMethods.isElementPresent(driver, self.video_test_lnk)
            self.verify_true_or_false(driver, check, 'verify_test_card_is_present', 'Test Link')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_test_card_is_present')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_test_card_is_present')

    def verify_practice_card_is_present(self, driver):
        try:
            CommonMethods.scrollToElement(driver, 'Practice')
            CommonMethods.wait_for_element_visible(driver, self.video_practice_lnk, 5)
            check = CommonMethods.isElementPresent(driver, self.video_practice_lnk)
            self.verify_true_or_false(driver, check, 'verify_practice_card_is_present', 'Test Link')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_practice_card_is_present')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_practice_card_is_present')

    def verify_test_icon_is_present(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.video_test_icon, 5)
            check = CommonMethods.isElementPresent(driver, self.video_test_icon)
            self.verify_true_or_false(driver, check, 'verify_test_icon_is_present', 'Test icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_test_icon_is_present')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_test_icon_is_present')

    def verify_practice_icon_is_present(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.video_practice_icon, 5)
            check = CommonMethods.isElementPresent(driver, self.video_practice_icon)
            self.verify_true_or_false(driver, check, 'verify_practice_icon_is_present', 'Practice icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_practice_icon_is_present')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_practice_icon_is_present')

    def verify_test_label_is_present(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.video_test_lable, 5)
            check = CommonMethods.isElementPresent(driver, self.video_test_lable)
            self.verify_true_or_false(driver, check, 'verify_test_label_is_present', 'Test Lable ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_test_label_is_present')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_test_label_is_present')

    def verify_practice_label_is_present(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.video_practice_lable, 5)
            check = CommonMethods.isElementPresent(driver, self.video_practice_lable)
            self.verify_true_or_false(driver, check, 'verify_practice_label_is_present', 'Practice Lable ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_practice_label_is_present')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_practice_label_is_present')

    def verify_x_test_is_present(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.video_test_x_test, 5)
            check = CommonMethods.isElementPresent(driver, self.video_test_x_test)
            self.verify_true_or_false(driver, check, 'verify_x_test_is_present', 'X test')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_x_test_is_present')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_x_test_is_present')

    def verify_pratice_stage_name_is_present(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.video_practice_stage_name_test, 5)
            check = CommonMethods.isElementPresent(driver, self.video_practice_stage_name_test)
            self.verify_true_or_false(driver, check, 'verify_pratice_stage_name_is_present', 'Practice stag name')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_pratice_stage_name_is_present')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_pratice_stage_name_is_present')

    def verify_forward_icon_test(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.video_test_right_arrow, 5)
            check = CommonMethods.isElementPresent(driver, self.video_test_right_arrow)
            self.verify_true_or_false(driver, check, 'verify_forward_icon_test', 'Forward Icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_forward_icon_test')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_forward_icon_test')

    def verify_forward_icon_practice(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.video_practice_right_arrow, 5)
            check = CommonMethods.isElementPresent(driver, self.video_practice_right_arrow)
            self.verify_true_or_false(driver, check, 'verify_forward_icon_practice', 'Forward Icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_forward_icon_practice')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_forward_icon_practice')

    def tap_on_test_on_video_sub_list(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                self.wait_till_video_load(driver)
                CommonMethods.scrollToElement(driver, 'Test')
                #                 VideoPage.chapter_name = CommonMethods.getTextOfElement(driver, self.video_chapter_title_in_video_list)
                check = CommonMethods.wait_for_element_visible(driver, self.video_test_right_arrow, 5)
                CommonMethods.elementClick(driver, self.video_test_right_arrow)
                self.verify_true_or_false(driver, check, 'tap_on_test_on_video_sub_list', 'Test link')
            elif device == 'tab':
                CommonMethods.scrollToElement(driver, 'Test')
                #                 VideoPage.chapter_name = CommonMethods.getTextOfElement(driver, self.video_chapter_name_id)
                check = CommonMethods.wait_for_element_visible(driver, self.video_test_right_arrow, 5)
                CommonMethods.elementClick(driver, self.video_test_right_arrow)
                self.verify_true_or_false(driver, check, 'tap_on_test_on_video_sub_list', 'Test link')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_test_on_video_sub_list')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_test_on_video_sub_list')

    def tap_on_start_btn_in_test_screen_finish_test(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                if CommonMethods.scrollToElementAndClick(driver, 'Start'):
                    CommonMethods.wait_for_element_visible(driver, self.test_screen_Test_btn, 10)
                    CommonMethods.elementClick(driver, self.test_screen_Test_btn)
                    CommonMethods.wait_for_element_visible(driver, self.self.test_submit_Btn, 10)
                    CommonMethods.elementClick(driver, self.test_submit_Btn)
                    CommonMethods.wait_for_element_visible(driver, self.self.test_submit_Btn, 10)
                    CommonMethods.elementClick(driver, self.test_submit_Btn)
                    CommonMethods.elementClick(driver, self.video_badge_close_btn)
                    driver.start_activity('com.byjus.thelearningapp.premium',
                                          'com.byjus.app.home.activity.HomeActivity')
                    self.verify_corana_dialog(driver)
                else:
                    logging.info('The keyfocus screen has videos')
            elif device == 'tab':
                start_btn = CommonMethods.getElements(driver, self.test_screen_start_elements)
                start_btn[0].click()
                check = CommonMethods.wait_for_element_visible(driver, self.test_screen_Test_btn, 5)
                self.verify_true_or_false(driver, check, 'tap_on_start_btn_in_test_screen', 'Test link')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_start_btn_in_test_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_start_btn_in_test_screen')

    def tap_on_practice_on_video_sub_list(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                CommonMethods.scrollToElement(driver, 'Practice')
                VideoPage.chapter_name = CommonMethods.getTextOfElement(driver, self.video_chapter_title_in_video_list)
                check = CommonMethods.wait_for_element_visible(driver, self.video_practice_right_arrow, 5)
                CommonMethods.elementClick(driver, self.video_practice_right_arrow)
                self.verify_true_or_false(driver, check, 'tap_on_practice_on_video_sub_list', 'Test link')
            elif device == 'tab':
                CommonMethods.scrollToElement(driver, 'Practice')
                VideoPage.chapter_name = CommonMethods.getTextOfElement(driver, self.video_chapter_name_id)
                check = CommonMethods.wait_for_element_visible(driver, self.video_practice_right_arrow, 5)
                CommonMethods.elementClick(driver, self.video_practice_right_arrow)
                self.verify_true_or_false(driver, check, 'tap_on_practice_on_video_sub_list', 'Test link')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_practice_on_video_sub_list')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_practice_on_video_sub_list')

    def verify_chapter_in_test_screen(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.test_page_id, 5)
            check1 = CommonMethods.findText(driver, VideoPage.chapter_name)
            check2 = CommonMethods.findText(driver, 'Objective Tests ')
            check3 = CommonMethods.findText(driver, 'Subjective Tests ')
            check = check1 and check2 and check3
            self.verify_true_or_false(driver, check, 'verify_chapter_in_test_screen', 'Test Screen elements')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_chapter_in_test_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_chapter_in_test_screen')

    def navigate_to_test_screen(self, driver):
        try:
            VideoPage.chapter_name = CommonMethods.getTextOfElement(driver, self.video_chapter_title_library_screen)
            test_btn = (By.XPATH,
                        "//android.widget.TextView[@text = \'" + VideoPage.chapter_name + "\']//ancestor::android.widget.LinearLayout[@resource-id ='com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.Button[@text = 'Test']")
            CommonMethods.elementClick(driver, test_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_test_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_test_screen')

    def tap_on_practice_card2(self, driver, chapter):
        try:
            CommonMethods.scrollToElement(driver, chapter)
            VideoPage.chapter_name = chapter
            practice_btn = (By.XPATH,
                            "//android.widget.TextView[@text = \'" + chapter + "\']//ancestor::android.widget.LinearLayout[@resource-id ='com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.Button[@text = 'Practice']")
            CommonMethods.elementClick(driver, practice_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_practice_card')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_practice_card')

    def verify_redirect_to_chapter_screen(self, driver):
        try:
            chapter_name = VideoPage.chapter_name
            CommonMethods.scrollToElement(driver, chapter_name)
            check = CommonMethods.findText(driver, chapter_name)
            self.verify_true_or_false(driver, check, 'verify_redirect_to_chapter_screen', VideoPage.chapter_name)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_redirect_to_chapter_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_redirect_to_chapter_screen')

    def verifyTextPresent(self, driver, text):
        try:
            sleep(3)
            check = CommonMethods.findText(driver, text)
            self.verify_true_or_false(driver, check, 'verifyTextPresent', text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyTextPresent')
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyTextPresent')

    def verify_practice_btn(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.practice_start_practice_btn)
            self.verify_true_or_false(driver, check, 'verify_practice_btn', 'Practice Btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_practice_btn')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_practice_btn')

    def verify_user_is_in_chapter_screen(self, driver):
        try:
            check = CommonMethods.scrollToElement(driver, 'Chapters')
            self.verify_true_or_false(driver, check, 'verify_user_is_in_chapter_screen', 'Chapters screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_user_is_in_chapter_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_user_is_in_chapter_screen')

    def scroll_video_list_up_and_down(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                first_lnk_title = CommonMethods.getTextOfElement(driver, self.video_1st_list_lnk_text)
                self.click_on_2nd_video_lnk(driver)
                check1 = CommonMethods.scrollToElement(driver, 'Practice')
                check2 = CommonMethods.scrollToElement(driver, first_lnk_title)
                check = check1 and check2
                self.verify_true_or_false(driver, check, 'scroll_video_list_up_and_down', 'Scroll up and down')
                self.verify_true_or_false(driver, check, 'scroll_video_list_up_and_down', 'Practice Btn')
            elif device == 'tab':
                check1 = CommonMethods.scrollToElement(driver, 'Practice')
                first_video = CommonMethods.getTextOfElement(driver, self.video_tab_video_lst_1st_video_title)
                check2 = CommonMethods.scrollToElement(driver, first_video)
                check = check1 and check2
                self.verify_true_or_false(driver, check, 'scroll_video_list_up_and_down', 'Scroll up and down')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'scroll_video_list_up_and_down')
        except:
            CommonMethods.exception(driver, featureFileName, 'scroll_video_list_up_and_down')

    def delete_all_bookmark(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
            else:
                while check == True:
                    CommonMethods.elementClick(driver, self.bookmark_icon)
                    check = CommonMethods.isElementPresent(driver, self.bookmark_icon)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'remove_bookmark')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'remove_bookmark')

    def tap_on_bookmark_menu(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                CommonMethods.elementClick(driver, self.back_button_id)
                CommonMethods.wait_for_element_visible(driver, self.ham_bookmark, 3)
                CommonMethods.elementClick(driver, self.ham_bookmark)
            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_bookmark_menu')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_bookmark_menu')

    def tap_on_bookmark_icon(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.video_bookmark_icon_id, 5):
                CommonMethods.elementClick(driver, self.video_bookmark_icon_id)
            else:
                logging.info('Bookmark icon Not Found')
                pytest.fail("Failed due to Bookmark icon")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_bookmark_icon')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_bookmark_icon')

    def verify_user_is_able_to_bookmark(self, driver):
        try:
            status = CommonMethods.getAttributeOfElement(driver, 'clickable', self.video_bookmark_icon_id).capitalize()
            check = bool(status)
            self.verify_true_or_false(driver, check, 'verify_user_is_able_to_bookmark', 'Bookmark icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_bookmark_icon')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_bookmark_icon')

    def verify_toast_msg(self, driver, text):
        try:
            check = CommonMethods.isElementPresent(driver, self.toast_msg)

            if check == True:
                act_txt = CommonMethods.getTextOfElement(driver, self.toast_msg)
                exp_txt = text
                assert act_txt == exp_txt, "toast  text  failed "
            else:
                logging.info("toast text verification failed ")
                pytest.fail("toast text verification failed ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_toast_msg')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_toast_msg')

    def rgb2hex(self, rgb):
        return '#%02x%02x%02x' % rgb

    def get_the_rgb_lst(self, driver, locator):
        try:
            s1 = set()
            CommonMethods.wait_for_element_visible(driver, locator, 10)
            element1 = CommonMethods.getElement(driver, locator)
            location = element1.location
            size = element1.size
            png = driver.get_screenshot_as_png()
            img = Image.open(BytesIO(png))
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            im = img.crop((left, top, right, bottom))
            pix_val1 = list(dict.fromkeys(list(im.get_data())))
            for i in range(len(pix_val1)):
                rgb = list(pix_val1[i])
                try:
                    rgb.pop(3)
                except:
                    pass  # just to bypass for tap scenarios it will not have 3rd index
                tup = tuple(rgb)
                result = self.rgb2hex(tup)
                s1.add(result)
            return s1
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'get_the_rgb_lst')

        except:
            CommonMethods.exception(driver, featureFileName, 'get_the_rgb_lst')

    def verify_subject_chapter_color(self, first, secound, count):
        result = first & secound
        if len(result) >= count:
            logging.info("both have same color")
        else:
            logging.info("both color not matching")

    def verify_chapter_subject_theme_color(self, driver):
        subject_rgb = VideoPage.subject_rgb_lst
        chapter_rgb = self.get_the_rgb_lst(driver, self.video_chapter_name_id)
        self.verify_subject_chapter_color(subject_rgb, chapter_rgb, 40)

    def verify_the_bookmark_icon_color_with_subject(self, driver):
        subject_rgb = VideoPage.subject_rgb_lst
        book_mark_icon = self.get_the_rgb_lst(driver, self.video_bookmark_icon_id)
        self.verify_subject_chapter_color(subject_rgb, book_mark_icon, 5)

    def enble_toggle_btn(self, driver):
        status = CommonMethods.getAttributeOfElement(driver, 'checked', self.video_auto_enable_switch)
        if CommonMethods.wait_for_element_visible(driver, self.video_auto_enable_switch, 3):
            if status == 'true':
                VideoPage.auto_play_switch_color = self.get_the_rgb_lst(driver, self.video_auto_enable_switch)
                logging.info('Autoplay is enable')
                CommonMethods.click_on_device_back_btn(driver)
            elif status == 'false':
                CommonMethods.elementClick(driver, self.video_auto_enable_switch)
                VideoPage.auto_play_switch_color = self.get_the_rgb_lst(driver, self.video_auto_enable_switch)
                CommonMethods.click_on_device_back_btn(driver)
        else:
            logging.info('Error in getting Auto play option screen')

    def verify_video_icon_after_completion(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                check1 = CommonMethods.isElementPresent(driver, self.video_auto_play_btn)
                check2 = CommonMethods.isElementPresent(driver, self.video_player_back_btn)
                check3 = CommonMethods.isElementPresent(driver, self.video_up_next)
                check4 = CommonMethods.isElementPresent(driver, self.video_next_video_title)
                check5 = CommonMethods.isElementPresent(driver, self.video_next_video_chapter_name)
                check6 = CommonMethods.isElementPresent(driver, self.video_auto_cancelBtn_id)
                self.verify_true_or_false(driver, check1, 'verify_video_icon_after_completion', "auto load icon")
                self.verify_true_or_false(driver, check2, 'verify_video_icon_after_completion', "Player Back Button")
                self.verify_true_or_false(driver, check3, 'verify_video_icon_after_completion', "Up next Text")
                self.verify_true_or_false(driver, check4, 'verify_video_icon_after_completion', "next video Title")
                self.verify_true_or_false(driver, check5, 'verify_video_icon_after_completion',
                                          "next video chapter name")
                self.verify_true_or_false(driver, check6, 'verify_video_icon_after_completion', "Cancel Button")
            elif device == 'tab':
                check1 = CommonMethods.isElementPresent(driver, self.video_auto_play_btn)
                check2 = CommonMethods.isElementPresent(driver, self.video_tab_player_back_btn)
                check3 = CommonMethods.isElementPresent(driver, self.video_up_next)
                check4 = CommonMethods.isElementPresent(driver, self.tab_video_next_video_title)
                check5 = CommonMethods.isElementPresent(driver, self.video_tab_next_video_chapter_name)
                check6 = CommonMethods.isElementPresent(driver, self.video_tab_auto_cancel_btn)
                self.verify_true_or_false(driver, check1, 'verify_video_icon_after_completion', "auto load icon")
                self.verify_true_or_false(driver, check2, 'verify_video_icon_after_completion', "Player Back Button")
                self.verify_true_or_false(driver, check3, 'verify_video_icon_after_completion', "Up next Text")
                self.verify_true_or_false(driver, check4, 'verify_video_icon_after_completion', "next video Title")
                self.verify_true_or_false(driver, check5, 'verify_video_icon_after_completion',
                                          "next video chapter name")
                self.verify_true_or_false(driver, check6, 'verify_video_icon_after_completion', "Cancel Button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_icon_after_completion')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_icon_after_completion')

    def next_video_should_play(self, driver):
        try:
            check1 = CommonMethods.wait_for_element_visible(driver, self.video_auto_play_btn, 5)
            VideoPage.next_video_title = CommonMethods.getTextOfElement(driver, self.video_next_video_title)
            sleep(10)
            expected_video_title = CommonMethods.getTextOfElement(driver, self.video_title_in_list_id)
            check = CommonMethods.verifyTwoText(VideoPage.next_video_title, expected_video_title)
            self.verify_true_or_false(driver, check1, 'next_video_should_play', "auto play btn")
            self.verify_true_or_false(driver, check, 'next_video_should_play', 'Video Title')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'next_video_should_play')
        except:
            CommonMethods.exception(driver, featureFileName, 'next_video_should_play')

    def tap_on_any_video(self, driver):
        try:
            sleep(3)
            device = CommonMethods.get_device_type(driver)
            if device == 'mobile':
                ele = CommonMethods.getElements(driver, self.video_play_list_elements)
                ele_length = len(ele)
                n = random.randint(1, ele_length - 1)
                ele[n].click()
            elif device == 'tab':
                ele = CommonMethods.getElements(driver, self.tab_videos_list_elements)
                ele_length = len(ele)
                n = random.randint(1, ele_length - 1)
                ele[n].click()
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_any_video')
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_any_video')

    def verify_video_icons_should_disapper(self, driver):
        try:
            check1 = CommonMethods.wait_for_element_visible(driver, self.ten_sec_bkwd_btn_id, 2)
            check2 = CommonMethods.wait_for_element_visible(driver, self.ten_sec_fwd_btn_id, 2)
            check3 = CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 2)
            check = not check1 or check2 or check3
            self.verify_true_or_false(driver, check, 'verify_video_icons_should_disapper', "all video icons")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_icons_should_disapper')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_icons_should_disapper')

    def verify_video_icons_should_apper(self, driver):
        try:
            check1 = CommonMethods.wait_for_element_visible(driver, self.ten_sec_bkwd_btn_id, 2)
            check2 = CommonMethods.wait_for_element_visible(driver, self.ten_sec_fwd_btn_id, 2)
            check3 = CommonMethods.wait_for_element_visible(driver, self.video_play_btn, 2)
            check = check1 and check2 and check3
            self.verify_true_or_false(driver, check, 'verify_video_icons_should_disapper', "all video icons")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_video_icons_should_apper')
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_video_icons_should_apper')

