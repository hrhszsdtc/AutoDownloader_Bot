# Copyright (C) 2023 hrhszsdtc

import os
import random
import sys

import utils
"""
主程序常量库
"""
os.chdir("src")
try:
    PYTHON_COM = sys.executable
except AttributeError as e:
    utils.perror(f"{e}:Python3 is not installed.")
    sys.exit(-1)

# UserAgent
with open("config/user_agents.txt", "r") as f:
    HEADERS = f.readlines()
    HEADER = random.choice(HEADERS)

# 日志文件名
LOG_FILE = "../log"
