#!/usr/bin/python3
"""Response header value #0"""


from sys import argv
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen(argv[1]) as r:
        html = r.info()
        print(html['X-Request-Id'])
