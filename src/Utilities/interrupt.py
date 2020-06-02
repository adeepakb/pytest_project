'''
This module contains methods which can be used for mobile interruption
'''

from subprocess import call

from appium.webdriver.connectiontype import ConnectionType


def get_network_connection(driver):
    return driver.network_connection


def set_connection_type(driver, conntype):
    if(conntype.upper() in 'WIFI_ONLY'):
        driver.set_network_connection(ConnectionType.WIFI_ONLY)
    elif(conntype.upper() in 'DATA_ONLY'):
        driver.set_network_connection(ConnectionType.DATA_ONLY)
    elif(conntype.upper() in 'AIRPLANE_MODE'):
        driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
    elif(conntype.upper() in 'ALL_NETWORK_ON'):
        driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
    elif(conntype.upper() in 'OFFLINE'):
        driver.set_network_connection(ConnectionType.NO_CONNECTION)


def click_on_home_button(driver):
    driver.press_keycode(3)

    
def click_on_back_button(driver):
    driver.press_keycode(4)

    
def click_on_menu_button(driver):
    driver.press_keycode(82)

    
def restart_device():
    # only for windows with android
    call(['cmd.exe', '/c', 'adb reboot'])


def shutdown_device():
    # only for windows with android
    call(['cmd.exe', '/c', 'adb shell reboot -p'])

