'''
This module contains the path for the supporting files
'''
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

CONFIG_PATH = PATH('../config/config.json')
Login_Credentials = PATH('../config/login_data.json')
Hamburger_Options = PATH('../config/application_data.json')
Registration_data = PATH('../Test_data/Registration_data.json')
