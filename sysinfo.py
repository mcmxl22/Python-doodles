#! /usr/bin/env python
# By Micah M. 2018
# sysinfo version 1.0
# Python 3.7

import platform
import psutil


def sysinfo():
    sysinfo = platform.uname()
    meminfo = psutil.virtual_memory()
    print(sysinfo)
    print(meminfo)

if __name__ == "__main__":
    sysinfo()
