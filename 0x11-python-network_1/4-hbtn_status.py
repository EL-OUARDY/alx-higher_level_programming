#!/usr/bin/python3
"""
This script  fetches a URL, using the package 'requests'
"""

import requests

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"
    body = requests.get(url).text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
