#!/usr/bin/python3

"""this displays the value of the variable X-Request-Id in the response header"""

from sys import argv
import requests


if __name__ == "__main__":
    request = requests.get(argv[1])

    print(request.headers.get('X-Request-Id'))
