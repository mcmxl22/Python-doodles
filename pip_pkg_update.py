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
        print('Checking for updates.')
        results = os.system('pip list --outdated')
        if results == 0:
            print('All packages are up to date.\n')
            pkg_update()
        else:
            print(results)
            while True:
                update_list = list(results)
                current = update_list.pop(0)
                print(f'Updating {current}.')
                os.system(f'''pip install --upgrade
		             {current}''')
                print('Done')
            pkg_update()

    elif choice == '2':
        raise SystemExit

    else:
        pkg_update()


if __name__ == "__main__":
    pkg_update()
