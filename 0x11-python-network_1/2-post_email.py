#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""


if __name__ == '__main__':
    import sys
    import urllib
    from urllib.request import urlopen

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    with urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
