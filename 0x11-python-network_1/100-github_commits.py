#!/usr/bin/python3

"""lists the 10 most recent commits on a provided GitHub repository"""
from sys import argv
import requests


if __name__ == "__main__":
    repository_name = argv[1]
    owner_name = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner_name, repository_name)
    pars = {"per_page": 10}

    commits = r.json()
    r = requests.get(url, pars=pars)

    for commit in commits:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))
