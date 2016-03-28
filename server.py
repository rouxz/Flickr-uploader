import os
import time
import sys
import logging
from http.server import BaseHTTPRequestHandler as Handler
from http.server import HTTPServer as Server
import urllib
import threading
import json
from static import *

class CustomizedHandler(Handler):

    def send_ok(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def do_GET(self):
        try:
            logging.info("Request arrived %s" % self.path)
            self.send_ok()
            self.wfile.write(bytes("Confirmation OK",'utf-8'))
            http_query = urllib.parse.parse_qs(self.path)
            print(str(http_query))
            #write the information from the query to a specific JSON file
            if http_query['oauth_verifier'][0] != "":
                print(http_query['oauth_verifier'][0])
                query = {'oauth_verifier' : http_query['oauth_verifier'][0]}
                f = open(VERIFIER_JSON, 'w')
                json.dumps(query, f, indent=4)
                # f.write(http_query['oauth_verifier'][0])
            return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)



""" create a server for getting all the callbacks """
def setServer(debug=True):

    # Change current directory to avoid exposure of control files
    os.chdir('.')

    try:

        server = Server(('127.0.0.1', 8000), CustomizedHandler)
        logging.info('started httpserver...')
        server.serve_forever()
    except KeyboardInterrupt:
    	logging.info('^C received, shutting down server')
    	server.socket.close()
    #close server anyhow
    server.server_close()
    logging.info("Server shut down")
