import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from utilities.staging_tllms import Stagingtllms
from pages.android.session_data import SessionData
from pages.android.login_android import LoginAndroid
from pages.android.scroll_cards import ScrollCards
from utilities.tutor_common_methods import TutorCommonMethods


class AutomaticAssetDownload:
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.action = TouchAction(driver)
        self.login = LoginAndroid(driver)
        self.driver = driver
        self.session_data = SessionData(driver)
        self.scroll_cards = ScrollCards(driver)
        self.my_profile_icon = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/imageViewUserProfile"]'
        self.auto_download_toggle = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/autoDownloadToggleImage"]'
        self.card = '//*[@resource-id ="com.byjus.thelearningapp.premium:id/cvScheduleCard"]'
        self.download_icon = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/pbManualDownload]'
        self.custom_panel = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/customPanel"]'
        self.custom_panel_download = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/download_button"]'
        self.custom_panel_cancel = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/tvCancelDownload"]'

    def verify_profile_screen(self):
        self.obj.wait_for_locator('xpath', self.my_profile_icon)
        self.obj.is_element_present('xpath', self.my_profile_icon)
        self.scroll()

    def is_auto_download_toggle_present(self):
        return self.obj.get_element('xpath', self.auto_download_toggle).is_displayed()

    def is_auto_download_toggle_enabled(self):
        return self.obj.get_element('xpath', self.auto_download_toggle).is_selected()

    def click_on_auto_download_toggle(self):
        self.obj.get_element('xpath', self.auto_download_toggle).click()

    def click_back(self):
        self.obj.click_back()

    def scroll(self):
        size = self.driver.get_window_size()
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.2)
        start_x = int(size['width'] / 2)
        self.action.press(x=start_x, y=start_y).wait(1000).move_to(x=start_x, y=end_y).release().perform()

    def verify_download_icons_present(self):
        count = 0
        i = 0
        upnext_card_found = False
        session_cards_list = self.obj.get_elements('xpath', self.card)
        while i < 5:
            if self.session_data.get_session_status(session_cards_list[i]) == 'UP NEXT':
                upnext_card_found = True
            if upnext_card_found:
                flag = self.is_download_icon_displayed_for_card(session_cards_list[i])
                assert flag, "Download icons not present for 16 upcoming sessions.only " + str(
                    count) + "download icons present"
                count += 1
                print("Number of download icons ", count)
            if count == 16:
                break
            i += 1
            if i == 5:
                self.scroll_cards.scroll_by_card(session_cards_list[4], session_cards_list[0])
                i = 1
                session_cards_list = self.obj.get_elements('xpath', self.card)

    def verify_session_present_today(self, driver):
        flag = Stagingtlms(driver).is_session_present_today()
        if flag is True:
            pass
        else:
            pytest.skip("No session today for this user")

    def is_download_icon_displayed_for_card(self, card):
        try:
            card.find_element_by_xpath('//*[@resource-id = "com.byjus.thelearningapp.premium:id/pbManualDownload"]')
            return True
        except NoSuchElementException:
            return False

    def click_on_download_icon_for_card(self, card):
        card.find_element_by_xpath('//*[@resource-id = "com.byjus.thelearningapp.premium:id/pbManualDownload"]').click()

    def is_asset_downloaded(self, card):
        try:
            element = card.find_element_by_xpath(
                '//*[@resource-id = "com.byjus.thelearningapp.premium:id/tvManualDownloadStatus"]')
            download_status = element.text
            if download_status == 'Downloaded':
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def scroll_and_iterate_till(self, desired_status):
        i = 0
        session_cards_list = self.obj.get_elements('xpath', self.card)
        while i < 4:
            status = self.session_data.check_for_up_next(session_cards_list[i])
            if callable(desired_status):
                match = desired_status(status)
            else:
                match = status == desired_status

            if match:
                yield session_cards_list[i]
            i += 1
            if i == 4:
                self.scroll_cards.scroll_by_card(session_cards_list[4], session_cards_list[0])
                i = 0
                session_cards_list = self.obj.get_elements('xpath', self.card)

    def click_on_up_next_card(self):
        for card in self.scroll_and_iterate_till("UP NEXT"):
            card.click()
            break

    def verify_download_icon_present_for_up_next_card(self):
        for card in self.scroll_and_iterate_till("UP NEXT"):
            flag = self.is_download_icon_displayed_for_card(card)
            assert flag, "Download icon is not present for the up next card"
            break

    def wait_for_download_to_be_completed(self):
        try:
            # for card in self.scroll_and_iterate_till("UP NEXT"):
            #     element = card.find_element_by_xpath("//android.widget.TextView[@text='Downloaded']")
            #     WebDriverWait(self.driver, 15).until(ec.visibility_of(element))
            self.login.wait_for_locator('class_name', 'android.widget.Toast', 15)
        except (StaleElementReferenceException, NoSuchElementException):
            pass

    def verify_asset_auto_downloaded_for_up_next_card(self):
        flag = False
        for card in self.scroll_and_iterate_till("UP NEXT"):
            flag = self.is_asset_downloaded(card)
            break
        return flag

    def click_on_download_icon_for_up_next_card(self):
        for card in self.scroll_and_iterate_till("UP NEXT"):
            self.click_on_download_icon_for_card(card)
            break

    def verify_download_materials_popup_for_session(self):
        assert self.obj.is_element_present('xpath', self.custom_panel), "Prepare for your session popup is not present"
        assert self.obj.is_element_present('xpath',
                                           self.custom_panel_download), "Download button is not present in the prepare for your session popup"
        assert self.obj.is_element_present('xpath',
                                           self.custom_panel_cancel), "Cancel button is not present in the prepare for your session popup"

    def is_download_materials_popup_dismissed(self):
        self.login.wait_for_element_not_to_be_present(self.custom_panel, 20)

    def clear_app_from_recents_and_relaunch(self):
        self.obj.clear_app_from_recents()
        self.obj.execute_command(
            'adb shell monkey -p com.byjus.thelearningapp.premium -c android.intent.category.LAUNCHER 1')

    def relaunch_app(self):
        self.obj.execute_command(
            'adb shell monkey -p com.byjus.thelearningapp.premium -c android.intent.category.LAUNCHER 1')

    def delete_downloaded_asset(self):
        self.obj.execute_command(
            'adb shell rm -r /storage/emulated/0/Android/data/com.byjus.thelearningapp.premium/files')

    def tap_on_cancel(self):
        self.obj.get_element('xpath', self.custom_panel_cancel).click()

    def verify_download_icon_is_not_present_for_up_next_card(self):
        for card in self.scroll_and_iterate_till("UP NEXT"):
            flag = self.is_download_icon_displayed_for_card(card)
            assert (not flag), "Download icon is present for the up next card for which teaching material is not added"
            break

    def is_android_notification_present(self, expected_notification):
        flag = False
        self.driver.open_notifications()
        notification_titles = self.obj.get_elements('id', 'android:id/title')
        for title in notification_titles:
            title_text = title.text
            print(title_text)
            if title_text == expected_notification:
                flag = True
        return flag

    def is_assets_in_jpg_format(self):
        folders = self.obj.execute_command(
            'adb shell ls /storage/emulated/0/Android/data/com.byjus.thelearningapp.premium/files')[0]
        for folder in folders.split(b'\n'):
            try:
                session_id = int(folder)
            except ValueError:
                continue
            files = self.obj.execute_command(
                'adb shell find /storage/emulated/0/Android/data/com.byjus.thelearningapp.premium/files/%s' % session_id)[
                0]
            for file in files.split(b'\n')[1:-1]:  # remove folder and last empty entry
                assert file.endswith(b'.jpg'), "Downloaded material is not in jpg format"

    def login_to_asset_not_tagged_account(self, driver):
        self.obj.execute_command('adb shell pm clear com.byjus.thelearningapp.premium')
        self.obj.execute_command(
            'adb shell monkey -p com.byjus.thelearningapp.premium -c android.intent.category.LAUNCHER 1')
        self.login.allow_deny_permission(["Allow", "Allow", "Allow"])
        self.login.enter_cc_and_phone_number('asset_not_tagged_account_details')
        self.login.click_on_next()
        otp = Stagingtlms(driver).get_otp("asset_not_tagged_account_details")
        self.login.enter_otp(otp)
