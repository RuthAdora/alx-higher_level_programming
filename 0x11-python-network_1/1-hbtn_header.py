#!/usr/bin/python3
<<<<<<< HEAD
"""takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
import sys

import urllib.request

=======
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


>>>>>>> f7687c909fa5c8750871e5a26a98a0178817ada3
if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
