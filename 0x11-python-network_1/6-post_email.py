#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays
the body of the response, using the package 'requests'
"""

import sys
import requests

if __name__ == "__main__":

    # get arguments entered by the user
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    body = requests.post(url, data).text
    print(body)
