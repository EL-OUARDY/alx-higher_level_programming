#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to /search_user endpoint
with the letter as a parameter
using the package 'requests'
"""

import sys
import requests

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"

    # get search letter entered by the user
    search_letter = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {"q": search_letter}
    response = requests.post(url, data)
    try:
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError as e:
        print("Not a valid JSON")
