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
import logging 
import datetime
import time
import os

if __name__ == "__main__":
    if not os.path.exists("logs/"): os.mkdir("logs")
    alllogs = os.listdir("logs/")

    if len(alllogs) >= 5:
        # Oldest file will have a lower number.

        oldest_name = ""
        oldest_time = time.time()
        for i in alllogs:
            comparable = os.path.getmtime(f"logs/{i}")
            if comparable < oldest_time:
                oldest_name = i
                oldest_time = comparable
        os.remove(f"logs/{oldest_name}")

    logger = logging.getLogger("program")
    times = datetime.datetime.today()
    time_now = f"logs/math_is_ez_{times.year}y_{times.month}mo_{times.day}d_{times.hour}h_{times.minute}min_{times.second}s.log"
    logging.basicConfig(format='[%(asctime)s] [%(process)d] [%(levelname)s] - %(message)s', 
                        filename=time_now, 
                        level=20)
    logger.info("Program Started.")

def mainmenu(clas: object):
    @functools.wraps(clas)
    def wrapper(*args, **kwargs):
        value = clas(*args, **kwargs).execute()
        return value;
    return wrapper();

import menus