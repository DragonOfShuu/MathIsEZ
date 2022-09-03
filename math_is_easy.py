'''
===========================================

PROGRAM BY MUSHROOMENDER or DRAGON OF SHUU
Made to assist in calculating certain 
math concepts, such as trigonometry
and circles. This program can calculate
symbolic math using the SymPy module.

REQUIREMENTS:
> Python 3.10

OPTIONAL (the system will install it)
> SymPy
> pyperclip
> NumPy

===========================================
'''

from __future__ import annotations

# =============
#  = Modules =
# =============

import sys

if sys.version_info < (3, 10):
    print("Python version is not supported! Only 3.10 and above is supported!")
    sys.exit(1)

# Initalize Package Manager
import package_manager

# Import the rest of the modules
import functools
import colorama

def mainmenu(clas: object):
    @functools.wraps(clas)
    def wrapper(*args, **kwargs):
        value = clas(*args, **kwargs).execute()
        return value;
    return wrapper();

from utils.save_data.save_interpreter import Data
import menus