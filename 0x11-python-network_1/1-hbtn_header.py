#!/usr/bin/python3
"""
This script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response, using urllib package
"""

import sys
import urllib.request

if __name__ == "__main__":

    # get URL from passed user arguments
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print(dict(headers).get("X-Request-Id"))
