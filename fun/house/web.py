#!/usr/bin/env python3
"""
Web version 1.6
Python 3.7
"""

from webbrowser import open


class Web_site:
    def __init__(self, url):
        self.url = url


    def visit(self):
        """website"""
        site_name = input("Type site name: ")
        url = f"https://www.{site_name}.com"
        open(url)

address = Web_site.visit("site")


if __name__ == "__main__":
    address
