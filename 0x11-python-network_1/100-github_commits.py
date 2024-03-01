#!/usr/bin/python3
"""
This script list 10 commits (from the most recent to oldest)
of a given repository of a user
using Github API and the package 'requests'
"""

import sys
import requests

if __name__ == "__main__":

    # get target user and repository from arguments
    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]

    # append username to endpoint_url
    endpoint_url = (
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    )

    # define our query parameter
    params = {"per_page": 10}

    # call Github API to get last 10 commits
    commits = requests.get(endpoint_url, params=params).json()

    # print retreived commits from our API call
    for commit in commits:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author}")
