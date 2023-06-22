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
import logging  # 引入logging模块
import os.path
from datetime import datetime

# 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 创建一个handler，用于写入日志文件
rq = datetime.now().strftime("%Y%m%d")[:None] #获取当天的日期，在logs文件夹下每天生成一个日志文件
log_path = os.path.dirname(os.getcwd()) + '/logs/'
log_name = log_path + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, encoding="utf-8", mode='a+') # mode的使用见以下Python文件读写
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
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


def lerror(msg):
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


def error(string):
    # 判断系统类型
    if SYSTEM == 2:
        print(f"[\033[0;31mERROR\033[0m]{string}")
    else:
        print(f"[ERROR]{string}")

    lerror(string)


def pok(string):
    # 判断系统类型
    if SYSTEM == 2:
        print(f"[ \033[0;32mOK\033[0m ] {string}")
    else:
        print(f"[ ok ]{string}")
    info(string)


"""
主程序常量库
"""

# 系统下调用python的命令
PYTHON_COM = "python"

# 系统类型，填1代表WINDOWS，填2为LINUX或UNIX
SYSTEM = 1
if SYSTEM not in {1, 2}:
    # 抛出异常退出程序
    sys.exit(1)
if SYSTEM == 2:
    PYTHON_COM = "python3"

# ZZH LOGO
ZZH = "\
  __________\t  __________\t ___     ___\n\
 /_________/|\t /_________/|\t/__/|   /__/|\n\
 |_______  |^\t |_______  |^\t|  ||   |  ||\n\
       /  / / \t       /  / /\t|  ||___|  ||\n\
     /  / /  \t     /  / /\t|  |/___|  ||\n\
   /  / /___\t   /  / /___\t|  ______  ||\n\
 /  /______/|\t /  /______/|\t|  ||   |  ||\n\
|__________|/\t|__________|/\t|  ||   |  ||\n\
                            \t|__|/   |__|/"

ZZH2 = "\
  __________\t   __________\t  ___     ___\n\
 /_________/|\t /_________/|\t/__/|   /__/|\n\
 |_______  |^\t |_______  |^\t|  ||   |  ||\n\
       /  / / \t      /  / /\t|  ||___|  ||\n\
     /  / /  \t     /  / /\t  |  |/___|  ||\n\
   /  / /___\t    /  / /___\t |  ______  ||\n\
 /  /______/|\t /  /______/|\t|  ||   |  ||\n\
|__________|/\t|__________|/\t|  ||   |  ||\n\
                           \t|__|/   |__|/"

# 默认语言：中文
zh_cn = [
    "正在解析",
    "域名",
    "报歉,该域名下",
    "来自",
    "的资源暂时不支持爬取",
    "提示",
    "输入exit退出,输入url地址开始爬取",
    "检查URL",
    "URL不可用",
    "URL检查完毕",
    "启动网络爬虫",
    "要爬取的URL地址",
    "程序非正常退出,可能是崩溃了",
    '请向ZZH20081023@163.com发送标题为"BugReport"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您的反馈!',
    "没有叫做",
    "的模式",
]

# 伪装成浏览器(此处伪装成chrome)
HEADERS = (
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
)

# 日志文件名
LOG_FILE = "../log"

# 脚本保护
file = open("./configs/protect.conf", "r")
PROTECT = file.readline()
if not (PROTECT in {"0", "1"}):
    print(f"CONFIG ERROR:./config/protect.conf can't be {PROTECT}")
    sys.exit(1)
file.close()
