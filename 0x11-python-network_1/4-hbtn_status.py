#!/usr/bin/python3
<<<<<<< HEAD
"""
 fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
=======
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
>>>>>>> f7687c909fa5c8750871e5a26a98a0178817ada3
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
