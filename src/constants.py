# Copyright (C) 2023 hrhszsdtc

import os
import random
import sys

import utils

# 域名映射字典
DN = {
    "bilibili": ("bilibili.com", "www.bilibili.com", "b23.tv"),
    "iqiyi": ("www.iqiyi.com", "iqiyi.com"),
}
DOMAIN_NAME = {x: k for k, v in DN.items() for x in v}

# 版权信息
copyright_notice = "Copyright (C) 2023 hrhszsdtc"

# 反馈事项
feedback_notice = "请联系hrhszdtc团队(https://github.com/hrhszsdtc)并发送反馈报告,报告应包含:\n1. 使用的程序和运行环境\n2. 系统版本\n3. 报错信息\n4. 报错前的操作\n5. 其他可能的信息\n感谢您的反馈!"

script_path = os.path.abspath(__file__)
script_folder = os.path.dirname(script_path)
os.chdir(script_folder)

try:
    PYTHON_COM = sys.executable
except AttributeError as e:
    utils.perror(f"{e}:Python3 is not installed.")
    sys.exit(-1)

# UserAgent
with open("config/user_agents.txt", "r", encoding='utf-8') as f:
    HEADERS = f.readlines()
    HEADER = random.choice(HEADERS)

# 日志文件名
LOG_FILE = "../log"
