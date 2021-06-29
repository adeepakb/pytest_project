from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.ps_home_screen import PSHomescreenFactory
from pages.factory.classnotes import ClassNotesFactory
import pytest_check as check

scenarios('../features/Classnotes in PDF.feature')


@fixture()
def login_in(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in


@fixture()
def home_screen(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        home_screen = PSHomescreenFactory().get_page(driver, Platform.ANDROID.value)
        yield home_screen
    elif Platform.WEB.name in platform_list:
        home_screen = PSHomescreenFactory().get_page(driver, Platform.WEB.value)
        yield home_screen


@fixture()
def classnotes(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        classnotes = ClassNotesFactory().get_page(driver, Platform.ANDROID.value)
        yield classnotes
    elif Platform.WEB.name in platform_list:
        classnotes = ClassNotesFactory().get_page(driver, Platform.WEB.value)
        yield classnotes


@given("launch the application and navigate to home screen")
def navigate_to_one_to_many_and_mega_user(login_in):
    login_in.navigate_to_one_to_many_and_mega_user()


@when("tap on byjus classes card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@when("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(login_in):
    login_in.select_premium_school()


@then('tap on device back icon')
def tap_back_icon_and_verify(home_screen):
    home_screen.click_back()


@then(parsers.parse('verify that "{text}" shown in the postrequisites card'))
@then(parsers.parse('verify that user navigates to "{text}" screen'))
@then(parsers.parse('Verify the text "{text}"'))
def verify_text(login_in, text):
    check.equal(login_in.text_match(text).result, True, login_in.text_match(text).reason)


@then('tap on "Get help" button')
def tap_on_get_help(home_screen):
    home_screen.tap_on_get_help()


@then('Verify that quick help bottom sheet opens')
def verify_bottom_sheet(home_screen):
    check.equal(home_screen.is_bottom_sheet_present().result, True, home_screen.is_bottom_sheet_present().reason)


@then(parsers.parse('verify that user is able to switch between "{text1}" and "{text2}" tabs'))
def select_tab(home_screen, text1, text2):
    home_screen.tap_on_tab(text1)
    check.equal(home_screen.is_tab_selected(text1).result, True, home_screen.is_tab_selected(text1).reason)
    home_screen.tap_on_tab(text2)
    check.equal(home_screen.is_tab_selected(text2).result, True, home_screen.is_tab_selected(text2).reason)


@then(parsers.parse('tap on "{text}" tab'))
def select_tab(home_screen, text):
    home_screen.tap_on_tab(text)


@then('Verify that For you tab contents are loading')
def verify_session_card_details(home_screen):
    home_screen.verify_card_details()


@then('Verify the completed session card along with Subject Name, topic Name and the text "Completed" with date and '
      'the session rating given by the user in stars followed by the numeric')
@then('Verify that Completed sessions tab contents are loading')
def verify_completed_card_details(home_screen):
    details_dict = home_screen.verify_completed_card_details()
    check.equal(all(v is not None for v in[details_dict['Subject'], details_dict['Topic'], details_dict['Schedule Date'],details_dict['Session status']])
                and details_dict['Session status'] == "Completed"), True, "Completed Session card details not loaded"


@given(parsers.parse('post-requisite "{requisite_name}" should be tagged for the particular classroom session'))
def attach_post_requisite(home_screen, driver, requisite_name):
    home_screen.attach_post_requisite(driver, requisite_name)


@then('verify classnote icon beside class-note text is present')
def is_classnote_icon_present(classnotes):
    details = classnotes.is_classnote_icon_present()
    check.equal(details.result, True, details.reason)


@then('verify Download button is present')
def is_download_icon_present(classnotes):
    details = classnotes.is_download_icon_present()
    check.equal(details.result, True, details.reason)


@then("tap on completed session card")
def tap_on_any_session_card(classnotes):
    classnotes.tap_on_first_session_card()


@then(parsers.parse('verify "{text}" option is not displayed if the post requisite contain only 2 resource type'))
def verify_text(login_in, text):
    check.equal(login_in.text_match(text).result, False, login_in.text_match(text).reason)


@then('verify that in the Completed tab, post requisite card is present')
def is_requisite_list(classnotes):
    details = classnotes.is_requisite_list()
    check.equal(details.result, True, details.reason)


@then(parsers.parse('tap on "{text}"'))
def tap_on_premium_card(login_in, text):
    login_in.click_on_link(text)


@then('verify the user is navigated to the session details screen where all the tagged resource types are shown')
def all_tagged_resource_types(classnotes):
    details = classnotes.all_tagged_resource_types()
    check.equal(details.result, True, details.reason)


@then('Verify App back button on left hand side of the screen')
def is_back_nav_present(home_screen):
    check.equal(home_screen.is_back_nav_present().result, True, home_screen.is_back_nav_present().reason)


@then('Verify Get help button')
def is_get_help_present(home_screen):
    check.equal(home_screen.is_get_help_present().result, True, home_screen.is_get_help_present().reason)


@then(parsers.parse('Verify that "{text}" tab is highlighted by default'))
def is_tab_selected(home_screen, text):
    check.equal(home_screen.is_tab_selected(text).result, True, home_screen.is_tab_selected(text).reason)


@then('Verify the Class Notes card is present and Pdf size displayed below the down Arrow Button')
def verify_class_notes(classnotes):
    classnotes.verify_classnotes_present_to_download()


@then('tap on class notes download icon')
def click_on_download(classnotes):
    classnotes.click_on_download()


@then('Verify that PDF download in the storage of the phone')
def verify_class_notes(classnotes):
    details = classnotes.is_assets_in_pdf_format()
    check.equal(details.result, True, details.reason)


@then('verify class notes downloaded state along with forward icon')
def click_on_download(classnotes):
    details = classnotes.verify_forward_icon_present()
    check.equal(details.result, True, details.reason)


@then('verify while taping on the forward icon pdf file should open')
def tap_classnotes_forward_icon(classnotes):
    details = classnotes.tap_classnotes_forward_icon_and_verify()
    check.equal(details.result, True, details.reason)


@then(parsers.parse('switch "{text}" the device data'))
def switch_off_data(login_in, text):
    login_in.toggle_wifi_connection(text)


@then('verify that after the pdf download and user able to share')
def verify_share_file_options(classnotes):
    details = classnotes.verify_share_file_options()
    check.equal(details.result, True, details.reason)


@then('click on More options-Download option')
def click_on_pdf_download_option(classnotes):
    classnotes.click_on_pdf_download_option()


@then('verify that loader keeps loading the file')
def classnote_progressing(classnotes):
    details = classnotes.classnote_processing()
    check.equal(details.result, True, details.reason)


@given("login to tutor-plus-cms-staging")
def login_to_cms_staging(classnotes):
    classnotes.login_to_cms_staging()


@when("verify that user uploads classnotes pdf more than 15 MB size")
def update_class_note(classnotes):
    classnotes.upload_class_note_morethan_15mb()


@then("verify that an error message should be displayed")
def verify_classnote_upload_error(classnotes):
    details = classnotes.verify_classnote_upload_error()
    check.equal(details.result, True, details.reason)


@when('user try to upload class Notes in any other format (ex img or csv)')
def incorrect_note_format(classnotes):
    classnotes.upload_incorrect_format_class_note()


@then('upload was not successful')
def incorrect_note_format(classnotes):
    details = classnotes.incorrect_note_format_error()
    check.equal(details.result, True, details.reason)


@given(parsers.parse('post-requisite "{requisite_name}" classnote should be updated to "{class_note_id}" for the '
                     'particular classroom session'))
def update_post_requisite_class_note(classnotes, requisite_name, class_note_id):
    classnotes.update_post_requisite_class_note(requisite_name, class_note_id)


@then('verify that user asked to select pdf viewer to open')
def verify_pdf_viewer_options(classnotes):
    details = classnotes.verify_pdf_viewer_options()
    check.equal(details.result, True, details.reason)


@then('verify that user should get message to download pdf viewer')
def verify_no_pdf_viewer_message(classnotes):
    details = classnotes.verify_no_pdf_viewer_message()
    check.equal(details.result, True, details.reason)


@given('verify that device does not have pdf viewer')
def uninstall_pdf_reader_apps(classnotes):
    classnotes.uninstall_pdf_reader_apps()


@then('install back pdf viewer apps')
def install_pdf_reader_apps(classnotes):
    classnotes.install_pdf_reader_apps()
