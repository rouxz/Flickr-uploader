import logging
import requests
import json
import apikey
from static import *
from requests_oauthlib import OAuth1
import urllib
import webbrowser
import server
import threading

""" get credentials from flickr"""
class Credentials:

    def __init__(self, debug=True):
        self.debug = debug
        #get query token
        if (self.debug):
            print("Request token for connection")
        self.access_token = self.getRequestToken()

        #create a thread launching a webserver to wait for the callback verifier
        thread_server = threading.Thread(target=server.setServer)
        thread_server.deamon = True
        thread_server.start()

        #get access token
        if (self.debug):
            print("Request access token ")
        self.authorization = self.getAuthorisationToken()

        #verifier is empty
        self.verifier = ""



    """ get provitional token before authentication """
    def getRequestToken(self):
        #prefills all the parameters for getting the request token
        oauth = OAuth1(apikey.KEY, client_secret=apikey.SECRET, signature_type = 'query',  callback_uri='http://127.0.0.1:8000')


        # #send request to server
        if (self.debug):
            logging.debug("Firing request token query")
        r = requests.get(url=OAUTH_ENDPOINT + OAUTH_REQUEST_TOKEN_SERVICE, auth=oauth)

        #get status of the request
        if (self.debug):
            logging.debug("Request token status:" + str(r.status_code))

        #parse the information received if everything is alright
        if (r.status_code == requests.codes.OK):
            credentials = urllib.parse.parse_qs(r.content)
            self.resource_owner_key = credentials[bytes('oauth_token','utf-8')][0]
            self.resource_owner_secret = credentials[bytes('oauth_token_secret','utf-8')][0]

            logging.info("Request token obtained")


    """ get the user authorization """
    """ it requires input from request token """
    def getAuthorisationToken(self):
        # #send authorization to server
        if (self.debug):
            logging.debug("Opening browser for allowing the app")

        # r = requests.get(url=OAUTH_ENDPOINT + OAUTH_USER_AUTHORISATION_SERVICE, params=params)
        webbrowser.open(OAUTH_ENDPOINT + OAUTH_USER_AUTHORISATION_SERVICE + "/?oauth_token=" + self.resource_owner_key.decode("utf-8"))


    """ get the access token and store it """

    def getAccessToken(self):
        pass
