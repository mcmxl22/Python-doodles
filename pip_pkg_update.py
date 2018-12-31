#!/usr/bin/env python
"""By Micah M. 2018
   pip_pkg_update version 1
   Python 3.7.2"""


import os


def pkg_update():
    """Update pip packages."""
    options = ['Check for updates?', '1 Yes', '2 Exit']
    for option in options:
        print(option)
    choice = input('> ')
    if choice == '1':
        results = os.system('pip list --outdated')
        if results == 0:
            print('All packages are up to date.')
            pkg_update()
        else:
            print(results)
            update_choice = input('Enter name of package to update. ')
            if update_choice in results:
                update_pkg = os.system(f'''pip install --upgrade
				                          {update_choice}'''
		        print('Done')

    elif choice == '2':
        raise SystemExit


if __name__ == "__main__":
    pkg_update()
