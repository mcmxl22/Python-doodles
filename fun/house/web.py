#!/usr/bin/env python3
"""
Web version 1.4
Python 3.7
"""

import webbrowser


def web_site(site_name):
    """website"""
    site_name = input('Type site name: ')
    url = f'https://www.{site_name}.com'
    webbrowser.open(url)

if __name__ == "__main__":
    web_site('site_name')
