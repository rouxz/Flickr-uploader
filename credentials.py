import requests
import json
import os
import hashlib

""" get credentials from flickr"""

"""Calculate the signature for flickr from a dictionnary of all parameters"""
""" return it as a hexadecimal value"""
def signature(dict):

    concat = ""
    for key, value in sorted(dict.items()): # Note the () after items!
        concat = concat + key + str(value)

    #Calculate the md5 hash
    sig = hashlib.md5(bytes(concat, 'utf-8')).hexdigest()
    return sig


def getRequestToken():
    param_dict = {"oauth_nonce":95613465, \
        "oauth_timestamp": 1305586162, \
        "oauth_consumer_key": "653e7a6ecc1d528c516cc8f92cf98611" , \
        "oauth_signature_method":"HMAC-SHA1",
        "oauth_version":"1.0",\
        "oauth_signature":7w18YS2bONDPL%2FzgyzP5XTr5af4%3D,\
        "oauth_callback":"http%3A%2F%2Fwww.example.com}",\
    }
