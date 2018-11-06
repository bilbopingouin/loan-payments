import os
import sys
import argparse

from distutils.core import setup
import py2exe


#--------------------------------

def generate_exe():
    global target_script

    py2exe_options =    {
                            'bundle_files':1,
                            'compressed': True,
                            'optimize': 2,
                            'dll_excludes': ['w9xpopen.exe']
                        }

    list_includes = {
                    }

    setup(      
              console = [{'script': 'calculate_debt.py', }],
              options = {'py2exe': py2exe_options},
              zipfile = None,                
          )

#--------------------------------

def main(argv):
    if not "py2exe" in argv:
        sys.argv.append("py2exe")

    generate_exe()

    return 0

#--------------------------------

if __name__ == "__main__":
    sys.exit(main(sys.argv))
