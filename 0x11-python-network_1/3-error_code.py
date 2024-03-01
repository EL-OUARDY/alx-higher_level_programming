#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8), managing errors
using urllib package
"""

import sys
import urllib.request

if __name__ == "__main__":

    # get URL from passed user arguments
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
