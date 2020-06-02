''' it will load the json file '''

import json
import os
import sys


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

def getdata(filename,var,key):
    with open(filename) as f:
      
        return json.load(f)[var][key]
    
    