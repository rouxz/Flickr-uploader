from static import *
from credentials import *

def main():
    print(LINE)
    print(NAME)
    print(LINE)

    #Signature test
    print(signature({"babar": "osu", "amour": 1}))


if __name__ == "__main__":
    main()
