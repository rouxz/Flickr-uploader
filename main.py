from static import *
import credentials
import logging
import server
import json

def main():
    print(LINE)
    print(NAME)
    print(LINE)

    #set up the logging
    logging.basicConfig(filename='log.log', level=logging.DEBUG)
    logging.info(NAME + " started   ")




    credential = credentials.Credentials()

if __name__ == "__main__":
    # main()
    # f = open(VERIFIER_JSON, 'wb')
    with open(VERIFIER_JSON, 'wb') as f:
        json.dumps({'a':'a'}, f, indent=4)
