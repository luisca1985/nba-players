import requests
import sys
# import json

def app(arg):
    URL = 'https://mach-eight.uc.r.appspot.com/'
    data = requests.get(URL).json()
    print(data)


if __name__ == '__main__':
    arg = sys.argv[0] if sys.argv[0] else 100
    app(arg)