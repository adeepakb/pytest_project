""" it will load the json file """
import json
import os

from cryptography.fernet import Fernet


def get_data(filename, var, key=None):

    if key is not None:
        with open(filename) as f:
            if "config" in filename:
                key = os.getenv('SECRET')
                f = Fernet(key)
                encrypted_data = json.load(f)["encrypted_data"]["token"] #getdata('../config/config.json', 'encrypted_data', 'token')
                decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))
                return decrypted_data[var][key]
            else:
                return json.load(f)[var][key]
    else:
        with open(filename) as f:
            return json.load(f)[var]


