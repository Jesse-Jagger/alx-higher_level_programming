#!/usr/bin/python3

"""this outputs the value of the X-Request-Id variable in the header"""

from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
