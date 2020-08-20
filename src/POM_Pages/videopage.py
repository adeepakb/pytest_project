import logging
import pytest
from time import sleep
from Constants.load_json import *
from appium.webdriver.common.touch_action import TouchAction
from Utilities.common_methods import CommonMethods
from Constants.constants import CONFIG_PATH, Login_Credentials
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from POM_Pages.locators import video
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from io import BytesIO
import random
from Utilities.generic_methods import GenericMethods
from cgitb import grey
from appium.common.logger import logger




# f = open("../../Test_data/featureFileName.txt","r")
# f = open("C:/EclipseWorkspaces/csse120/K12_Automation/src/Test_data/featureFileName.txt","r")
# featureFileName = f.read()
featureFileName = "video"

CommonMethods = CommonMethods()
data_file = CONFIG_PATH
video_name = None




class VideoPage():
    
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
    video_end_time = None
    video_start_time_portrait = None
    video_start_time_landscape = None
    video_sub_title_name = None
    title_of_next_video = None
    practice_stage_name =None
    
    def __init__(self,driver):
        self.driver = driver
    
    
    register_page_email_txt_bx = (By.ID,"com.byjus.thelearningapp.premium:id/etEmail")
    register_page_register_btn = (By.ID,"com.byjus.thelearningapp.premium:id/btnRegister")
    register_page_name_field = (By.ID,"com.byjus.thelearningapp.premium:id/etName")    
    login_register_btn = (By.ID, "com.byjus.thelearningapp.premium:id/primaryAction")
    registration_name_field= (By.ID,"com.byjus.thelearningapp.premium:id/etName")
    register_btn = (By.ID,"com.byjus.thelearningapp.premium:id/btnRegister")
    chooseCourse_Title_xpath = (By.XPATH, "//android.widget.TextView[@text='your course']")
    maths_subject = (By.XPATH, "//android.widget.TextView[@text='Mathematics']")
    toast_msg= (By.XPATH, "//android.widget.Toast")
    practice_continue_btn = (By.ID,"com.byjus.thelearningapp.premium:id/primaryAction")
    practice_submit_btn = (By.ID,"com.byjus.thelearningapp.premium:id/action_morph_btn")
    practice_2nd_answer = (By.XPATH,"//android.widget.ListView//android.view.View[@index=1]//android.view.View[@index=1]")
    practice_start_practice_btn = (By.ID,"com.byjus.thelearningapp.premium:id/tvStartPractice")
    homescreen_corana_dialog_ok_btn = (By.XPATH,"//android.widget.TextView[@text = 'OK']")
    homescreen_corana_dialog = (By.ID,"com.byjus.thelearningapp.premium:id/dialog_layout")
    profile_header_id = (By.ID,"com.byjus.thelearningapp.premium:id/llHeaderTextParent")
    profile_name = (By.ID,"com.byjus.thelearningapp.premium:id/header_title_text")
    profile_mob_num = (By.ID,"com.byjus.thelearningapp.premium:id/mobile_number")
    back_button_id = (By.ID,"com.byjus.thelearningapp.premium:id/backNav")
    user_name_profile_page = (By.ID,"com.byjus.thelearningapp.premium:id/tvUserName")
    profile_name_hamburger = (By.ID,"com.byjus.thelearningapp.premium:id/home_drawer_imgvw_arrow_right")
    account_details_title = (By.ID,"com.byjus.thelearningapp.premium:id/account_details_title")
    phone_num = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    country_Code = (By.ID, "com.byjus.thelearningapp.premium:id/spnrCountry")
    video = (By.XPATH, "//android.widget.ImageView[@instance='2']")
    Btn_test = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_list_item_test_txtvw")
    Btn_practice = (By.ID, "com.byjus.thelearningapp.premium:id/practice_mode_bottom_txtvw")
    Btn_play_pause = (By.XPATH, "//android.widget.ImageView[@instance='3']")
    loginBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/btnLogin")
    OtpTxtBx_id = (By.ID, "com.byjus.thelearningapp.premium:id/etOTP")
    librayBtn_id = (By.XPATH,"//android.widget.Button[@text='Library']")
    personalizeScreen_xpath = (By.XPATH,"//android.widget.Button[@text='Personalised']")
    first_videoLnk_xpath = (By.XPATH, "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group' and @index=1]/androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_videos_lstvw']/android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_cardview' and @index = 0]")
    video_frame_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_subtitles")
    chapter_videoLnk_elements = (By.XPATH,"//android.widget.ImageView[@resource-id ='com.byjus.thelearningapp.premium:id/chapter_video_thumbnail_imgvw']")
    tab_chapter_videoLnk_elements = (By.ID,"com.byjus.thelearningapp.premium:id/chapter_view_group")
    video_pause_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_pause")
    video_play_btn = (By.ID, "com.byjus.thelearningapp.premium:id/exo_play")
    video_play_next_btn = (By.ID,"com.byjus.thelearningapp.premium:id/ivNext")
    video_play_previous_btn = (By.ID,"com.byjus.thelearningapp.premium:id/ivPrevious")
    videoPlayingNow_xpath = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']/android.widget.LinearLayout[@index=0]//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
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
    video1stLink_xpath = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']/android.widget.LinearLayout[@index=0]")
    allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    none_of_the_above_id = (By.ID,"com.google.android.gms:id/cancel")
    select_8th_grade = (By.XPATH,"//android.widget.Button[@text='8th']")
    video_time_remaining = (By.ID,"com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv")
    video_test_lnk = (By.XPATH, "//android.widget.TextView[@text = 'Test']")
    video_practice_lnk = (By.XPATH, "//android.widget.TextView[@text = 'Practice']")
    video_comming_soon_dialog_popup = (By.XPATH, "//android.widget.TextView[@text='Coming Soon' and @resource-id = 'com.byjus.thelearningapp.premium:id/dialog_title']")
    chapter_name_text = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_list_view']//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/header_title_text']")
    verify_library_screen = (By.ID,"com.byjus.thelearningapp.premium:id/chapter_statusIcon_imgvw") # it is the playbtn inside the video thumnail which will be only for library screen
    chapter_screen_library_personalize_btn_elements = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/toolbarView']/android.widget.FrameLayout") # this btn will be in the right corner of the chapter list screen
    multiple_accounts_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_linearlayout")
    user_profile_name = (By.ID, "com.byjus.thelearningapp.premium:id/tv_profile_name")
    profile_select_radio_button = (By.ID, "com.byjus.thelearningapp.premium:id/profile_select_radio_button")
    continue_button = (By.ID, "com.byjus.thelearningapp.premium:id/tv_submit")
    loginPageVerify_id = (By.XPATH, "//android.widget.Button[@text='Login']")
    welcome_button = (By.ID, "com.byjus.thelearningapp.premium:id/welcomeButton")

#    subject page
    subject_title_id = (By.ID,"com.byjus.thelearningapp.premium:id/title")
    
#     Video Player Screen Locators
    screen_orientation_id = (By.ID,"com.byjus.thelearningapp.premium:id/orientation_toggle")
    video_backBtn_id = (By.ID,"com.byjus.thelearningapp.premium:id/back")
    videoSpeed_up_dwnIcon_id = (By.ID,"com.byjus.thelearningapp.premium:id/playback_speed")
    video_subtitileIcon_id = (By.ID,"com.byjus.thelearningapp.premium:id/subtitle_tracks")
    video_mutipleAudioTracks_id = (By.ID,"com.byjus.thelearningapp.premium:id/audio_tracks")
    video_settingIcon_id = (By.ID,"com.byjus.thelearningapp.premium:id/settings")
    video_progressBar_id = (By.ID,"com.byjus.thelearningapp.premium:id/exo_progress")
    videoPauseBtn_id2 = "com.byjus.thelearningapp.premium:id/exo_pause"
    video_1stLnk = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']/android.widget.LinearLayout[@index=0]//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
    video_video_frame_id = (By.ID,"com.byjus.thelearningapp.premium:id/videoViewLayout")
    video_auto_play_buttom_sheet = (By.ID, "com.byjus.thelearningapp.premium:id/design_bottom_sheet")
    video_name_list_elements = (By.ID,"com.byjus.thelearningapp.premium:id/videoName")
    video_grades_elements = (By.ID,"com.byjus.thelearningapp.premium:id/course_view_group")
    ham_bookmark=(By.XPATH,("//android.widget.TextView[@text='Bookmarks']"))
    video_title_on_player = (By.ID,"com.byjus.thelearningapp.premium:id/tvVideoName")
    practice_back_arrow_btn = (By.ID,"com.byjus.thelearningapp.premium:id/roundedNavButton")
    current_tumbnail_progress_bar = (By.XPATH,"//android.widget.ProgressBar[@resource-id='com.byjus.thelearningapp.premium:id/video_progress_view' and @selected='true']")
#   VideoPlayer List Screen
    video_1st_list_lnk_text = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView//android.widget.LinearLayout[@index = 0]//android.widget.TextView[@resource-id = 'com.byjus.thelearningapp.premium:id/videoName']")
    video_list_seperater_line = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView//android.widget.LinearLayout[@index = 0]//android.view.View")
    video_list_lnk_xpath = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view' and @index=1]//android.widget.LinearLayout[@index=0]")    
    video_tab__sub_1st_video_lnk = (By.XPATH,"//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group' and @index = 1]")
    video_title_in_list_id = (By.ID, "com.byjus.thelearningapp.premium:id/video_title_2")
    video_title = (By.ID, "com.byjus.thelearningapp.premium:id/video_title_2")
    video_name_list = (By.XPATH,"//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName']")
    video_auto_cancelBtn_id = (By.XPATH,"//android.widget.TextView[@text = 'Cancel']")
    video_tab_auto_cancel_btn = (By.ID,"com.byjus.thelearningapp.premium:id/btnCancelAutoPlay")
    video_chapter_name_id = (By.ID,"com.byjus.thelearningapp.premium:id/chapter_title_2")
    video_list_view_id = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_videos_lstvw']/android.widget.LinearLayout")
    video_share_icon_id = (By.ID,"com.byjus.thelearningapp.premium:id/ivShare")
    video_bookmark_icon_id = (By.ID,"com.byjus.thelearningapp.premium:id/bookmark")
    video_topic_videos_id = (By.ID,"com.byjus.thelearningapp.premium:id/videoName")
    video_progress_tab_id = (By.ID, "com.byjus.thelearningapp.premium:id/exo_progress")
    video_tab_video_lst_1st_video = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout[@index=0]")
    video_tab_video_lst_1st_video_title = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']/android.widget.LinearLayout[@index=0]//android.widget.TextView[@index = 1]")
    video_tab_video_player_close_btn = (By.ID,"com.byjus.thelearningapp.premium:id/video_list_close")
    video_player_list_lay = (By.ID,"com.byjus.thelearningapp.premium:id/video_list_lay")
    video_grade_selection_btn = (By.ID, "com.byjus.thelearningapp.premium:id/tvGrade")
    mob_video_title_on_player = (By.ID,"com.byjus.thelearningapp.premium:id/videoTitle")
    analysis_screen_start_test = (By.ID,"com.byjus.thelearningapp.premium:id/analytics_empty_state_start")
    analysis_screen_continue_test = (By.ID,"com.byjus.thelearningapp.premium:id/continueTextView")
    
#     video Locator for tab  
    video_list_btn_tab = (By.ID, 'com.byjus.thelearningapp.premium:id/video_list')
    video_list_close_btn_tab = (By.ID, 'com.byjus.thelearningapp.premium:id/video_list_close')
    video_tab_videoframe = (By.ID,"com.byjus.thelearningapp.premium:id/exo_subtitles")
    video_buffering =(By.ID, "com.byjus.thelearningapp.premium:id/exo_buffering")
    video_badge_close_btn = (By.ID,"com.byjus.thelearningapp.premium:id/ivCloseBtn")
    video_auto_enable_switch = (By.ID, "com.byjus.thelearningapp.premium:id/swAutoplay")
    video_play_list_elements = (By.XPATH, "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName']")
    video_practice_lnk = (By.XPATH, "//android.widget.TextView[@text = 'Practice']")
    video_auto_play_btn =(By.ID,"com.byjus.thelearningapp.premium:id/autoPlayProgressView")
    video_videos_list_in_video_list_lay_elements = (By.ID,"com.byjus.thelearningapp.premium:id/videoItem")
    tab_videos_list_elements = (By.ID,"com.byjus.thelearningapp.premium:id/videoItem") 
    test_page_id = (By.ID,"com.byjus.thelearningapp.premium:id/chaptertest_recyclerview")
    test_page_chapter_name=(By.ID,"com.byjus.thelearningapp.premium:id/header_title_text")
#     video Locators for tab
    video_frame_pause_btn = (By.ID,"com.byjus.thelearningapp.premium:id/ivPlay")
    video_play_pause_btn = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/center_area']//android.widget.ImageButton")
    video_10s_bckwrd_text = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/center_area']//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp.premium:id/exo_rew']//android.widget.TextView")
    video_10s_frwrd_text = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/center_area']//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp.premium:id/exo_ffwd']//android.widget.TextView")

#     Video Auto Enable 
    video_next_video_title = (By.XPATH,"//android.widget.LinearLayout[@resource-id = 'com.byjus.thelearningapp.premium:id/llNextVideoInfo']/android.widget.TextView[@resource-id ='com.byjus.thelearningapp.premium:id/tvNextVideoTitle']")
    tab_video_next_video_title = (By.ID,"com.byjus.thelearningapp.premium:id/tvNextVideoTitle")
    video_next_video_chapter_name = (By.XPATH,"//android.widget.LinearLayout[@resource-id = 'com.byjus.thelearningapp.premium:id/llNextVideoInfo']/android.widget.TextView[@resource-id = 'com.byjus.thelearningapp.premium:id/tvChapterName']")
    video_tab_next_video_chapter_name = (By.ID,"com.byjus.thelearningapp.premium:id/tvChapterName")
    video_up_next = (By.ID,"com.byjus.thelearningapp.premium:id/tvUpNext")
    video_video_player_chapter_txt = (By.ID,"com.byjus.thelearningapp.premium:id/tvNextVideoTitle")
    video_player_back_btn = (By.ID,"com.byjus.thelearningapp.premium:id/back")
    video_tab_player_back_btn = (By.ID,"com.byjus.thelearningapp.premium:id/backButton")
    video_analyze_icon_btn = (By.ID,"com.byjus.thelearningapp.premium:id/iv_analysis")

    video_keyFocus_1st_lnk = (By.XPATH,"//android.widget.RelativeLayout[@resource-id='com.byjus.thelearningapp.premium:id/layout_keyfocusarea' and @index = 0]")
    video_test_icon = (By.XPATH,"//android.widget.TextView[@text = 'Test']//parent::android.widget.RelativeLayout//android.widget.LinearLayout")
    video_practice_icon = (By.XPATH,"//android.widget.TextView[@text = 'Practice']//parent::android.widget.RelativeLayout//android.widget.LinearLayout")
    video_test_lable = (By.XPATH,"//android.widget.TextView[@text = 'Test' and @resource-id = 'com.byjus.thelearningapp.premium:id/primaryText']")
    video_practice_lable = (By.XPATH,"//android.widget.TextView[@text = 'Practice' and @resource-id = 'com.byjus.thelearningapp.premium:id/primaryText']")
    video_test_x_test = (By.XPATH,"//android.widget.TextView[@text = 'Test']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id ='com.byjus.thelearningapp.premium:id/secondaryText']")
    video_practice_stage_name_test = (By.XPATH,"//android.widget.TextView[@text = 'Practice']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id ='com.byjus.thelearningapp.premium:id/secondaryText']")
    video_test_right_arrow = (By.XPATH,"//android.widget.TextView[@text = 'Test']//parent::android.widget.RelativeLayout//android.widget.ImageView[@resource-id ='com.byjus.thelearningapp.premium:id/right_arrow']")
    video_practice_right_arrow = (By.XPATH,"//android.widget.TextView[@text = 'Practice']//parent::android.widget.RelativeLayout//android.widget.ImageView[@resource-id ='com.byjus.thelearningapp.premium:id/right_arrow']")
    #video_chapter_title_in_video_list = (By.XPATH,"//android.widget.TextView[@index = 3]")
    video_chapter_title_in_video_list =(By.ID,"com.byjus.thelearningapp.premium:id/chapter_title_2")

    video_test_objective = (By.XPATH,"//android.widget.TextView[@text = 'Objective Tests']")
    video_test_subjective = (By.XPATH,"//android.widget.TextView[@text = 'Subjective Tests']")
    video_chapter_title_library_screen = (By.XPATH,"//android.widget.LinearLayout[@index = 1 and @resource-id = 'com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.TextView[@resource-id = 'com.byjus.thelearningapp.premium:id/chapter_title_view']")
    bookmark_icon=(By.XPATH,("//androidx.recyclerview.widget.RecyclerView//android.widget.RelativeLayout[@index=0]//android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/ivBookmarkTag']"))
    chapterScreen_chapter_name = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/llHeaderTextParent']//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/header_title_text']")
    video_playback_speed_dialog = (By.XPATH,"//android.widget.TextView[@text ='Playback Speed']")
    video_playback_speed_frame = (By.ID,"com.byjus.thelearningapp.premium:id/design_bottom_sheet")
    video_practice_question_screen = (By.ID,"com.byjus.thelearningapp.premium:id/practiceProgressParent")
    grade_text_in_hamburger_list = (By.ID,"com.byjus.thelearningapp.premium:id/home_drawer_txtvw_course")
    
    
#     Journey Locators
    first_journey_card = (By.XPATH,"//android.widget.RelativeLayout[@resource-id='com.byjus.thelearningapp.premium:id/parent_layout']//android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/tvSubtopicName']")
    journey_start_btn = (By.ID,"com.byjus.thelearningapp.premium:id/btnPositive")
    test_screen_start_elements = (By.XPATH,"//android.widget.TextView[@text='Analyse']")
    test_screen_Test_btn = (By.ID,"com.byjus.thelearningapp.premium:id/test_start_button")
    test_submit_Btn = (By.ID,"com.byjus.thelearningapp.premium:id/rectangleNavButton")
    noneOftheAbove_xpath = (By.ID,"com.google.android.gms:id/cancel")
    video_title_journey = (By.ID,"com.byjus.thelearningapp.premium:id/labelVideoName")
    journey_video_continue_btn = (By.ID,"com.byjus.thelearningapp.premium:id/progressAutoPlay")
    journey_node_title = (By.ID,"com.byjus.thelearningapp.premium:id/node_title_text")
    jounney_video_nxt_btn =(By.XPATH,"//android.widget.Button[@text='Next']")
    
    
#    Gmail Share Locators
    Gmail_text=(By.XPATH,"//android.widget.TextView[@text='Gmail']")
    Gmail_to=(By.XPATH,"//android.widget.MultiAutoCompleteTextView")
    Gmail_send=(By.XPATH,'//android.widget.TextView[@content-desc="Send"]')
    Gmail_compose_txt=(By.XPATH,"//android.widget.TextView[@text='Compose']")
    Gmail_subject_text=(By.XPATH,'//android.widget.EditText[@text="BYJU\'S The Learning App"]')
    Gmail_tosend=(By.XPATH,"//android.widget.MultiAutoCompleteTextView[@resource-id='com.google.android.gm:id/to']")
    Gmail_compose_txt=(By.XPATH,"//android.widget.TextView[@text='Compose']")
    Gmail_body_text=(By.XPATH,'//*[contains(@resource-id, "wc_body_layout")]//android.widget.EditText')
    message_txt=(By.ID,"com.android.mms:id/embedded_text_editor")
    objective_test_list_xpath = (By.XPATH,
                                 "//android.widget.LinearLayout[@index=1]//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname']")
    subjective_test_list_xpath = (By.XPATH,
                                  "//android.widget.LinearLayout[@index=2]//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname']")
    
    def click_on_video(self, browser):
        browser.find_element_by_id(self.video).click() 
    
    def reset_app(self):
        CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')
        CommonMethods.run('adb shell am start -n com.byjus.thelearningapp.premium/com.byjus.app.onboarding.activity.SplashActivity')
       
       
    def restart_app(self):
        CommonMethods.run('adb shell am start -n com.byjus.thelearningapp.premium/com.byjus.app.onboarding.activity.SplashActivity')
    

    def login_the_user(self, browser, count):
        if count == False:
            self.reset_app()
            GenericMethods.navigate_to_login_page(browser, getdata(Login_Credentials, 'login_details', 'grade'))
            self.login_to_home_page(browser)
            self.navigate_to_home_screen(browser, getdata(Login_Credentials, 'login_details', 'subject'))
            self.switch_to_grade(browser, getdata(Login_Credentials, 'login_details', 'course'))
            logging.info("successfully App resgistered with new number")
            count = True
            return count
        else:
            logging.info("Already App is resgistered with user")
            
                
    def click_test_btn(self, browser):
        browser.find_element_by_id(self.Btn_test).click()
        
        
    def tap_on_skip_btn(self, browser):
        CommonMethods.elementClick(browser, self.overlay_skip_btn)
        
    def click_practice_btn(self, browser):
        browser.find_element_by_id(self.Btn_practice).click()

    def reset_and_login_with_otp(self, browser):
        CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')
        CommonMethods.run(
            'adb shell am start -n com.byjus.thelearningapp.premium/com.byjus.app.onboarding.activity.SplashActivity')
        CommonMethods.accept_notification(browser, self.allow_btn_id)
        CommonMethods.wait_for_locator(browser, self.loginPageVerify_id, 5)
        CommonMethods.elementClick(browser, self.loginPageVerify_id)
        CommonMethods.click_none_of_the_above(browser, self.none_of_the_above_id)
        CommonMethods.wait_for_locator(browser, self.country_Code, 5)
        CommonMethods.elementClick(browser, self.country_Code)
        sleep(2)
        CommonMethods.scrollToElementAndClick(browser, getdata(Login_Credentials, 'login_detail3'
                                                               , 'country_code'))
        CommonMethods.enterText(browser, getdata(Login_Credentials, 'login_detail3', 'mobile_no'),
                                self.phone_num)
        CommonMethods.wait_for_locator(browser, self.loginBtn_id, 15)
        CommonMethods.elementClick(browser, self.loginBtn_id)
        CommonMethods.wait_for_locator(browser, self.OtpTxtBx_id, 15)
        CommonMethods.enterText(browser, getdata(Login_Credentials, 'login_detail3', 'OTP'),
                                self.OtpTxtBx_id)
        if CommonMethods.wait_for_element_visible(browser, self.multiple_accounts_dialog, 5):
            profiles = CommonMethods.getElements(browser, self.user_profile_name)
            radio_buttons = CommonMethods.getElements(browser, self.profile_select_radio_button)
            for profile in profiles:
                for button in radio_buttons:
                    if profile.text == getdata(Login_Credentials, 'login_detail3', 'profile_name'):
                        button.click()
                        break
        CommonMethods.elementClick(browser, self.continue_button)
        CommonMethods.wait_for_locator(browser, self.welcome_button, 15)
        CommonMethods.elementClick(browser, self.welcome_button)

    def verify_home_page(self, browser):
        print("------------------------method")
        try:
            if CommonMethods.wait_for_element_visible(browser, self.back_button_id, 3):
                CommonMethods.elementClick(browser, self.back_button_id)
                CommonMethods.wait_for_locator(browser, self.profile_name_hamburger, 5)
                CommonMethods.elementClick(browser, self.profile_name_hamburger)
                CommonMethods.wait_for_locator(browser, self.user_name_profile_page, 5)
                account_text = CommonMethods.getTextOfElement(browser, self.account_details_title)
                CommonMethods.scrollToElement(browser, account_text)
                expected_mob_num = CommonMethods.getTextOfElement(browser, self.profile_mob_num)
                actual_mob_num = getdata(data_file, 'profile_credentials', 'mobileNum')
                if CommonMethods.verifyTwoText(actual_mob_num, expected_mob_num):
                    print("---------------above")
                    CommonMethods.click_on_device_back_btn(browser)
                    print("----------------------below")
                    logging.info('home page verified')
                else:
                    self.reset_and_login_with_otp(browser)
                    return True
            else:
                logging.info('user is not in Home page')
                return False
        except:
            logging.info('Error in Verifing Home Page')

    def allow_notifications(self, browser):
        if CommonMethods.wait_for_element_visible(browser, self.allow_btn_id, 5):
            CommonMethods.accept_notification(browser, self.allow_btn_id)
            CommonMethods.accept_notification(browser, self.allow_btn_id)
            
    def check_for_skip_btn(self, browser): 
        if CommonMethods.wait_for_element_visible(browser, self.skipBtn_id, 5):
            CommonMethods.elementClick(browser, self.skipBtn_id)
            CommonMethods.wait_for_element_visible(browser, self.chooseCourse_Title_xpath, 7)
            CommonMethods.elementClick(browser, getdata(data_file, 'profile_credentials', 'grade'))
            CommonMethods.wait_for_element_visible(browser, self.noneOftheAbove_xpath, 7)
            CommonMethods.elementClick(browser, self.noneOftheAbove_xpath)
            CommonMethods.elementClick(browser, self.login_link_id)
            
    def user_registration(self, browser):
        grade = getdata(data_file, 'profile_credentials', 'grade')
        sub_grade = (By.XPATH,"//android.widget.Button[@text=\'"+grade+"\']")
        if CommonMethods.wait_for_element_visible(browser, self.login_register_btn, 3):
            CommonMethods.elementClick(browser, self.login_register_btn)
            CommonMethods.wait_for_element_visible(browser, self.chooseCourse_Title_xpath, 7)
            CommonMethods.elementClick(browser, sub_grade)
            CommonMethods.wait_for_element_visible(browser, self.registration_name_field, 7)
            CommonMethods.enterText(browser, "testJ", self.registration_name_field)
            CommonMethods.wait_for_element_visible(browser, self.register_btn, 5)
            CommonMethods.elementClick(browser, self.register_btn)
            
    def login_to_home_page(self, browser):
        self.reset_and_login_with_otp(browser)
        
    def verify_to_login_page(self, browser):
        self.allow_notifications(browser)
        self.check_for_skip_btn(browser)
        self.login_to_home_page(browser)
        
            
    def verify_badge(self, browser):
        if CommonMethods.wait_for_element_visible(browser, self.video_badge_close_btn, 10):
            CommonMethods.elementClick(browser, self.video_badge_close_btn)
    
    def verify_corana_dialog(self, browser):
        if CommonMethods.wait_for_element_visible(browser, self.homescreen_corana_dialog_ok_btn, 10):
            CommonMethods.elementClick(browser, self.homescreen_corana_dialog_ok_btn)   
    
    def tap_on_device_back_btn(self, browser):
        sleep(3)
        CommonMethods.click_on_device_back_btn(browser)
        
    
    def tap_on_back_arrow_btn(self, browser):
        sleep(3)
        back_arrow = CommonMethods.getElement(browser, self.practice_back_arrow_btn)
        back_arrow.click()

    def navigate_to_home_screen(self, browser, text):
        try:
            sleep(10)
            subject_rgb = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")
            if CommonMethods.wait_for_element_visible(browser, self.homescreen_corana_dialog_ok_btn, 10):
                CommonMethods.elementClick(browser, self.homescreen_corana_dialog_ok_btn)
                self.verify_badge(browser)
                self.verify_home_page(browser)
                VideoPage.subject_rgb_lst = self.get_the_rgb_lst(browser, subject_rgb)
            elif CommonMethods.wait_for_element_visible(browser, self.back_button_id, 5):
                self.verify_badge(browser)
                self.verify_home_page(browser)
                VideoPage.subject_rgb_lst = self.get_the_rgb_lst(browser, subject_rgb)
            elif CommonMethods.wait_for_element_visible(browser, self.video_badge_close_btn, 5):
                self.verify_badge(browser)
            else:
                self.reset_and_login_with_otp(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigateToHomeScreen')
        except:
            CommonMethods.exception(browser, featureFileName, 'navigateToHomeScreen')
            
    def navigate_to_library(self, browser, sub):
        try:
            CommonMethods.wait_for_element_visible(browser, self.profile_header_id, 10)
            pythonSub_xpath =(By.XPATH,"//android.widget.TextView[@text=\'"+sub+"\']")
            CommonMethods.wait_for_element_visible(browser, pythonSub_xpath, 3)
            CommonMethods.elementClick(browser,pythonSub_xpath)
#             if CommonMethods.isElementPresent(browser, self.personalizeScreen_xpath):
#                 logging.info('successfully navigated to library')
#             else:
#                 for i in range(10):
#                     CommonMethods.run('adb shell input touchscreen swipe 300 300 300 800')
#                     check = CommonMethods.wait_for_element_visible(browser, self.librayBtn_id, 5)
#                     if check == True:
#                         break
#                 CommonMethods.wait_for_locator(browser, self.librayBtn_id, 10)
#                 CommonMethods.elementClick(browser,self.librayBtn_id)
#                 logging.info('successfully navigated to library')
            if CommonMethods.wait_for_element_visible(browser, self.verify_library_screen, 10):
                logging.info('successfully navigated to library')
            else:
                ele = CommonMethods.getElements(browser, self.chapter_screen_library_personalize_btn_elements)
                ele[1].click()
                logging.info('successfully navigated to library')            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'navigate_to_library')        
        except :
            CommonMethods.exception(browser,featureFileName,'navigate_to_library')
            
    
    def navigate_to_personalised_Screen(self, browser, sub):
        try:
            CommonMethods.wait_for_element_visible(browser, self.profile_header_id, 10)
            pythonSub_xpath =(By.XPATH,"//android.widget.TextView[@text=\'"+sub+"\']")
            CommonMethods.wait_for_element_visible(browser, pythonSub_xpath, 3)
            CommonMethods.elementClick(browser,pythonSub_xpath)
#             if not CommonMethods.wait_for_element_visible(browser, self.verify_library_screen, 10):
#                 logging.info('successfully navigated to Personalized chapter screen')
#             else:
#                 CommonMethods.wait_for_element_visible(browser, self.chapter_screen_library_personalize_btn, 10)
#                 CommonMethods.elementClick(browser, self.chapter_screen_library_personalize_btn)
#                 logging.info('successfully navigated to Personalized chapter screen')  
                
            if not CommonMethods.wait_for_element_visible(browser, self.verify_library_screen, 10):
                logging.info('successfully navigated to library')
            else:
                ele = CommonMethods.getElements(browser, self.chapter_screen_library_personalize_btn_elements)
                ele[1].click()
                logging.info('successfully navigated to library') 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'navigate_to_personalised_Screen')        
        except :
            CommonMethods.exception(browser,featureFileName,'navigate_to_personalised_Screen')

    def tap_on_chapter(self, browser, sub):
        try:
            CommonMethods.wait_for_element_visible(browser, self.profile_header_id, 10)
            pythonSub_xpath =(By.XPATH,"//android.widget.TextView[@text=\'"+sub+"\']")
            CommonMethods.wait_for_element_visible(browser, pythonSub_xpath, 3)
            CommonMethods.elementClick(browser,pythonSub_xpath)
            sleep(5)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_chapter')
        
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_chapter')
            
    def navigateToSubjectLib2(self,browser,sub):
        try:
            browser.start_activity("com.android.chrome","com.google.android.apps.chrome.Main")  
            browser.get("https://app.byjus.com/fp1RtHwywC?infoParam=7329")
        except:
            pytest.fail("Activity Failed To start")
            
    def tap_on_any_video_in_sub_screen(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                sleep(3)
                ele = CommonMethods.getElements(browser, self.chapter_videoLnk_elements)
                ele_length = len(ele)
                n = random.randint(1,ele_length-1)
                ele[n].click()
                logging.info("video is selected")     
            elif  device == 'tab':
                sleep(3)
                ele = CommonMethods.getElements(browser, self.tab_chapter_videoLnk_elements)
                ele_length = len(ele)
                n = random.randint(1,ele_length-1)
                ele[n].click()
                logging.info("video is selected")     
            else:
                logging.info("Failed Locator in Method tap_on_any_video_in_sub_screen")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail('Failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_any_video_in_sub_screen')
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_any_video_in_sub_screen')
    
    
    def tap_on_any_journey_card_in_sub_screen(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                for i in range(5):
                    CommonMethods.run('adb shell input touchscreen swipe 300 300 300 800')
                CommonMethods.wait_for_element_visible(browser, self.first_journey_card, 10)
                ele = CommonMethods.getElements(browser, self.first_journey_card)
                ele[0].click()
            elif  device == 'tab':
                for i in range(5):
                    CommonMethods.run('adb shell input touchscreen swipe 300 300 300 800')
                CommonMethods.wait_for_element_visible(browser, self.first_journey_card, 10)
                ele = CommonMethods.getElements(browser, self.first_journey_card)
                ele[0].click()
            else:
                logging.info("Failed Locator in Method tap_on_any_video_in_sub_screen")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail('Failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_any_journey_card_in_sub_screen')
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_any_journey_card_in_sub_screen')
            
            
    def tap_on_start_video(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                CommonMethods.wait_for_element_visible(browser, self.journey_start_btn, 60)
                CommonMethods.elementClick(browser, self.journey_start_btn)
            elif  device == 'tab':
                logging.info("handle")
            else:
                logging.info("Failed Locator in Method tap_on_start_video")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail('Failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_start_video')
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_start_video')
    
    
    def verify_video_playing(self,browser):
        try:   
            if CommonMethods.wait_for_element_visible(browser, self.video_list_btn_tab, 3) or CommonMethods.wait_for_element_visible(browser, self.video_list_close_btn_tab, 3):
                pass  
            sleep(3)
            check2 = CommonMethods.isElementPresent(browser,self.videoPlayingNow_xpath)
            CommonMethods.elementClick(browser, self.video1stLink_xpath)
            sleep(2)
            CommonMethods.elementClick(browser, self.video1stLink_xpath)
            check1 = CommonMethods.isElementPresent(browser,self.video_pause_btn_id) 
            if check1 or check2 :
                logging.info('video is playing successfully')
            else:
                logging.info("Failed Locator in Method verify_video_playing")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail('Failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_playing')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_playing')
            
    def verify_reply_next_previous_btn(self, browser):
        try:   
            check1 = CommonMethods.isElementPresent(browser, self.video_play_btn)
            check2 = CommonMethods.isElementPresent(browser, self.video_play_previous_btn)
            check3 = CommonMethods.isElementPresent(browser, self.video_play_next_btn)
            self.verify_true_or_false(browser, check1, 'verify_reply_next_previous_btn', 'Reply Btn')
            self.verify_true_or_false(browser, check2, 'verify_reply_next_previous_btn', 'Previous Btn')
            self.verify_true_or_false(browser, check3, 'verify_reply_next_previous_btn', 'Next Btn')
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_reply_next_previous_btn')
            
        except :
            CommonMethods.exception(browser,featureFileName,'verify_reply_next_previous_btn')
            
    def tap_on_pause_btn(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                self.wait_till_video_load(browser)
                self.click_on_video_icon(browser, self.video_pause_btn_id)
                VideoPage.video_start_time = CommonMethods.getTextOfElement(browser, self.progressTime_id)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_pause_btn')
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_pause_btn')
    
    def tap_on_player_screen(self):
        CommonMethods.run('adb shell input tap 40 200')
            
    def verify_play_btn_in_lanscape(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                check = CommonMethods.isElementPresent(browser, self.video_play_btn)
                self.verify_true_or_false(browser, check, 'verify_play_btn_in_lanscape', 'Video play button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_play_btn_in_lanscape')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_play_btn_in_lanscape')
            
            
    def drag_video_progress_bar_right(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                VideoPage.video_start_time = self.get_video_start_time(browser)
                self.seek_video_50_percent(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'drag_video_progress_bar_right')
        except :
            CommonMethods.exception(browser,featureFileName,'drag_video_progress_bar_right')
            
    def verify_video_paused(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                if CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 3):
                    logging.info('video Paused Successfully')
                else:
                    logging.info("Failed Locator in Method verify_video_paused")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            elif device == 'mobile':
                check = CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 10)
                self.verify_true_or_false(browser, check, 'verify_video_paused', 'pause btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_paused')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_paused') 
            
            
    def verify_video_is_not_paused(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                if CommonMethods.wait_for_element_visible(browser, self.video_pause_btn_id, 3):
                    logging.info('video Paused Successfully')
                else:
                    logging.info("Failed Locator in Method verify_video_paused")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            elif device == 'mobile':
                check = self.is_video_icon_present(browser, self.video_pause_btn_id)
            self.verify_true_or_false(browser, check, 'verify_video_title', 'video Title')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_paused')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_paused')
            
    def tap_on_playbtn(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                VideoPage.video_start_time = self.get_video_start_time(browser)
                if CommonMethods.elementClick(browser, self.video_play_btn):
                    logging.info('taped on play button successfully')       
            elif device == 'mobile':
                check = CommonMethods.elementClick(browser,self.video_play_btn)
                if check == True:
                    pass
                else:
                    logging.info('Failed to tap on Play Button')
                    pytest.fail('Failed to tap on Play Button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_playbtn')
        
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_playbtn')
            
    def custom_wait(self, sec):
        try:
            sec = int(sec)
            sleep(sec)
        except:
            logging.info("failed in Custom Wait")
            pytest.fail('Failed')
            
    def verify_frwd_10Sec(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                start_time = self.get_video_start_time(browser)
                self.tap_on_video_player_icon(browser, self.ten_sec_fwd_btn_id)
                self.wait_till_video_load(browser)
                end_time = self.get_video_start_time(browser)
                if end_time >= start_time+10:
                    logging.info('video forwaded 10 sec')   
                else:
                    logging.info("Failed Locator in Method verify_frwd_10Sec")
                    CommonMethods.takeScreenShot(self,browser,featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page") 
            elif device == 'mobile':
                start_time = self.get_video_start_time(browser)
                self.tap_on_video_player_icon(browser, self.ten_sec_fwd_btn_id)
                self.wait_till_video_load(browser)
                end_time = self.get_video_start_time(browser)
                if end_time >= start_time+10:
                    logging.info('video forwaded 10 sec')   
                else:
                    logging.info("Failed Locator in Method verify_frwd_10Sec")
                    CommonMethods.takeScreenShot(self,browser,featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page") 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_frwd_10Sec')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_frwd_10Sec') 
            
    def tap_on_video_player_icon(self, browser, locator):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 20:
                wait_count += 1 
                CommonMethods.elementClick(browser, self.video_tab_videoframe) 
                flag = CommonMethods.elementClick(browser, locator)
                check = not flag
        except:
            logging.info('Error in clicking the video player icon')
            
    def verify_video_backwrd_10Sec(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                start_time = self.get_video_start_time(browser)
                self.tap_on_video_player_icon(browser, self.ten_sec_bkwd_btn_id)
                self.wait_till_video_load(browser)
                end_time = self.get_video_start_time(browser)
                logging.info(start_time)
                logging.info(end_time)
                if end_time < start_time:
                    logging.info('video Backward 10 sec')   
                else:
                    logging.info("Failed Locator in Method verify_video_backwrd_10Sec")
                    CommonMethods.takeScreenShot(self,browser,featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page") 
            elif device == 'mobile':
                start_time = self.get_video_start_time(browser)
                self.tap_on_video_player_icon(browser, self.ten_sec_bkwd_btn_id)
                self.wait_till_video_load(browser)
                end_time = self.get_video_start_time(browser)
                logging.info(start_time)
                logging.info(end_time)
                if end_time < start_time:
                    logging.info('video Backward 10 sec')   
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_backwrd_10Sec')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_backwrd_10Sec')
            
            
    def tap_on_device_home_btn(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                VideoPage.videoProgressTimeBfr = self.get_video_start_time(browser)
                CommonMethods.click_on_device_home_btn()
            elif device == 'mobile':
                VideoPage.videoProgressTimeBfr = self.get_video_start_time(browser)
                CommonMethods.click_on_device_home_btn()
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_device_home_btn')
        
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_device_home_btn')
            
    def take_app_foreground(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                if CommonMethods.take_app_foreground(browser,self.byjusAppPackage):
                    logging.info('App taken to foreground')
                else:
                    logging.info("Failed Locator in Method take_app_foreground")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            elif device == 'mobile':
                if CommonMethods.take_app_foreground(browser,self.byjusAppPackage):
                    pass
                else:
                    logging.info("Failed Locator in Method take_app_foreground")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'viewAppForeground')
        
        except :
            CommonMethods.exception(browser,featureFileName,'viewAppForeground')
            
    def navigateToLoginPage(self,browser):
        try: 
            if CommonMethods.wait_for_element_visible(browser, self.skipBtn_id, 2):
                browser.find_element_by_id("com.byjus.thelearningapp.premium:id/buttonSkip").click()
                browser.find_element_by_xpath("//android.widget.Button[@text='8th']").click()
                browser.find_element_by_id("com.byjus.thelearningapp.premium:id/tvLoginBl").click()
            else:
                logging.error("failed to navigate to login page")  
        except:
            logging.info('Exception occured While bringing the app foreground')
                
    def verify_video_playing_from_last_progress(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
#                 logging.info('entered tab')
#                 sleep(2)
#                 video_before_time =  self.videoProgressTimeBfr
#                 logging.info('taken time'+video_before_time)
#                 self.wait_till_video_load(browser)
#                 videoProgressTimeAfter = self.get_video_start_time(browser)
#                 logging.info('taken after time'+videoProgressTimeAfter)
#                 sleep(2)
#                 if videoProgressTimeAfter >= video_before_time:
#                     logging.info('Video Resumed From last Progress')
#                     pass
#                 else:
#                     logging.info("Failed Locator in Method verify_video_playing_from_last_progress")
#                     CommonMethods.takeScreenShot(browser,featureFileName)
#                     pytest.fail("Failed Due to Locator in Video Page")
                actual = self.get_video_start_time(browser)
                self.wait_till_video_load(browser)
                expected = VideoPage.video_start_time
                check = actual >= expected
                self.verify_true_or_false(browser, check, 'verify_video_playing_from_last_progress', "video time")
            elif device == 'mobile':
                sleep(2)
                video_before_time =  VideoPage.videoProgressTimeBfr
                self.wait_till_video_load(browser)
                videoProgressTimeAfter = self.get_video_start_time(browser)
                sleep(2)
                if videoProgressTimeAfter >= video_before_time:
                    logging.info('Video Resumed From last Progress')
                else:
                    logging.info("Failed Locator in Method verify_video_playing_from_last_progress")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_playing_from_last_progress')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_playing_from_last_progress')        

    def change_orientation_landscape(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == "tab":
                logging.info('video will always play in landscape mode')
            elif device == "mobile":
                VideoPage.video_start_time_portrait = self.get_video_start_time(browser)
                check = self.click_on_video_icon(browser, self.screen_orientation_id)
#                 check = self.tap_on_video_player_icon(browser, self.screen_orientation_id)
                if check == True:
                    logging.info('device set to landscape')
                else:
                    self.test_fail(browser, 'change_orientation_landscape')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'change_orientation_landscape')
        
        except :
            CommonMethods.exception(browser,featureFileName,'change_orientation_landscape') 
            
    def change_orientation_potrait(self, browser):
        try:
            VideoPage.video_start_time_landscape = self.get_video_start_time(browser)
            check = self.click_on_video_icon(browser, self.screen_orientation_id)
            self.verify_true_or_false(browser, check, 'change_orientation_potrait', 'screen toggle')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'change_orientation_landscape')
        except :
            CommonMethods.exception(browser,featureFileName,'change_orientation_landscape')
            
            
    def seek_the_video_player_to_50percent(self, browser):
        try:
            before_start_time = self.get_video_start_time(browser)
            self.pause_video(browser)
            x1,y1,x2,y2 = self.get_element_coordinates(browser, self.video_progressBar_id)
            x2 = x2/2
            y2 = y2/2
            CommonMethods.run('adb shell input touchscreen swipe {} {} {} {}'.format(x1, y1, x2, y2))
            self.tap_on_video_player_icon(browser, self.video_play_btn)
            after_start_time = self.get_video_start_time(browser)
            check = after_start_time > before_start_time +10
            self.verify_true_or_false(browser, check, 'seek_the_video_player_to_50percent', 'seek bar')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'seek_the_video_player_to_50percent')
        except :
            CommonMethods.exception(browser,featureFileName,'seek_the_video_player_to_50percent')  
            
    def verify_video_continue_without_pausing(self, browser):
        try:
            check = self.is_video_icon_present(browser, self.video_pause_btn_id)
            self.verify_true_or_false(browser, check, 'verify_video_continue_without_pausing', 'play button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_continue_without_pausing')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_continue_without_pausing')
        
    
    def is_video_paused(self, browser):
        if CommonMethods.wait_for_element_visible(browser, self.video_pause_btn_id, 5):
            return True
        else:
            return False
    
    def wait_till_video_load(self, browser):
        browser.implicitly_wait(0.1)
        loading_count = 0
        try:
            while CommonMethods.wait_for_element_visible(browser, self.video_buffering, 2) and loading_count < 75:
                loading_count += 1
                sleep(0.2)
            logging.info('video Loading done successfully')
        except:
            logging.info("Error in waiting for video to load")
        
    def wait_till_element_visible(self, browser, locator):
        browser.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.wait_for_element_visible(browser, locator, 1) and loading_count < 75:
                loading_count += 1
                sleep(0.2)
            logging.info('video Loading done successfully')
        except:
            logging.info('Error in waiting for the element')
        
    def wait_till_video_complete(self, browser, time):
        browser.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 2) and loading_count < time+100:
                loading_count += 1
                sleep(0.2)
            return True
        except:
            logging.error('Error in playing the video completely')
                
    
    def pause_video(self,browser):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1 
                CommonMethods.elementClick(browser, self.video_tab_videoframe) 
                CommonMethods.elementClick(browser, self.video_pause_btn_id)
                flag = CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 5)
                check = not flag
        except:
            logging.info('Error in pausing the video')
            
    def play_video(self,browser):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1 
                CommonMethods.elementClick(browser, self.video_tab_videoframe) 
                if CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 3):
                    CommonMethods.elementClick(browser, self.video_play_btn)
                flag = self.is_video_icon_present(browser, self.video_pause_btn_id)
                check = not flag
        except:
            logging.info('Error in pausing the video')
        
    def get_x_y_coordinate(self, browser, locator):
        locator = locator
        loc = CommonMethods.get_element_location(browser, locator)
        x = loc["x"]
        y = loc["y"]
        return x,y
    
    def get_element_coordinates(self, browser, locator):
        try:
            loc = CommonMethods.get_size_of_element(browser, locator)
            x = loc['x']
            y = loc['y']
            height = loc['height']
            width = loc['width']
            x2 = x+width
            y2 = y+height
            return x,y,x2,y2
        except:
            return None,None,None,None
    
    def click_on_x_y_coordinate(self, x, y):
        try:
            CommonMethods.run('adb shell input tap {} {}'.format(x, y))
            return True
        except:
            return False
              
    def verify_video_back_btn(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(browser, self.video_backBtn_id)
                self.verify_true_or_false(browser, check, 'verify_video_back_btn', 'video back Button')
            elif device == 'mobile':    
                CommonMethods.wait_for_locator(browser, self.video_backBtn_id, 5)
                check = CommonMethods.isElementPresent(browser, self.video_backBtn_id)
                if check == True:
                    pass
                else:
                    logging.info("Failed due to Element not visible in Method verify_video_back_btn")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_back_btn')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_back_btn') 
            
            
    def verify_video_card_opened(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.video_frame_id, 10)
            self.verify_true_or_false(browser, check, 'verify_video_card_opened', 'Video screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_back_btn')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_back_btn')  
            
    """checks for video buffering icon if present the method will be passed if not present the method will fail"""        
    def verify_video_buffering(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.video_buffering, 10)
            self.verify_true_or_false(browser, check, 'verify_video_buffering', 'Video buffering')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_buffering')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_buffering')  
              
    def tap_on_app_back_button(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.video_backBtn_id, 5)
            check = CommonMethods.elementClick(browser, self.video_backBtn_id)
            self.verify_true_or_false(browser, check, 'tap_on_app_back_button', "app back button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_app_back_button')
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_app_back_button')
     
    def verify_speedBtn(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(browser, self.videoSpeed_up_dwnIcon_id)
                self.verify_true_or_false(browser, check, 'verify_speedBtn', 'video speed up down icon')
#             elif device == 'mobile':
#                 CommonMethods.wait_for_locator(browser, self.videoSpeed_up_dwnIcon_id, 5)
#                 check = CommonMethods.isElementPresent(browser, self.videoSpeed_up_dwnIcon_id)
#                 if check == True:
#                     pass
#                 else:
#                     logging.info("Failed due to Element not visible in Method verify_speedBtn")
#                     CommonMethods.takeScreenShot(browser,featureFileName)
#                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_speedBtn')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_speedBtn') 
            
            
    def verify_question_page(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.video_practice_question_screen, 10)
            self.verify_true_or_false(browser, check, 'verify_question_page', 'question screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_question_page')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_question_page') 
            
            
    def verify_app_redirected_to_journey_screen(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.journey_video_continue_btn, 10)
            self.verify_true_or_false(browser, check, 'verify_app_redirected_to_journey_screen', 'journey Screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_app_redirected_to_journey_screen')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_app_redirected_to_journey_screen') 
            
            
    def verify_subtitile(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(browser, self.videoSpeed_up_dwnIcon_id)
#             elif device == 'mobile':
#                 CommonMethods.wait_for_locator(browser, self.video_subtitileIcon_id, 5)
#                 check = CommonMethods.isElementPresent(browser, self.video_subtitileIcon_id)
#                 if check == True:
#                     pass
#                 else:
#                     logging.info("Failed due to Element not visible in Method verify_subtitile")
#                     CommonMethods.takeScreenShot(browser,featureFileName)
#                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_subtitile')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_subtitile') 
            
    def verify_multipleAudio(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(browser, self.video_mutipleAudioTracks_id)
                self.verify_true_or_false(browser, check, 'verify_multipleAudio', 'Mutiple Audio Icon')
#             elif device == 'mobile':
#                 CommonMethods.wait_for_locator(browser, self.video_mutipleAudioTracks_id, 5)
#                 check = CommonMethods.isElementPresent(browser, self.video_mutipleAudioTracks_id)
#                 if check == True:
#                     pass
#                 else:
#                     logging.info("Failed due to Element not visible in Method verify_multipleAudio")
#                     CommonMethods.takeScreenShot(browser,featureFileName)
#                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_multipleAudio')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_multipleAudio') 
            
    def verify_setting_icon(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(browser, self.video_settingIcon_id)
                self.verify_true_or_false(browser, check, 'verify_setting_icon', 'video setting Icon')
#             elif device == 'mobile':
#                 CommonMethods.wait_for_locator(browser, self.video_settingIcon_id, 5)
#                 check = CommonMethods.isElementPresent(browser, self.video_settingIcon_id)
#                 if check == True:
#                     pass
#                 else:
#                     logging.info("Failed due to Element not visible in Method verify_setting_icon")
#                     CommonMethods.takeScreenShot(browser,featureFileName)
#                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_setting_icon')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_setting_icon')
            
    def verify_text_present(self,browser,text):
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
            
    def tap_on_text_lnk(self, browser, text):
        try:
            ele = CommonMethods.find_element_of_radio_btn(browser, text)
            ele.click()
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyTextPresent')           
        except :
            CommonMethods.exception(browser,featureFileName,'verifyTextPresent') 
            
            
    def tap_on_test_in_chapter_screen(self, browser):
        try:
            CommonMethods.scrollToElementAndClick(browser, 'Test')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_test_in_chapter_screen')           
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_test_in_chapter_screen')
            
    def verify_radio_btn_text_present(self,browser,text):
        try:
            check = CommonMethods.find_radio_btn(browser,text)
            if check == True:
                logging.info(text+' is present and verified')
            else:
                logging.error('Failed in Finding the text '+text)
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed in login page")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_radio_btn_text_present')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verify_radio_btn_text_present')
            
            
    def verify_speed_down_compare_to_normal(self, browser):
        try:
            sleep(3)
            start_time = self.get_video_start_time(browser)
            sleep(16)
            end_time = self.get_video_start_time(browser)
            check = (end_time - start_time) <= 16 
            self.verify_true_or_false(browser, check, 'verify_speed_down_compare_to_normal', '0.75x is shown')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_speed_down_compare_to_normal')         
        except :
            CommonMethods.exception(browser,featureFileName,'verify_speed_down_compare_to_normal')
            
            
    def verify_speed_down_compare_to_075x(self, browser):
        try:
            sleep(3)
            start_time = self.get_video_start_time(browser)
            sleep(16)
            end_time = self.get_video_start_time(browser)
            check = (end_time - start_time) <=  12 
            self.verify_true_or_false(browser, check, 'verify_speed_down_compare_to_075x', '0.5x is shown')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_speed_down_compare_to_075x')         
        except :
            CommonMethods.exception(browser,featureFileName,'verify_speed_down_compare_to_075x')
            
    def verify_speed_up_compare_to_normal(self, browser):
        try:
            self.wait_till_video_load(browser)
            start_time = self.get_video_start_time(browser)
            self.play_video(browser)
            sleep(16)
            end_time = self.get_video_start_time(browser)
            check = (end_time - start_time) >= 16 
            self.verify_true_or_false(browser, check, 'verify_speed_up_compare_to_normal', '1.25x is shown')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_speed_up_compare_to_normal')         
        except :
            CommonMethods.exception(browser,featureFileName,'verify_speed_up_compare_to_normal')
            
            
    def verify_speed_up_compare_to_125x(self, browser):
        try:
            sleep(3)
            start_time = self.get_video_start_time(browser)
            self.play_video(browser)
            sleep(16)
            end_time = self.get_video_start_time(browser)
            check = (end_time - start_time) >= 18
            self.verify_true_or_false(browser, check, 'verify_speed_up_compare_to_125x', '1.5x is shown')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_speed_up_compare_to_125x')         
        except :
            CommonMethods.exception(browser,featureFileName,'verify_speed_up_compare_to_125x')
            
    def verify_selected_playback_speed(self,browser,text):
        try:
            sleep(3) # need to wait till the video loads
            self.wait_till_video_load(browser)
            element = CommonMethods.find_element_of_radio_btn(browser,text)
            check = bool(element.get_attribute('checked').capitalize())
            self.verify_true_or_false(browser, check, 'verify_selected_playback_speed', text)        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_selected_playback_speed')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verify_selected_playback_speed')
            
            
    def verify_playback_speed_buttom_sheet(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.video_playback_speed_frame)
            self.verify_true_or_false(browser, check, 'verify_playback_speed_buttom_sheet', "play back speed bottom dialog")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_playback_speed_buttom_sheet')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verify_playback_speed_buttom_sheet')       
            
    def tap_on_playback_speed_icon(self,browser):
        try:
#             device = CommonMethods.get_device_type(browser)
#             if device == 'mobile':
            CommonMethods.wait_for_element_visible(browser, self.videoSpeed_up_dwnIcon_id, 10)
            self.tap_on_video_player_icon(browser, self.videoSpeed_up_dwnIcon_id)
            check = CommonMethods.wait_for_element_visible(browser, self.video_playback_speed_dialog, 5) 
            self.verify_true_or_false(browser, check, 'tap_on_playback_speed_icon', 'Playback speed Text')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_playback_speed_icon')
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_playback_speed_icon')
            
    def verify_play_pause_Icon(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(browser, self.video_play_pause_btn)
                self.verify_true_or_false(browser, check, 'verify_play_pause_Icon', 'video play/pause')
#             elif device == 'mobile':
#                 CommonMethods.wait_for_locator(browser, self.video_play_btn, 5)
#                 check = CommonMethods.isElementPresent(browser, self.video_play_btn)
#                 if check == True:
#                     pass
#                 else:
#                     logging.info("Failed due to Element not visible in Method verify_play_pause_Icon")
#                     CommonMethods.takeScreenShot(browser,featureFileName)
#                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_play_pause_Icon')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_play_pause_Icon')
            
    def verify_fastFrwd(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(browser, self.ten_sec_bkwd_btn_id)
                self.verify_true_or_false(browser, check, 'verify_fastFrwd', 'video fast forward Icon')
                check = self.is_video_icon_present(browser, self.video_10s_frwrd_text)
                self.verify_true_or_false(browser, check, 'verify_fastFrwd', '10 sec video fast forward Text')
#             elif device == 'mobile':
#                 CommonMethods.wait_for_locator(browser, self.ten_sec_bkwd_btn_id, 5)
#                 check1 = CommonMethods.isElementPresent(browser, self.ten_sec_bkwd_btn_id)
#                 check2 = CommonMethods.isElementPresent(browser, self.ten_sec_fwd_btn_id)
#                 if check1 and check2:
#                     pass
#                 else:
#                     logging.info("Failed due to Element not visible in Method verify_fastFrwd")
#                     CommonMethods.takeScreenShot(browser,featureFileName)
#                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_fastFrwd')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_fastFrwd')
            
    def verify_fast_backwrd_icon(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(browser, self.ten_sec_bkwd_btn_id)
                self.verify_true_or_false(browser, check, 'verify_fast_backwrd_icon', 'video fast backward')
                check = self.is_video_icon_present(browser, self.video_10s_bckwrd_text)
                self.verify_true_or_false(browser, check, 'verify_fast_backwrd_icon', '10 sec video fast backward Text')
#             elif device == 'mobile':
#                 CommonMethods.wait_for_locator(browser, self.ten_sec_bkwd_btn_id, 5)
#                 check1 = CommonMethods.isElementPresent(browser, self.ten_sec_bkwd_btn_id)
#                 check2 = CommonMethods.isElementPresent(browser, self.ten_sec_fwd_btn_id)
#                 if check1 and check2:
#                     pass
#                 else:
#                     logging.info("Failed due to Element not visible in Method verify_fastFrwd")
#                     CommonMethods.takeScreenShot(browser,featureFileName)
#                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_fastFrwd')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_fastFrwd')
            
    def verify_video_progress_bar(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab' or 'mobile':
                check = self.is_video_icon_present(browser, self.video_progress_tab_id)
                self.verify_true_or_false(browser, check, 'verify_video_progress_bar', 'video progress bar')
#             elif device == 'mobile':
#                 CommonMethods.wait_for_locator(browser, self.video_progressBar_id, 5)
#                 check = CommonMethods.isElementPresent(browser, self.video_progressBar_id)
#                 if check == True:
#                     pass
#                 else:
#                     logging.info("Failed due to Element not visible in Method verify_video_progress_bar")
#                     CommonMethods.takeScreenShot(browser,featureFileName)
#                     pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_progress_bar')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_progress_bar')
            
    def verify_video_fullScreen_icon(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                logging.info('Tab has no portrait mode')
            elif device == 'mobile':
                check = self.is_video_icon_present(browser, self.screen_orientation_id)
                self.verify_true_or_false(browser, check, 'verify_video_fullScreen_icon', 'orientation toggle bar')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_fullScreen_icon')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_fullScreen_icon')
            
#     def tap_on_pause_btn(self,browser):
#         try:
#             sleep(3)
#             orientation = CommonMethods.get_screen_orientation(browser)
#             loc = CommonMethods.get_element_location(browser, self.videoPlayBtn_id)
#             x = loc["x"]
#             y = loc["y"]
#             CommonMethods.elementClick(browser, self.videoPlayBtn_id)
#             CommonMethods.run('adb shell input tap {} {}'.format(x, y))
#             CommonMethods.run('adb shell input tap {} {}'.format(x, y))
#             if orientation == 'LANDSCAPE':
#                 pass
#             else:
#                 logging.info("Failed Locator in Method tap_on_pause_btn")
#                 CommonMethods.takeScreenShot(browser, featureFileName)
#                 pytest.fail("Failed Due to Locator in Video Page")
#         except NoSuchElementException:
#             CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_pause_btn')
#         
#         except :
#             CommonMethods.exception(browser,featureFileName,'tap_on_pause_btn')
            
    def tap_on_video_from_video_list(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            
            if device == 'mobile':
                if not CommonMethods.wait_for_element_visible(browser, self.videoPlayingNow_xpath, 5):
                    CommonMethods.elementClick(browser, self.video_tab_video_lst_1st_video)
                
            elif device == 'tab':
                CommonMethods.wait_for_locator(browser, self.video_list_lnk_xpath, 3)
                CommonMethods.elementClick(browser, self.video_list_lnk_xpath)
                
            else:
                logging.info("Failed due to Element not visible in Method tap_on_video_from_video_list")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_video_from_video_list')
        
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_video_from_video_list')
    
    """This method is written to verify the video playing in this we will be inspecting x y coordinates of pause btn
    and taken the time video will be palyed for 10 sec and we will check the difference and pass the method"""        
    def video_should_played(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                if CommonMethods.wait_for_element_visible(browser, self.video_tab_video_player_close_btn, 5):
                    CommonMethods.elementClick(browser, self.video_tab_video_lst_1st_video)
                    if CommonMethods.wait_for_element_visible(browser, self.video_tab_video_player_close_btn, 5):
                        CommonMethods.elementClick(browser, self.video_tab_video_player_close_btn)
                self.wait_till_video_load(browser)
                before_video_time = self.get_video_start_time(browser)
                sleep(10)
                after_video_time = self.get_video_start_time(browser)
                if after_video_time > before_video_time:
                    logging.info('Video is playing successfully')
                else:
                    logging.info("Failed due to Element not visible in Method video_should_played")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
            elif device == 'mobile':
#                 CommonMethods.wait_for_element_visible(browser, self.video_buffering, 20)
                self.wait_till_video_load(browser)
                self.pause_video(browser)
                x,y = self.get_x_y_coordinate(browser, self.video_progressBar_id)
                CommonMethods.run('adb shell input tap {} {}'.format(x,y))
                self.wait_till_video_load(browser)
                before_video_time = self.get_video_start_time(browser)
                sleep(10)
                after_video_time = self.get_video_start_time(browser)
                if after_video_time > before_video_time:
                    logging.info('Video is playing successfully')
                else:
                    logging.info("Failed due to Element not visible in Method video_should_played")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'video_should_played')
        
        except :
            CommonMethods.exception(browser,featureFileName,'video_should_played')
            
    """This method is written to verify the video playing in this we will be inspecting x y coordinates of pause btn
    and taken the time video will be palyed for 10 sec and we will check the difference and pass the method"""        
    def Video_should_played(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                if CommonMethods.wait_for_element_visible(browser, self.video_tab_video_player_close_btn, 2):
                    CommonMethods.elementClick(browser, self.video_tab_video_lst_1st_video)
                    if CommonMethods.wait_for_element_visible(browser, self.video_tab_video_player_close_btn, 2):
                        CommonMethods.elementClick(browser, self.video_tab_video_player_close_btn)
                self.wait_till_video_load(browser)
                before_video_time = self.get_video_start_time(browser)
                sleep(10)
                after_video_time = self.get_video_start_time(browser)
                if after_video_time > before_video_time:
                    logging.info('Video is playing successfully')
                else:
                    logging.info("Failed due to Element not visible in Method video_should_played")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
            elif device == 'mobile':
                self.wait_till_video_load(browser)
                self.tap_on_video_player_icon(browser, self.video_pause_btn_id)
#                 self.pause_video(browser)
                x,y = self.get_x_y_coordinate(browser, self.video_progressBar_id)
                CommonMethods.run('adb shell input tap {} {}'.format(x,y))
                self.wait_till_video_load(browser)
                before_video_time = self.get_video_start_time(browser)
                sleep(10)
                after_video_time = self.get_video_start_time(browser)
                if after_video_time > before_video_time:
                    logging.info('Video is playing successfully')
                else:
                    logging.info("Failed due to Element not visible in Method video_should_played")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'video_should_played')
        except :
            CommonMethods.exception(browser,featureFileName,'video_should_played')
            
    def verify_video_playing_in_landscape(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                orientation = CommonMethods.get_screen_orientation(browser)
                check = orientation == 'LANDSCAPE'
                self.verify_true_or_false(browser, check, 'verify_video_playing_in_landscape', "Landscape")
            elif device == 'mobile':
#                 check1 = not CommonMethods.wait_for_element_visible(browser, self.video_player_list_lay, 3)
                sleep(3)
                orientation = CommonMethods.get_screen_orientation(browser)
                check = orientation == 'LANDSCAPE'
                if check == True:
                    self.Video_should_played(browser)
                    VideoPage.video_start_time_landscape = self.get_video_start_time(browser)

                else:
                    logging.info("Failed due to Element not visible in Method verify_video_playing_in_landscape")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_playing_in_landscape')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_playing_in_landscape')
            
    def verify_video_in_potrait(self, browser):
        try: 
            self.video_should_played(browser)
            check  = self.is_video_icon_present(browser, self.video_pause_btn_id)
            self.video_start_time = self.get_video_start_time(browser) 
            check1 = CommonMethods.wait_for_element_visible(browser, self.video_player_list_lay, 3)
            check2 = CommonMethods.wait_for_element_visible(browser, self.video_frame_id, 3)
            if check and check1 and check2:
                logging.info('Video is played successfully in portrait')
            else:
                logging.info("Failed due to Element not visible in Method video_should_played")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_in_potrait')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_in_potrait')
            
    def video_play_without_any_interruption_in_landscape(self, browser):
        try:
            video_start_time_landscape = self.get_video_start_time(browser)
            check = video_start_time_landscape > VideoPage.video_start_time_portrait
            self.verify_true_or_false(browser, check, 'video_play_without_any_interruption_in_landscape', 'Potrait time')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_in_potrait')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_in_potrait')   
            
    def video_play_without_any_interruption_in_potrait(self, browser):
        try:
#             video_time_landscape = self.video_title_in_list_id
            VideoPage.video_start_time_portrait = self.get_video_start_time(browser)
            check = VideoPage.video_start_time_portrait >= VideoPage.video_start_time_landscape
            self.verify_true_or_false(browser, check, 'video_play_without_any_interruption_in_landscape', 'Potrait time')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_in_potrait')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_in_potrait') 
            
    def open_subtopic_video_slider(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 3):
                CommonMethods.elementClick(browser, self.video_auto_cancelBtn_id)   
            CommonMethods.run('adb shell input touchscreen swipe 1272 400 600 400')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'open_subtopic_video_slider')
        except :
            CommonMethods.exception(browser,featureFileName,'open_subtopic_video_slider')  
        
    def get_video_start_time(self, browser):
        check = True
        time = None
        wait_count = 0
        try:
            while check and wait_count < 20:
                    wait_count += 1 
                    CommonMethods.elementClick(browser, self.video_tab_videoframe)
                    time = CommonMethods.getTextOfElement(browser, self.progressTime_id)
                    if time is not None:
                        after_split = time.split(':')
                        minutes = int(after_split[0])
                        sec = int(after_split[1])
                        Total_sec = minutes*60 + sec
                        check = False
                        return Total_sec       
        except:
            logging.info('Problem in fetching start progression time')
            
    def get_video_title_on_player(self, browser):
        check = True
        title = None
        wait_count = 0
        try:
            while check and wait_count < 20:
                    wait_count += 1 
                    CommonMethods.elementClick(browser, self.video_tab_videoframe) 
#                     time = self.get_element_text(browser, self.progressTime_id)
                    title = CommonMethods.getTextOfElement(browser, self.video_title_on_player)
                    if title is not None:
                        check = False
                        return title       
        except:
            logging.info('Problem in fetching start progression time')
     
    def get_video_end_time(self, browser):
        check = True
        time = None
        wait_count = 0
        try:
            while check and wait_count < 20:
                    wait_count += 1 
                    CommonMethods.elementClick(browser, self.video_tab_videoframe) 
#                     time = self.get_element_text(browser, self.progressTime_id)
                    time = CommonMethods.getTextOfElement(browser, self.remaingTime_id)
                    if time is not None:
                        after_split = time.split(':')
                        minutes = int(after_split[0])
                        sec = int(after_split[1])
                        Total_sec = minutes*60 + sec
                        check = False
                        return Total_sec       
        except:
            logging.info('Problem in fetching start progression time')
            
    def is_video_icon_present(self, browser, locator):
        check = True
        time = None
        wait_count = 0
        try:
            while check and wait_count < 10:
                wait_count += 1 
                CommonMethods.elementClick(browser, self.video_tab_videoframe) 
                icon = CommonMethods.wait_for_element_visible(browser, locator, 2)
                if icon == True :
                    check = False  
                    return True   
        except:
            return False
            logging.info('Error in searching for video icon')
    
    def click_on_video_icon(self, browser, locator):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 10:
                wait_count += 1 
                CommonMethods.elementClick(browser, self.video_tab_videoframe) 
                flag = CommonMethods.elementClick(browser, locator)
                if flag is True:
                    check = False  
                    return True   
        except:
            return False
            logging.info('Error in searching for video icon')
     
            
    def verify_autoloded_and_played(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
# #                 self.wait_till_element_visible(browser, self.video_auto_play_btn)
#                 sleep(7) # wait till the video is auto loaded
                expected_video = None
                if CommonMethods.wait_for_element_visible(browser, self.video_auto_play_btn, 5):
                    expected_video = CommonMethods.getTextOfElement(browser, self.video_next_video_chapter_name)
                sleep(5) # wait till the Autoplay is loaded
                self.wait_till_video_load(browser)
                Current_playing_actual = CommonMethods.getTextOfElement(browser, self.video_title_in_list_id)
                expected_video = self.get_text_of_video_in_list(browser, 2)
                check = Current_playing_actual == expected_video
                self.verify_true_or_false(browser, check, 'verify_autoloded_and_played','video played')
            elif device == 'tab':
                VideoPage.title_of_next_video = CommonMethods.getTextOfElement(browser, self.tab_video_next_video_title)
                sleep(7)
                self.wait_till_video_load(browser)
                expected_video = self.get_video_title_on_player(browser)
                check = VideoPage.title_of_next_video == expected_video
                self.verify_true_or_false(browser, check, 'verify_autoloded_and_played', 'next video verification')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_autoloded_and_played')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_autoloded_and_played')
            
            
#             
        
        
            
#     def get_video_end_time(self, browser):
#         check = True
#         time = None
#         wait_count = 0
#         try:
#             while check and wait_count < 10:
#                 wait_count += 1 
#                 CommonMethods.elementClick(browser, self.video_tab_videoframe) 
#                 time = CommonMethods.getTextOfElement(browser, self.remaingTime_id)
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
    def click_on_video_player_list_btn(self, browser):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 10:
                wait_count += 1 
                CommonMethods.elementClick(browser, self.video_tab_videoframe)
                CommonMethods.elementClick(browser, self.video_list_btn_tab)
                if CommonMethods.wait_for_element_visible(browser, self.video_list_close_btn_tab, 2):
                    check = False
                    
        except:
            logging.info('Problem in Showing the Video List screen in tab')
                    
    def verify_playingTxt_tag(self,browser,text):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                self.click_on_video_player_list_btn(browser)
                if CommonMethods.wait_for_element_visible(browser, self.video_list_close_btn_tab, 3):
#                     Playing text verification is not possible
                    pass
                    
                
            elif device == 'mobile':    
                check = CommonMethods.isElementPresent(browser, self.videoPlayingNow_xpath)
                if check == True:
                    pass
                else:
                    logging.info("Failed due to Element not visible in Method verify_playingTxt_tag")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_playingTxt_tag')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_playingTxt_tag')
            
    def video_should_highlighted(self, browser):
        try:
            check = False
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                title = self.get_video_title_on_player(browser)
                sleep(3)
                self.get_video_slider_window()
                elements_list = CommonMethods.getElements(browser, self.video_name_list)
                for i in range(len(elements_list)):
                    logging.info(elements_list[i].text)
                    if title == elements_list[i].text:
                        selected = elements_list[i].get_attribute("selected")
                        if selected == 'true':
                            check = True
                            logging.info(title +" is highlighted ")
                            break
            elif device == 'mobile':
                self.wait_till_autoload_completes(browser)
                CommonMethods.wait_for_element_visible(browser, self.video_title_in_list_id, 10)
                title = CommonMethods.getAttributeOfElement(browser,'text', self.video_title_in_list_id)
                elements_list = CommonMethods.getElements(browser, self.video_name_list)
                for i in range(len(elements_list)):
                    logging.info(elements_list[i].text)
                    if title == elements_list[i].text:
                        selected = elements_list[i].get_attribute("selected")
                        if selected == 'true':
                            check = True
                            logging.info(title +" is highlighted ")
                            break
            self.verify_true_or_false(browser, check, "video_should_highlighted", "Highlight on Video List screen")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'video_should_highlighted')
        except :
            CommonMethods.exception(browser,featureFileName,'video_should_highlighted')
    
    def verify_subtopic_videos(self, browser):
        try:
            check = False
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                elements_list = CommonMethods.getElements(browser, self.video_name_list)
                check = len(elements_list) >= 1
                self.verify_true_or_false(browser, check, 'verify_subtopic_videos', 'video lists')
                    
            elif device == 'mobile':
                elements_list = CommonMethods.getElements(browser, self.video_name_list)
                check = len(elements_list) >= 1
                self.verify_true_or_false(browser, check, 'verify_subtopic_videos', 'video lists')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_subtopic_videos')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_subtopic_videos')
           
    def video_should_complete(self,browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
#                 self.video_should_played(browser)
#                 video_length = self.get_video_end_time(browser)
                self.select_short_video(browser)
#                 self.wait_video_to_complete(browser, video_length)
                if CommonMethods.wait_for_element_visible(self, browser, self.video_play_btn, 3):
                    logging.info('Completed the Video Without any interaction')
                    return True
                else:
                    logging.info("Failed due to Element not visible in Method video_should_complete")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    return False
                    pytest.fail("Failed due to Element not visible in Video Page")  
            elif device == 'mobile':    
#                 sleep(20)
#                 CommonMethods.elementClick(browser, self.video1stLink_xpath)
#                 videoLength = CommonMethods.getTextOfElement(browser, self.remaingTime_id)
#                 videoLength = videoLength.split(':')
#                 l1 = int(videoLength[0])*60
#                 l2 = int(videoLength[1])+120
#                 length = l1+l2
#                 CommonMethods.elementClick(browser, self.video1stLink_xpath)
#                 CommonMethods.wait_for_locator(browser, self.video_auto_cancelBtn_id,length)
#                 check = CommonMethods.isElementPresent(browser, self.video_auto_cancelBtn_id)
#                 if check == True:
#                     CommonMethods.elementClick(browser,self.video_auto_cancelBtn_id)
#                     pass
#                 else:
#                     logging.info("Failed due to Element not visible in Method video_should_complete")
#                     CommonMethods.takeScreenShot(browser,featureFileName)
#                     pytest.fail("Failed due to Element not visible in Video Page")
                self.wait_till_video_load(browser)
                end_time = self.get_video_end_time(browser)
                check = self.wait_till_video_complete(browser, end_time)
                self.verify_true_or_false(browser, check, 'video_should_complete', 'Auto cancel Button')
                return True
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'video_should_complete')
        
        except :
            CommonMethods.exception(browser,featureFileName,'video_should_complete')
    
    def wait_video_to_complete(self, browser, wait_time):
        browser.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 1) and loading_count < wait_time+100:
                loading_count += 1
                sleep(0.2)
        except:
            logging.info('Exception in Completing Videos')
        
    def select_short_video(self, browser):
        browser.implicitly_wait(0.1)
        list = []
        loading_count = 10
        try:
            while loading_count < 10:
                loading_count += 1
                ele = CommonMethods.getElements(self, browser, self.video_time_remaining)
                for i in len(ele):
                    ele_str = ele.text
                    res = (int(i) for i in ele_str.split() if i.isdigit())
                    list.append(res)
                    
        except:
            logging.info('Exception in selecting the shortest video')
        
        
            
    def verify_start_time(self,browser):
        try:
            self.pause_video(browser)
            x,y = self.get_x_y_coordinate(browser, self.video_progressBar_id)
            CommonMethods.run('adb shell input tap {} {}'.format(x,y))
            start_time = self.get_video_start_time(browser)
            check = start_time == 0
            self.verify_true_or_false(browser, check, 'verify_start_time', 'video starting video')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_start_time')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_start_time')
            
            
    def verify_back_btn_in_subtopic_video_lst(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.video_tab_video_player_close_btn)
            self.verify_true_or_false(browser, check, 'verify_back_btn_in_subtopic_video_lst', 'video back btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_back_btn_in_subtopic_video_lst')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_back_btn_in_subtopic_video_lst')
            
    def verify_end_time(self,browser):
        try:
            end_time = self.get_video_end_time(browser)
            check = end_time > 0 
            self.verify_true_or_false(browser, check, 'verify_start_time', 'video starting video')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_end_time')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_end_time')
            
    def tap_forward(self,browser):
        try:
            VideoPage.videoProgressTimeBfr = self.get_video_start_time(browser)
            self.click_on_video_icon(browser, self.ten_sec_fwd_btn_id)
            VideoPage.videoProgressTimeAfter = self.get_video_start_time(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_forward')
        except :
            CommonMethods.exception(browser,featureFileName,'tap_forward')
            
            
    def tap_backward_10sec(self,browser):
        try:
            VideoPage.videoProgressTimeBfr = self.get_video_start_time(browser)
            self.click_on_video_icon(browser, self.ten_sec_bkwd_btn_id)
            VideoPage.videoProgressTimeAfter = self.get_video_start_time(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_backward_10sec')
        except :
            CommonMethods.exception(browser,featureFileName,'tap_backward_10sec')
            
    def verify_fwrd_time(self, browser):
        try:
            startTime = self.videoProgressTimeBfr
            stopTime = self.videoProgressTimeAfter
            if stopTime >= startTime:
                logging.info("Verified video 10 sec forward")
            else:
                logging.info("Failed Locator in Method verify_fwrd_time")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_fwrd_time')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_fwrd_time')
            
            
    def verify_video_continue_after_pause(self, browser):
        try:
            startTime = self.videoProgressTimeBfr
            stopTime = self.videoProgressTimeAfter
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_continue_after_pause')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_continue_after_pause')
            
    def verify_backward_10sec(self, browser):
        try:
            startTime = self.videoProgressTimeBfr
            stopTime = self.videoProgressTimeAfter
            if stopTime < startTime:
                logging.info("Verified video 10 sec backward")
            else:
                logging.info("Failed Locator in Method verify_backward_10sec")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_backward_10sec')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_backward_10sec')       
    
    
    def tap_on_practice_card(self, browser):
        try:
            CommonMethods.scrollToElement(browser, 'Practice')    
            VideoPage.practice_stage_name = CommonMethods.getTextOfElement(browser, self.video_practice_stage_name_test)
            CommonMethods.scrollToElementAndClick(browser, 'Practice')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_practice_card')
        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_practice_card') 
            
            
    def progress_till_video_play(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.practice_start_practice_btn, 3):
                CommonMethods.elementClick(browser, self.practice_start_practice_btn) 
                sleep(7)
                CommonMethods.elementClick(browser, self.practice_continue_btn)
                sleep(3)
                self.wait_for_video_in_practice(browser)
                CommonMethods.elementClick(browser, self.practice_continue_btn)
                self.pause_video(browser)
                check = CommonMethods.wait_for_element_visible(browser, self.video_settingIcon_id, 3)
                self.verify_false(browser, check, 'progress_till_video_play', 'setting icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'progress_till_video_play')
        except :
            CommonMethods.exception(browser,featureFileName,'progress_till_video_play')   
            
            
    def progress_till_practice_stage_complete(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.practice_start_practice_btn, 3):
                CommonMethods.elementClick(browser, self.practice_start_practice_btn) 
                sleep(7)
                CommonMethods.elementClick(browser, self.practice_continue_btn)
                sleep(3)
                self.complete_practice_stage(browser)
                CommonMethods.elementClick(browser, self.practice_continue_btn)
                self.pause_video(browser)
                check = CommonMethods.wait_for_element_visible(browser, self.video_settingIcon_id, 3)
                self.verify_false(browser, check, 'progress_till_video_play', 'setting icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'progress_till_practice_stage_complete')
        except :
            CommonMethods.exception(browser,featureFileName,'progress_till_practice_stage_complete')
            
            
    def verify_setting_icon_not_seen(self, browser):
        try:
            self.pause_video(browser)
            check = CommonMethods.wait_for_element_visible(browser, self.video_settingIcon_id, 3)
            self.verify_false(browser, check, 'progress_till_video_play', 'setting icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_setting_icon_not_seen')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_setting_icon_not_seen') 
            
    def verify_video_screen(self, browser):
        try:
            self.pause_video(browser)
            check = CommonMethods.wait_for_element_visible(browser, self.video_title_on_player, 3)
            self.verify_true_or_false(browser, check, 'verify_video_screen', 'video frame')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_screen')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_screen') 
            
            
    def verify_video_title(self, browser):
        try:
            self.pause_video(browser)
            check = CommonMethods.wait_for_element_visible(browser, self.video_title_on_player, 5)
            self.verify_true_or_false(browser, check, 'verify_video_title', 'video Title')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_title')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_title')
            
            
    def wait_for_video_in_practice(self, browser):
        browser.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.wait_for_element_visible(browser, self.practice_continue_btn, 2) and loading_count < 75:
                loading_count += 1
                CommonMethods.elementClick(browser, self.practice_2nd_answer)
                if CommonMethods.wait_for_element_visible(browser, self.practice_submit_btn, 5):
                    CommonMethods.elementClick(browser, self.practice_submit_btn)
                    if CommonMethods.wait_for_element_visible(browser, self.practice_submit_btn, 5):
                        CommonMethods.elementClick(browser, self.practice_submit_btn)
                    elif CommonMethods.wait_for_element_visible(browser, self.practice_continue_btn, 5):
                        logging.info("found video in practice")
                elif CommonMethods.wait_for_element_visible(browser, self.practice_start_practice_btn, 5) or CommonMethods.wait_for_element_visible(browser, self.video_badge_close_btn, 5) :
                    CommonMethods.elementClick(browser, self.video_badge_close_btn)
                    CommonMethods.elementClick(browser, self.practice_start_practice_btn)
        except:
            logging.info('Error in finding the video')
            
            
    def complete_practice_stage(self, browser):
        """
        this method completes the entire practice stage 
        """
        browser.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.wait_for_element_visible(browser, self.practice_continue_btn, 2) and loading_count < 75:
                loading_count += 1
                CommonMethods.elementClick(browser, self.practice_2nd_answer)
                if CommonMethods.wait_for_element_visible(browser, self.practice_submit_btn, 5):
                    CommonMethods.elementClick(browser, self.practice_submit_btn)
                    if CommonMethods.wait_for_element_visible(browser, self.practice_submit_btn, 5):
                        CommonMethods.elementClick(browser, self.practice_submit_btn)
                    elif CommonMethods.wait_for_element_visible(browser, self.practice_continue_btn, 5):
                        x1,y1,x2,y2 = self.get_element_coordinates(browser, self.video_progressBar_id)
                        CommonMethods.run('adb shell input touchscreen swipe {} {} {} {}'.format(x1, y1, x2, 1000))
                elif CommonMethods.wait_for_element_visible(browser, self.practice_start_practice_btn, 5) or CommonMethods.wait_for_element_visible(browser, self.video_badge_close_btn, 5) :
                    CommonMethods.elementClick(browser, self.video_badge_close_btn)
                    logging.info('Stage Completed Successfully')
        except:
            logging.error('Error in Completing Practice Stage')
               
#     def verify_video_in_potrait(self,browser):
#         try:
#             sleep(20)
#             orientation = CommonMethods.get_screen_orientation(browser)
#             CommonMethods.elementClick(browser, self.videoPlayingNow_xpath)
#             sleep(5)
#             startProgress_time = CommonMethods.getTextOfElement(browser, self.progressTime_id)
#             CommonMethods.elementClick(browser, self.videoPlayingNow_xpath)
#             sleep(10)
#             CommonMethods.elementClick(browser, self.videoPlayingNow_xpath)
#             sleep(5)
#             endProgress_time = CommonMethods.getTextOfElement(browser, self.progressTime_id)
#             start_time = startProgress_time.split(':')
#             end_time = endProgress_time.split(':')
#             start =int(start_time[1])
#             stop = int(end_time[1])
#             if orientation == 'PORTRAIT' and start < stop:
#                 pass
#             else:
#                 logging.info("Failed Locator in Method verify_video_in_potrait")
#                 CommonMethods.takeScreenShot(browser,featureFileName)
#                 pytest.fail("Failed Due to Locator in Video Page")
#         except NoSuchElementException:
#             CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_in_potrait')
#         
#         except :
#             CommonMethods.exception(browser,featureFileName,'verify_video_in_potrait')
    def verify_video_in_landscape(self,browser):
        try:
            sleep(3)
            orientation = CommonMethods.get_screen_orientation(browser)
            loc = CommonMethods.get_element_location(browser,self.video_play_btn)
            x = loc["x"]
            y = loc["y"]
            startProgress_time = CommonMethods.getTextOfElement(browser, self.progressTime_id)
            CommonMethods.elementClick(browser, self.video_play_btn)
            sleep(10)
            # for i in range(1,6):
            CommonMethods.run('adb shell input tap {} {}'.format(x,y))
            CommonMethods.run('adb shell input tap {} {}'.format(x,y))
                # if CommonMethods.isElementPresent(browser, self.video_pause_btn_id):
                #     break
            endProgress_time = CommonMethods.getTextOfElement(browser, self.progressTime_id)
            start_time = startProgress_time.split(':')
            end_time = endProgress_time.split(':')
            start = int(start_time[1])
            stop = int(end_time[1])
            if orientation == 'LANDSCAPE' and start < stop :
                pass
            else:
                logging.info("Failed Locator in Method verify_video_in_landscape")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_in_landscape')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_in_landscape')
            
    def select_topic(self,browser, topic, chapter):
        try:
            CommonMethods.scrollToElement(browser, chapter)
            sleep(2)
            topic_xpath = (By.XPATH,"//android.widget.TextView[@text=\'"+topic+"\']")
            sub_chapter_xpath = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.RelativeLayout//android.widget.TextView[@text=\'"+chapter+"\']//parent::android.widget.RelativeLayout//following::androidx.recyclerview.widget.RecyclerView")
            video_count = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.RelativeLayout//android.widget.TextView[@text=\'"+chapter+"\']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/video_count']") 
            swipe_count = CommonMethods.get_swipe_count(browser,video_count)
            swipe_count =int(swipe_count[0])
            logging.info(swipe_count)
            CommonMethods.select_topic(browser,sub_chapter_xpath,topic_xpath,swipe_count)
            sleep(3)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'select_topic')
        except :
            CommonMethods.exception(browser,featureFileName,'select_topic')
            
            
    def select_video_card_from_journey(self,browser, topic, chapter):
        try:
            library_txt = (By.XPATH,"//android.widget.Button[@text ='Library']")
            for i in range(10):
                CommonMethods.run("adb shell input swipe 400 400 400 1000")
                if CommonMethods.isElementPresent(browser, library_txt):
                    break
            CommonMethods.scrollToElement(browser, chapter)
            sleep(2)
            topic_xpath = (By.XPATH,"//android.widget.TextView[@text=\'"+topic+"\']")
            sub_chapter_xpath = (By.XPATH,"//android.widget.TextView[@text =\'"+chapter+"\']/parent::android.widget.RelativeLayout[@resource-id='com.byjus.thelearningapp.premium:id/parent_layout']//androidx.recyclerview.widget.RecyclerView")
            swipe_count = 10
            CommonMethods.select_topic(browser,sub_chapter_xpath,topic_xpath,swipe_count)
            sleep(3)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'select_video_card_from_journey')
        except :
            CommonMethods.exception(browser,featureFileName,'select_video_card_from_journey')
            
    def verify_video_chapter_name(self,browser,chapter):
        try:
            actual_text = CommonMethods.getTextOfElement(browser, self.video_chapter_name_id)
            expected_text = chapter
            check = CommonMethods.verifyTwoText(actual_text, expected_text)
            if check == True :
                pass
            else:
                logging.info("Failed Locator in Method verify_video_chapter_name")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_chapter_name')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_chapter_name')
            
    def verify_video_subtitle_name(self,browser,title):
        try: 
            actual_text = CommonMethods.getTextOfElement(browser, self.video_title_in_list_id)
            expected_text = title
            check = CommonMethods.verifyTwoText(actual_text, expected_text)
            if check == True :
                logging.info('verified the video playing')
            else:
                logging.info("Failed Locator in Method verify_video_subtitle_name")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_subtitle_name')
        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_subtitle_name')  
            
    def verify_list_view(self,browser):
        try:
            ele_list = CommonMethods.getElements(browser, self.video_list_view_id)
            for i in range(len(ele_list)):
                check = ele_list[i].is_displayed()
                if check == True:
                    logging.info('all the videos are in list')
                else:
                    logging.info("Failed Locator in Method verify_list_view")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page") 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_list_view')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_list_view')    
            
    def verify_video_name(self,browser):
        try:
            sleep(15)
            video_title_name = CommonMethods.getAttributeOfElement(browser,'text', self.video_title_in_list_id)
            video_title = "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName' and @text = \'"+video_title_name+"\']"
            video_title_xapth = (By.XPATH,video_title)
            check = CommonMethods.isElementPresent(browser, video_title_xapth)
            self.verify_true_or_false(browser, check, 'verify_video_name', 'video name')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_name')

        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_name') 
        
    def verify_video_thumbnail(self,browser):
        try:
            video_title_name = CommonMethods.getAttributeOfElement(browser,'text', self.video_title_in_list_id) 
            video_thumbnail = (By.XPATH,"//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName' and @text =\'"+video_title_name+"\']//parent::android.widget.RelativeLayout//android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/thumbnail']")
            check = CommonMethods.isElementPresent(browser, video_thumbnail)
            self.verify_true_or_false(browser, check, 'verify_video_thumbnail', 'video thumbnail') 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_thumbnail')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_thumbnail')   
            
    def verify_video_duration(self,browser):
        try:
            video_title_name = CommonMethods.getAttributeOfElement(browser,'text', self.video_title_in_list_id)
            sleep(2)
            video_title =(By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'"+video_title_name+"\']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
            if CommonMethods.isElementPresent(browser, video_title):
                CommonMethods.elementClick(browser, self.video1stLink_xpath)
            sleep(3)   
            duration = CommonMethods.getAttributeOfElement(browser,'text', video_title)
            check = duration.__contains__('min')
            self.verify_true_or_false(browser, check, 'verify_video_duration', 'video duration') 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_duration')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_duration')
            
    def verify_video_progress(self,browser):
        try:
            video_title_name = CommonMethods.getAttributeOfElement(browser,'text', self.video_title_in_list_id)
            video_progress =(By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'"+video_title_name+"\']//parent::android.widget.RelativeLayout//android.widget.ProgressBar")
            if CommonMethods.isElementPresent(browser, video_progress):
                pass
            else:
                logging.info("Failed Locator in Method verify_video_progress")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed Due to Locator in Video Page") 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_progress')

        except :
            CommonMethods.exception(browser,featureFileName,'verify_video_progress')

    def verify_min_completed(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                video_title_name = CommonMethods.getAttributeOfElement(browser, 'text', self.video_title_on_player)
                sleep(2)
                video_title = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
                duration = CommonMethods.getAttributeOfElement(browser, 'text', video_title)
                check = duration.__contains__('min | Completed')
                if check == True:
                    logging.info('xx and completed in video is verified')
                else:
                    logging.info("Failed Locator in Method verify_min_completed")
                    CommonMethods.takeScreenShot(browser, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")    
            elif device == 'mobile':
                video_title_name = CommonMethods.getAttributeOfElement(browser, 'text', self.video_title_in_list_id)
                sleep(2)
                video_title = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
                duration = CommonMethods.getAttributeOfElement(browser, 'text', video_title)
                check = duration.__contains__('min | Completed')
                if check == True:
                    logging.info('xx and completed in video is verified')
                else:
                    logging.info("Failed Locator in Method verify_min_completed")
                    CommonMethods.takeScreenShot(browser, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_min_completed')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_min_completed')
            
            
    def verify_min_remaining_paused(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                video_title_name = CommonMethods.getAttributeOfElement(browser, 'text', self.video_title_on_player)
                sleep(2)
                video_title = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
                duration = CommonMethods.getAttributeOfElement(browser, 'text', video_title)
                check = duration.__contains__('min remaining | Paused') or duration.__contains__('min | Completed')
                if check == True:
                    logging.info('xx and remaining | Paused in video is verified')
                else:
                    logging.info("Failed Locator in Method verify_min_remaining_paused")
                    CommonMethods.takeScreenShot(browser, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")    
            elif device == 'mobile':
                video_title_name = CommonMethods.getAttributeOfElement(browser, 'text', self.video_title_in_list_id)
                sleep(2)
                video_title = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv']")
                duration = CommonMethods.getAttributeOfElement(browser, 'text', video_title)
                check = duration.__contains__('min remaining | Paused') or duration.__contains__('min | Completed')
                if check == True:
                    logging.info('xx and remaining | Paused in video is verified')
                else:
                    logging.info("Failed Locator in Method verify_min_remaining_paused")
                    CommonMethods.takeScreenShot(browser, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_min_remaining_paused')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_min_remaining_paused')
            
            
    def verify_progression_100_percent(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'tab':
                video_title_name = CommonMethods.getAttributeOfElement(browser, 'text', self.video_title_on_player)
                sleep(2)
                progression_percent = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.ProgressBar[@resource-id='com.byjus.thelearningapp.premium:id/video_progress_view']")
                percent = CommonMethods.getAttributeOfElement(browser, 'text', progression_percent)
                check = percent.__contains__('100')
                if check == True:
                    logging.info('Progress is 100% percent')
                else:
                    logging.info("Failed Locator in Method verify_progression_100_percent")
                    CommonMethods.takeScreenShot(browser, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")    
            elif device == 'mobile':
                video_title_name = CommonMethods.getAttributeOfElement(browser, 'text', self.video_title_in_list_id)
                sleep(2)
                progression_percent = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout//android.widget.TextView[@text=\'" + video_title_name + "\']//parent::android.widget.RelativeLayout//android.widget.ProgressBar[@resource-id='com.byjus.thelearningapp.premium:id/video_progress_view']")
                percent = CommonMethods.getAttributeOfElement(browser, 'text', progression_percent)
                check = percent.__contains__('100')
                if check == True:
                    logging.info('Progress is 100% percent')
                else:
                    logging.info("Failed Locator in Method verify_progression_100_percent")
                    CommonMethods.takeScreenShot(browser, featureFileName)
                    pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_progression_100_percent')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_progression_100_percent')

    def tap_on_same_video(self,browser):
        try:
            sleep(2)
            video_title_name = CommonMethods.getAttributeOfElement(browser,'text', self.video_title_in_list_id)
            video_title = "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName' and @text = \'"+video_title_name+"\']"
            video_title_xapth = (By.XPATH,video_title)
            check = CommonMethods.wait_for_element_visible(browser, video_title_xapth, 3)
            if check == True:
                CommonMethods.elementClick(browser, video_title_xapth)
                logging.info('Clicked on same video')
            else:
                logging.info("Failed Locator in Method tap_on_same_video")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_same_video')

        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_same_video')
            
            
    def verify_video_where_it_stopped(self, browser):
        try:
            video_time_before = self.videoProgressTimeBfr
            video_time_after =  self.get_element_text(browser, self.videoProgressTimeBfr)
            check1 =  self.is_video_icon_present(browser, self.video_pause_btn_id)
            check2 = video_time_after == video_time_before or video_time_after 
            
#             else:
#                 logging.info("Failed Locator in Method tap_on_same_video")
#                 CommonMethods.takeScreenShot(browser,featureFileName)
#                 pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_same_video')

        except :
            CommonMethods.exception(browser,featureFileName,'tap_on_same_video')

    def verify_pause_btn(self,browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser,self.video_play_btn, 5)
            self.verify_true_or_false(browser, check, 'verify_pause_btn', 'Pause Button')
            VideoPage.videoProgressTimeBfr = CommonMethods.getTextOfElement(browser, self.progressTime_id)
#             if check is True:
#                 time = CommonMethods.getTextOfElement(browser, self.progressTime_id)
#                 after_split = time.split(':')
#                 minutes = int(after_split[0])
#                 sec = int(after_split[1])
#                 Total_sec = minutes*60 + sec
#                 VideoPage.videoProgressTimeBfr = Total_sec
#                 logging.info('Pause btn is verified')
#             else:
#                 logging.info("Failed Locator in Method verify_pause_btn")
#                 CommonMethods.takeScreenShot(browser,featureFileName)
#                 pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_pause_btn')
        except :
            CommonMethods.exception(browser,featureFileName,'verify_pause_btn')
            
    """This method will tap on pause btn in video player when video is playing"""
    def tap_pause_btn(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 3):
                logging.info('video is paused in video Player')
            else:
                sleep(2)
                self.pause_video(browser)
                logging.info('video is paused in video Player')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_pause_btn')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_pause_btn')

#     def tap_pause_btn(self, browser):
#         try:
#             if CommonMethods.isElementPresent(browser,self.videoPlayBtn_id):
#                 pass
#             else:
#                 sleep(3)
#                 video_title_name = CommonMethods.getAttributeOfElement(browser, 'text', self.video_title_id)
#                 video_title = "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName' and @text = \'" + video_title_name + "\']"
#                 video_title_xapth = (By.XPATH, video_title)
#                 CommonMethods.elementClick(browser,video_title_xapth)
#         except NoSuchElementException:
#             CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_pause_btn')
# 
#         except:
#             CommonMethods.exception(browser, featureFileName, 'tap_pause_btn')

    def verify_video_resumed_from_same_point(self, browser):
        try:
            self.wait_till_video_load(browser)
            videoProgressTimeAfter = self.get_video_start_time(browser)
            check = self.is_video_icon_present(browser, self.video_pause_btn_id)
            self.verify_true_or_false(browser, check, 'verify_video_resumed_from_same_point', 'Pause Btn')
            if videoProgressTimeAfter >= VideoPage.videoProgressTimeBfr:
                logging.info('Video is played and resumed from where it is stopped')
            else:
                sleep(3)
                video_title_name = CommonMethods.getAttributeOfElement(browser, 'text', self.video_title_in_list_id)
                video_title = "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/videoName' and @text = \'" + video_title_name + "\']"
                video_title_xapth = (By.XPATH, video_title)
                CommonMethods.elementClick(browser,video_title_xapth)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_video_resumed_from_same_point')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_resumed_from_same_point')

    def verify_video_size_40_percent(self, browser):
        try:
#             window_height = CommonMethods.get_window_height(browser)
            window_height = browser.get_window_size()
            video_frame_height = CommonMethods.getElement(browser,self.video_video_frame_id).size
            percent = (video_frame_height["height"]/window_height["height"])*100
            if percent > 30 and percent < 50:
                logging.info('Video is playing in 40% screen')
            else:
                logging.info("Failed Locator in Method verify_video_size_40_percent")
                CommonMethods.takeScreenShot(browser, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_video_size_40_percent')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_size_40_percent')
            
            
    def seek_video_player_50_percent(self, browser):
        try:
            VideoPage.video_start_time = self.get_video_start_time(browser)
            self.drag_video_progress_to_half(browser)
            VideoPage.video_end_time = self.get_video_start_time(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'seek_video_player_50_percent')
        except:
            CommonMethods.exception(browser, featureFileName, 'seek_video_player_50_percent')
            
            
    def switch_to_grade(self, browser, grade):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.back_button_id, 3):
                CommonMethods.elementClick(browser, self.back_button_id)
                CommonMethods.wait_for_locator(browser, self.profile_name_hamburger, 5)
                CommonMethods.elementClick(browser, self.profile_name_hamburger)
                selected_grade = CommonMethods.getTextOfElement(browser, self.video_grade_selection_btn)
                if selected_grade == grade:
                    CommonMethods.click_on_device_back_btn(browser)
                else:
                    CommonMethods.wait_for_element_visible(browser, self.video_grade_selection_btn, 5)
                    CommonMethods.elementClick(browser, self.video_grade_selection_btn)
                    self.select_grade(browser, grade)
                    sleep(5)
                    CommonMethods.click_on_device_back_btn(browser)   
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'switch_to_grade')
        except:
            CommonMethods.exception(browser, featureFileName, 'switch_to_grade')
            
            
    def select_grade(self, browser, grade):
        browser.implicitly_wait(0.1)
        loading_count = 0
        try:
            while not CommonMethods.findText(browser, grade) and loading_count < 15:
                loading_count += 1
                length = len(CommonMethods.getElements(browser, self.video_grades_elements))
                x1,y1 = self.get_elements_coordinates(browser, self.video_grades_elements, length)
                x2,y2 = self.get_elements_coordinates(browser, self.video_grades_elements, 1)
                CommonMethods.run('adb shell input swipe {} {} {} {}'.format(x1,y1,x2, y2))
            if CommonMethods.findText(browser, grade):
                grade_txt = "//android.widget.TextView[@text = \'"+grade+"\']"
                sel_grade = (By.XPATH,grade_txt)
                CommonMethods.elementClick(browser, sel_grade)
                logging.info('selected grade '+grade)
            else:
                logging.info('error in selecting the grade')   
        except:
            logging.error('Error in playing the video completely')

    def verify_subtopic_name(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.video_title_in_list_id)
            if check == True:
                logging.info('Sub title name is present')
            else:
                logging.info("Failed Locator in Method verify_subtopic_name")
                CommonMethods.takeScreenShot(browser, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_subtopic_name')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_subtopic_name')

    def verify_share_bookmerks_icon(self, browser):
        try:
            #check1 = CommonMethods.isElementPresent(browser, self.video_share_icon_id)
            check2 = CommonMethods.isElementPresent(browser, self.video_bookmark_icon_id)
            if check2:
                logging.info('share bookmark is present')
            else:
                logging.info("Failed Locator in Method verify_share_bookmerks_icon")
                CommonMethods.takeScreenShot(browser, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_share_bookmerks_icon')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_share_bookmerks_icon')

    def verify_topic_videos(self, browser):
        try:
            ele = CommonMethods.getElements(browser, self.video_topic_videos_id)
            if len(ele) > 2 :
                pass
            else:
                logging.info("Failed Locator in Method verify_topic_videos")
                CommonMethods.takeScreenShot(browser, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_topic_videos')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_topic_videos')

    def verify_card_lnk(self, browser, card):
        try:
            lnk_name = (By.XPATH, "//android.widget.TextView[@text=\'"+card+"\']")
            CommonMethods.scrollToElement(browser, card)
            check = CommonMethods.isElementPresent(browser, lnk_name)
            if check == True :
                pass
            else:
                logging.info("Failed Locator in Method verify_card_lnk")
                CommonMethods.takeScreenShot(browser, featureFileName)
                pytest.fail("Failed Due to Locator in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_card_lnk')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_card_lnk')

    def video_progression(self, browser):
        try:
            check = self.is_video_icon_present(browser, self.video_progress_tab_id)
            self.verify_true_or_false(browser, check, 'video_progression', 'video progression')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'video_progression')
        except:
            CommonMethods.exception(browser, featureFileName, 'video_progression')
            
            
    def verify_video_stopped_loading_next_video(self, browser):
        try:
            check1 = CommonMethods.wait_for_element_visible(browser, self.video_play_next_btn, 3)
            check2 = CommonMethods.wait_for_element_visible(browser, self.video_play_previous_btn, 3)
            check = check1 or check2
            self.verify_true_or_false(browser, check, 'video_progression', 'video progression')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_video_stopped_loading_next_video')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_stopped_loading_next_video')

    def verify_chapter_name_color_with_subject_theme(self, browser):
        try:
            subject_rgb = VideoPage.subject_rgb_lst
            chapter_name_title = self.get_the_rgb_lst(browser, self.video_chapter_name_id)
            self.verify_subject_chapter_color(subject_rgb, chapter_name_title, 10)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_chapter_name_color_with_subject_theme')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_chapter_name_color_with_subject_theme')
            
            
# Video Utility methods 
    def verify_true_or_false(self, browser, check, method_name, ele_name):
        if check == True:
            logging.info('The '+ele_name+' is present on screen')
        else:
            logging.info("Failed due to Element not visible in "+method_name)
            CommonMethods.takeScreenShot(browser,featureFileName)
            pytest.fail("Failed due to Element not visible in Video Page")
            
            
    
            
    def verify_false(self, browser, check, method_name, ele_name):
        if check == False:
            logging.info('The '+ele_name+' is not present on screen')
        else:
            logging.info("Failed due to Element not visible in "+method_name)
            CommonMethods.takeScreenShot(browser,featureFileName)
            pytest.fail("Failed due to Element not visible in Video Page")
            
            
    def test_fail(self, browser, method_name):
        logging.info("Failed in "+method_name)
        CommonMethods.takeScreenShot(browser,featureFileName)
        pytest.fail("Failed in Video Page")
        
    def verify_video_is_playing(self, browser, frame):
        check = True
        time = None
        wait_count = 0
        try:
            while check and wait_count < 10:
                wait_count += 1 
                CommonMethods.elementClick(browser, self.video_tab_videoframe) 
                time = CommonMethods.getTextOfElement(browser, self.progressTime_id)
                if time is not None:
                    after_split = time.split(':')
                    minutes = int(after_split[0])
                    sec = int(after_split[1])
                    Total_sec = minutes*60 + sec
                    check = False
                    return Total_sec        
        except:
            logging.info('Problem in fetching start progression time')
    
    
    '''Only for video Scenarios'''        
    def get_element_text(self, browser, locator):
        txt = None
        try:
            ele = browser.find_element(locator)
            txt = ele.text()
            if txt is not None:
                return txt
            else:
                return None
        except:
            return None
            
    def tap_on_first_video_lnk_and_complete(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                sleep(3) # wait till the video start loading
                self.wait_till_video_load(browser)
#                 self.start_the_video(browser)
                self.tap_on_first_video_lnk(browser)
                self.wait_till_video_load(browser)
                self.pause_video(browser)
                self.end_the_video(browser)
                self.wait_till_video_load(browser)
                self.play_video(browser)
                flag = CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 30)
            elif device == 'tab':
                sleep(3) # wait till the video start loading
                self.wait_till_video_load(browser)
                self.start_the_video(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_first_video_lnk_and_complete')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_first_video_lnk_and_complete')
    
    def tap_on_first_video_lnk(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.video1stLink_xpath, 3):
                CommonMethods.elementClick(browser, self.video1stLink_xpath)
            self.wait_till_video_load(browser)
            self.pause_video(browser)
            x,y = self.get_x_y_coordinate(browser, self.video_progressBar_id)
            CommonMethods.run('adb shell input tap {} {}'.format(x,y))
            self.wait_till_video_load(browser)
            self.click_on_video_icon(browser, self.video_play_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_first_video_lnk')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_first_video_lnk')       
            
    def turn_off_auto_play(self, browser):
        try:
            self.wait_till_video_load(browser)
            self.pause_video(browser)
#             self.tap_on_video_player_icon(browser, self.video_settingIcon_id)
            CommonMethods.elementClick(browser, self.video_settingIcon_id)
            CommonMethods.wait_for_element_visible(browser, self.video_auto_enable_switch, 5)
            status = CommonMethods.getAttributeOfElement(browser, 'checked', self.video_auto_enable_switch)
            if CommonMethods.wait_for_element_visible(browser, self.video_auto_enable_switch, 3):
                if status == 'false':
                    VideoPage.auto_play_switch_color = self.get_the_rgb_lst(browser, self.video_auto_enable_switch)
                    logging.info('Autoplay is disable')
                    CommonMethods.click_on_device_back_btn(browser)   
                elif status == 'true':
                    CommonMethods.elementClick(browser, self.video_auto_enable_switch)
                    VideoPage.auto_play_switch_color = self.get_the_rgb_lst(browser, self.video_auto_enable_switch)
                    CommonMethods.click_on_device_back_btn(browser)   
            else:
                logging.info('Error in getting Auto play option screen')
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'turn_off_autoplay')

        except:
            CommonMethods.exception(browser, featureFileName, 'turn_off_autoplay')
            
            
    def turn_on_auto_play(self, browser):
        try:
            self.wait_till_video_load(browser)
#             self.pause_video(browser)
            self.tap_on_video_player_icon(browser, self.video_pause_btn_id)
#             x,y = self.get_x_y_coordinate(browser, self.video_progressBar_id)
#             CommonMethods.run('adb shell input tap {} {}'.format(x,y))
#             self.pause_video(browser)
            self.tap_on_video_player_icon(browser, self.video_pause_btn_id)
            CommonMethods.wait_for_element_visible(browser, self.video_settingIcon_id, 5)
            CommonMethods.elementClick(browser, self.video_settingIcon_id)
            CommonMethods.wait_for_element_visible(browser, self.video_auto_enable_switch, 5)
            status = CommonMethods.getAttributeOfElement(browser, 'checked', self.video_auto_enable_switch)
            if CommonMethods.wait_for_element_visible(browser, self.video_auto_enable_switch, 3):
                if status == 'true':
                    VideoPage.auto_play_switch_color = self.get_the_rgb_lst(browser, self.video_auto_enable_switch)
                    logging.info('Autoplay is enabled')
                    CommonMethods.click_on_device_back_btn(browser)   
                elif status == 'false':
                    CommonMethods.elementClick(browser, self.video_auto_enable_switch)
                    VideoPage.auto_play_switch_color = self.get_the_rgb_lst(browser, self.video_auto_enable_switch)
                    CommonMethods.click_on_device_back_btn(browser)   
            else:
                logging.info('Error in getting Auto play option screen')
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'turn_on_auto_play')

        except:
            CommonMethods.exception(browser, featureFileName, 'turn_on_auto_play')
    
    def verify_purple_color(self, browser):
        try:
#             purple_color = {"#6a4ac7"}
            purple_color = {'#c0b7db', '#d1c7ec', '#beb5d8', '#e0e0e0', '#cdc3e8', '#765bc6', '#eeeeee', '#a18fd7', '#9788c4', '#f8f7fd', '#f9f7fd', '#cbc1e7', '#876ed0', '#f2f2f2', '#8f7bc8', '#f7f7f8', '#6b4cc7', '#ffffff', '#6c4dc7', '#b9b0d2', '#6d4ec7', '#7155c6', '#fefeff', '#f9f9fa', '#d1d1d1', '#866dce', '#f1f1f1', '#795ec8', '#8d7bc3', '#dfdfdf', '#cdc3e9', '#c0b7d9', '#d4caf0', '#c0b5e2', '#e5e1ee', '#e4e0ee', '#785dc9', '#c6bce1', '#c4bbdf', '#a398c2', '#e7e7e8', '#e9e9e9', '#917ad2', '#d4d4d4', '#fdfcfe', '#f8f8f8', '#b4afc1', '#cfc8e6', '#afa0dc', '#ededee', '#7357c5', '#836bcc', '#ccc5e3', '#a196c2', '#eae6f7', '#fafafa', '#d1c7ed', '#cec4e9', '#dbd4f3', '#d2d2d3', '#cfcfd0', '#856fc5', '#c6bde1', '#d8d0f1', '#ccc3e9', '#c9c0e5', '#f1f1f2', '#ece8f8', '#c9c9c9', '#765ac9', '#d2c9ef', '#6d4fc7', '#ddddde', '#c2c2c3', '#785ccb', '#d1d1d2', '#ccc3e8', '#b9aed4', '#f3f3f3', '#cecece', '#6e4fc7', '#cbcacc', '#7357c8', '#eeedf1', '#7c61cb', '#d2d2d2', '#d4d4d5', '#d7d7d7', '#907ccc', '#6c4dc8', '#927cd3', '#eceaf0', '#e4def5', '#c8bfe3', '#6f50c8', '#ad9fd8', '#ccc2e7', '#efeef0', '#7053c6', '#cbcbcc', '#ebebeb', '#d8d0f2', '#d5ccf0', '#e0d9f4', '#ab9cd8', '#6b4cc8', '#927fc8', '#bfb6da', '#ccc2e8', '#d9d9da', '#d0d0d0', '#e0daf4', '#dfdfe0', '#d6d6d6', '#e4e4e4', '#dedde1', '#f5f4f7', '#795eca', '#ccc1e8', '#f8f8f9', '#e4e3e7', '#907ec6', '#bbb0d7', '#d3caf0', '#afa6c6', '#f6f6f7', '#6c4cca', '#fbfbfe', '#f5f5f5', '#c0bbce', '#cec4ea', '#fffeff', '#9080c0', '#ded9eb', '#6b4bc9', '#d2c8ee', '#a69fbd', '#b7aecf', '#dbd3f2', '#c4bbde', '#6d4dc6', '#c8c7ca', '#d3c9ef', '#afa6c9', '#bdb4d6', '#ddd6f3', '#dad2f2', '#fcfcfc', '#f5f3fc', '#bfb2e0', '#c7bee2', '#c2b8df', '#cdc4ea', '#836cc7', '#b1a9ca', '#cdcdce', '#e3e3e3', '#7d62cc', '#d6d6d7', '#9985d5', '#eaeaea', '#cacaca', '#a28fd8', '#7c64c5', '#dedede', '#e5e5e5', '#6a4bc8', '#e3ddf5', '#f4f4f4', '#f0f0f0', '#aba4c2', '#e1dbf5', '#e1e1e1', '#efefef', '#d0c6eb', '#e8e8e8', '#7558ca', '#795fc7', '#917bd2', '#c8bee3', '#fafafb', '#9f92c8', '#e8e8e9', '#7458c8', '#efeff0', '#8874c4', '#bdbbc1', '#f7f6fc', '#755ac6', '#d4cbf0', '#a293cf', '#dadada', '#6c4ccb', '#f5f2fc', '#b7aed0', '#8169ca', '#cccccd', '#bdb3d9', '#dcd7ea', '#9989ca', '#b5adcd', '#ececec', '#cacacb', '#bebdc1', '#bbb2d5', '#6a4bc7', '#7457c9', '#c7c6ca', '#937dd3', '#9682d0', '#c0b5e1', '#8871cd', '#846ec4', '#826cc1', '#9682d2', '#a69bc8', '#6a4ac7', '#e0e0e1', '#b9acdd', '#a296c3', '#cdcdcd', '#ededed', '#f6f6f6', '#cfc5eb', '#f3f3f4', '#e2e2e2', '#7357c7', '#b9b1d3', '#c3bfcd', '#d8cff1', '#f2f1f6', '#cfc5ea', '#7154c6', '#9282c3', '#c1b8da', '#c9c9ca', '#8873c4', '#6a4bc6', '#a797d8', '#846dc3', '#f6f5f7', '#c1b8db', '#d3d2d6', '#d3caef', '#947ed1', '#6f51c9', '#e9e9ea', '#eae9ed', '#d5d5d6', '#a290d8', '#f5f5f6', '#d0d0d1', '#6b4bc8', '#e4dff6', '#7a62c1', '#bfbec2', '#edecf0', '#e2e2e3', '#7b61c9', '#f4f4f5', '#e6e6e6', '#f9f9f9', '#7559ca', '#a594d8', '#aea6c6', '#bab7c3', '#c9c0e4', '#dddddd', '#dbdbdb', '#7b60cc', '#d3d3d3', '#b8afd3', '#cccccc', '#fbfbfb', '#f7f7f7', '#fefefe', '#e1dfe5', '#bbb4d2', '#a998da', '#7053c7', '#cbc1e6', '#dedce2', '#a08ed6', '#fcfbfe', '#cac1e6', '#fdfdfd', '#f8f7fc'}
            
#             check = purple_color.issubset(VideoPage.auto_play_switch_color)
            check = len(set(purple_color) & set(VideoPage.auto_play_switch_color)) > 150
            self.verify_true_or_false(browser, check, 'verify_purple_color', "Auto Play toggle button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_purple_color')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_purple_color')
            
    def verify_journey_next_btn_in_video_disabled(self, browser):
        try:
            next_btn_color_disabled = {'#e9e9e9', '#fafafa', '#bcbcbc', '#d1d1d1', '#bfbfbf', '#b3b3b3', '#c3c3c3', '#b5b5b5', '#cecece', '#dedede', '#c5c5c5', '#cfcfcf', '#f5f5f5', '#cbcbcb', '#bdbdbd', '#bebebe', '#cdcdcd', '#c4c4c4', '#c2c2c2', '#fdfdfd', '#d9d9d9', '#b1b1b1', '#d6d6d6', '#eeeeee', '#f0f0f0', '#f8f8f8', '#cccccc', '#b6b6b6', '#e2e2e2', '#ebebeb', '#bbbbbb', '#aeaeae', '#d4d4d4', '#d2d2d2', '#c9c9c9', '#dddddd', '#c7c7c7', '#f7f7f7', '#b8b8b8', '#f6f6f6', '#e7e7e7', '#c1c1c1', '#f3f3f3', '#acacac', '#afafaf', '#e4e4e4', '#fcfcfc', '#bababa', '#fbfbfb', '#b2b2b2', '#f4f4f4', '#f2f2f2', '#dfdfdf', '#c0c0c0', '#ffffff', '#e8e8e8', '#d5d5d5', '#e0e0e0', '#e6e6e6', '#ececec', '#d3d3d3', '#eaeaea', '#dbdbdb', '#d0d0d0', '#c6c6c6', '#b9b9b9', '#ededed', '#b0b0b0', '#f9f9f9', '#adadad', '#e5e5e5', '#dadada', '#cacaca', '#c8c8c8', '#fefefe', '#b7b7b7', '#b4b4b4', '#f1f1f1', '#e1e1e1', '#d7d7d7', '#e3e3e3', '#efefef', '#d8d8d8', '#dcdcdc'}
            current_next_btn_color = self.get_the_rgb_lst(browser, self.jounney_video_nxt_btn)
            check = len(set(next_btn_color_disabled) & set(current_next_btn_color)) > 10
            self.verify_true_or_false(browser, check, 'verify_purple_color', "Auto Play toggle button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_purple_color')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_purple_color')
            
            
    def verify_journey_next_btn_in_video_enabled(self, browser):
        try:
            self.wait_till_video_load(browser)
            next_btn_color_enabled = {'#c5c5c5', '#d6d6d6', '#dddddd', '#b3b3b3', '#afafaf', '#f7f7f7', '#f5f5f5', '#f2f2f2', '#d4d4d4', '#fafafa', '#ffffff', '#b6b6b6', '#c3c3c3', '#f3f3f3', '#c2c2c2', '#ebebeb', '#f4f4f4', '#c1c1c1', '#ededed', '#f0f0f0', '#e3e3e3', '#cfcfcf', '#fefefe', '#e6e6e6', '#b9b9b9', '#f8f8f8', '#d8d8d8', '#c4c4c4', '#d5d5d5', '#c6c6c6', '#ececec', '#d3d3d3', '#f9f9f9', '#dbdbdb', '#dcdcdc', '#d1d1d1', '#efefef', '#eaeaea', '#c9c9c9', '#acacac', '#cecece', '#dfdfdf', '#e8e8e8', '#bcbcbc', '#adadad', '#fdfdfd', '#e9e9e9', '#eeeeee', '#aeaeae', '#fbfbfb', '#b4b4b4', '#bbbbbb', '#d9d9d9', '#e1e1e1', '#e4e4e4', '#dadada', '#b0b0b0', '#c7c7c7', '#dedede', '#b1b1b1', '#bababa', '#c8c8c8', '#f6f6f6', '#cacaca', '#b5b5b5', '#f1f1f1', '#c0c0c0', '#e0e0e0', '#b2b2b2', '#b8b8b8', '#e2e2e2', '#bdbdbd', '#b7b7b7', '#d7d7d7', '#cccccc', '#bebebe', '#e5e5e5', '#fcfcfc', '#cbcbcb', '#cdcdcd', '#d2d2d2', '#e7e7e7', '#d0d0d0', '#bfbfbf'}
            current_next_btn_color = self.get_the_rgb_lst(browser, self.jounney_video_nxt_btn)
            check = len(set(next_btn_color_enabled) & set(current_next_btn_color)) > 10
            self.verify_true_or_false(browser, check, 'verify_purple_color', "Auto Play toggle button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_purple_color')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_purple_color')
            
            
    def verify_green_color(self, browser):
        green_color_lst = {'#69ab02', '#579f10', '#7abc01', '#62a901', '#5fa502', '#71b301', '#7cbb02', '#80c100', '#82bf02', '#84c301', '#60a502', '#7abc00', '#70b501', '#6fb101', '#6cae01', '#58a301', '#71b500', '#59a301', '#7dbb02', '#74b801', '#85c001', '#7ab901', '#67ae01', '#bbdeba', '#66ac01', '#76b900', '#7fbc01', '#5ca501', '#82be02', '#5aa401', '#60a901', '#61a502', '#91ba04', '#7dbe01', '#75b402', '#58a201', '#60a602', '#72b301', '#68ab02', '#60a802', '#81c100', '#7dbe00', '#77ba01', '#89c701', '#539f02', '#79bc01', '#78bb00', '#65a802', '#57a101', '#8ac803', '#72b202', '#62a602', '#5fa701', '#74b800', '#73b700', '#86c500', '#89c702', '#55a002', '#db5d22', '#fd3c3c', '#70b102', '#7ebf01', '#6bb001', '#c7774f', '#83c300', '#63ab02', '#56a102', '#80c101', '#8dc810', '#6daf02', '#6aad01', '#7dbf01', '#cd9253', '#67ae02', '#67ab01', '#82c201', '#6fb002', '#84c300', '#61a901', '#509d02', '#5ba502', '#7dba02', '#549f02', '#65ac01', '#549f01', '#6daf01', '#7bbc00', '#7ebc02', '#84c001', '#75b800', '#a1c432', '#87c601', '#c5e7aa', '#7fc000', '#6fb400', '#6db200', '#77b602', '#80c001', '#6bad02', '#79bb00', '#65ac02', '#61aa01', '#88c600', '#78bb01', '#71b102', '#9fd340', '#76b602', '#68ac01', '#5ea701', '#70b401', '#68ae01', '#85c401', '#73b601', '#73b401', '#88c601', '#73b600', '#60a801', '#64ac01', '#7fc001', '#539f01', '#87c302', '#9ed33f', '#84c400', '#79b902', '#64a801', '#80be02', '#66ad02', '#5da702', '#69af01', '#73b701', '#85c102', '#60a603', '#64ab02', '#64a802', '#66ad01', '#62aa02', '#7fbf00', '#83c200', '#75b601', '#a89e0e', '#e0f6fa', '#7bba02', '#71b201', '#5da403', '#78ba00', '#84c102', '#7ebb01', '#fc3d3d', '#77b900', '#7ab902', '#89c301', '#62aa01', '#529e01', '#7cbe01', '#6db201', '#85c101', '#86c400', '#7fbd02', '#83c301', '#6cae02', '#71a632', '#78b801', '#88c301', '#509c01', '#6fb301', '#7ebf00', '#7cbd00', '#75b501', '#74b701', '#529e02', '#80bd02', '#519d02', '#72b601', '#74b700', '#6eb001', '#56a101', '#5ba501', '#83bf02', '#89c602', '#4f9b01', '#7bbd01', '#4f9c02', '#57a201', '#6bae01', '#68af01', '#79bb01', '#59a302', '#6eb301', '#5ca601', '#5ea402', '#5ba401', '#5ca303', '#87c500', '#77b701', '#74b501', '#6aac02', '#5da302', '#79b702', '#5ea403', '#65aa02', '#87c600', '#509d01', '#78ba01', '#64ab01', '#5ea702', '#89c600', '#7bbd00', '#54a001', '#5da601', '#bbdeb9', '#81be02', '#5fa402', '#61aa02', '#519d01', '#67ad01', '#83c002', '#5da602', '#82bf01', '#58a202', '#61a602', '#7bbc01', '#7cba02', '#509c02', '#86c201', '#73b302', '#7cbd01', '#88c402', '#84c401', '#d24c24', '#8ac704', '#6fb300', '#519e02', '#55a001', '#75b801', '#82c200', '#65a903', '#5ca502', '#67aa02', '#5aa402', '#74b402', '#89c700', '#71b501', '#6ab001', '#86c202', '#6cb101', '#7ab802', '#79b801', '#65a902', '#6cb201', '#76b901', '#4f9c01', '#70b400', '#61a902', '#70b201', '#63ab01', '#62a701', '#6eb002', '#58a302', '#5fa802', '#6fb401', '#c5e7ab', '#e1f6fa', '#7dbc02', '#7ebd02', '#61a703', '#77b901', '#539e01', '#69ad01', '#76b601', '#66aa02', '#87c201', '#7bb902', '#81c101', '#80c000', '#6dae02', '#6bb101', '#72b600', '#73b23e', '#81c201', '#81bd01', '#85c400', '#78b702', '#86c501', '#5fa801', '#65ad01', '#63a802', '#89c402', '#85c501', '#63a702', '#7b810d', '#6db001', '#54a002', '#57a010', '#75b502', '#85c202', '#57a202'}
        current_thumbnail_color = self.get_the_rgb_lst(browser, self.current_tumbnail_progress_bar)
        check = len(set(green_color_lst) & set(current_thumbnail_color)) > 10
        self.verify_true_or_false(browser, check, 'verify_green_color', "video thumbnail progress bar color")
    
      
    def verify_grey_color(self, browser):
        try:
#             grey_color = {"#ececec","#b2b2b2"}
            grey_color = {'#b3b3b3', '#aeaeae', '#ededed', '#bebebe', '#e8e8e8', '#b5b5b5', '#adadad', '#f8f8f8', '#d0d0d0', '#acacac', '#f6f6f6', '#a6a6a6', '#cbcbcb', '#dbdbdb', '#d5d5d5', '#ebebeb', '#dcdcdc', '#c7c7c7', '#afafaf', '#b9b9b9', '#cecece', '#a3a3a3', '#bababa', '#fdfdfd', '#d7d7d7', '#c9c9c9', '#c5c5c5', '#d9d9d9', '#e9e9e9', '#bdbdbd', '#cacaca', '#fcfcfc', '#a1a1a1', '#eeeeee', '#b7b7b7', '#a7a7a7', '#e0e0e0', '#fbfbfb', '#f4f4f4', '#ffffff', '#979797', '#f1f1f1', '#eaeaea', '#f5f5f5', '#dadada', '#9a9a9a', '#e7e7e7', '#b2b2b2', '#b0b0b0', '#d4d4d4', '#e4e4e4', '#b1b1b1', '#cccccc', '#efefef', '#e6e6e6', '#a8a8a8', '#dfdfdf', '#b4b4b4', '#f0f0f0', '#dedede', '#cdcdcd', '#fefefe', '#d3d3d3', '#b6b6b6', '#9d9d9d', '#e5e5e5', '#a5a5a5', '#bfbfbf', '#dddddd', '#ababab', '#b8b8b8', '#f9f9f9', '#fafafa', '#f3f3f3', '#ececec', '#d6d6d6', '#e1e1e1', '#d1d1d1', '#c3c3c3', '#e2e2e2', '#d2d2d2', '#aaaaaa', '#f7f7f7', '#f2f2f2'}
#             check = grey_color.issubset(VideoPage.auto_play_switch_color)
            check = len(set(grey_color) & set(VideoPage.auto_play_switch_color)) > 50
            self.verify_true_or_false(browser, check, 'verify_grey_color', "Auto Play toggle button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_grey_color')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_grey_color')
    
            
    def verify_video_player_previous_btn(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.video_play_previous_btn, 3)
            self.verify_false(browser, check, 'verify_video_player_previous_btn', 'previous Btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_video_player_previous_btn')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_player_previous_btn')  
    
    
    def verify_video_player_previous_cancel_btn(self, browser):
        try:
            """Works for both mobile and tab"""
            check1 = CommonMethods.wait_for_element_visible(browser, self.video_up_next, 3)
            check2 = CommonMethods.wait_for_element_visible(browser, self.video_video_player_chapter_txt, 3)
            check3 = CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 3)
            self.verify_false(browser, check1, 'verify_video_player_previous_cancel_btn', 'video up next')
            self.verify_false(browser, check2, 'verify_video_player_previous_cancel_btn', 'chapter text')
            self.verify_false(browser, check3, 'verify_video_player_previous_cancel_btn', 'Cancel Btn') 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_video_player_previous_cancel_btn')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_player_previous_cancel_btn') 
            
    def verify_video_player_next_btn(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.video_play_next_btn, 5)
            self.verify_true_or_false(browser, check, 'verify_video_player_next_btn', 'Next Btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_video_player_next_btn')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_player_next_btn')   
            
            
    def verify_video_player_next_btn_not_present(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.video_play_next_btn, 5)
            self.verify_false(browser, check, 'verify_video_player_next_btn_not_present', 'Next Btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_video_player_next_btn_not_present')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_player_next_btn_not_present')   
            
    def tap_on_reply_icon(self, browser):
        try:
            sleep(2)
            check = CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 3)
            VideoPage.video_sub_title_name = CommonMethods.getTextOfElement(browser, self.video_title)
            if check == True:
                CommonMethods.elementClick(browser, self.video_play_btn)
                logging.info('clicked on auto replay icon')
            else:
                logging.info("Failed due to Element not visible in tap_on_reply_icon")
                CommonMethods.takeScreenShot(browser,featureFileName)
                pytest.fail("Failed due to Element not visible in Video Page")  
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_video_player_next_btn')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_player_next_btn')
            
    def verify_reply_icon(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser,self.video_play_btn)
            self.verify_true_or_false(browser, check, 'verify_reply_icon', "Reply Button")   
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_reply_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_reply_icon')
    
    """" This is used to verify whether the next arrow icon is there or not"""        
    def verify_play_next_icon(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser,self.video_play_next_btn)
            self.verify_true_or_false(browser, check, 'verify_play_next_icon', "play next Button") 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_play_next_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_play_next_icon')
    
    """"This is used to verify the current video name on the video Player"""        
    def verify_current_video_name(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                actual = CommonMethods.getTextOfElement(browser, self.mob_video_title_on_player)
                expected = CommonMethods.getTextOfElement(browser, self.video_title_in_list_id)
                check = CommonMethods.verifyTwoText(actual, expected)
                self.verify_true_or_false(browser, check, 'verify_current_video_name', "title on player matches")    
            elif device == 'tab':
                actual = CommonMethods.getTextOfElement(browser, self.video_title_on_player)
                expected = CommonMethods.getTextOfElement(browser, self.video_title_in_list_id)
                check = CommonMethods.verifyTwoText(actual, expected)
                self.verify_true_or_false(browser, check, 'verify_current_video_name', "title on player matches")    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_current_video_name')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_current_video_name')
    
    """This method tap on last link in video list lay"""        
    def tap_on_last_video_in_list(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                self.click_on_video_last_lnk(browser)
            elif device == 'tab':
                self.click_on_video_last_lnk(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_last_video_in_list_and_complete')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_last_video_in_list_and_complete')
    
    def complete_video(self, browser):
        try:
            self.wait_till_video_load(browser)
            sleep(5)
            self.pause_video(browser)
            self.end_the_video(browser)
#             self.verify_pause_btn(browser)
            self.verify_seek_bar_is_near_to_complete(browser)
            self.tap_on_video_player_icon(browser, self.video_play_btn)
#             check = CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 120)
            check = CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 120) or CommonMethods.wait_for_element_visible(browser, self.video_frame_pause_btn, 60) or CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 60)
            self.verify_true_or_false(browser, check, 'complete_video', 'Play Btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'complete_video')
        except:
            CommonMethods.exception(browser, featureFileName, 'complete_video')
            
    def verify_seek_bar_is_near_to_complete(self, browser):
        check = True
        while check:
            self.wait_till_video_load(browser)
            start_time = CommonMethods.getTextOfElement(browser, self.progressTime_id)
            start_time = start_time.split(':')
            minutes = int(start_time[0])
            sec = int(start_time[1])
            start_time = minutes*60 + sec
            end_time = CommonMethods.getTextOfElement(browser, self.remaingTime_id)
            end_time = end_time.split(':')
            minutes = int(end_time[0])
            sec = int(end_time[1])
            end_time = minutes*60 + sec
            if (end_time - start_time) <= 20:
                check =False
            else:
                CommonMethods.elementClick(browser, self.ten_sec_fwd_btn_id)
        
    def check_for_alerts(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.video_badge_close_btn, 4):
                CommonMethods.elementClick(browser, self.video_badge_close_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'complete_video')
        except:
            CommonMethods.exception(browser, featureFileName, 'complete_video')       
            
    def seek_video_50_percent(self, browser):
        try:
            self.wait_till_video_load(browser)
            self.pause_video(browser)
            CommonMethods.run('adb shell input tap 612 770')
            VideoPage.video_start_time = self.get_video_start_time(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'seek_video_50_percent')
        except:
            CommonMethods.exception(browser, featureFileName, 'seek_video_50_percent')
            
            
    def verify_video_play_from_left(self, browser):
        try:
            self.play_video(browser)
            actual_time = self.get_video_start_time(browser)
            expected_time = VideoPage.video_start_time
            check = actual_time > expected_time
            self.verify_true_or_false(browser, check, 'verify_video_play_from_left', 'video time') 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_video_play_from_left')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_play_from_left')
            
            
    def wait_till_autoload_completes(self, browser):
        try:
            VideoPage.next_video_title = CommonMethods.getTextOfElement(browser, self.video_next_video_title)
            CommonMethods.wait_for_element_visible(browser, self.video_auto_play_btn, 5)
            sleep(7) # till the auto load completes
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'wait_till_autoload_completes')
        except:
            CommonMethods.exception(browser, featureFileName, 'wait_till_autoload_completes')
    
    
    def Complete_the_video_till_end(self, browser):
        try:
            self.wait_till_video_load(browser)
            self.pause_video(browser)
            self.end_the_video(browser)
            self.play_video(browser)
            check = CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 60)
            if check == True:
                CommonMethods.elementClick(browser, self.video_auto_cancelBtn_id)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'Complete_the_video_till_end')

        except:
            CommonMethods.exception(browser, featureFileName, 'Complete_the_video_till_end')
    
    def click_on_video_last_lnk(self, browser):
        try:
            CommonMethods.scrollToElement(browser, 'Practice')
            ele = CommonMethods.getElements(browser, self.video_play_list_elements)
            size = len(ele)
            ele[size-1].click() 
        except:
            logging.info('Error in clicking on last video link') 
            
            
    def tap_on_2nd_video_lnk_and_complete(self, browser):
        try:
            self.click_on_2nd_video_lnk(browser)
            self.wait_till_video_load(browser)
            self.end_the_video(browser)
            self.wait_till_video_load(browser)
            self.play_video(browser)
            flag = CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 30)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_last_video_in_list_and_complete')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_last_video_in_list_and_complete')
    
    def get_index_of_the_playing_video(self, browser):
        try:
            ele = CommonMethods.getElements(browser, self.video_play_list_elements)
            for i in range(len(ele)):
                element = ele[i]
                check = element.get_attribute('selected')
                if check == 'true':
                    return i+1 # index starts with zero so we are adding 1 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_last_video_in_list_and_complete')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_last_video_in_list_and_complete')
    
    def tap_on_second_video_lnk(self, browser):
        try:
            self.click_on_2nd_video_lnk(browser)
            self.wait_till_video_load(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_second_video_lnk')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_second_video_lnk')        
    
    def get_text_of_video_in_list(self, browser, position):
        ele = CommonMethods.getElements(browser, self.video_play_list_elements)
        videoName = ele[position-1].text
        return videoName 
    
            
    def click_on_2nd_video_lnk(self, browser):
        try:
            ele = CommonMethods.getElements(browser, self.video_play_list_elements)
            ele[1].click() 
        except:
            logging.info('Error in clicking on 2nd video link')
            
            
    def click_on_1st_video_lnk(self, browser):
        try:
            ele = CommonMethods.getElements(browser, self.video_play_list_elements)
            ele[0].click() 
        except:
            logging.info('Error in clicking on 1st video link')
            
    def get_elements_coordinates(self, browser, locator, position):
        try:
            ele = CommonMethods.getElements(browser, locator)
            element = ele[position-1]
            loc = element.location
            x = loc["x"]
            y = loc["y"]
            return x,y
        except:
            logging.info('Error in getting coordinate of the element')
            
    def get_text_of_video_lnk(self, browser, position):
        try:
            ele = CommonMethods.getElements(browser, self.video_play_list_elements)
            element_txt = ele[position-1].text
            return element_txt
        except:
            logging.info('Error in getting the video ele link')
            
    def verify_auto_loading_not_present(self, browser):
        try:
            """Works for both mobile and tab"""
            check = CommonMethods.wait_for_element_visible(browser, self.video_auto_play_btn, 3)
            self.verify_false(browser, check, 'verify_auto_loading_not_present', 'auto play')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_auto_loading_not_present')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_auto_loading_not_present') 
             
            
    def verify_reply_icon_is_shown(self, browser):
        try:
            check =CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 3)
            self.verify_true_or_false(browser, check, 'verify_reply_icon_is_shown', 'reply icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_reply_icon_is_shown')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_reply_icon_is_shown')  
            
    def verify_previour_next_icon_is_shown(self, browser):
        try:
            check1 =CommonMethods.wait_for_element_visible(browser, self.video_play_next_btn, 3)
            self.verify_true_or_false(browser, check1, 'verify_previour_next_icon_is_shown', 'next icon')
            check2 =CommonMethods.wait_for_element_visible(browser, self.video_play_previous_btn, 3)
            self.verify_true_or_false(browser, check2, 'verify_previour_next_icon_is_shown', 'previous icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_previour_next_icon_is_shown')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_previour_next_icon_is_shown') 
            
    def end_the_video(self,browser):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1 
#                 self.pause_video(browser) 
#                 x1,y1,x2,y2 = self.get_element_coordinates(browser, self.video_progressBar_id)
#                 x2 = x2-33
#                 y2 = y2-22
#                 CommonMethods.run('adb shell input tap {} {}'.format(x2, y2))
                x1,y1,x2,y2 = self.get_element_coordinates(browser, self.video_progressBar_id)
                x2 = x2-50
                y2 = y2-20
                CommonMethods.run('adb shell input touchscreen swipe {} {} {} {}'.format(x1, y1, x2, y2))
                check = not True
        except:
            logging.info("Error in ending the video") 
            
    def drag_video_progress_to_half(self, browser):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1 
                x1,y1 = self.get_element_coordinates(browser, self.video_tab_videoframe)
                CommonMethods.run('adb shell input tap {} {}'.format(x1+30, y1+100))
                x1,y1,x2,y2 = self.get_element_coordinates(browser, self.video_progressBar_id)
                x2 = x2/2
                y2 = y2/2
                CommonMethods.run('adb shell input touchscreen swipe {} {} {} {}'.format(x1, y1, x2, y2))
                check = not True
        except:
            logging.info("Error in drag_progress_to_half in the video") 
         
            
    def start_the_video(self,browser):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1 
#                 self.pause_video(browser) 
                x1,y1,x2,y2 = self.get_element_coordinates(browser, self.video_progressBar_id)
                CommonMethods.run('adb shell input tap {} {}'.format(x1, y1))
#                 CommonMethods.run('adb shell input touchscreen swipe {} {} {} {}'.format(x1,y2,x2, y2))
                check = not True
        except:
            logging.info("Error in ending the video")          
                 
            
    def end_till_cancel_btn(self,browser):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1 
                self.pause_video(browser) 
                x1,y1,x2,y2 = self.get_element_coordinates(browser, self.video_progressBar_id)
                CommonMethods.run('adb shell input touchscreen swipe {} {} {} {}'.format(x1, y1, x2-10, y2-10))
                check = False
        except:
            logging.info("Error in ending the video")
            
            
    def verify_same_video_is_played(self, browser):
        try:
            self.wait_till_video_load(browser)
            sleep(5)
            video_title_now = CommonMethods.getTextOfElement(browser, self.video_title)
            video_title_previous = VideoPage.video_sub_title_name
            check = video_title_now == video_title_previous
            self.verify_true_or_false(browser, check, 'verify_same_video_is_played', 'video sub tile')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_same_video_is_played')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_same_video_is_played')
            
    def user_redirects_to_journey_screen(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.journey_node_title, 10)
            self.verify_true_or_false(browser, check, 'user_redirects_to_journey_screen', 'journey screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'user_redirects_to_journey_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'user_redirects_to_journey_screen')
            
            
    def tap_on_next_btn_in_video_player(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                check = CommonMethods.wait_for_element_visible(browser, self.video_play_next_btn, 3)
                current_link_index = self.get_index_of_the_playing_video(browser)
                VideoPage.video_sub_title_name = self.get_text_of_video_lnk(browser, current_link_index+1)
                if check == True:
                    CommonMethods.elementClick(browser, self.video_play_next_btn)
                    logging.info('clicked on next icon')
                else:
                    logging.info("Failed due to Element not visible in tap_on_next_icon")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
            elif device == 'tab':
                check = CommonMethods.wait_for_element_visible(browser, self.video_play_next_btn, 3)
                self.get_video_slider_window()
                current_link_index = self.get_index_of_the_playing_video(browser)
                VideoPage.video_sub_title_name = self.get_text_of_video_lnk(browser, current_link_index+1)
                logging.info("nexe video name- "+VideoPage.video_sub_title_name)
                if check == True:
                    CommonMethods.elementClick(browser, self.video_list_close_btn_tab)
                    CommonMethods.elementClick(browser, self.video_play_next_btn)
                    logging.info('clicked on next icon')
                else:
                    logging.info("Failed due to Element not visible in tap_on_next_icon")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_next_btn_in_video_player')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_next_btn_in_video_player')  
    
    def get_video_slider_window(self):
        CommonMethods.run("adb shell input touchscreen swipe 1270 350 700 350")    
        
        
    def click_next_btn_video_player(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.video_play_next_btn, 10)
            VideoPage.video_sub_title_name = CommonMethods.getTextOfElement(browser, self.video_title)
            CommonMethods.elementClick(browser, self.video_play_next_btn)
            logging.info('clicked on next button') 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_next_btn_in_video_player')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_next_btn_in_video_player')   
            
    def tap_on_previous_icon_in_video_player(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                check = CommonMethods.wait_for_element_visible(browser, self.video_play_previous_btn, 3)
                current_link_index = self.get_index_of_the_playing_video(browser)
                VideoPage.video_sub_title_name = self.get_text_of_video_lnk(browser, current_link_index-1)
                if check == True:
                    CommonMethods.elementClick(browser, self.video_play_previous_btn)
                    logging.info('clicked on previous icon')
                else:
                    logging.info("Failed due to Element not visible in tap_on_previous_icon")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page") 
            elif device == 'tab':
                check = CommonMethods.wait_for_element_visible(browser, self.video_play_previous_btn, 3)
                self.get_video_slider_window()
                current_link_index = self.get_index_of_the_playing_video(browser)
                VideoPage.video_sub_title_name = self.get_text_of_video_lnk(browser, current_link_index-1)
                if check == True:
                    CommonMethods.elementClick(browser, self.video_list_close_btn_tab)
                    CommonMethods.elementClick(browser, self.video_play_previous_btn)
                    logging.info('clicked on next icon')
                else:
                    logging.info("Failed due to Element not visible in tap_on_previous_icon")
                    CommonMethods.takeScreenShot(browser,featureFileName)
                    pytest.fail("Failed due to Element not visible in Video Page")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_previous_icon_in_video_player')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_previous_icon_in_video_player') 
            
    
    def verify_next_video_is_played(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                sleep(7)
                self.wait_till_video_load(browser)
                video_title_now = CommonMethods.getTextOfElement(browser, self.video_title)
                video_title_previous = VideoPage.video_sub_title_name 
                check = video_title_now == video_title_previous
                self.verify_true_or_false(browser, check, 'verify_next_video_is_played', 'video sub tile')
            elif device == 'tab':
                sleep(7)
                self.wait_till_video_load(browser)
                video_title_now = self.get_video_title_on_player(browser)
#                 video_title_previous = VideoPage.video_sub_title_name
                video_title_previous = VideoPage.video_sub_title_name
                check = video_title_now == video_title_previous
                self.verify_true_or_false(browser, check, 'verify_next_video_is_played', 'video sub tile') 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_next_video_is_played')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_next_video_is_played')     
            
            
    def verify_previous_video_is_played(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                sleep(5)
                self.wait_till_video_load(browser)
                video_title_now = CommonMethods.getTextOfElement(browser, self.video_title)
                video_title_previous = VideoPage.video_sub_title_name
                check = video_title_now == video_title_previous
                self.verify_true_or_false(browser, check, 'verify_next_video_is_played', 'video sub tile')
            elif device == 'tab':
                self.wait_till_video_load(browser)
                video_title_now = self.get_video_title_on_player(browser)
                video_title_previous = VideoPage.video_sub_title_name
                check = video_title_now == video_title_previous
                self.verify_true_or_false(browser, check, 'verify_next_video_is_played', 'video sub tile') 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_previous_video_is_played')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_previous_video_is_played')  
                
    def tap_on_video_player_setting_icon(self, browser):
        try:
            self.wait_till_video_load(browser)
            self.tap_on_video_player_icon(browser, self.video_pause_btn_id)
            check = CommonMethods.elementClick(browser, self.video_settingIcon_id)
            self.verify_true_or_false(browser, check, 'tap_on_video_player_setting_icon', 'setting icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_video_player_setting_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_video_player_setting_icon')
    
    def verify_subtopic_video_slider(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.video_player_list_lay, 10)
            self.verify_true_or_false(browser, check, 'verify_subtopic_video_slider', 'setting icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_subtopic_video_slider')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_subtopic_video_slider')              
    
    """This method will tap on cancel button once the video is completed and stores the next video title"""        
    def tap_on_cancel_button(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 10)
                VideoPage.next_video_title = CommonMethods.getTextOfElement(browser, self.video_next_video_title)
                check = CommonMethods.elementClick(browser, self.video_auto_cancelBtn_id)
                self.verify_true_or_false(browser, check, 'tap_on_cancel_button', 'cancel button')
            elif device == 'tab':
                CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 10)
                VideoPage.next_video_title = CommonMethods.getTextOfElement(browser, self.video_next_video_title)
                check = CommonMethods.elementClick(browser, self.video_auto_cancelBtn_id)
                self.verify_true_or_false(browser, check, 'tap_on_cancel_button', 'cancel button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_cancel_button')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_cancel_button')
            
            
    def select_video_from_list(self, browser, video_name):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                CommonMethods.scrollToElementAndClick(browser, video_name)
                VideoPage.video_end_time = self.get_video_end_time(browser)
#             elif device == 'tab':
#                 CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 10)
#                 VideoPage.next_video_title = CommonMethods.getTextOfElement(browser, self.video_next_video_title)
#                 check = CommonMethods.elementClick(browser, self.video_auto_cancelBtn_id)
#                 self.verify_true_or_false(browser, check, 'tap_on_cancel_button', 'cancel button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'select_video_from_list')
        except:
            CommonMethods.exception(browser, featureFileName, 'select_video_from_list')
    
    ''' gmailverify_tap methods verifies gmail icon in share bottomsheet dialog  and taps on it   '''         
    def tap_on_gmail_icon(self,browser):
        try:
            if CommonMethods.wait_for_element_visible( browser, self.Gmail_text, 5):
                CommonMethods.elementClick( browser, self.Gmail_text)
                if CommonMethods.wait_for_element_visible( browser, self.Gmail_text, 5):
                    CommonMethods.elementClick( browser, self.Gmail_text)
            else:
                logging.info('Gmail option  not found ')
                pytest.fail("Failed due to gmail option is not present in bottomsheet")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'gmailverify_tap')  
               
        except:
            CommonMethods.exception(browser, featureFileName, 'gmailverify_tap')        
            
                     
    def verify_gmail_shared_via_gmail(self,browser):
        """
        this method verifies the content is sharing via gmail medium
        
        variable : None
        
        
        return Type : None
        """
        try:
            check = CommonMethods.scrollToElement(browser, "Compose") and CommonMethods.scrollToElement(browser, "BYJU'S The Learning App")
            if check:
                logging.info("successfuly the app content is sharing via gmail")    
            else:
                logging.info('Gmail is not visible or the device is not signed in with any of the gmail Account')
                pytest.fail("Failed due to not signed in with any of the gmail Account")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'gmailverify_tap')  
               
        except:
            CommonMethods.exception(browser, featureFileName, 'gmailverify_tap')      
            
    def tap_on_video_share_icon(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                CommonMethods.wait_for_element_visible(browser, self.video_share_icon_id, 10)
                CommonMethods.elementClick(browser, self.video_share_icon_id)
#             elif device == 'tab':
#                 CommonMethods.wait_for_element_visible(browser, self.video_auto_cancelBtn_id, 10)
#                 VideoPage.next_video_title = CommonMethods.getTextOfElement(browser, self.video_next_video_title)
#                 check = CommonMethods.elementClick(browser, self.video_auto_cancelBtn_id)
#                 self.verify_true_or_false(browser, check, 'tap_on_cancel_button', 'cancel button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_video_share_icon')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_video_share_icon')
            
            
    def verify_setting_bottom_sheet(self, browser):
        try:
            check =  CommonMethods.isElementPresent(browser, self.video_auto_play_buttom_sheet)
            self.verify_true_or_false(browser, check, 'verify_setting_bottom_sheet', 'auto play switch')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_setting_bottom_sheet')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_setting_bottom_sheet')
            
            
    def complete_video_without_performing_any_action(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.video_play_btn, VideoPage.video_end_time)
            self.verify_true_or_false(browser, check, 'complete_video_without_performing_any_action', 'Video Complete')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'complete_video_without_performing_any_action')
        except:
            CommonMethods.exception(browser, featureFileName, 'complete_video_without_performing_any_action')
            
            
            
    def verify_video_player_reply_icon(self, browser):
        try:
            check =  CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 10)
            self.verify_true_or_false(browser, check, 'verify_setting_bottom_sheet', 'auto play switch')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_setting_bottom_sheet')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_setting_bottom_sheet')
            
            
    def verify_back_btn_on_video(self, browser):
        try:
            check =  CommonMethods.isElementPresent(browser, self.video_player_back_btn)
            self.verify_true_or_false(browser, check, 'verify_back_btn_on_video', 'auto play switch')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_back_btn_on_video')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_back_btn_on_video')
            
            
    def verify_previous_icon_on_video(self, browser):
        try:
            check =  CommonMethods.isElementPresent(browser, self.video_play_previous_btn)
            self.verify_true_or_false(browser, check, 'verify_previous_icon_on_video', 'previous btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_previous_icon_on_video')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_previous_icon_on_video')
            
    def verify_previous_icon_not_on_video(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.video_play_previous_btn, 10)
            self.verify_false(browser, check, 'verify_previous_icon_on_video', 'previous btn')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_previous_icon_on_video')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_previous_icon_on_video')
            
    
    def tap_on_analysis_icon(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.video_analyze_icon_btn, 5)
            if check == True:
                CommonMethods.elementClick(browser, self.video_analyze_icon_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_analysis_icon')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_analysis_icon')
            
            
    def tap_on_keyFocus_area(self, browser):
        try:
            CommonMethods.scrollToElement(browser, 'Key focus areas')
            check = CommonMethods.wait_for_element_visible(browser, self.video_keyFocus_1st_lnk, 7)
            if check == True:
                CommonMethods.elementClick(browser, self.video_keyFocus_1st_lnk)
            elif CommonMethods.wait_for_element_visible(browser, self.analysis_screen_start_test, 7) or CommonMethods.wait_for_element_visible(browser, self.analysis_screen_continue_test, 7):
                CommonMethods.elementClick(browser, self.analysis_screen_start_test)
                CommonMethods.elementClick(browser, self.analysis_screen_continue_test)
                subject = (By.XPATH,"//android.widget.TextView[@text='Physics']")
                CommonMethods.wait_for_element_visible(browser, subject, 10)
                CommonMethods.elementClick(browser, subject)
                if CommonMethods.wait_for_element_visible(browser, self.verify_library_screen, 10):
                    logging.info('successfully navigated to library')
                else:
                    ele = CommonMethods.getElements(browser, self.chapter_screen_library_personalize_btn_elements)
                    ele[1].click()
                    logging.info('successfully navigated to library')
                CommonMethods.scrollToElementAndClick(browser, "Test")
                Start = (By.XPATH,"//android.widget.TextView[@text='Start']")
                CommonMethods.wait_for_element_visible(browser, Start, 10)
                ele = CommonMethods.getElements(browser, Start)
                ele[0].click()
                CommonMethods.wait_for_element_visible(browser, (By.ID,"com.byjus.thelearningapp.premium:id/test_start_button"), 10)
                CommonMethods.elementClick(browser, (By.ID,"com.byjus.thelearningapp.premium:id/test_start_button"))
                CommonMethods.wait_for_element_visible(browser, (By.XPATH,"//android.widget.Button[@text='Submit']"), 10)
                CommonMethods.elementClick(browser, (By.XPATH,"//android.widget.Button[@text='Submit']"))
                CommonMethods.wait_for_element_visible(browser, (By.XPATH,"//android.widget.Button[@text='Submit']"), 10)
                CommonMethods.elementClick(browser, (By.XPATH,"//android.widget.Button[@text='Submit']"))
                browser.start_activity('com.byjus.thelearningapp.premium','com.byjus.app.home.activity.HomeActivity')
                self.verify_corana_dialog(browser)
                self.tap_on_analysis_icon(browser)
                CommonMethods.scrollToElement(browser, 'Key focus areas')
                check = CommonMethods.wait_for_element_visible(browser, self.video_keyFocus_1st_lnk, 7)
                if check == True:
                    CommonMethods.elementClick(browser, self.video_keyFocus_1st_lnk)
                else:
                    logging.info("Error in taking test")
                    pytest.fail("Error in taking test")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_keyFocus_area')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_keyFocus_area')
#     def end_the_video(self, browser):
#         try: 
#             self.wait_till_video_load(browser)
#             x,y = self.get_element_coordinates(browser, self.video_progressBar_id)
#             self.click_on_video_icon(browser, self.video_play_btn)
#             x2 = x-10
#             y2 = y-10
#             sleep(3)
#             CommonMethods.elementClick(browser, self.video_frame_id)
#             self.click_on_x_y_coordinate(x2, y2) 
#             CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 60)
#         except:
#             logging.info("Error in ending the video")  

    def verify_comming_soon_on_video_card(self, browser, chapter):
        try:
            CommonMethods.scrollToElement(browser, chapter)
            comming_soon_locator = (By.XPATH,"//android.widget.TextView[@text=\'"+chapter+"\']//parent::android.widget.RelativeLayout//following-sibling::androidx.recyclerview.widget.RecyclerView//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_comingsoon_txtvw']")
            check = CommonMethods.isElementPresent(browser, comming_soon_locator)
            self.verify_true_or_false(browser, check, 'verify_comming_soon_on_video_card', 'Comming soon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_comming_soon_on_video_card')
        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_comming_soon_on_video_card')
            
            
    def tap_on_comming_soon_on_video_card(self, browser, chapter):
        try:
            comming_soon_locator = (By.XPATH,"//android.widget.TextView[@text=\'"+chapter+"\']//parent::android.widget.RelativeLayout//following-sibling::androidx.recyclerview.widget.RecyclerView//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_comingsoon_txtvw']")
            CommonMethods.elementClick(browser, comming_soon_locator)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_comming_soon_on_video_card')
        
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_comming_soon_on_video_card')
            
            
    def verify_comming_soon_dialog(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.video_comming_soon_dialog_popup, 5)
            check = CommonMethods.isElementPresent(browser, self.video_comming_soon_dialog_popup)
            self.verify_true_or_false(browser, check, 'verify_comming_soon_dialog', 'Comming soon text')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_comming_soon_dialog')
        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_comming_soon_dialog')
            
            
    def verify_test_card_is_present(self, browser):
        try:
            self.wait_till_video_load(browser)
            CommonMethods.scrollToElement(browser, 'Test')
            CommonMethods.wait_for_element_visible(browser, self.video_test_lnk, 5)
            check = CommonMethods.isElementPresent(browser, self.video_test_lnk)
            self.verify_true_or_false(browser, check, 'verify_test_card_is_present', 'Test Link')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_test_card_is_present')
        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_test_card_is_present')
            
    def verify_practice_card_is_present(self, browser):
        try:
            self.wait_till_video_load(browser)
            CommonMethods.scrollToElement(browser, 'Practice')
            CommonMethods.wait_for_element_visible(browser, self.video_practice_lnk, 5)
            check = CommonMethods.isElementPresent(browser, self.video_practice_lnk)
            self.verify_true_or_false(browser, check, 'verify_practice_card_is_present', 'Test Link')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_practice_card_is_present')
        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_practice_card_is_present')
            
            
    def verify_test_icon_is_present(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.video_test_icon, 5)
            check = CommonMethods.isElementPresent(browser, self.video_test_icon)
            self.verify_true_or_false(browser, check, 'verify_test_icon_is_present', 'Test icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_test_icon_is_present')
        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_test_icon_is_present')
    
    def verify_practice_icon_is_present(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.video_practice_icon, 5)
            check = CommonMethods.isElementPresent(browser, self.video_practice_icon)
            self.verify_true_or_false(browser, check, 'verify_practice_icon_is_present', 'Practice icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_practice_icon_is_present')
        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_practice_icon_is_present')        
            
    def verify_test_label_is_present(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.video_test_lable, 5)
            check = CommonMethods.isElementPresent(browser, self.video_test_lable)
            self.verify_true_or_false(browser, check, 'verify_test_label_is_present', 'Test Lable ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_test_label_is_present')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_test_label_is_present')
    
    
    def verify_practice_label_is_present(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.video_practice_lable, 5)
            check = CommonMethods.isElementPresent(browser, self.video_practice_lable)
            self.verify_true_or_false(browser, check, 'verify_practice_label_is_present', 'Practice Lable ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_practice_label_is_present')        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_practice_label_is_present')       
            
    def verify_x_test_is_present(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.video_test_x_test, 5)
            check = CommonMethods.isElementPresent(browser, self.video_test_x_test)
            self.verify_true_or_false(browser, check, 'verify_x_test_is_present', 'X test')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_x_test_is_present')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_x_test_is_present')
            
            
    def verify_pratice_stage_name_is_present(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.video_practice_stage_name_test, 5)
            check = CommonMethods.isElementPresent(browser, self.video_practice_stage_name_test)
            self.verify_true_or_false(browser, check, 'verify_pratice_stage_name_is_present', 'Practice stag name')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_pratice_stage_name_is_present')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_pratice_stage_name_is_present')
            
    def verify_forward_icon_test(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.video_test_right_arrow, 5)
            check = CommonMethods.isElementPresent(browser, self.video_test_right_arrow)
            self.verify_true_or_false(browser, check, 'verify_forward_icon_test', 'Forward Icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_forward_icon_test')
        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_forward_icon_test')
            
            
    def verify_forward_icon_practice(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.video_practice_right_arrow, 5)
            check = CommonMethods.isElementPresent(browser, self.video_practice_right_arrow)
            self.verify_true_or_false(browser, check, 'verify_forward_icon_practice', 'Forward Icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_forward_icon_practice')
        
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_forward_icon_practice')
            
    def tap_on_test_on_video_sub_list(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                self.wait_till_video_load(browser)
                CommonMethods.scrollToElement(browser, 'Test')
                VideoPage.chapter_name = CommonMethods.getTextOfElement(browser, self.video_chapter_title_in_video_list)
                chapter=  VideoPage.chapter_name
                check = CommonMethods.wait_for_element_visible(browser, self.video_test_right_arrow, 5)
                CommonMethods.elementClick(browser, self.video_test_right_arrow)
                logging.info(VideoPage.chapter_name)
                self.verify_true_or_false(browser, check, 'tap_on_test_on_video_sub_list', 'Test link')
            elif device == 'tab':
                CommonMethods.scrollToElement(browser, 'Test')
                VideoPage.chapter_name = CommonMethods.getTextOfElement(browser, self.video_chapter_name_id)
                check = CommonMethods.wait_for_element_visible(browser, self.video_test_right_arrow, 5)
                CommonMethods.elementClick(browser, self.video_test_right_arrow)
                self.verify_true_or_false(browser, check, 'tap_on_test_on_video_sub_list', 'Test link')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_test_on_video_sub_list')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_test_on_video_sub_list') 
    
    
    def tap_on_start_btn_in_test_screen_finish_test(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                if CommonMethods.scrollToElementAndClick(browser, 'Start'):
                    CommonMethods.wait_for_element_visible(browser, self.test_screen_Test_btn, 10)
                    CommonMethods.elementClick(browser, self.test_screen_Test_btn)
                    CommonMethods.wait_for_element_visible(browser, self.self.test_submit_Btn, 10)
                    CommonMethods.elementClick(browser, self.test_submit_Btn)
                    CommonMethods.wait_for_element_visible(browser, self.self.test_submit_Btn, 10)
                    CommonMethods.elementClick(browser, self.test_submit_Btn)
                    CommonMethods.elementClick(browser, self.video_badge_close_btn)
                    browser.start_activity('com.byjus.thelearningapp.premium','com.byjus.app.home.activity.HomeActivity')
                    self.verify_corana_dialog(browser)
                else:
                    logging.info('The keyfocus screen has videos')
            elif device == 'tab':
                start_btn = CommonMethods.getElements(browser, self.test_screen_start_elements)
                start_btn[0].click()
                check = CommonMethods.wait_for_element_visible(browser, self.test_screen_Test_btn, 5)
                self.verify_true_or_false(browser, check, 'tap_on_start_btn_in_test_screen', 'Test link')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_start_btn_in_test_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_start_btn_in_test_screen')         
            
    def tap_on_practice_on_video_sub_list(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                CommonMethods.scrollToElement(browser, 'Practice')
                VideoPage.chapter_name = CommonMethods.getTextOfElement(browser, self.video_chapter_title_in_video_list)
                check = CommonMethods.wait_for_element_visible(browser, self.video_practice_right_arrow, 5)
                CommonMethods.elementClick(browser, self.video_practice_right_arrow)
                self.verify_true_or_false(browser, check, 'tap_on_practice_on_video_sub_list', 'Test link')
            elif device == 'tab':
                CommonMethods.scrollToElement(browser, 'Practice')
                VideoPage.chapter_name = CommonMethods.getTextOfElement(browser, self.video_chapter_name_id)
                check = CommonMethods.wait_for_element_visible(browser, self.video_practice_right_arrow, 5)
                CommonMethods.elementClick(browser, self.video_practice_right_arrow)
                self.verify_true_or_false(browser, check, 'tap_on_practice_on_video_sub_list', 'Test link')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_practice_on_video_sub_list')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_practice_on_video_sub_list') 
            
    def verify_chapter_in_test_screen(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.test_page_id, 5)
            #check1 = CommonMethods.findText(browser, VideoPage.chapter_name)
            # check2 = CommonMethods.findText(browser, 'Objective Tests ')
            # check3 = CommonMethods.findText(browser, 'Subjective Tests ')
            # check = check1 and check2 and check3
            chapter_name = VideoPage.chapter_name
            check = CommonMethods.getTextOfElement(browser, self.test_page_chapter_name) == chapter_name
            self.verify_true_or_false(browser, check, 'verify_chapter_in_test_screen', 'Test Screen elements')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_chapter_in_test_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_chapter_in_test_screen')   
            
            
    def navigate_to_test_screen(self, browser):
        try:
            VideoPage.chapter_name = CommonMethods.getTextOfElement(browser, self.video_chapter_title_library_screen)
            test_btn = (By.XPATH,"//android.widget.TextView[@text = \'"+VideoPage.chapter_name+"\']//ancestor::android.widget.LinearLayout[@resource-id ='com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.Button[@text = 'Test']")
            CommonMethods.elementClick(browser, test_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_test_screen')
        
        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_test_screen') 
    
    def tap_on_practice_card2(self, browser, chapter):
        try:
            CommonMethods.scrollToElement(browser, chapter)
            VideoPage.chapter_name = chapter
            practice_btn = (By.XPATH,"//android.widget.TextView[@text = \'"+chapter+"\']//ancestor::android.widget.LinearLayout[@resource-id ='com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.Button[@text = 'Practice']")
            CommonMethods.elementClick(browser, practice_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_practice_card')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_practice_card')         
            
    def verify_redirect_to_chapter_screen(self, browser):
        try:
            chapter_name = VideoPage.chapter_name
            CommonMethods.scrollToElement(browser, chapter_name)
            check = CommonMethods.findText(browser, chapter_name)
            self.verify_true_or_false(browser, check, 'verify_redirect_to_chapter_screen', VideoPage.chapter_name)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_redirect_to_chapter_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_redirect_to_chapter_screen')     
                  
    def verifyTextPresent(self,browser,text):
        try:
            sleep(3)
            check = CommonMethods.findText(browser,text)
            self.verify_true_or_false(browser, check, 'verifyTextPresent', text)  
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyTextPresent')        
        except :
            CommonMethods.exception(browser,featureFileName,'verifyTextPresent')   
            
            
    def verify_practice_btn(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.practice_start_practice_btn)
            self.verify_true_or_false(browser, check, 'verify_practice_btn', 'Practice Btn')  
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_practice_btn')        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_practice_btn')  
            
            
    def verify_user_is_in_chapter_screen(self, browser):
        try:
            check = CommonMethods.scrollToElement(browser, 'Chapters')
            self.verify_true_or_false(browser, check, 'verify_user_is_in_chapter_screen', 'Chapters screen')  
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_user_is_in_chapter_screen')        
        except :
            CommonMethods.exception(browser,featureFileName,'verify_user_is_in_chapter_screen')     
            
            
    def scroll_video_list_up_and_down(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                first_lnk_title = CommonMethods.getTextOfElement(browser, self.video_1st_list_lnk_text)
                self.click_on_2nd_video_lnk(browser)
                check = CommonMethods.scrollToElement(browser, 'Practice')
                self.verify_true_or_false(browser, check, 'scroll_video_list_up_and_down', 'Scroll down')
                sleep(5)
                for i in range(10):
                    x1,y1,x2,y2 = self.get_element_coordinates(browser, self.video_list_seperater_line)
                    CommonMethods.run('adb shell input touchscreen swipe {} {} {} {}'.format(x1, y1, x2, 1000))
                    check = CommonMethods.getTextOfElement(browser, self.video_1st_list_lnk_text) == first_lnk_title
                    if check == True:
                        self.verify_true_or_false(browser, check, 'scroll_video_list_up_and_down', 'Scroll up') 
                        break
            elif device == 'tab':
                check1 = CommonMethods.scrollToElement(browser, 'Practice')
                first_video = CommonMethods.getTextOfElement(browser, self.video_tab_video_lst_1st_video_title)
                check2 = CommonMethods.scrollToElement(browser, first_video)
                check = check1 and check2
                self.verify_true_or_false(browser, check, 'scroll_video_list_up_and_down', 'Scroll up and down')   
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'scroll_video_list_up_and_down')        
        except :
            CommonMethods.exception(browser,featureFileName,'scroll_video_list_up_and_down')  
               
    def delete_all_bookmark(self,browser):
        try:
            check=CommonMethods.wait_for_element_visible(browser, self.bookmark_icon, 10)
            if check == False:
                logging.info("No Bookmarks items are present ")
                CommonMethods.click_on_device_back_btn(browser)
            else:
                while  check==True:
                    CommonMethods.elementClick(browser, self.bookmark_icon)
                    check=CommonMethods.isElementPresent(browser, self.bookmark_icon)
                CommonMethods.click_on_device_back_btn(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept( browser, featureFileName, 'remove_bookmark')
        except:
            CommonMethods.noSuchEleExcept( browser, featureFileName, 'remove_bookmark') 
            
    def tap_on_bookmark_menu(self,browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.back_button_id, 3):
                CommonMethods.elementClick(browser, self.back_button_id)
                CommonMethods.wait_for_element_visible(browser, self.ham_bookmark, 3)
                CommonMethods.elementClick(browser, self.ham_bookmark)
            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_bookmark_menu')  
               
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_bookmark_menu')   
            
    def tap_on_bookmark_icon(self,browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.video_bookmark_icon_id, 5):
                CommonMethods.elementClick(browser, self.video_bookmark_icon_id)
            else:
                logging.info('Bookmark icon Not Found')
                pytest.fail("Failed due to Bookmark icon")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_bookmark_icon')  
               
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_bookmark_icon')   
            
            
    def verify_user_is_able_to_bookmark(self,browser):
        try:
            status = CommonMethods.getAttributeOfElement(browser, 'clickable', self.video_bookmark_icon_id).capitalize()
            check = bool(status)
            self.verify_true_or_false(browser, check, 'verify_user_is_able_to_bookmark', 'Bookmark icon')
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_bookmark_icon')      
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_bookmark_icon')
            
    def verify_toast_msg(self, browser, text):
        try:
            check=CommonMethods.isElementPresent( browser, self.toast_msg)
            if check == True:    
                act_txt=CommonMethods.getTextOfElement(browser,self.toast_msg)
                exp_txt= text
                assert act_txt == exp_txt ,"toast  text  failed "
            else:
                logging.info("toast text verification failed ")
                pytest.fail("toast text verification failed ")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_toast_msg')  
               
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_toast_msg')  
            
    def verify_video_progress_100_percent(self, browser):
        try:
            check=CommonMethods.isElementPresent( browser, self.toast_msg)
            
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_progress_100_percent')    
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_progress_100_percent')    
    
    def rgb2hex(self, rgb):
        return '#%02x%02x%02x' % rgb        
            
    def get_the_rgb_lst(self, browser, locator):
        try:
            s1 = set()
            CommonMethods.wait_for_element_visible(browser, locator, 10)
            element1 = CommonMethods.getElement(browser, locator)
            location = element1.location
            size = element1.size
            png = browser.get_screenshot_as_png()
            img = Image.open(BytesIO(png))
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height'] 
            im = img.crop((left, top, right, bottom))
            pix_val1 = list(dict.fromkeys(list(im.getdata())))
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
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'get_the_rgb_lst')  
               
        except:
            CommonMethods.exception(browser, featureFileName, 'get_the_rgb_lst') 
            
    def verify_subject_chapter_color(self, first, secound, count):
        result = first & secound
        len2 = len(result)
        if len(result) >= count:
            logging.info("both have same color")
        else:
            logging.info("both color not matching")
        
            
    def verify_chapter_subject_theme_color(self, browser):
        subject_rgb = VideoPage.subject_rgb_lst
        chapter_rgb = self.get_the_rgb_lst(browser, self.video_chapter_name_id)
        self.verify_subject_chapter_color(subject_rgb, chapter_rgb, 40)
        
        
    def verify_the_bookmark_icon_color_with_subject(self, browser):
        subject_rgb = VideoPage.subject_rgb_lst
        book_mark_icon = self.get_the_rgb_lst(browser, self.video_bookmark_icon_id)
        self.verify_subject_chapter_color(subject_rgb, book_mark_icon, 5)
        
        
    def enble_toggle_btn(self, browser):
        status = CommonMethods.getAttributeOfElement(browser, 'checked', self.video_auto_enable_switch)
        if CommonMethods.wait_for_element_visible(browser, self.video_auto_enable_switch, 3):
            if status == 'true':
                VideoPage.auto_play_switch_color = self.get_the_rgb_lst(browser, self.video_auto_enable_switch)
                logging.info('Autoplay is enable')
                CommonMethods.click_on_device_back_btn(browser)   
            elif status == 'false':
                CommonMethods.elementClick(browser, self.video_auto_enable_switch)
                VideoPage.auto_play_switch_color = self.get_the_rgb_lst(browser, self.video_auto_enable_switch)
                CommonMethods.click_on_device_back_btn(browser)   
        else:
            logging.info('Error in getting Auto play option screen')
            
    def verify_video_icon_after_completion(self, browser):
        try:
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                check1 = CommonMethods.isElementPresent( browser, self.video_auto_play_btn)
                check2 =  CommonMethods.isElementPresent(browser, self.video_player_back_btn)
                check3 = CommonMethods.isElementPresent(browser, self.video_up_next)
                check4 = CommonMethods.isElementPresent(browser, self.video_next_video_title)
                check5 = CommonMethods.isElementPresent(browser, self.video_next_video_chapter_name)
                check6 = CommonMethods.isElementPresent(browser, self.video_auto_cancelBtn_id)
                self.verify_true_or_false(browser, check1, 'verify_video_icon_after_completion', "auto load icon")
                self.verify_true_or_false(browser, check2, 'verify_video_icon_after_completion', "Player Back Button")
                self.verify_true_or_false(browser, check3, 'verify_video_icon_after_completion', "Up next Text")
                self.verify_true_or_false(browser, check4, 'verify_video_icon_after_completion', "next video Title")
                self.verify_true_or_false(browser, check5, 'verify_video_icon_after_completion', "next video chapter name")
                self.verify_true_or_false(browser, check6, 'verify_video_icon_after_completion', "Cancel Button")
            elif device == 'tab':
                check1 = CommonMethods.isElementPresent( browser, self.video_auto_play_btn)
                check2 =  CommonMethods.isElementPresent(browser, self.video_tab_player_back_btn)
                check3 = CommonMethods.isElementPresent(browser, self.video_up_next)
                check4 = CommonMethods.isElementPresent(browser, self.tab_video_next_video_title)
                check5 = CommonMethods.isElementPresent(browser, self.video_tab_next_video_chapter_name)
                check6 = CommonMethods.isElementPresent(browser, self.video_tab_auto_cancel_btn)
                self.verify_true_or_false(browser, check1, 'verify_video_icon_after_completion', "auto load icon")
                self.verify_true_or_false(browser, check2, 'verify_video_icon_after_completion', "Player Back Button")
                self.verify_true_or_false(browser, check3, 'verify_video_icon_after_completion', "Up next Text")
                self.verify_true_or_false(browser, check4, 'verify_video_icon_after_completion', "next video Title")
                self.verify_true_or_false(browser, check5, 'verify_video_icon_after_completion', "next video chapter name")
                self.verify_true_or_false(browser, check6, 'verify_video_icon_after_completion', "Cancel Button")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_icon_after_completion')  
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_icon_after_completion')
    
            
    def next_video_should_play(self, browser):
        try:
            check1 = CommonMethods.wait_for_element_visible(browser, self.video_auto_play_btn, 5)
            VideoPage.next_video_title = CommonMethods.getTextOfElement(browser, self.video_next_video_title)
            sleep(10)
            expected_video_title = CommonMethods.getTextOfElement(browser, self.video_title_in_list_id)
            check = CommonMethods.verifyTwoText(VideoPage.next_video_title, expected_video_title)
            self.verify_true_or_false(browser, check1, 'next_video_should_play', "auto play btn")
            self.verify_true_or_false(browser, check, 'next_video_should_play', 'Video Title')
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'next_video_should_play')   
        except:
            CommonMethods.exception(browser, featureFileName, 'next_video_should_play')
        
    
    def tap_on_any_video(self, browser):
        try:
            sleep(3)
            device = CommonMethods.get_device_type(browser)
            if device == 'mobile':
                ele = CommonMethods.getElements(browser, self.video_play_list_elements)
                ele_length = len(ele)
                n = random.randint(1,ele_length-1)
                ele[n].click()              
            elif device == 'tab':
                ele = CommonMethods.getElements(browser, self.tab_videos_list_elements)
                ele_length = len(ele)
                n = random.randint(1,ele_length-1)
                ele[n].click()    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_any_video')   
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_any_video')
            
            
    def verify_video_icons_should_disapper(self, browser):
        try:
            check1 = CommonMethods.wait_for_element_visible(browser, self.ten_sec_bkwd_btn_id, 2)
            check2 = CommonMethods.wait_for_element_visible(browser, self.ten_sec_fwd_btn_id, 2)
            check3 = CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 2)
            check = not check1 or check2 or check3
            self.verify_true_or_false(browser, check, 'verify_video_icons_should_disapper', "all video icons")     
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_icons_should_disapper')      
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_icons_should_disapper')
            
            
    def verify_video_icons_should_apper(self, browser):
        try:
            check1 = CommonMethods.wait_for_element_visible(browser, self.ten_sec_bkwd_btn_id, 2)
            check2 = CommonMethods.wait_for_element_visible(browser, self.ten_sec_fwd_btn_id, 2)
            check3 = CommonMethods.wait_for_element_visible(browser, self.video_play_btn, 2)
            check = check1 and check2 and check3
            self.verify_true_or_false(browser, check, 'verify_video_icons_should_disapper', "all video icons")     
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_video_icons_should_apper')      
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_video_icons_should_apper')
    
            
