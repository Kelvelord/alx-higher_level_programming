#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""


if __name__ == '__main__':
    import sys
    from urllib.request import urlopen

    url = sys.argv[1]
    with urlopen(url) as response:
        content = dict(response.headers)
        print(content.get("X-Request-Id"))
