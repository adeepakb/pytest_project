""" it will load the json file """
import json


def get_data(filename, var, key=None):
    if key is not None:
        with open(filename) as f:
            return json.load(f)[var][key]
    else:
        with open(filename) as f:
            return json.load(f)[var]


