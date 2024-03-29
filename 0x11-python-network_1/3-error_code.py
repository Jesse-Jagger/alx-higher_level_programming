#!/usr/bin/python3

"""this requests to the URL and output the body of the response in utf-8"""

import urllib.request
from sys import argv
import urllib.error


if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as re:
            content = re.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as er:
        print("Error code:", er.code)

