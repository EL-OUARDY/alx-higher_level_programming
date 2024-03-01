#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header, using the package 'requests'
"""

import sys
import requests

if __name__ == "__main__":

    # get url entered by the user
    url = sys.argv[1]
    headers = requests.get(url).headers
    print(headers.get("X-Request-Id"))
