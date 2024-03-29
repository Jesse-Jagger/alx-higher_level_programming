#!/usr/bin/python3

"""this script fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    cont = resp.read()

print("Body response:")
print("\t- type: {}".format(type(cont)))
print("\t- content: {}".format(cont))
print("\t- utf8 content: {}".format(cont.decode('utf-8')))
