import logging
import requests
import json
import os
import hashlib
import apikey
from static import *
import hmac
import random
import time
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session


""" get credentials from flickr"""

"""Calculate the signature for flickr from a dictionnary of all parameters"""
""" return it as a hexadecimal value"""
""" param_dict is a dictionnary of all parameters
    url is the type of url that will be called
    token is the token_secret by default is empty
    http_verb is the verb of the query , default is GET"""

def signature(url, param_dict, token_secret = "",  http_verb = "GET", debug = True):
    """ calculate the signature based on HMAC-SHA1 """
    key = bytes(apikey.SECRET + "&" + token_secret, 'utf-8')
    txt = http_verb + "&" + url
    for k, v in sorted(param_dict.items()):
        txt = txt + "&" +  k + "=" + str(v)
    print(bytes(txt, 'utf-8'))
    #Calculate the md5 hash
    sig = hmac.new(key, msg = bytes(txt, 'utf-8'), digestmod = 'SHA1').hexdigest()
    print(sig)
    return sig


def getRequestToken(debug=True):
    #prefills all the parameters for getting the request token
    oauth = OAuth1(apikey.KEY, client_secret=apikey.SECRET, signature_type = 'query',  callback_uri='http://example.com')
    r = requests.get(url=OAUTH_ENDPOINT + OAUTH_REQUEST_TOKEN_SERVICE, auth=oauth)

    # #send request to server
    if (debug):
        logging.debug("Firing request token query")
    if (debug):
        logging.debug("Request token status:" + str(r.status_code))
        print("Request token status:" + str(r.status_code))

    if (r.status_code == requests.codes.OK):
        print("OK")
