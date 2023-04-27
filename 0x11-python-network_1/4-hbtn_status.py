#!/usr/bin/python3
"""A script that
- fetches https://intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    content = requests.get(url)
    print("Body response:")
    print("\t - type: {}".format(type(content.text)))
    print("\t - content: {}".format(content.text))
