#!/usr/bin/python3
<<<<<<< HEAD
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import sys
from urllib import request, error
=======
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request

>>>>>>> f7687c909fa5c8750871e5a26a98a0178817ada3

if __name__ == "__main__":
    url = sys.argv[1]

<<<<<<< HEAD
    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
=======
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
>>>>>>> f7687c909fa5c8750871e5a26a98a0178817ada3
        print("Error code: {}".format(e.code))
