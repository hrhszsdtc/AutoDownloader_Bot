import sys

import sqlite3
import os
import sys
import time
import tkinter as tk
import urllib
import urllib.request
from pickle import dump, load
import logging  # 引入logging模块
import os.path
from datetime import datetime

import logging  # 引入logging模块
import os.path
from datetime import datetime

# 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 创建一个handler，用于写入日志文件
rq = datetime.now().strftime("%Y%m%d")[:None]  # 获取当天的日期，在logs文件夹下每天生成一个日志文件
log_path = os.path.dirname(os.getcwd()) + "/logs/"
log_name = log_path + rq + ".log"
logfile = log_name
log_path = os.path.dirname(os.getcwd()) + "/logs/"
if not os.path.exists(log_path):
    os.makedirs(log_path)
fh = logging.FileHandler(logfile, encoding="utf-8", mode="a+")  # mode的使用见以下Python文件读写
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 定义handler的输出格式
formatter = logging.Formatter(
    "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
)
fh.setFormatter(formatter)

# 将logger添加到handler里面
logger.addHandler(fh)


# 日志
def info(msg):
    logger.info(msg)


def debug(msg):
    logger.debug(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def critical(msg):
    logger.critical(msg)


def pout(string):
    # 判断系统类型
    if SYSTEM == 2:
        print(f"[*]\033[0;33m{string}\033[0m")
    else:
        print(f"[*]{string}")

    info(string)


def pwarm(string):
    # 判断系统类型
    if SYSTEM == 2:
        print(f"\033[0;31m[!]{string}\033[0m")
    else:
        print(f"[!]{string}")
    warning(string)


def perror(string):
    # 判断系统类型
    if SYSTEM == 2:
        print(f"[\033[0;31mERROR\033[0m]{string}")
    else:
        print(f"[ERROR]{string}")

    error(string)


def pok(string):
    # 判断系统类型
    if SYSTEM == 2:
        print(f"[ \033[0;32mOK\033[0m ] {string}")
    else:
        print(f"[ ok ]{string}")
    info(string)