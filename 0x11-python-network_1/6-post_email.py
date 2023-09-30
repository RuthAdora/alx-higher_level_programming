#!/usr/bin/python3
<<<<<<< HEAD
"""script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays
the body of the response.
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
=======
"""Sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
>>>>>>> f7687c909fa5c8750871e5a26a98a0178817ada3
    print(r.text)
