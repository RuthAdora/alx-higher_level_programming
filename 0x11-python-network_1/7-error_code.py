#!/usr/bin/python3
<<<<<<< HEAD
""" script that takes in a URL, sends a request to
 the URL and displays the body of the response."""
import sys

import requests

if __name__ == "__main__":
    url = sys.argv[1]
=======
"""Sends a request to a given URL and displays the response body.
Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

>>>>>>> f7687c909fa5c8750871e5a26a98a0178817ada3
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
