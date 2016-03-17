from static import *
import credentials
import logging

def main():
    print(LINE)
    print(NAME)
    print(LINE)

    #set up the logging
    logging.basicConfig(filename='log.log', level=logging.DEBUG)
    logging.info(NAME + " started   ")

    #Signature test
    print("Request token for connection")
    credentials.getRequestToken()


if __name__ == "__main__":
    main()
