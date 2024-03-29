#!/usr/bin/python3

"""this script- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""

from requests.auth import HTTPBasicAuth
import sys
import requests

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
