#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response, handling errors
using the package 'requests'
"""

import sys
import requests

if __name__ == "__main__":

    # get url entered by the user
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)  # print respose body
