#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
using the package 'requests'
"""

import sys
import requests

if __name__ == "__main__":

    endpoint_url = "https://api.github.com/users"

    # get username & password from arguments
    username = sys.argv[1]
    pwd = sys.argv[2]

    # append username to endpoint_url
    endpoint_url = f"{endpoint_url}/{username}"

    # set authorization header
    header = {"Authorization": f"Bearer {pwd}"}

    # call Github API
    response = requests.get(endpoint_url, headers=header)

    # print only user id
    print(response.json().get("id"))
