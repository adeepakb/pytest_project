import sys
import os
import time
#import numpy as np 
import re
from PIL import Image
import pytesseract
import glob
import logging
import pytest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

def delete_all_previous_screenshots():
    f_files = glob.glob('../../ScreenShots/*.png')
    for f in f_files:
        os.remove(f)

def screenshot(browser):
    delete_all_previous_screenshots()
    ts = time.strftime("%Y_%m_%d_%H%M%S")
    activityname = browser.current_activity
    #logging.info(activityname)
    filename = activityname+"_" + ts + ".png"
    ScrnShotpath="../../ScreenShots/"+ filename
    browser.save_screenshot(ScrnShotpath)
    return ScrnShotpath

'''
We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
'''

# we need to install Tesseract first in the system 

def get_text_from_image(browser,imagefilepath,rtext):
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract"
    open_image = Image.open(imagefilepath)
    img_to_text = pytesseract.image_to_string(open_image)
    to_find_text = re.compile(rtext)
#     print(img_to_text)
    search_text = to_find_text.search(img_to_text)
    if search_text:
        found_text= search_text.group()
        print(found_text)
        return found_text
    else:
        logging.info("text is not matched")
        pytest.fail("failed in get_text_from_image method")
