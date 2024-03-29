#!/usr/bin/python3

"""this sends a POST request to the passed URL with the email"""
import urllib.request
from sys import argv
import urllib.parse

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as re:
        con = re.read().decode('utf-8')
        print(con)
