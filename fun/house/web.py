#!/usr/bin/env python3
"""
Web version 1.5
Python 3.7
"""

import webbrowser


class Web_site:
    def _init_(self, url:str) -> None:
        self.url = url


    def visit(site_name) -> bool:
        """website"""
        site_name = input("Type site name: ")
        url = f"https://www.{site_name}.com" 
        open_site = webbrowser.open(url)
        return open_site


def main():
    adress = Web_site.visit("site")


if __name__ == "__main__":
    main()
