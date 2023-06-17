#std_output.py
#coding:utf-8

import sqlite3
import os
import sys
import time
import tkinter as tk
import urllib
import urllib.request
from pickle import dump, load

from constant import *
from std_output import *

'''
标准输出函数
'''

def log(string):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(string)
        file.close()
        return string


def pout(string):
    # 判断系统类型
    if SYSTEM == 2:
        print(f"[*]\033[0;33m{string}\033[0m")
    else:
        print(f"[*]{string}")

    log(f"[{time.time()}]{string}\n")


def pwarm(string):
    # 判断系统类型
    if SYSTEM == 2:
        print(f"\033[0;31m[!]{string}\033[0m")
    else:
        print(f"[!]{string}")
    log(f"[{time.time()}][!]{string}\n")


def error(string):
    # 判断系统类型
    if SYSTEM == 2:
        print(f"[\033[0;31mERROR\033[0m]{string}")
    else:
        print(f"[ERROR]{string}")

    log(f"[{time.time()}][ERROR]{string}\n")


def pok(string):
    # 判断系统类型
    if SYSTEM == 2:
        print(f"[ \033[0;32mOK\033[0m ] {string}")
    else:
        print(f"[ ok ]{string}")
    log(f"[{time.time()}][ ok ]{string}\n")

