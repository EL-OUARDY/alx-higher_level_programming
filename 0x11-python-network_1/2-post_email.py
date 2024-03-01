#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8), using urllib package
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":

    # get URL from passed user arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # post parameter
    param = {'email': email}

    # prepare parameters to send via the POST request
    data = urllib.parse.urlencode(param).encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)
